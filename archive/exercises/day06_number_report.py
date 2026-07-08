# 任务：写 `day06_number_report.py`。输出 1-100 中所有偶数，计算 1-100 总和，统计能被 3 整除的数量。
# 验收：必须用 `for` 和 `range()`；输出总和与统计结果。
# 效果：你能让程序自动重复处理一批数字。

total = 0
count_div3 = 0

print("1-100中的所有偶数：", end="")

# 使用 for 和 range() 遍历 1 到 100
for i in range(1, 101):
    # 1. 输出偶数
    if i % 2 == 0: 
        print(i, end=" ")  # 在同一行用空格分隔

    # 2. 累加总和
    total += i  # 等价于 total = total + i

    # 3. 统计能被3整除的数
    if i % 3 == 0:
        count_div3 += 1

# 输出总和和统计结果
print()  # 换行
print(f"1-100的总和：{total}")
print(f"能被3整除的个数：{count_div3}")