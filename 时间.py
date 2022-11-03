import time
def 获取当前时间():
    now=time.time()
    return now
def 获取当前时间元组():
    now=time.localtime()
    return now
def 获取格式化时间戳():
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    return now