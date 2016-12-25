#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import random
from PIL import Image
from io import BytesIO
import GUIHelper

class BookHelper:

    # Constants

    rootUrl = "https://www.12306.cn"

    def get_login_captcha_url(self):
        rand = random.uniform(0,1)
        return "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&" + str(rand)

    checkCaptchaUrl = "https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn"
    loginUrl = "https://kyfw.12306.cn/otn/login/loginAysnSuggest"

    #

    s = requests.session()
    captcha_points = []

    def __init__(self):
        self.s.get(self.rootUrl)

    def login(self, username, pwd):
        r = self.s.get(self.get_login_captcha_url(self), verify=False)
        gui = GUIHelper.GUIHelper(self, self.set_point, self.login_call_back, Image.open(BytesIO(r.content)))

    def login_call_back(self):
        print("login call backed")

    def set_point(self, x, y):
        self.captcha_points.append(x)
        self.captcha_points.append(y)
        print(self.captcha_points)

test = BookHelper
test.login(test, username="aa", pwd="aa");
