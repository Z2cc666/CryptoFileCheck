import os
from flask import Flask, render_template, request, redirect, url_for, flash
from main import generate_keys, calculate_sha256, sign_hash, verify_signature

app = Flask(__name__)
app.secret_key = "replace_with_your_secret_key"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

generate_keys()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        flash("未选择文件")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash("未选择文件")
        return redirect(request.url)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    file_hash = calculate_sha256(filepath)
    signature = sign_hash(file_hash)

    sig_path = filepath + ".sig"
    with open(sig_path, "wb") as f:
        f.write(signature)

    flash(f"文件已上传并签名。签名文件保存为：{sig_path}")
    return redirect(url_for('index'))

@app.route("/verify", methods=["POST"])
def verify():
    if 'file' not in request.files or 'signature' not in request.files:
        flash("请上传文件和对应的签名文件")
        return redirect(url_for('index'))

    file = request.files['file']
    signature_file = request.files['signature']

    if file.filename == '' or signature_file.filename == '':
        flash("请确保文件和签名文件都已选择")
        return redirect(url_for('index'))

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    sig_path = os.path.join(app.config['UPLOAD_FOLDER'], signature_file.filename)

    file.save(file_path)
    signature_file.save(sig_path)

    file_hash = calculate_sha256(file_path)

    with open(sig_path, "rb") as f:
        signature = f.read()

    valid = verify_signature(file_hash, signature)
    if valid:
        flash("签名验证成功 ✅ 文件未被篡改")
    else:
        flash("签名验证失败 ❌ 文件可能被篡改")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
