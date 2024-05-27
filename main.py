from mycompiler import * 
from myparser import *

# Main Code
def main():
    compiler = Compiler()
    compiler.ReadFile("source_code.txt")
    compiler.LexicalAnalysis()
    # compiler.PrintResults()

    print(compiler.GetTokenList())

    tokenizer = Tokenizer(compiler.GetTokenList())
    parser = Parser(tokenizer)
    parser.parse_program()

main()
    

