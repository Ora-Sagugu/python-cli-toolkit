"""Guess Number — CLI number guessing game with attempt limit."""

import random

MAX_ATTEMPTS = 7


def read_guess():
    """Read and validate user guess."""
    while True:
        try:
            return int(input("请输入你猜的数字（1-100）："))
        except ValueError:
            print("请输入有效的整数。")


def main():
    target = random.randint(1, 100)
    attempts = 0

    print("猜数字游戏开始！我已经想好了一个 1~100 之间的整数。")
    print(f"你有最多 {MAX_ATTEMPTS} 次机会。\n")

    while attempts < MAX_ATTEMPTS:
        guess = read_guess()
        attempts += 1

        if guess < target:
            print("太小了，再试试！")
        elif guess > target:
            print("太大了，再试试！")
        else:
            print(f"恭喜你猜对了！答案就是 {target}。")
            print(f"你一共猜了 {attempts} 次。")
            return

        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"还剩 {remaining} 次机会。\n")

    print(f"次数已用尽，正确答案是 {target}。")


if __name__ == "__main__":
    main()
