#!/usr/bin/env python
import cirq


qregister = [cirq.LineQubit(0)]
operations = [cirq.H(qregister[0]), cirq.measure(qregister[0])]
circuit = cirq.Circuit(operations)
simulator = cirq.Simulator()
result = simulator.simulate(circuit)

print(result)
print(circuit)
