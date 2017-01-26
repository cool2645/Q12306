# 春运抢票软件 2017

English version is [here](https://github.com/hudson6666/Q12306/wiki/README).

这个程序使用 Python 3.5.2 和 Pillow 3.4.2。

## 环境搭建

这里只以 Ubuntu 为例，其他操作系统请咨询发行版提供者。

```
sudo apt update
sudo apt install python3-dev python3-pip python3-tk
pip3 install Pillow==3.4.2
cp Q12306.cfg.example Q12306.cfg
cp Q12306.json.example Q12306.json
# 编辑配置文件
# vim Q12306.cfg
# vim Q12306.json
python3 BookHelper.py
```

## 开发日志

这个程序还没开发好 = = 喜欢的拿去帮忙开发

2017.01.26 23 读取抢票配置文件，匹配待抢车次的信息  
2017.01.26 00 查询车站和车次信息  
2017.01.19 22 修复登陆提示系统繁忙的问题，现已可以成功登陆  
2016.12.25 15 完成登录但是一直系统繁忙 用浏览器没问题  
2016.12.25 12 完成验证码GUI和主程序通信  
2016.12.25 11 完成验证码GUI模块  
2016.12.24 16 创建项目  
