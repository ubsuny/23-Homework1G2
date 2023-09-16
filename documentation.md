<div style="text-align:center;">
  <img src="https://images.squarespace-cdn.com/content/v1/5d52f7bd9d7b3e0001819015/1576093121344-1Z1Q3H99J0C5JYRIO5OJ/my_circuit.png" alt="Adder_Circuit" width="800" height="350">
</div>

# Quantum Addition with Qiskit for Quantum Computer

This code demonstrates how to perform quantum addition of two classical numbers using Qiskit. It encodes the numbers into quantum states, applies quantum gates to perform the addition, and then measures the result.

Usage:
1. Define the classical numbers to be added (number1 and number2).
2. Determine the number of qubits needed to represent the numbers.
3. Create a quantum circuit with enough qubits.
4. Encode the classical numbers into quantum states using X gates.
5. Perform the addition by applying controlled-X (CNOT) gates.
6. Measure the result.
7. Simulate the circuit using the Qiskit simulator.
8. Get the measurement result and convert it to a decimal number.
9. Print the result and visualize it using a histogram.

Example:
For number1 = 30 and number2 = 2, the result of addition is calculated as 30 + 2 = 32.

```python
# Import necessary libraries
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram

# Define the classical numbers to be added
number1 = 30
number2 = 2

# Determine the number of qubits needed to represent the numbers
max_value = max(number1, number2)
num_qubits = max(1, (max_value.bit_length() + 1))

# Create a quantum circuit with enough qubits
qc = QuantumCircuit(num_qubits * 2, num_qubits)

# Encode the classical numbers into quantum states
for i in range(num_qubits):
    if (number1 >> i) & 1:
        qc.x(i)  # Apply X gate for 1 bits in number1
    if (number2 >> i) & 1:
        qc.x(i + num_qubits)  # Apply X gate for 1 bits in number2

# Perform the addition by applying CNOT gates
for i in range(num_qubits - 1):
    qc.ccx(i, i + num_qubits, i + num_qubits + 1)
    qc.cx(i, i + num_qubits)

# Measure the result
qc.measure(range(num_qubits, num_qubits * 2), range(num_qubits))

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1)
result = job.result()

# Get the measurement result
counts = result.get_counts(qc)
result_decimal = int(list(counts.keys())[0], 2)

# Print the result
print(f"The result of {number1} + {number2} is {result_decimal}")

# Visualize the measurement result using a histogram
print(counts)
plot_histogram(counts)
```