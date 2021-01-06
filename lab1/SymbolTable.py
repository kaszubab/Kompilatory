class Symbol(object):
    def __init__(self, name, type=None):
        self.name = name
        self.type = type


class BuiltinTypeSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    __repr__ = __str__


class VariableSymbol(Symbol):
    def __init__(self, name, type):
        super().__init__(name, type)

    def __str__(self):
        return '<{name}:{type}>'.format(name=self.name, type=self.type)

    __repr__ = __str__



class MatrixSymbol(Symbol):
    def __init__(self, name, type, cols):
        super().__init__(name, type)
        self.cols = cols


    def __str__(self):
        return self.name + " " + self.type

    __repr__ = __str__


class SymbolTable(object):

    def __init__(self, parent, scope_name, scope_level): # parent scope and symbol table name
        self.parent = parent
        self.scope_name = scope_name
        self.scope_level = scope_level

        self._symbols = dict()

        self._init_buildins()

    def _init_buildins(self):
        self.put(BuiltinTypeSymbol("INTEGER"))
        self.put(BuiltinTypeSymbol("FLOAT"))
        self.put(BuiltinTypeSymbol("STRING"))
        

    

    def put(self, symbol): # put variable symbol or fundef under <name> entry
        self._symbols[symbol.name] = symbol
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        symbol = self._symbols.get(name)

        if symbol is not None:
            return symbol
        
        if self.parent is not None:
            return self.parent.get(name)
        
        return None

    def getParentScope(self):
        return self.parent
    #

    def check_if_in_loop(self):
        if self.scope_name in ['for', 'while']:
            return True
        elif self.parent is not None:
            self.parent.check_if_in_loop()
        else:
            False
