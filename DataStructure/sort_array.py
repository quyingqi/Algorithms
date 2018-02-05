__author__ = 'cookie'
# -*- coding: utf-8 -*-
#!/usr/bin/env python
#  2018/2/2 14:26

class HeapSort():
    # 建立小根堆
    def min_sort(self, array):
        LEN = len(array)
        # 先全部调整一次
        for k in range((LEN+1)//2-1, -1, -1): # 从最后一个根节点开始调整，依次往前
            self.adjust_down(array, k, LEN-1)
        # 再开始边交换最大值到最后，边调整
        self.build_min_heap(array, LEN-1)
        return array

    def build_min_heap(self, array, last):
        if last < 1:
            return
        array[0], array[last] = array[last], array[0] # 此时array的根节点是最大值，与最后一个节点交换
        self.adjust_down(array, 0, last-1) # 从根节点开始调整一次，根节点又成了最大
        self.build_min_heap(array, last-1)

    def adjust_down(self, array, k, last): #从k节点开始往下调整，把最大的值换到k节点上来
        left = k*2+1
        right = left+1
        tmp = None
        if right <= last and array[right] > array[left]:
            tmp = right
        elif left <= last:
            tmp = left
        if tmp and array[tmp] > array[k]:  # 如果需要交换，则要继续往下调整
            array[tmp], array[k] = array[k], array[tmp]
            self.adjust_down(array, tmp, last)

class QuickSort():
    def quick_sort(self, array):
        self.helper(array, 0, len(array)-1)

    def helper(self, array, low, high):
        if low >= high:
            return
        # 设置左右两个指针，轮着移动，使得最后左边的数都小于标杆，右边的数都大于标杆
        mid = low
        i, j = low, high
        while(i < j):
            while(array[j] >= array[mid] and i < j): # 注意！！因为标杆在左边，所以先从右边开始！！！
                j -= 1
            while(array[i] <= array[mid] and i < j):
                i += 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        if array[i] < array[mid]:
            array[i], array[mid] = array[mid], array[i] # 不然i就不是小于标杆的数，不能跟标杆交换了

        self.helper(array, low, i-1)
        self.helper(array, i+1, high)

class MergeSort():
    def merge_sort(self, array):
        self.helper(array, 0, (len(array)-1)//2, len(array)-1)

    def helper(self, array, low, mid, high):
        if low >= high:
            return
        self.helper(array, low, (low+mid)//2, mid)
        self.helper(array, mid+1, (mid+1+high)//2, high)
        self.merge(array, low, mid, high)

    def merge(self, array, low, mid, high):
        merged = []
        i, j = low, mid+1
        while(i <= mid and j <= high):
            if array[i] <= array[j]:
                merged.append(array[i])
                i += 1
            else:
                merged.append(array[j])
                j += 1
        while(i <= mid):
            merged.append(array[i])
            i += 1
        while(j <= high):
            merged.append(array[j])
            j += 1
        array[low:high+1] = merged

if __name__ == '__main__':
    array = [4,3,5,7,2,5,1]
    #HeapSort().min_sort(array)
    #QuickSort().quick_sort(array)
    MergeSort().merge_sort(array)
    print(array)