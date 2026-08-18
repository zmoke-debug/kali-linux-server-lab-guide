# 3. 本地邮件服务：Postfix + Dovecot

本章在 Kali Linux 虚拟机中搭建本地邮件实验。邮件服务配置复杂且容易被滥用，
只建议在隔离网络中进行。

## 3.1 安装组件

```bash
sudo apt update
sudo apt install -y postfix dovecot-imapd mailutils
```

Postfix 安装向导中选择 `Local only`，系统邮件名填写虚拟机的本地域名，
例如 `kali.lab`。

## 3.2 创建测试用户

```bash
sudo useradd -m mailuser
sudo passwd mailuser
```

不要使用真实邮箱密码。检查服务状态：

```bash
sudo systemctl enable --now postfix dovecot
sudo systemctl status postfix dovecot --no-pager
```

## 3.3 本地收发测试

发送本地邮件：

```bash
echo "Kali mail lab" | mail -s "test message" mailuser
```

查看邮件目录：

```bash
sudo ls -la /var/mail/mailuser
sudo journalctl -u postfix -n 30 --no-pager
sudo journalctl -u dovecot -n 30 --no-pager
```

如果需要使用 Foxmail、Thunderbird 等客户端，只在实验网络中开放 IMAP
端口，并优先配置 TLS。不要把开放中继、SMTP 认证或真实域名配置到公网环境。

## 3.4 停止实验服务

```bash
sudo systemctl disable --now postfix dovecot
```
