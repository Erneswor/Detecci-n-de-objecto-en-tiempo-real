import cv2
import time
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import ObjectDetector
from mediapipe.tasks.python import BaseOptions

# Este programa detecta objetos en tiempo real utilizando un modelo EfficientDet Lite.
# puede detectar personas, portátiles, sillas, taza y otros objetos.

# Configuración del modelo
MODEL_PATH = 'efficientdet_lite0.tflite'  # Ruta al modelo
base_options = BaseOptions(model_asset_path=MODEL_PATH)

# Configuración del detector de objetos
def detection_callback(result, output_image, timestamp):
    global detection_result_list
    detection_result_list.append(result)

detection_result_list = []

options = vision.ObjectDetectorOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.LIVE_STREAM,  # Modo de transmisión en vivo
    max_results=5, 
    score_threshold=0.5,  # Filtro de confianza mínima recomendado 0.5
    category_allowlist=["person", "laptop", "chair"],  # Detectar solo personas, laptos y sillas
    result_callback=detection_callback  
)

# Inicializar detector
detector = ObjectDetector.create_from_options(options)

# Leer el video de entrada
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir frame a formato MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # Detectar objetos sobre el frame
    detector.detect_async(mp_image, time.time_ns() // 1_000_000)

    # Dibujar resultados si hay detecciones
    if detection_result_list:
        for detection in detection_result_list[0].detections:
            bbox = detection.bounding_box
            bbox_x, bbox_y, bbox_w, bbox_h = bbox.origin_x, bbox.origin_y, bbox.width, bbox.height
            category = detection.categories[0]
            score = category.score * 100
            category_name = category.category_name

            # Dibujar el cuadro delimitador y la etiqueta
            cv2.rectangle(frame, (bbox_x, bbox_y), (bbox_x + bbox_w, bbox_y + bbox_h), (100, 255, 0), 2)
            cv2.rectangle(frame, (bbox_x, bbox_y - 30), (bbox_x + bbox_w, bbox_y), (100, 255, 0), -1)
            cv2.putText(frame, f"{category_name} {score:.2f}%", (bbox_x + 5, bbox_y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255, 255, 255), 2)

        detection_result_list.clear()

    # Mostrar el frame procesado
    cv2.imshow('Video', frame)

    # Salir si se presiona la tecla 'ESC'
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
detector.close()  # Liberar recursos