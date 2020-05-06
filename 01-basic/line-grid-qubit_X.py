#!/usr/bin/env python
"""This script demos there is no difference between using LineQubit and
GridQubit in Cirq when developing an algorithm. The difference only matters
when implementing corresponding cicuits in real world."""
import cirq


def simulate_and_measure(qubit, repetitions=10, mkey="m"):
    """
    Simulate the circuit and get measurement.

    :param qubit: the input qubit
    :param repetitions: the repetitions of simulation, integer
    :param mkey: measurement type
    :return: (result, circuit) tuple
    """
    operations = [cirq.X(qubit), cirq.measure(qubit, key=mkey)]
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)

    return result, circuit


def demo(input_parameters):
    result, circuit = simulate_and_measure(*input_parameters)

    print("Circuit:")
    print(circuit)
    print("")
    print("Results:")
    print(result)
    print(result.histogram(key=input_parameters[2]))


input_parameters = [cirq.LineQubit(0), 10, "m"]
demo(input_parameters)

input_parameters = [cirq.GridQubit(0, 0), 10, "m"]
demo(input_parameters)

# Besides, the index of each qubit is only used for the indication of qubit ID.
# No matter what the index is, it does not impact the final measurement.
input_parameters = [cirq.LineQubit(1), 10, "m"]
demo(input_parameters)

input_parameters = [cirq.GridQubit(0, 1), 10, "m"]
demo(input_parameters)
