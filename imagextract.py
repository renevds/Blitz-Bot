import time

import cv2
import mss
import numpy
import pytesseract

replacelist = ["\n", "\f"]

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def readtext():
    alltext = ""
    for x in range(4):
        for y in range(4):
            with mss.mss() as sct:
                im = sct.grab({'top': 635 + 150*x, 'left':305 + 150*y, 'width': 65, 'height': 90})


                mss.tools.to_png(im.rgb, im.size, output="img(" + str(x) + "," + str(y) + ").png")
                im = numpy.asarray(im)
                im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                cv2.imwrite("grey_img(" + str(x) + "," + str(y) + ").png", im)

                text = pytesseract.image_to_string(im, config='--psm 10') #10 for single column
                for i in replacelist:
                    text = text.replace(i,"")
                alltext += text[0]

    alltext = alltext.replace("|", "i")
    alltext = alltext.lower()
    print(alltext)
    return alltext

if __name__ == '__main__':
    print(readtext())