# 任务：写 day01_self_intro.py。用 input() 收集姓名、年龄、城市、今天学习分钟数，用 print() 输出一段完整自我介绍。
# 验收：运行后至少输入 4 次，输出 4 行以上；不能只写固定文字。
# 效果：你能让程序和人对话，知道程序从哪里拿输入、往哪里给输出。

name=input("请输入你的名字")
age=input("请输入你的年龄")
city=input("请输入你所在的城市")
today_learn_minite=input("请输入你今天学习的分钟数")
print("大家好，我叫"+name+"，我今年"+age+"岁，来自"+city+"，今天我学习了"+today_learn_minite+"分钟。")
print(f"大家好，我叫{name}，我今年{age}岁，来自{city}，今天我学习了{today_learn_minite}分钟。")
