from SymbolTable import *
import AST


compatible_types = {
    "INTEGER": ["INTEGER"],
    "FLOAT": ["INTEGER", "FLOAT"],
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

    def get_type(self, node):
        if node.type == "INTEGER":
            return Integer()
        elif node.type == "FLOAT":
            return Float()
        elif node.type == "STRING":
            return String()
        elif node.type == "VECTOR":
            return Vector(self.get_type(node.elements[0]))
        elif node.type == "-":
            return self.get_type(node.expresion)
        elif node.type == "TRANSPOSE":
            return self.get_type(node.matrix)
        else:
            self.report_error(node.lineno, "Illegal type")
            return None

    def check_vector(self, vector):
        def same_type(elems):
            first_elem_type = self.get_type(elems[0])
            for elem in elems[1:]:
                if self.get_type(elem) != first_elem_type:
                    return False
            return True
        
        def check_dimensions(elems):
            first_len = len(elems[0].elements)
            for elem in elems[1:]:
                if len(elem.elements) != first_len:
                    return False
            
            return True
        
        if not same_type(vector.elements):
            self.report_error(vector.lineno, "Vector with elements of different types")
            
        if vector.elements[0].type == "VECTOR":
            if not check_dimensions(vector.elements):
                self.report_error(vector.lineno, "Vector of vectors of different length")
        

    def visit_Instructions(self, node):
        if self.currentScope is None:
            self.currentScope = SymbolTable(None, 'instructions', 0)
        
        else:
            new_scope = SymbolTable(self.currentScope, 'instructions', self.currentScope.scope_level+1)
            self.currentScope = new_scope

        for elem in node.elements:
            self.visit(elem)

        self.currentScope = self.currentScope.getParentScope()


    def visit_Row(self, node):
        for elem in node.elements:
            self.visit(elem)

    def visit_Print(self, node):
        self.visit(node.row)

    def visit_Block(self, node):
        new_scope = SymbolTable(self.currentScope, 'block', self.currentScope.scope_level+1)
        self.currentScope = new_scope
        self.visit(node.instructions)
        self.currentScope = self.currentScope.getParentScope()

    def visit_If(self, node):
        self.visit(node.condition)

        parent_scope = self.currentScope

        if_scope = SymbolTable(parent_scope, 'if', parent_scope.scope_level+1)
        self.currentScope = if_scope
        self.visit(node.if_block)

        else_scope = SymbolTable(parent_scope, 'else', parent_scope.scope_level+1)
        self.currentScope = else_scope
        self.visit(node.else_block)

        self.currentScope = parent_scope
    
    def visit_While(self, node):
        self.visit(node.condition)

        parent_scope = self.currentScope

        body_scope = SymbolTable(parent_scope, 'while', parent_scope.scope_level+1)
        self.currentScope = body_scope
        self.visit(node.body)

        self.currentScope = parent_scope

    def visit_For(self, node):
        self.visit(node.variable)
        self.visit(node.range)

        parent_scope = self.currentScope

        for_scope = SymbolTable(parent_scope, 'for', parent_scope.scope_level+1)
        self.currentScope = for_scope

        if self.currentScope.get(node.variable.name) != None:
            self.report_error(node.lineno, f"{node.variable.name} has been already declared")

        self.currentScope.put(VariableSymbol(node.variable.name, "INTEGER"))
        
        self.visit(node.body)
        
        self.currentScope = parent_scope


    def visit_Break(self, node):
        if not self.currentScope.check_if_in_loop():
            self.report_error(node.lineno, "break outside loop")

    
    def visit_Continue(self, node):
        if not self.currentScope.check_if_in_loop():
            self.report_error(node.lineno, "continue outside loop")

    def visit_Return(self, node):
        self.visit(node.expresion)


    def visit_Range(self, node):
        begin = node.begin
        end = node.end

        if begin.type != "INTEGER" and begin.type != "ID" and begin.type != '-':
            self.report_error(node.lineno, "Range must begin with integer")

        if end.type != "INTEGER" and end.type != "ID" and end.type != '-':
            self.report_error(node.lineno, "Range must end with integer")

        if begin.type == "ID":
            begin_var = self.currentScope.get(begin.name)
            if begin_var.type != "INTEGER":
                self.report_error(node.lineno, "Range must begin with integer")

        if end.type == "ID":
            end_var = self.currentScope.get(end.name)
            if not isinstance(end_var.type, Integer):
                self.report_error(node.lineno, "Range must end with integer")

        if begin.type == '-':
            if begin.expression.type != "INTEGER" and begin.expression.type != 'ID':
                self.report_error(node.lineno, "Range must begin with integer")
            
            if begin.expression.type == 'ID':
                begin_var = self.currentScope.get(begin.expression.name)
                if not isinstance(begin_var.type, Integer):
                    self.report_error(node.lineno, "Range must begin with integer")

        if end.type == '-':
            if end.expression.type != "INTEGER" and end.expression.type != 'ID':
                self.report_error(node.lineno, "Range must end with integer")
            
            if end.expression.type == 'ID':
                end_var = self.currentScope.get(end.expression.name)
                if not isinstance(end_var.type, Integer):
                    self.report_error(node.lineno, "Range must end with integer")

        self.visit(node.begin)
        self.visit(node.end)


    def visit_Assigment(self, node):
        self.visit(node.right)

        if node.left.type == "ID":
            
            
            self.currentScope.put(VariableSymbol(node.left.name, self.get_type(node.right)))
        
        elif node.left.type == "REF":
            self.visit(node.left)
            
            left_var = self.currentScope.get(node.left.id)

            if not left_var is None and isinstance(left_var.type, Vector):
                if left_var.type != self.get_type(node.right):
                    self.report_error(node.lineno, "Can't insert incompatible type into Vector")

    def visit_Comparsion(self, node):
        self.visit(node.left)
        self.visit(node.right)

        if node.left.type == "Vector" or node.right.type == "Vector":
            self.report_error(node.lineno, "Can't compare Vectors")
        
        #TODO I have no concpet of checking this
        

    def visit_Transposition(self, node):
        self.visit(node.matrix)
        
        if node.matrix.type != "ID" and node.matrix.type != "VECTOR":
            self.report_error(node.lineno, "Can't transose element")
        
        if node.matrix.type == "ID":
            var = self.currentScope.get(node.matrix.id)

            if var and not isinstance(var.type, Vector):
                self.report_error(node.lineno, "Can't transpose elemtnet")

    
    def visit_Ref(self, node):
        self.visit(node.matrix_row)
        
        if self.currentScope.get(node.id) is None:
            self.report_error(node.lineno, "Can't reference to not exisiting array")
    
    def visit_UnaryMinus(self, node):
        self.visit(node.expression)

        if node.expression.type not in ['ID', 'INTTEGER', 'FLOAT']:
            self.report_error(node.lineno, "Unary minus with wrong expression")
        
        if node.expresion.type == 'ID':
            var = self.currentScope.get(node.expression.name)
            if var:
                if not isinstance(var.type, (Integer, Float)):
                    self.report_error(node.lineno, "Can't make unary minus for element")

    
    def visit_MartixInitalization(self, node):
        if node.expression.type != "INTEGER" and node.expression.type != "ID":
            self.report_error(node.lineno, "Matrix initialization only with integer")
        
        if node.expression.type == "ID":
            self.visit(node.expression)
            var = self.currentScope.get(node.expression.name)
            if var and not isinstance(var.type, Integer):
                self.report_error(node.lineno, "Matrix initialization only with integer")


    #TODO
    def visit_Vector(self, node):
        self.check_vector(node)

    def visit_IntNum(self, node):
        pass

    def visit_FloatNum(self, node):
        pass

    def visit_String(self, node):
        pass

    def visit_Variable(self, node):
        if self.currentScope.get(node.name) is None:
            self.report_error(node.lineno, "Unexisitnig variable")

    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        self.visit(node.left)     # type1 = node.left.accept(self) 
        self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op



        if not node.left.type == "ID" and not node.left.type == "REF" \
            and not node.right.type == "ID" and not node.right.type == "REF":

            left_type = self.get_type(node.left)
            right_type = self.get_type(node.right)

            if op in [".+", ".-", ".*", "./"]:
                if not isinstance(left_type, Vector) and not isinstance(right_type, Vector):
                    self.report_error(node.lineno, "Element wise operations only on vectors")
            
            if op in ["+", "-", "*", "/"]:
                pass

