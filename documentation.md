
## Basic idea: Steps to implement a classical operation on a Quantum Computer:
1. **Quantum Circuit**: Think of a quantum circuit as a set of instructions for the quantum computer. Just like a recipe guides a chef in the kitchen, a quantum circuit guides the quantum computer in performing specific tasks.
2. **Encoding**: When you want to add two numbers, the first step is to encode these numbers into a quantum state. This is like translating the numbers into a language that the quantum computer understands. If you have the numbers 3 and 2, you would represent them as a set of qubits in a specific way.
3. **Quantum Addition**: The heart of the process involves performing addition using quantum gates and operations. This step is where the quantum magic happens. Quantum gates are like specialized tools that the quantum computer uses to manipulate the qubits in a way that simulates addition.
4. **Measurement**: After the quantum addition, we need to find out the result. Measurement is the process of checking what the qubits look like after the quantum operations. The result is often probabilistic, meaning there can be multiple possible outcomes.
5. **Simulation or Real Quantum Computer**: At this stage, you decide whether to run the code on a quantum simulator (a software-based quantum computer emulator) or on a real quantum computer. Simulators are like virtual quantum computers, while real quantum computers are physical machines designed to perform quantum computations.
6. **Execution**: If you choose a quantum simulator, you run your quantum circuit on it. If you choose a real quantum computer, you send your quantum circuit to the machine for execution.
7. **Result**: After execution, you receive a result. In the case of addition, this result represents the sum of the two numbers you encoded in the beginning.

Now, you can either write code on an IDE or use IBM's composer to construct quantum circuits like half or full adder in GUI.

<div style="text-align:center;">
  <img src="https://images.squarespace-cdn.com/content/v1/5d52f7bd9d7b3e0001819015/1576093121344-1Z1Q3H99J0C5JYRIO5OJ/my_circuit.png" alt="Adder_Circuit" width="750" height="350">
</div>

## 1. Writing code (Using ChatGPT)
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
For num1 = 1 and num2 = 1, the result of addition is calculated as 1 + 1 = 2.

```python
# Import necessary libraries
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram

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

    # Create a quantum circuit with enough qubits
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
        """
        Performs quantum addition using controlled-X gates.

        This function performs quantum addition by applying controlled-X (CNOT) gates to the qubits. 
        It iterates through the qubits and applies CNOT gates to perform the addition operation.

        Args:
            i (int): The index of the qubit being operated on.
        """


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

    return result_decimal, counts  # Return both the result and the counts

# Example usage
number1 = 3
number2 = 2
shots = 1024  # Specify the number of shots
result, counts = add_quantum(number1, number2, shots=shots)
print(f"The result of {number1} + {number2} is {result}")

# Plot histogram of measurement outcomes
plot_histogram(counts)

```

# 2. Constructing half adder circuit (using IBM composer)
## Truth Table
![image](https://github.com/ubsuny/23-Homework1G2/assets/143649367/42201d3d-491c-4e8f-a65f-0f3d4a30f300)

### Adding 1+1
![hald_adder](https://github.com/Pranjal-Srivastava-2023/23-Homework1G2_forked/assets/143828394/8d061657-4037-4c15-bb97-ddd201f15e7e)
output = carry = 1 and sum = 0
### Adding 0+1
![half_adder2](https://github.com/ubsuny/23-Homework1G2/assets/143828394/cc8a59de-5c20-40e2-8848-1d11511bb3fc)
output = carry = 0 and sum = 1
### Adding 1+0
![ha_one_zero](https://github.com/s4il3sh/23-Homework1G2/assets/144289804/ed83dc76-8cce-4b0d-9656-7d67ba1cf37d)
output = carry = 0 and sum = 1
### Adding 0+0
![ha_zero_zero](https://github.com/s4il3sh/23-Homework1G2/assets/144289804/7d102862-b6d9-43b9-9244-96a516c90484)
output = carry = 0 and sum = 0

# Limitation of the Quantum Computer
1) High cost: Quantum computers are very expensive to build and maintain. This is because they require specialized hardware and operating environments.
2) Noise and errors: Quantum computers are more prone to noise and errors than traditional computers. This is because qubits are very sensitive to their environment.
3) Scalability: It is difficult to build and scale quantum computers. This is because qubits are difficult to control and manipulate.
4) Software development: Developing software for quantum computers is challenging. This is because quantum algorithms are very different from classical algorithms.
5) Security risks: Quantum computers could be used to break current encryption algorithms. This could pose a threat to data security and privacy.
6) The problem of the quantum full-adder circuit is not very efficient. It requires a large number of qubits and gates, and it is very susceptible to errors. So, it is not yet possible to add large numbers on a quantum computer faster than on a classical computer.


