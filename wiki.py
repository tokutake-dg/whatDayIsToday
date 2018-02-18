# coding:utf-8
import wikipedia
import datetime

now = datetime.datetime.today()

wikipedia.set_lang("jp")
todayData = wikipedia.page(now.strftime("%-m月%-d日"))

print(todayData.content)
