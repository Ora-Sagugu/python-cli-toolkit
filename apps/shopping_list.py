"""Shopping List — CLI shopping cart with pricing and item management."""

# state
shopping_list = []


def add_item():
    name = input("请输入商品名称：").strip()
    if not name:
        print("商品名称不能为空。\n")
        return
    while True:
        try:
            price = float(input("请输入单价："))
            qty = int(input("请输入数量："))
            if price < 0 or qty <= 0:
                print("单价不能为负，数量必须大于 0。")
                continue
            break
        except ValueError:
            print("输入无效，单价和数量必须是数字，请重试。")
    item = {"name": name, "price": price, "qty": qty}
    shopping_list.append(item)
    print(f"已添加：{name} × {qty}，单价 {price:.2f} 元\n")


def view_list():
    if not shopping_list:
        print("购物清单为空。\n")
        return

    print("===== 当前购物清单 =====")
    total = 0
    for i, item in enumerate(shopping_list, 1):
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(
            f"{i}. {item['name']}  |  单价: {item['price']:.2f}  |  "
            f"数量: {item['qty']}  |  小计: {subtotal:.2f}"
        )
    print("-" * 30)
    print(f"总价：{total:.2f} 元\n")


def delete_item():
    if not shopping_list:
        print("购物清单为空。\n")
        return
    view_list()
    try:
        num = int(input("请输入要删除的商品编号："))
    except ValueError:
        print("请输入有效的数字。\n")
        return
    if 1 <= num <= len(shopping_list):
        removed = shopping_list.pop(num - 1)
        print(f"已删除：{removed['name']}\n")
    else:
        print("编号无效。\n")


def main():
    while True:
        print("===== 购物清单系统 =====")
        print("1. 添加商品")
        print("2. 查看清单")
        print("3. 删除商品")
        print("0. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_list()
        elif choice == "3":
            delete_item()
        elif choice == "0":
            print("退出购物清单，再见！")
            break
        else:
            print("无效选项，请重新输入。\n")


if __name__ == "__main__":
    main()
