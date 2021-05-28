#-------------------------------------------------------------------------------------------------
#--------------------------------------------IMAGE STREAMING--------------------------------------------------
#-------------------------------------------------------------------------------------------------
import requests
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session, Response
import jinja2
import pandas as pd
import cv2

image_streaming = Blueprint('image_streaming', __name__, template_folder='templates', static_folder='static', url_prefix='/image_streaming')

app = Flask(__name__)

camera = cv2.VideoCapture(0)

#--------------------------------------------UI--------------------------------------------------
@image_streaming.route('/ui')
def image_streaming_ui():
    return render_template('image_streaming.html')

#--------------------------------------------API--------------------------------------------------
@image_streaming.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


if __name__ == '__main__':
    app.run()

