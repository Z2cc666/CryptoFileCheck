
# SecureHashVerify
<img width="720" alt="截屏2025-05-27 晚上7 55 19" src="https://github.com/user-attachments/assets/46b88b1f-6680-42d7-aa30-234599b66687" />


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
##界面功能演示
<img width="720" alt="截屏2025-05-27 晚上7 55 19" src="https://github.com/user-attachments/assets/ccb27fa5-e1c3-4191-a6e5-77b36535618a" />
<img width="726" alt="截屏2025-05-27 晚上7 55 30" src="https://github.com/user-attachments/assets/70698127-ca7c-4601-8b40-6a6983525be2" />
<img width="733" alt="截屏2025-05-27 晚上8 12 38" src="https://github.com/user-attachments/assets/0bba2f52-1f4a-4933-a81d-4d62c1b33c64" />
<img width="739" alt="截屏2025-05-27 晚上8 12 50" src="https://github.com/user-attachments/assets/4c15b16a-8599-4ba2-a823-275c1bdc087b" />
<img width="731" alt="截屏2025-05-27 晚上8 12 56" src="https://github.com/user-attachments/assets/6c9976ce-561b-4c1a-b5bf-8290ead6305a" />
<img width="736" alt="截屏2025-05-27 晚上8 13 04" src="https://github.com/user-attachments<img width="633" alt="截屏2025-05-27 晚上8 13 10" src="https://github.com/user-attachments/assets/d708517a-3f96-4d88-9803-5c7c082c469e" />
/assets/23b3a9ba-cb27-40a5-b5cf-ecbb26150d00" />
<img width="641" alt="截屏2025-05-27 晚上8 13 16" src="https://github.com/user-attachments/assets/e40ff3d4-ecd1-45b6-a65d-21237c47faab" />

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


