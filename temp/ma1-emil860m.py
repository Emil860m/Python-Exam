class CA:
    """Elementary Cellular Automaton - by emil860m Emil Fenger

    Represents a range 1, 3-cell neighbourhood elementary cellular automaton."""

    def __init__(self, rule, init_state='0' * 20 + '1' + '0' * 20):
        """Initialize the CA with the given rule and initial state."""
        # Initializing the state as well as the rule
        # The rule is contained in a dictionary with the keys being the 3 input cells and the values being outputs
        keys = [str(f'{b:03b}') for b in range(8)]
        values = [d for d in str(f'{rule:08b}')]
        self.rule = dict(zip(keys, values))
        self.current_state = init_state

    def state(self):
        """Returns the current state."""
        return self.current_state

    def next(self):
        """Progress one step and then return the current state."""
        # Can maybe be made more pythonic, but i can't even find better examples on the internet.
        # At least when using strings to store the state
        # Using fence posts in both ends of the state, since the first and last digit is calculated differently
        # than the rest
        line = self.current_state
        new_line = ""
        new_line += self.rule['0' + line[0] + line[1]]
        for i in range(1, len(line) - 1):
            new_line += self.rule[line[i - 1] + line[i] + line[i + 1]]
        new_line += self.rule[line[len(line) - 2] + line[len(line) - 1] + '0']
        self.current_state = new_line
        return self.current_state

    def run(self, num=18):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        # Calling state and printing
        # Calling next, n number of times and printing
        print(self.state().replace('0', ' ').replace('1', '*'))
        for i in range(num):
            print(self.next().replace('0', ' ').replace('1', '*'))


ca = CA(90)
ca.run(100)
