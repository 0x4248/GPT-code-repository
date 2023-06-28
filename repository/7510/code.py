import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

class QuantumSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def apply_gate(self, gate, targets):
        """Applies a quantum gate to the specified qubits."""
        self.circuit.gate(gate, targets)

    def measure(self, targets):
        """Performs a measurement on the specified qubits."""
        self.circuit.measure(targets)

    def simulate(self):
        """Simulates the quantum circuit and returns the resulting state."""
        simulator = Aer.get_backend('statevector_simulator')
        transpiled_circuit = transpile(self.circuit, simulator)
        qobj = assemble(transpiled_circuit)
        result = simulator.run(qobj).result()
        state = result.get_statevector()
        return state

    def visualize(self):
        """Visualizes the quantum circuit."""
        print(self.circuit.draw())

# Main program
if __name__ == '__main__':
    num_qubits = 3
    simulator = QuantumSimulator(num_qubits)

    # Apply quantum gates
    simulator.apply_gate("h", [0])
    simulator.apply_gate("cx", [0, 1])
    simulator.apply_gate("x", [2])

    # Perform measurement
    simulator.measure([0, 1, 2])

    # Simulate and visualize the circuit
    state = simulator.simulate()
    simulator.visualize()

    print("Final state:", state)
