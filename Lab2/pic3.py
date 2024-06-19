import cv2
import numpy as np

def help():
    print("2018-07-12")
    print("DeBlur_v8")
    print("You will learn how to recover an out-of-focus image by Wiener filter")

def calcPSF(outputImg, filterSize, R):
    h = np.zeros(filterSize, dtype=np.float32)
    point = (filterSize[0] // 2, filterSize[1] // 2)
    cv2.circle(h, point, R, 255, -1, 8)
    summa = np.sum(h)
    outputImg[:] = h / summa

def fftshift(inputImg, outputImg):
    outputImg = inputImg.copy()
    cx = outputImg.shape[1] // 2
    cy = outputImg.shape[0] // 2
    q0 = outputImg[:cy, :cx]
    q1 = outputImg[:cy, cx:]
    q2 = outputImg[cy:, :cx]
    q3 = outputImg[cy:, cx:]
    tmp = q0.copy()
    q0[:] = q3
    q3[:] = tmp
    tmp = q1.copy()
    q1[:] = q2
    q2[:] = tmp

def filter2DFreq(inputImg, outputImg, H):
    planes = [inputImg.copy(), np.zeros_like(inputImg, dtype=np.float32)]
    complexI = cv2.merge(planes)
    cv2.dft(complexI, complexI, cv2.DFT_SCALE)

    planesH = [H.copy(), np.zeros_like(H, dtype=np.float32)]
    complexH = cv2.merge(planesH)
    complexIH = cv2.mulSpectrums(complexI, complexH, 0)

    cv2.idft(complexIH, complexIH)
    planes = cv2.split(complexIH)
    outputImg[:] = planes[0]

def calcWnrFilter(input_h_PSF, output_G, nsr):
    h_PSF_shifted = np.zeros_like(input_h_PSF, dtype=np.float32)
    fftshift(input_h_PSF, h_PSF_shifted)
    planes = [h_PSF_shifted.copy(), np.zeros_like(h_PSF_shifted, dtype=np.float32)]
    complexI = cv2.merge(planes)
    cv2.dft(complexI, complexI)
    planes = cv2.split(complexI)
    denom = np.power(np.abs(planes[0]), 2) + nsr
    output_G[:] = planes[0] / denom

if __name__ == "__main__":
    help()

    parser = cv2.CommandLineParser()
    parser.addParam("help", "h", cv2.CommandLineParser.TYPE_BOOL, required=False, help="print this message")
    parser.addParam("image", "", cv2.CommandLineParser.TYPE_STRING, required=False, default="original.jpg", help="input image name")
    parser.addParam("R", "", cv2.CommandLineParser.TYPE_INT, required=False, default=5, help="radius")
    parser.addParam("SNR", "", cv2.CommandLineParser.TYPE_INT, required=False, default=100, help="signal to noise ratio")

    params = parser.parse(cv2.utils.commandLineParser_ParamType_ALL)
    if params["help"]:
        parser.printMessage()
        exit(0)

    R = params["R"]
    snr = params["SNR"]
    strInFileName = params["image"]
    cv2.samples.addSamplesDataSearchSubDirectory("doc/tutorials/imgproc/out_of_focus_deblur_filter/images")

    imgIn = cv2.imread(cv2.samples.findFile(strInFileName), cv2.IMREAD_GRAYSCALE)
    if imgIn is None:
        print("ERROR : Image cannot be loaded..!!")
        exit(-1)

    imgOut = np.zeros_like(imgIn, dtype=np.float32)

    # it needs to process even image only
    roi = (0, 0, imgIn.shape[1] & -2, imgIn.shape[0] & -2)

    # Hw calculation (start)
    Hw = np.zeros_like(imgIn, dtype=np.float32)
    h = np.zeros((roi[2], roi[3]), dtype=np.float32)
    calcPSF(h, (roi[2], roi[3]), R)
    calcWnrFilter(h, Hw, 1.0 / float(snr))
    # Hw calculation (stop)

    # filtering (start)
    filter2DFreq(imgIn[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]], imgOut, Hw)
    # filtering (stop)

    imgOut = cv2.convertScaleAbs(imgOut)
    imgOut = cv2.normalize(imgOut, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imshow("Original", imgIn)
    cv2.imshow("Debluring", imgOut)
    cv2.imwrite("result.jpg", imgOut)
    cv2.waitKey(0)

