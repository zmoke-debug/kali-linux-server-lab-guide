# Kali Linux Service Lab

一个可以直接复现实验的 Kali Linux 服务实践项目，内容来自四个主题：

1. FTP 文件服务：`vsftpd`、用户权限、被动模式和连接测试
2. Web 服务：Tomcat 与 Flask 的部署、运行和对比
3. 邮件服务：Postfix + Dovecot 的本地收发邮件实验
4. Linux 命令与 Shell：JSON 数据解析、CSV 生成和 FTP 自动传输

项目将原始实验报告整理成了可阅读的教程、配置模板和可执行示例。所有服务都默认面向虚拟机内的本地实验，不建议直接暴露到公网。

## 项目结构

```text
.
├── docs/
│   ├── 01-ftp-service.md
│   ├── 02-web-service.md
│   ├── 03-mail-service.md
│   └── 04-shell-data-pipeline.md
├── examples/
│   └── hotel_db.sample.json
├── scripts/
│   ├── parse_hotel.py
│   └── ftp_upload.sh
├── web/
│   └── flask_app/
│       ├── app.py
│       └── requirements.txt
├── config/
│   └── ftp.env.example
└── README.md
```

## 快速开始

建议使用一台 Kali Linux 虚拟机，并先安装基础工具：

```bash
sudo apt update
sudo apt install -y git curl lftp jq python3 python3-venv
```

按以下顺序学习：

```text
docs/01-ftp-service.md
docs/02-web-service.md
docs/03-mail-service.md
docs/04-shell-data-pipeline.md
```

运行 Flask 示例：

```bash
cd web/flask_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

另开终端验证：

```bash
curl http://127.0.0.1:2025/
curl http://127.0.0.1:2025/health
```

运行 JSON 解析示例：

```bash
python3 scripts/parse_hotel.py examples/hotel_db.sample.json output.csv
cat output.csv
```

## 安全边界

- 仅在虚拟机、隔离网络或本机回环地址中进行实验。
- 不要提交真实密码、私钥、证书、`.env` 文件或真实业务数据。
- FTP 明文传输和匿名写入只用于理解实验，不适合生产环境。
- 邮件服务配置中的本地域名和测试账号只能用于实验。
- Flask 自带开发服务器不适合生产部署；生产环境应使用 Gunicorn、Nginx 或其他正式部署方案。
- 实验结束后关闭不再使用的服务和防火墙端口。

## 说明

项目中的版本号、镜像地址和配置项可能随 Kali Linux 更新而变化。遇到差异时，请以当前软件的官方文档和本机帮助信息为准。

## 许可证

本项目使用 MIT License，便于他人学习、修改和继续实践。
