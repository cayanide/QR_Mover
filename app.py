import os
import qrcode
import base64
from flask import Flask, render_template, request, send_file, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

Bootstrap(app)

def generate_qr_code(file_url):
    """Generate a QR code and return its base64 representation."""
    qr = qrcode.QRCode(box_size=10, border=5)
    qr.add_data(file_url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return img_base64

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    file_name = None

    if request.method == "POST":
        if "file" in request.files:
            uploaded_file = request.files["file"]
            if uploaded_file.filename != "":
                file_name = secure_filename(uploaded_file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)
                uploaded_file.save(file_path)

                # Generate a QR code pointing to the download link
                file_url = url_for("download_file", file_name=file_name, _external=True)
                qr_code = generate_qr_code(file_url)

    return render_template("index.html", qr_code=qr_code, file_name=file_name)

@app.route("/download/<file_name>")
def download_file(file_name):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678, debug=True)
