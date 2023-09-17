# **Python code esigned to add two numbers using a quantum circuit:**
# Importing the required modules from the Qiskit library for quantum computing
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram

# Define a function to add two numbers using a quantum circuit.
def add_quantum(num1, num2, shots=1024):
    """
    Adds two numbers using a quantum circuit.

    Args:
        num1 (int): The first number to be added.
        num2 (int): The second number to be added.
        shots (int): The number of shots (measurements) to perform.

    Returns:
        int: The sum of num1 and num2.
    """
    # Determine the number of qubits needed to represent the numbers
    max_value = max(num1, num2)
    num_qubits = max(1, (max_value.bit_length() + 1))
# Here, num_qubits calculates the number of bits needed to represent that maximum value, 
#and adds 1 to ensure there's room for the carry bit in binary addition.
   
    # Create a quantum circuit with enough qubits
    qc = QuantumCircuit(num_qubits * 2, num_qubits) # Here, a quantum circuit (qc) is created with twice the number 
                                                    # of qubits as the sum, plus an additional num_qubits for the output.
    
    # Encode the classical numbers into quantum states
    for i in range(num_qubits):
        if (num1 >> i) & 1:
            qc.x(i)  # Apply X gate for 1 bits in num1
        if (num2 >> i) & 1:
            qc.x(i + num_qubits)  # Apply X gate for 1 bits in num2
 # This loop encodes the binary representation of num1 and num2 into the quantum circuit 
# by applying an X gate to each qubit where the corresponding bit is set to 1.
    
    # Perform the addition by applying CNOT gates
    for i in range(num_qubits - 1):
        qc.ccx(i, i + num_qubits, i + num_qubits + 1)
        qc.cx(i, i + num_qubits)

    # Measure the result
    qc.measure(range(num_qubits, num_qubits * 2), range(num_qubits))
#It measures the qubits in the output range and maps the 
# measurement results back to classical bits.
    
    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = execute(compiled_circuit, simulator, shots=shots)  # Specify the number of shots
    result = job.result()

    # Get the measurement result
    counts = result.get_counts(qc)
    result_decimal = int(list(counts.keys())[0], 2)
#This code retrieves the measurement counts and converts 
# the binary measurement result to a decimal integer.  
    return result_decimal, counts  # Return both the result and the counts
# The function returns both the result of the addition (result_decimal) and 
# the counts of different measurement outcomes.

# Example usage
number1 = 3
number2 = 2
shots = 1024  # Specify the number of shots
result, counts = add_quantum(number1, number2, shots=shots)
print(f"The result of {number1} + {number2} is {result}")

# Plot histogram of measurement outcomes
plot_histogram(counts)
