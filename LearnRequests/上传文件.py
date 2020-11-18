"""
上传文件，一般都是post接口，用files参数上传文件
"""

import requests

url = "http://www.httpbin.org/post"

# files参数，字典格式，’name‘: file-tuple
# file-tuple可以是2-tuple，3-tuple，4-tuple

with open("d:/test.txt", encoding='utf-8') as f:
    # ,text/plain 如果上传的是一个文本文件，可以去掉content_type，默认文件是文本类型
    file = {"file1": ("test.txt", f, "text/plain")}  # MIME类型text/plain，image/png，image/gif application/json
    r = requests.post(url, files=file)
    print(r.text)
# \u206c\u4f60\u597d  unicode编码，网上有unicode转中文的小工具，可以在线转
# 上传图片，10k以内
with open("d:/abc.png", mode='rb') as f:
    file = {"file1": ("abc.png", f, "image/png")}
    r = requests.post(url, files=file)
    print(r.text)

# 一次可以上传多个文件
with open("d:/abc.png", mode='rb') as f:
    with open("d:/test.txt", encoding="utf-8") as w:
        file = {"file1": ("abc.png", f, "image/png"), "file2": ("test.txt", w, "text/plain")}
        r = requests.post(url, files=file)
        print(r.text)
