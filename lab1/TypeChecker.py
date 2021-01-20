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
        if not hasattr(node, "type") and node.name == "BINEXPR":
            if isinstance(self.get_type(node.left), String) or isinstance(self.get_type(node.left), String):
                if node.op != '+':
                    self.report_error(node.lineno, f"operator {node.op} illegal for type String")
                    return None
                elif not (isinstance(self.get_type(node.left), String) and isinstance(self.get_type(node.left), String)):
                    self.report_error(node.lineno, f"String addition is posssible only between two String values")
                    return None
            if isinstance(self.get_type(node.left), Matrix) or isinstance(self.get_type(node.left), Matrix):
                return Matrix()
            if isinstance(self.get_type(node.left), Float) or isinstance(self.get_type(node.right), Float):
                return Float()
            if isinstance(self.get_type(node.left), String) or isinstance(self.get_type(node.right), String):
                return String()
            return Integer()
        # else:
        #     print(node.type)
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
        elif node.type == "MATRIX":
            return Matrix()
        elif node.type == "ID":
            # print(node.name)
            self.visit(node)
            return self.currentScope.get(node.name).type
        elif node.type == "REF":
            ref_target = self.currentScope.get(node.id)
            if isinstance(ref_target.type, Matrix):
                return Matrix()
            return Vector(Integer())
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
            # print(elem)
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

        if(node.else_block):
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
        begin = self.get_type(node.begin)
        end = self.get_type(node.end)

        if not isinstance(begin, Integer):
            self.report_error(node.lineno, "Range must begin with integer")

        if not isinstance(end, Integer):
            self.report_error(node.lineno, "Range must end with integer")

        self.visit(node.begin)
        self.visit(node.end)


    def visit_Assigment(self, node):
        self.visit(node.right)

        if node.left.type == "ID":
            # print(self.get_type(node.right))
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
        
        left = self.get_type(node.left)
        right = self.get_type(node.right)

        if (isinstance(left, String) and not isinstance(right, String)) or (isinstance(right, String) and not isinstance(left, String)):
            self.report_error(node.lineno, f"Can't compare {left.__str__()} and  {right.__str__()}")

        

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

        ref_target = self.currentScope.get(node.id)
        if isinstance(ref_target.type, Matrix):
            if len(node.matrix_row.elements) > 2:
                self.report_error(node.lineno, "Too large number of dimensions for Matrix")

    def visit_UnaryMinus(self, node):
        self.visit(node.expression)

        if node.expression.type not in ['ID', 'INTTEGER', 'FLOAT']:
            self.report_error(node.lineno, "Unary minus with wrong expression")
        
        if node.expresion.type == 'ID':
            var = self.currentScope.get(node.expression.name)
            if var:
                if not isinstance(var.type, (Integer, Float)):
                    self.report_error(node.lineno, "Can't make unary minus for element")

    
    def visit_MatrixInitialization(self, node):
        if node.expression.type == "ROW":
            self.visit(node.expression)
            for elem in node.expression.elements:
                if not isinstance(self.get_type(elem), Integer):
                    self.report_error(node.lineno, "Matrix initialization only with integer")

        elif node.expression.type != "INTEGER" and node.expression.type != "ID":
            self.report_error(node.lineno, "Matrix initialization only with integer")
        
        elif node.expression.type == "ID":
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
        self.visit(node.left)     # type1 = node.left.accept(self) 
        self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op

        # print("From Bin expr", node.left, node.right)
        left = self.get_type(node.left)
        right = self.get_type(node.right)
        # print("From Bin expr", left, right)


        if not left == "ID" and not right == "REF" and not left == "ID" and not right == "REF":

            is_matrix_like = lambda arg: isinstance(arg, Vector) or isinstance(arg, Matrix)

            if op in [".+", ".-", ".*", "./"]:
                if not (is_matrix_like(left) and is_matrix_like(right)):
                    self.report_error(node.lineno, "Element wise operations only on vectors")
            
            if op in ["+", "-", "*", "/"]:
                pass