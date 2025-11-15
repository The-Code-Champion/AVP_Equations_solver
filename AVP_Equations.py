from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    path = os.path.join(os.path.dirname(__file__), 'Main_Page.html')
    if not os.path.exists(path):
        return "<p>Main_Page.html not found in project folder.</p>", 500
    return send_file(path)

if __name__ == '__main__':
    # run the server so the Main_Page buttons reach routes (create routes/pages later)
    app.run(debug=True, host='127.0.0.1', port=5000)