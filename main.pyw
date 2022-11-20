# coding=utf-8
# main.pyw
'''
作者微信:18038128007
禁止侵权
'''
import os
from platform import win32_edition
import Wdata
import pygame
import sys
import tkinter as tk
import time
import easygui as g
from tkinter import *
import traceback
import tkinter
import qrcode
import re
from tkinter.constants import *
import pyautogui
import requests
import tkinter
import 随机
from playsound import playsound
from tkinter import filedialog
from ku import *
import json
import re
def use():
    def translator(str):
        """
        input : str 需要翻译的字符串
        output：translation 翻译后的字符串
        """
        # API
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # 传输的参数， i为要翻译的内容
        key = {
            'type': "AUTO",
            'i': str,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        # key 这个字典为发送给有道词典服务器的内容
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        if response.status_code == 200:
            # 通过 json.loads 把返回的结果加载成 json 格式
            result = json.loads(response.text)
    #         print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
    #         print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
            translation = result['translateResult'][0][0]['tgt']
            return translation
        else:
            print("有道词典调用失败")
            # 相应失败就返回空
            return None
    """有道翻译函数  DONE!"""
    try:
        def rg():
            code.insert(INSERT,"果")
        class youjian():
                #复制功能函数
            def copy():
                global content
                content=code.get(SEL_FIRST,SEL_LAST)
                print("复制完成")
                return content
            #剪切函数
            def cut():
                global content
                content=code.get(SEL_FIRST,SEL_LAST)
                code.delete(SEL_FIRST,SEL_LAST)
                print("剪切完成")
                return content
                #粘贴功能函数
            def paste():
                    code.insert(INSERT,content)
                    print("粘贴完成")
            def backout():
                code.edit_undo()
            def regain():
                code.edit_redo()
        def popupmenu(event):
            menu.post(event.x_root, event.y_root)
        def opens():
            filename=filedialog.askopenfilename()
            f=open(filename,'r')
            f2=f.read()
            f.close()
            code.insert(INSERT,f2)
        def file():
            filename=filedialog.asksaveasfilename(filetypes=[("CN",".cn")])
            with open(filename+'.cn','w') as f:
                f.write(code.get('1.0','end'))
        def qk():
            code.delete(1.0, tk.END)
        def de():
            put.delete(1.0,tk.END)
        yan=requests.get("https://v.api.aa1.cn/api/yiyan/index.php")
        r=yan.text
        r=r.strip('''<div style="display:none"><iframe src="http://random-api-suiji.aa1.cn/map/map.php" width="100%" height="100%" frameborder="0"></iframe>
</div><p>''')
        def colorprint(txt,color='black'):
                global textMess
                if put != None :
                    if put!='black':
                        put.tag_config(color, foreground=color)   
                    code.insert(tk.END, txt,color)
                    code.see(tk.END)
        def yx():
            global 显示文字
            global 打印
            global 询问
            global 弹出
            global 创建界面
            global 大小
            global 标题
            global 显示按钮
            global 字符型
            global 浮点型
            global 整数型
            global 多行文本框
            global 再次编译
            def colorprint(txt,color='black'):
                global textMess
                if put != None :
                    if put!='black':
                        put.tag_config(color, foreground=color)   
                    put.insert(tk.END, txt,color)
                    put.see(tk.END)
            def 打印(txt,color='black'):
                global textMess
                if put != None :
                    if put!='black':
                        put.tag_config(color, foreground=color)   
                    put.insert(tk.END, txt,color)
                    put.see(tk.END)
            def 询问(put):
                a=g.enterbox(put)
                return a
            def 创建界面():
                return tk.Tk()
            def 弹出(msg):
                return g.msgbox(msg)
            def 显示按钮(对象,文本,函数=None):
                return tk.Button(对象,text=文本,command=函数)
            def 显示文字(对象,文本,样式=None):
                return tk.Label(对象,text=文本,font=样式)
            def 字符型(bl):
                return str(bl)
            def 浮点型(参数):
                return float(参数)
            def 整数型(参数):
                return int(参数)
            def 再次编译(execs):
                return exec(execs)
            def 输入框(对象):
                return tk.Entry(对象)
            start=time.time()
            c=code.get('1.0','end')
            with open('code.txt',"w")as f:
                f.write(c)
            f = open("code.txt")
            codes=f.read()
            try:
                if "否则如果"in codes:
                    codes=codes.replace("否则如果","elif")
                if "列表"in codes:
                    codes=codes.replace("列表","list")
                if "否则"in codes:
                    codes=codes.replace("否则","else")
                if "标题"in codes:
                    codes=codes.replace("标题","title")
                if "大小"in codes:
                    codes=codes.replace("大小","geometry")
                if "如果"in codes:
                    codes=codes.replace("如果","if")
                if "导入库 "in codes:
                    codes=codes.replace("导入库 ","import ")
                if "条件循环"in codes:
                    codes=codes.replace("弹出","while")
                if "变量循环"in codes:
                    codes=codes.replace("变量循环","for")
                if "里面"in codes:
                    codes=codes.replace("里面","in")
                if "画布"in codes:
                    codes=codes.replace("画布","Canvas")
                if "和"in codes:
                    codes=codes.replace("和","and")
                if "定义"in codes:
                    codes=codes.replace("定义","def")
                if "打破"in codes:
                    codes=codes.replace("打破","break")
                if "创建类"in codes:
                    codes=codes.replace("创建类","class")
                if "一起"in codes:
                    codes=codes.replace("一起","with")
                if "打开"in codes:
                    codes=codes.replace("打开","open")
                if "退出"in codes:
                    codes=codes.replace("退出","quit")
                if "监听"in codes:
                    codes=codes.replace("监听","bind")
                if "从"in codes:
                    codes=codes.replace("从","from")
                if "看作"in codes:
                    codes=codes.replace("看作","as")
                if "返回值"in codes:
                    codes=codes.replace("返回值","return")
                if "写入"in codes:
                    codes=codes.replace("写入","write")
                if "尝试"in codes:
                    codes=codes.replace("尝试","try")
                if "报错"in codes:
                    codes=codes.replace("报错","except")
                if "（"in codes:
                    codes=codes.replace("（","(")
                if "）"in codes:
                    codes=codes.replace("）",")")
                if "，"in codes:
                    codes=codes.replace("，",",")
                if "："in codes:
                    codes=codes.replace("：",":")
                if "获取值"in codes:
                    codes=codes.replace("获取值",'get')
                if "窗口插入文本"in codes:
                    codes=codes.replace("窗口插入文本",'insert')
                if "多行文本框"in codes:
                    codes=codes.replace("多行文本框",'tk.Text')
                if "主菜单"in codes:
                    codes=codes.replace("主菜单",'add_cascade')
                if "创建菜单"in codes:
                    codes=codes.replace("创建菜单",'Menu')
                if "菜单内容"in codes:
                    codes=codes.replace("菜单内容",'add_command')
                if "设置操作"in codes:
                    codes=codes.replace("设置操作",'config')
                end=time.time()
                t=end-start
                t=str(t)
                put.insert(INSERT,"用时"+t+"\n")
                with open("new.py","w")as fp:
                    fp.write(codes)
                exec(codes)
                print(f.read())
            except (Exception, BaseException) as e:
                e=str(e)
                baoc=translator(e)
                colorprint("代码报错，终止运行\n"+baoc+"\n",'red')
        def yxf5(event):
            global 显示文字
            global 打印
            global 询问
            global 弹出
            global 创建界面
            global 大小
            global 标题
            global 显示按钮
            global 字符型
            global 浮点型
            global 整数型
            global 多行文本框
            global 再次编译
            def colorprint(txt,color='black'):
                global textMess
                if put != None :
                    if put!='black':
                        put.tag_config(color, foreground=color)   
                    put.insert(tk.END, txt,color)
                    put.see(tk.END)
            def 打印(txt,color='black'):
                global textMess
                if put != None :
                    if put!='black':
                        put.tag_config(color, foreground=color)   
                    put.insert(tk.END, txt,color)
                    put.see(tk.END)
            def 询问(put):
                a=g.enterbox(put)
                return a
            def 创建界面():
                return tk.Tk()
            def 弹出(msg):
                return g.msgbox(msg)
            def 显示按钮(对象,文本,函数=None):
                return tk.Button(对象,text=文本,command=函数)
            def 显示文字(对象,文本,样式=None):
                return tk.Label(对象,text=文本,font=样式)
            def 字符型(bl):
                return str(bl)
            def 浮点型(参数):
                return float(参数)
            def 整数型(参数):
                return int(参数)
            def 再次编译(execs):
                return exec(execs)
            def 输入框(对象):
                return tk.Entry(对象)
            start=time.time()
            c=code.get('1.0','end')
            with open('code.txt',"w")as f:
                f.write(c)
            f = open("code.txt")
            codes=f.read()
            try:
                if "否则如果"in codes:
                    codes=codes.replace("否则如果","elif")
                if "否则"in codes:
                    codes=codes.replace("否则","else")
                if "标题"in codes:
                    codes=codes.replace("标题","title")
                if "大小"in codes:
                    codes=codes.replace("大小","geometry")
                if "如果"in codes:
                    codes=codes.replace("如果","if")
                if "导入库 "in codes:
                    codes=codes.replace("导入库 ","import ")
                if "条件循环"in codes:
                    codes=codes.replace("弹出","while")
                if "变量循环"in codes:
                    codes=codes.replace("变量循环","for")
                if "里面"in codes:
                    codes=codes.replace("里面","in")
                if "和"in codes:
                    codes=codes.replace("和","and")
                if "定义"in codes:
                    codes=codes.replace("定义","def")
                if "打破"in codes:
                    codes=codes.replace("打破","break")
                if "创建类"in codes:
                    codes=codes.replace("创建类","class")
                if "一起"in codes:
                    codes=codes.replace("一起","with")
                if "打开"in codes:
                    codes=codes.replace("打开","open")
                if "退出"in codes:
                    codes=codes.replace("退出","quit")
                if "从"in codes:
                    codes=codes.replace("从","from")
                if "看作"in codes:
                    codes=codes.replace("看作","as")
                if "返回值"in codes:
                    codes=codes.replace("返回值","return")
                if "写入"in codes:
                    codes=codes.replace("写入","write")
                if "尝试"in codes:
                    codes=codes.replace("尝试","try")
                if "报错"in codes:
                    codes=codes.replace("报错","except")
                if "（"in codes:
                    codes=codes.replace("（","(")
                if "）"in codes:
                    codes=codes.replace("）",")")
                if "，"in codes:
                    codes=codes.replace("，",",")
                if "："in codes:
                    codes=codes.replace("：",":")
                if "获取值"in codes:
                    codes=codes.replace("获取值",'get')
                if "窗口插入文本"in codes:
                    codes=codes.replace("窗口插入文本",'insert')
                if "多行文本框"in codes:
                    codes=codes.replace("多行文本框",'tk.Text')
                if "主菜单"in codes:
                    codes=codes.replace("主菜单",'add_cascade')
                if "创建菜单"in codes:
                    codes=codes.replace("创建菜单",'Menu')
                if "菜单内容"in codes:
                    codes=codes.replace("菜单内容",'add_command')
                if "设置操作"in codes:
                    codes=codes.replace("设置操作",'config')
                end=time.time()
                t=end-start
                t=str(t)
                put.insert(INSERT,"用时"+t+"\n")
                with open("new.py","w")as fp:
                    fp.write(codes)
                exec(codes)
                print(f.read())
            except (Exception, BaseException) as e:
                e=str(e)
                baoc=translator(e)
                colorprint("代码报错，终止运行\n"+baoc+"\n",'red')
        def api():
            url=g.enterbox("需要的API:获取用户资料\n请输入用户")
            r=requests.get('https://api.github.com/users/'+url)
            g.msgbox(r.text)
        def by():
            c=code.get('1.0','end')
            with open('code.txt',"w")as f:
                f.write(c)
            lj=g.enterbox("输出目录")
            os.system("xcopy Cnexe.exe "+lj)
            os.system("xcopy code.txt "+lj)
        def git():
            git=g.enterbox("请确认git环境\n输入下载地址")
            if git==None:
                pass
            elif git=="":
                pass
            else:
                os.system("git clone "+git)
        global code
        win = tk.Tk()
        imgBtn = tk.PhotoImage(file='./icon/ico_run.png')
        imgBtn1 = tk.PhotoImage(file='./icon/ico_new.png')
        imgBtn2 = tk.PhotoImage(file='./icon/ico_save.png')
        imgBtn3 = tk.PhotoImage(file='./icon/git.png')
        btnyx=tk.Button(image=imgBtn,command=yx)
        btnyx.place(x=0,y=0)
        btnnew=tk.Button(image=imgBtn1,command=qk)
        btnnew.place(x=55,y=0)
        btnsave=tk.Button(image=imgBtn2,command=file)
        btnsave.place(x=110,y=0)
        btngit=tk.Button(image=imgBtn3,command=git)
        btngit.place(x=0,y=600)
        win.iconbitmap('./icon/ico.ico')
        win.title("Cn-可视化中文编程")
        win.geometry("1000x700")
        put = tk.Text(win, height=20, width=100)
        put.place(x=100, y=400)
        code=tk.Text(win,height=20,width=100)
        code.place(x=100,y=50)

        put.insert(INSERT,"输出框\n")
        code.config(bg='skyblue')
        code.bind("<Button-3>", popupmenu)
        win.config(bg="gray")
        menubar = Menu(win)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='文件', menu=filemenu)
        filemenu.add_command(label='打开', command=opens)
        filemenu.add_command(label='保存', command=file)
        filemenu.add_command(label='新文件', command=qk)
        filemenu.add_command(label='清空输出框', command=de)
        win.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='编译', menu=filemenu)
        filemenu.add_command(label='编译exe', command=by)
        filemenu.add_command(label='运行 F5', command=yx)
        win.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        def cmd():
            os.system("cmd")
        menubar.add_cascade(label='终端', menu=filemenu)
        filemenu.add_command(label='新建终端', command=cmd)
        filemenu.add_command(label='git', command=git)
        filemenu.add_command(label='github-api', command=api)
        win.config(menu=menubar)
        def fs():
            win.config(bg="pink")
        def ls():
            win.config(bg="blue")
        def hf():
            win.config(bg='gray')
        def py():
            ljj=g.enterbox("扩展位置")
            if ljj==None:
                pass
            elif ljj=="":
                pass
            else:
                os.system("xcopy "+ljj+" ")
        def d():
            ljjj=g.enterbox("扩展名称")
            if ljjj==None:
                pass
            elif ljjj=="":
                pass
            else:
                os.system("del "+ljjj)
                g.msgbox("删除完毕")
        def scr():
            g.msgbox("加微信:18038128007")
        def jx():
            code.insert(INSERT,'''从 web 导入库 *
win=创建界面
win.标题('视频解析器')
win.大小('500x300')
e=输入框(win).pack()
定义 jx():
	url=e.get()
	start网页('https://okjx.cc/?url='+url)
显示按钮(win,text='开始解析',command=jx).pack()''')
        def jsq():
            code.insert(INSERT,'''加数1=询问("加数1")
加数2=询问("加数2")
加数1=整数型(加数1)
加数2=整数型(加数2)
弹出(加数1+加数2)''')
        def dlj():
            code.insert(INSERT,'''登录=创建界面()
登录.标题("登录界面")
登录.大小('240x100')
文本=显示文字(登录,'登录')
文本2=显示文字(登录,'用户名')
文本2.place(x=0,y=0)
输入框1=输入框(登录)
输入框1.place(x=40,y=0)
文本3=显示文字(登录,'密码')
文本3.place(x=0,y=30)
输入框2=输入框(登录)
输入框2.place(x=40,y=30)
按钮=显示按钮(登录,'登录')
按钮.place(x=100,y=60)''')
        def cq():
            code.insert(INSERT,'''从 随机 导入库 *
电脑猜拳=生成随机数(1,3)
玩家=询问（'请输入猜拳'）
如果 玩家 == '石头' 和 电脑猜拳 == 1：
	打印（'平局啦','blue'）
否则如果 玩家 == '石头' 和 电脑猜拳 == 2：
	打印（'你赢啦','green'）
否则如果 玩家 == '石头' 和 电脑猜拳 == 3：
	打印（'很遗憾，你输了'，'red'）
否则如果 玩家 == '剪刀' 和 电脑猜拳 == 1：
	打印（'很遗憾，你输了'，'red'）
否则如果 玩家 == '剪刀' 和 电脑猜拳 == 2：
	打印（'平局啦','blue'）
否则如果 玩家 == '剪刀' 和 电脑猜拳 == 3：
	打印（'你赢啦','green'）
否则如果 玩家 == '布' 和 电脑猜拳 == 1：
	打印（'你赢啦','blue'）
否则如果 玩家 == '布' 和 电脑猜拳 == 2：
	打印（'很遗憾，你输了'，'red'）
否则如果 玩家 == '布' 和 电脑猜拳 == 3：
	打印（'平局啦'，'green'）''')
        def csz():
            code.insert(INSERT,'''从 随机 导入库 *
a=询问("最大数")
b=询问("最小数")
a=整数型(a)
b=整数型(b)
c=生成随机数(b,a)
while(True):
	d=询问("你所猜的数")
	d=整数型(d)
	如果 d == c:
		弹出("答对了")
		打破
	否则如果 d > c:
		弹出("太大了")
	否则如果 d < c:
		弹出("太小了")''')
        def pq():
            code.insert(INSERT,'''从 请求 导入库 *
url=询问("需要爬取的网页")
code=请求网页("get",url)
弹出(code.text)''')
        def wl():
            code.insert(INSERT,'''#网页生成二维码实例
#需要自行下载扩展网页二维码库
从 网页二维码 导入库 *
url("https://www.baidu.com")
保存路径("C:\\Users\\用户名\\Desktop")''')
        def kh(event):
            code.insert(INSERT,")")
            pyautogui.press("left",1)
        def ds(event):
            code.insert(INSERT,"'")
            pyautogui.press("left",1)
        def di(event):
            code.insert(INSERT,".")
        def dw(event):
            code.insert(INSERT,'"')
            pyautogui.press("left",1)
        def xm():
            ll=g.enterbox("路径")
            if ll == None:
                pass
            elif ll == "":
                pass
            else:
                os.system("xcopy main.cn "+ll)
                os.system("xcopy cndll.py "+ll)
        def dl():
            audio_path = 'https://sr-sycdn.kuwo.cn/2ad64275cbd4b287f8bc15f91d5b163d/63514b36/resource/n3/31/3/426812521.mp3'
            playsound(audio_path)
        def dy():
            os.system('start ./dy/douyin.exe')
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='个性化', menu=filemenu)
        filemenu.add_command(label='粉色皮肤', command=fs)
        filemenu.add_command(label='蓝色皮肤', command=ls)
        filemenu.add_command(label='恢复', command=hf)
        win.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='扩展', menu=filemenu)
        filemenu.add_command(label='添加扩展 *.py/*pyd', command=py)
        filemenu.add_command(label='云端扩展商城 *.py/*pyd', command=ku)
        filemenu.add_command(label='删除扩展', command=d)
        filemenu.add_command(label='上传自己的扩展', command=scr)
        win.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='创建项目', menu=filemenu)
        filemenu.add_command(label='创建项目', command=xm)
        win.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='休闲', menu=filemenu)
        filemenu.add_command(label='单曲 达拉崩吧', command=dl)
        win.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='实例项目', menu=filemenu)
        filemenu.add_command(label='加法计算器', command=jsq)
        filemenu.add_command(label='爬虫网页源码', command=pq)
        filemenu.add_command(label='猜数字', command=csz)
        filemenu.add_command(label='网页转二维码', command=wl)
        filemenu.add_command(label='vip视频解析', command=jx)
        filemenu.add_command(label='猜拳', command=cq)
        filemenu.add_command(label='登录', command=dlj)
        win.config(menu=menubar)
        menu = tk.Menu(win, tearoff=0)
        menu.add_command(label="复制", command=youjian.copy)
        menu.add_command(label="粘贴", command=youjian.paste)
        menu.add_command(label="剪切", command=youjian.cut)
        menubar = Menu(win)
        menu.add_command(label="撤销", command=youjian.backout)
        menubar = Menu(win)
        menu.add_command(label="重做", command=youjian.regain)
        menubar = Menu(win)
        code.tag_config('failed', foreground='red')
        code.tag_config('passed', foreground='blue')
        code.tag_config('t', foreground='green')

        def search(text_widget, keyword, tag):
            pos = '1.0'
            while True:
                idx = text_widget.search(keyword, pos, END)
                if not idx:
                    break
                pos = '{}+{}c'.format(idx, len(keyword))
                text_widget.tag_add(tag, idx, pos)
        def test(event):
            search(code, '导入库', 'failed')
            search(code, '变量循环', 'failed')
            search(code, 'while', 'failed')
            search(code, 'len', 'failed')
            search(code, '从', 'passed')
            search(code, '如果', 'passed')
            search(code, '打印', 'failed')
            search(code, '否则如果', 'passed')
            search(code, '否则', 'passed')
            search(code, '整数型', 't')
            search(code, '字符型', 't')
            search(code, '浮点型', 't')
            search(code, '弹出', 'failed')
            search(code, '打破', 'failed')
            search(code, '询问', 'failed')
            search(code, 'True', 't')
            search(code, 'False', 't')
            search(code, '创建界面', 'failed')
            search(code, '创建类', 'failed')
            search(code, '定义', 'failed')
            search(code, '看作', 't')
            search(code, '尝试', 't')
            search(code, '写入', 't')
            search(code, '返回值', 't')
            search(code, '报错', 't')
            search(code, '一起', 't')
            search(code, '打开', 't')
            search(code, '退出', 't')
            search(code, '显示按钮', 'passed')
            search(code, '显示文字', 'passed')
            search(code, '标题', 'passed')
            search(code, '大小', 'passed')
            search(code, '输入框', 't')
            search(code, 'pack', 't')
            search(code, 'place', 't')
            search(code, '和', 't')
            search(code, '里面', 't')
            search(code, '重新编译', 'failed')
            search(code, '多行文本框', 'failed')
            search(code, '获取值', 'failed')
            search(code, '设置操作', 'failed')
            search(code, '窗口插入文本', 't')
            search(code, '主菜单', 't')
            search(code, '菜单内容', 't')
            search(code, '创建菜单', 't')
        code.bind('<Key>',test)
        win.bind("(",kh)
        win.bind("'",ds)
        win.bind('"',dw)
        def blog():
            os.system("start https://heikeling.cnblogs.com")
        btnweb=tk.Button(win,text="我的博客",command=blog)
        btnweb.pack()
        put.insert(INSERT,r+"\n")
        win.bind("<F5>",yxf5)

        win.mainloop()
    except (Exception, BaseException) as e:
        g.msgbox("无法启动，原因"+str(e))
use()
