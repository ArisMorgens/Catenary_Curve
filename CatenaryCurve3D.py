import math
import numpy as np
import matplotlib.pyplot as plt
from CatenaryCurve2D import Catenary_2D

L = 1.5 #Rope length
dx = 0.6 #Horizontal distance between the 2 mounting points
dz = 0.4 #Vertical distance between the 2 mounting points
x1 = 0.5 #Left mounting point position on x-axis
y1 = 0.2 #Left mounting point position on y-axis
z1 = 0.1 #Left mounting point position on z-axis
f =  0.3*math.pi #Angle in radians


def Catenary_3D(x1,y1,z1,f):
    MA = [[math.cos(f),-math.sin(f),0,x1],[math.sin(f),math.cos(f),0,y1],[0,0,1,z1],[0,0,0,1]]

    Catenary_2D(L,dx,dz)

    y = np.zeros(len(Catenary_2D.x))
    Ones = np.ones(len(Catenary_2D.x))
    D2 = [list(Catenary_2D.x),list(y),list(Catenary_2D.z),list(Ones)]
    D3 = np.dot(MA,D2)

    x_3D = D3[0,:]
    y_3D = D3[1,:]
    z_3D = D3[2,:]
    
    plt.figure(2)
    ax = plt.axes(projection ='3d')
    ax.plot3D(x_3D, y_3D, z_3D, 'o-y', mec = 'k')
    font1 = {'family':'serif','color':'#2d867e','size':20}
    font2 = {'family':'serif','color':'#2d867e','size':15}
    plt.xlabel("X-Axis", fontdict = font2)
    plt.ylabel("Y-Axis", fontdict = font2)
    plt.title("3D Catenary Curve", fontdict = font1)
    ax.set_aspect('equal')
    
    #Close Plot window by pressing Enter in terminal
    plt.show(block = False)
    plt.pause(1)
    input()
    plt.close()
    
Catenary_3D(x1,y1,z1,f)
