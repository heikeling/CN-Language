import tkinter as tk
import tkinter as tk
import time
import easygui as g
from tkinter import *
import re
import requests
import tkinter
from tkinter import filedialog
import traceback
win = tk.Tk()
win.title("Cn for windows")
put=tk.Text()
put.pack()
class main():
        def yx():
        
            f = open("code.txt")
            
            codes=f.read()
            def 打印(txt,color='black'):
                        global textMess
                        if put != None :
                            if put!='black':
                                put.tag_config(color, foreground=color)   
                            put.insert(tk.END, txt,color)
                            put.see(tk.END)
            try:
                if "询问"in codes:
                    codes=codes.replace("询问","g.enterbox")
                if "否则如果"in codes:
                    codes=codes.replace("否则如果","elif")
                if "如果"in codes:
                    codes=codes.replace("如果","if")
                if "否则"in codes:
                    codes=codes.replace("那么","else")
                if "导入库 "in codes:
                    codes=codes.replace("导入库 ","import ")
                if "创建界面"in codes:
                    codes=codes.replace("创建界面","tk.Tk()")
                if "标题"in codes:
                    codes=codes.replace("标题","title")
                if "大小"in codes:
                    codes=codes.replace("大小","geometry")
                if "显示按钮"in codes:
                    codes=codes.replace("显示按钮","tk.Button")
                if "显示文字"in codes:
                    codes=codes.replace("显示文字","tk.Label")
                if "输入框"in codes:
                    codes=codes.replace("输入框","tk.Entry")
                if "保持窗口"in codes:
                    codes=codes.replace("保持窗口","mainloop()")
                if "弹出"in codes:
                    codes=codes.replace("弹出","g.msgbox")
                if "条件循环"in codes:
                    codes=codes.replace("弹出","while")
                if "变量循环"in codes:
                    codes=codes.replace("变量循环","for")
                if "里面"in codes:
                    codes=codes.replace("里面","in")
                if "和"in codes:
                    codes=codes.replace("和","and")
                if "整数型"in codes:
                    codes=codes.replace("整数型","int")
                if "字符型"in codes:
                    codes=codes.replace("字符型","str")
                if "浮点型"in codes:
                    codes=codes.replace("浮点型","float")
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
                if "再次编译"in codes:
                    codes=codes.replace("再次编译","exec")
                if "获取值"in codes:
                    codes=codes.replace("获取值",'get')
                if "多行文本框"in codes:
                    codes=codes.replace("多行文本框",'tk.Text')
                if "设置操作"in codes:
                    codes=codes.replace("设置操作",'config')
                with open("new.py","w")as fp:
                    fp.write(codes)
                exec(codes)
                print(f.read())
            except (Exception, BaseException) as e:
                def colorprint(txt,color='black'):
                        global textMess
                        if put != None :
                            if put!='black':
                                put.tag_config(color, foreground=color)   
                            put.insert(tk.END, txt,color)
                            put.see(tk.END)
                
                e=str(e)
                colorprint("代码报错，终止运行\n"+e+"\n",'red')
main.yx()
win.mainloop()
