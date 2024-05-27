class Tokenizer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def next(self):
        if(self.position >= len(self.tokens)):
            return None
        self.position += 1
        return self.current()

    def expect_next(self, expected_token):
        token = self.next()
        if token != expected_token:
            raise Exception(f"Expected token {expected_token} but got {token}")
        return token
    
    def expect_current(self, expected_token):
        token = self.current()
        if token != expected_token:
            raise Exception(f"Expected token {expected_token} but got {token}")
        return token
    
    def peek(self):
        return self.tokens[self.position + 1] if self.position + 1 < len(self.tokens) else None

class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer


    def parse_program(self):
        '''
        Program -> statements_block
        '''
        print("Program")
        self.parse_statements_block()

    def parse_statements_block(self):
        '''
        statements_block -> statements statements_block | ε
        '''
        print("|    statements_block")
        self.parse_statements()

    def parse_statements(self):
        '''
        statements -> declare_statement | set_statement | expression | if_statement | while_statement | function | read_statement | write_statement
        '''
        current_token = self.tokenizer.current()
        if current_token == None:
            print("End of program")
            return

        # Check for declaration statement (type followed by identifier)
        if current_token in {'int', 'float', 'double', 'bool', 'string', 'char'}:
            print("|    |    statements")
            self.parse_declare_statement()
        elif current_token == 'set':
            print("|    |    statements")
            self.parse_set_statement()
        elif current_token == 'if':
            print("|    |    statements")
            self.parse_if_statement()
        
            
            
        self.tokenizer.next()
        self.parse_statements()


    def parse_declare_statement(self):
        '''
        declare_statement -> type id
        '''
        print("|    |    |    declare_statement")
        type_token = self.tokenizer.current()
        id_token = self.tokenizer.next()
        print("|    |    |    |    Type:",type_token)
        print("|    |    |    |    id:",id_token)

    def parse_set_statement(self):
        print("|    |    |    set_statement")
        id_token = self.tokenizer.next()
        print("|    |    |    |    id:",id_token)
        self.tokenizer.expect_next('=')
        print("|    |    |    |    equal:",'=')
        expr = self.parse_expression()

    def parse_if_statement(self):
        print("|    |    |    if_statement")
        self.tokenizer.expect_current('if')
        self.parse_condition()

        self.tokenizer.expect_next('then')
        print ("|    |    |    then:",'then')
        self.tokenizer.next()
        self.parse_statements()

        self.tokenizer.expect_next('else')
        print ("|    |    |    else:",'else')
        self.parse_statements()

        self.tokenizer.expect_next('endif')
        print ("|    |    |    endif:",'endif')

    def parse_while_statement(self):
        print("TODO")

    def parse_function(self):
        self.tokenizer.expect('function')
        function_name = self.tokenizer.next()
        self.tokenizer.expect('(')
        param = self.tokenizer.next()
        self.tokenizer.expect(')')
        do_block = self.parse_statements_block()
        self.tokenizer.expect('endfunction')
        return {'type': 'function', 'name': function_name, 'parameter': param, 'body': do_block}

    def parse_read_statement(self):
        print("TODO")

    def parse_write_statement(self):
        print("TODO")

    def parse_expression(self):
        term1 = self.tokenizer.next()
        op = self.tokenizer.peek()
        if op in {'+', '-', '*', '/'}:
            self.tokenizer.next()
            term2 = self.tokenizer.next()
            print("|    |    |    |    Expression:",term1,op,term2)
        else:
            print("|    |    |    |    Expression:",term1)

    def parse_condition(self):
        print("|    |    |    |    condition")
        self.parse_expression()
        operator = self.tokenizer.next()
        if operator in {'<', '<=', '>', '>=', '==', '!='}:
            print("|    |    |    |    operator:",operator)
            self.parse_expression()
        else:
            raise Exception(f"Unexpected relational operator {operator}")


