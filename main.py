"""CLI Toolkit — entry point for all apps."""

import importlib


APPS = {
    "1": ("猜数字", "apps.guess_number"),
    "2": ("待办清单", "apps.todo"),
    "3": ("购物清单", "apps.shopping_list"),
    "4": ("简单记账", "apps.accounting"),
}


def main():
    while True:
        print("===== Python CLI Toolkit =====")
        for key, (name, _) in APPS.items():
            print(f"  {key}. {name}")
        print("  0. 退出")
        choice = input("请选择要运行的工具：").strip()

        if choice == "0":
            print("再见！")
            break
        if choice not in APPS:
            print("无效选项，请重新输入。\n")
            continue

        _, module_path = APPS[choice]
        module = importlib.import_module(module_path)
        print()
        module.main()
        print()


if __name__ == "__main__":
    main()
