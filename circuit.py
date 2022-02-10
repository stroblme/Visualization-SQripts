from blochBase import blochSphere
from statevectorBase import statevectorBase
from circuitBase import circuitBase

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, assemble, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_city, array_to_latex
from numpy import pi

NAMING="q"

q = QuantumRegister(2, name=NAMING)
qc = circuitBase(q)

qc.h(0)
qc.x(1)
qc.save('circuit_h0x1')

del(q, qc)

### Präsi begin
q = QuantumRegister(3, name=NAMING)
qc = circuitBase(q)
qc.save('circuit_3empty')

del(q, qc)

q = QuantumRegister(1, name=NAMING)
qc = circuitBase(q)
qc.h(0)
qc.save('circuit_h0_noMeas')

del(q, qc)

q = QuantumRegister(1, name=NAMING)
qc = circuitBase(q)
qc.x(0)
qc.y(0)
qc.z(0)
qc.rz(pi/4, 0)
qc.save('circuit_xyzp_noMeas')

del(q, qc)

q = QuantumRegister(2, name=NAMING)
qc = circuitBase(q)
qc.cx(0,1)
qc.cx(1,0)
qc.cx(0,1)
qc.swap(0,1)
qc.save('circuit_swap_cx')

### Präsi end

del(q, qc)

q = QuantumRegister(1, name=NAMING)
c = ClassicalRegister(1, name="meas")
qc = circuitBase(q, c)

qc.h(0)

svb = statevectorBase(qc)
svb.plotHistogram('circuit_h0_ideal')

qc.measure(q[0], c[0])
qc.save('circuit_h0')

svb = statevectorBase(qc)
svb.plotHistogram('hist_h0')

del(q, c, qc)

q = QuantumRegister(2, name=NAMING)
c = ClassicalRegister(2, name="meas")
qc = circuitBase(q, c)

qc.h(0)
qc.cx(q[0], q[1])

svb = statevectorBase(qc)
svb.plotHistogram('hist_h0cx01_ideal')

qc.measure(q[1], c[1])
qc.measure(q[0], c[0])
qc.save('circuit_h0cx01')

svb = statevectorBase(qc)
svb.plotHistogram('hist_h0cx01')

del(q, qc, svb)

q = QuantumRegister(1, name=NAMING)
qc = circuitBase(q)

# qc.x(0, label="$\\prod_d~\\mathtt{x}$")
qc.x(0, label="$\\mathtt{X}^{\otimes d}$")
qc.save('circuit_xd0')

del(q, qc)

q = QuantumRegister(1, name=NAMING)
qc = circuitBase(q)

qc.x(0, label="$\\mathtt{\\tilde G}$")
qc.save('circuit_g0')

del(q, qc)

q = QuantumRegister(1, name="case_a")
qc = circuitBase(q)

qc.x(0, label="$\\mathtt{I}$")
qc.x(0, label="$\\mathtt{G}$")
qc.save('circuit_i0g0')

del(q, qc)

q = QuantumRegister(1, name="case_b")
qc = circuitBase(q)

qc.x(0, label="$\\mathtt{X}$")
qc.x(0, label="$\\mathtt{G}$")
qc.save('circuit_x0g0')

del(q,qc)

q = QuantumRegister(2, name=NAMING)
qc = circuitBase(q)

qc.cx(0, 1)
qc.save('circuit_cx01')

del(q,qc)

q = QuantumRegister(2, name=NAMING)
qc = circuitBase(q)

qc.swap(0, 1)
qc.save('circuit_swap01')

del(q,qc)

q = QuantumRegister(2, name=NAMING)
qc = circuitBase(q)

qc.cx(1, 0)
qc.cx(0, 1)
qc.cx(1, 0)
qc.save('circuit_cx10cx01cx10')

del(q,qc)

epsilon = 0
def qft_rotations(circuit, n, minRotation=0, suppressPrint=True):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    global epsilon

    if n == 0:
        # epsilon += 0.03
        return circuit
    n -= 1
    circuit.h(n) # apply hadamard
    
    rotGateSaveCounter = 0
    # epsilon = 0.04 * random.randint(0,10)
    # epsilon = float(input('epsilon'))
    for qubit in range(n):
        # rot = pi/2**(n-qubit)
        rot = pi/2**(n-qubit) + epsilon
        if rot <= minRotation:
            rotGateSaveCounter += 1
            if not suppressPrint:
                print(f"Rotations lower than {minRotation}: is {rot}")
        else:
            circuit.cp(rot, qubit, n)

    # At the end of our function, we call the same function again on
    # the next qubits (we reduced n by one earlier in the function)
    if n != 0 and rotGateSaveCounter != 0 and not suppressPrint:
        print(f"Saved {rotGateSaveCounter} rotation gates which is {int(100*rotGateSaveCounter/n)}% of {n} qubits")
    qft_rotations(circuit, n, minRotation=minRotation, suppressPrint=suppressPrint)
    
def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft(circuit, n, minRotation=0, suppressPrint=False):
    """QFT on the first n qubits in circuit"""
    qft_rotations(circuit, n, minRotation=minRotation, suppressPrint=suppressPrint)
    swap_registers(circuit, n)
    # self.measure(circuit,n)
    return circuit

q = QuantumRegister(4, name=NAMING)
qc = circuitBase(q)

qc = qft(qc, 4, minRotation=0)

qc.save('circuit_qft_mr0')

del(q, qc)

q = QuantumRegister(4, name=NAMING)
qc = circuitBase(q)

qc = qft(qc, 4, minRotation=0.8)

qc.save('circuit_qft_mr08')

del(q, qc)


q = QuantumRegister(2, name=NAMING)
qc = circuitBase(q)

qc.cp(pi/4, 0, 1)

qc.save('circuit_cp01')