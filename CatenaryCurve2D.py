import math
import numpy as np
import matplotlib.pyplot as plt
import sys

#The Catenary_2D function creates a 2D catenary curve
#on the x-y plane. It represents rope that is hanging
#of its 2 mounting points. One of the mounting points
#is the reference point and is placed on (0,0).
# L: The length of the rope.
#dx: The horizontal distance of the 2 mounting points.
#dz: The vertical distance of the 2 mounting points.
#The z variable can be replaced by y, so that the
#catenary curve is placed on the x-y plane.

def Catenary_2D(L,dx,dz):
    Num = 40 #Number of points on the curve
    A = [None] * 20
    z = [None] * Num   

    if (pow(L,2)) <= pow(dx,2)+pow(dz,2):
        print('Rope length too small.')
        exit()
    else:
        r1 = math.sqrt(pow(L,2)-pow(dz,2))/dx
        
        if r1 < 3:
            A0 = math.sqrt(6*(r1-1))
        else:
            A0 = np.log(2*r1)+np.log(np.log(2*r1))

        A[0] = A0
        
        for i in range(19): #approximately 5 iterations are needed
            A[i+1] = A[i]-((math.sinh(A[i])-(r1*A[i]))/(math.cosh(A[i])-r1))

            err = abs(r1-((math.sinh(A[i+1]))/A[i+1]))

            if err < 1e-8:
                break
            
        AA = A[i+1]
        i = i+1

    a = dx/(2*AA)
    b = ((dx)/2) - a*math.atanh(dz/L)
    c = - a*math.cosh((-b)/a)
    Catenary_2D.x = np.linspace(0, dx, Num)
    Catenary_2D.z = a*np.cosh((Catenary_2D.x-b)/a) + c
    
    plt.figure(1)
    plt.plot(Catenary_2D.x, Catenary_2D.z, 'o-y', mec = 'k')
    font1 = {'family':'serif','color':'#2d867e','size':20}
    font2 = {'family':'serif','color':'#2d867e','size':15}

    plt.xlabel("X-Axis", fontdict = font2)
    plt.ylabel("Z-Axis", fontdict = font2)
    plt.title("2D Catenary Curve", fontdict = font1)
    
    ax = plt.gca()
    ax.set_aspect('equal')

    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)

