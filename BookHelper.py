#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import random
import configparser
import time
import json
from PIL import Image, ImageFile
from io import BytesIO
ImageFile.LOAD_TRUNCATED_IMAGES = True
import GUIHelper

class BookHelper:

    # Constants

    rootUrl = "https://www.12306.cn"
    initUrl = "https://kyfw.12306.cn/otn/login/init"
    def get_login_captcha_url(self):
        rand = random.uniform(0,1)
        return "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&" + str(rand)

    checkCaptchaUrl = "https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn"
    loginUrl = "https://kyfw.12306.cn/otn/login/loginAysnSuggest"
    stationUrl = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
    queryTicketUrl = "https://kyfw.12306.cn/otn/leftTicket/queryZ"

    #

    s = requests.session()
    captcha_points = []
    captcha_str = ""
    stations = {}
    orders = []

    def __init__(self):
        self.s.get(self.initUrl, verify=False)
        self.get_stations()

    def login(self, username, pwd):

        while True:

            self.captcha_points = []
            self.captcha_str = ""

            # get captcha pic and show window
            r = self.s.get(self.get_login_captcha_url(), verify=False)
            gui = GUIHelper.GUIHelper(self.set_point, self.login_call_back, Image.open(BytesIO(r.content)))

            # validate captcha
            print("Is it async?")

            headers = {
                'Host' : 'kyfw.12306.cn',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Origin': 'https://kyfw.12306.cn',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://kyfw.12306.cn/otn/login/init',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'
            }
            data = {
                'randCode' : self.captcha_str,
                'rand' : 'sjrand'
            }
            r = self.s.post(self.checkCaptchaUrl, headers=headers, data=data)
            r_array = r.json()
            print(self.s.cookies)
            if r_array['data']['result'] == '1' :
                break

        time.sleep(1)

        # do login

        headers = {
            'Host': 'kyfw.12306.cn',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Origin': 'https://kyfw.12306.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://kyfw.12306.cn/otn/login/init',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'
        }
        data = {
            'loginUserDTO.user_name': username,
            'userDTO.password': pwd,
            'randCode' : self.captcha_str
        }
        r = self.s.post(self.loginUrl, headers=headers, data=data)
        print(r.json())
        print(self.s.cookies)


    def login_call_back(self):
        print("login call backed")
        self.captcha_str = ",".join(self.captcha_points)
        print(self.captcha_str)

    def set_point(self, x, y):
        self.captcha_points.append(str(x))
        self.captcha_points.append(str(y))
        print(self.captcha_points)

    def get_stations(self):
        ss = self.s.get(self.stationUrl, verify = False)
        ss = ss.text
        sss = ss[ss.index('@') + 1 : ss.index(';') - 1]
        stations = sss.split('@')
        for station in stations:
            tmp = station.split('|')
            self.stations[tmp[1]] = tmp[2]
        #print(self.stations)

    def query_ticket(self, fromStation, toStation, date, ppType):
        fromStation = self.stations[fromStation]
        toStation = self.stations[toStation]
        r = self.s.get(self.queryTicketUrl + "?leftTicketDTO.train_date=" + date + "&leftTicketDTO.from_station=" + fromStation + "&leftTicketDTO.to_station=" + toStation + "&purpose_codes=" + ppType)
        print(r.json())

    def get_profile(self, profile):
        profile_file = open(profile)
        try:
            p = profile_file.read()
        finally:
            profile_file.close()
        self.orders = json.loads(p)
        self.orders.sort(key=lambda order:order['order'])
        print(self.orders)

test = BookHelper()
config = configparser.ConfigParser()
config.read("Q12306.cfg")
username = config.get("user", "username")
password = config.get("user", "password")
profile = config.get("user", "profile")

test.get_profile(profile)
#test.login(username, password)
test.query_ticket("沈阳", "沈阳北", "2017-02-22", "ADULT")
