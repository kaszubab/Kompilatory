class Node(object):
    def __init__(self):
        self.type = "Node"


class Instructions(Node):
    def __init__(self, elem, elements=None):
        self.elements = []
        if elements:
            self.elements = elements.elements

        self.elements.append(elem)

class Row(Node):
    def __init__(self, elem, elements=None):
        self.elemetns = []
        if elements:
            self.elemetns = elements.elements

        self.elemetns.append(elem)


class Print(Node):
    def __init__(self, row):
        self.type = "PRINT"
        self.row = row
    

class Block(Node):
    def __init__(self, instructions):
        self.type = "BLOCK"
        self.instructions = instructions
    


class If(Node):
    def __init__(self, condition, if_block, else_block):
        self.type = "IF"
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class Else(Node):
    def __init__(self, else_block):
        self.else_block = else_block

class While(Node):
    def __init__(self, condition, body):
        self.type = "WHILE"
        self.condition = condition
        self.body = body

class For(Node):
    def __init__(self, variable, _range, body):
        self.type = "FOR"
        self.variable = variable,
        self.range = _range
        self.body = body

class Break(Node):
    def __init__(self):
        self.type = "BREAK"

class Continue(Node):
    def __init__(self):
        self.type = "CONTINUE"


class Return(Node):
    def __init__(self, expresion):
        self.type = "RETURN"
        self.expresion = expresion

class Range(Node):
    def __init__(self, begin, end):
        self.type = "RANGE"
        self.begin = begin
        self.end = end


class Assigment(Node):
    def __init__(self, assigment_type, left, right):
        self.assigment_type = assigment_type
        self.left = left
        self.right = right

class Comparsion(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class Transposition(Node):
    def __init__(self, matrix):
        self.type = "TRANSPOSE"
        self.matrix = matrix


class Ref(Node):
    def __init__(self, id, matrix_row):
        self.type = "REF"
        self.id = id
        self.matrix_row = matrix_row



class UnaryMinus(Node):
    def __init__(self, expression):
        self.type = "-"
        self.expression = expression

class MartixInitalization(Node):
    def __init__(self, function, expresion):
        self.function = function
        self.expresion = expresion


class Vector(Node):
    def __init__(self, elem, elements = None):
        self.type = "VECTOR"
        self.elements = elements if elements else []
        self.elements.append(elem)

class InnerVector(Node):
     def __init__(self, elem, elements=None):
        self.elements = []
        if elements:
            self.elements = elements.elements

        self.elements.append(elem)

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class String(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass