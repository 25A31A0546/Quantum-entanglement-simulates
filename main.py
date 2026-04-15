import numpy as np

# ── Quantum Gates ──────────────────────────────────────────────
H = (1/np.sqrt(2)) * np.array([[1,  1],
                                 [1, -1]])   # Hadamard

I = np.eye(2)                                # Identity

CNOT = np.array([[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,1],
                  [0,0,1,0]])                # CNOT (entangler)

# ── Simulation ─────────────────────────────────────────────────
def simulate():
    # Step 0: Initial state |00>
    q0 = np.array([1.0, 0.0])
    initial = np.kron(q0, q0)               # [1, 0, 0, 0]

    # Step 1: Apply Hadamard to qubit 1
    H_full = np.kron(H, I)
    after_h = H_full @ initial              # superposition

    # Step 2: Apply CNOT → Bell State |Φ+>
    after_cnot = CNOT @ after_h             # entangled

    # Step 3: Measure
    probs = np.abs(after_cnot)**2
    labels = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    result = np.random.choice(labels, p=probs)

    return {
        "steps": [
            {
                "label": "Step 0 — Initial State",
                "state": initial.tolist(),
                "labels": labels,
                "description": "Both qubits initialized to |0⟩. Joint state is |00⟩. Like two routers freshly booted — tables empty, state known."
            },
            {
                "label": "Step 1 — After Hadamard Gate",
                "state": np.round(after_h, 4).tolist(),
                "labels": labels,
                "description": "Hadamard puts Qubit 1 into superposition. Like a hub broadcasting to all ports — signal exists in both paths simultaneously."
            },
            {
                "label": "Step 2 — After CNOT Gate (Entangled!)",
                "state": np.round(after_cnot, 4).tolist(),
                "labels": labels,
                "description": "CNOT creates the Bell State |Φ+⟩. Qubits are entangled — like two synchronized BGP neighbors sharing the same routing table state."
            }
        ],
        "probabilities": np.round(probs, 4).tolist(),
        "labels": labels,
        "measurement": result
    }
