"""Todo List — CLI task manager with completion status and filtering."""

# state
tasks = []


def add_task():
    content = input("请输入任务内容：").strip()
    if not content:
        print("任务内容不能为空。\n")
        return
    tasks.append({"content": content, "done": False})
    print(f"已添加任务：{content}\n")


def view_tasks(filter_mode=None):
    """Show tasks. filter_mode: None=all, 'done', 'pending'."""
    filtered = tasks
    if filter_mode == "done":
        filtered = [t for t in tasks if t["done"]]
        title = "已完成任务"
    elif filter_mode == "pending":
        filtered = [t for t in tasks if not t["done"]]
        title = "未完成任务"
    else:
        title = "全部任务"

    if not filtered:
        print(f"暂无{title.replace('任务', '')}任务。\n")
        return

    print(f"===== {title} =====")
    for i, task in enumerate(filtered, 1):
        status = "✓" if task["done"] else "✗"
        print(f"  {i}. [{status}] {task['content']}")
    print()


def _pick_task_index(prompt):
    """Return 0-based index from user input against current tasks list."""
    if not tasks:
        return None
    view_tasks()
    try:
        num = int(input(prompt))
    except ValueError:
        print("请输入有效的数字。\n")
        return None
    if 1 <= num <= len(tasks):
        return num - 1
    print("编号无效。\n")
    return None


def complete_task():
    idx = _pick_task_index("请输入要完成的任务编号：")
    if idx is None:
        return
    tasks[idx]["done"] = True
    print(f"任务已标记为完成：{tasks[idx]['content']}\n")


def delete_task():
    idx = _pick_task_index("请输入要删除的任务编号：")
    if idx is None:
        return
    removed = tasks.pop(idx)
    print(f"已删除任务：{removed['content']}\n")


def main():
    while True:
        print("===== 待办清单 =====")
        print("1. 添加任务")
        print("2. 查看全部")
        print("3. 查看已完成")
        print("4. 查看未完成")
        print("5. 完成任务")
        print("6. 删除任务")
        print("0. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks("done")
        elif choice == "4":
            view_tasks("pending")
        elif choice == "5":
            complete_task()
        elif choice == "6":
            delete_task()
        elif choice == "0":
            print("退出待办清单，再见！")
            break
        else:
            print("无效选项，请重新输入。\n")


if __name__ == "__main__":
    main()
