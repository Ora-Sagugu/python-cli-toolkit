# ## Day 3 - 2026-06-25 - 字符串
# 任务：写 `day03_text_tool.py`。输入一句话，输出长度、全大写、全小写、去掉首尾空格、替换一个词、判断是否包含指定关键词。
# 验收：至少用 `len()`、`.strip()`、`.replace()`、`in`。
# 效果：你能处理用户输入的文字，不再只会打印原样内容。

text = input("请输入一句话：")
print(f"长度：{len(text)}")
print(f"全大写：{text.upper()}")
print(f"全小写：{text.lower()}")
print(f"去掉首尾空格：{text.strip()}")
print(f"替换后的文本：{text.replace('旧词', '新词')}")
print(f"是否包含关键词：{'关键词' in text}")