import antlr3
from ryterLexer import ryterLexer
from ryterParser import ryterParser

input = """scriptio conjuro ;
   	anima 
    	harry , virga : integer;
   	initium	
   		Aguamenti(harry,virga) 
	finis."""

char_stream = antlr3.ANTLRStringStream(input)
# or to parse a file:
# char_stream = antlr3.ANTLRFileStream(path_to_input)
# or to parse an opened file or any other file-like object:
# char_stream = antlr3.ANTLRInputStream(file)
 
lexer = ryterLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = ryterParser(tokens)
print parser.program()

