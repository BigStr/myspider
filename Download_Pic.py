# encoding: utf-8
from urllib2 import urlopen
from pymongo import MongoClient

# 抽取出照片的网址，下载，保存在pic文件夹中
def downPic():
    client = MongoClient()
    db = client.TaoBao 
    col = db.TaoLady
    for data in col.find(no_cursor_timeout = True):
	try:
                name = data['realName']
	        print(name)
		url = "http:" + data['avatarUrl']
        	pic = urlopen(url)
		print(url)
        	with open("pic/" + name + ".jpg", "wb") as file:
           		 file.write(pic.read())
	except:
		pass


if __name__ == '__main__':
    downPic()
