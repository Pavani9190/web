from flask import Flask, request, jsonify
import cv2
import mediapipe as mp
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir requisições de qualquer origem

# Configuração do MediaPipe
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

@app.route('/recognize', methods=['POST'])
def recognize():
    file = request.data  # Receber dados binários diretamente
    np_array = np.frombuffer(file, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Conversão para RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detecção de rosto
    results = face_detection.process(rgb_image)
    
    face_locations = []
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            face_locations.append(bbox)
    
    return jsonify({'face_locations': face_locations})

if __name__ == '__main__':
    app.run(debug=True, port=5500)
