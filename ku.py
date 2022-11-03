import tkinter as tk
import requests
import easygui as g
def ku():
    k=tk.Toplevel()
    k.iconbitmap("./icon/favicon.ico")
    k.title("下载CN所需库")
    k.geometry("500x300")
    def xs():
        a=requests.get("https://heikeling.github.io/xiaoshicn.py")
        with open('xiaoshicn.py','wb')as f:
            f.write(a.content)
        g.msgbox("下载完成")
    def we():
        a=requests.get("https://heikeling.github.io/web.py")
        with open('web.py','wb')as f:
            f.write(a.content)
        g.msgbox("下载完成")
    def w():
        a=requests.get("https://heikeling.github.io/api图形码.py")
        with open('api图形码.py','wb')as f:
            f.write(a.content)
        g.msgbox("下载完成")
    def wz():
        a=requests.get("https://heikeling.github.io/网页二维码.py")
        with open('网页二维码.py','wb')as f:
            f.write(a.content)
        g.msgbox("下载完成")
    lb=tk.Label(k,text="引用方法:输入 导入库 某某库名").pack()
    btn=tk.Button(k,text="下载小诗编程提供的xiaoshicn库",command=xs).pack()
    btn=tk.Button(k,text="下载Cn开发者提供的web库(网页控制)",command=we).pack()
    btn=tk.Button(k,text="下载Cn开发者提供的api图形码库(api接口图形验证码)",command=w).pack()
    btn=tk.Button(k,text="下载Cn开发者提供的网页二维码库(网址生成二维码)",command=wz).pack()
    k.mainloop()
if __name__ == "__main__":
    ku()