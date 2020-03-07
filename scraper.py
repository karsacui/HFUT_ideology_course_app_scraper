# -*- encoding=utf8 -*-
__author__ = "karsacui"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#总词典
all_questions = {}

dict2 = {}
while True:
    #扫描屏幕中的元素
    result_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.jqorz.szk:id/mRecyclerView").child("android.widget.FrameLayout")

    for result in result_obj:
        #暂存词典
        dict = {}
        #检查序列号是否存在，不存在就跳过
        if result.child("android.widget.LinearLayout").child("android.widget.LinearLayout").child(name='com.jqorz.szk:id/tv_Question_Serial'):
            serial = result.child("android.widget.LinearLayout").child("android.widget.LinearLayout").child(name='com.jqorz.szk:id/tv_Question_Serial').get_text()
        else:
            continue
        #检查问题是否存在，不存在就跳过
        if result.child("android.widget.LinearLayout").child("android.widget.LinearLayout").child(name='com.jqorz.szk:id/tv_Question_Content'):
            question = result.child("android.widget.LinearLayout").child("android.widget.LinearLayout").child(name='com.jqorz.szk:id/tv_Question_Content').get_text()
            dict['question'] = question
        else:
            continue
        if result.offspring("com.jqorz.szk:id/lv_OpinionA"):
            dict['A'] = result.offspring("com.jqorz.szk:id/lv_OpinionA").child(name='com.jqorz.szk:id/tv_OpinionA_Content').get_text()
        if result.offspring("com.jqorz.szk:id/lv_OpinionB"):
            dict['B'] = result.offspring("com.jqorz.szk:id/lv_OpinionB").child(name='com.jqorz.szk:id/tv_OpinionB_Content').get_text()
        if result.offspring("com.jqorz.szk:id/lv_OpinionC"):
            dict['C'] = result.offspring("com.jqorz.szk:id/lv_OpinionC").child(name='com.jqorz.szk:id/tv_OpinionC_Content').get_text()
        if result.offspring("com.jqorz.szk:id/lv_OpinionD"):
            dict['D'] = result.offspring("com.jqorz.szk:id/lv_OpinionD").child(name='com.jqorz.szk:id/tv_OpinionD_Content').get_text()
        #检查答案是否存在，不存在就跳过
        if result.offspring("com.jqorz.szk:id/tv_Answer_Content"):
            answer = result.offspring("com.jqorz.szk:id/tv_Answer_Content").get_text()
            dict['answer'] = answer
        else:
            continue 
        print(serial, dict)
        #存储入总词典
        all_questions[serial] = dict
    if dict == dict2 and dict != {}:
        print(dict,dict2)
        break
    dict2 = dict
    poco.swipe([0.5, 0.8], [0.5, 0.2])
    
print(all_questions)
    
