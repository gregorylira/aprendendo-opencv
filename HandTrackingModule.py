import cv2


img = cv2.imread('./imagem_teste.jpg')


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)