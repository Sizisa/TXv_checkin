# coding: utf-8


import requests
import json
import os

qmsg = 'https://qmsg.zendee.cn:443/send/23108d70ff75a7ef5a18a53c3938b002'
auth_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=191234987&g_vstk=44874804&g_actk=574009123&callback=jQuery1910965368943734177_1595985562219&_=1595985562220'
cookie1='RK=q3J9E9MmTj; ptcz=dc89eb452648b12124ad551b12ea200b082a3dce23af0ca2e3749f02f3a08fd9; pgv_pvid=4403475030; pgv_pvi=7673968640; o_cookie=1327438873; pac_uid=1_1327438873; ied_qq=o1327438873; pgv_si=s5039121408; sd_userid=69621595638226845; sd_cookie_crttime=1595638226845; tvfe_boss_uuid=f6ca8a2f39640cf3; video_guid=4affd9a315f25151; video_platform=2; pgv_info=ssid=s8244400141; main_login=qq; vqq_access_token=5BDCFCA9C0571A438D20A2F61E0163D4; vqq_appid=101483052; vqq_openid=A7A15EDA4AE45C149445FEE5ADDCDC58; vqq_vuserid=157362773; vqq_refresh_token=20718E7BED61601D6F7FAFA18D273AD3; login_time_init=2020-7-26 18:7:42; login_type=1; idt=1595917900; uin=o1327438873; skey=@mbqVPMq4n; qqmusic_uin=1327438873; qqmusic_key=@mbqVPMq4n; qqmusic_fromtag=6; vqq_vusession=HdWgYqRza6yZOoQ_dKBrgQ..; uid=250640454; vqq_next_refresh_time=6585; vqq_login_time_init=1595985444; login_time_last=2020-7-29 9:17:24'
cookie2='RK=q3J9E9MmTj; ptcz=dc89eb452648b12124ad551b12ea200b082a3dce23af0ca2e3749f02f3a08fd9; pgv_pvid=4403475030; pgv_pvi=7673968640; o_cookie=1327438873; pac_uid=1_1327438873; ied_qq=o1327438873; pgv_si=s5039121408; sd_userid=69621595638226845; sd_cookie_crttime=1595638226845; tvfe_boss_uuid=f6ca8a2f39640cf3; video_guid=4affd9a315f25151; video_platform=2; pgv_info=ssid=s8244400141; main_login=qq; vqq_access_token=5BDCFCA9C0571A438D20A2F61E0163D4; vqq_appid=101483052; vqq_openid=A7A15EDA4AE45C149445FEE5ADDCDC58; vqq_vuserid=157362773; vqq_refresh_token=20718E7BED61601D6F7FAFA18D273AD3; login_time_init=2020-7-26 18:7:42; login_type=1; idt=1595917900; uin=o1327438873; skey=@mbqVPMq4n; qqmusic_uin=1327438873; qqmusic_key=@mbqVPMq4n; qqmusic_fromtag=6; uid=250640454; vqq_next_refresh_time=6585; vqq_login_time_init=1595985444; login_time_last=2020-7-29 9:17:24;vqq_vusession='



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
