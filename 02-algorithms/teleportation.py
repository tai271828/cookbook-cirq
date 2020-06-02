import math
import random
import cirq


def main():
    circuit = cirq.Circuit()
    message, alice, bob = cirq.LineQubit.range(3)

    # Prepare the Bell state of Alice's and Bob's qubits
    # That is, making the entangled state of them
    circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])

    # Mock up the message state that will be sent by Alice
    # TODO: mocking in the random way
    circuit.append(cirq.I(message))

    # Bell measurement and get two classical bits
    circuit.append([cirq.CNOT(message, alice), cirq.H(message)])
    circuit.append(cirq.measure(message))
    circuit.append(cirq.measure(alice))

    # decode the state of the qubit owned by bob
    circuit.append([cirq.CNOT(alice, bob), cirq.CZ(message, bob)])

    # simulate the circuit
    simulator = cirq.Simulator()
    final_result = simulator.simulate(circuit)

    print(circuit)
    # The final_state should be one of the computation basis
    # |000> + |001> + |010> + |011> +
    # |100> + |101> + |110> + |111>
    #
    # Because the initial state of message is |0> and cirq.I does not change its state,
    # so the final_state should be 1x|000>
    print(final_result.final_state)


if __name__ == '__main__':
    main()
