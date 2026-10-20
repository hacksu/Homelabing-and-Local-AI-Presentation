from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')


if __name__ == '__main__':
    print("Starting homelab and local AI presentation at http://0.0.0.0:5174")
    app.run(debug=True, host='0.0.0.0', port=5174)
