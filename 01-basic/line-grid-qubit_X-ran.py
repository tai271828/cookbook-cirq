#!/usr/bin/env python
"""
This script demos there is no difference between using LineQubit and
GridQubit in Cirq when developing an algorithm. The difference only matters
when implementing corresponding cicuits in real world.
"""
import cirq
import random


def simulate_and_measure(qubit, repetitions=10, mkey="m", power=0.1):
    """
    Simulate the circuit and get measurement.

    :param qubit: the input qubit
    :param repetitions: the repetitions of simulation, integer
    :param mkey: measurement type
    :param power: power of matrix, integer
    :return: (result, circuit) tuple
    """
    operations = [cirq.X(qubit)**power, cirq.measure(qubit, key=mkey)]

    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)

    return result, circuit


def demo(parameters):
    result, circuit = simulate_and_measure(*parameters)

    print("")
    print("Circuit:")
    print(circuit)
    print("")
    print("Results:")
    print(result)
    print(result.histogram(key=parameters[2]))
    print("")


for i in range(0, 11):
    i = i * 0.1
    input_parameters = [cirq.LineQubit(0), 100, "m", i]
    demo(input_parameters)


ranX = random.random()
print(f"ranX is {ranX}")
input_parameters = [cirq.LineQubit(0), 100, "m", ranX]
demo(input_parameters)
