import qoolqit as qq

# ==========================================
# 1. Create a 2-atom register
# ==========================================

register = qq.Register({
    0: (0.0, 0.0),
    1: (4.0, 0.0)
})

# ==========================================
# 2. Define the laser amplitude
# ==========================================

amplitude = qq.RampWaveform(
    duration=1.0,
    initial_value=0.0,
    final_value=0.2
)

# ==========================================
# 3. Define the laser detuning
# ==========================================

detuning = qq.ConstantWaveform(
    duration=1.0,
    value=0.0
)

# ==========================================
# 4. Create the laser drive
# ==========================================

drive = qq.Drive(
    amplitude=amplitude,
    detuning=detuning
)

# ==========================================
# 5. Create quantum program
# ==========================================

program = qq.QuantumProgram(
    register,
    drive
)

print("Before compilation:")
print(program)

# ==========================================
# 6. Create the QoolQit Analog Device
# ==========================================

device = qq.AnalogDevice()

print("\nDevice:")
print(device)

# ==========================================
# 7. Compile the program
# ==========================================

program.compile_to(device)

print("\nAfter compilation:")
print(program)

# ==========================================
# 8. Run on local emulator
# ==========================================

backend = qq.execution.LocalEmulator(
    num_shots=1000
)

job = backend.run(program)

# ==========================================
# 9. Get results
# ==========================================

results = job.results()

print("\nResults:")
print(results)

print("\nFinal bitstrings:")
print(results.final_bitstrings)