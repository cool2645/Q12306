#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import random

class BookHelper:

    rootUrl = "https://www.12306.cn"

    def get_login_captcha_url(self):
        rand = random.uniform(0,1)
        return "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&" + str(rand)

    checkCaptchaUrl = "https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn"
    loginUrl = "https://kyfw.12306.cn/otn/login/loginAysnSuggest"

    s = requests.session()

    def __init__(self):
        self.s.get(self.rootUrl)

    def login(self, username, pwd):
        import GUIHelper

