# 任务：写 `day07_name_list.py`。维护一个姓名列表：添加 3 个名字、删除 1 个、修改 1 个、遍历打印全部名字。
# 验收：必须用 `.append()`、`.remove()` 或 `del`、索引修改、`for` 遍历。
# 效果：你能管理一组同类数据。

# 初始化空列表
names = []

# 1. 添加 3 个名字（使用 .append()）
names.append("张三")
names.append("李四")
names.append("王五")
print("添加后：", names)

# 2. 删除 1 个名字（使用 .remove() 删除指定元素，或用 del 按索引删）
names.remove("李四")   # 按值删除
print("删除后：", names)

# 3. 修改 1 个名字（通过索引修改）
names[0] = "赵六"      # 将索引 0 的 "张三" 改为 "赵六"
print("修改后：", names)

# 4. 遍历打印全部名字（必须用 for 循环）
print("最终名单：")
for name in names:
    print(name)