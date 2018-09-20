import matplotlib.pyplot as plt
import networkx as nx

def test():
    G = nx.random_graphs.barabasi_albert_graph(1000, 3)  # 生成n=1000,m=3的无标度的图
    print("某个节点的度:", G.degree(0))  # 返回某个节点的度
    print("所有节点的度:", G.degree())  # 返回所有节点的度
    print("所有节点的度分布序列:", nx.degree_histogram(G))  # 返回图中所有节点的度分布序列（从1至最大度的出现频次）
    degree = nx.degree_histogram(G)  # 返回图中所有节点的度分布序列
    print(degree)
    print(type(degree))
    x = range(len(degree))  # 生成X轴序列，从1到最大度
    y = [z / float(sum(degree)) for z in degree]  # 将频次转化为频率，利用列表内涵
    plt.loglog(x, y, color="blue", linewidth=2)  # 在双对坐标轴上绘制度分布曲线
    plt.show()  # 显示图表

def degreeDistribute(degreelist):
    print(degreelist)
    x = range(len(degreelist))
    y = [z / float(sum(degreelist)) for z in degreelist]
    plt.loglog(x, y, color="blue", linewidth=2)
    plt.show()

def degreeDistribute1(degreelist):
    x = []
    y = []
    for i in range(0, len(degreelist)):
        x.append(i)
        y.append(degreelist.count(i)/len(degreelist))
    plt.plot(x, y, 'b-', label="1", linewidth=2)
    plt.title('DD')
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
    plt.xlabel('degree')
    plt.ylabel('number')
    plt.show()

def degreeDistribute2(degreelist1, degreelist2):
    x1 = []
    y1 = []
    for i in range(0, len(degreelist1)):
        x1.append(i)
        y1.append(degreelist1.count(i)/len(degreelist1))

    x2 = []
    y2 = []
    for i in range(0, len(degreelist2)):
        x2.append(i)
        y2.append(degreelist2.count(i)/len(degreelist2))

    l1, = plt.plot(x1, y1, label='original')
    l2, = plt.plot(x2, y2, color='red', linewidth=1.0, linestyle='--', label='sampling', marker='.', markersize=1)

    plt.title('DD')
    plt.legend(handles=[l1, l2], labels=['original', 'sampling'], loc='upper right')
    plt.xlabel('degree')
    plt.ylabel('number')
    plt.show()

def degreeDistribute3(degreelist1, degreelist2, degreelist3):
    x1 = []
    y1 = []
    for i in range(0, len(degreelist1)):
        x1.append(i)
        y1.append(degreelist1.count(i)/len(degreelist1))

    x2 = []
    y2 = []
    for i in range(0, len(degreelist2)):
        x2.append(i)
        y2.append(degreelist2.count(i)/len(degreelist2))

    x3 = []
    y3 = []
    for i in range(0, len(degreelist3)):
        x3.append(i)
        y3.append(degreelist3.count(i) / len(degreelist3))

    l1, = plt.plot(x1, y1, label='original', linewidth=2.0)
    l2, = plt.plot(x2, y2, color='red', linewidth=2.0, linestyle='--', label='sampling', marker='.', markersize=1)
    l3, = plt.plot(x3, y3, color='green', linewidth=2.0, linestyle='--', label='sampling', marker='.', markersize=1)

    plt.title('DD')
    plt.legend(handles=[l1, l2, l3], labels=['original', 'RW', 'RW_MY'], loc='upper right')
    plt.xlabel('degree')
    plt.ylabel('number')
    plt.show()