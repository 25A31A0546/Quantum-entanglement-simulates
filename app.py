from flask import Flask, send_from_directory, jsonify
from main import simulate

app = Flask(__name__)

@app.route('/')
def index():
        return send_from_directory('.', 'frontend.html')

@app.route('/simulate')
def run_simulation():
    data = simulate()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)