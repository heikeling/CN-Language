import tkinter
import tkinter.messagebox as msgbox
a="Cn"
def 消息弹窗(标题,内容):
    msgbox.showinfo(标题,内容)
def 警告弹窗(标题="",内容):
    msgbox.showwarning(标题,内容)
def 错误弹窗(标题="",内容):
    msgbox.showerror(标题,内容)
