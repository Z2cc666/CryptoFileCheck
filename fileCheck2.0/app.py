import os
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from main import generate_keys, calculate_sha256, sign_hash, verify_signature

app = Flask(__name__)
app.secret_key = "replace_with_your_secret_key"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 生成密钥对
generate_keys()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({"success": False, "message": "未选择文件"})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"success": False, "message": "未选择文件"})

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # 计算文件哈希并签名
        file_hash = calculate_sha256(filepath)
        signature = sign_hash(file_hash)

        # 保存签名文件
        sig_path = filepath + ".sig"
        with open(sig_path, "wb") as f:
            f.write(signature)

        # 计算文件信息用于显示
        file_size = os.path.getsize(filepath)
        hash_hex = file_hash.hex()

        return jsonify({
            "success": True, 
            "message": "文件签名生成成功！",
            "filename": file.filename,
            "filesize": file_size,
            "hash": hash_hex,
            "signature_file": f"{file.filename}.sig"
        })
    
    except Exception as e:
        return jsonify({"success": False, "message": f"签名生成失败: {str(e)}"})

@app.route("/verify", methods=["POST"])
def verify():
    try:
        if 'file' not in request.files or 'signature' not in request.files:
            return jsonify({"success": False, "message": "请上传文件和对应的签名文件"})

        file = request.files['file']
        signature_file = request.files['signature']

        if file.filename == '' or signature_file.filename == '':
            return jsonify({"success": False, "message": "请确保文件和签名文件都已选择"})

        # 保存上传的文件
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        sig_path = os.path.join(app.config['UPLOAD_FOLDER'], signature_file.filename)

        file.save(file_path)
        signature_file.save(sig_path)

        # 计算文件哈希
        file_hash = calculate_sha256(file_path)

        # 读取签名
        with open(sig_path, "rb") as f:
            signature = f.read()

        # 验证签名
        valid = verify_signature(file_hash, signature)
        
        # 获取文件信息
        file_size = os.path.getsize(file_path)
        hash_hex = file_hash.hex()

        if valid:
            return jsonify({
                "success": True,
                "message": "签名验证成功！文件未被篡改",
                "verified": True,
                "filename": file.filename,
                "filesize": file_size,
                "hash": hash_hex
            })
        else:
            return jsonify({
                "success": True,
                "message": "签名验证失败！文件可能被篡改",
                "verified": False,
                "filename": file.filename,
                "filesize": file_size,
                "hash": hash_hex
            })

    except Exception as e:
        return jsonify({"success": False, "message": f"验证失败: {str(e)}"})

@app.route("/download/<filename>")
def download_signature(filename):
    """下载签名文件"""
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True, port=5006)