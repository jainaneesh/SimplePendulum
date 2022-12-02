from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import numpy as np


def pendulum(theta,t,b,g,l,m):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = (-b/m)*theta2-(g/l)*math.sin(theta1)
    dtheta_dt = [dtheta1_dt,dtheta2_dt]
    return dtheta_dt

theta_0 = [0,3]
t = np.linspace(0,20,300)

b = 0.05
g = 9.81
m = 1
l = 1

dtheta_dt = odeint(pendulum,theta_0,t,args=(b,g,l,m))
plt.plot(t,dtheta_dt[:,0],'b-',label=r'$\frac{d\theta_1}{dt}=\theta_2$')
plt.plot(t,dtheta_dt[:,1],'r--',label=r'$\frac{d\theta_2}{dt}-\frac{b}{m}\theta_2-\frac{g}{l}sin\theta_1$')
plt.ylabel('Plot')
plt.xlabel('Time')
plt.legend(loc='best')
plt.show()