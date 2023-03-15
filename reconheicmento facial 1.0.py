import cv2

# Carrega o classificador Haar Cascade para detecção de face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Lê o quadro da webcam
    ret, frame = cap.read()

    # Converte o quadro em escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta as faces no quadro
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenha um retângulo ao redor de cada face detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostra o quadro resultante na tela
    cv2.imshow('Reconhecimento Facial', frame)

    # Espera por uma tecla pressionada e verifica se é a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha a janela
cap.release()
cv2.destroyAllWindows()
