# ## Day 4 - 2026-06-26 - if 判断
# 任务：写 `day04_score_level.py`。输入分数，输出优秀/良好/及格/不及格；输入年龄，判断是否成年。
# 验收：必须包含 `if / elif / else`；至少测试 59、60、79、80、90。
# 效果：你能让程序根据不同情况走不同路线。

score = int(input("请输入分数（0-100）："))
if score >= 90:print("优秀")
elif score >= 80:print("良好")
elif score >= 60:print("及格")
else:print("不及格")