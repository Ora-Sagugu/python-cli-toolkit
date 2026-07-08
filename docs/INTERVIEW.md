# 面试问答备忘

> 针对 Python CLI Toolkit 项目，按「概览 → 代码细节 → 扩展」三层准备。

---

## 第一层：项目概览（30 秒）

**Q：这项目做什么？**

A：这是 4 个 Python 标准库 CLI 小工具的集合，包括猜数字、待办清单、购物清单和记账。用来练手菜单驱动程序、list/dict 数据建模和输入校验，每个工具都可以独立运行。

**Q：为什么不做 Web？**

A：刻意用 CLI 聚焦 Python 语言本身和程序结构。后续可以把业务逻辑迁移到 Flask 或 FastAPI，CLI 层已经验证了核心逻辑。

**Q：为什么零依赖？**

A：降低 clone 后的运行成本，也展示对标准库的掌握。面试时可以直接 `python main.py` 演示。

---

## 第二层：代码细节（必问）

### Guess Number

**Q：`while True` 和 `break` 怎么配合？**

A：`while True` 创建无限循环，猜对时用 `return` 或 `break` 退出。这里用 `attempts < MAX_ATTEMPTS` 控制上限，次数用尽也会退出。

**Q：用户输入字母会怎样？**

A：裸写 `int(input())` 会抛 `ValueError`。我在 `read_guess()` 里用 `try/except` 捕获，提示用户重新输入。

**Q：7 次限制怎么实现？**

A：`while attempts < MAX_ATTEMPTS`，每次有效猜测后 `attempts += 1`，循环结束后若未猜对则打印正确答案。

### Todo List

**Q：为什么用 list 存 dict？**

A：list 表示「一组同类记录」，dict 表示「单条记录的多字段」。比多个平行 list（一个存内容、一个存状态）更不容易 index 错位。

**Q：`enumerate(tasks, 1)` 第二个参数是什么？**

A：起始编号。设为 1 让用户看到的编号从 1 开始，内部转 index 时减 1。

**Q：`tasks.pop(num - 1)` 为什么减 1？**

A：用户输入的是 1-based 编号，Python list 是 0-based index。

**Q：数据怎么持久化？**

A：当前存在内存，程序退出即丢失。下一步可以用 `json.dump` / `json.load` 读写本地文件，启动时加载、退出时保存。

### Shopping List

**Q：总价为什么用循环累加？**

A：商品数量不确定，不能手写加法。遍历每条记录算小计再累加，数据变多时逻辑不用改。

**Q：`float` 做金额精确吗？**

A：练手够用。生产环境应该用 `decimal.Decimal` 避免浮点精度问题。

**Q：删除商品后编号变了怎么办？**

A：每次删除前先展示当前列表，用户基于最新编号操作。删除后立即 `pop`，后续编号自动重排。

### Accounting

**Q：收入和支出怎么区分？**

A：每条记录有 `type` 字段，值为 `"income"` 或 `"expense"`。

**Q：筛选和汇总能共用逻辑吗？**

A：可以。`view_records(filter_type)` 用条件过滤，`calc_summary()` 用生成器表达式分别累加收入和支出。进一步可以把统计逻辑抽成独立函数供测试。

**Q：只有支出没有收入，余额怎么算？**

A：`balance = total_income - total_expense`，收入为 0 时余额就是负的总支出，逻辑仍然正确。

### 通用

**Q：list 和 dict 分别适合什么？**

A：list 适合有序的一组同类数据；dict 适合表示单个对象的多个属性（键值对）。

**Q：函数封装的好处？**

A：逻辑复用、职责清晰、方便单独测试。每个 app 的 `main()` 只管菜单调度，具体操作拆成独立函数。

**Q：菜单选项多了，`if/elif` 有什么问题？**

A：选项多时可改用 dict 映射：`handlers = {"1": add_task, "2": view_tasks}`，新增选项只加一行，不用改一长串 elif。

---

## 第三层：扩展与工程

**Q：怎么写测试？**

A：把业务逻辑从 `input()` 里拆出来（如 `calc_summary()`），用 pytest 传 mock 数据断言结果，UI 层单独测或手工测。

**Q：生产环境你会怎么改？**

A：JSON/SQLite 持久化、类型注解、`dataclass` 替代 dict、统一异常处理、日志（`logging` 模块）、单元测试覆盖。

**Q：遇到的最大 bug？**

A：（准备一个真实例子）比如 Todo 删除时 index 越界、购物清单输入非数字导致崩溃、中文 dict key 拼写不一致导致 KeyError。改英文 key + 输入校验后解决。

---

## 可能被刁钻的问题

**Q：这不就是入门作业吗？**

A：定位是练手项目，但做了统一入口、输入校验、完成度补齐和代码规范。GitHub 上我还有 QR-Paper-Studio 等更完整的项目，这个 repo 展示 Python 基础和 CLI 程序结构。

**Q：为什么 dict key 用英文？**

A：代码标识符用英文是行业规范，便于协作和阅读；用户界面提示可以用中文。数据和代码分离。

---

## 演示建议

1. 先跑 `python main.py`，展示统一入口
2. 演示 Todo 的「筛选已完成/未完成」
3. 演示 Accounting 的「汇总统计」
4. 主动提一句：「下一步计划加 JSON 持久化」
