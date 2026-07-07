# ## Day 8 - 2026-06-30 - dict 字典
# 任务：写 `day08_contact_card.py`。创建一个联系人字典，包含姓名、电话、城市、备注；允许用户修改电话并打印完整名片。
# 验收：必须通过 key 读取和修改值；输出时逐项打印。
# 效果：你能用键值对表示一个真实对象。

# 1. 创建一个包含姓名、电话、城市、备注的联系人字典
contact = {
    "姓名": "小明",
    "电话": "13800138000",
    "城市": "上海",
    "备注": "同事"
}

print("原始名片：")
for key, value in contact.items():
    print(f"{key}：{value}")

# 2. 允许用户修改电话（通过 key 修改值）
new_phone = input("\n请输入新的电话号码：")
contact["电话"] = new_phone   # 通过 key 修改值

# 3. 逐项打印完整名片
# print("\n更新后的名片：")
print("更新后的名片：")


# print(f"姓名：{contact['姓名']}")1
# print(f"电话：{contact['电话']}")
# print(f"城市：{contact['城市']}")
# print(f"备注：{contact['备注']}")

for key, value in contact.items():
    print(f"{key}：{value}")