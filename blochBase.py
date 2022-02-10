from qutip import *
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.patches import Arc
from matplotlib.lines import Line2D
from colors import LIGHTGRAY, GRAY, WHITE, HIGHLIGHT, MAIN, DARKGRAY

class blochSphere(Bloch):
    LABEL_VECT_DISTANCER=1.1
    NUM_OF_ARC_POINTS=100

    def __init__(self, plotBack=False, labelAxis=False):
        fig = plt.figure(figsize=[5.1,5])

        super(blochSphere, self).__init__(fig=fig)
        self.spheres=list()
        self.arcs=list()
        self.make_sphere()
        self.font_size = 18
        # self.font_color == LIGHTGRAY
        self.sphere_color = WHITE
        self.sphere_alpha = 0.04
        self.frame_color = GRAY
        self.vector_color = [HIGHLIGHT]
        self.vector_style = "wedge"

        if plotBack and labelAxis:
            self.xlabel = ['$\\vert + \\rangle$\n$\\qquad x$',"$\\vert - \\rangle$"]
            self.xlpos = [1.4,-1.4]
            self.ylabel = ['$\\vert -\\imath \\rangle$\n$y$',"$\\vert +\\imath \\rangle$"]
            self.ylpos = [1.18,-1.2]
            self.zlabel = ['$\\vert 0 \\rangle \\quad z$',"$\\vert 1 \\rangle$"]
            self.zlpos = [1.18,-1.35]
        elif labelAxis:
            self.xlabel = ['$\\vert + \\rangle \\quad x$',""]
            self.xlpos = [1.4,-1.4]
            self.ylabel = ['$\\vert -\\imath \\rangle$\n$y$',""]
            self.ylpos = [1.2,-1.2]
            self.zlabel = ['$\\vert 0 \\rangle \\quad z$',"$\\vert 1 \\rangle$"]
        else:
            self.xlabel = ['$\\vert + \\rangle$',""]
            self.xlpos = [1.4,-1.4]
            self.ylabel = ['$\\vert -\\imath \\rangle$ ',""]
            self.ylpos = [1.2,-1.2]
            self.zlabel = ['$\\vert 0 \\rangle$',""]

        self.spheres=list() # attention, this mechanism requires the parent class to contain a customPlot(self) function


    def saveDefault(self, name):

        self.save(f"../Thesis/figures/{name}.pdf", format="pdf")

    def addVect(self, vec, label=None, drawAngles=False, angleArcPos=0.5, angleArcRadius=0.5, norm=True):
        if norm:
            vec = vec*1/np.linalg.norm(vec)
        else:
            vec = np.array(vec)
        self.add_vectors(vec)
        if label != None:
            self.add_annotation(self.LABEL_VECT_DISTANCER*vec, '$\\vert \psi \\rangle$')

        if drawAngles:
            _, theta, phi = self.cartToSphere(*vec)
            radius = angleArcRadius
            angleArcPos = int(100*angleArcPos)
            arcIndex = np.linspace(0, theta, num = self.NUM_OF_ARC_POINTS)
            X, Y, Z, = self.generateTheta(radius, arcIndex)
            X, Y, Z, = self.rotZ(X, Y, Z, phi)
            self.add_arcs([X,Y,Z])
            self.add_annotation(np.array([-Y[angleArcPos],X[angleArcPos],Z[angleArcPos]])*1.2, '$\\theta$')

            arcIndex = np.linspace(0, phi, num = self.NUM_OF_ARC_POINTS)
            X, Y, Z, = self.generatePhi(radius, arcIndex)
            self.add_arcs([X,Y,Z])
            self.add_annotation(np.array([-Y[angleArcPos],X[angleArcPos],Z[angleArcPos]])*1.2, '$\\phi$')

            # Don't draw helper arc, if it would look ugly
            if theta <= np.pi/2:
                arcIndex = np.linspace(theta, np.pi/2, num = self.NUM_OF_ARC_POINTS)
            elif theta <= np.pi:
                arcIndex = np.array([0])
            elif theta <= 3*np.pi/2:
                arcIndex = np.linspace(theta, 3*np.pi/2, num = self.NUM_OF_ARC_POINTS)
            else:
                arcIndex = np.array([0])


            X, Y, Z, = self.generateTheta(radius, arcIndex)
            X, Y, Z, = self.rotZ(X, Y, Z, phi)
            self.add_arcs([X,Y,Z])

        

    def cartToSphere(self, x, y, z):
        r = np.sqrt(x**2 + y**2 + z**2)
        theta = np.arccos(z/r)
        phi = np.arctan(y/x)
        #TODO: just fix everything that's messed up. Check if that can be reduced
        if y < 0:
            phi+=np.pi
        if x > 0 and y < 0:
            phi+=np.pi
        if x < 0 and y > 0:
            phi+=np.pi

        return(r, theta, phi)

    def generateTheta(self, r, theta):
        theta = theta + np.pi
        y = -r * np.sin(theta)
        x = r * np.cos(theta) * 0
        z = -r * np.cos(theta)
        return(x, y, z)

    def generatePhi(self, r, phi):
        # phi = phi + np.pi
        y = -r * np.cos(phi)
        x = r * np.sin(phi)
        z = -r * np.cos(phi) * 0
        return(x, y, z)

    def rotZ(self, X, Y, Z, phi):
        phi = phi + np.pi   #TODO: check why we need this

        r = np.array((  (np.cos(phi), -np.sin(phi), 0),
                        (np.sin(phi),  np.cos(phi), 0),
                        (0,            0          , 1)))

        RX = list()
        RY = list()
        RZ = list()

        #TODO: This  needs approvement
        for x,y,z in np.transpose(np.array([X, Y, Z])):
            (rx,ry,rz) = r.dot(np.array([x,y,z]))
            RX.append(rx)
            RY.append(ry)
            RZ.append(rz)
        return RX, RY, RZ
        

    def add_arcs(self, arc):
        self.arcs.append(arc)

    def plot_arcs(self):
        for i, arc in enumerate(self.arcs):
            if i%3==0:
                color=MAIN
            elif i%2==0:
                color=GRAY
            else:
                color=MAIN
            self.axes.plot(*arc, color=color)
        
    def customPlot(self):
        for sphere in self.spheres:
            self.__plot_back(*sphere)
            self.__plot_front(*sphere)

        self.plot_arcs()

        markerstyle= "o"
        span = np.linspace(-1.0, 1.0, 2)
        self.axes.plot(span, 0 * span, zs=0, zdir='z', label='X',marker=markerstyle, ms=2, clip_on=False, lw=self.frame_width, color=DARKGRAY)
        self.axes.plot(0 * span, span, zs=0, zdir='z', label='Y', marker=markerstyle, ms=2, clip_on=False, lw=self.frame_width, color=DARKGRAY)
        self.axes.plot(0 * span, span, zs=0, zdir='y', label='Z',marker=markerstyle, ms=2, clip_on=False, lw=self.frame_width, color=DARKGRAY)


    def addSquishedSphere(self, x, y, z):
        self.spheres.append([x,y,z])

    def __plot_back(self, x_c, y_c, z_c):
        # back half of sphere
        u = np.linspace(0, np.pi, 25)
        v = np.linspace(0, np.pi, 25)
        x = y_c*np.outer(np.cos(u), np.sin(v))
        y = x_c*np.outer(np.sin(u), np.sin(v))
        z = z_c*np.outer(np.ones(np.size(u)), np.cos(v))
        self.axes.plot_surface(x, y, z, rstride=2, cstride=2,
                               color=MAIN, linewidth=0,
                               alpha=self.sphere_alpha*15)
        # wireframe
        self.axes.plot_wireframe(x, y, z, rstride=5, cstride=5,
                                 color=HIGHLIGHT,
                                 alpha=self.frame_alpha*0.7)

    def __plot_front(self, x_c, y_c, z_c):
        # front half of sphere
        u = np.linspace(-np.pi, 0, 25)
        v = np.linspace(0, np.pi, 25)
        x = y_c*np.outer(np.cos(u), np.sin(v))
        y = x_c*np.outer(np.sin(u), np.sin(v))
        z = z_c*np.outer(np.ones(np.size(u)), np.cos(v))
        self.axes.plot_surface(x, y, z, rstride=2, cstride=2,
                               color=MAIN, linewidth=0,
                               alpha=self.sphere_alpha*15)
        # wireframe
        self.axes.plot_wireframe(x, y, z, rstride=5, cstride=5,
                                 color=HIGHLIGHT,
                                 alpha=self.frame_alpha*0.7)
    

