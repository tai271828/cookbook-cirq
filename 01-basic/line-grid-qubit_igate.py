#!/usr/bin/env python
import cirq


qubit = cirq.LineQubit(0)


gate_operation = cirq.I(qubit)
circuit = cirq.Circuit(gate_operation)


simulator = cirq.Simulator()
state_vector = simulator.simulate(circuit).final_state[0]


print()
print(state_vector)
print(circuit)

