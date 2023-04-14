from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "hello world from docker and nginx"})


app.run(debug=True, host="0.0.0.0", port=5000)
