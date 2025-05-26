
# SecureHashVerify

> 基于 Python、Flask、RSA 和 SHA-256 的文件完整性验证系统。

SecureHashVerify 是一个轻量级 Web 应用，能够使用 **RSA 数字签名** 与 **SHA-256 哈希算法**，帮助用户验证文件是否被篡改或损坏，保护文件传输与分发安全。

---

## 功能特性

- 生成公钥与私钥（PEM 格式）
- 使用 SHA-256 哈希算法计算文件摘要
- 使用 RSA 私钥对摘要签名
- 使用 RSA 公钥验证签名是否有效
- 基于 Flask 的 Web 界面，支持文件上传与结果展示

---

## 安装与运行

### 克隆项目

```bash
git clone https://github.com/Z2cc666/CryptoFileCheck.git
cd CryptoFileCheck
````

### 创建虚拟环境并安装依赖

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate.bat  # Windows

pip install -r requirements.txt
```

### 启动 Flask 应用

```bash
python App.py
```

打开浏览器访问 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 项目结构

```
SecureHashVerify/
│
├── templates/              # HTML模板（Flask使用）
│   └── index.html
│
├── keys/                   # 自动生成的RSA密钥
│   ├── private_key.pem
│   └── public_key.pem
│
├── uploads/                # 临时存储用户上传文件
│
├── main.py                 # 核心加密逻辑：哈希、签名、验证
├── App.py                  # Flask入口文件
├── requirements.txt        # 项目依赖
└── README.md               # 项目说明
```

---

## 依赖

* Flask
* cryptography

安装命令：

```bash
pip install flask cryptography
```

---

## 未来改进

* 美化 UI 界面（可用 Bootstrap 或其他前端框架）
* 增加批量文件签名与验证功能
* 支持签名文件下载
* 使用数据库保存验证记录

---

## 许可协议

MIT License

---

## 作者信息

* 作者：Chelwa
* 联系邮箱：2747325606@qq.com


