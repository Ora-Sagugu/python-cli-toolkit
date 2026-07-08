# ## Day 9 - 2026-07-01 - function 函数
# 任务：写 `day09_tools.py`。封装 3 个函数：计算折扣价、判断分数等级、打印联系人名片。
# 验收：每个函数至少调用 2 次；函数里不能依赖手写固定结果。
# 效果：你能把重复逻辑装进函数，开始写可复用代码。

# ---------------- 函数1：计算折扣价 ----------------
def calc_discount(original_price, discount):    # :param discount: 折扣，如 0.8 表示 8 折
    final_price = original_price * discount
    return round(final_price, 2)                # 保留两位小数


# ---------------- 函数2：判断分数等级 ----------------
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# ---------------- 函数3：打印联系人名片 ----------------
def print_contact_card(contact):
    print("----- 联系人名片 -----")
    print(f"姓名：{contact.get('姓名', '未知')}")
    print(f"电话：{contact.get('电话', '未知')}")
    print(f"城市：{contact.get('城市', '未知')}")
    print(f"备注：{contact.get('备注', '无')}")
    print("----------------------")

# ============== 调用测试 ==============
print("=== 函数1：计算折扣价 ===")
price1 = calc_discount(100, 0.85)   # 100元打8.5折
price2 = calc_discount(250, 0.6)    # 250元打6折
print(f"100元打85折：{price1}元")
print(f"250元打6折：{price2}元")

print("\n=== 函数2：判断分数等级 ===")
grade1 = get_grade(95)
grade2 = get_grade(73)
grade3 = get_grade(58)             # 额外调用也可以，至少两次，这里三次
print(f"95分 → {grade1}")
print(f"73分 → {grade2}")
print(f"58分 → {grade3}")

print("\n=== 函数3：打印联系人名片 ===")
contact1 = {
    "姓名": "小明",
    "电话": "13800138000",
    "城市": "上海",
    "备注": "同学"
}
contact2 = {
    "姓名": "小红",
    "电话": "13912345678",
    "城市": "北京"
    # 备注故意不写，测试 get 默认值
}

print_contact_card(contact1)
print_contact_card(contact2)  # 第二次调用，参数不同