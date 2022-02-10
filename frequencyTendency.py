from matplotlib import pyplot as plt
import numpy as np
from colors import *
from scipy.stats import binom

GATECOUNT=30
GATEERROR=0.1
GATESHRINKING=0.976
MEASUREMENTOFFSETERROR=-0.1
MEASUREMENTAMPLITUDEERROR=0.9
MEASUREMENTNOISINESS=0.2
BINOMDRAWS=100
BINOMMEAN=0.5

def minmax(minV, maxV, V):
    return min(maxV,max(minV,V))

def fctGenerator(offset=0, noise=0, amplitude=1, angle=0, shrinking=1, count=GATECOUNT):
    return np.array([minmax(-1,1,   offset +
                                    noise*(BINOMDRAWS/2-(np.random.binomial(BINOMDRAWS, BINOMMEAN)))/BINOMDRAWS +
                                    amplitude *
                                    (shrinking**i)*
                                    np.cos((np.pi+angle)*i)) for i in range(0,count)])


xGateResults = fctGenerator(0,0,1,0,GATECOUNT)
# xGateResults = np.array([np.cos(np.pi*i) for i in range(0,int(GATECOUNT/2))])


plt.plot(xGateResults, '--o', color=MAIN)
fig = plt.gcf()
ax = plt.gca()
ax.set_yticks([-1,1])
ax.set_yticklabels(["$\\vert 0\\rangle$", "$\\vert 1\\rangle$"])
ax.set_ylabel("$\\vert \\psi \\rangle$ - Quantum State")
ax.set_xlabel("$d$ - Number of $\\mathtt{X}$ gates")

plt.savefig("../Thesis/figures/coherentNoise_ideal.pdf", format="pdf", bbox_inches="tight")

plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

xGateResults_gateError = fctGenerator(0,0,1,GATEERROR,1,GATECOUNT)
# xGateResults_gateError = np.array([np.cos((np.pi+GATEERROR)*i) for i in range(0,GATECOUNT)])

plt.plot(xGateResults_gateError, '--o', color=MAIN)
fig = plt.gcf()
ax = plt.gca()

idealHull_A= fctGenerator(0,0,1,0,GATECOUNT+1)[0::2]
idealHull_B= fctGenerator(0,0,1,0,GATECOUNT+2)[1::2]
x = np.array([2*i for i in range(0,int(GATECOUNT/2))])
ax.plot(x, idealHull_A, color=LIGHTGRAY)
ax.plot(x, idealHull_B, color=LIGHTGRAY)
ax.fill_between(x,idealHull_A, idealHull_B, color=LIGHTGRAY)

ax.set_yticks([-1,1])
ax.set_yticklabels(["$\\vert 0\\rangle$", "$\\vert 1\\rangle$"])
ax.set_ylabel("$\\vert \\psi \\rangle$ - Quantum State")
ax.set_xlabel("$d$ - Number of $\\mathtt{X}$ gates")

plt.savefig("../Thesis/figures/coherentNoise_gateError.pdf", format="pdf", bbox_inches="tight")

plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

x = [0.0, 1.0]
startError = 0.08
startIdeal = 0.0
endError=0.8
endIdeal=1.0


fig = plt.gcf()
ax = plt.gca()
error=ax.plot(x, [startError, endError], color=HIGHLIGHT)
ideal=ax.plot(x, [startIdeal, endIdeal], color=MAIN)
ax.fill_between(x, [startError, endError], [startIdeal, endIdeal], color=LIGHTGRAY)
ax.set_yticks([startIdeal, startError, endError, endIdeal])
ax.set_ylabel("Probability $\\tilde p$ for $\\mathtt{\\tilde{M}}=1$")
ax.set_xlabel("Probability $p$ for $\\mathtt{M}=1$")
ax.legend([error, ideal], labels=["$\\epsilon=0.08 \\quad \\nu=0.2$", "$\\epsilon=0 \\quad \\nu=0$"], loc="upper left")

# plt.show()
plt.savefig("../Thesis/figures/coherentNoise_probabilityShift.pdf", format="pdf", bbox_inches="tight")

plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

xGateResults_gateErrorOffset = fctGenerator(MEASUREMENTOFFSETERROR,0,MEASUREMENTAMPLITUDEERROR,GATEERROR,1,GATECOUNT)
# xGateResults_gateErrorOffset = np.array([minmax(-1,1, MEASUREMENTOFFSETERROR+ MEASUREMENTAMPLITUDEERROR*np.cos((np.pi+GATEERROR)*i)) for i in range(0,GATECOUNT)])

plt.plot(xGateResults_gateErrorOffset, '--o', color=MAIN)
fig = plt.gcf()
ax = plt.gca()

