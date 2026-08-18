# 2. Web 服务：Tomcat 与 Flask

本章提供两个独立的 Web 服务实验。它们不能同时监听同一个端口。

## 2.1 Flask 示例

项目内置了一个不依赖外部数据库的最小 Flask 服务：

```bash
cd web/flask_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

验证：

```bash
curl http://127.0.0.1:2025/
curl http://127.0.0.1:2025/health
```

如果需要让同一实验网络中的其他机器访问，把 `app.py` 中的绑定地址从
`127.0.0.1` 改为 `0.0.0.0`，并只在隔离网络中开放端口。

## 2.2 Tomcat 实验

安装 Java 和 Tomcat：

```bash
sudo apt install -y openjdk-17-jdk
cd /tmp
TOMCAT_VERSION="10.1.X"  # 替换为 Apache 官网当前稳定版本
curl -LO "https://dlcdn.apache.org/tomcat/tomcat-10/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz"
```

Tomcat 的具体下载版本会变化，建议从 Apache Tomcat 官网选择当前稳定版本。
解压后执行：

```bash
sudo mkdir -p /opt/tomcat
sudo tar -xzf apache-tomcat-*.tar.gz -C /opt/tomcat --strip-components=1
sudo chmod +x /opt/tomcat/bin/*.sh
/opt/tomcat/bin/startup.sh
curl http://127.0.0.1:8080/
```

## 2.3 选择建议

| 项目 | Tomcat | Flask |
| --- | --- | --- |
| 技术类型 | Java Web 容器 | Python 微框架 |
| 上手难度 | 较高 | 较低 |
| 典型用途 | Servlet、JSP、企业 Java 应用 | API、原型、小型服务 |
| 本项目中的定位 | 部署流程学习 | 可直接运行的示例 |

Flask 自带服务器只适合开发和实验；生产环境请使用 Gunicorn、Nginx 或其他正式部署方案。
