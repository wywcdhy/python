# 第一种方法 open ("filepath",'r')
# file.read()
# file.close()

# if __name__ == '__main__':
#     f = open('F:\\PythonCode\\Test1\\test2\\test.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()


# 方法二 with open("filepath","r") as f:
#     for line in f.readlines():
#         print(line)
# if __name__ == '__main__':
#     with open("F:\\PythonCode\\Test1\\test2\\test.txt","r",encoding='UTF-8') as f:
#         for line in f.readlines():
#             print(line)

# # 要读取二进制文件（例如图片、音频、视频）内容，使用rb模式打开：
# if __name__ == '__main__':
#
#     with open("C:\\Users\\Administrator\\Desktop\\1.png","rb") as f:
#         print(f.read())
# 读取大文件方法
# 方法一
import os
import pickle
import re
from datetime import datetime

import mysql.connector


def read_in_block(file_path):
    BLOCK_SIZE = 1024
    with open(file_path, "r", encoding='UTF-8', errors='ignore') as f:
        while True:
            block = f.read(BLOCK_SIZE)  # 每次读取固定长度到内存缓冲区
            if block:
                yield block
            else:
                return  # 如果读取到文件末尾，则退出


# if __name__ == '__main__':
#     for block in read_in_block("F:\\PythonCode\\Test1\\test2\\test.txt"):
#         print(block)
# # 方法二
#     with open('F:\\PythonCode\\Test1\\test2\\test.txt',encoding='utf-8') as f:
#         for line in f:
#             print(line)
# 大批量读取txt
def read_in_block1(filename):
    BLOCK_SIZE = 1024
    with open(filename, "r", encoding='utf-8', errors='ignore') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if not block:
                return
            else:
                yield block


def connect_to_mysql():
    # conn = mysql.connector.connect(user='root', password='123456', database='test')
    # cursor = conn.cursor()
    # cursor.execute("insert into user(id,name,age)values(null,'python', 20)")
    # print(cursor.rowcount)
    # conn.commit()
    # cursor.execute("select * from user order by id desc limit 3")
    # print(cursor.fetchall())
    # cursor.close()
    # conn.close
    conn = mysql.connector.connect(user='root', password='HE123456', database='test', host='119.91.23.180',
                                   port='3306')
    cursor = conn.cursor()
    cursor.execute('select * from users')
    print(cursor.fetchall())


if __name__ == '__main__':
    # print(os.path.abspath('.'))
    path = os.path.abspath('.')
    # new_path = os.path.join(path,'test.txt')
    # print(new_path)

    # L = [x for x in os.listdir('F:\\PythonCode') if os.path.isdir(x)]
    #
    # L2 = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
    # dirs = os.listdir('F:\\PythonCode')
    # print(dirs)
    # print(L)
    # print(L2)
    # print(path)
    # print(pickle.dumps(L2))
    # # 反序列化
    # L3 = pickle.dumps(L2)
    # print(pickle.loads(L3))
    # datetime1 = datetime.now()
    # ts = datetime1.timestamp()
    # print(datetime1.strftime('%Y-%m-%d %H:%M:%S'))
    # print(datetime1.timestamp())
    # print(datetime.fromtimestamp(ts))
    # print(datetime.utcfromtimestamp(ts))
    # datetime.fromtimestamp()  # 获取本地时间，datetime类型
    # datetime.utcfromtimestamp()  # 获取UTC时间，datetime类型

    m = re.match(r'^1[35789]\d{9}$', '13271222223')
    print(m)
    m = re.match(r'^1[35789]\d{9}$', '13271222231$15')
    print(m)
    connect_to_mysql()
