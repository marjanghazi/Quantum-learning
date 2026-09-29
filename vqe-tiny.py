import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("Tiny VQE started!")

# -------------------------------------------------
# Our 2-qubit Hamiltonian
#
# H = Z0 + Z1
#
# The ground-state energy is -2
# and the ground state is |11>
# -------------------------------------------------

simulator = AerSimulator(method="statevector")


# -------------------------------------------------
# Create a parameterized quantum circuit
# -------------------------------------------------

def create_circuit(theta1, theta2):

    qc = QuantumCircuit(2)

    # Prepare a trial state
    qc.ry(theta1, 0)
    qc.ry(theta2, 1)

    return qc


# -------------------------------------------------
# Calculate expectation value of Z
# -------------------------------------------------

def expectation_z(statevector, qubit):

    probabilities = np.abs(statevector) ** 2

    expectation = 0

    for index, probability in enumerate(probabilities):

        # Determine the qubit's bit value
        bit = (index >> qubit) & 1

        if bit == 0:
            expectation += probability
        else:
            expectation -= probability

    return expectation


# -------------------------------------------------
# Calculate total energy
#
# H = Z0 + Z1
# -------------------------------------------------

def calculate_energy(theta1, theta2):

    qc = create_circuit(theta1, theta2)

    qc.save_statevector()

    result = simulator.run(qc).result()

    statevector = result.get_statevector()

    z0 = expectation_z(statevector, 0)
    z1 = expectation_z(statevector, 1)

    energy = z0 + z1

    return energy


# -------------------------------------------------
# Start with random parameters
# -------------------------------------------------

theta1 = np.random.uniform(0, 2 * np.pi)
theta2 = np.random.uniform(0, 2 * np.pi)

print("\nInitial parameters:")
print("theta1 =", theta1)
print("theta2 =", theta2)

print("Initial energy:", calculate_energy(theta1, theta2))


# -------------------------------------------------
# Simple classical optimization
# -------------------------------------------------

learning_rate = 0.2
iterations = 50

for step in range(iterations):

    # Numerical gradient

    epsilon = 0.0001

    energy = calculate_energy(theta1, theta2)

    gradient_theta1 = (
        calculate_energy(theta1 + epsilon, theta2)
        - calculate_energy(theta1 - epsilon, theta2)
    ) / (2 * epsilon)

    gradient_theta2 = (
        calculate_energy(theta1, theta2 + epsilon)
        - calculate_energy(theta1, theta2 - epsilon)
    ) / (2 * epsilon)

    # Gradient descent

    theta1 -= learning_rate * gradient_theta1
    theta2 -= learning_rate * gradient_theta2

    if step % 5 == 0:
        print(
            f"Iteration {step:2d} | "
            f"Energy = {calculate_energy(theta1, theta2):.6f}"
        )


# -------------------------------------------------
# Final result
# -------------------------------------------------

final_energy = calculate_energy(theta1, theta2)

print("\nOptimization finished!")

print("Final theta1:", theta1)
print("Final theta2:", theta2)
print("Final energy:", final_energy)

print("\nExpected ground-state energy: -2")