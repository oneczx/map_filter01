import numpy as np
import time
import  scipy.misc as misc

arr_b = np.zeros(shape=(6000, 6001))
print(type(arr_b))
arr_a = np.zeros(shape=(6000, 6001))
arr_c = np.zeros(shape=(6000, 6001))

#
b = np.ones(shape=(10, 10))
print(type(arr_b))
a = np.zeros(shape=(10, 10))
c = np.zeros(shape=(10, 10))
#
def readFile(path):
    # 打开文件（注意路径）
    f = open("outbc22.txt")
    # 逐行进行处理
    first_ele = True
    x = 0
    y = 0
    for data in f.readlines():
        # print(data)# 打印每一行
        #data = data.split(',')
        data = data.strip('\n')
        # print(data)

        for i in data:

            i = int(i)

            arr_a[x][y] = i
            y = y + 1

        x = x + 1
        y = 0
        # print(arr_b[index_x][index_y])

    return arr_a

def flip180(arr):
    new_arr = arr.reshape(arr.size)
    new_arr = new_arr[::-1]
    new_arr = new_arr.reshape(arr.shape)
    return new_arr

if __name__ == '__main__':
    start = time.clock()

    arr_a = readFile("outbc22.txt")
    print(arr_a.shape)
    # mew_arr = flip180(arr_a)

    image = np.array(arr_a)
    # image1 = np.array(mew_arr)
    #矩阵旋转
    images = np.rot90(image)
    #new_arr2 = flip180(image)
    image2 = np.array(images)
    print(type(image2))
    print(image2.shape)
    # misc.imsave("maptestbc.jpg", images)
    misc.imsave("maptesta2049.jpg", image2)
    # misc.imsave("maptestbccc.jpg", image1)
    # misc.imsave("maptestbccbc.jpg", image2)

   # np.savetxt(r'mapptest66.txt', image, fmt="%d", delimiter='', footer='By Accelerator')
    end = time.clock()
    runing_time = end - start
    print(runing_time)
