# Day 2 - 2026-06-24 - 变量 / 数字
# 任务：写 day02_calculator.py。
# 输入商品单价、数量、折扣，输出原价、折后价、节省金额。
# 验收：至少用 5 个变量；数字要做加减乘除；输出结果带说明文字。
# 效果：你能把现实里的计算步骤翻译成变量和公式。

unit_price = float(input("请输入商品单价（元）："))
quantity = int(input("请输入购买数量："))
discount = float(input("请输入折扣（如0.8表示8折）："))

original_price = unit_price * quantity
discounted_price = original_price * discount
savings = original_price - discounted_price

print(f"原价：{original_price:.2f}元")
print(f"折后价：{discounted_price:.2f}元")
print(f"节省金额：{savings:.2f}元")