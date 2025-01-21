# Introduction
A rope suspended between two mounting points follows a [catenary curve](https://en.wikipedia.org/wiki/Catenary). This principle finds application in robotics, in scenarios containing hanging ropes, where the mounting points can be drones and robotic arms.

![](Images/HangingRopeFromSwarm.png)

The python scripts of this repo contain two functions that create a 2D and a 3D catenary curve.
Catenary_2D output | Catenary_3D output
:---------------------------------:|:---------------------------------:
![](Images/Catenary2D_example.png) | ![](Images/Catenary3D_example.png)

# Functions
## Catenary_2D
Catenary_2D(L, dx, dz) creates a catenary curve on x-z plan, placing the reference mounting point on (0,0).

| Variable | Description |
| :---: | :--- |
| L | The length of the rope |
| dx | The horizontal distance of the 2 mounting points |
| dz | The vertical distance of the 2 mounting points |

## Catenary_3D
Catenary_3D(x1,y1,z1,f) generalizes the catenary created by Catenary_2d into three-dimensional space. This is why the position of the reference mounting point is needed as well as the rotation of the curve around the z-axis.

| Variable | Description |
| :---: | :--- |
| x1 | Reference mounting point position on x-axis |
| y1 | Reference mounting point position on y-axis |
| z1 | Reference mounting point position on z-axis |
| f | Rotation of the curve on around z-axis in radians |


# Mathematical Approach
## Catenary_2D
The method is a little bit different than the one used for determining parameters [here](https://en.wikipedia.org/wiki/Catenary#Determining_parameters). The equation of a catenary, the curve formed by a uniform string hanging between two points, is:

$$f(x) =  a  \cdot \cosh{\left(\frac{x}{ a } \right)}$$

However, this solution assumes that the curve is in a standing position with its lowest point above x = 0.
In order to allow for the catenary to be centered at any point, its equation is written as:

$$f(x) =  a  \cdot \cosh{ \left( \frac{x-b}{ a } \right) } + c$$

where $b$ is the center of the curve and $c$ is the vertical offset from the origin.

By letting $r = \frac{\sqrt{L^2 - {dz}^2}}{dx}$, the problem can been transformed into finding the solution for $A$.

$$r = \frac{\sinh{\left( A \right)}}{A}$$

Its form does not allow for a closed-form solution, so a numerical approach is implemented. Then, the three parameters $a$, $b$ and $c$ can be calculated as follows.

$$ a  = \frac{dx}{2\cdot A}$$

$$b = \overline{x} -  a  \cdot \tanh{\left( \frac{dz}{L} \right)}$$

$$c = z_1 -  a  \cdot \cosh{ \left( \frac{x_1 -b}{a} \right) }$$

where $dx=x_2-x_1,~ dz=z_2-z_1,~ \overline{x} = \frac{x_1 + x_2}{2}$. Note that in Catenary_2D(), the reference mounting point is placed at (0,0), meaning that $x1,z1 = 0$. For a more described analysis check the Acknowledgement section below.


## Catenary_3D
After finding the catenary curve in two-dimensions, it can be easily generalized into a three-dimensional space. 

The curve is always laying on the plane perpendicular to the ground formed by the two mounting points. A local coordinate system is introduced. Its origin lies on the reference mounting point, its x-axis is parallel to the ground facing along the curve plane and its z-axis is perpendicular to the ground. The coordinates of every point on the local coordinate system {A} can be transfered to the global coordinate system {U} through the transformation matrix ${}^{U}M_A$.


```math
{}^{U}\underline{P} = {}^{U}M_A \cdot {}^{A}\underline{P}
\longrightarrow
\begin{bmatrix}
{}^{{U}}x\\
{}^{{U}}y\\
{}^{{U}}z\\
1
\end{bmatrix}
=
\begin{bmatrix}
\cos{\psi} & -\sin{\psi} & 0 & x_1\\
\sin{\psi} & \cos{\psi} & 0 & y_1\\
0 & 0 & 1 & z_1 \\
0 & 0 & 0 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
{}^{{A}}x\\
0\\
{}^{{A}}z\\
1
\end{bmatrix}
```
where $\psi$ is the rotation angle around the z-axis.$
# Acknowledgement

