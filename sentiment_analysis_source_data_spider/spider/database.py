from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text
from  sqlalchemy.orm import sessionmaker
Base = declarative_base() #生成一个SqlORM 基类
engine = create_engine("mysql+pymysql://root:pqc19960320@120.77.220.239:32777/sourceData")
#echo如果为True，那么当他执行整个代码的数据库的时候会显示过程
#创建一个类继承Base基类
class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = {"mysql_charset": "utf8"}
    id = Column(Integer,primary_key=True,autoincrement=True)
    content=Column(Text)

Base.metadata.create_all(engine) #创建所有表结构

def addEntry(data):
    SessionCls = sessionmaker(bind=engine)
    #bind绑定
    #创建与数据库的会话session class
    #注意,这里返回给session的是个class,不是实例
    session = SessionCls()
    a=[]
    for d in data:
        h= Comment(content=d)
        a.append(h)
    session.add_all(a)

    #添加一个
    # session.add(h1)
    #可以添加多个字段
    # session.add_all( [h1,h2,h3])
    #修改字段名字,只要没提交,此时修改也没问题
    #h2.hostname = 'ubuntu_test'
    #支持数据回滚
    #session.rollback()
    #提交
    session.commit()
    session.close()
