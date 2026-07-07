# ## Day 5 - 2026-06-27 - while 循环
# 任务：写 `day05_password_loop.py`。设置密码，用户最多输入 3 次；输对显示成功，输错 3 次显示锁定。
# 验收：必须用 `while`；必须有次数计数；输对后能提前结束。
# 效果：你能写“重复尝试直到成功/失败”的程序。

password = "123456"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("请输入密码：")
    if user_input == password:
        print("密码正确，登录成功！")
        break
    else:
        attempts += 1
        # if attempts < max_attempts:
        #     print(f"密码错误，您还有 {max_attempts - attempts} 次机会。")
        # else:
        #     print("密码错误，账户已被锁定。")   