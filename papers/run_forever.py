#!/usr/bin/env python3
"""
Paper Tracker 常驻进程：每天上午 10 点自动执行一次（VLN + 3D 分割 两个方向），不依赖 cron。
tmux 里执行一条命令即可，不 kill 会一直跑，到点自动更新 output/vln_papers.md 与 output/seg3d_papers.md。
"""

import os
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

PROXY = "http://192.168.100.117:18000"
os.environ["http_proxy"] = PROXY
os.environ["https_proxy"] = PROXY

SCRIPT_DIR = Path(__file__).resolve().parent
TARGET_HOUR = 10  # 上午 10 点
TARGET_MINUTE = 0


def seconds_until_next_run():
    """返回距离下一个 10:00 的秒数。若当前就是 10:00 刚过，则算明天 10:00。"""
    now = datetime.now()
    next_run = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=0, microsecond=0)
    if now >= next_run:
        next_run += timedelta(days=1)
    return (next_run - now).total_seconds()


def main():
    print("Paper Tracker - 常驻模式（每天 10:00 自动更新 vln_papers.md + seg3d_papers.md）")
    print("按 Ctrl+C 或关闭 tmux 窗口可退出")
    print("=" * 50)

    while True:
        secs = seconds_until_next_run()
        next_time = datetime.now() + timedelta(seconds=secs)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 下次执行: {next_time.strftime('%Y-%m-%d %H:%M:%S')} (约 {secs/3600:.1f} 小时后)")
        try:
            import time
            time.sleep(secs)
        except KeyboardInterrupt:
            print("\n已退出")
            sys.exit(0)

        print("\n" + "=" * 50)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始执行抓取 (vln + seg3d)...")
        ret = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "arxiv_vln_tracker.py"), "--force", "--all"],
            cwd=str(SCRIPT_DIR),
            env=os.environ,
        )
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 本次执行结束，返回值 {ret.returncode}\n")


if __name__ == "__main__":
    main()
