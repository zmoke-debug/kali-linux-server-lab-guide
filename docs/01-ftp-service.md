# 1. FTP 文件服务

本章使用 `vsftpd` 在 Kali Linux 虚拟机中搭建一个只供实验使用的 FTP 服务。

## 1.1 安装与检查

```bash
sudo apt update
sudo apt install -y vsftpd lftp
sudo systemctl enable --now vsftpd
sudo systemctl status vsftpd --no-pager
```

## 1.2 创建实验用户

不要使用真实账号或真实密码：

```bash
sudo useradd -m -s /bin/bash labuser
sudo passwd labuser
sudo mkdir -p /home/labuser/uploads
sudo chown -R labuser:labuser /home/labuser/uploads
```

## 1.3 最小本地用户配置

先备份配置：

```bash
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.backup
```

在 `/etc/vsftpd.conf` 中确认以下配置：

```ini
listen=YES
listen_ipv6=NO
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
chroot_local_user=YES
allow_writeable_chroot=YES
pasv_min_port=40000
pasv_max_port=40100
```

重启服务并检查端口：

```bash
sudo systemctl restart vsftpd
sudo ss -ltnp | grep ':21'
```

## 1.4 测试上传

```bash
cp config/ftp.env.example config/ftp.env
# 编辑 config/ftp.env，填写实验用户信息
python3 scripts/parse_hotel.py examples/hotel_db.sample.json output.csv
bash scripts/ftp_upload.sh config/ftp.env
```

## 1.5 安全说明

FTP 默认不加密，实验完成后关闭服务：

```bash
sudo systemctl disable --now vsftpd
```

实际环境请使用 SFTP 或 FTPS，不要开启匿名写入，也不要把 21 端口暴露到公网。
