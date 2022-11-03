import os
def 终端执行(z):
    os.system(z)
def 终端执行获取返回(z):
    result = os.popen(z)
    res = result.read()
    return res