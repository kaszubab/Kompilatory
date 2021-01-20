class Memory:

    def __init__(self, memory_name):
        self.name = memory_name
        self.variables = {}

    def __contains__(self, variable_name):
        return variable_name in self.variables

    def get(self, variable_name):
        """Gets from memory current value of variable <variable_name>."""
        return self.variables[variable_name]

    def put(self, variable_name, value):
        """Puts into memory current value of variable <variable_name>."""
        self.variables[variable_name] = value


class MemoryStack:

    def __init__(self):
        self.stack = [Memory('global')]

    def get(self, variable_name):
        """Gets from memory stack current value of variable <variable_name>."""
        for memory in self.stack[::-1]:
            if variable_name in memory:
                return memory.get(variable_name)

        raise KeyError(f'{variable_name} was not defined')

    def insert(self, variable_name, value):
        """Inserts into memory stack variable <variable_name> with value <value>"""
        for memory in self.stack[::-1]:
            if variable_name in memory:
                memory.put(variable_name, value)
                break
            # if loop hadn't broken and reached global
            # memory then the variable hadn't been declared
            if memory.name == 'global':
                self.stack[-1].put(variable_name, value)

    def push(self, memory_name):
        """Pushes memory <memory> onto the stack."""
        self.stack.append(Memory(memory_name))

    def pop(self):
        """Pops the top memory from the stack."""
        self.stack.pop()