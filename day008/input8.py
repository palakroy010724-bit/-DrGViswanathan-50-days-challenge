import matplotlib.pyplot as plt
import numpy as np 
angle= int(input("enter angle(in degrees):"))
u= int(input("enter initial velocity(m/sec):"))
g=9.8
angle_rad= np.radians(angle)
t_flight=2*u*np.sin(angle_rad)/g
t=np.linspace(0,t_flight,num=500)
rangee= u*np.cos(angle_rad)*t
height=u*np.sin(angle_rad)*t-0.5*g*t**2
plt.plot(rangee,height)
plt.xlabel("distance")
plt.ylabel("velocity")
plt.title("PROJECTILE MOTION")
plt.grid()
plt.show()