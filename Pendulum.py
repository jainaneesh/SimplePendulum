from scipy.integrate import odeint
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np
from PIL import Image
import glob
import natsort
import os
import imageio

# directory = "Animation"
# parent_dir = "C:/Users/jaina/Desktop/Python/SimplePendulum/"
# path = os.path.join(parent_dir,directory)
# print(path)

# os.mkdir(path)

# x1 = []
# y1 = []
# global count

def pendulum(theta,t,b,g,l,m):
    # cnt = count
    global count
    # global fig
    count = count+1
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = (-b/m)*theta2-(g/l)*math.sin(theta1)
    dtheta_dt = [dtheta1_dt,dtheta2_dt]    
    x1 = l*math.sin(theta1)
    y1 = -l*math.cos(theta1)
    filename = 'test%5d.png'%count
    fig = plt.figure(count)
    # plt.figure(count)  
    plt.plot([-2, 2],[0, 0],'b-')
    plt.plot([x0, x1],[y0, y1],'r-')
    plt.xlim(-2, 2)
    plt.ylim(-4, 4)
    plt.grid()
    plt.axis('equal')
    # plt.show()        
    plt.savefig(filename)
    # plt.hold(False)
    plt.close(fig)
    # count = count + 1
    # print(count)
    return dtheta_dt

theta_0 = [0,3]
t = np.linspace(0,20,300)
# print(len(t))
# t.reshape(len(t),1)
# print(t.shape)
x0 = 0
y0 = 0
count = 0
b = 0.05
g = 9.81
m = 1
l = 1

dtheta_dt = odeint(pendulum,theta_0,t,args=(b,g,l,m))
# print(dtheta_dt.shape)
# imgs = glob.glob("*.png")
# images = natsort.natsorted(imgs,reverse = False)
# frames = []
# for i in images:
#     new_frame = Image.open(i)
#     frames.append(new_frame)

# # # print(type(frames))
# frames[0].save('Pendulum_Animation_Using_Python.gif',format = 'GIF', append_images = frames[1:], save_all = True, duration = 40, loop = 1)

#Plotting for animation
# x = np.zeros((len(t),1),dtype=float)
# y = np.zeros((len(t),1),dtype=float)
# for i in range(1,len(t)):
#     x[i] = l*math.sin(dtheta_dt[i,0])
#     y[i] = -l*math.cos(dtheta_dt[i,0])
# print(x)
# print(y)
# plt.plot(x,y,'r.')
# plt.grid()
# plt.show()
plt.plot(t,dtheta_dt[:,0],'b-',label=r'$\frac{d\theta_1}{dt}=\theta_2$')
plt.plot(t,dtheta_dt[:,1],'r--',label=r'$\frac{d\theta_2}{dt}-\frac{b}{m}\theta_2-\frac{g}{l}sin\theta_1$')
plt.ylabel('Plot')
plt.xlabel('Time')
plt.legend(loc='best')
plt.show()

import imageio
with imageio.get_writer('pendulum.gif', mode='i') as writer:
    for i in range(1, 1302):
        image = imageio.imread("C:/Users/jaina/Desktop/Python/SimplePendulum/Animation/filename")
        writer.append_data(image)