import numpy as np
import time
import  scipy.misc as misc

arr_b = np.zeros(shape=(4500, 4501))
print(type(arr_b))
arr_a = np.zeros(shape=(4500, 4501))
arr_c = np.zeros(shape=(4500, 4501))

#
b = np.ones(shape=(10, 10))
print(type(arr_b))
a = np.zeros(shape=(10, 10))
c = np.zeros(shape=(10, 10))
#
def readFile(path):
    # 打开文件（注意路径）
    f = open("outbc11.txt")
    # 逐行进行处理
    first_ele = True
    x = 0
    y = 0
    for data in f.readlines():
        # print(data)# 打印每一行
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


def readFiles(path):
    # 打开文件（注意路径）
    f = open("outbc22.txt")
    # 逐行进行处理
    first_ele = True
    xx = 0
    yy = 0
    for data in f.readlines():
        # print(data)# 打印每一行

        data = data.strip('\n')
      #  print(data)

        # print(data)
        for i in data:
            i = int(i)

            arr_b[xx][yy] = i
            yy = yy + 1

        xx = xx + 1
        yy = 0
        # print(arr_b[index_x][index_y])

    return arr_b


# def readarr_b(arr_b):
#     for i in range(0, 10):
#         for j in range(0, 10):
#             print(arr_b[i][j])


if __name__ == '__main__':
    start = time.clock()

    arr_a = readFile("outbc11.txt")
    print(arr_a.shape)
    arr_b = readFiles("outbc22.txt")
    print(arr_b.shape)
    arr_c =  arr_a + arr_b
    print(arr_c.shape,type(arr_c))
   # c = b -a
    #np.savetxt(r'666.txt', arr_c, fmt="%d")
    image = np.array(arr_c)
    #矩阵旋转
    images = np.rot90(image)
    print(type(image))
    print(image.shape)
    misc.imsave("maptestend20410.jpg", images)
    misc.imsave("maptesta204101.jpg", arr_a)
    misc.imsave("maptestb204102.jpg", arr_b)
    np.savetxt(r'mapptestBbCc2048.txt', images, fmt="%d", delimiter='', footer='By Accelerator')

    end = time.clock()
    runing_time = end - start
    print(runing_time)
