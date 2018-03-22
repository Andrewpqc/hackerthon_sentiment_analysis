"""parse the comments"""
import mysql.connector
import jieba.posseg as pseg
import jieba
import os
import time
from emotion_words import po_words, ne_words

# Load User's Dictionary
path_list = os.getcwd().split('/')
path_list.append("dict.txt")
dict_path = '/'.join(path_list)
jieba.load_userdict(dict_path)

#不重要词的词性
dismiss = [
    'b', 'c', 'r', 'uj', 'u', 'p', 'q', 'uz', 't', 'ul', 'k', 'f', 'ud', 'ug',
    'uv'
]

conn_des = mysql.connector.connect(
    user='root',
    password='xxxx',
    database='Hackerthon',
    host="xxxx",
    port=32777)
# conn_src=mysql.connector.connect(user='root', password='pqc19960320',
#                                database='sourceData',host="120.77.220.239",port=32777)
#源游标
# cursor_src = conn_src.cursor()
#目标游标
cursor_des = conn_des.cursor()

# cursor_src.execute("select * from comments limit 500")
# values = cursor_src.fetchall()
cursor_des.execute("select * from allcomment limit 2347")
results = cursor_des.fetchall()
#一篇评论
index = 0
for result in results:
    print(index)
    index += 1
    time.sleep(0.2)
    poscount1 = 0
    nagcount1 = 0
    srcstring = result[1].strip()  #训练的源字符串
    word_list = []
    pseg_cut = pseg.cut(srcstring)
    for word, flag in pseg_cut:
        if flag not in dismiss:
            word_list.append(word)
#接下来就是计算好评数和坏评数了。
    for word in word_list:
        if word in po_words:
            poscount1 += 1
        elif word in ne_words:
            nagcount1 += 1
    try:
        cursor_des.execute(
            "update allcomment set poscount=%d,nagcount=%d where id=%d" %
            (poscount1, nagcount1, int(result[0])))
    except mysql.connector.errors.ProgrammingError:
        print('programmingError')
        continue
    except mysql.connector.errors.DatabaseError:
        print("databaseError")
        time.sleep(3)

conn_des.commit()

cursor_des.close()
#

#
#
#
#

# import mysql.connector
# conn_des = mysql.connector.connect(user='root', password='xxxx',
#                                 database='Hackerthon',host="xxxxx",port=32777)
# cursor=conn_des.cursor()
# cursor.execute("select * from allcomment limit 2")
# results=cursor.fetchall()
# for i in results:
#     print(i)
# conn_des.commit()
# cursor.close()
