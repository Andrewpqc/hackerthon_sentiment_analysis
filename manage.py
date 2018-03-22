import os
from app import create_app, db
from flask_script import Manager, Shell
from app.models import TrainDesData, Comment, Movie
from flask_migrate import Migrate, MigrateCommand

app = create_app("default")
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app,
        db=db,
        TrainDesData=TrainDesData,
        Comment=Comment,
        Movie=Movie)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def get_theta():
    import math
    theta = [0, 0, 0]
    step = 0.01
    comments = TrainDesData.query.all()
    for m in range(40000):
        xxx = 0
        for comment in comments:
            print(xxx)
            xxx += 1
            x = [1, float(comment.poscount), float(comment.nagcount)]
            feature_sum = 0
            for i in range(3):
                feature_sum += theta[i] * x[i]

            h = 1 / (1 + math.e**-(feature_sum))
            for i in range(3):
                theta[i] = theta[i] + step * (comment.emotion - h) * x[i]
    print("Theta Gotten: ", theta)
    return theta


# [44751.0773169849, 57001.01137011098, 6551.006424249747] 5000*500样本
# [89501.0773157487, 114001.01136854848, 13101.006424319943] 10000*500样本
# [179001.07731027488, 228001.01136506314, 26201.006424205938] 20000*500样本
# [358001.0773901941, 456001.0114158664, 52401.00642363201] 40000*500样本


@manager.command
def get_emotion():
    print("Calculating thetas...")
    import math
    #get_theta()计算出来的如下结果：
    theta = [358000.224245114, 456000.10811124597, 52400.042114550015]

    print("Done!")
    comments = Comment.query.all()
    for comment in comments:
        x = [1, float(comment.poscount), float(comment.nagcount)]
        hypothesis = 0.0
        feature_sum = 0
        for i in range(3):
            feature_sum += theta[i] * x[i]
        hypothesis = 1 / (1 + math.e**-(feature_sum))
        print(hypothesis)
        if 0.0 < hypothesis < 0.25:
            comment.result = 1.0  #A
            db.session.add(comment)
            db.session.commit()
        elif 0.25 <= hypothesis < 0.6:
            comment.result = 2.0  #AA
            db.session.add(comment)
            db.session.commit()
        elif 0.6 <= hypothesis < 0.85:
            comment.result = 3.0  #AAA
            db.session.add(comment)
            db.session.commit()
        elif 0.85 <= hypothesis < 1.0:
            comment.result = 4.0  #AAAA
            db.session.add(comment)
            db.session.commit()


@manager.command
def fake():
    pass

if __name__ == '__main__':
    manager.run()
