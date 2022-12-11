from scipy.integrate import odeint
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np
from PIL import Image
import os
import imageio

directory = "Animation/"
parent_dir = "C:/Users/jaina/Desktop/Python/SimplePendulum/"
path = os.path.join(parent_dir,directory)
# print(path)

# os.mkdir(path)

# x1 = []
# y1 = []
# global count

def pendulum(theta,t,b,g,l,m):
    global count
    global path
    count = count+1
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = (-b/m)*theta2-(g/l)*math.sin(theta1)
    dtheta_dt = [dtheta1_dt,dtheta2_dt]    
    x1 = l*math.sin(theta1)
    y1 = -l*math.cos(theta1)
    num = '{0:04}'.format(count)
    filename = 'Test' + str(num) + '.png'    
    fig = plt.figure(count,figsize=(7,7))
    plt.plot([-2, 2],[0, 0],'b-',linewidth=3)
    plt.plot([x0, x1],[y0, y1],'r-')
    plt.plot(x1,y1,'ro')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-2, 1)     
    plt.savefig(path + filename)
    plt.close(fig)
    return dtheta_dt

theta_0 = [0,3]
t = np.linspace(0,20,300)
x0 = 0
y0 = 0
count = 0
b = 0.05
g = 9.81
m = 1
l = 1

dtheta_dt = odeint(pendulum,theta_0,t,args=(b,g,l,m))

fig = plt.figure(2)
plt.plot(t,dtheta_dt[:,0],'b-',label=r'$\frac{d\theta_1}{dt}=\theta_2$')
plt.plot(t,dtheta_dt[:,1],'r--',label=r'$\frac{d\theta_2}{dt}-\frac{b}{m}\theta_2-\frac{g}{l}sin\theta_1$')
plt.ylabel('Plot')
plt.xlabel('Time')
plt.legend(loc='best')
plt.savefig(parent_dir + "SimplePendulum.png")

import imageio.v2 as imageio
with imageio.get_writer("C:/Users/jaina/Desktop/Python/SimplePendulum/PENDULUM.gif", mode='i') as writer:
    for i in range(1, 1302):
        # filename='test' + str(i)+ '.png'
        num = '{0:04}'.format(i)
        filename = 'Test' + str(num) + '.png'
        # filename = 'test%5d.png'%i
        # image = imageio.imread("C:/Users/jaina/Desktop/Python/SimplePendulum/Animation/filename")
        image = imageio.imread(path + filename)
        writer.append_data(image)