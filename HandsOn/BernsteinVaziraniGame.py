"""Bernstein-Vazirani interactive game.

Updated for modern Qiskit (>= 1.0):
- Replaces `from qiskit import *` with explicit imports.
- Replaces `Aer.get_backend("qasm_simulator")` with `AerSimulator()`.
- Replaces `execute(...)` (removed in Qiskit 1.0) with `transpile(...) + .run(...)`.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


secret_number = input("Enter a secret number \n")
try:
    secret_number = bin(int(secret_number))[2:]
except ValueError:
    print("you should give an integer")
    raise SystemExit(0)

qubit_number = len(secret_number)

circuit = QuantumCircuit(qubit_number + 1, qubit_number)
circuit.h(range(qubit_number))
circuit.x(qubit_number)
circuit.h(qubit_number)

for index, one in enumerate(reversed(secret_number)):
    if one == "1":
        circuit.cx(index, qubit_number)

circuit.h(range(qubit_number))
circuit.measure(range(qubit_number), range(qubit_number))

simulator = AerSimulator()
compiled = transpile(circuit, simulator)
result = simulator.run(compiled, shots=1).result()
counts = result.get_counts()
listOfCounts = list(counts.keys())
integer_number = int(listOfCounts[0], 2)

print(
    f"Your secret number is {integer_number} and it took only 1 shot to guess this "
    f"in a Quantum Computer. It would take {qubit_number} shots in classical computers."
)
