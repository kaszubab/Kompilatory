from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

def print_with_intend(val, indent):
    print(indent * "| " + str(val))

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)
    
    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for e in self.elements:
            e.printTree(indent)

    @addToClass(AST.Row)
    def printTree(self, indent=0):
        for e in self.elements:
            e.printTree(indent)


    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.row.printTree(indent + 1)

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.condition.printTree(indent + 1)
        print_with_intend("THEN", indent)
        self.if_block.printTree(indent + 1)
        print_with_intend("ELSE", indent)
        self.else_block.printTree(indent + 1)


    @addToClass(AST.While)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.condition.printTree(indent + 1)
        self.body.printTree(indent + 1)
        

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.variable.printTree(indent + 1)
        self.range.printTree(indent + 1)
        self.body.printTree(indent + 1)


    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
    
   
    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.expresion.printTree(indent + 1)
    

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.begin.printTree(indent + 1)
        self.end.printTree(indent + 1)

    
    @addToClass(AST.Assigment)
    def printTree(self, indent=0):
        print_with_intend(self.assigment_type, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Comparsion)
    def printTree(self, indent=0):
        print_with_intend(self.operator, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)


    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.matrix.printTree(indent + 1)
        

    @addToClass(AST.Ref)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        print_with_intend(self.id, indent + 1)
        self.matrix_row.printTree(indent + 1)


    @addToClass(AST.UnaryMinus)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        self.expresion.printTree(indent + 1)
        

    @addToClass(AST.MatrixInitialization)
    def printTree(self, indent=0):
        print_with_intend(self.function, indent)
        self.expression.printTree(indent + 1)
    
    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print_with_intend(self.type, indent)
        for e in self.elements:
            e.printTree(indent + 1)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print_with_intend(self.value, indent)


    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print_with_intend(self.value, indent)


    @addToClass(AST.String)
    def printTree(self, indent=0):
        print_with_intend(self.value, indent)
    
    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print_with_intend(self.name, indent)


    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print_with_intend(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)
    

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass    
        # fill in the body


    # define printTree for other classes
    # ...

