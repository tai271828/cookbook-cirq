#!/usr/bin/env python
"""
This script demos the difference between using repetitions option or not. By using the option, the simulation will
return a trial state but not wave function.
"""
import cirq
import random


def simulate_and_measure(qubit, repetitions=10, mkey="m", power=0.1, sim_mode="sim"):
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
    if sim_mode == "sim":
        result = simulator.simulate(circuit)
    else:
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
    if parameters[4] == "sim":
        print("no histogram in sim mode")
    else:
        print(result.histogram(key=parameters[2]))
    print(f"The type of the result is {type(result)}")
    print("")


ranX = random.random()
print(f"ranX is {ranX}")

input_parameters = [cirq.LineQubit(0), 100, "m", ranX, "sim"]
demo(input_parameters)

input_parameters = [cirq.LineQubit(0), 100, "m", ranX, "run"]
demo(input_parameters)