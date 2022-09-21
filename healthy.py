import os
import requests

if __name__ == "__main__":
  push = os.environ["push"]
  username = os.environ["username"]
  password = os.environ["password"]
  if len(username) == 0 and len(password) == 0:
    print("用户名或密码未设置！！！")
    exit(0)
  if len(push) == 0:
    print("未设置PUSH_KEY，无法使用Server酱推送运行日志！！！")
  print("用户名与密码设置成功，正在开始执行后续代码...")
