from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("Grover's Search started!")

# -------------------------------------------------
# We have 2 qubits -> 4 possible states:
#
# 00
# 01
# 10
# 11
#
# Our hidden target will be: 11
# -------------------------------------------------

qc = QuantumCircuit(2, 2)

# -------------------------------------------------
# STEP 1: Create equal superposition
# -------------------------------------------------

qc.h(0)
qc.h(1)

# -------------------------------------------------
# STEP 2: Oracle
#
# Mark the target state |11>
# The CZ gate changes the phase of |11>
# -------------------------------------------------

qc.cz(0, 1)

# -------------------------------------------------
# STEP 3: Diffusion operator
#
# This amplifies the amplitude of the marked state
# -------------------------------------------------

qc.h(0)
qc.h(1)

qc.x(0)
qc.x(1)

qc.h(1)
qc.cx(0, 1)
qc.h(1)

qc.x(0)
qc.x(1)

qc.h(0)
qc.h(1)

# -------------------------------------------------
# STEP 4: Measure
# -------------------------------------------------

qc.measure(0, 0)
qc.measure(1, 1)

# -------------------------------------------------
# Display circuit
# -------------------------------------------------

print("\nGrover Circuit:\n")
print(qc.draw())

# -------------------------------------------------
# Run simulation
# -------------------------------------------------

simulator = AerSimulator()

job = simulator.run(qc, shots=1000)
result = job.result()

print("\nSearch results:")
print(result.get_counts())