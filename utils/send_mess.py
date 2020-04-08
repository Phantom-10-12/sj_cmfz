# 发送验证短信
import requests

from sj_cmfz.settings import API_KEY


class Yun_Pian(object):
    def __init__(self, api_key):
        self.api_key = api_key,
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone, code):
        parmas = {
            'apikey': self.api_key,
            'mobile': phone,
            'text': f'【善杰test】正在进行登录操作，您的验证码是{code}'
        }
        request = requests.post(self.single_send_url, data=parmas)
        print(request)


if __name__ == '__main__':
    yun_pian = Yun_Pian(API_KEY)
    yun_pian.send_message("15234958824", "256385")
