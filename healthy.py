# 时间 2022/09/23 19:30:00
# 作者 ByteSys
# 声明 该程序仅供学习交流，请自觉遵守中华人民共和国网络安全法

import os
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from time import sleep
from time import time
from hashlib import md5

def timeStamp():
  return str(int(round(time()*1000)))

def token(request,header):
  url = 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_=' + timeStamp()
  res = request.get(url,headers=header)
  html = BeautifulSoup(res.text,'html.parser')
  return html.find(id='zzdk_token').get('value')

def notice(key,title,msg):
  #推送通知消息
  url = 'https://sctapi.ftqq.com/%s.send' % key
  body = { 'title':'每日打卡运行日志-%s' % title ,'desp':msg }
  res = requests.post(url,data=body)
  text = json.loads(res.text)
  if text['code'] != 0:
    print("[SCTPUSH]Error: 推送失败,错误信息: " + text['info'])
    return
  pushid = text['data']['pushid']
  readkey = text['data']['readkey']
  print("[SCTPUSH]Info: 推送成功,PushId=%sReadKey=%s" % (pushid,readkey))
  
  #查询推送状态
  sleep(30) #推送需要时间
  url = 'https://sctapi.ftqq.com/push?id=%s&readkey=%s' % (pushid,readkey)
  res = requests.get(url)
  text = json.loads(res.text)
  if text['data'] == None:
    print("[SCTPUSH]Error: 未查询到有任何信息")
    return
  data = text['data']
  print("[SCTPUSH]Info: [用户ID]:%s , [标题]:%s , [内容]:%s , [建立时间]:%s" % (data['uid'],data['title'],data['desp'],data['created_at']))
  
if __name__ == "__main__":
  push = os.environ["push"]
  username = os.environ["username"]
  password = os.environ["password"]
  if len(username) == 0 and len(password) == 0:
    print("[Process]Error: 用户名或密码未设置！！！")
    exit(0)
  if len(push) == 0:
    print("[Process]Info: 未设置PUSH_KEY，无法使用Server酱推送运行日志！！！")
  print("[Process]Info: 用户名与密码设置成功，正在开始执行后续代码...")
  
  #登录账号
  request = requests.session()
  header = {"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"}
  p = md5(password.encode()).hexdigest()
  password = p[:5] + "a" + p[5:9] + "b" + p[9:30]
  body = { "uname" : username , "pd_mm" : password }
  url = 'http://xggl.hnqczy.com/website/login'
  res = request.post(url,headers=header,data=body)
  text = json.loads(res.text)
  if res.status_code == 200 and text.get('error',0) == True:
    print(text['msg'])
    print("[Process]Error: 服务器返回错误，程序终止...")
    exit(0)
  print("[Process]Info: 登录成功，开始打卡...")
  
  #获取上次的打卡信息
  url = 'http://xggl.hnqczy.com/content/student/temp/zzdk/lastone?_t_s_=' + timeStamp()
  res = request.get(url,headers=header)
  data = json.loads(res.text)
  print("[Process]Info: 获取上次打卡信息成功...")
  
  #开始打卡
  body = {
    'dkdz':data['dkdz'],
    'dkdzZb':'113.134,27.8275',
    'dkly':data['dkly'],
    'zzdk_token':token(request,header),
    'dkd':data['dkd'],
    'jzdValue':'%s,%s,%s' % (data['jzdSheng']['dm'], data['jzdShi']['dm'], data['jzdXian']['dm']),
    'jzdSheng.dm':data['jzdSheng']['dm'],
    'jzdShi.dm':data['jzdShi']['dm'],
    'jzdXian.dm':data['jzdXian']['dm'],
    'jzdDz':data['jzdDz'],
    'jzdDz2':data['jzdDz2'],
    'lxdh':data['lxdh'],
    'sfzx':data['sfzx'],
    'sfzx1':(['不在校','在校'])[int(data['sfzx'])],
    'twM.dm':'01', 'tw1':'[35.0~37.2]正常',
    'yczk.dm':'01', 'yczk1':'无症状',
    'jzInd':'0', 'brStzk.dm':'01', 'brStzk1':'身体健康、无异常',
    'brJccry.dm':'01', 'brJccry1':'未接触传染源',
    'jrStzk.dm':'01', 'jrStzk1':'身体健康、无异常',
    'jrJccry.dm':'01', 'jrJccry1':'未接触传染源',
    'jkm':'1', 'jkml':'绿色', 'xcm':'1', 'xcm1':'绿色',
    'xgym':'3', 'xgym1':'', 'operationType':'Create'
  }
  print("[Process]Info: 打卡信息: %s" % (body))
  url = 'http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_=' + timeStamp()
  res = request.post(url,headers=header,data=body)
  text = json.loads(res.text)
  if text['result'] == False:
    print("[Process]Error: %s" % text['errorInfoList'][0]['message'])
    print("[Process]Info: 打卡失败，推送失败信息...")
    notice(push,"打卡失败","操作用户：%s\r\n\r\n操作日志：%s\r\n\r\n操作时间：%s(UTC)" % (username,text['errorInfoList'][0]['message'],str(datetime.now())))
  else:
    print("[Process]Info: 打卡成功，推送成功信息...")
    notice(push,"打卡成功","操作用户：%s\r\n\r\n操作日志：%s\r\n\r\n操作时间：%s(UTC)" % (username,"无异常",str(datetime.now())))
print("[Process]Info: 程序运行完成...")
