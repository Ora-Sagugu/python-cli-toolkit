# ## Day 11 - 2026-07-03 - 项目 1：猜数字
# 任务：写 `project01_guess_number.py`。程序随机生成 1-100 的数字，用户猜，提示大了/小了/猜对了，最后输出尝试次数。
# 验收：必须用 `random.randint()`、`while`、`if`；猜对后结束。
# 效果：你完成第一个有规则、有反馈、有结束条件的项目。

import random

# 1. 随机生成 1-100 的目标数字
target = random.randint(1, 100)

# 2. 初始化尝试次数
attempts = 0

print("猜数字游戏开始！我已经想好了一个 1~100 之间的整数。")

# 3. 循环猜数，直到猜对
while True:
    guess = int(input("请输入你猜的数字："))
    attempts += 1  # 每猜一次，次数加一

    # 4. 判断大小
    if guess < target:
        print("太小了，再试试！")
    elif guess > target:
        print("太大了，再试试！")
    else:
        print(f"恭喜你猜对了！答案就是 {target}。")
        print(f"你一共猜了 {attempts} 次。")
        break  # 猜对，退出循环