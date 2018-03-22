from app import db

# #记录训练数据模型
# class TrainSourceData(db.Model):
#     __tablename__="comments"
#     __table_args__ = {"mysql_charset": "utf8"}
#     id = db.Column(db.BigInteger, primary_key=True)
#     content=db.Column(db.Text)


#训练数据处理之后的结果
class TrainDesData(db.Model):
    __tablename__ = "commentsdes"
    __table_args__ = {"mysql_charset": "utf8"}
    id = db.Column(db.Integer, primary_key=True)
    contentsrc = db.Column(db.Text)
    contentsplit = db.Column(db.Text)
    poscount = db.Column(db.Integer, default=0)
    nagcount = db.Column(db.Integer, default=0)
    emotion = db.Column(db.Integer, default=0)


#需要分析的电影
class Movie(db.Model):
    __tablename__ = "movie"
    __table_args__ = {"mysql_charset": "utf8"}
    id = db.Column(db.Integer, primary_key=True)
    movieid = db.Column(db.BigInteger)
    bigComment = db.Column(db.Text)
    rate1 = db.Column(db.Float)  #什么鬼0-0.3
    rate2 = db.Column(db.Float)  #及格0.3-0.5
    rate3 = db.Column(db.Float)  #推荐0.5-0.8
    rate4 = db.Column(db.Float)  #很棒0.8-1.0


#需要分析的数据
class Comment(db.Model):
    __tablename__ = "allcomment"
    __table_args__ = {"mysql_charset": "utf8"}
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movieid = db.Column(db.BigInteger)  #记录电影的id
    poscount = db.Column(db.Integer, default=0)
    nagcount = db.Column(db.Integer, default=0)
    result = db.Column(db.Float, default=0.0)
