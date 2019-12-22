# -*- encoding=utf8 -*-
__author__ = "Demax"


from airtest.core.api import *
import json 

#add path to json cfg where we add login and password
cfg = {}
with open('D:\Скрипты\data.cfg') as json_file: 
    cfg = json.load(json_file)

#import poco libs
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()

touch(Template(r"tpl1565111832904.png", record_pos=(0.369, 0.704), resolution=(1080, 1920)))

touch(Template(r"tpl1565111845059.png", record_pos=(-0.419, -0.192), resolution=(1080, 1920)))


#login and pw on client
poco("android.widget.LinearLayout").offspring("com.trassir.android.client.cn:id/cloud_editable_login").click()

text(cfg['login'])
text(cfg['password'])

touch(Template(r"tpl1565111873183.png", record_pos=(0.0, 0.137), resolution=(1080, 1920)))

touch(Template(r"tpl1565111900648.png", record_pos=(-0.42, -0.187), resolution=(1080, 1920)))

touch(Template(r"tpl1565111909376.png", record_pos=(0.001, 0.164), resolution=(1080, 1920)))

