# This is the Unit Test
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram

# Define a function to add two numbers using a quantum circuit.
def add_quantum(num1, num2, shots=1024):
    # Determine the number of qubits needed to represent the numbers
    max_value = max(num1, num2)
    num_qubits = max(1, (max_value.bit_length() + 1))
    qc = QuantumCircuit(num_qubits * 2, num_qubits)
    
    # Encode the classical numbers into quantum states
    for i in range(num_qubits):
        if (num1 >> i) & 1:
            qc.x(i)  # Apply X gate for 1 bits in num1
        if (num2 >> i) & 1:
            qc.x(i + num_qubits)  # Apply X gate for 1 bits in num2

    # Perform the addition by applying CNOT gates
    for i in range(num_qubits - 1):
        qc.ccx(i, i + num_qubits, i + num_qubits + 1)
        qc.cx(i, i + num_qubits)

    # Measure the result
    qc.measure(range(num_qubits, num_qubits * 2), range(num_qubits))
    
    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = execute(compiled_circuit, simulator, shots=shots)  # Specify the number of shots
    result = job.result()

    # Get the measurement result
    counts = result.get_counts(qc)
    result_decimal = int(list(counts.keys())[0], 2) 
    return result_decimal, counts

# Unit tests
print("Unit Tests:")

number1 = 0
number2 = 0
shots = 1024  # Specify the number of shots
result1, counts = add_quantum(number1, number2, shots=shots)
print(f"The result of {number1} + {number2} is {result1}")

number3 = 1
number4 = 0
shots = 1024  # Specify the number of shots
result2, counts = add_quantum(number3, number4, shots=shots)
print(f"The result of {number3} + {number4} is {result2}")

number5 = 1
number6 = 1
shots = 1024  # Specify the number of shots
result3, counts = add_quantum(number5, number6, shots=shots)
print(f"The result of {number5} + {number6} is {result3}")
