from flask import Flask, render_template
import subprocess
import signal

app = Flask(__name__)

camera_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_detection')
def run_detection():
    global camera_process
    if camera_process is None:
        camera_process = subprocess.Popen(["python", "detect.py", "--weights", "best.pt", "--img", "416", "--conf", "0.5", "--source", "0"])
        return render_template('detection.html')
    else:
        return 'Detection already running'

@app.route('/stop_camera')
def stop_camera():
    global camera_process
    if camera_process:
        camera_process.terminate()
        camera_process.wait()
        camera_process = None
        return render_template('index.html')
    else:
        return 'Camera is not running'



@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
