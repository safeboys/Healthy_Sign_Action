import os

if __name__ == "__main__":
  username = os.environ["username"]
  password = os.environ["password"]
  if len(username) == 0 and len(password) == 0:
    print("用户名或密码未设置！！！")
    exit(0)
  print("用户名与密码设置成功，正在开始执行后续代码...")
