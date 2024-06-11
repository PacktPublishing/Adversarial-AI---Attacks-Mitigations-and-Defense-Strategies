# app.py for Flask web application
from flask import Flask, render_template, request, redirect, url_for,  send_from_directory
import logging
import requests
import os

FLASK_API_URL = os.environ.get('FLASK_API_URL', 'http://localhost:5000')
UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    image_url =  None
    if request.method == 'POST':
        # Get the image from the form and send it to the Flask API
        image = request.files.get('image')
        image_size = image.content_length
        logger.info(f'Received prediction request for an image of: {image_size} bytes')
        if image:
            image.save(os.path.join(UPLOAD_FOLDER, image.filename))
            image.seek(0)
            image_url = url_for('uploaded_file', filename=image.filename)
            response = requests.post(f"{FLASK_API_URL}/predict", files={'file': image})
            logger.info(f'Received prediction response: { response.json()}')
            if response.status_code == 200:
                prediction_data = response.json().get('prediction')
                if prediction_data:
                    prediction = prediction_data.get('class_name')
    return render_template('index.html', prediction=prediction,image_url=image_url )

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    work_dir = os.getcwd();
    print(work_dir)
    app.run(host='0.0.0.0', port=8000)
