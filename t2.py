import numpy as np
import matplotlib.pyplot as plt

#定义存储输入数据x和目标数据y的数组
x, y = [], []
#遍历数据集
for sample in open("C:/Users/67034/Desktop/ml/MachineLearning-master/_Data/prices.txt","r"):
    _x,_y = sample.split(",")
    x.append(float(_x))
    y.append(float(_y))
x, y = np.array(x), np.array(y)
x = (x - x.mean()) / x.std()

plt.figure()
plt.scatter(x, y, c = "g", s = 6)
plt.show()

x0 = np.linspace(-2, 4, 100)

def get_model(deg):
    return lambda input_x = x0: np.polyval(np.polyfit(x, y, deg), input_x)

#根据参数n，输入的x，y返回相应的损失
def get_cost(deg, input_x, input_y):
    return 0.5 * ((get_model(deg)(input_x) - input_y) ** 2).sum()
test_set = (1, 4, 10)
for d in test_set:
    print(get_cost(d,x,y))

#画图
plt.scatter(x, y, c="g", s=20)
for d in test_set:
    plt.plot(x0, get_model(d)(), label = "degree = {}".format(d))
#把横轴/纵轴的范围限制在(-2,4),(10^5,8*10^5)
plt.xlim(-2,4)
plt.ylim(1e5,8e5)
#调用legend方法使曲线对应的label正确显示
plt.legend()
plt.show()