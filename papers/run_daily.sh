#!/bin/bash
# Paper Tracker 每日执行（VLN + 3D 分割 两个方向）
# crontab 示例: 0 10 * * * /mnt/dataset/jmzhou/papers/run_daily.sh >> /mnt/dataset/jmzhou/papers/output/cron.log 2>&1

export http_proxy=http://192.168.100.117:18000
export https_proxy=http://192.168.100.117:18000

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "Paper Tracker (vln + seg3d) - $(date '+%Y-%m-%d %H:%M:%S')"
echo "=========================================="

python3 arxiv_vln_tracker.py --force --all

echo "Done at $(date '+%Y-%m-%d %H:%M:%S')"
echo ""
