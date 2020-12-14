from SymbolTable import *


compatible_types = {
    "INT": ["INT"],
    "FLOAT": ["INT", "FLOAT"],
    "STRING": ['STRING']
}



class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):
    def __init__(self):
        self.currentScope = None

    def report_error(self, lineno, msg):
        print("Found error in line: ", lineno, " error message: \n", msg)

    def visit_Instructions(self, node):
        if self.currentScope is None:
            self.currentScope = SymbolTable(None, 'instructions', '0')
        
        else:
            new_scope = SymbolTable(self.currentScope, 'instructions', self.currentScope.scope_level+1)
            self.currentScope = new_scope

        for elem in node.elements:
            self.visit(elem)


    def visit_Row(self, node):
        for elem in node.elements:
            self.visit(elem)

    def visit_Print(self, node):
        for elem in node.row.elements:
            self.visit(elem)

    def visit_Block(self, node):
        self.visit(node.instructions)

    def visit_If(self, node):
        self.visit(node.condition)

        parent_scope = self.currentScope

        if_scope = SymbolTable(parent_scope, 'if', parent_scope.scope_level+1)
        self.currentScope = if_scope
        self.visit(node.if_block)

        else_scope = SymbolTable(parent_scope, 'else', parent_scope.scope_level+1)
        self.currentScope = else_scope
        self.visit(node.else_block)
    
    def visit_While(self, node):
        self.visit(node.condition)

        parent_scope = self.currentScope

        body_scope = SymbolTable(parent_scope, 'while', parent_scope.scope_level+1)
        self.currentScope = body_scope
        self.visit(node.body)

    def visit_For(self, node):
        self.visit(node.variable)
        self.visit(node.range)

        

        parent_scope = self.currentScope

        for_scope = SymbolTable(parent_scope, 'for', parent_scope.scope_level+1)
        self.currentScope = for_scope

        if self.currentScope.get(node.variable.name) != None:
            self.report_error(node.lineno, f"{node.variable.name} has been already declared")

        self.currentScope.put(VariableSymbol(node.variable.name), BuiltinTypeSymbol("INTEGER"))
        
        self.visit(node.body)
        
    def visit_Break(self, node):
        if self.currentScope.check_if_in_loop():
            pass
        else:
            self.report_error(node.lineno, "break outside loop")

    
    def visit_Continue(self, node):
        if self.currentScope.check_if_in_loop():
            pass
        else:
            self.report_error(node.lineno, "continue outside loop")

    def visit_Return(self, node):
        self.visit(node.expresion)


    def visit_Range(self, node):
        self.visit(node.begin)
        self.visit(node.end)

        if node.begin.type == "INT":
            pass
        
        if node.begin.type == "ID":
            begin_var = self.currentScope.get(node.begin.name)
            if begin_var.type != "INTEGER":
                self.report_error(node.lineno, "Range must begin with integer")

        if node.end.type == "INT":
            pass
        
        if node.end.type == "ID":
            end_var = self.currentScope.get(node.begin.name)
            if end_var.type != "INTEGER":
                self.report_error(node.lineno, "Range must end with integer")


    def visit_Assigment(self, node):
        self.visit(node.left)
        self.visit(node.right)

        if node.left.type == "ID":
            left_type = self.currentScope.get(node.left.name) 
            right_type = node.right.type
            if left_type is not None:
                if  not right_type in compatible_types[left_type]:
                    self.report_error(node.lineno, f"Incompatible types: {left_type}, {right_type}")
            else:
                self.currentScope.put(VariableSymbol(node.left.name, node.right.type))
        
        #TODO trzeba sprawdzić czy typ macierzy jest zgodny z tym co po prawej
        if node.left.type == "REF":
            pass


    def visit_Comparsion(self, node):
        self.visit(node.left)
        self.visit(node.right)

        if not node.right.type in compatible_types[node.left.type]:
            self.report_error(node.lineno, f"Incompatible types: {node.left.type}, {node.right.type}")


    def visit_Transposition(self, node):
        pass

    
    #TODO przemyśleć czy tu nie trzeba więcej sprawdzać
    def visit_Ref(self, node):
        self.visit(node.matrix_row)
        
        if self.currentScope.get(node.id) is None:
            self.report_error(node.lineno, "Can't reference to not exisiting array")
    
    def visit_UnaryMinus(self, node):
        self.visit(node.expression)

        if node.expression.type not in ['ID', 'INT', 'FLOAT']:
            self.report_error(node.lineno, "Unary minus with wrong expression")
        
        #TODO sprawdzenie, czy dla typu zmiennej można zrobić unary minus
        if node.expresion.type == 'ID':
            if self.currentScope.get(node.expression.name) is None:
                self.report_error(node.lineno, f"Unexisting variable {node.expression}")


    #TODO 
    def visit_MartixInitalization(self, node):
        pass

    #TODO
    def visit_Vector(self, node):
        pass

    def visit_IntNum(self, node):
        pass
    
    def visit_FloatNum(self, node):
        pass

    def visit_String(self, node):
        pass

    def visit_Variable(self, node):
        pass

    #TODO
    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        # ... 
        #
 


