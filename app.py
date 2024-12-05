from flask import Flask, render_template, request, jsonify, send_from_directory

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
import tensorflow_text as text
import re


DATASET_FILE_PATH = "uploads/dataset.csv"
MODEL_FILE_PATH = "model.pkl"
model = tf.saved_model.load("models/translator_id-en")

def translate_en(en_text):
    output = model(tf.constant(en_text)).numpy()
    output = output.decode("utf-8")
    output = re.sub(r"\s*([^\s\w\d])\s*", r"\1", output)
    return output

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/index")
def root():
    return render_template("pages/test.html")

# route test post that recive json  formData from the frontend, print it and return it
@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    print(data["content"])
    translated = translate_en(data["content"])
    return jsonify(translated)

# route config
@app.route("/public/<path:subdir>/<path:filename>")
def serve_static(subdir, filename):
    # Define the base directory for static files
    base_dir = "public"

    # Construct the full directory path
    directory = f"{base_dir}/{subdir}"

    # Serve the file from the specified directory
    return send_from_directory(directory, filename)


if __name__ == "__main__":
    app.run(debug=True)
