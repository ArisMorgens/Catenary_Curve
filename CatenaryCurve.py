import math
import numpy as np
import matplotlib.pyplot as plt
import sys

#The Catenary_2D function creates a 2D catenary curve
#on the x-y plane. It represents rope that is hanging
#from 2 mounting points. One of the mounting points
#is the reference point and is placed on (0,0).

# L: The length of the rope.
#dx: The horizontal distance between the 2 mounting points.
#dz: The vertical distance between the 2 mounting points.

#The Catenary_3D function generalizes the curve created
#by Catenary_2D into three-dimensional space.

#x1: Reference mounting point's position on x-axis.
#y1: Reference mounting point's position on y-axis.
#z1: Reference mounting point's position on z-axis.
# f: Rotation of the curve around z-axis in radians.


class Catenary:
    def __init__(self, L, Num):
        self.Num = Num #Number of points on the curve
        self.L = L
        
    def Catenary_2D(self, dx, dz):
        global x, z
        A = [None] * 20
        z = [None] * self.Num

        if (pow(self.L,2)) <= pow(dx,2)+pow(dz,2):
            print('Rope length too small.')
            exit()
        else:
            r1 = math.sqrt(pow(self.L,2)-pow(dz,2))/dx
            
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

        a = dx/(2*AA)
        b = ((dx)/2) - a*math.atanh(dz/self.L)
        c = - a*math.cosh((-b)/a)
        x = np.linspace(0, dx, self.Num)
        z = a*np.cosh((x-b)/a) + c
        
        plt.figure()
        plt.plot(x, z, 'o-y', mec = 'k')
        font1 = {'family':'serif','color':'#2d867e','size':20}
        font2 = {'family':'serif','color':'#2d867e','size':15}

        plt.xlabel("X-Axis", fontdict = font2)
        plt.ylabel("Z-Axis", fontdict = font2)
        plt.title("2D Catenary Curve", fontdict = font1)
        
        ax = plt.gca()
        ax.set_aspect('equal')

        plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)


    def Catenary_3D(self,x1,y1,z1,f):
        MA = [[math.cos(f),-math.sin(f),0,x1],[math.sin(f),math.cos(f),0,y1],[0,0,1,z1],[0,0,0,1]]

        y = np.zeros(len(x))
        Ones = np.ones(len(x))
        D2 = [list(x),list(y),list(z),list(Ones)]
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
        
Curve = Catenary(1.5, 40)
Curve.Catenary_2D(0.6, 0.2)
Curve.Catenary_3D(1,1,1,math.pi/6)

