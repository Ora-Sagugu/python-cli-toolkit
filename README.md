# python-15-day-learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Progress](https://img.shields.io/badge/Progress-Day%2011%2F15-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

用 15 天系统学习 Python 基础语法，每天交付 1 个可运行脚本，最终完成 4 个命令行小项目。

*A structured 15-day Python fundamentals journey with daily exercises and 4 CLI mini-projects.*

---

## 学习进度

| Day | 日期 | 主题 | 文件 | 状态 |
|-----|------|------|------|------|
| 1 | 06-23 | print / input | `exercises/day01_self_intro.py` | 已完成 |
| 2 | 06-24 | 变量 / 数字 | `exercises/day02_calculator.py` | 已完成 |
| 3 | 06-25 | 字符串 | `exercises/day03_text_tool.py` | 已完成 |
| 4 | 06-26 | if 判断 | `exercises/day04_score_level.py` | 已完成 |
| 5 | 06-27 | while 循环 | `exercises/day05_password_loop.py` | 已完成 |
| 6 | 06-28 | for 循环 / range | `exercises/day06_number_report.py` | 已完成 |
| 7 | 06-29 | list 列表 | `exercises/day07_name_list.py` | 已完成 |
| 8 | 06-30 | dict 字典 | `exercises/day08_contact_card.py` | 已完成 |
| 9 | 07-01 | function 函数 | `exercises/day09_tools.py` | 已完成 |
| 10 | 07-02 | 综合练习 | `exercises/day10_menu_practice.py` | 已完成 |
| 11 | 07-03 | 项目 1：猜数字 | `projects/project01_guess_number.py` | 已完成 |
| 12 | 07-04 | 项目 2：Todo | `projects/project02_todo.py` | 待完成 |
| 13 | 07-05 | 项目 3：购物清单 | `projects/project03_shopping_list.py` | 待完成 |
| 14 | 07-06 | 项目 4：简单记账 | `projects/project04_accounting.py` | 待完成 |
| 15 | 07-07 | 整理 / 复盘 / 修项目 | — | 待完成 |

---

## 项目亮点

### 项目 1：猜数字

程序随机生成 1–100 的整数，用户循环猜测，提示「大了 / 小了」，猜对后输出尝试次数。

- **技术点**：`random.randint`、`while` 循环、`if / elif / else`
- **运行**：`python projects/project01_guess_number.py`

### 项目 2：Todo（待完成）

命令菜单：添加任务、查看任务、完成任务、删除任务、退出。

### 项目 3：购物清单（待完成）

添加商品名称、单价、数量；查看清单；计算总价。

### 项目 4：简单记账（待完成）

添加收入/支出记录，查看全部记录，统计总收入、总支出、余额。

---

## 快速开始

```bash
git clone https://github.com/<你的用户名>/python-15-day-learning.git
cd python-15-day-learning
python projects/project01_guess_number.py
```

**环境要求**：Python 3.8+，无第三方依赖（纯标准库）。

---

## 学习方法

每天固定节奏：

- **20 分钟学**：只学当天主题，不扩展
- **50 分钟敲**：必须自己输入代码
- **20 分钟改**：故意改错、修错、加一个小功能

完整学习计划见 [python_15_day_plan.md](python_15_day_plan.md)。

---

## 后续计划

- Day 12–14：完成 Todo、购物清单、记账三个项目
- Day 15：四个项目各加 1 个改进，README 定稿
