print("Teleportation program started!")

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 3 qubits:
# q0 = Alice's original qubit
# q1 = Alice's half of the Bell pair
# q2 = Bob's qubit
#
# 3 classical bits:
# c0, c1 = Alice's measurement results
# c2 = Bob's final measurement

qc = QuantumCircuit(3, 3)

# ==========================================
# STEP 1: Prepare the state to teleport
# ==========================================

# Create |+> state on q0
qc.h(0)

# ==========================================
# STEP 2: Create a Bell pair
# ==========================================

# Put q1 into superposition
qc.h(1)

# Entangle q1 and q2
qc.cx(1, 2)

# ==========================================
# STEP 3: Alice's Bell-state measurement
# ==========================================

# Entangle q0 with q1
qc.cx(0, 1)

# Apply Hadamard to q0
qc.h(0)

# Measure Alice's two qubits
qc.measure(0, 0)
qc.measure(1, 1)

# ==========================================
# STEP 4: Bob's corrections
# ==========================================

# If c1 == 1, apply X to Bob's qubit
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

# If c0 == 1, apply Z to Bob's qubit
with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

# ==========================================
# STEP 5: Measure Bob's qubit
# ==========================================

qc.measure(2, 2)

# ==========================================
# Display circuit
# ==========================================

print("\nQuantum Teleportation Circuit:\n")
print(qc.draw())

# ==========================================
# Run simulation
# ==========================================

simulator = AerSimulator()

job = simulator.run(qc, shots=1000)
result = job.result()

print("\nMeasurement results:")
print(result.get_counts())