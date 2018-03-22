"""训练得出数据模型"""

from app.models import TrainDesData


def get_theta():
    import math
    theta = [0.0, 0.0, 0.0]
    step = 0.01
    comments = TrainDesData.query.all()[:2]
    for m in range(3):
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


# def get_emotion():
#     import math
#     print("Calculating thetas...")
#     theta=get_theta()
#     print("Done!")
#     comments = TrainDesData.query.filter_by(emotion=-1).all()
#     for comment in comments:
#         x = [1, float(comment.poscount), float(comment.nagcount)]
#         hypothesis = 0.0
#         feature_sum = 0.0
#         for i in range(3):
#             feature_sum += theta[i]*x[i]
#         hypothesis = 1 / (1+math.e**-(feature_sum))
#         if 0 < hypothesis < 0.4:
#             comment.analysis_score = 0
#         elif 0.4 <= hypothesis < 0.6:
#             comment.analysis_score = 0.5
#         elif 0.6 <= hypothesis < 1:
#             comment.analysis_score = 1
