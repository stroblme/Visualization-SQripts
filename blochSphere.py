from blochBase import blochSphere

# b = blochSphere(plotBack=True, labelAxis=True)
# vec = [1, -2, 3]
# b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=True)
# b.show()
# input()
b = blochSphere(plotBack=False, labelAxis=True)
vec = [1, -2, 3]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=True)
b.saveDefault("blochSphereNoLabel")

del(b)

b = blochSphere(plotBack=False, labelAxis=True)
vec = [0, 0, 1]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=False, norm=False)
b.saveDefault("blochSphere10")

del(b)

b = blochSphere(plotBack=False, labelAxis=True)
vec = [0, 0, -1]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=False, norm=False)
b.saveDefault("blochSphere01")

del(b)

b = blochSphere(plotBack=False, labelAxis=True)
vec = [0, 0, 0.8]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=False, norm=False)
b.saveDefault("blochSphere08")

del(b)
b = blochSphere(plotBack=False, labelAxis=True)
vec = [0, 0, 0.4]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=False, norm=False)
b.saveDefault("blochSphere04")
del(b)

b = blochSphere(plotBack=False, labelAxis=True)
vec = [0, 0, -0.3]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=False, norm=False)
b.saveDefault("blochSphere03")
del(b)

b = blochSphere(plotBack=False, labelAxis=True)
vec = [0, 0, -0.5]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=False, norm=False)
b.saveDefault("blochSphere05")
del(b)

b = blochSphere(plotBack=True, labelAxis=True)
vec = [1, -2, 3]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=True)
b.saveDefault("blochSphere")

del(b)
b = blochSphere()
vec = [0, 0, 1]
b.addVect(vec)
b.saveDefault("blochSphere_g")

del(b)
b = blochSphere()
vec = [0, 0, -1]
b.addVect(vec)
b.saveDefault("blochSphere_x")

del(b)
b = blochSphere()
vec = [1, 0, 0]
b.addVect(vec)
b.saveDefault("blochSphere_h")

del(b)

b = blochSphere()

b.addSquishedSphere(1,0.7,0.7)
b.saveDefault("blochSphere_squished")
