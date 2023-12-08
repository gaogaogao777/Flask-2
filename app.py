from flask import Flask, render_template
from flask import Flask, render_template, url_for, request, jsonify
app = Flask(__name__)

# Replace these with your actual name and student ID
your_name = "Your Name"
student_id_last_5_digits = "12345"

@app.route('/')
def index():
    # You can add your picture filename or URL here
    # picture_filename = "static/baidi.jpg"  # Replace with the actual file name
    picture_filename = url_for('static', filename='baidi.jpg')
    return render_template('index.html', name=your_name, id_last_5_digits=student_id_last_5_digits)

if __name__ == '__main__':
    app.run()