idealHull_A= fctGenerator(0,0,1,GATEERROR,1,GATECOUNT+1)[0::2]
idealHull_B= fctGenerator(0,0,1,GATEERROR,1,GATECOUNT+2)[1::2]
x = np.array([2*i for i in range(0,int(GATECOUNT/2)+1)])
ax.plot(x, idealHull_A, color=LIGHTGRAY)
ax.plot(x, idealHull_B, color=LIGHTGRAY)
ax.fill_between(x,idealHull_A, idealHull_B, color=LIGHTGRAY)

ax.set_yticks([-1,1])
ax.set_yticklabels(["$\\vert 0\\rangle$", "$\\vert 1\\rangle$"])
ax.set_ylabel("$\\vert \\psi \\rangle$ - Quantum State")
ax.set_xlabel("$d$ - Number of $\\mathtt{X}$ gates")

plt.savefig("../Thesis/figures/coherentNoise_measurementError.pdf", format="pdf", bbox_inches="tight")


plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

xGateResults_gateErrorOffsetNoise = fctGenerator(MEASUREMENTOFFSETERROR,MEASUREMENTNOISINESS,MEASUREMENTAMPLITUDEERROR,GATEERROR,1,GATECOUNT)
# xGateResults_gateErrorOffsetNoise = np.array([minmax(-1,1, MEASUREMENTOFFSETERROR +
#                                                 MEASUREMENTNOISINESS*(0.5-(np.random.binomial(BINOMDRAWS, BINOMMEAN)))/BINOMDRAWS +
#                                                 MEASUREMENTAMPLITUDEERROR *
#                                                 np.cos((np.pi+GATEERROR)*i)) for i in range(0,GATECOUNT)])

plt.plot(xGateResults_gateErrorOffsetNoise, '--o', color=MAIN)
fig = plt.gcf()
ax = plt.gca()

idealHull_A= fctGenerator(MEASUREMENTOFFSETERROR,0,MEASUREMENTAMPLITUDEERROR,GATEERROR,1,GATECOUNT+1)[0::2]
idealHull_B= fctGenerator(MEASUREMENTOFFSETERROR,0,MEASUREMENTAMPLITUDEERROR,GATEERROR,1,GATECOUNT+2)[1::2]
x = np.array([2*i for i in range(0,int(GATECOUNT/2)+1)])
ax.plot(x, idealHull_A, color=LIGHTGRAY)
ax.plot(x, idealHull_B, color=LIGHTGRAY)
ax.fill_between(x,idealHull_A, idealHull_B, color=LIGHTGRAY)

ax.set_yticks([-1,1])
ax.set_yticklabels(["$\\vert 0\\rangle$", "$\\vert 1\\rangle$"])
ax.set_ylabel("$\\vert \\psi \\rangle$ - Quantum State")
ax.set_xlabel("$d$ - Number of $\\mathtt{X}$ gates")

# plt.show()
plt.savefig("../Thesis/figures/coherentNoise_measurementErrorNoise.pdf", format="pdf", bbox_inches="tight")

plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

xGateResults_gateErrorOffsetNoise = fctGenerator(MEASUREMENTOFFSETERROR,MEASUREMENTNOISINESS,MEASUREMENTAMPLITUDEERROR,GATEERROR,GATESHRINKING,GATECOUNT)
# xGateResults_gateErrorOffsetNoise = np.array([minmax(-1,1, MEASUREMENTOFFSETERROR +
#                                                 MEASUREMENTNOISINESS*(0.5-(np.random.binomial(BINOMDRAWS, BINOMMEAN)))/BINOMDRAWS +
#                                                 MEASUREMENTAMPLITUDEERROR *
#                                                 np.cos((np.pi+GATEERROR)*i)) for i in range(0,GATECOUNT)])

plt.plot(xGateResults_gateErrorOffsetNoise, '--o', color=MAIN)
fig = plt.gcf()
ax = plt.gca()

idealHull_A= fctGenerator(MEASUREMENTOFFSETERROR,0,MEASUREMENTAMPLITUDEERROR,GATEERROR,1,GATECOUNT+1)[0::2]
idealHull_B= fctGenerator(MEASUREMENTOFFSETERROR,0,MEASUREMENTAMPLITUDEERROR,GATEERROR,1,GATECOUNT+2)[1::2]
x = np.array([2*i for i in range(0,int(GATECOUNT/2)+1)])
ax.plot(x, idealHull_A, color=LIGHTGRAY)
ax.plot(x, idealHull_B, color=LIGHTGRAY)
ax.fill_between(x,idealHull_A, idealHull_B, color=LIGHTGRAY)

ax.set_yticks([-1,1])
ax.set_yticklabels(["$\\vert 0\\rangle$", "$\\vert 1\\rangle$"])
ax.set_ylabel("$\\vert \\psi \\rangle$ - Quantum State")
ax.set_xlabel("$d$ - Number of $\\mathtt{X}$ gates")

# plt.show()
plt.savefig("../Thesis/figures/coherentNoise_measurementErrorNoiseShrinking.pdf", format="pdf", bbox_inches="tight")

