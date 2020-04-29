import cv2
import time
import numpy as np

start = time.time()

img = cv2.imread('./Short.png')

red = [0,0,255]
orange = [0,100,255]
green = [255,0,0]

index_red = np.where(np.all(img[:] == red, axis=2))
index_orange = np.where(np.all(img[:] == orange, axis=2))
index_green = np.where(np.all(img[:] == green, axis=2))

pixel_red = (index_red[1][0], index_red[0][0])
pixel_orange = (index_orange[1][0], index_orange[0][0])
pixel_green = (index_green[1][0], index_green[0][0])


cmPerPixel = 1.6*(10**-4) # cm
h_pixel = 0
f = 0.473   # cm (camera focus)

point_red = [0, 0]            #cm
point_orange = [27.5, -5.8]  
point_green = [21, 8.3]

result = 0
resultA2B = 0
resultB2C = 0
resultC2A = 0

def distance_calculation(pixel_1st, pixel_2nd, point_1st, point_2nd, result_tmp):
    for i in range(2):
        h_pixel = (abs(pixel_1st[i]-pixel_2nd[i]))*cmPerPixel
        h_realworld = abs(point_1st[i]-point_2nd[i])
        tmp = f*h_pixel/h_realworld
        sp = tmp + f
        s = 1 / abs(1/f - 1/sp)
        result_tmp += s
    return result_tmp

resultA = distance_calculation(pixel_red, pixel_orange, point_red, point_orange, resultA2B)
resultB = distance_calculation(pixel_orange, pixel_green, point_orange, point_green, resultB2C)
resultC = distance_calculation(pixel_green, pixel_red, point_green, point_red, resultC2A)

result_sum = resultA+resultB+resultC

finish = time.time()

print("average distance is : \"{:.3f}\"cm".format(result_sum/6))
print("Executing time is : \"{:.3f}\"s".format(finish-start))
