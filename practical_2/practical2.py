# n_input = int(input("Enter no. of input symbols: "))
# input_symbols = input("Enter input symbols: ")
# input_symbols = input_symbols.split(" ")
# n_states = int(input("Enter no. of states: "))
# init_state = int(input("Enter initial state: "))
# n_accepting = int(input("Enter no. of accepting states: "))
# acc_state = input("Enter accpting states: ")
# acc_state = acc_state.split(" ")
# acc_state = [int(x) for x in acc_state]
# print(n_input)
# print(input_symbols)
# print(acc_state)
# print(acc_state[0] + acc_state[1])

def create_automata():
    num_symbols = int(input("Enter the number of input symbols: "))
    symbols = input(f"Enter the {num_symbols} input symbols separated by space: ").split()

    num_states = int(input("Enter the number of states: "))
    initial_state = int(input("Enter the initial state: "))

    num_accepting_states = int(input("Enter the number of accepting states: "))
    accepting_states = set(map(int, input(f"Enter {num_accepting_states} accepting states separated by space: ").split()))

    automata = [[-1 for _ in range(num_symbols)] for _ in range(num_states)]

    num_transition = num_states * num_symbols
    print("Enter the state transitions in the format: <from_state> <input_symbol> <to_state>")
    for _ in range(num_transition):
        from_state, symbol, to_state = input().split()
        from_state = int(from_state)
        to_state = int(to_state)
        symbol_index = symbols.index(symbol)
        automata[from_state][symbol_index] = to_state

    return automata, num_states, initial_state, accepting_states, symbols

def validate_string(automaton, input_string):
    automata, num_states, initial_state, accepting_states, symbols = automaton
    current_state = initial_state

    for symbol in input_string:
        if symbol not in symbols:
            print(f"Invalid symbol '{symbol}' in the input string.")
            return False
        symbol_index = symbols.index(symbol)
        next_state = automata[current_state][symbol_index]
        if next_state == -1:
            print(f"No transition from state {current_state} on symbol '{symbol}'.")
            return False
        current_state = next_state

    if current_state in accepting_states:
        print("Valid String")
        return True
    else:
        print("Invalid String")
        return False


def main():
    print("Hello, world")

    automaton = create_automata()

    input_string = input("Enter the input string: ")

    validate_string(automaton, input_string)

if __name__ == "__main__":
    main()



