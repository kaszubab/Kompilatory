
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys
import operator as op

sys.setrecursionlimit(10000)

class Interpreter(object):

    def __init__(self):
        self.memory_stack = MemoryStack()
        self.operators = {
            '+': op.add,
            '-': op.sub,
            '*': op.mul,
            '/': op.truediv,
            '.+': op.add,
            '.-': op.sub,
            '.*': op.mul,
            './': op.truediv,
            '<': op.lt,
            '>': op.gt,
            '<=': op.le,
            '>=': op.ge,
            '!=': op.ne,
            '==': op.eq,
        }
        self.special_assignments = {
            "+=": '+',
            "-=": '-',
            "*=": '*',
            "/=": '/'
        }

        self.initialization_functions = {
            "eye": lambda x, y : self.eye(x, y),
            "ones": lambda x, y : self.balanced(x, y, 1),
            "zeros": lambda x, y : self.balanced(x, y, 0),
        }

    def eye(self, x, y):
        matrix = []
        for i in range(x):
            matrix.append([])
            for j in range(y):
                matrix[i].append(0)
                if i == j:
                    matrix[i][j] = 1
        return matrix

    def balanced(self, x_val, y, value):
        matrix = []
        for i in range(x_val):
            matrix.append([])
            for j in range(y):
                matrix[i].append(value)
        return matrix

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Assigment)
    def visit(self, node):
        right = self.visit(node.right)

        if node.assigment_type in self.special_assignments:  # operator of type: +=, -=, *=, /=
            left = self.visit(node.left)
            try:
                right = self.operators[self.special_assignments[node.assigment_type]](left, right)
            except:
                print(
                    f'Runtime error: Invalid types {type(left)} {type(right)} with {self.special_assignments[node.assigment_type]}: line {node.lineno}')
                sys.exit(0)


        if isinstance(node.left, AST.Variable):
            self.memory_stack.insert(node.left.name, right)
            return right
        else:
            ref_dict = self.visit(node.left)
            variable = ref_dict['variable']
            ids = ref_dict['row']
            if(len(ids) == 1):
                if not isinstance(ids[0], range):
                    variable[ids[0]] = [right for i in variable[ids[0]]]
                else:
                    for i in ids[0]:
                        variable[i] = [right for i in variable[i]]

            if(len(ids) == 2):
                if not isinstance(ids[0], range) and not isinstance(ids[1], range):
                    variable[ids[0]][ids[1]] = right
                else:
                    if isinstance(ids[0], range) and not isinstance(ids[1], range):
                        for i in ids[0]:
                            variable[i][ids[1]] = right
                    elif isinstance(ids[1], range) and not isinstance(ids[0], range):
                        for i in ids[1]:
                            variable[ids[0]][i] = right
                    elif isinstance(ids[0], range) and  isinstance(ids[1], range):
                        for i in ids[0]:
                            for j in ids[1]:
                                variable[i][j] = right


    @when(AST.MatrixInitialization)
    def visit(self, node):
        value = self.visit(node.expression)
        if len(value) == 1:
            return self.initialization_functions[node.function](value[0], value[0])
        elif len(value) == 2:
            return self.initialization_functions[node.function](value[0], value[1])
        else:
            print(f'Invalid length {len(value)} for function {node.function}')
            sys.exit(0)

    @when(AST.Ref)
    def visit(self, node):
        return {'row': self.visit(node.matrix_row),
                'variable': self.memory_stack.get(node.id)
                }


    @when(AST.For)
    def visit(self, node):
        self.memory_stack.push('for_loop')
        loop_range = self.visit(node.range)
        for i in loop_range:
            self.memory_stack.insert(node.variable.name, i)
            try:
                self.visit(node.body)
            except BreakException:
                break
            except ContinueException:
                pass
        self.memory_stack.pop()

    @when(AST.While)
    def visit(self, node):
        self.memory_stack.push('while_loop')
        while self.visit(node.condition):
            try:
                self.visit(node.body)
            except BreakException:
                break
            except ContinueException:
                pass
        self.memory_stack.pop()

    @when(AST.If)
    def visit(self, node):
        self.memory_stack.push('if')
        if self.visit(node.condition):
            self.visit(node.if_block)
        elif node.else_block is not None:
            self.visit(node.else_block)
        self.memory_stack.pop()

    @when(AST.Break)
    def visit(self, node):
        raise BreakException

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(node.expresion)

    @when(AST.Range)
    def visit(self, node):
        begin = self.visit(node.begin)
        end = self.visit(node.end)
        return range(begin, end)

    @when(AST.Print)
    def visit(self, node):
        visited_row = self.visit(node.row)
        if isinstance(visited_row[0], dict):
            value = visited_row[0]
            print(value['variable'][value['row'][0]][value['row'][1]])
            return
        print(', '.join([str(elem) for elem in visited_row]))

    @when(AST.Row)
    def visit(self, node):
        return [self.visit(elem) for elem in node.elements]


    # Expressions
    @when(AST.BinExpr)
    def visit(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if(len(node.op) == 2):
            if len(left) != len(right):
                print(f'Invalid matrix dimensions {len(left)} x {len(left[0])} and {len(right)} x {len(right[0])}')
                sys.exit(0)
            elif len(left[0]) != len(right[0]):
                print(f'Invalid matrix dimensions {len(left)} x {len(left[0])} and {len(right)} x {len(right[0])}')
                sys.exit(0)
            else:
                matrix = [[] for i in left]
                for idx, el in enumerate(left):
                    for idx_i, el_i in enumerate(el):
                        matrix[idx].append(self.operators[node.op](el_i, right[idx][idx_i]))
                return matrix


        return self.operators[node.op](left, right)

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.Variable)
    def visit(self, node):
        return self.memory_stack.get(node.name)

        # Other

    @when(AST.Block)
    def visit(self, node):
        self.visit(node.instructions)

    @when(AST.Instructions)
    def visit(self, node):
        for element in node.elements:
            # print(element)
            self.visit(element)
            # print(element)
            # print("Instruction finished")

    @when(AST.Comparsion)
    def visit(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.operators[node.operator](left, right)


