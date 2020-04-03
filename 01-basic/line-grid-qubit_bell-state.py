"""This script demos there is no difference between using LineQubit and
GridQubit in Cirq when developing an algorithm. The difference only matters
when implementing corresponding cicuits in real world."""
import cirq


def simulate_and_measure(qregister, repetitions=10, mkey="m"):
    """
    Simulate the circuit and get measurement.

    :param qregister: in this case for Bell state, there are 2 qubits in a list
    :param repetitions: the repetitions of simulation, integer
    :param mkey: measurement type
    :return: (result, circuit) tuple
    """
    operations = [cirq.H(qregister[0]), cirq.measure(qregister[0], qregister[1], key=mkey)]
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


qregister = [cirq.LineQubit(0), cirq.LineQubit(1)]
input_parameters = [qregister, 10, "m"]
demo(input_parameters)

qregister = [cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)]
input_parameters = [qregister, 10, "m"]
demo(input_parameters)

# Besides, the index of each qubit is only used for the indication of qubit ID.
# No matter what the index is, it does not impact the final measurement.
qregister = [cirq.LineQubit(2), cirq.LineQubit(3)]
input_parameters = [qregister, 10, "m"]
demo(input_parameters)

qregister = [cirq.GridQubit(1, 1), cirq.GridQubit(1, 2)]
input_parameters = [qregister, 10, "m"]
demo(input_parameters)

# let's try a different measurement method
qregister = [cirq.LineQubit(0), cirq.LineQubit(1)]
input_parameters = [qregister, 10, "z"]
demo(input_parameters)

qregister = [cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)]
input_parameters = [qregister, 10, "z"]
demo(input_parameters)

# let's try more measurement repetitions
qregister = [cirq.LineQubit(0), cirq.LineQubit(1)]
input_parameters = [qregister, 1000, "m"]
demo(input_parameters)

qregister = [cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)]
input_parameters = [qregister, 1000, "m"]
demo(input_parameters)
