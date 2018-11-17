import numpy as np
import matplotlib.pyplot as plt
import cv2

fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
imagem = cv2.imread('img/abc.jpg')
ax1.set_title('Placa Antiga')
ax1.imshow(imagem)

ax2 = fig.add_subplot(2,2,2)
imagem = cv2.imread('img/abc.jpg',cv2.IMREAD_GRAYSCALE)
imagem = cv2.resize(imagem,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
th,thresh1 = cv2.threshold(imagem,155,205,cv2.THRESH_BINARY)
ax2.set_title('Placa Antiga (Com tratamento)')
ax2.imshow(thresh1)

ax3 = fig.add_subplot(2,2,3)
imagem = cv2.imread('img/placa_nova.png')
ax3.set_title('Placa Nova')
ax3.imshow(imagem)

ax4 = fig.add_subplot(2,2,4)
imagem = cv2.imread('img/placa_nova.png',cv2.IMREAD_GRAYSCALE)
imagem = cv2.resize(imagem,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)
th,thresh1 = cv2.threshold(imagem,190,200,cv2.THRESH_BINARY)
ax4.set_title('Placa Antiga (Com tratamento)')
ax4.imshow(thresh1)

plt.show()