#!/bin/bash
# 常驻运行：每天 10 点自动执行，不依赖 cron。tmux 里跑一次即可。
# 用法: tmux 里执行: cd /mnt/dataset/jmzhou/papers && ./run_forever.sh

export http_proxy=http://192.168.100.117:18000
export https_proxy=http://192.168.100.117:18000

cd "$(dirname "$0")"
exec python3 run_forever.py
