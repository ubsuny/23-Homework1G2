## Steps to implement a classical operation on a Quantum Computer:

1. **Quantum Circuit**: Think of a quantum circuit as a set of instructions for the quantum computer. Just like a recipe guides a chef in the kitchen, a quantum circuit guides the quantum computer in performing specific tasks.
2. **Encoding**: When you want to add two numbers, the first step is to encode these numbers into a quantum state. This is like translating the numbers into a language that the quantum computer understands. If you have the numbers 3 and 2, you would represent them as a set of qubits in a specific way.
3. **Quantum Addition**: The heart of the process involves performing addition using quantum gates and operations. This step is where the quantum magic happens. Quantum gates are like specialized tools that the quantum computer uses to manipulate the qubits in a way that simulates addition.
4. **Measurement**: After the quantum addition, we need to find out the result. Measurement is the process of checking what the qubits look like after the quantum operations. The result is often probabilistic, meaning there can be multiple possible outcomes.
5. **Simulation or Real Quantum Computer**: At this stage, you decide whether to run the code on a quantum simulator (a software-based quantum computer emulator) or on a real quantum computer. Simulators are like virtual quantum computers, while real quantum computers are physical machines designed to perform quantum computations.
6. **Execution**: If you choose a quantum simulator, you run your quantum circuit on it. If you choose a real quantum computer, you send your quantum circuit to the machine for execution.
7. **Result**: After execution, you receive a result. In the case of addition, this result represents the sum of the two numbers you encoded in the beginning.

Now, you can either write code on an IDE or use IBM's composer to construct quantum circuits like half or full adder in GUI.

## 1. Writing code (Using ChatGPT)
## Quantum Addition with Qiskit

This code demonstrates how to perform quantum addition of two classical numbers using Qiskit. It encodes the numbers into quantum states, applies quantum gates to perform the addition, and then measures the result.

Algorithm:
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
For num1 = 1 and num2 = 1, the result of addition is calculated as 1 + 1 = 2. The result is probabilistic in nature. We make the measurement 1024 times these are called shots. So, 1 + 1 is not always 2.

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

    """
    Simulates the quantum circuit using the Qiskit Aer simulator.

    This function simulates the given quantum circuit using the Qiskit Aer simulator. It compiles the circuit,specifies the number of shots for measurements, and returns the simulation result.

  Args:
        qc (QuantumCircuit): The quantum circuit to be simulated.
        shots (int): The number of shots (measurements) to perform.

    Returns:
        Result: The result of the quantum circuit simulation.
    """


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
## Limitations of the code quantum_addition.py
The unit test results are:
-  1 + 0 = 0
-  1 + 1 = 2
-  0 + 0 = 0

However, it is not working correctly for certain input numbers,

-  7 + 7 = 10
-  1 + 15 = 12
-  15 + 15 = 10

These discrepancies are due to several reasons:
- The binary addition of these numbers requires an extra bit for the carry. If the code doesn't account for this properly, it may produce incorrect results.
-  Even for relatively small numbers, if the quantum circuit has a strict limit on the number of qubits (e.g., 5 qubits), it will fail to represent and compute the sum correctly.
-  In some cases where one number is significantly smaller than the other, then the code doesn't correctly handle mixed-size inputs, it may produce incorrect results.
-  If the binary representation of either number exceeds the available qubits, it will cause issues.
-  The binary addition is performed using CNOT gates. If the number of qubits is insufficient to perform the addition, it will result in incorrect or unexpected behavior.

## 2. Constructing half adder circuit (using IBM composer)
## Truth Table (half adder)
![image](https://github.com/ubsuny/23-Homework1G2/assets/143649367/42201d3d-491c-4e8f-a65f-0f3d4a30f300)

## Adding 1+1
![hald_adder](https://github.com/Pranjal-Srivastava-2023/23-Homework1G2_forked/assets/143828394/8d061657-4037-4c15-bb97-ddd201f15e7e)

## Explanation
 The following steps are performed:
- Start with all qubits in the |0⟩ state, which represents binary 0.
- Apply a NOT gate to q0 and q1. This operation flips their states from |0⟩ to   |1⟩, representing the inputs 1 and 1, respectively.
- Next, apply a CNOT gate from q0 to q2. The CNOT gate flips the state of   q2   (controlled qubit) if and only if q0 (target qubit) is in the |1⟩ state.       This represents the XOR operation between q0 and q2, which results in q2       being in the |1⟩ state if q0 is in the |1⟩ state. This represents the sum      bit.
- Also apply another CNOT gate from q1 to q2. This represents the XOR            operation between q1 and q2, which results in q2 being in the |1⟩ state if     q1 is in the |1⟩ state.
- Finally, apply a CCNOT (Toffoli) gate from q0 and q1 to q3. The CCNOT gate     is a controlled-controlled-X gate that flips the state of q3 if both q0 and    q1 are in the |1⟩ state and the result is stored in q3 as the carry bit.

  After these operations, we will have the following results:

    - q2 will be in the |0⟩ state, representing the sum bit, and get 0 as the sum.
    - q3 will be in the |1⟩ state, representing the carry bit, which is 1 as a       carry.
  So, in this circuit, we've successfully performed the half-adder operation     for 1+1, resulting in sum=0 and carry=1.
- The measurement for this operation was made using ibm_perth quantum computer and

  ## Results
  ```python
  {
  "quasi_dists": [
    {
      "10": 0.816048498403436,
      "11": 0.03503644534795631,
      "00": 0.07111106824997514,
      "01": 0.07780398799863257
    }
  ],
  "metadata": [
    {
      "shots": 1024,
      "readout_mitigation_overhead": 1.683986607946126,
      "readout_mitigation_time": 0.09256109222769737
    }
  ]

## Adding 0+1
We simply use another NOT Gate to flip |1⟩ to |0⟩ in q[0]. The rest of the working is same as the previous circuit.
![half_adder2](https://github.com/ubsuny/23-Homework1G2/assets/143828394/cc8a59de-5c20-40e2-8848-1d11511bb3fc)

## Limitations of the Quantum Computer
Quantum computers, including those used in platforms like IBM Quantum Composer, have several limitations when it comes to designing circuits and solving practical problems.

1) Exponential State Space: Quantum computers face the challenge of an exponentially growing state space as the number of qubits increases. This makes it impractical to represent and manipulate all possible states for certain types of computations. Each additional qubit doubles the number of potential quantum states, leading to an exponential increase in the size of the quantum state space.

2) Limited Software Ecosystem: Quantum software tools and libraries are still in their early stages of development, which can make it challenging for users to design and implement quantum circuits efficiently.

3) Gate Errors: Quantum gates are not perfect, and gate errors can accumulate in complex quantum circuits, making it difficult to perform long and accurate computations.

4) Error rates: For example, the X gate flips the state of a qubit, changing |0⟩ to |1⟩ and vice versa. Error rates for a gate like the X gate can vary depending on the quantum hardware and environmental conditions.

5) Scalability Challenges: Building large-scale, fault-tolerant quantum computers is a significant engineering challenge.

6) Qubit Decoherence: Quantum states are fragile and can easily lose their coherence, leading to errors in computations.

7) High cost: Quantum computers are very expensive to build and maintain. This is because they require specialized hardware and operating environments.
  
8) Noise and errors: Quantum computers are more prone to noise and errors than traditional computers. This is because qubits are very sensitive to their environment.
