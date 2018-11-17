import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('img/placa_nova.png',cv2.IMREAD_GRAYSCALE)
imagem = cv2.resize(imagem,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
th,thresh1 = cv2.threshold(imagem,190,200,cv2.THRESH_BINARY)

placa_lida = pytesseract.image_to_string(thresh1)
placa_lida = placa_lida.replace("\n", " ")
placa_lida = placa_lida.replace("  "," ")
print(placa_lida)

plt.imshow(thresh1)
plt.show()

placas_permitidas = ('BRASIL AB 123 CD','BRASIL BD 456 XZ','CHILE DD 789 TR')
if placa_lida in placas_permitidas:
  print('Placa autorizada!')
else:
  print('{} não encontrada! Acesso negado!'.format(placa_lida))