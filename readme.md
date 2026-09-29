# Quantum Computing Learning

A structured, hands-on journey through **Quantum Computing**, progressing from mathematical and conceptual foundations to gate-based quantum programming, quantum algorithms, variational methods, and analog neutral-atom computing.

This repository documents my learning through **small, reproducible implementations**, with the goal of understanding not only *how to write quantum code*, but also **why the underlying quantum mechanics and algorithms work**.

> **Learning principle:** Build → Run → Observe → Understand → Extend.

The projects are intentionally incremental. Each project introduces a new quantum concept and builds on the previous one.

---

## 👨‍💻 About This Learning Journey

I am a Computer Science undergraduate transitioning into **Quantum Computing and Quantum Information**, with particular interests in:

* Quantum Computing
* Quantum Algorithms
* Quantum Information Science
* Quantum Cryptography
* Post-Quantum Cryptography (PQC)
* Quantum-Safe Communication
* Neutral-Atom Quantum Computing
* Rydberg-Atom Quantum Computing
* Variational Quantum Algorithms
* Quantum Security

My broader goal is to develop a strong foundation that connects **computer science, quantum algorithms, quantum hardware, and quantum-safe security**.

This repository is one part of that journey.

---

# 🧭 Learning Roadmap

My current progression is:

```text
Quantum State Representation
          │
          ▼
    Quantum Measurement
          │
          ▼
     Qiskit Circuits
          │
          ├── Quantum Teleportation
          │
          ▼
     Quantum Algorithms
          │
          └── Grover's Search
          │
          ▼
 Variational Quantum Computing
          │
          └── Tiny VQE
          │
          ▼
 Analog Quantum Computing
          │
          ▼
 Neutral-Atom Computing
          │
          └── Rydberg Atoms
                 │
                 ▼
          Rydberg Blockade
                 │
                 ▼
       Maximum Independent Set
                 │
                 ▼
       Quantum Optimization
```

The repository will continue to evolve as I move toward more advanced topics.

---

# 📁 Projects

