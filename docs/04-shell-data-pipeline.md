# 4. Linux 命令与 Shell 数据处理

这一章把原实验中的 Shell 编程、JSON 解析和 FTP 自动传输整理成一条可复用流程：

```text
hotel_db.json -> parse_hotel.py -> output.csv -> ftp_upload.sh -> FTP 服务器
```

## 4.1 解析 JSON

解析器支持 JSON 数组，也支持嵌套在字典或列表中的酒店记录：

```bash
python3 scripts/parse_hotel.py examples/hotel_db.sample.json output.csv
head output.csv
```

输出使用 `utf-8-sig` 编码，便于在 Windows Excel 中直接打开中文 CSV。

## 4.2 使用 jq 快速检查

```bash
sudo apt install -y jq
jq 'type' examples/hotel_db.sample.json
jq '.[0]' examples/hotel_db.sample.json
```

## 4.3 上传到 FTP

复制并修改配置模板：

```bash
cp config/ftp.env.example config/ftp.env
chmod 600 config/ftp.env
```

然后运行：

```bash
bash scripts/ftp_upload.sh config/ftp.env
```

配置文件不会被提交，密码只通过环境配置传入脚本。不要把密码直接写进
Shell 脚本或命令历史。

## 4.4 常用排错命令

```bash
python3 --version
python3 -m py_compile scripts/parse_hotel.py
ss -ltnp
sudo systemctl status vsftpd
sudo journalctl -u vsftpd -n 50 --no-pager
ls -lh output.csv
```

端口冲突时，先找出占用进程：

```bash
sudo lsof -i :2025
sudo lsof -i :21
```
