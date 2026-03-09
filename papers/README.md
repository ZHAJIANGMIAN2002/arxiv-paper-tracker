# Arxiv Paper Tracker

自动从 [arXiv](https://arxiv.org) 抓取指定方向的最新论文，提取**标题、作者、单位、摘要**，将摘要翻译为中文，并生成/更新 Markdown 报告。支持**每日定时**运行（常驻进程或 cron），适合长期追踪 VLN、3D 分割等方向。

## 功能概览

- **多研究方向**：内置两个方向，可扩展
  - **VLN**：Vision-and-Language Navigation（视觉语言导航）
  - **Seg3D**：3D 语义/实例分割（点云、场景分割等）
- **每篇论文包含**：发布日期、标题、作者、**单位/机构**（从论文 HTML 页解析）、分类、Arxiv/PDF 链接、英文摘要 + **中文翻译摘要**
- **去重**：按 arxiv id 记录已抓取论文，再次运行只追加新论文
- **定时更新**：支持每天固定时间（默认 10:00）自动执行，无需 cron 亦可使用常驻脚本

## 环境要求

- Python 3.8+
- 可访问 arXiv 与 Google 翻译（国内用户需自行配置代理）

## 安装

```bash
git clone https://github.com/<owner>/<repo>.git
cd <repo>   # 进入克隆下来的仓库目录
pip install -r requirements.txt
```

依赖：

- `feedparser`：解析 arXiv API 返回的 Atom
- `requests`：HTTP 请求
- `deep-translator`：摘要英译中（调用 Google 翻译）

**代理（可选）**：若无法直连 arXiv / Google 翻译，运行前设置环境变量 `http_proxy`、`https_proxy`，或在 `arxiv_vln_tracker.py`、`run_forever.sh`、`run_daily.sh` 中修改代理地址。无需代理时，将脚本中的 `PROXY` 置空即可。

## 使用方法

### 1. 单次运行（立即抓取并写 md）

```bash
cd papers

# 只抓 VLN，有则更新 vln_papers.md
python3 arxiv_vln_tracker.py --force

# 只抓 3D 分割，有则更新 seg3d_papers.md
python3 arxiv_vln_tracker.py --topic seg3d --force

# 同时抓两个方向，更新两个 md
python3 arxiv_vln_tracker.py --force --all
```

常用参数：

| 参数 | 说明 |
|------|------|
| `--topic vln` | 仅 VLN（默认） |
| `--topic seg3d` | 仅 3D 语义/实例分割 |
| `--all` | VLN + Seg3D 都跑一遍 |
| `--force` | 即使本次没有新论文，也写一次 md（更新「最后更新」时间等） |
| `--dry-run` | 只拉取、过滤并打印列表，不写文件、不翻译 |

示例：先试跑、看会抓到哪些论文再决定是否写文件：

```bash
python3 arxiv_vln_tracker.py --topic seg3d --dry-run
```

### 2. 每天定时更新（推荐：一条命令常驻）

不依赖系统 cron，在 **tmux** 里跑一个常驻进程，每天到点自动执行一次（VLN + Seg3D 都会跑）：

```bash
cd papers
./run_forever.sh
```

- 启动后会打印「下次执行时间」（默认每天 10:00）
- 到点后自动执行 `arxiv_vln_tracker.py --force --all`，更新 `vln_papers.md` 和 `seg3d_papers.md`
- 不关 tmux、不 kill 进程则会一直跑，每天更新

可配合 tmux：`tmux new -s paper` 后执行上述命令，用 `Ctrl+B D` 脱离，`tmux attach -t paper` 重新连接。

### 3. 使用系统 cron 每天执行

若希望用系统定时任务而不是常驻进程：

```bash
# 安装 cron 条目（每天 10:00 执行，并写日志）
./setup_cron.sh
```

或手动添加 crontab：

```bash
0 10 * * * /path/to/papers/run_daily.sh >> /path/to/papers/output/cron.log 2>&1
```

`run_daily.sh` 内部会执行 `python3 arxiv_vln_tracker.py --force --all`，即两个方向都会更新。

## 输出文件说明

| 路径 | 说明 |
|------|------|
| `output/vln_papers.md` | VLN 方向论文列表（按日期分段，新内容在文件上方） |
| `output/seg3d_papers.md` | 3D 分割方向论文列表 |
| `output/fetched_ids.json` | VLN 已抓取的 arxiv id，用于去重 |
| `output/fetched_ids_seg3d.json` | Seg3D 已抓取的 arxiv id |
| `output/tracker.log` | 主脚本运行日志 |
| `output/cron.log` | 使用 cron 时的每日执行日志（由 run_daily.sh 写入） |

Markdown 中每篇论文包含：发布日期、标题、作者、单位、分类、Arxiv/PDF 链接、英文摘要与中文翻译。

## 测试

```bash
cd papers
python3 test_tracker.py
```

会跑单元测试与一次集成测试（使用临时目录）。需代理时请先设置环境变量或修改脚本中的代理。

## 项目结构

```
papers/
├── README.md              # 本说明
├── requirements.txt      # Python 依赖
├── arxiv_vln_tracker.py  # 主脚本：抓取、过滤、翻译、写 md
├── test_tracker.py       # 测试
├── run_forever.py        # 常驻进程：每天到点执行
├── run_forever.sh        # 启动常驻
├── run_daily.sh          # 供 cron 调用的单次执行
├── setup_cron.sh         # 写入 crontab
└── output/               # 输出目录
    ├── vln_papers.md
    ├── seg3d_papers.md
    ├── fetched_ids.json
    ├── fetched_ids_seg3d.json
    └── tracker.log
```

## License

可按你选择的许可证开源（如 MIT）。若使用本脚本，欢迎注明来源或加星。

## 致谢

- 论文数据来源：[arXiv API](https://info.arxiv.org/help/api/)
- 摘要翻译：[deep-translator](https://github.com/nidhaloff/deep-translator)（Google 翻译）
