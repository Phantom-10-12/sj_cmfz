# 生成随机验证码

class Captcha(object):
    # 生成随机验证码
    def create_code(self):
        import random
        code = ""
        for i in range(6):
            code += str(random.randint(0, 9))
        return code

    # 将手机号与验证码存入redis
    def save_code(self, phone, code):
        from redis import Redis
        import time
        time = time.time()
        redis = Redis(host='123.57.70.140', port=6379)
        info = {"phone": phone, "code": code, "time": time}
        redis.set(phone, info)

    # 获取redis中的手机号0的验证码
    def get_code(self, phone):
        from redis import Redis
        redis = Redis(host='123.57.70.140', port=6379)
        info = redis.get(phone)
        print(info)


if __name__ == '__main__':
    captcha = Captcha()
    captcha.save_code(15234958824,123456)
    # captcha.get_code(15234958824)
