import re


class TokenLexeme:
    """
    Token Lexeme DataType for TokenLexemeList
    """
    def __init__(self, token, lexeme):
        self.token = token
        self.lexeme = lexeme

    def __str__(self):
        return f"Token: {self.token}, Lexeme: {self.lexeme}"

class Compiler:
    """
    Main Compiler Logic
    """
    def __init__(self) -> None:
        self.FilePath = ''
        self.LexemeList = []
        self.TokenLexemeList = []
        self.SymbolTable = {}
        # Lexeme left side and token right side
        self.TokenLexemeGrammer = {"LEXEME": "TOKEN",
                                   "INT": "int", 
                                   "FLOAT": "float",
                                   "DOUBLE": "double",
                                   "BOOL": "bool",
                                   "STRING": "string",
                                   "SET": "set",
                                   "CHAR": "char",
                                   "SET": "set",
                                   "IF": "if",
                                   "THEN": "then",
                                   "ELSE": "else",
                                   "FOR": "for",
                                   "WHILE": "while",
                                   "DO": "do",
                                   "ENDWHILE": "endwhile",
                                   "UNTIL": "until",
                                   "ENDUNTIL": "enduntil",
                                   "CALL": "call",
                                   "FUNCTION": "function",
                                   "ENDFUNCTION": "endfunction",
                                   "WRITE": "write",
                                   "READ": "read",
                                   "+": "+",
                                   "-": "-",
                                   "*": "*",
                                   "/": "/",
                                   "=": "=",
                                   ">": ">",
                                   "<": "<",
                                   "==": "==",
                                   "<=": "<=",
                                   ">=": ">=",
                                   "!=": "!=",
                                   "(": "(",
                                   ")": ")",   
                                   "ENDIF": "endif",
                                   }

    
    def ReadFile(self, filePath):
        """
        - Read source code file
        - Update FilePath
        - Update LexemeList
        """
        # Update File Path
        self.FilePath = filePath
        # Open file and update LexemeList with each space separated word in the file
        with open(self.FilePath, 'r') as file:
            content = file.read()
            self.LexemeList = content.split()

    def Tokenizer(self, lexeme):
        """
        - Take lexeme as input string and return detected token
        """
        if lexeme in self.TokenLexemeGrammer:
            # First: check if it is a reserved word in grammar
            token = self.TokenLexemeGrammer[lexeme]
        elif re.match(r'[A-Za-z]+', lexeme):
            # Second: check if it is an identifier
            token = "id"
            self.AddSybmol(lexeme)
        elif re.match(r'[0-9]+', lexeme):
            # Third: check if it is a number
            token = "number"
        else:
            # Lastly: if it does not exist, return ERROR
            token = "ERROR"
        
        return token
    
    def AddSybmol(self, lexeme):
        """
        - Add symbol to symbol table
        """
        # Add to symbol table if lexeme(key) not added before
        if lexeme not in self.SymbolTable:
            # Add dataType as last token added in the TokenLexemeList
            self.SymbolTable[lexeme] = self.TokenLexemeList[-1].token

    def LexicalAnalysis(self):
        """
        - Lexical Analysis based on compiler TokenLexeme Grammer
        - Update TokenLexemeList with tokens and lexemes based on LexemeList
        - Update Symbol Table
        """
        for lexeme in self.LexemeList:

            # Analyze lexeme and return token
            token = self.Tokenizer(lexeme)

            # Add token and lexeme to the list
            self.TokenLexemeList.append(TokenLexeme(token, lexeme))

    def PrintResults(self):
        """
        - Print TokenLexemeList 
        - Print SymbolTable
        """

        # Print each token and lexeme
        print("----- Lexical Analysis -----")
        for pair in self.TokenLexemeList:
            print(f"Token: {pair.token}, Lexeme: {pair.lexeme}")

        # Print each symbol and corresponding dataType in symbolTable
        print("----- Symbol Table -----")
        for key, value in self.SymbolTable.items():
            print(f"Name: {key}, Type:{value}")
    
    def GetTokenList(self):
        """
        - Return TokenLexemeList
        """
        tokenList = []
        for pair in self.TokenLexemeList:
            tokenList.append(pair.token)
        return tokenList
