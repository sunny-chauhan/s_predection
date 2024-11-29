from flask import Flask, request, render_template, jsonify
import cv2
import os
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    image_file = request.files.get('imageFile')
    video_file = request.files.get('videoFile')

    if image_file and video_file:
        return "Error: Please upload only one file at a time!"

    if image_file:
        file_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(file_path)
        soil_type = process_image(file_path)
        return jsonify({"message": f"Image processed successfully--> Detected soil type : {soil_type}"})

    if video_file:
        file_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
        video_file.save(file_path)
        soil_type = process_video(file_path)
        return jsonify({"message": f"Video processed successfully--> Detected soil type : {soil_type}"})

    return "Error: No file uploaded!"

def process_image(file_path):
    # Example image processing logic
    image = cv2.imread(file_path)
    # Dummy logic for soil classification
    average_pixel_value = np.mean(image)
    if average_pixel_value > 128:
        return "Sandy Soil"
    else:
        return "Clay Soil"

def process_video(file_path):
    # Example video processing logic
    cap = cv2.VideoCapture(file_path)
    frame_count = 0
    average_pixel_value = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        average_pixel_value += np.mean(frame)
        frame_count += 1

    cap.release()
    average_pixel_value /= frame_count
    if average_pixel_value > 128:
        return "Loamy Soil"
    else:
        return "Silt Soil"

if __name__ == '__main__':
    app.run(debug=True)
