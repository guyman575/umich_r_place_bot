import os
import sys
import random
from time import sleep
from place import Place

b=13
y=8
uname = input("Username: ")
passw = input("Password: ")
p = Place(uname,passw)

color_mat = [[b]*32,
[b,b,y,y,b,b,b,y,y,b,b,b,y,y,y,b,b,y,b,b,b,b,y,b,b,y,b,y,y,y,b,b],
[b,y,b,b,b,b,y,b,b,y,b,b,y,b,b,y,b,y,b,b,b,b,y,b,b,y,b,y,b,b,b,b],
[b,y,b,y,y,b,y,b,b,y,b,b,y,y,y,b,b,y,b,b,b,b,y,b,b,y,b,y,y,y,b,b],
[b,y,b,b,y,b,y,b,b,y,b,b,y,b,b,y,b,y,b,b,b,b,y,b,b,y,b,y,b,b,b,b],
[b,b,y,y,b,b,b,y,y,b,b,b,y,y,y,b,b,y,y,y,y,b,y,y,y,y,b,y,y,y,y,b]]

offset_x = 70
offset_y = 807

while True:
    for i in range (32):
        for j in range(6):
            data = p.get(i + offset_x, j + offset_y)
            c = data['color']
            print(c)
            if c != color_mat[j][i]:
                print(c,color_mat[j][i])
                print(i + offset_x,j + offset_y)
                p.draw(x=i + offset_x, y=j + offset_y,color=color_mat[j][i])
                print(p.get(i + offset_x, j + offset_y))
                sleep(300)










# while True:
#     os.system('xdotool mousemove 1010 1065')
#     sleep(random.randint(1,10))
#     os.system('xdotool click 1')
#     sleep(random.randint(1,10))
#     os.system('xdotool mousemove 322 265')
#     sleep(random.randint(1,10))
#     os.system('xdotool click 1')
#     sleep(300 + random.randint(1,10))
