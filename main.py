# coding: utf-8


import requests
import json
import os

qmsg = os.environ['qmsg']
auth_url = os.environ['url']
cookie1=os.environ['cookie1']
cookie2=os.environ['cookie2']

print(qmsg+"")
print(auth_url+"")
print(cookie1+"")
print(cookie2+"")

qq_url = qmsg

url1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'



login_headers = {
    'Referer': 'https://v.qq.com',
    'Cookie': cookie1
}

login = requests.get(auth_url, headers=login_headers)
cookie = requests.utils.dict_from_cookiejar(login.cookies)

if not cookie:
    print ("auth_refresh error")
    payload = {'msg': '腾讯视频V力值签到通知'+'\n'+ '获取Cookie失败，Cookie失效'}
    requests.post(qq_url, params=payload)
    

sign_headers = {
    'Cookie': cookie2 + cookie['vqq_vusession'] + ';'
    ,'Referer': 'https://m.v.qq.com'
}
def respondHandle( str ):
    if '-777903' in str:
        return "已获取过V力值"
    elif '-777902' in str:
        return "任务未完成"
    elif 'OK' in str:
        return "成功，获得V力值：" + str[42:-3]
    else:
        return "执行出错"
    

def start():
  sign1 = requests.get(url1,headers=sign_headers).text

  if 'Account Verify Error' in sign1:
    print ('Sign1 error,Cookie Invalid')
    status = "链接1 失败，Cookie失效"
  else:
    print ('Sign1 Success')
    status = "链接1 成功，获得V力值：" + sign1[42:-14]


  
  payload = {'msg': '腾讯视频V力值签到通知'+"\n"+ status}
  requests.post(qq_url, params=payload)

def main_handler(event, context):
  return start()
if __name__ == '__main__':
  start()