| #  | Project                                                              | Main Concept                                          | Technology   | Status         |
| -- | -------------------------------------------------------------------- | ----------------------------------------------------- | ------------ | -------------- |
| 01 | [Quantum Coin Flipper](#01--quantum-coin-flipper)                    | Superposition, amplitudes, measurement                | Python       | ✅ Completed    |
| 02 | [Quantum Teleportation](#02--quantum-teleportation-circuit)          | Entanglement, Bell states, classical correction       | Qiskit       | ✅ Completed    |
| 03 | [Grover's Search](#03--grovers-search)                               | Quantum search, phase oracle, amplitude amplification | Qiskit       | ✅ Completed    |
| 04 | [Tiny VQE](#04--tiny-vqe)                                            | Variational algorithms, Hamiltonians, optimization    | Qiskit + Aer | ✅ Completed    |
| 05 | [Rydberg / Analog Computing](#05--rydberg--analog-quantum-computing) | Neutral atoms, analog evolution, Rydberg interactions | QoolQit      | 🚧 In Progress |

---

# 01 — Quantum Coin Flipper

### File

```text
coin-flipper.py
```

### Objective

The first project establishes the fundamental idea of a **quantum state represented by amplitudes**.

Instead of beginning with a quantum-computing framework, this implementation uses pure Python to demonstrate the mathematics directly.

The simulated qubit is prepared in the equal superposition:

$$
|\psi\rangle =
\frac{1}{\sqrt{2}}|0\rangle +
\frac{1}{\sqrt{2}}|1\rangle
$$

The corresponding state vector is:

```text
[0.7071, 0.7071]
```

The amplitudes are converted into probabilities using the Born rule:

$$
P(x)=|\alpha_x|^2
$$

Therefore:

```text
P(0) ≈ 0.5
P(1) ≈ 0.5
```

### Example Output

```text
Amplitude of |0>: 0.7071067811865475
Amplitude of |1>: 0.7071067811865475

Probability of measuring 0: 0.4999999999999999
Probability of measuring 1: 0.4999999999999999

Measurement result: 0
```

### Concepts Learned

* Qubit state representation
* State vectors
* Probability amplitudes
* Born rule
* Quantum measurement
* Difference between amplitudes and probabilities
* Probabilistic nature of quantum measurement

### Why This Project Matters

Before using Qiskit or another framework, I wanted to understand the underlying representation of a qubit rather than treating a quantum circuit as a black box.

---

# 02 — Quantum Teleportation Circuit

### File

```text
teleportation-circuit.py
```

### Objective

Implement the **quantum teleportation protocol** using Qiskit.

Quantum teleportation demonstrates how an unknown quantum state can be transferred from one qubit to another using:

* Quantum entanglement
* Local quantum operations
* Classical communication
* Conditional quantum operations

No physical matter is teleported. The protocol transfers the **quantum state information**.

### Circuit Structure

The three qubits can be viewed as:

```text
q0 → Alice's original state
q1 → Alice's entangled qubit
q2 → Bob's qubit
```

The protocol follows approximately:

```text
Prepare quantum state
        │
        ▼
Create Bell pair
        │
        ▼
Alice performs Bell-basis operations
        │
        ▼
Measure Alice's two qubits
        │
        ▼
Classical information
        │
        ▼
Conditional X/Z corrections
        │
        ▼
Bob reconstructs the state
```

### Key Quantum Operations

The implementation uses:

* Hadamard gate `H`
* Controlled-NOT `CX`
* Pauli-X `X`
* Pauli-Z `Z`
* Quantum measurement
* Classical conditional operations

### Concepts Learned

* Superposition
* Entanglement
* Bell states
* Quantum measurement
* Classical bits vs quantum bits
* Conditional quantum operations
* Quantum communication protocols

### Example Simulation

The circuit was executed using Qiskit Aer, producing measurement statistics across multiple shots.

The presence of all three measured bits in the output also provided practical experience interpreting multi-qubit measurement results.

### Key Insight

Teleportation shows that quantum information can be transferred using **entanglement plus classical communication**, without physically transmitting the original qubit itself.

---

# 03 — Grover's Search

### File

```text
grover-search.py
```

### Objective

Implement a small instance of **Grover's quantum search algorithm**.

For the learning implementation, a two-qubit search space is used, with a marked target state.

For example:

```text
00
01
10
11  ← target
```

The algorithm demonstrates how quantum interference can amplify the probability of a desired state.

### Algorithm

The implementation follows the fundamental Grover structure:

```text
Initialize equal superposition
            │
            ▼
       Oracle
            │
            ▼
   Phase inversion
            │
            ▼
       Diffusion
            │
            ▼
Amplitude amplification
            │
            ▼
        Measurement
```

### Oracle

The oracle marks the target state by applying a phase flip.

For the two-qubit target:

```text
|11⟩
```

a controlled-Z operation can be used to introduce the required phase transformation.

### Diffusion Operator

The diffusion step performs the amplitude amplification process.

Conceptually:

```text
Wrong states
    ↓
Destructive interference

Target state
    ↓
Constructive interference
```

This is one of the most important ideas in Grover's algorithm: the algorithm does not simply "search faster" in a classical sense; it uses **quantum interference to redistribute probability amplitude** toward the marked state.

### Concepts Learned

* Quantum search
* Oracle construction
* Phase kickback / phase marking
* Amplitude amplification
* Quantum interference
* Diffusion operator
* Measurement statistics

### Broader Significance

Grover's algorithm provides an important example of how quantum algorithms can achieve a quadratic query-speedup for unstructured search:

$$
O(N) \rightarrow O(\sqrt{N})
$$

for the idealized oracle-query model.

---

# 04 — Tiny VQE

### File

```text
vqe-tiny.py
```

### Objective

Build a small implementation of the **Variational Quantum Eigensolver (VQE)**.

This project introduces the hybrid quantum-classical paradigm used by many near-term quantum algorithms.

Instead of directly calculating the ground-state energy, the algorithm searches for parameters that minimize the expectation value:

$$
E(\theta)=
\langle\psi(\theta)|H|\psi(\theta)\rangle
$$

### Hamiltonian

The learning example uses the simple Hamiltonian:

$$
H = Z_0 + Z_1
$$

The ground state is:

$$
|11\rangle
$$

with energy:

$$
E_{\min}=-2
$$

### Variational Circuit

The trial state is parameterized using rotation gates:

```text
|0⟩ ── Ry(θ₁) ──
|0⟩ ── Ry(θ₂) ──
```

The parameters are then optimized classically.

### Hybrid Loop

```text
Classical parameters
        │
        ▼
Parameterized quantum circuit
        │
        ▼
Quantum state
        │
        ▼
Expectation value
        │
        ▼
Classical optimizer
        │
        ▼
Updated parameters
        │
        └───────────────┐
                        │
                        ▼
                     Repeat
```

### Optimization Result

One successful run converged to approximately:

```text
theta1 ≈ π
theta2 ≈ π

Final energy ≈ -2.0
```

This matched the expected ground-state energy:

```text
Expected ground-state energy: -2
```

### Concepts Learned

* Hamiltonians
* Expectation values
* Variational quantum states
* Parameterized quantum circuits
* Hybrid quantum-classical algorithms
* Classical optimization
* Ground-state estimation
* Energy landscapes

### Important Note

This is intentionally a **toy VQE implementation**. The Hamiltonian is simple and the optimization method is educational rather than representative of a production chemistry or materials simulation.

The purpose is to understand the architecture of VQE before moving toward more realistic problems.

---

# 05 — Rydberg / Analog Quantum Computing

### File

```text
rydberg-mis.py
```

### Objective

Begin the transition from **gate-based quantum computing** to **analog neutral-atom quantum computing** using QoolQit.

This project explores a fundamentally different computational model where quantum evolution is described through physical parameters such as:

* Atom positions
* Laser amplitude
* Laser detuning
* Pulse duration
* Rydberg interactions

rather than constructing a circuit entirely from discrete gates.

---

## Neutral-Atom Computing

Neutral-atom quantum computers use individual atoms as quantum systems.

The atoms can be trapped and controlled using optical techniques, while laser fields manipulate their internal states.

A key concept is the **Rydberg state**.

When an atom is excited into a highly excited Rydberg state, its interaction with nearby Rydberg-excited atoms can become extremely strong.

---

# Rydberg Blockade

The central physical phenomenon I am studying in this project is the **Rydberg blockade**.

Conceptually:

```text
Atom A excited to Rydberg state
             │
             ▼
      Strong interaction
             │
             ▼
      Energy shift of B
             │
             ▼
B becomes off-resonant
             │
             ▼
Simultaneous excitation suppressed
```

For two atoms, the computational configurations can be represented as:

```text
00 → neither atom excited
01 → atom 1 excited
10 → atom 0 excited
11 → both atoms excited
```

The `11` configuration is particularly important when studying blockade.

---

## Current QoolQit Implementation

The current implementation constructs:

1. A two-atom register
2. An analog amplitude waveform
3. A detuning waveform
4. A quantum program
5. An analog device
6. Compilation to the device
7. Local quantum simulation
8. Measurement over 1,000 shots

Example register:

```python
register = qq.Register({
    0: (0.0, 0.0),
    1: (4.0, 0.0)
})
```

The program applies an analog drive to the atoms and then executes it using QoolQit's local emulator.

### Current Result

A representative run produced:

```text
Counter({
    '00': 991,
    '10': 7,
    '01': 2
})
```

with no `11` outcomes in 1,000 shots.

This demonstrates successful analog-program execution and measurement.

However, I am deliberately **not treating the absence of `11` alone as proof of Rydberg blockade**. The current pulse produces very little excitation overall, so the next stage is to design controlled experiments that distinguish low excitation probability from genuine interaction-induced blockade.

---

# 🔬 Next Rydberg Experiments

The next stage is to investigate the physics more systematically.

### Experiment A — Excitation Probability

Measure how the final-state distribution changes as the drive parameters are varied.

### Experiment B — Atom Separation

Compare atoms at different distances:

```text
Large separation
      ↓
Weak interaction

Small separation
      ↓
Strong Rydberg interaction
      ↓
Blockade regime
```

### Experiment C — Blockade Signature

Study whether the probability of simultaneous excitation:

$$
P(11)
$$

is suppressed specifically because of the interatomic interaction.

### Experiment D — Maximum Independent Set

Once the two-atom physics is understood, extend the system to graph-based optimization.

---

# 🧩 From Rydberg Blockade to Maximum Independent Set

A major motivation for this project is understanding how neutral-atom hardware can encode optimization problems.

The **Maximum Independent Set (MIS)** problem asks:

> What is the largest subset of vertices in a graph such that no two selected vertices share an edge?

For example:

```text
Graph:

A ─── B
│     │
C ─── D
```

An independent set cannot contain two vertices connected by an edge.

In a Rydberg-atom encoding:

```text
Graph vertex
     ↓
Physical atom

Graph edge
     ↓
Interaction relationship
```

The Rydberg blockade can naturally discourage neighboring atoms from simultaneously occupying the excited state.

This creates an interesting connection between:

```text
Graph theory
     +
Atomic physics
     +
Quantum dynamics
     =
Analog quantum optimization
```

The eventual goal of this project is to explore that mapping explicitly rather than treating MIS as a black-box library function.

---

# 🧠 Concepts Covered So Far

This repository currently covers concepts across several layers of quantum computing.

### Quantum Foundations

* Qubits
* State vectors
* Probability amplitudes
* Born rule
* Measurement
* Superposition

### Quantum Circuits

* Quantum gates
* Hadamard gates
* CNOT
* Pauli-X
* Pauli-Z
* Controlled operations
* Circuit measurement

### Quantum Information

* Entanglement
* Bell states
* Quantum teleportation
* Classical communication
* Quantum state transfer

### Quantum Algorithms

* Grover's algorithm
* Oracles
* Phase marking
* Amplitude amplification
* Quantum interference

### Variational Quantum Computing

* Hamiltonians
* Expectation values
* Parameterized circuits
* Variational states
* Classical optimization
* VQE
* Hybrid quantum-classical computation

### Analog / Neutral-Atom Computing

* Analog quantum evolution
* Neutral atoms
* Rydberg states
* Rydberg interactions
* Rydberg blockade
* Atom registers
* Laser amplitude
* Detuning
* Pulse waveforms
* Analog device constraints
* Graph-to-physics mappings
* Maximum Independent Set

---

# 🛠️ Technologies

### Programming

* Python

### Quantum Software

* Qiskit
* Qiskit Aer
* QoolQit

### Quantum Computing Models

```text
Gate-based quantum computing
        │
        └── Qiskit

Analog quantum computing
        │
        └── QoolQit

Neutral-atom quantum computing
        │
        └── Rydberg systems
```

---

# 📚 Learning Philosophy

I am intentionally avoiding a "copy a quantum circuit from a tutorial and run it" approach.

For each project, I try to understand four layers:

### 1. Physical / Mathematical Idea

What quantum phenomenon or mathematical structure is being used?

### 2. Algorithm

How does the quantum algorithm exploit that phenomenon?

### 3. Implementation

How is the algorithm represented in a quantum SDK?

### 4. Result

What does the simulator output actually mean?

This distinction is especially important when moving between **gate-based circuits and analog quantum computing**, because the programming abstractions become very different.

---

# 🔭 Future Learning Roadmap

The repository will gradually expand toward:

```text
Current
  │
  ├── Quantum foundations
  ├── Quantum circuits
  ├── Grover
  ├── VQE
  └── Rydberg analog computing
          │
          ▼
    Rydberg blockade
          │
          ▼
       MIS encoding
          │
          ▼
   Quantum optimization
          │
          ▼
   Quantum error concepts
          │
          ▼
 Quantum error correction
          │
          ▼
Quantum cryptography / QKD
          │
          ▼
Post-quantum cryptography
          │
          ▼
Quantum-safe systems
```

Longer term, I want to connect my quantum-computing work with my existing interest in **quantum-safe communication and post-quantum cryptography**, exploring the relationship between quantum algorithms, quantum hardware, and cybersecurity.

---

# 🔐 Connection to My Broader Quantum Work

This repository focuses specifically on **learning quantum computing through implementation**.

It complements my separate work on **QuantX**, a quantum-safe communication project focused on post-quantum cryptography.

The distinction is intentional:

```text
Quantum Computing Learning
        │
        ├── Quantum algorithms
        ├── Quantum circuits
        ├── VQE
        ├── Analog computing
        └── Neutral atoms
                 │
                 ▼
        Understanding quantum systems


QuantX
        │
        ├── ML-KEM / Kyber
        ├── ML-DSA / Dilithium
        ├── AES-GCM
        └── Quantum-safe communication
                 │
                 ▼
        Protecting classical systems
        against quantum-era threats
```

Together, these areas are helping me build a broader understanding of both **quantum computation and quantum-era cybersecurity**.

---

# 📈 Progress Tracking

| Area                        | Current Level            |
| --------------------------- | ------------------------ |
| Qubit fundamentals          | 🟢 Hands-on              |
| Quantum measurement         | 🟢 Hands-on              |
| Qiskit circuits             | 🟢 Hands-on              |
| Entanglement                | 🟢 Hands-on              |
| Quantum teleportation       | 🟢 Implemented           |
| Grover's algorithm          | 🟢 Implemented           |
| Variational algorithms      | 🟢 Implemented           |
| Hamiltonians                | 🟢 Introductory hands-on |
| Quantum optimization        | 🟡 Developing            |
| Analog quantum computing    | 🟡 Developing            |
| Neutral-atom computing      | 🟡 Developing            |
| Rydberg blockade            | 🟡 Investigating         |
| Rydberg MIS                 | 🟡 In progress           |
| Quantum error correction    | 🔵 Planned               |
| QKD                         | 🔵 Planned               |
| Advanced quantum algorithms | 🔵 Planned               |

The labels represent my **current learning stage**, not a claim of professional expertise.

---

# 🎯 What I Want This Repository to Demonstrate

Rather than presenting a collection of disconnected quantum scripts, I want this repository to document a progression:

> **I started with the mathematical representation of a qubit, moved into quantum circuits and information protocols, implemented quantum algorithms, learned the hybrid quantum-classical model, and then began exploring analog neutral-atom quantum computing.**

The purpose is not to claim mastery.

The purpose is to make the **learning process, technical understanding, experiments, and progression visible and reproducible**.

---

# 📌 Repository Structure

```text
quantum-computing-learning/
│
├── coin-flipper.py
├── teleportation-circuit.py
├── grover-search.py
├── vqe-tiny.py
├── rydberg-mis.py
│
└── README.md
```

As the repository grows, projects will be organized into progressively deeper sections.

---

# 🚀 Running the Projects

Clone the repository and install the required Python packages.

For the Qiskit projects:

```bash
pip install qiskit qiskit-aer
```

For the QoolQit project:

```bash
pip install qoolqit
```

Then run an individual project:

```bash
python coin-flipper.py
```

```bash
python teleportation-circuit.py
```

```bash
python grover-search.py
```

```bash
python vqe-tiny.py
```

```bash
python rydberg-mis.py
```

---

# 📖 References & Learning Resources

My learning is based on a combination of:

* Quantum computing textbooks and lecture material
* Qiskit documentation
* Qiskit educational material
* Quantum algorithm literature
* Neutral-atom and Rydberg quantum-computing literature
* Quantum-information resources
* Hands-on experimentation with simulators and quantum software

As the repository develops, I will add project-specific references and papers rather than treating this README as the only source of theory.

---

# 🌱 Status

**Active Learning Repository**

This repository is continuously evolving.

New projects will be added as I progress from introductory concepts toward more advanced quantum computing, quantum information, optimization, and quantum-security topics.

---

## ⭐ Why This Repository Exists

Quantum computing is a field where understanding the theory, algorithms, software abstractions, and physical implementation all matter.

I am using this repository to learn those layers progressively:

```text
Mathematics
    ↓
Quantum mechanics concepts
    ↓
Algorithms
    ↓
Quantum circuits
    ↓
Simulation
    ↓
Hardware models
    ↓
Quantum applications
```

**This is my ongoing attempt to learn quantum computing by building, testing, questioning, and understanding each layer.**

---

**Author:** Syed Marjan Ghazi
**Field:** Computer Science → Quantum Computing / Quantum Information / Quantum Security
**Repository:** Quantum Computing Learning
