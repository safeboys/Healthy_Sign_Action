import os
import requests
from hashlib import md5

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
  
  request = requests.session()
  header = {
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
  }
  body = {
    "uname" : username,
    "pd_mm" : md5(password.encode()).hexdigest()
  }
  url = 'http://xggl.hnqczy.com/website/login'
  response = request.post(url,headers=header,data=body)
  print(response.text)
