__author__ = 'cookie'
# -*- coding: utf-8 -*-
#!/usr/bin/env python
#  2018/2/2 14:26

def min_sort(array):
    LEN = len(array)
    # 先全部调整一次
    for k in range((LEN+1)//2-1, -1, -1): # 从最后一个根节点开始调整，依次往前
        adjust_down(array, k, LEN-1)
    # 再开始边交换最大值到最后，边调整
    build_min_heap(array, LEN-1)
    return array

def build_min_heap(array, last):
    if last < 1:
        return
    array[0], array[last] = array[last], array[0] # 此时array的根节点是最大值，与最后一个节点交换
    adjust_down(array, 0, last-1) # 从根节点开始调整一次，根节点又成了最大
    build_min_heap(array, last-1)

def adjust_down(array, k, last): #从k节点开始往下调整，把最大的值换到k节点上来
    left = k*2+1
    right = left+1
    tmp = None
    if right <= last and array[right] > array[left]:
        tmp = right
    elif left <= last:
        tmp = left
    if tmp and array[tmp] > array[k]:  # 如果需要交换，则要继续往下调整
        array[tmp], array[k] = array[k], array[tmp]
        adjust_down(array, tmp, last)

if __name__ == '__main__':
    array = [4,3,5,7,2,5,1]
    min_sort(array)
    print(array)