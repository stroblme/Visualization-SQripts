from qiskit import QuantumCircuit, QuantumRegister, Aer, assemble, execute

from qiskit.quantum_info import Statevector

from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_city, array_to_latex

def get_bit_string(n, n_qubits):
    """Returns the binary string of an integer with n_qubits characters

    Args:
        n (int): integer to be converted
        n_qubits (int): number of qubits

    Returns:
        string: binary string
    """

    assert n < 2**n_qubits, 'n too big to binarise, increase n_qubits or decrease n'

    bs = "{0:b}".format(n)
    bs = "0"*(n_qubits - len(bs)) + bs

    return bs

class statevectorBase():
    def __init__(self, qc):
        self.simulator = Aer.get_backend('statevector_simulator')

        # Execute and get counts
        self.result = execute(qc, self.simulator).result()
        self.statevector = self.result.get_statevector(qc)
        self.counts = dict()
        for i in range(2**qc.num_qubits):
            bs=get_bit_string(i,qc.num_qubits)
            if bs in self.result.get_counts():
                self.counts[bs]=self.result.get_counts()[bs]
            else:
                self.counts[bs]=0

    def __save__(self, fig, name):
        fig.savefig(f"../Thesis/figures/{name}.pdf")

    def plotStateCity(self, name, title=None):
        fig = plot_state_city(self.statevector, title=title, color='#006a5b')
        self.__save__(fig, name)

    def plotHistogram(self, name, title=None):
        fig = plot_histogram(self.counts, title=title, color='#006a5b')
        self.__save__(fig, name)