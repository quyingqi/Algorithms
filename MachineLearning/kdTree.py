__author__ = 'cookie'
# -*- coding:utf-8 -*-
# 2018-1-31
import numpy as np

class kdNode():
    def __init__(self, val=None, split=None, l=None, r=None):
        '''
        :param val: 数据点
        :param split: 划分域
        :param l: 节点的左儿子
        :param r: 节点的右儿子
        '''
        self.val = val
        self.split = split
        self.left = l
        self.right = r

def create_kdTree(data_list):
    '''
    :param root: 当前树的根节点
    :param data_list: 数据点的集合（无序）
    :return: 构造的kdTree的树根
    '''
    LEN = len(data_list)
    if LEN == 0:
        return
    # 数据点的维度
    dimension = len(data_list[0])
    # 方差
    max_var = 0

    # 最后选择的划分域
    split = 0
    for i in range(dimension):
        ll = [t[i] for t in data_list]
        var = computeVariance(ll)
        if var > max_var:
            max_var = var
            split = i
    print(split)
    # 根据划分域的数据对数据点进行排序
    data_list.sort(key=lambda x: x[split])

    # 选择下标为len / 2的点作为分割点
    val = data_list[LEN//2]
    root = kdNode(val, split)
    root.left = create_kdTree(data_list[: LEN//2])
    root.right = create_kdTree(data_list[LEN//2+1 :])
    return root

def computeVariance(arrayList):
    '''
    :param arrayList: 数据点在某一维度的所有值
    :return: 方差
    '''
    LEN = len(arrayList)
    array = np.array(arrayList, float)
    #D[X] = E[x^2] - (E[x])^2
    mean = np.sum(array) / LEN
    mean2 = np.sum(array**2) / LEN
    variance =  mean2 - mean**2
    return variance

def findNN(root, query):
    '''
    :param root: kdTree的树根
    :param query: 查询点
    :return: 返回距离data最近的点NN，同时返回最短距离min_dist
    '''
    #初始化为root的节点
    NN = root.val # 记录最近的节点
    min_dist = computeDist(query, NN) # 记录最近节点到query的距离
    nodeList = [] # 记录走过的路径
    tmp_root = root

    # 二分查找建立路径
    while(tmp_root):
        nodeList.append(tmp_root)
        print(tmp_root.val)
        dd = computeDist(query, tmp_root.val)
        if dd < min_dist:
            min_dist = dd
            NN = tmp_root.val
        # 当前节点的划分域
        ss = tmp_root.split
        if query[ss] <= tmp_root.val[ss]:
            tmp_root = tmp_root.left
        else:
            tmp_root = tmp_root.right

    # 回溯查找
    while(nodeList):
        back_val = nodeList.pop()
        ss = back_val.split

        # 判断是否需要进入父亲节点的子空间进行搜索
        if abs(query[ss] - back_val.val[ss]) < min_dist:
            if query[ss] <= back_val.val[ss]:
                tmp_root = back_val.right
            else:
                tmp_root = back_val.left

            if tmp_root:
                nodeList.append(tmp_root)
                curDist = computeDist(query, tmp_root.val)
                if curDist < min_dist:
                    min_dist = curDist
                    NN = tmp_root.val

    return NN, min_dist

def computeDist(pt1, pt2):
    """
    计算两个数据点的距离
    :return: pt1和pt2之间的距离
    """
    p1 = np.array(pt1, float)
    p2 = np.array(pt2, float)
    dist = np.sqrt(np.sum((p1-p2)**2))
    return dist

if __name__ == '__main__':
    data_list = [(1,5),(2,7),(3,1),(4,6),(5,3),(6,2),(6,4),(7,7)]
    root = create_kdTree(data_list)
    NN, min_dist = findNN(root, (3,2))
    print(NN, min_dist)