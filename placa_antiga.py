import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('img/abc.jpg',cv2.IMREAD_GRAYSCALE)
imagem = cv2.resize(imagem,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
th,thresh1 = cv2.threshold(imagem,155,205,cv2.THRESH_BINARY) 

placa_lida = pytesseract.image_to_string(thresh1)
print(placa_lida)
plt.imshow(thresh1)
plt.show()