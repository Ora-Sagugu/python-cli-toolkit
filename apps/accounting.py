"""Accounting — CLI income/expense tracker with filtering and summary."""

# state
records = []


def add_record():
    print("记录类型：1. 收入  2. 支出")
    type_choice = input("请选择：").strip()
    if type_choice == "1":
        record_type = "income"
        type_label = "收入"
    elif type_choice == "2":
        record_type = "expense"
        type_label = "支出"
    else:
        print("无效类型。\n")
        return

    while True:
        try:
            amount = float(input("请输入金额："))
            if amount <= 0:
                print("金额必须大于 0。")
                continue
            break
        except ValueError:
            print("请输入有效的数字。")

    note = input("请输入备注（可留空）：").strip()
    records.append({"type": record_type, "amount": amount, "note": note})
    print(f"已添加{type_label}记录：{amount:.2f} 元\n")


def view_records(filter_type=None):
    """Show records. filter_type: None=all, 'income', 'expense'."""
    filtered = records
    if filter_type == "income":
        filtered = [r for r in records if r["type"] == "income"]
        title = "收入记录"
    elif filter_type == "expense":
        filtered = [r for r in records if r["type"] == "expense"]
        title = "支出记录"
    else:
        title = "全部记录"

    if not filtered:
        print(f"暂无{title}。\n")
        return

    print(f"===== {title} =====")
    for i, record in enumerate(filtered, 1):
        type_label = "收入" if record["type"] == "income" else "支出"
        note = record["note"] or "—"
        print(f"  {i}. [{type_label}] {record['amount']:.2f} 元  |  {note}")
    print()


def calc_summary():
    """Calculate total income, expense, and balance."""
    total_income = sum(r["amount"] for r in records if r["type"] == "income")
    total_expense = sum(r["amount"] for r in records if r["type"] == "expense")
    balance = total_income - total_expense
    return total_income, total_expense, balance


def show_summary():
    if not records:
        print("暂无记录，无法统计。\n")
        return
    total_income, total_expense, balance = calc_summary()
    print("===== 汇总统计 =====")
    print(f"  总收入：{total_income:.2f} 元")
    print(f"  总支出：{total_expense:.2f} 元")
    print(f"  余额：  {balance:.2f} 元\n")


def main():
    while True:
        print("===== 简单记账 =====")
        print("1. 添加记录")
        print("2. 查看全部")
        print("3. 只看收入")
        print("4. 只看支出")
        print("5. 汇总统计")
        print("0. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            view_records("income")
        elif choice == "4":
            view_records("expense")
        elif choice == "5":
            show_summary()
        elif choice == "0":
            print("退出记账，再见！")
            break
        else:
            print("无效选项，请重新输入。\n")


if __name__ == "__main__":
    main()
