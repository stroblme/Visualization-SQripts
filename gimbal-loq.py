from blochBase import blochSphere

# b = blochSphere(plotBack=True, labelAxis=True)
# vec = [1, -2, 3]
# b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=True)
# b.show()
# input()
b = blochSphere(plotBack=False, labelAxis=True)
vec = [1, -2, 3]
b.addVect(vec, '$\\vert \psi \\rangle$', drawAngles=True)
b.saveSVG("gl_bloch_sphere")
