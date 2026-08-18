#!/usr/bin/env bash
set -euo pipefail

CONFIG_FILE="${1:-config/ftp.env}"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "找不到配置文件: $CONFIG_FILE" >&2
  echo "请复制 config/ftp.env.example 为 config/ftp.env 并填写实验参数。" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$CONFIG_FILE"

: "${FTP_HOST:?FTP_HOST 未设置}"
: "${FTP_PORT:?FTP_PORT 未设置}"
: "${FTP_USER:?FTP_USER 未设置}"
: "${FTP_PASSWORD:?FTP_PASSWORD 未设置}"
: "${FTP_REMOTE_DIR:?FTP_REMOTE_DIR 未设置}"
: "${FTP_LOCAL_FILE:?FTP_LOCAL_FILE 未设置}"

if [[ ! -f "$FTP_LOCAL_FILE" ]]; then
  echo "找不到待上传文件: $FTP_LOCAL_FILE" >&2
  exit 1
fi

command -v lftp >/dev/null || {
  echo "未安装 lftp，请先执行: sudo apt install lftp" >&2
  exit 1
}

lftp -u "$FTP_USER","$FTP_PASSWORD" -p "$FTP_PORT" "$FTP_HOST" <<EOF
set net:timeout 10
set net:max-retries 2
set ftp:passive-mode true
cd "$FTP_REMOTE_DIR"
put "$FTP_LOCAL_FILE"
ls -l "$FTP_LOCAL_FILE"
bye
EOF

echo "上传完成: $FTP_LOCAL_FILE -> ftp://$FTP_HOST:$FTP_PORT$FTP_REMOTE_DIR"
