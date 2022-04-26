import numpy as np
import cv2
import random as rng

def main():
    img = cv2.imread('placas.jpg')
    
#CONVERSÃO DA IMAGEM
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#REMOVENDO RUIDOS
    frame_blur = cv2.GaussianBlur(hsv.copy(), (5, 5), 3)
    frame_blur = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#SEPARANDO O VERMELHO 
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([50, 255, 255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask0 + mask1

#TRANSFORMANDO IMAGEM EM BINÁRIA
    img_bin = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

#PROCURANDO O CONTORNO
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#DESENHANDO O CONTORNO
    drawing = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)

    for i in range(len(contours)):
        cv2.drawContours(drawing, contours, i, (0, 256), 1)

#DISPLAY 
    
    cv2.imshow('Imagem original', img )
    cv2.imshow('Tons de vermelho', mask)
    cv2.imshow('Contours', drawing)
    print(img_bin)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    cv2.saveScreenshot (out, 1)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
