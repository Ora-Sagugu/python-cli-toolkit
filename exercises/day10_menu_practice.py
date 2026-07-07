# ## Day 10 - 2026-07-02 - 综合练习
# 任务：写 `day10_menu_practice.py`。做一个命令菜单：1 算折扣，2 判断分数，3 管理姓名列表，0 退出。
# 验收：必须用 `while` 做菜单循环；必须调用函数；输入 0 能退出。
# 效果：你第一次写出“可反复使用”的小程序结构。
# 文件：day10_menu_practice.py
# 综合菜单程序：1 算折扣 2 判断分数 3 管理姓名列表 0 退出

# ---------- 功能函数（复用之前思路） ----------
def calc_discount():
    """计算折扣价"""
    price = float(input("请输入原价："))
    discount = float(input("请输入折扣（如 0.85 表示 85 折）："))
    final = round(price * discount, 2)
    print(f"折后价：{final} 元\n")

def get_grade():
    """判断分数等级"""
    score = int(input("请输入分数（0-100）："))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"等级：{grade}\n")

def manage_names():
    """管理姓名列表（添加、删除、查看）"""
    names = []  # 每次进入管理时重置列表（也可考虑全局，但这里练习局部列表）
    while True:
        print("--- 姓名管理 ---")
        print("1. 添加名字")
        print("2. 删除名字")
        print("3. 查看所有名字")
        print("0. 返回主菜单")
        choice = input("请选择：")
        if choice == "1":
            name = input("输入要添加的名字：")
            names.append(name)
            print(f"已添加 {name}\n")
        elif choice == "2":
            if len(names) == 0:
                print("列表为空，无法删除\n")
            else:
                name = input("输入要删除的名字：")
                if name in names:
                    names.remove(name)
                    print(f"已删除 {name}\n")
                else:
                    print("名字不在列表中\n")
        elif choice == "3":
            print("当前名单：", names, "\n")
        elif choice == "0":
            break
        else:
            print("无效选项，请重试\n")

# ---------- 主菜单循环 ----------
while True:
    print("===== 主菜单 =====")
    print("1. 计算折扣")
    print("2. 判断分数等级")
    print("3. 管理姓名列表")
    print("0. 退出程序")
    option = input("请输入选项：")

    if option == "1":
        calc_discount()
    elif option == "2":
        get_grade()
    elif option == "3":
        manage_names()
    elif option == "0":
        print("程序已退出，再见！")
        break
    else:
        print("无效选项，请重新输入\n")
