import cv2
import numpy as np

# # Cargar una imagen y mostrarla en una ventana
# width = 320
# height = 240
# imagen = cv2.imread("C:\\Users\\vagoa\\Downloads\\diamond_painting_map (7).png")
# imagen2 = cv2.imread("C:\\Users\\vagoa\\Downloads\\color_legend (8).png")

# # Redimensiona las imágenes antes de mostrarlas
# imagen_resized = cv2.resize(imagen, (width, height))
# imagen2_resized = cv2.resize(imagen2, (width*2, height*2))
# imagen_revert = cv2.flip(imagen_resized, -1)

# cv2.imshow("Imagen", imagen_revert)
# cv2.moveWindow("Imagen", 100, 100)
# cv2.imshow("Imagen 2", imagen2_resized)
# cv2.moveWindow("Imagen 2", 800, 100)

# cv2.waitKey(0)
# cv2.destroyAllWindows() 

#Reproducir un video y mostrarlo en una ventana
cap = cv2.VideoCapture("C:\\Users\\vagoa\\Downloads\\video.mp4")
while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
glasses_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # Región de interés para buscar lentes solo dentro de la cara
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Detecta lentes dentro de la cara
        glasses = glasses_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)
        for (ex, ey, ew, eh) in glasses:
            # Dibuja un rectángulo verde alrededor de los lentes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)



    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()


#Ejercicios:
# 1. Elaborar un programa en el cual aparezcan dos
#    imagenes que tengan diferentes dimensiones.
# 2. Elaborar un programa en el cual muestres la primera
#   imagen y que la segunda sea invertido tanto horizontal como 
#   verticalmente