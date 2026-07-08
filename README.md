# Python CLI Toolkit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Stdlib](https://img.shields.io/badge/Dependencies-stdlib%20only-green)
![Apps](https://img.shields.io/badge/CLI%20Apps-4-orange)

一组 **Python 标准库命令行小工具**，零第三方依赖，可直接运行演示。

*A collection of stdlib-only CLI mini-apps for Python practice.*

---

## 工具一览

| 工具 | 功能 | 技术点 |
|------|------|--------|
| Guess Number | 猜数字，最多 7 次机会 | `random`, `while`, 输入校验 |
| Todo List | 任务增删改查 + 完成状态筛选 | `list` of `dict`, `enumerate` |
| Shopping List | 商品管理 + 自动计价 + 删除 | 聚合计算, `float` 格式化 |
| Accounting | 收入/支出记录 + 分类筛选 + 汇总 | 条件过滤, 遍历统计 |

---

## 快速开始

```bash
git clone https://github.com/Ora-Sagugu/python-cli-toolkit.git
cd python-cli-toolkit
python main.py
```

也可以单独运行某个工具：

```bash
python apps/todo.py
python apps/accounting.py
```

**环境要求**：Python 3.8+，无需安装任何第三方包。

---

## 项目结构

```
python-cli-toolkit/
├── main.py              # 统一启动器
├── apps/
│   ├── guess_number.py
│   ├── todo.py
│   ├── shopping_list.py
│   └── accounting.py
├── archive/             # 早期练习归档（备查）
└── docs/
    └── INTERVIEW.md     # 面试问答备忘
```

---

## 设计说明

- **数据建模**：用 `list` 存一组 `dict`，每个 dict 表示一条业务记录（任务、商品、账目）
- **纯标准库**：降低环境成本，聚焦 Python 语法和 CLI 交互模式
- **可扩展方向**：JSON 文件持久化、`dataclass` 替代 dict、单元测试、Web 化（Flask/FastAPI）

---

## License

MIT
