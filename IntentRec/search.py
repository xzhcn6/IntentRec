# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from configs import intent_predict, intent_list
from DataModel import models

# 接收POST请求数据
def search_post(request):
    result = 0
    sentence = request.POST['sentence']

    sentence = str(sentence).replace(' ', '').replace('\n', '')

    print("/miniconda3/envs/py3/bin/python "+intent_predict+' '+sentence)
    result = os.popen("/miniconda3/envs/py3/bin/python "+intent_predict+' '+sentence).readlines()

    print(result)
    if len(result):
        tmp = result[-1].split('|')[0]
        if tmp in intent_list:
            context = {'sentence': result[-1], 'flag': 1}
        else:
            context = {'sentence': "您查询的问题太复杂啦！", 'flag': 0}
    else:
        context = {'sentence': "您查询的问题太复杂啦！", 'flag': 0}
    return HttpResponse(json.dumps(context), content_type="application/json")
    #return render(request, 'recognition.html', context)

# 接收POST请求数据
def add_intent(request):
    sentence = request.POST['sentence']
    typeid = request.POST['typeid']
    authorname = request.POST['authorname']
    verifycode = request.POST['verifycode'].lower()
    value = request.session.get("verCode")

    context = {}
    if verifycode != value.lower():
        context = {'response': "验证码错误!！"}
    if sentence.strip() =='':
        context = {'response': "请输入您想做的事情!！"}
    types = models.Type.objects.filter(id=typeid.strip())
    if len(types) == 0:
        context = {'response': "请输入正确的意图类型的ID!！"}

    import datetime
    intent = models.Intent.objects.create(i_type=types[0], content=sentence, author=authorname, create_date=datetime.datetime.now())
    print(type(intent))
    if type(intent) != models.Intent:
        context = {'response': "提交失败，请重试!！"}
    else:
        context = {'response': "提交成功，感谢您的支持!！"}

    return HttpResponse(json.dumps(context), content_type="application/json")
    #return render(request, 'recognition.html', context)

# 随机颜色的生成
def createcolor():
    import random
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


def getVerificationCode(request):
    # 创建画布
    # mode  模式,"RGB"
    # size  画布的尺寸
    from PIL import Image
    from PIL import ImageDraw, ImageFont
    import random

    image = Image.new("RGB", (200, 70), createcolor())
    imageDraw = ImageDraw.Draw(image, "RGB")
    imageFont = ImageFont.truetype("static/adobearabic-italic.otf", size=50)
    # imageDraw.text((5,10),"i love you!",fill=createcolor(),font=imageFont)
    import io
    charsource = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    #charsource = "qwertyuiopasdfghjklzxcvbnm1234567890"
    sum = ""
    for i in range(4):
        ch = random.choice(charsource)
        imageDraw.text((15 + i * 50, 10), ch, fill=createcolor(), font=imageFont)
        sum += ch
    # 通过session记录这个验证码并且设置过期时间为60秒
    request.session["verCode"] = sum
    request.session.set_expiry(60)
    # 画麻子
    for i in range(2000):
        x = random.randint(0, 200)
        y = random.randint(0, 70)
        imageDraw.point((x, y), fill=createcolor())

    # 创建一个字节流
    byteIO = io.BytesIO()
    # 把图片放在字节流里面去
    image.save(byteIO, "png")
    return HttpResponse(byteIO.getvalue(), "image/png")