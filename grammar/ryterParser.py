# $ANTLR 3.5.2 ryter.g 2015-01-22 20:29:24

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
AND=4
ARGDECL=5
ARGDECLS=6
ARGLIST=7
ARRAY=8
ASSIGN=9
AT=10
BEGIN=11
BLOCK=12
BOOLEAN=13
CASE=14
CHAR=15
CHR=16
COLON=17
COMMA=18
COMMENT_1=19
COMMENT_2=20
CONST=21
CONSTLIST=22
DIV=23
DO=24
DOT=25
DOTDOT=26
DOWNTO=27
ELIST=28
ELSE=29
END=30
EQUAL=31
EXIT=32
EXPONENT=33
FIELD=34
FIELDLIST=35
FILE=36
FOR=37
FORWARD=38
FUNCTION=39
FUNC_CALL=40
GE=41
GOTO=42
GT=43
IDENT=44
IDLIST=45
IF=46
IMPLEMENTATION=47
IN=48
INTEGER=49
INTERFACE=50
LABEL=51
LBRACK=52
LBRACK2=53
LCURLY=54
LE=55
LPAREN=56
LT=57
MINUS=58
MOD=59
NIL=60
NOT=61
NOT_EQUAL=62
NUM_INT=63
NUM_REAL=64
OF=65
OR=66
PACKED=67
PLUS=68
POINTER=69
PROCEDURE=70
PROC_CALL=71
PROGRAM=72
RBRACK=73
RBRACK2=74
RCURLY=75
REAL=76
RECORD=77
REPEAT=78
RPAREN=79
SCALARTYPE=80
SEMI=81
SET=82
SLASH=83
STAR=84
STRING=85
STRING_LITERAL=86
SUBRANGE=87
THEN=88
TO=89
TYPE=90
TYPEDECL=91
TYPELIST=92
UNIT=93
UNTIL=94
USES=95
VAR=96
VARDECL=97
VARIANT_CASE=98
VARIANT_TAG=99
VARIANT_TAG_NO_ID=100
WHILE=101
WITH=102
WS=103

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AND", "ARGDECL", "ARGDECLS", "ARGLIST", "ARRAY", "ASSIGN", "AT", "BEGIN", 
    "BLOCK", "BOOLEAN", "CASE", "CHAR", "CHR", "COLON", "COMMA", "COMMENT_1", 
    "COMMENT_2", "CONST", "CONSTLIST", "DIV", "DO", "DOT", "DOTDOT", "DOWNTO", 
    "ELIST", "ELSE", "END", "EQUAL", "EXIT", "EXPONENT", "FIELD", "FIELDLIST", 
    "FILE", "FOR", "FORWARD", "FUNCTION", "FUNC_CALL", "GE", "GOTO", "GT", 
    "IDENT", "IDLIST", "IF", "IMPLEMENTATION", "IN", "INTEGER", "INTERFACE", 
    "LABEL", "LBRACK", "LBRACK2", "LCURLY", "LE", "LPAREN", "LT", "MINUS", 
    "MOD", "NIL", "NOT", "NOT_EQUAL", "NUM_INT", "NUM_REAL", "OF", "OR", 
    "PACKED", "PLUS", "POINTER", "PROCEDURE", "PROC_CALL", "PROGRAM", "RBRACK", 
    "RBRACK2", "RCURLY", "REAL", "RECORD", "REPEAT", "RPAREN", "SCALARTYPE", 
    "SEMI", "SET", "SLASH", "STAR", "STRING", "STRING_LITERAL", "SUBRANGE", 
    "THEN", "TO", "TYPE", "TYPEDECL", "TYPELIST", "UNIT", "UNTIL", "USES", 
    "VAR", "VARDECL", "VARIANT_CASE", "VARIANT_TAG", "VARIANT_TAG_NO_ID", 
    "WHILE", "WITH", "WS"
]




class ryterParser(Parser):
    grammarFileName = "ryter.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ryterParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.program_return, self).__init__()

            self.tree = None





    # $ANTLR start "program"
    # ryter.g:219:1: program : programHeading ( INTERFACE )? block DOT -> ^( PROGRAM programHeading block ) ;
    def program(self, ):
        retval = self.program_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INTERFACE2 = None
        DOT4 = None
        programHeading1 = None
        block3 = None

        INTERFACE2_tree = None
        DOT4_tree = None
        stream_INTERFACE = RewriteRuleTokenStream(self._adaptor, "token INTERFACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_programHeading = RewriteRuleSubtreeStream(self._adaptor, "rule programHeading")
        try:
            try:
                # ryter.g:220:5: ( programHeading ( INTERFACE )? block DOT -> ^( PROGRAM programHeading block ) )
                # ryter.g:220:7: programHeading ( INTERFACE )? block DOT
                pass 
                self._state.following.append(self.FOLLOW_programHeading_in_program2242)
                programHeading1 = self.programHeading()

                self._state.following.pop()
                stream_programHeading.add(programHeading1.tree)


                # ryter.g:220:22: ( INTERFACE )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == INTERFACE) :
                    alt1 = 1
                if alt1 == 1:
                    # ryter.g:220:23: INTERFACE
                    pass 
                    INTERFACE2 = self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_program2245) 
                    stream_INTERFACE.add(INTERFACE2)





                self._state.following.append(self.FOLLOW_block_in_program2255)
                block3 = self.block()

                self._state.following.pop()
                stream_block.add(block3.tree)


                DOT4 = self.match(self.input, DOT, self.FOLLOW_DOT_in_program2263) 
                stream_DOT.add(DOT4)


                # AST Rewrite
                # elements: block, programHeading
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 223:7: -> ^( PROGRAM programHeading block )
                # ryter.g:223:10: ^( PROGRAM programHeading block )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROGRAM, "PROGRAM")
                , root_1)

                self._adaptor.addChild(root_1, stream_programHeading.nextTree())

                self._adaptor.addChild(root_1, stream_block.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "program"


    class programHeading_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.programHeading_return, self).__init__()

            self.tree = None





    # $ANTLR start "programHeading"
    # ryter.g:226:1: programHeading : ( PROGRAM ! identifier ( LPAREN ! identifierList RPAREN !)? SEMI !| UNIT identifier SEMI !);
    def programHeading(self, ):
        retval = self.programHeading_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROGRAM5 = None
        LPAREN7 = None
        RPAREN9 = None
        SEMI10 = None
        UNIT11 = None
        SEMI13 = None
        identifier6 = None
        identifierList8 = None
        identifier12 = None

        PROGRAM5_tree = None
        LPAREN7_tree = None
        RPAREN9_tree = None
        SEMI10_tree = None
        UNIT11_tree = None
        SEMI13_tree = None

        try:
            try:
                # ryter.g:227:5: ( PROGRAM ! identifier ( LPAREN ! identifierList RPAREN !)? SEMI !| UNIT identifier SEMI !)
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == PROGRAM) :
                    alt3 = 1
                elif (LA3_0 == UNIT) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # ryter.g:227:7: PROGRAM ! identifier ( LPAREN ! identifierList RPAREN !)? SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    PROGRAM5 = self.match(self.input, PROGRAM, self.FOLLOW_PROGRAM_in_programHeading2296)

                    self._state.following.append(self.FOLLOW_identifier_in_programHeading2299)
                    identifier6 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier6.tree)


                    # ryter.g:227:27: ( LPAREN ! identifierList RPAREN !)?
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LPAREN) :
                        alt2 = 1
                    if alt2 == 1:
                        # ryter.g:227:28: LPAREN ! identifierList RPAREN !
                        pass 
                        LPAREN7 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_programHeading2302)

                        self._state.following.append(self.FOLLOW_identifierList_in_programHeading2305)
                        identifierList8 = self.identifierList()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, identifierList8.tree)


                        RPAREN9 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_programHeading2307)




                    SEMI10 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_programHeading2312)


                elif alt3 == 2:
                    # ryter.g:228:7: UNIT identifier SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    UNIT11 = self.match(self.input, UNIT, self.FOLLOW_UNIT_in_programHeading2321)
                    UNIT11_tree = self._adaptor.createWithPayload(UNIT11)
                    self._adaptor.addChild(root_0, UNIT11_tree)



                    self._state.following.append(self.FOLLOW_identifier_in_programHeading2323)
                    identifier12 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier12.tree)


                    SEMI13 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_programHeading2325)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "programHeading"


    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.identifier_return, self).__init__()

            self.tree = None





    # $ANTLR start "identifier"
    # ryter.g:231:1: identifier : IDENT ;
    def identifier(self, ):
        retval = self.identifier_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENT14 = None

        IDENT14_tree = None

        try:
            try:
                # ryter.g:232:5: ( IDENT )
                # ryter.g:232:7: IDENT
                pass 
                root_0 = self._adaptor.nil()


                IDENT14 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_identifier2341)
                IDENT14_tree = self._adaptor.createWithPayload(IDENT14)
                self._adaptor.addChild(root_0, IDENT14_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "identifier"


    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.block_return, self).__init__()

            self.tree = None





    # $ANTLR start "block"
    # ryter.g:235:1: block : ( labelDeclarationPart | constantDefinitionPart | typeDefinitionPart | variableDeclarationPart | procedureAndFunctionDeclarationPart | usesUnitsPart | IMPLEMENTATION )* compoundStatement ;
    def block(self, ):
        retval = self.block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IMPLEMENTATION21 = None
        labelDeclarationPart15 = None
        constantDefinitionPart16 = None
        typeDefinitionPart17 = None
        variableDeclarationPart18 = None
        procedureAndFunctionDeclarationPart19 = None
        usesUnitsPart20 = None
        compoundStatement22 = None

        IMPLEMENTATION21_tree = None

        try:
            try:
                # ryter.g:236:5: ( ( labelDeclarationPart | constantDefinitionPart | typeDefinitionPart | variableDeclarationPart | procedureAndFunctionDeclarationPart | usesUnitsPart | IMPLEMENTATION )* compoundStatement )
                # ryter.g:236:7: ( labelDeclarationPart | constantDefinitionPart | typeDefinitionPart | variableDeclarationPart | procedureAndFunctionDeclarationPart | usesUnitsPart | IMPLEMENTATION )* compoundStatement
                pass 
                root_0 = self._adaptor.nil()


                # ryter.g:236:7: ( labelDeclarationPart | constantDefinitionPart | typeDefinitionPart | variableDeclarationPart | procedureAndFunctionDeclarationPart | usesUnitsPart | IMPLEMENTATION )*
                while True: #loop4
                    alt4 = 8
                    LA4 = self.input.LA(1)
                    if LA4 == LABEL:
                        alt4 = 1
                    elif LA4 == CONST:
                        alt4 = 2
                    elif LA4 == TYPE:
                        alt4 = 3
                    elif LA4 == VAR:
                        alt4 = 4
                    elif LA4 == FUNCTION or LA4 == PROCEDURE:
                        alt4 = 5
                    elif LA4 == USES:
                        alt4 = 6
                    elif LA4 == IMPLEMENTATION:
                        alt4 = 7

                    if alt4 == 1:
                        # ryter.g:236:9: labelDeclarationPart
                        pass 
                        self._state.following.append(self.FOLLOW_labelDeclarationPart_in_block2360)
                        labelDeclarationPart15 = self.labelDeclarationPart()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, labelDeclarationPart15.tree)



                    elif alt4 == 2:
                        # ryter.g:237:9: constantDefinitionPart
                        pass 
                        self._state.following.append(self.FOLLOW_constantDefinitionPart_in_block2370)
                        constantDefinitionPart16 = self.constantDefinitionPart()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, constantDefinitionPart16.tree)



                    elif alt4 == 3:
                        # ryter.g:238:9: typeDefinitionPart
                        pass 
                        self._state.following.append(self.FOLLOW_typeDefinitionPart_in_block2380)
                        typeDefinitionPart17 = self.typeDefinitionPart()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, typeDefinitionPart17.tree)



                    elif alt4 == 4:
                        # ryter.g:239:9: variableDeclarationPart
                        pass 
                        self._state.following.append(self.FOLLOW_variableDeclarationPart_in_block2390)
                        variableDeclarationPart18 = self.variableDeclarationPart()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, variableDeclarationPart18.tree)



                    elif alt4 == 5:
                        # ryter.g:240:9: procedureAndFunctionDeclarationPart
                        pass 
                        self._state.following.append(self.FOLLOW_procedureAndFunctionDeclarationPart_in_block2400)
                        procedureAndFunctionDeclarationPart19 = self.procedureAndFunctionDeclarationPart()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, procedureAndFunctionDeclarationPart19.tree)



                    elif alt4 == 6:
                        # ryter.g:241:9: usesUnitsPart
                        pass 
                        self._state.following.append(self.FOLLOW_usesUnitsPart_in_block2410)
                        usesUnitsPart20 = self.usesUnitsPart()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, usesUnitsPart20.tree)



                    elif alt4 == 7:
                        # ryter.g:242:9: IMPLEMENTATION
                        pass 
                        IMPLEMENTATION21 = self.match(self.input, IMPLEMENTATION, self.FOLLOW_IMPLEMENTATION_in_block2420)
                        IMPLEMENTATION21_tree = self._adaptor.createWithPayload(IMPLEMENTATION21)
                        self._adaptor.addChild(root_0, IMPLEMENTATION21_tree)




                    else:
                        break #loop4


                self._state.following.append(self.FOLLOW_compoundStatement_in_block2437)
                compoundStatement22 = self.compoundStatement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, compoundStatement22.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "block"


    class usesUnitsPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.usesUnitsPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "usesUnitsPart"
    # ryter.g:247:1: usesUnitsPart : USES ^ identifierList SEMI !;
    def usesUnitsPart(self, ):
        retval = self.usesUnitsPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        USES23 = None
        SEMI25 = None
        identifierList24 = None

        USES23_tree = None
        SEMI25_tree = None

        try:
            try:
                # ryter.g:248:5: ( USES ^ identifierList SEMI !)
                # ryter.g:248:7: USES ^ identifierList SEMI !
                pass 
                root_0 = self._adaptor.nil()


                USES23 = self.match(self.input, USES, self.FOLLOW_USES_in_usesUnitsPart2454)
                USES23_tree = self._adaptor.createWithPayload(USES23)
                root_0 = self._adaptor.becomeRoot(USES23_tree, root_0)



                self._state.following.append(self.FOLLOW_identifierList_in_usesUnitsPart2457)
                identifierList24 = self.identifierList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifierList24.tree)


                SEMI25 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_usesUnitsPart2459)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "usesUnitsPart"


    class labelDeclarationPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.labelDeclarationPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "labelDeclarationPart"
    # ryter.g:251:1: labelDeclarationPart : LABEL ^ label ( COMMA ! label )* SEMI !;
    def labelDeclarationPart(self, ):
        retval = self.labelDeclarationPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LABEL26 = None
        COMMA28 = None
        SEMI30 = None
        label27 = None
        label29 = None

        LABEL26_tree = None
        COMMA28_tree = None
        SEMI30_tree = None

        try:
            try:
                # ryter.g:252:5: ( LABEL ^ label ( COMMA ! label )* SEMI !)
                # ryter.g:252:7: LABEL ^ label ( COMMA ! label )* SEMI !
                pass 
                root_0 = self._adaptor.nil()


                LABEL26 = self.match(self.input, LABEL, self.FOLLOW_LABEL_in_labelDeclarationPart2477)
                LABEL26_tree = self._adaptor.createWithPayload(LABEL26)
                root_0 = self._adaptor.becomeRoot(LABEL26_tree, root_0)



                self._state.following.append(self.FOLLOW_label_in_labelDeclarationPart2480)
                label27 = self.label()

                self._state.following.pop()
                self._adaptor.addChild(root_0, label27.tree)


                # ryter.g:252:20: ( COMMA ! label )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # ryter.g:252:22: COMMA ! label
                        pass 
                        COMMA28 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_labelDeclarationPart2484)

                        self._state.following.append(self.FOLLOW_label_in_labelDeclarationPart2487)
                        label29 = self.label()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, label29.tree)



                    else:
                        break #loop5


                SEMI30 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_labelDeclarationPart2492)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "labelDeclarationPart"


    class label_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.label_return, self).__init__()

            self.tree = None





    # $ANTLR start "label"
    # ryter.g:255:1: label : unsignedInteger ;
    def label(self, ):
        retval = self.label_return()
        retval.start = self.input.LT(1)


        root_0 = None

        unsignedInteger31 = None


        try:
            try:
                # ryter.g:256:5: ( unsignedInteger )
                # ryter.g:256:7: unsignedInteger
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_unsignedInteger_in_label2510)
                unsignedInteger31 = self.unsignedInteger()

                self._state.following.pop()
                self._adaptor.addChild(root_0, unsignedInteger31.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "label"


    class constantDefinitionPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.constantDefinitionPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "constantDefinitionPart"
    # ryter.g:259:1: constantDefinitionPart : CONST ^ constantDefinition ( SEMI ! constantDefinition )* SEMI !;
    def constantDefinitionPart(self, ):
        retval = self.constantDefinitionPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONST32 = None
        SEMI34 = None
        SEMI36 = None
        constantDefinition33 = None
        constantDefinition35 = None

        CONST32_tree = None
        SEMI34_tree = None
        SEMI36_tree = None

        try:
            try:
                # ryter.g:260:5: ( CONST ^ constantDefinition ( SEMI ! constantDefinition )* SEMI !)
                # ryter.g:260:7: CONST ^ constantDefinition ( SEMI ! constantDefinition )* SEMI !
                pass 
                root_0 = self._adaptor.nil()


                CONST32 = self.match(self.input, CONST, self.FOLLOW_CONST_in_constantDefinitionPart2527)
                CONST32_tree = self._adaptor.createWithPayload(CONST32)
                root_0 = self._adaptor.becomeRoot(CONST32_tree, root_0)



                self._state.following.append(self.FOLLOW_constantDefinition_in_constantDefinitionPart2530)
                constantDefinition33 = self.constantDefinition()

                self._state.following.pop()
                self._adaptor.addChild(root_0, constantDefinition33.tree)


                # ryter.g:260:33: ( SEMI ! constantDefinition )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == SEMI) :
                        LA6_1 = self.input.LA(2)

                        if (LA6_1 == IDENT) :
                            alt6 = 1




                    if alt6 == 1:
                        # ryter.g:260:35: SEMI ! constantDefinition
                        pass 
                        SEMI34 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_constantDefinitionPart2534)

                        self._state.following.append(self.FOLLOW_constantDefinition_in_constantDefinitionPart2537)
                        constantDefinition35 = self.constantDefinition()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, constantDefinition35.tree)



                    else:
                        break #loop6


                SEMI36 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_constantDefinitionPart2542)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "constantDefinitionPart"


    class constantDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.constantDefinition_return, self).__init__()

            self.tree = None





    # $ANTLR start "constantDefinition"
    # ryter.g:263:1: constantDefinition : identifier EQUAL ^ constant ;
    def constantDefinition(self, ):
        retval = self.constantDefinition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUAL38 = None
        identifier37 = None
        constant39 = None

        EQUAL38_tree = None

        try:
            try:
                # ryter.g:264:5: ( identifier EQUAL ^ constant )
                # ryter.g:264:7: identifier EQUAL ^ constant
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_identifier_in_constantDefinition2560)
                identifier37 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier37.tree)


                EQUAL38 = self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_constantDefinition2562)
                EQUAL38_tree = self._adaptor.createWithPayload(EQUAL38)
                root_0 = self._adaptor.becomeRoot(EQUAL38_tree, root_0)



                self._state.following.append(self.FOLLOW_constant_in_constantDefinition2565)
                constant39 = self.constant()

                self._state.following.pop()
                self._adaptor.addChild(root_0, constant39.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "constantDefinition"


    class constantChr_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.constantChr_return, self).__init__()

            self.tree = None





    # $ANTLR start "constantChr"
    # ryter.g:267:1: constantChr : CHR ^ LPAREN ! ( unsignedInteger | identifier ) RPAREN !;
    def constantChr(self, ):
        retval = self.constantChr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CHR40 = None
        LPAREN41 = None
        RPAREN44 = None
        unsignedInteger42 = None
        identifier43 = None

        CHR40_tree = None
        LPAREN41_tree = None
        RPAREN44_tree = None

        try:
            try:
                # ryter.g:268:5: ( CHR ^ LPAREN ! ( unsignedInteger | identifier ) RPAREN !)
                # ryter.g:268:7: CHR ^ LPAREN ! ( unsignedInteger | identifier ) RPAREN !
                pass 
                root_0 = self._adaptor.nil()


                CHR40 = self.match(self.input, CHR, self.FOLLOW_CHR_in_constantChr2582)
                CHR40_tree = self._adaptor.createWithPayload(CHR40)
                root_0 = self._adaptor.becomeRoot(CHR40_tree, root_0)



                LPAREN41 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_constantChr2585)

                # ryter.g:268:20: ( unsignedInteger | identifier )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == NUM_INT) :
                    alt7 = 1
                elif (LA7_0 == IDENT) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # ryter.g:268:21: unsignedInteger
                    pass 
                    self._state.following.append(self.FOLLOW_unsignedInteger_in_constantChr2589)
                    unsignedInteger42 = self.unsignedInteger()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedInteger42.tree)



                elif alt7 == 2:
                    # ryter.g:268:37: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_constantChr2591)
                    identifier43 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier43.tree)





                RPAREN44 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_constantChr2594)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "constantChr"


    class constant_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.constant_return, self).__init__()

            self.tree = None





    # $ANTLR start "constant"
    # ryter.g:271:1: constant : ( unsignedNumber |s= sign n= unsignedNumber -> ^( $s $n) | identifier |s2= sign id= identifier -> ^( $s2 $id) | string | constantChr );
    def constant(self, ):
        retval = self.constant_return()
        retval.start = self.input.LT(1)


        root_0 = None

        s = None
        n = None
        s2 = None
        id = None
        unsignedNumber45 = None
        identifier46 = None
        string47 = None
        constantChr48 = None

        stream_sign = RewriteRuleSubtreeStream(self._adaptor, "rule sign")
        stream_unsignedNumber = RewriteRuleSubtreeStream(self._adaptor, "rule unsignedNumber")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # ryter.g:272:5: ( unsignedNumber |s= sign n= unsignedNumber -> ^( $s $n) | identifier |s2= sign id= identifier -> ^( $s2 $id) | string | constantChr )
                alt8 = 6
                LA8 = self.input.LA(1)
                if LA8 == NUM_INT or LA8 == NUM_REAL:
                    alt8 = 1
                elif LA8 == MINUS or LA8 == PLUS:
                    LA8_2 = self.input.LA(2)

                    if ((NUM_INT <= LA8_2 <= NUM_REAL)) :
                        alt8 = 2
                    elif (LA8_2 == IDENT) :
                        alt8 = 4
                    else:
                        nvae = NoViableAltException("", 8, 2, self.input)

                        raise nvae


                elif LA8 == IDENT:
                    alt8 = 3
                elif LA8 == STRING_LITERAL:
                    alt8 = 5
                elif LA8 == CHR:
                    alt8 = 6
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # ryter.g:272:7: unsignedNumber
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unsignedNumber_in_constant2612)
                    unsignedNumber45 = self.unsignedNumber()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedNumber45.tree)



                elif alt8 == 2:
                    # ryter.g:273:7: s= sign n= unsignedNumber
                    pass 
                    self._state.following.append(self.FOLLOW_sign_in_constant2622)
                    s = self.sign()

                    self._state.following.pop()
                    stream_sign.add(s.tree)


                    self._state.following.append(self.FOLLOW_unsignedNumber_in_constant2626)
                    n = self.unsignedNumber()

                    self._state.following.pop()
                    stream_unsignedNumber.add(n.tree)


                    # AST Rewrite
                    # elements: s, n
                    # token labels: 
                    # rule labels: retval, s, n
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    if s is not None:
                        stream_s = RewriteRuleSubtreeStream(self._adaptor, "rule s", s.tree)
                    else:
                        stream_s = RewriteRuleSubtreeStream(self._adaptor, "token s", None)

                    if n is not None:
                        stream_n = RewriteRuleSubtreeStream(self._adaptor, "rule n", n.tree)
                    else:
                        stream_n = RewriteRuleSubtreeStream(self._adaptor, "token n", None)


                    root_0 = self._adaptor.nil()
                    # 273:31: -> ^( $s $n)
                    # ryter.g:273:34: ^( $s $n)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_s.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_n.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt8 == 3:
                    # ryter.g:274:7: identifier
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_identifier_in_constant2645)
                    identifier46 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier46.tree)



                elif alt8 == 4:
                    # ryter.g:275:7: s2= sign id= identifier
                    pass 
                    self._state.following.append(self.FOLLOW_sign_in_constant2655)
                    s2 = self.sign()

                    self._state.following.pop()
                    stream_sign.add(s2.tree)


                    self._state.following.append(self.FOLLOW_identifier_in_constant2659)
                    id = self.identifier()

                    self._state.following.pop()
                    stream_identifier.add(id.tree)


                    # AST Rewrite
                    # elements: id, s2
                    # token labels: 
                    # rule labels: id, retval, s2
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if id is not None:
                        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id", id.tree)
                    else:
                        stream_id = RewriteRuleSubtreeStream(self._adaptor, "token id", None)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    if s2 is not None:
                        stream_s2 = RewriteRuleSubtreeStream(self._adaptor, "rule s2", s2.tree)
                    else:
                        stream_s2 = RewriteRuleSubtreeStream(self._adaptor, "token s2", None)


                    root_0 = self._adaptor.nil()
                    # 275:29: -> ^( $s2 $id)
                    # ryter.g:275:32: ^( $s2 $id)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_s2.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_id.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt8 == 5:
                    # ryter.g:276:7: string
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_string_in_constant2678)
                    string47 = self.string()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, string47.tree)



                elif alt8 == 6:
                    # ryter.g:277:7: constantChr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_constantChr_in_constant2686)
                    constantChr48 = self.constantChr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constantChr48.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "constant"


    class unsignedNumber_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.unsignedNumber_return, self).__init__()

            self.tree = None





    # $ANTLR start "unsignedNumber"
    # ryter.g:280:1: unsignedNumber : ( unsignedInteger | unsignedReal );
    def unsignedNumber(self, ):
        retval = self.unsignedNumber_return()
        retval.start = self.input.LT(1)


        root_0 = None

        unsignedInteger49 = None
        unsignedReal50 = None


        try:
            try:
                # ryter.g:281:5: ( unsignedInteger | unsignedReal )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == NUM_INT) :
                    alt9 = 1
                elif (LA9_0 == NUM_REAL) :
                    alt9 = 2
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # ryter.g:281:7: unsignedInteger
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unsignedInteger_in_unsignedNumber2703)
                    unsignedInteger49 = self.unsignedInteger()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedInteger49.tree)



                elif alt9 == 2:
                    # ryter.g:282:7: unsignedReal
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unsignedReal_in_unsignedNumber2711)
                    unsignedReal50 = self.unsignedReal()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedReal50.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unsignedNumber"


    class unsignedInteger_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.unsignedInteger_return, self).__init__()

            self.tree = None





    # $ANTLR start "unsignedInteger"
    # ryter.g:285:1: unsignedInteger : NUM_INT ;
    def unsignedInteger(self, ):
        retval = self.unsignedInteger_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NUM_INT51 = None

        NUM_INT51_tree = None

        try:
            try:
                # ryter.g:286:5: ( NUM_INT )
                # ryter.g:286:7: NUM_INT
                pass 
                root_0 = self._adaptor.nil()


                NUM_INT51 = self.match(self.input, NUM_INT, self.FOLLOW_NUM_INT_in_unsignedInteger2728)
                NUM_INT51_tree = self._adaptor.createWithPayload(NUM_INT51)
                self._adaptor.addChild(root_0, NUM_INT51_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unsignedInteger"


    class unsignedReal_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.unsignedReal_return, self).__init__()

            self.tree = None





    # $ANTLR start "unsignedReal"
    # ryter.g:289:1: unsignedReal : NUM_REAL ;
    def unsignedReal(self, ):
        retval = self.unsignedReal_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NUM_REAL52 = None

        NUM_REAL52_tree = None

        try:
            try:
                # ryter.g:290:5: ( NUM_REAL )
                # ryter.g:290:7: NUM_REAL
                pass 
                root_0 = self._adaptor.nil()


                NUM_REAL52 = self.match(self.input, NUM_REAL, self.FOLLOW_NUM_REAL_in_unsignedReal2745)
                NUM_REAL52_tree = self._adaptor.createWithPayload(NUM_REAL52)
                self._adaptor.addChild(root_0, NUM_REAL52_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unsignedReal"


    class sign_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.sign_return, self).__init__()

            self.tree = None





    # $ANTLR start "sign"
    # ryter.g:293:1: sign : ( PLUS | MINUS );
    def sign(self, ):
        retval = self.sign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set53 = None

        set53_tree = None

        try:
            try:
                # ryter.g:294:5: ( PLUS | MINUS )
                # ryter.g:
                pass 
                root_0 = self._adaptor.nil()


                set53 = self.input.LT(1)

                if self.input.LA(1) == MINUS or self.input.LA(1) == PLUS:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set53))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "sign"


    class string_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.string_return, self).__init__()

            self.tree = None





    # $ANTLR start "string"
    # ryter.g:297:1: string : STRING_LITERAL ;
    def string(self, ):
        retval = self.string_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STRING_LITERAL54 = None

        STRING_LITERAL54_tree = None

        try:
            try:
                # ryter.g:298:5: ( STRING_LITERAL )
                # ryter.g:298:7: STRING_LITERAL
                pass 
                root_0 = self._adaptor.nil()


                STRING_LITERAL54 = self.match(self.input, STRING_LITERAL, self.FOLLOW_STRING_LITERAL_in_string2783)
                STRING_LITERAL54_tree = self._adaptor.createWithPayload(STRING_LITERAL54)
                self._adaptor.addChild(root_0, STRING_LITERAL54_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "string"


    class typeDefinitionPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.typeDefinitionPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeDefinitionPart"
    # ryter.g:301:1: typeDefinitionPart : TYPE ^ typeDefinition ( SEMI ! typeDefinition )* SEMI !;
    def typeDefinitionPart(self, ):
        retval = self.typeDefinitionPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPE55 = None
        SEMI57 = None
        SEMI59 = None
        typeDefinition56 = None
        typeDefinition58 = None

        TYPE55_tree = None
        SEMI57_tree = None
        SEMI59_tree = None

        try:
            try:
                # ryter.g:302:5: ( TYPE ^ typeDefinition ( SEMI ! typeDefinition )* SEMI !)
                # ryter.g:302:7: TYPE ^ typeDefinition ( SEMI ! typeDefinition )* SEMI !
                pass 
                root_0 = self._adaptor.nil()


                TYPE55 = self.match(self.input, TYPE, self.FOLLOW_TYPE_in_typeDefinitionPart2800)
                TYPE55_tree = self._adaptor.createWithPayload(TYPE55)
                root_0 = self._adaptor.becomeRoot(TYPE55_tree, root_0)



                self._state.following.append(self.FOLLOW_typeDefinition_in_typeDefinitionPart2803)
                typeDefinition56 = self.typeDefinition()

                self._state.following.pop()
                self._adaptor.addChild(root_0, typeDefinition56.tree)


                # ryter.g:302:28: ( SEMI ! typeDefinition )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == SEMI) :
                        LA10_1 = self.input.LA(2)

                        if (LA10_1 == IDENT) :
                            alt10 = 1




                    if alt10 == 1:
                        # ryter.g:302:30: SEMI ! typeDefinition
                        pass 
                        SEMI57 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_typeDefinitionPart2807)

                        self._state.following.append(self.FOLLOW_typeDefinition_in_typeDefinitionPart2810)
                        typeDefinition58 = self.typeDefinition()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, typeDefinition58.tree)



                    else:
                        break #loop10


                SEMI59 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_typeDefinitionPart2815)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "typeDefinitionPart"


    class typeDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.typeDefinition_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeDefinition"
    # ryter.g:306:1: typeDefinition : identifier e= EQUAL ^ ( type | functionType | procedureType ) ;
    def typeDefinition(self, ):
        retval = self.typeDefinition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        e = None
        identifier60 = None
        type61 = None
        functionType62 = None
        procedureType63 = None

        e_tree = None

        try:
            try:
                # ryter.g:307:5: ( identifier e= EQUAL ^ ( type | functionType | procedureType ) )
                # ryter.g:307:7: identifier e= EQUAL ^ ( type | functionType | procedureType )
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_identifier_in_typeDefinition2834)
                identifier60 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier60.tree)


                e = self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_typeDefinition2838)
                e_tree = self._adaptor.createWithPayload(e)
                root_0 = self._adaptor.becomeRoot(e_tree, root_0)



                #action start
                e.setType(TYPEDECL);
                #action end


                # ryter.g:308:7: ( type | functionType | procedureType )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == ARRAY or LA11 == BOOLEAN or LA11 == CHAR or LA11 == CHR or LA11 == FILE or LA11 == IDENT or LA11 == INTEGER or LA11 == LPAREN or LA11 == MINUS or LA11 == NUM_INT or LA11 == NUM_REAL or LA11 == PACKED or LA11 == PLUS or LA11 == POINTER or LA11 == REAL or LA11 == RECORD or LA11 == SET or LA11 == STRING or LA11 == STRING_LITERAL:
                    alt11 = 1
                elif LA11 == FUNCTION:
                    alt11 = 2
                elif LA11 == PROCEDURE:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # ryter.g:308:9: type
                    pass 
                    self._state.following.append(self.FOLLOW_type_in_typeDefinition2851)
                    type61 = self.type()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, type61.tree)



                elif alt11 == 2:
                    # ryter.g:309:9: functionType
                    pass 
                    self._state.following.append(self.FOLLOW_functionType_in_typeDefinition2861)
                    functionType62 = self.functionType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, functionType62.tree)



                elif alt11 == 3:
                    # ryter.g:310:9: procedureType
                    pass 
                    self._state.following.append(self.FOLLOW_procedureType_in_typeDefinition2872)
                    procedureType63 = self.procedureType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, procedureType63.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "typeDefinition"


    class functionType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.functionType_return, self).__init__()

            self.tree = None





    # $ANTLR start "functionType"
    # ryter.g:314:1: functionType : FUNCTION ^ ( formalParameterList )? COLON ! resultType ;
    def functionType(self, ):
        retval = self.functionType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FUNCTION64 = None
        COLON66 = None
        formalParameterList65 = None
        resultType67 = None

        FUNCTION64_tree = None
        COLON66_tree = None

        try:
            try:
                # ryter.g:315:5: ( FUNCTION ^ ( formalParameterList )? COLON ! resultType )
                # ryter.g:315:7: FUNCTION ^ ( formalParameterList )? COLON ! resultType
                pass 
                root_0 = self._adaptor.nil()


                FUNCTION64 = self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_functionType2897)
                FUNCTION64_tree = self._adaptor.createWithPayload(FUNCTION64)
                root_0 = self._adaptor.becomeRoot(FUNCTION64_tree, root_0)



                # ryter.g:315:17: ( formalParameterList )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == LPAREN) :
                    alt12 = 1
                if alt12 == 1:
                    # ryter.g:315:18: formalParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterList_in_functionType2901)
                    formalParameterList65 = self.formalParameterList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, formalParameterList65.tree)





                COLON66 = self.match(self.input, COLON, self.FOLLOW_COLON_in_functionType2905)

                self._state.following.append(self.FOLLOW_resultType_in_functionType2908)
                resultType67 = self.resultType()

                self._state.following.pop()
                self._adaptor.addChild(root_0, resultType67.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "functionType"


    class procedureType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.procedureType_return, self).__init__()

            self.tree = None





    # $ANTLR start "procedureType"
    # ryter.g:318:1: procedureType : PROCEDURE ^ ( formalParameterList )? ;
    def procedureType(self, ):
        retval = self.procedureType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROCEDURE68 = None
        formalParameterList69 = None

        PROCEDURE68_tree = None

        try:
            try:
                # ryter.g:319:5: ( PROCEDURE ^ ( formalParameterList )? )
                # ryter.g:319:7: PROCEDURE ^ ( formalParameterList )?
                pass 
                root_0 = self._adaptor.nil()


                PROCEDURE68 = self.match(self.input, PROCEDURE, self.FOLLOW_PROCEDURE_in_procedureType2925)
                PROCEDURE68_tree = self._adaptor.createWithPayload(PROCEDURE68)
                root_0 = self._adaptor.becomeRoot(PROCEDURE68_tree, root_0)



                # ryter.g:319:18: ( formalParameterList )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == LPAREN) :
                    alt13 = 1
                if alt13 == 1:
                    # ryter.g:319:19: formalParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterList_in_procedureType2929)
                    formalParameterList69 = self.formalParameterList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, formalParameterList69.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "procedureType"


    class type_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.type_return, self).__init__()

            self.tree = None





    # $ANTLR start "type"
    # ryter.g:322:1: type : ( simpleType | structuredType | pointerType );
    def type(self, ):
        retval = self.type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        simpleType70 = None
        structuredType71 = None
        pointerType72 = None


        try:
            try:
                # ryter.g:323:5: ( simpleType | structuredType | pointerType )
                alt14 = 3
                LA14 = self.input.LA(1)
                if LA14 == BOOLEAN or LA14 == CHAR or LA14 == INTEGER or LA14 == LPAREN or LA14 == REAL or LA14 == STRING:
                    alt14 = 1
                elif LA14 == NUM_INT:
                    LA14_2 = self.input.LA(2)

                    if (LA14_2 == DOTDOT) :
                        LA14 = self.input.LA(3)
                        if LA14 == NUM_INT:
                            alt14 = 1
                        elif LA14 == NUM_REAL:
                            alt14 = 1
                        elif LA14 == MINUS or LA14 == PLUS:
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == IDENT:
                                alt14 = 1
                            else:
                                nvae = NoViableAltException("", 14, 17, self.input)

                                raise nvae


                        elif LA14 == IDENT:
                            alt14 = 1
                        elif LA14 == STRING_LITERAL:
                            alt14 = 1
                        elif LA14 == CHR:
                            LA14_20 = self.input.LA(4)

                            if (LA14_20 == LPAREN) :
                                LA14_26 = self.input.LA(5)

                                if (LA14_26 == NUM_INT) :
                                    LA14_28 = self.input.LA(6)

                                    if (LA14_28 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 28, self.input)

                                        raise nvae


                                elif (LA14_26 == IDENT) :
                                    LA14_29 = self.input.LA(6)

                                    if (LA14_29 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 29, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 26, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 20, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 10, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 2, self.input)

                        raise nvae


                elif LA14 == NUM_REAL:
                    LA14_3 = self.input.LA(2)

                    if (LA14_3 == DOTDOT) :
                        LA14 = self.input.LA(3)
                        if LA14 == NUM_INT:
                            alt14 = 1
                        elif LA14 == NUM_REAL:
                            alt14 = 1
                        elif LA14 == MINUS or LA14 == PLUS:
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == IDENT:
                                alt14 = 1
                            else:
                                nvae = NoViableAltException("", 14, 17, self.input)

                                raise nvae


                        elif LA14 == IDENT:
                            alt14 = 1
                        elif LA14 == STRING_LITERAL:
                            alt14 = 1
                        elif LA14 == CHR:
                            LA14_20 = self.input.LA(4)

                            if (LA14_20 == LPAREN) :
                                LA14_26 = self.input.LA(5)

                                if (LA14_26 == NUM_INT) :
                                    LA14_28 = self.input.LA(6)

                                    if (LA14_28 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 28, self.input)

                                        raise nvae


                                elif (LA14_26 == IDENT) :
                                    LA14_29 = self.input.LA(6)

                                    if (LA14_29 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 29, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 26, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 20, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 10, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 3, self.input)

                        raise nvae


                elif LA14 == MINUS or LA14 == PLUS:
                    LA14 = self.input.LA(2)
                    if LA14 == NUM_INT:
                        LA14_11 = self.input.LA(3)

                        if (LA14_11 == DOTDOT) :
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == MINUS or LA14 == PLUS:
                                LA14 = self.input.LA(5)
                                if LA14 == NUM_INT:
                                    alt14 = 1
                                elif LA14 == NUM_REAL:
                                    alt14 = 1
                                elif LA14 == IDENT:
                                    alt14 = 1
                                else:
                                    nvae = NoViableAltException("", 14, 17, self.input)

                                    raise nvae


                            elif LA14 == IDENT:
                                alt14 = 1
                            elif LA14 == STRING_LITERAL:
                                alt14 = 1
                            elif LA14 == CHR:
                                LA14_20 = self.input.LA(5)

                                if (LA14_20 == LPAREN) :
                                    LA14_26 = self.input.LA(6)

                                    if (LA14_26 == NUM_INT) :
                                        LA14_28 = self.input.LA(7)

                                        if (LA14_28 == RPAREN) :
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 28, self.input)

                                            raise nvae


                                    elif (LA14_26 == IDENT) :
                                        LA14_29 = self.input.LA(7)

                                        if (LA14_29 == RPAREN) :
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 29, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 14, 26, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 20, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 10, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 11, self.input)

                            raise nvae


                    elif LA14 == NUM_REAL:
                        LA14_12 = self.input.LA(3)

                        if (LA14_12 == DOTDOT) :
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == MINUS or LA14 == PLUS:
                                LA14 = self.input.LA(5)
                                if LA14 == NUM_INT:
                                    alt14 = 1
                                elif LA14 == NUM_REAL:
                                    alt14 = 1
                                elif LA14 == IDENT:
                                    alt14 = 1
                                else:
                                    nvae = NoViableAltException("", 14, 17, self.input)

                                    raise nvae


                            elif LA14 == IDENT:
                                alt14 = 1
                            elif LA14 == STRING_LITERAL:
                                alt14 = 1
                            elif LA14 == CHR:
                                LA14_20 = self.input.LA(5)

                                if (LA14_20 == LPAREN) :
                                    LA14_26 = self.input.LA(6)

                                    if (LA14_26 == NUM_INT) :
                                        LA14_28 = self.input.LA(7)

                                        if (LA14_28 == RPAREN) :
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 28, self.input)

                                            raise nvae


                                    elif (LA14_26 == IDENT) :
                                        LA14_29 = self.input.LA(7)

                                        if (LA14_29 == RPAREN) :
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 29, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 14, 26, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 20, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 10, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 12, self.input)

                            raise nvae


                    elif LA14 == IDENT:
                        LA14_13 = self.input.LA(3)

                        if (LA14_13 == DOTDOT) :
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == MINUS or LA14 == PLUS:
                                LA14 = self.input.LA(5)
                                if LA14 == NUM_INT:
                                    alt14 = 1
                                elif LA14 == NUM_REAL:
                                    alt14 = 1
                                elif LA14 == IDENT:
                                    alt14 = 1
                                else:
                                    nvae = NoViableAltException("", 14, 17, self.input)

                                    raise nvae


                            elif LA14 == IDENT:
                                alt14 = 1
                            elif LA14 == STRING_LITERAL:
                                alt14 = 1
                            elif LA14 == CHR:
                                LA14_20 = self.input.LA(5)

                                if (LA14_20 == LPAREN) :
                                    LA14_26 = self.input.LA(6)

                                    if (LA14_26 == NUM_INT) :
                                        LA14_28 = self.input.LA(7)

                                        if (LA14_28 == RPAREN) :
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 28, self.input)

                                            raise nvae


                                    elif (LA14_26 == IDENT) :
                                        LA14_29 = self.input.LA(7)

                                        if (LA14_29 == RPAREN) :
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 29, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 14, 26, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 20, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 10, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 13, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 4, self.input)

                        raise nvae


                elif LA14 == IDENT:
                    LA14_5 = self.input.LA(2)

                    if (LA14_5 == DOTDOT) :
                        LA14 = self.input.LA(3)
                        if LA14 == NUM_INT:
                            alt14 = 1
                        elif LA14 == NUM_REAL:
                            alt14 = 1
                        elif LA14 == MINUS or LA14 == PLUS:
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == IDENT:
                                alt14 = 1
                            else:
                                nvae = NoViableAltException("", 14, 17, self.input)

                                raise nvae


                        elif LA14 == IDENT:
                            alt14 = 1
                        elif LA14 == STRING_LITERAL:
                            alt14 = 1
                        elif LA14 == CHR:
                            LA14_20 = self.input.LA(4)

                            if (LA14_20 == LPAREN) :
                                LA14_26 = self.input.LA(5)

                                if (LA14_26 == NUM_INT) :
                                    LA14_28 = self.input.LA(6)

                                    if (LA14_28 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 28, self.input)

                                        raise nvae


                                elif (LA14_26 == IDENT) :
                                    LA14_29 = self.input.LA(6)

                                    if (LA14_29 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 29, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 26, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 20, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 10, self.input)

                            raise nvae


                    elif (LA14_5 == END or LA14_5 == RPAREN or LA14_5 == SEMI) :
                        alt14 = 1
                    else:
                        nvae = NoViableAltException("", 14, 5, self.input)

                        raise nvae


                elif LA14 == STRING_LITERAL:
                    LA14_6 = self.input.LA(2)

                    if (LA14_6 == DOTDOT) :
                        LA14 = self.input.LA(3)
                        if LA14 == NUM_INT:
                            alt14 = 1
                        elif LA14 == NUM_REAL:
                            alt14 = 1
                        elif LA14 == MINUS or LA14 == PLUS:
                            LA14 = self.input.LA(4)
                            if LA14 == NUM_INT:
                                alt14 = 1
                            elif LA14 == NUM_REAL:
                                alt14 = 1
                            elif LA14 == IDENT:
                                alt14 = 1
                            else:
                                nvae = NoViableAltException("", 14, 17, self.input)

                                raise nvae


                        elif LA14 == IDENT:
                            alt14 = 1
                        elif LA14 == STRING_LITERAL:
                            alt14 = 1
                        elif LA14 == CHR:
                            LA14_20 = self.input.LA(4)

                            if (LA14_20 == LPAREN) :
                                LA14_26 = self.input.LA(5)

                                if (LA14_26 == NUM_INT) :
                                    LA14_28 = self.input.LA(6)

                                    if (LA14_28 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 28, self.input)

                                        raise nvae


                                elif (LA14_26 == IDENT) :
                                    LA14_29 = self.input.LA(6)

                                    if (LA14_29 == RPAREN) :
                                        alt14 = 1
                                    else:
                                        nvae = NoViableAltException("", 14, 29, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 26, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 20, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 10, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 6, self.input)

                        raise nvae


                elif LA14 == CHR:
                    LA14_7 = self.input.LA(2)

                    if (LA14_7 == LPAREN) :
                        LA14_14 = self.input.LA(3)

                        if (LA14_14 == NUM_INT) :
                            LA14_21 = self.input.LA(4)

                            if (LA14_21 == RPAREN) :
                                LA14_27 = self.input.LA(5)

                                if (LA14_27 == DOTDOT) :
                                    LA14 = self.input.LA(6)
                                    if LA14 == NUM_INT:
                                        alt14 = 1
                                    elif LA14 == NUM_REAL:
                                        alt14 = 1
                                    elif LA14 == MINUS or LA14 == PLUS:
                                        LA14 = self.input.LA(7)
                                        if LA14 == NUM_INT:
                                            alt14 = 1
                                        elif LA14 == NUM_REAL:
                                            alt14 = 1
                                        elif LA14 == IDENT:
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 17, self.input)

                                            raise nvae


                                    elif LA14 == IDENT:
                                        alt14 = 1
                                    elif LA14 == STRING_LITERAL:
                                        alt14 = 1
                                    elif LA14 == CHR:
                                        LA14_20 = self.input.LA(7)

                                        if (LA14_20 == LPAREN) :
                                            LA14_26 = self.input.LA(8)

                                            if (LA14_26 == NUM_INT) :
                                                LA14_28 = self.input.LA(9)

                                                if (LA14_28 == RPAREN) :
                                                    alt14 = 1
                                                else:
                                                    nvae = NoViableAltException("", 14, 28, self.input)

                                                    raise nvae


                                            elif (LA14_26 == IDENT) :
                                                LA14_29 = self.input.LA(9)

                                                if (LA14_29 == RPAREN) :
                                                    alt14 = 1
                                                else:
                                                    nvae = NoViableAltException("", 14, 29, self.input)

                                                    raise nvae


                                            else:
                                                nvae = NoViableAltException("", 14, 26, self.input)

                                                raise nvae


                                        else:
                                            nvae = NoViableAltException("", 14, 20, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 14, 10, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 27, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 21, self.input)

                                raise nvae


                        elif (LA14_14 == IDENT) :
                            LA14_22 = self.input.LA(4)

                            if (LA14_22 == RPAREN) :
                                LA14_27 = self.input.LA(5)

                                if (LA14_27 == DOTDOT) :
                                    LA14 = self.input.LA(6)
                                    if LA14 == NUM_INT:
                                        alt14 = 1
                                    elif LA14 == NUM_REAL:
                                        alt14 = 1
                                    elif LA14 == MINUS or LA14 == PLUS:
                                        LA14 = self.input.LA(7)
                                        if LA14 == NUM_INT:
                                            alt14 = 1
                                        elif LA14 == NUM_REAL:
                                            alt14 = 1
                                        elif LA14 == IDENT:
                                            alt14 = 1
                                        else:
                                            nvae = NoViableAltException("", 14, 17, self.input)

                                            raise nvae


                                    elif LA14 == IDENT:
                                        alt14 = 1
                                    elif LA14 == STRING_LITERAL:
                                        alt14 = 1
                                    elif LA14 == CHR:
                                        LA14_20 = self.input.LA(7)

                                        if (LA14_20 == LPAREN) :
                                            LA14_26 = self.input.LA(8)

                                            if (LA14_26 == NUM_INT) :
                                                LA14_28 = self.input.LA(9)

                                                if (LA14_28 == RPAREN) :
                                                    alt14 = 1
                                                else:
                                                    nvae = NoViableAltException("", 14, 28, self.input)

                                                    raise nvae


                                            elif (LA14_26 == IDENT) :
                                                LA14_29 = self.input.LA(9)

                                                if (LA14_29 == RPAREN) :
                                                    alt14 = 1
                                                else:
                                                    nvae = NoViableAltException("", 14, 29, self.input)

                                                    raise nvae


                                            else:
                                                nvae = NoViableAltException("", 14, 26, self.input)

                                                raise nvae


                                        else:
                                            nvae = NoViableAltException("", 14, 20, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 14, 10, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 14, 27, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 14, 22, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 14, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 7, self.input)

                        raise nvae


                elif LA14 == ARRAY or LA14 == FILE or LA14 == PACKED or LA14 == RECORD or LA14 == SET:
                    alt14 = 2
                elif LA14 == POINTER:
                    alt14 = 3
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # ryter.g:323:7: simpleType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_simpleType_in_type2948)
                    simpleType70 = self.simpleType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, simpleType70.tree)



                elif alt14 == 2:
                    # ryter.g:324:7: structuredType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_structuredType_in_type2956)
                    structuredType71 = self.structuredType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, structuredType71.tree)



                elif alt14 == 3:
                    # ryter.g:325:7: pointerType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_pointerType_in_type2964)
                    pointerType72 = self.pointerType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, pointerType72.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "type"


    class simpleType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.simpleType_return, self).__init__()

            self.tree = None





    # $ANTLR start "simpleType"
    # ryter.g:328:1: simpleType : ( scalarType | subrangeType | typeIdentifier | stringtype );
    def simpleType(self, ):
        retval = self.simpleType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        scalarType73 = None
        subrangeType74 = None
        typeIdentifier75 = None
        stringtype76 = None


        try:
            try:
                # ryter.g:329:5: ( scalarType | subrangeType | typeIdentifier | stringtype )
                alt15 = 4
                LA15 = self.input.LA(1)
                if LA15 == LPAREN:
                    alt15 = 1
                elif LA15 == CHR or LA15 == MINUS or LA15 == NUM_INT or LA15 == NUM_REAL or LA15 == PLUS or LA15 == STRING_LITERAL:
                    alt15 = 2
                elif LA15 == IDENT:
                    LA15_3 = self.input.LA(2)

                    if (LA15_3 == DOTDOT) :
                        alt15 = 2
                    elif (LA15_3 == COMMA or LA15_3 == END or (RBRACK <= LA15_3 <= RBRACK2) or LA15_3 == RPAREN or LA15_3 == SEMI) :
                        alt15 = 3
                    else:
                        nvae = NoViableAltException("", 15, 3, self.input)

                        raise nvae


                elif LA15 == BOOLEAN or LA15 == CHAR or LA15 == INTEGER or LA15 == REAL:
                    alt15 = 3
                elif LA15 == STRING:
                    LA15_5 = self.input.LA(2)

                    if (LA15_5 == LBRACK2 or LA15_5 == LPAREN) :
                        alt15 = 4
                    elif (LA15_5 == COMMA or LA15_5 == END or (RBRACK <= LA15_5 <= RBRACK2) or LA15_5 == RPAREN or LA15_5 == SEMI) :
                        alt15 = 3
                    else:
                        nvae = NoViableAltException("", 15, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # ryter.g:329:7: scalarType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_scalarType_in_simpleType2981)
                    scalarType73 = self.scalarType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, scalarType73.tree)



                elif alt15 == 2:
                    # ryter.g:330:7: subrangeType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_subrangeType_in_simpleType2989)
                    subrangeType74 = self.subrangeType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, subrangeType74.tree)



                elif alt15 == 3:
                    # ryter.g:331:7: typeIdentifier
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typeIdentifier_in_simpleType2998)
                    typeIdentifier75 = self.typeIdentifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeIdentifier75.tree)



                elif alt15 == 4:
                    # ryter.g:332:7: stringtype
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_stringtype_in_simpleType3006)
                    stringtype76 = self.stringtype()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, stringtype76.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "simpleType"


    class scalarType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.scalarType_return, self).__init__()

            self.tree = None





    # $ANTLR start "scalarType"
    # ryter.g:335:1: scalarType : LPAREN identifierList RPAREN -> ^( SCALARTYPE identifierList ) ;
    def scalarType(self, ):
        retval = self.scalarType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LPAREN77 = None
        RPAREN79 = None
        identifierList78 = None

        LPAREN77_tree = None
        RPAREN79_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_identifierList = RewriteRuleSubtreeStream(self._adaptor, "rule identifierList")
        try:
            try:
                # ryter.g:336:5: ( LPAREN identifierList RPAREN -> ^( SCALARTYPE identifierList ) )
                # ryter.g:336:7: LPAREN identifierList RPAREN
                pass 
                LPAREN77 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_scalarType3023) 
                stream_LPAREN.add(LPAREN77)


                self._state.following.append(self.FOLLOW_identifierList_in_scalarType3025)
                identifierList78 = self.identifierList()

                self._state.following.pop()
                stream_identifierList.add(identifierList78.tree)


                RPAREN79 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_scalarType3027) 
                stream_RPAREN.add(RPAREN79)


                # AST Rewrite
                # elements: identifierList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 337:5: -> ^( SCALARTYPE identifierList )
                # ryter.g:337:8: ^( SCALARTYPE identifierList )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SCALARTYPE, "SCALARTYPE")
                , root_1)

                self._adaptor.addChild(root_1, stream_identifierList.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "scalarType"


    class subrangeType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.subrangeType_return, self).__init__()

            self.tree = None





    # $ANTLR start "subrangeType"
    # ryter.g:340:1: subrangeType : c1= constant DOTDOT c2= constant -> ^( SUBRANGE $c1 $c2) ;
    def subrangeType(self, ):
        retval = self.subrangeType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DOTDOT80 = None
        c1 = None
        c2 = None

        DOTDOT80_tree = None
        stream_DOTDOT = RewriteRuleTokenStream(self._adaptor, "token DOTDOT")
        stream_constant = RewriteRuleSubtreeStream(self._adaptor, "rule constant")
        try:
            try:
                # ryter.g:341:5: (c1= constant DOTDOT c2= constant -> ^( SUBRANGE $c1 $c2) )
                # ryter.g:341:7: c1= constant DOTDOT c2= constant
                pass 
                self._state.following.append(self.FOLLOW_constant_in_subrangeType3059)
                c1 = self.constant()

                self._state.following.pop()
                stream_constant.add(c1.tree)


                DOTDOT80 = self.match(self.input, DOTDOT, self.FOLLOW_DOTDOT_in_subrangeType3061) 
                stream_DOTDOT.add(DOTDOT80)


                self._state.following.append(self.FOLLOW_constant_in_subrangeType3065)
                c2 = self.constant()

                self._state.following.pop()
                stream_constant.add(c2.tree)


                # AST Rewrite
                # elements: c2, c1
                # token labels: 
                # rule labels: retval, c1, c2
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                if c1 is not None:
                    stream_c1 = RewriteRuleSubtreeStream(self._adaptor, "rule c1", c1.tree)
                else:
                    stream_c1 = RewriteRuleSubtreeStream(self._adaptor, "token c1", None)

                if c2 is not None:
                    stream_c2 = RewriteRuleSubtreeStream(self._adaptor, "rule c2", c2.tree)
                else:
                    stream_c2 = RewriteRuleSubtreeStream(self._adaptor, "token c2", None)


                root_0 = self._adaptor.nil()
                # 342:5: -> ^( SUBRANGE $c1 $c2)
                # ryter.g:342:8: ^( SUBRANGE $c1 $c2)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SUBRANGE, "SUBRANGE")
                , root_1)

                self._adaptor.addChild(root_1, stream_c1.nextTree())

                self._adaptor.addChild(root_1, stream_c2.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "subrangeType"


    class typeIdentifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.typeIdentifier_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeIdentifier"
    # ryter.g:345:1: typeIdentifier : ( identifier | CHAR | BOOLEAN | INTEGER | REAL | STRING );
    def typeIdentifier(self, ):
        retval = self.typeIdentifier_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CHAR82 = None
        BOOLEAN83 = None
        INTEGER84 = None
        REAL85 = None
        STRING86 = None
        identifier81 = None

        CHAR82_tree = None
        BOOLEAN83_tree = None
        INTEGER84_tree = None
        REAL85_tree = None
        STRING86_tree = None

        try:
            try:
                # ryter.g:346:5: ( identifier | CHAR | BOOLEAN | INTEGER | REAL | STRING )
                alt16 = 6
                LA16 = self.input.LA(1)
                if LA16 == IDENT:
                    alt16 = 1
                elif LA16 == CHAR:
                    alt16 = 2
                elif LA16 == BOOLEAN:
                    alt16 = 3
                elif LA16 == INTEGER:
                    alt16 = 4
                elif LA16 == REAL:
                    alt16 = 5
                elif LA16 == STRING:
                    alt16 = 6
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # ryter.g:346:7: identifier
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_identifier_in_typeIdentifier3098)
                    identifier81 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier81.tree)



                elif alt16 == 2:
                    # ryter.g:347:7: CHAR
                    pass 
                    root_0 = self._adaptor.nil()


                    CHAR82 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_typeIdentifier3106)
                    CHAR82_tree = self._adaptor.createWithPayload(CHAR82)
                    self._adaptor.addChild(root_0, CHAR82_tree)




                elif alt16 == 3:
                    # ryter.g:348:7: BOOLEAN
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOLEAN83 = self.match(self.input, BOOLEAN, self.FOLLOW_BOOLEAN_in_typeIdentifier3114)
                    BOOLEAN83_tree = self._adaptor.createWithPayload(BOOLEAN83)
                    self._adaptor.addChild(root_0, BOOLEAN83_tree)




                elif alt16 == 4:
                    # ryter.g:349:7: INTEGER
                    pass 
                    root_0 = self._adaptor.nil()


                    INTEGER84 = self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_typeIdentifier3122)
                    INTEGER84_tree = self._adaptor.createWithPayload(INTEGER84)
                    self._adaptor.addChild(root_0, INTEGER84_tree)




                elif alt16 == 5:
                    # ryter.g:350:7: REAL
                    pass 
                    root_0 = self._adaptor.nil()


                    REAL85 = self.match(self.input, REAL, self.FOLLOW_REAL_in_typeIdentifier3130)
                    REAL85_tree = self._adaptor.createWithPayload(REAL85)
                    self._adaptor.addChild(root_0, REAL85_tree)




                elif alt16 == 6:
                    # ryter.g:351:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING86 = self.match(self.input, STRING, self.FOLLOW_STRING_in_typeIdentifier3138)
                    STRING86_tree = self._adaptor.createWithPayload(STRING86)
                    self._adaptor.addChild(root_0, STRING86_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "typeIdentifier"


    class structuredType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.structuredType_return, self).__init__()

            self.tree = None





    # $ANTLR start "structuredType"
    # ryter.g:354:1: structuredType : ( PACKED ^ unpackedStructuredType | unpackedStructuredType );
    def structuredType(self, ):
        retval = self.structuredType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PACKED87 = None
        unpackedStructuredType88 = None
        unpackedStructuredType89 = None

        PACKED87_tree = None

        try:
            try:
                # ryter.g:355:5: ( PACKED ^ unpackedStructuredType | unpackedStructuredType )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == PACKED) :
                    alt17 = 1
                elif (LA17_0 == ARRAY or LA17_0 == CHR or LA17_0 == FILE or LA17_0 == IDENT or LA17_0 == MINUS or (NUM_INT <= LA17_0 <= NUM_REAL) or LA17_0 == PLUS or LA17_0 == RECORD or LA17_0 == SET or LA17_0 == STRING_LITERAL) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # ryter.g:355:7: PACKED ^ unpackedStructuredType
                    pass 
                    root_0 = self._adaptor.nil()


                    PACKED87 = self.match(self.input, PACKED, self.FOLLOW_PACKED_in_structuredType3156)
                    PACKED87_tree = self._adaptor.createWithPayload(PACKED87)
                    root_0 = self._adaptor.becomeRoot(PACKED87_tree, root_0)



                    self._state.following.append(self.FOLLOW_unpackedStructuredType_in_structuredType3159)
                    unpackedStructuredType88 = self.unpackedStructuredType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unpackedStructuredType88.tree)



                elif alt17 == 2:
                    # ryter.g:356:6: unpackedStructuredType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unpackedStructuredType_in_structuredType3166)
                    unpackedStructuredType89 = self.unpackedStructuredType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unpackedStructuredType89.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "structuredType"


    class unpackedStructuredType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.unpackedStructuredType_return, self).__init__()

            self.tree = None





    # $ANTLR start "unpackedStructuredType"
    # ryter.g:359:1: unpackedStructuredType : ( arrayType | recordType | setType | fileType | subrangeType );
    def unpackedStructuredType(self, ):
        retval = self.unpackedStructuredType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arrayType90 = None
        recordType91 = None
        setType92 = None
        fileType93 = None
        subrangeType94 = None


        try:
            try:
                # ryter.g:360:5: ( arrayType | recordType | setType | fileType | subrangeType )
                alt18 = 5
                LA18 = self.input.LA(1)
                if LA18 == ARRAY:
                    alt18 = 1
                elif LA18 == RECORD:
                    alt18 = 2
                elif LA18 == SET:
                    alt18 = 3
                elif LA18 == FILE:
                    alt18 = 4
                elif LA18 == CHR or LA18 == IDENT or LA18 == MINUS or LA18 == NUM_INT or LA18 == NUM_REAL or LA18 == PLUS or LA18 == STRING_LITERAL:
                    alt18 = 5
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # ryter.g:360:7: arrayType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_arrayType_in_unpackedStructuredType3183)
                    arrayType90 = self.arrayType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, arrayType90.tree)



                elif alt18 == 2:
                    # ryter.g:361:7: recordType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_recordType_in_unpackedStructuredType3191)
                    recordType91 = self.recordType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, recordType91.tree)



                elif alt18 == 3:
                    # ryter.g:362:7: setType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_setType_in_unpackedStructuredType3199)
                    setType92 = self.setType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, setType92.tree)



                elif alt18 == 4:
                    # ryter.g:363:7: fileType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_fileType_in_unpackedStructuredType3207)
                    fileType93 = self.fileType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, fileType93.tree)



                elif alt18 == 5:
                    # ryter.g:364:7: subrangeType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_subrangeType_in_unpackedStructuredType3215)
                    subrangeType94 = self.subrangeType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, subrangeType94.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unpackedStructuredType"


    class stringtype_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.stringtype_return, self).__init__()

            self.tree = None





    # $ANTLR start "stringtype"
    # ryter.g:367:1: stringtype : ( STRING ^ LPAREN ! ( identifier | unsignedNumber ) RPAREN !| STRING ^ LBRACK2 ! ( identifier | unsignedNumber ) RBRACK2 !);
    def stringtype(self, ):
        retval = self.stringtype_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STRING95 = None
        LPAREN96 = None
        RPAREN99 = None
        STRING100 = None
        LBRACK2101 = None
        RBRACK2104 = None
        identifier97 = None
        unsignedNumber98 = None
        identifier102 = None
        unsignedNumber103 = None

        STRING95_tree = None
        LPAREN96_tree = None
        RPAREN99_tree = None
        STRING100_tree = None
        LBRACK2101_tree = None
        RBRACK2104_tree = None

        try:
            try:
                # ryter.g:368:5: ( STRING ^ LPAREN ! ( identifier | unsignedNumber ) RPAREN !| STRING ^ LBRACK2 ! ( identifier | unsignedNumber ) RBRACK2 !)
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == STRING) :
                    LA21_1 = self.input.LA(2)

                    if (LA21_1 == LPAREN) :
                        alt21 = 1
                    elif (LA21_1 == LBRACK2) :
                        alt21 = 2
                    else:
                        nvae = NoViableAltException("", 21, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # ryter.g:368:7: STRING ^ LPAREN ! ( identifier | unsignedNumber ) RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING95 = self.match(self.input, STRING, self.FOLLOW_STRING_in_stringtype3233)
                    STRING95_tree = self._adaptor.createWithPayload(STRING95)
                    root_0 = self._adaptor.becomeRoot(STRING95_tree, root_0)



                    LPAREN96 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_stringtype3236)

                    # ryter.g:368:23: ( identifier | unsignedNumber )
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == IDENT) :
                        alt19 = 1
                    elif ((NUM_INT <= LA19_0 <= NUM_REAL)) :
                        alt19 = 2
                    else:
                        nvae = NoViableAltException("", 19, 0, self.input)

                        raise nvae


                    if alt19 == 1:
                        # ryter.g:368:24: identifier
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_stringtype3240)
                        identifier97 = self.identifier()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, identifier97.tree)



                    elif alt19 == 2:
                        # ryter.g:368:35: unsignedNumber
                        pass 
                        self._state.following.append(self.FOLLOW_unsignedNumber_in_stringtype3242)
                        unsignedNumber98 = self.unsignedNumber()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, unsignedNumber98.tree)





                    RPAREN99 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_stringtype3245)


                elif alt21 == 2:
                    # ryter.g:369:7: STRING ^ LBRACK2 ! ( identifier | unsignedNumber ) RBRACK2 !
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING100 = self.match(self.input, STRING, self.FOLLOW_STRING_in_stringtype3255)
                    STRING100_tree = self._adaptor.createWithPayload(STRING100)
                    root_0 = self._adaptor.becomeRoot(STRING100_tree, root_0)



                    LBRACK2101 = self.match(self.input, LBRACK2, self.FOLLOW_LBRACK2_in_stringtype3258)

                    # ryter.g:369:24: ( identifier | unsignedNumber )
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == IDENT) :
                        alt20 = 1
                    elif ((NUM_INT <= LA20_0 <= NUM_REAL)) :
                        alt20 = 2
                    else:
                        nvae = NoViableAltException("", 20, 0, self.input)

                        raise nvae


                    if alt20 == 1:
                        # ryter.g:369:25: identifier
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_stringtype3262)
                        identifier102 = self.identifier()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, identifier102.tree)



                    elif alt20 == 2:
                        # ryter.g:369:36: unsignedNumber
                        pass 
                        self._state.following.append(self.FOLLOW_unsignedNumber_in_stringtype3264)
                        unsignedNumber103 = self.unsignedNumber()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, unsignedNumber103.tree)





                    RBRACK2104 = self.match(self.input, RBRACK2, self.FOLLOW_RBRACK2_in_stringtype3267)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "stringtype"


    class arrayType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.arrayType_return, self).__init__()

            self.tree = None





    # $ANTLR start "arrayType"
    # ryter.g:372:1: arrayType : ( ARRAY ^ LBRACK ! typeList RBRACK ! OF ! componentType | ARRAY ^ LBRACK2 ! typeList RBRACK2 ! OF ! componentType );
    def arrayType(self, ):
        retval = self.arrayType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARRAY105 = None
        LBRACK106 = None
        RBRACK108 = None
        OF109 = None
        ARRAY111 = None
        LBRACK2112 = None
        RBRACK2114 = None
        OF115 = None
        typeList107 = None
        componentType110 = None
        typeList113 = None
        componentType116 = None

        ARRAY105_tree = None
        LBRACK106_tree = None
        RBRACK108_tree = None
        OF109_tree = None
        ARRAY111_tree = None
        LBRACK2112_tree = None
        RBRACK2114_tree = None
        OF115_tree = None

        try:
            try:
                # ryter.g:373:5: ( ARRAY ^ LBRACK ! typeList RBRACK ! OF ! componentType | ARRAY ^ LBRACK2 ! typeList RBRACK2 ! OF ! componentType )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == ARRAY) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == LBRACK) :
                        alt22 = 1
                    elif (LA22_1 == LBRACK2) :
                        alt22 = 2
                    else:
                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # ryter.g:373:7: ARRAY ^ LBRACK ! typeList RBRACK ! OF ! componentType
                    pass 
                    root_0 = self._adaptor.nil()


                    ARRAY105 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_arrayType3286)
                    ARRAY105_tree = self._adaptor.createWithPayload(ARRAY105)
                    root_0 = self._adaptor.becomeRoot(ARRAY105_tree, root_0)



                    LBRACK106 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_arrayType3289)

                    self._state.following.append(self.FOLLOW_typeList_in_arrayType3292)
                    typeList107 = self.typeList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeList107.tree)


                    RBRACK108 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_arrayType3294)

                    OF109 = self.match(self.input, OF, self.FOLLOW_OF_in_arrayType3297)

                    self._state.following.append(self.FOLLOW_componentType_in_arrayType3300)
                    componentType110 = self.componentType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, componentType110.tree)



                elif alt22 == 2:
                    # ryter.g:374:7: ARRAY ^ LBRACK2 ! typeList RBRACK2 ! OF ! componentType
                    pass 
                    root_0 = self._adaptor.nil()


                    ARRAY111 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_arrayType3308)
                    ARRAY111_tree = self._adaptor.createWithPayload(ARRAY111)
                    root_0 = self._adaptor.becomeRoot(ARRAY111_tree, root_0)



                    LBRACK2112 = self.match(self.input, LBRACK2, self.FOLLOW_LBRACK2_in_arrayType3311)

                    self._state.following.append(self.FOLLOW_typeList_in_arrayType3314)
                    typeList113 = self.typeList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeList113.tree)


                    RBRACK2114 = self.match(self.input, RBRACK2, self.FOLLOW_RBRACK2_in_arrayType3316)

                    OF115 = self.match(self.input, OF, self.FOLLOW_OF_in_arrayType3319)

                    self._state.following.append(self.FOLLOW_componentType_in_arrayType3322)
                    componentType116 = self.componentType()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, componentType116.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arrayType"


    class typeList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.typeList_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeList"
    # ryter.g:377:1: typeList : indexType ( COMMA indexType )* -> ^( TYPELIST ( indexType )+ ) ;
    def typeList(self, ):
        retval = self.typeList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA118 = None
        indexType117 = None
        indexType119 = None

        COMMA118_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_indexType = RewriteRuleSubtreeStream(self._adaptor, "rule indexType")
        try:
            try:
                # ryter.g:378:3: ( indexType ( COMMA indexType )* -> ^( TYPELIST ( indexType )+ ) )
                # ryter.g:378:5: indexType ( COMMA indexType )*
                pass 
                self._state.following.append(self.FOLLOW_indexType_in_typeList3335)
                indexType117 = self.indexType()

                self._state.following.pop()
                stream_indexType.add(indexType117.tree)


                # ryter.g:378:15: ( COMMA indexType )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == COMMA) :
                        alt23 = 1


                    if alt23 == 1:
                        # ryter.g:378:17: COMMA indexType
                        pass 
                        COMMA118 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_typeList3339) 
                        stream_COMMA.add(COMMA118)


                        self._state.following.append(self.FOLLOW_indexType_in_typeList3341)
                        indexType119 = self.indexType()

                        self._state.following.pop()
                        stream_indexType.add(indexType119.tree)



                    else:
                        break #loop23


                # AST Rewrite
                # elements: indexType
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 379:3: -> ^( TYPELIST ( indexType )+ )
                # ryter.g:379:6: ^( TYPELIST ( indexType )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TYPELIST, "TYPELIST")
                , root_1)

                # ryter.g:379:17: ( indexType )+
                if not (stream_indexType.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_indexType.hasNext():
                    self._adaptor.addChild(root_1, stream_indexType.nextTree())


                stream_indexType.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "typeList"


    class indexType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.indexType_return, self).__init__()

            self.tree = None





    # $ANTLR start "indexType"
    # ryter.g:382:1: indexType : simpleType ;
    def indexType(self, ):
        retval = self.indexType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        simpleType120 = None


        try:
            try:
                # ryter.g:383:5: ( simpleType )
                # ryter.g:383:7: simpleType
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_simpleType_in_indexType3370)
                simpleType120 = self.simpleType()

                self._state.following.pop()
                self._adaptor.addChild(root_0, simpleType120.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "indexType"


    class componentType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.componentType_return, self).__init__()

            self.tree = None





    # $ANTLR start "componentType"
    # ryter.g:386:1: componentType : type ;
    def componentType(self, ):
        retval = self.componentType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        type121 = None


        try:
            try:
                # ryter.g:387:5: ( type )
                # ryter.g:387:7: type
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_type_in_componentType3387)
                type121 = self.type()

                self._state.following.pop()
                self._adaptor.addChild(root_0, type121.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "componentType"


    class recordType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.recordType_return, self).__init__()

            self.tree = None





    # $ANTLR start "recordType"
    # ryter.g:390:1: recordType : RECORD ^ fieldList END !;
    def recordType(self, ):
        retval = self.recordType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECORD122 = None
        END124 = None
        fieldList123 = None

        RECORD122_tree = None
        END124_tree = None

        try:
            try:
                # ryter.g:391:5: ( RECORD ^ fieldList END !)
                # ryter.g:391:7: RECORD ^ fieldList END !
                pass 
                root_0 = self._adaptor.nil()


                RECORD122 = self.match(self.input, RECORD, self.FOLLOW_RECORD_in_recordType3404)
                RECORD122_tree = self._adaptor.createWithPayload(RECORD122)
                root_0 = self._adaptor.becomeRoot(RECORD122_tree, root_0)



                self._state.following.append(self.FOLLOW_fieldList_in_recordType3407)
                fieldList123 = self.fieldList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, fieldList123.tree)


                END124 = self.match(self.input, END, self.FOLLOW_END_in_recordType3409)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "recordType"


    class fieldList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.fieldList_return, self).__init__()

            self.tree = None





    # $ANTLR start "fieldList"
    # ryter.g:394:1: fieldList : (f1= fixedPart ( SEMI f2= variantPart | SEMI )? |f3= variantPart ) -> ^( FIELDLIST ( $f1)? ( $f2)? ( $f3)? ) ;
    def fieldList(self, ):
        retval = self.fieldList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMI125 = None
        SEMI126 = None
        f1 = None
        f2 = None
        f3 = None

        SEMI125_tree = None
        SEMI126_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_fixedPart = RewriteRuleSubtreeStream(self._adaptor, "rule fixedPart")
        stream_variantPart = RewriteRuleSubtreeStream(self._adaptor, "rule variantPart")
        try:
            try:
                # ryter.g:395:5: ( (f1= fixedPart ( SEMI f2= variantPart | SEMI )? |f3= variantPart ) -> ^( FIELDLIST ( $f1)? ( $f2)? ( $f3)? ) )
                # ryter.g:395:7: (f1= fixedPart ( SEMI f2= variantPart | SEMI )? |f3= variantPart )
                pass 
                # ryter.g:395:7: (f1= fixedPart ( SEMI f2= variantPart | SEMI )? |f3= variantPart )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == IDENT) :
                    alt25 = 1
                elif (LA25_0 == CASE) :
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # ryter.g:395:9: f1= fixedPart ( SEMI f2= variantPart | SEMI )?
                    pass 
                    self._state.following.append(self.FOLLOW_fixedPart_in_fieldList3431)
                    f1 = self.fixedPart()

                    self._state.following.pop()
                    stream_fixedPart.add(f1.tree)


                    # ryter.g:395:22: ( SEMI f2= variantPart | SEMI )?
                    alt24 = 3
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == SEMI) :
                        LA24_1 = self.input.LA(2)

                        if (LA24_1 == CASE) :
                            alt24 = 1
                        elif (LA24_1 == END or LA24_1 == RPAREN) :
                            alt24 = 2
                    if alt24 == 1:
                        # ryter.g:395:24: SEMI f2= variantPart
                        pass 
                        SEMI125 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_fieldList3435) 
                        stream_SEMI.add(SEMI125)


                        self._state.following.append(self.FOLLOW_variantPart_in_fieldList3439)
                        f2 = self.variantPart()

                        self._state.following.pop()
                        stream_variantPart.add(f2.tree)



                    elif alt24 == 2:
                        # ryter.g:395:46: SEMI
                        pass 
                        SEMI126 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_fieldList3443) 
                        stream_SEMI.add(SEMI126)






                elif alt25 == 2:
                    # ryter.g:396:9: f3= variantPart
                    pass 
                    self._state.following.append(self.FOLLOW_variantPart_in_fieldList3458)
                    f3 = self.variantPart()

                    self._state.following.pop()
                    stream_variantPart.add(f3.tree)





                # AST Rewrite
                # elements: f3, f2, f1
                # token labels: 
                # rule labels: retval, f1, f3, f2
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                if f1 is not None:
                    stream_f1 = RewriteRuleSubtreeStream(self._adaptor, "rule f1", f1.tree)
                else:
                    stream_f1 = RewriteRuleSubtreeStream(self._adaptor, "token f1", None)

                if f3 is not None:
                    stream_f3 = RewriteRuleSubtreeStream(self._adaptor, "rule f3", f3.tree)
                else:
                    stream_f3 = RewriteRuleSubtreeStream(self._adaptor, "token f3", None)

                if f2 is not None:
                    stream_f2 = RewriteRuleSubtreeStream(self._adaptor, "rule f2", f2.tree)
                else:
                    stream_f2 = RewriteRuleSubtreeStream(self._adaptor, "token f2", None)


                root_0 = self._adaptor.nil()
                # 398:7: -> ^( FIELDLIST ( $f1)? ( $f2)? ( $f3)? )
                # ryter.g:398:10: ^( FIELDLIST ( $f1)? ( $f2)? ( $f3)? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(FIELDLIST, "FIELDLIST")
                , root_1)

                # ryter.g:398:23: ( $f1)?
                if stream_f1.hasNext():
                    self._adaptor.addChild(root_1, stream_f1.nextTree())


                stream_f1.reset();

                # ryter.g:398:28: ( $f2)?
                if stream_f2.hasNext():
                    self._adaptor.addChild(root_1, stream_f2.nextTree())


                stream_f2.reset();

                # ryter.g:398:33: ( $f3)?
                if stream_f3.hasNext():
                    self._adaptor.addChild(root_1, stream_f3.nextTree())


                stream_f3.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fieldList"


    class fixedPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.fixedPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "fixedPart"
    # ryter.g:401:1: fixedPart : recordSection ( SEMI ! recordSection )* ;
    def fixedPart(self, ):
        retval = self.fixedPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMI128 = None
        recordSection127 = None
        recordSection129 = None

        SEMI128_tree = None

        try:
            try:
                # ryter.g:402:5: ( recordSection ( SEMI ! recordSection )* )
                # ryter.g:402:7: recordSection ( SEMI ! recordSection )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_recordSection_in_fixedPart3507)
                recordSection127 = self.recordSection()

                self._state.following.pop()
                self._adaptor.addChild(root_0, recordSection127.tree)


                # ryter.g:402:21: ( SEMI ! recordSection )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == SEMI) :
                        LA26_1 = self.input.LA(2)

                        if (LA26_1 == IDENT) :
                            alt26 = 1




                    if alt26 == 1:
                        # ryter.g:402:23: SEMI ! recordSection
                        pass 
                        SEMI128 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_fixedPart3511)

                        self._state.following.append(self.FOLLOW_recordSection_in_fixedPart3514)
                        recordSection129 = self.recordSection()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, recordSection129.tree)



                    else:
                        break #loop26




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fixedPart"


    class recordSection_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.recordSection_return, self).__init__()

            self.tree = None





    # $ANTLR start "recordSection"
    # ryter.g:405:1: recordSection : identifierList COLON type -> ^( FIELD identifierList type ) ;
    def recordSection(self, ):
        retval = self.recordSection_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COLON131 = None
        identifierList130 = None
        type132 = None

        COLON131_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_identifierList = RewriteRuleSubtreeStream(self._adaptor, "rule identifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        try:
            try:
                # ryter.g:406:5: ( identifierList COLON type -> ^( FIELD identifierList type ) )
                # ryter.g:406:7: identifierList COLON type
                pass 
                self._state.following.append(self.FOLLOW_identifierList_in_recordSection3534)
                identifierList130 = self.identifierList()

                self._state.following.pop()
                stream_identifierList.add(identifierList130.tree)


                COLON131 = self.match(self.input, COLON, self.FOLLOW_COLON_in_recordSection3536) 
                stream_COLON.add(COLON131)


                self._state.following.append(self.FOLLOW_type_in_recordSection3538)
                type132 = self.type()

                self._state.following.pop()
                stream_type.add(type132.tree)


                # AST Rewrite
                # elements: type, identifierList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 407:5: -> ^( FIELD identifierList type )
                # ryter.g:407:8: ^( FIELD identifierList type )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(FIELD, "FIELD")
                , root_1)

                self._adaptor.addChild(root_1, stream_identifierList.nextTree())

                self._adaptor.addChild(root_1, stream_type.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "recordSection"


    class variantPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.variantPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "variantPart"
    # ryter.g:410:1: variantPart : CASE ^ tag OF ! variant ( SEMI ! variant | SEMI !)* ;
    def variantPart(self, ):
        retval = self.variantPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CASE133 = None
        OF135 = None
        SEMI137 = None
        SEMI139 = None
        tag134 = None
        variant136 = None
        variant138 = None

        CASE133_tree = None
        OF135_tree = None
        SEMI137_tree = None
        SEMI139_tree = None

        try:
            try:
                # ryter.g:411:5: ( CASE ^ tag OF ! variant ( SEMI ! variant | SEMI !)* )
                # ryter.g:411:7: CASE ^ tag OF ! variant ( SEMI ! variant | SEMI !)*
                pass 
                root_0 = self._adaptor.nil()


                CASE133 = self.match(self.input, CASE, self.FOLLOW_CASE_in_variantPart3569)
                CASE133_tree = self._adaptor.createWithPayload(CASE133)
                root_0 = self._adaptor.becomeRoot(CASE133_tree, root_0)



                self._state.following.append(self.FOLLOW_tag_in_variantPart3572)
                tag134 = self.tag()

                self._state.following.pop()
                self._adaptor.addChild(root_0, tag134.tree)


                OF135 = self.match(self.input, OF, self.FOLLOW_OF_in_variantPart3574)

                self._state.following.append(self.FOLLOW_variant_in_variantPart3577)
                variant136 = self.variant()

                self._state.following.pop()
                self._adaptor.addChild(root_0, variant136.tree)


                # ryter.g:411:29: ( SEMI ! variant | SEMI !)*
                while True: #loop27
                    alt27 = 3
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == SEMI) :
                        LA27_2 = self.input.LA(2)

                        if (LA27_2 == CHR or LA27_2 == IDENT or LA27_2 == MINUS or (NUM_INT <= LA27_2 <= NUM_REAL) or LA27_2 == PLUS or LA27_2 == STRING_LITERAL) :
                            alt27 = 1
                        elif (LA27_2 == END or LA27_2 == RPAREN or LA27_2 == SEMI) :
                            alt27 = 2




                    if alt27 == 1:
                        # ryter.g:411:31: SEMI ! variant
                        pass 
                        SEMI137 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_variantPart3581)

                        self._state.following.append(self.FOLLOW_variant_in_variantPart3584)
                        variant138 = self.variant()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, variant138.tree)



                    elif alt27 == 2:
                        # ryter.g:411:47: SEMI !
                        pass 
                        SEMI139 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_variantPart3588)


                    else:
                        break #loop27




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "variantPart"


    class tag_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.tag_return, self).__init__()

            self.tree = None





    # $ANTLR start "tag"
    # ryter.g:414:1: tag : (id= identifier COLON t= typeIdentifier -> ^( VARIANT_TAG $id $t) |t2= typeIdentifier -> ^( VARIANT_TAG_NO_ID $t2) );
    def tag(self, ):
        retval = self.tag_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COLON140 = None
        id = None
        t = None
        t2 = None

        COLON140_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_typeIdentifier = RewriteRuleSubtreeStream(self._adaptor, "rule typeIdentifier")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # ryter.g:415:5: (id= identifier COLON t= typeIdentifier -> ^( VARIANT_TAG $id $t) |t2= typeIdentifier -> ^( VARIANT_TAG_NO_ID $t2) )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == IDENT) :
                    LA28_1 = self.input.LA(2)

                    if (LA28_1 == COLON) :
                        alt28 = 1
                    elif (LA28_1 == OF) :
                        alt28 = 2
                    else:
                        nvae = NoViableAltException("", 28, 1, self.input)

                        raise nvae


                elif (LA28_0 == BOOLEAN or LA28_0 == CHAR or LA28_0 == INTEGER or LA28_0 == REAL or LA28_0 == STRING) :
                    alt28 = 2
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # ryter.g:415:7: id= identifier COLON t= typeIdentifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_tag3611)
                    id = self.identifier()

                    self._state.following.pop()
                    stream_identifier.add(id.tree)


                    COLON140 = self.match(self.input, COLON, self.FOLLOW_COLON_in_tag3613) 
                    stream_COLON.add(COLON140)


                    self._state.following.append(self.FOLLOW_typeIdentifier_in_tag3617)
                    t = self.typeIdentifier()

                    self._state.following.pop()
                    stream_typeIdentifier.add(t.tree)


                    # AST Rewrite
                    # elements: id, t
                    # token labels: 
                    # rule labels: id, retval, t
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if id is not None:
                        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id", id.tree)
                    else:
                        stream_id = RewriteRuleSubtreeStream(self._adaptor, "token id", None)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    if t is not None:
                        stream_t = RewriteRuleSubtreeStream(self._adaptor, "rule t", t.tree)
                    else:
                        stream_t = RewriteRuleSubtreeStream(self._adaptor, "token t", None)


                    root_0 = self._adaptor.nil()
                    # 415:44: -> ^( VARIANT_TAG $id $t)
                    # ryter.g:415:47: ^( VARIANT_TAG $id $t)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VARIANT_TAG, "VARIANT_TAG")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_id.nextTree())

                    self._adaptor.addChild(root_1, stream_t.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt28 == 2:
                    # ryter.g:416:7: t2= typeIdentifier
                    pass 
                    self._state.following.append(self.FOLLOW_typeIdentifier_in_tag3640)
                    t2 = self.typeIdentifier()

                    self._state.following.pop()
                    stream_typeIdentifier.add(t2.tree)


                    # AST Rewrite
                    # elements: t2
                    # token labels: 
                    # rule labels: t2, retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if t2 is not None:
                        stream_t2 = RewriteRuleSubtreeStream(self._adaptor, "rule t2", t2.tree)
                    else:
                        stream_t2 = RewriteRuleSubtreeStream(self._adaptor, "token t2", None)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 416:26: -> ^( VARIANT_TAG_NO_ID $t2)
                    # ryter.g:416:29: ^( VARIANT_TAG_NO_ID $t2)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VARIANT_TAG_NO_ID, "VARIANT_TAG_NO_ID")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_t2.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "tag"


    class variant_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.variant_return, self).__init__()

            self.tree = None





    # $ANTLR start "variant"
    # ryter.g:419:1: variant : constList c= COLON ^ LPAREN ! fieldList RPAREN !;
    def variant(self, ):
        retval = self.variant_return()
        retval.start = self.input.LT(1)


        root_0 = None

        c = None
        LPAREN142 = None
        RPAREN144 = None
        constList141 = None
        fieldList143 = None

        c_tree = None
        LPAREN142_tree = None
        RPAREN144_tree = None

        try:
            try:
                # ryter.g:420:5: ( constList c= COLON ^ LPAREN ! fieldList RPAREN !)
                # ryter.g:420:7: constList c= COLON ^ LPAREN ! fieldList RPAREN !
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_constList_in_variant3667)
                constList141 = self.constList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, constList141.tree)


                c = self.match(self.input, COLON, self.FOLLOW_COLON_in_variant3671)
                c_tree = self._adaptor.createWithPayload(c)
                root_0 = self._adaptor.becomeRoot(c_tree, root_0)



                #action start
                c.setType(VARIANT_CASE);
                #action end


                LPAREN142 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_variant3680)

                self._state.following.append(self.FOLLOW_fieldList_in_variant3683)
                fieldList143 = self.fieldList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, fieldList143.tree)


                RPAREN144 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_variant3685)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "variant"


    class setType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.setType_return, self).__init__()

            self.tree = None





    # $ANTLR start "setType"
    # ryter.g:424:1: setType : SET ^ OF ! simpleType ;
    def setType(self, ):
        retval = self.setType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET145 = None
        OF146 = None
        simpleType147 = None

        SET145_tree = None
        OF146_tree = None

        try:
            try:
                # ryter.g:425:5: ( SET ^ OF ! simpleType )
                # ryter.g:425:7: SET ^ OF ! simpleType
                pass 
                root_0 = self._adaptor.nil()


                SET145 = self.match(self.input, SET, self.FOLLOW_SET_in_setType3703)
                SET145_tree = self._adaptor.createWithPayload(SET145)
                root_0 = self._adaptor.becomeRoot(SET145_tree, root_0)



                OF146 = self.match(self.input, OF, self.FOLLOW_OF_in_setType3706)

                self._state.following.append(self.FOLLOW_simpleType_in_setType3709)
                simpleType147 = self.simpleType()

                self._state.following.pop()
                self._adaptor.addChild(root_0, simpleType147.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "setType"


    class fileType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.fileType_return, self).__init__()

            self.tree = None





    # $ANTLR start "fileType"
    # ryter.g:428:1: fileType : ( FILE ^ OF ! type | FILE );
    def fileType(self, ):
        retval = self.fileType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FILE148 = None
        OF149 = None
        FILE151 = None
        type150 = None

        FILE148_tree = None
        OF149_tree = None
        FILE151_tree = None

        try:
            try:
                # ryter.g:429:5: ( FILE ^ OF ! type | FILE )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == FILE) :
                    LA29_1 = self.input.LA(2)

                    if (LA29_1 == OF) :
                        alt29 = 1
                    elif (LA29_1 == END or LA29_1 == RPAREN or LA29_1 == SEMI) :
                        alt29 = 2
                    else:
                        nvae = NoViableAltException("", 29, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # ryter.g:429:7: FILE ^ OF ! type
                    pass 
                    root_0 = self._adaptor.nil()


                    FILE148 = self.match(self.input, FILE, self.FOLLOW_FILE_in_fileType3726)
                    FILE148_tree = self._adaptor.createWithPayload(FILE148)
                    root_0 = self._adaptor.becomeRoot(FILE148_tree, root_0)



                    OF149 = self.match(self.input, OF, self.FOLLOW_OF_in_fileType3729)

                    self._state.following.append(self.FOLLOW_type_in_fileType3732)
                    type150 = self.type()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, type150.tree)



                elif alt29 == 2:
                    # ryter.g:430:7: FILE
                    pass 
                    root_0 = self._adaptor.nil()


                    FILE151 = self.match(self.input, FILE, self.FOLLOW_FILE_in_fileType3740)
                    FILE151_tree = self._adaptor.createWithPayload(FILE151)
                    self._adaptor.addChild(root_0, FILE151_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fileType"


    class pointerType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.pointerType_return, self).__init__()

            self.tree = None





    # $ANTLR start "pointerType"
    # ryter.g:433:1: pointerType : POINTER ^ typeIdentifier ;
    def pointerType(self, ):
        retval = self.pointerType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        POINTER152 = None
        typeIdentifier153 = None

        POINTER152_tree = None

        try:
            try:
                # ryter.g:434:5: ( POINTER ^ typeIdentifier )
                # ryter.g:434:7: POINTER ^ typeIdentifier
                pass 
                root_0 = self._adaptor.nil()


                POINTER152 = self.match(self.input, POINTER, self.FOLLOW_POINTER_in_pointerType3757)
                POINTER152_tree = self._adaptor.createWithPayload(POINTER152)
                root_0 = self._adaptor.becomeRoot(POINTER152_tree, root_0)



                self._state.following.append(self.FOLLOW_typeIdentifier_in_pointerType3760)
                typeIdentifier153 = self.typeIdentifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, typeIdentifier153.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "pointerType"


    class variableDeclarationPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.variableDeclarationPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "variableDeclarationPart"
    # ryter.g:438:1: variableDeclarationPart : VAR ^ variableDeclaration ( SEMI ! variableDeclaration )* SEMI !;
    def variableDeclarationPart(self, ):
        retval = self.variableDeclarationPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VAR154 = None
        SEMI156 = None
        SEMI158 = None
        variableDeclaration155 = None
        variableDeclaration157 = None

        VAR154_tree = None
        SEMI156_tree = None
        SEMI158_tree = None

        try:
            try:
                # ryter.g:439:5: ( VAR ^ variableDeclaration ( SEMI ! variableDeclaration )* SEMI !)
                # ryter.g:439:7: VAR ^ variableDeclaration ( SEMI ! variableDeclaration )* SEMI !
                pass 
                root_0 = self._adaptor.nil()


                VAR154 = self.match(self.input, VAR, self.FOLLOW_VAR_in_variableDeclarationPart3778)
                VAR154_tree = self._adaptor.createWithPayload(VAR154)
                root_0 = self._adaptor.becomeRoot(VAR154_tree, root_0)



                self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationPart3781)
                variableDeclaration155 = self.variableDeclaration()

                self._state.following.pop()
                self._adaptor.addChild(root_0, variableDeclaration155.tree)


                # ryter.g:439:32: ( SEMI ! variableDeclaration )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == SEMI) :
                        LA30_1 = self.input.LA(2)

                        if (LA30_1 == IDENT) :
                            alt30 = 1




                    if alt30 == 1:
                        # ryter.g:439:34: SEMI ! variableDeclaration
                        pass 
                        SEMI156 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_variableDeclarationPart3785)

                        self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationPart3788)
                        variableDeclaration157 = self.variableDeclaration()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, variableDeclaration157.tree)



                    else:
                        break #loop30


                SEMI158 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_variableDeclarationPart3793)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "variableDeclarationPart"


    class variableDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.variableDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "variableDeclaration"
    # ryter.g:442:1: variableDeclaration : identifierList c= COLON ^ type ;
    def variableDeclaration(self, ):
        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)


        root_0 = None

        c = None
        identifierList159 = None
        type160 = None

        c_tree = None

        try:
            try:
                # ryter.g:443:5: ( identifierList c= COLON ^ type )
                # ryter.g:443:7: identifierList c= COLON ^ type
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_identifierList_in_variableDeclaration3811)
                identifierList159 = self.identifierList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifierList159.tree)


                c = self.match(self.input, COLON, self.FOLLOW_COLON_in_variableDeclaration3815)
                c_tree = self._adaptor.createWithPayload(c)
                root_0 = self._adaptor.becomeRoot(c_tree, root_0)



                #action start
                c.setType(VARDECL);
                #action end


                self._state.following.append(self.FOLLOW_type_in_variableDeclaration3820)
                type160 = self.type()

                self._state.following.pop()
                self._adaptor.addChild(root_0, type160.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "variableDeclaration"


    class procedureAndFunctionDeclarationPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.procedureAndFunctionDeclarationPart_return, self).__init__()

            self.tree = None





    # $ANTLR start "procedureAndFunctionDeclarationPart"
    # ryter.g:446:1: procedureAndFunctionDeclarationPart : procedureOrFunctionDeclaration SEMI !;
    def procedureAndFunctionDeclarationPart(self, ):
        retval = self.procedureAndFunctionDeclarationPart_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMI162 = None
        procedureOrFunctionDeclaration161 = None

        SEMI162_tree = None

        try:
            try:
                # ryter.g:447:5: ( procedureOrFunctionDeclaration SEMI !)
                # ryter.g:447:7: procedureOrFunctionDeclaration SEMI !
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_procedureOrFunctionDeclaration_in_procedureAndFunctionDeclarationPart3837)
                procedureOrFunctionDeclaration161 = self.procedureOrFunctionDeclaration()

                self._state.following.pop()
                self._adaptor.addChild(root_0, procedureOrFunctionDeclaration161.tree)


                SEMI162 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_procedureAndFunctionDeclarationPart3839)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "procedureAndFunctionDeclarationPart"


    class procedureOrFunctionDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.procedureOrFunctionDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "procedureOrFunctionDeclaration"
    # ryter.g:450:1: procedureOrFunctionDeclaration : ( procedureDeclaration | functionDeclaration );
    def procedureOrFunctionDeclaration(self, ):
        retval = self.procedureOrFunctionDeclaration_return()
        retval.start = self.input.LT(1)


        root_0 = None

        procedureDeclaration163 = None
        functionDeclaration164 = None


        try:
            try:
                # ryter.g:451:5: ( procedureDeclaration | functionDeclaration )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == PROCEDURE) :
                    alt31 = 1
                elif (LA31_0 == FUNCTION) :
                    alt31 = 2
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # ryter.g:451:7: procedureDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_procedureDeclaration_in_procedureOrFunctionDeclaration3857)
                    procedureDeclaration163 = self.procedureDeclaration()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, procedureDeclaration163.tree)



                elif alt31 == 2:
                    # ryter.g:452:7: functionDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_functionDeclaration_in_procedureOrFunctionDeclaration3865)
                    functionDeclaration164 = self.functionDeclaration()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, functionDeclaration164.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "procedureOrFunctionDeclaration"


    class procedureDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.procedureDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "procedureDeclaration"
    # ryter.g:455:1: procedureDeclaration : PROCEDURE ^ identifier ( formalParameterList )? SEMI ! ( block | directive ) ;
    def procedureDeclaration(self, ):
        retval = self.procedureDeclaration_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROCEDURE165 = None
        SEMI168 = None
        identifier166 = None
        formalParameterList167 = None
        block169 = None
        directive170 = None

        PROCEDURE165_tree = None
        SEMI168_tree = None

        try:
            try:
                # ryter.g:456:5: ( PROCEDURE ^ identifier ( formalParameterList )? SEMI ! ( block | directive ) )
                # ryter.g:456:7: PROCEDURE ^ identifier ( formalParameterList )? SEMI ! ( block | directive )
                pass 
                root_0 = self._adaptor.nil()


                PROCEDURE165 = self.match(self.input, PROCEDURE, self.FOLLOW_PROCEDURE_in_procedureDeclaration3882)
                PROCEDURE165_tree = self._adaptor.createWithPayload(PROCEDURE165)
                root_0 = self._adaptor.becomeRoot(PROCEDURE165_tree, root_0)



                self._state.following.append(self.FOLLOW_identifier_in_procedureDeclaration3885)
                identifier166 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier166.tree)


                # ryter.g:456:29: ( formalParameterList )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == LPAREN) :
                    alt32 = 1
                if alt32 == 1:
                    # ryter.g:456:30: formalParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterList_in_procedureDeclaration3888)
                    formalParameterList167 = self.formalParameterList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, formalParameterList167.tree)





                SEMI168 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_procedureDeclaration3892)

                # ryter.g:457:7: ( block | directive )
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == BEGIN or LA33_0 == CONST or LA33_0 == FUNCTION or LA33_0 == IMPLEMENTATION or LA33_0 == LABEL or LA33_0 == PROCEDURE or LA33_0 == TYPE or (USES <= LA33_0 <= VAR)) :
                    alt33 = 1
                elif (LA33_0 == FORWARD) :
                    alt33 = 2
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae


                if alt33 == 1:
                    # ryter.g:457:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_procedureDeclaration3903)
                    block169 = self.block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, block169.tree)



                elif alt33 == 2:
                    # ryter.g:457:17: directive
                    pass 
                    self._state.following.append(self.FOLLOW_directive_in_procedureDeclaration3907)
                    directive170 = self.directive()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, directive170.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "procedureDeclaration"


    class functionDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.functionDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "functionDeclaration"
    # ryter.g:464:1: functionDeclaration : FUNCTION ^ identifier ( formalParameterList )? COLON ! resultType SEMI ! ( block | directive ) ;
    def functionDeclaration(self, ):
        retval = self.functionDeclaration_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FUNCTION171 = None
        COLON174 = None
        SEMI176 = None
        identifier172 = None
        formalParameterList173 = None
        resultType175 = None
        block177 = None
        directive178 = None

        FUNCTION171_tree = None
        COLON174_tree = None
        SEMI176_tree = None

        try:
            try:
                # ryter.g:465:5: ( FUNCTION ^ identifier ( formalParameterList )? COLON ! resultType SEMI ! ( block | directive ) )
                # ryter.g:465:7: FUNCTION ^ identifier ( formalParameterList )? COLON ! resultType SEMI ! ( block | directive )
                pass 
                root_0 = self._adaptor.nil()


                FUNCTION171 = self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_functionDeclaration3930)
                FUNCTION171_tree = self._adaptor.createWithPayload(FUNCTION171)
                root_0 = self._adaptor.becomeRoot(FUNCTION171_tree, root_0)



                self._state.following.append(self.FOLLOW_identifier_in_functionDeclaration3933)
                identifier172 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier172.tree)


                # ryter.g:465:28: ( formalParameterList )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == LPAREN) :
                    alt34 = 1
                if alt34 == 1:
                    # ryter.g:465:29: formalParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration3936)
                    formalParameterList173 = self.formalParameterList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, formalParameterList173.tree)





                COLON174 = self.match(self.input, COLON, self.FOLLOW_COLON_in_functionDeclaration3940)

                self._state.following.append(self.FOLLOW_resultType_in_functionDeclaration3943)
                resultType175 = self.resultType()

                self._state.following.pop()
                self._adaptor.addChild(root_0, resultType175.tree)


                SEMI176 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_functionDeclaration3945)

                # ryter.g:466:7: ( block | directive )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == BEGIN or LA35_0 == CONST or LA35_0 == FUNCTION or LA35_0 == IMPLEMENTATION or LA35_0 == LABEL or LA35_0 == PROCEDURE or LA35_0 == TYPE or (USES <= LA35_0 <= VAR)) :
                    alt35 = 1
                elif (LA35_0 == FORWARD) :
                    alt35 = 2
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # ryter.g:466:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_functionDeclaration3956)
                    block177 = self.block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, block177.tree)



                elif alt35 == 2:
                    # ryter.g:466:17: directive
                    pass 
                    self._state.following.append(self.FOLLOW_directive_in_functionDeclaration3960)
                    directive178 = self.directive()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, directive178.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "functionDeclaration"


    class directive_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.directive_return, self).__init__()

            self.tree = None





    # $ANTLR start "directive"
    # ryter.g:469:1: directive : FORWARD ;
    def directive(self, ):
        retval = self.directive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FORWARD179 = None

        FORWARD179_tree = None

        try:
            try:
                # ryter.g:470:5: ( FORWARD )
                # ryter.g:470:7: FORWARD
                pass 
                root_0 = self._adaptor.nil()


                FORWARD179 = self.match(self.input, FORWARD, self.FOLLOW_FORWARD_in_directive3979)
                FORWARD179_tree = self._adaptor.createWithPayload(FORWARD179)
                self._adaptor.addChild(root_0, FORWARD179_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "directive"


    class formalParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.formalParameterList_return, self).__init__()

            self.tree = None





    # $ANTLR start "formalParameterList"
    # ryter.g:474:1: formalParameterList : LPAREN formalParameterSection ( SEMI formalParameterSection )* RPAREN -> ^( ARGDECLS ( formalParameterSection )+ ) ;
    def formalParameterList(self, ):
        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LPAREN180 = None
        SEMI182 = None
        RPAREN184 = None
        formalParameterSection181 = None
        formalParameterSection183 = None

        LPAREN180_tree = None
        SEMI182_tree = None
        RPAREN184_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_formalParameterSection = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterSection")
        try:
            try:
                # ryter.g:475:5: ( LPAREN formalParameterSection ( SEMI formalParameterSection )* RPAREN -> ^( ARGDECLS ( formalParameterSection )+ ) )
                # ryter.g:475:7: LPAREN formalParameterSection ( SEMI formalParameterSection )* RPAREN
                pass 
                LPAREN180 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_formalParameterList3997) 
                stream_LPAREN.add(LPAREN180)


                self._state.following.append(self.FOLLOW_formalParameterSection_in_formalParameterList3999)
                formalParameterSection181 = self.formalParameterSection()

                self._state.following.pop()
                stream_formalParameterSection.add(formalParameterSection181.tree)


                # ryter.g:475:37: ( SEMI formalParameterSection )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == SEMI) :
                        alt36 = 1


                    if alt36 == 1:
                        # ryter.g:475:39: SEMI formalParameterSection
                        pass 
                        SEMI182 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_formalParameterList4003) 
                        stream_SEMI.add(SEMI182)


                        self._state.following.append(self.FOLLOW_formalParameterSection_in_formalParameterList4005)
                        formalParameterSection183 = self.formalParameterSection()

                        self._state.following.pop()
                        stream_formalParameterSection.add(formalParameterSection183.tree)



                    else:
                        break #loop36


                RPAREN184 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_formalParameterList4010) 
                stream_RPAREN.add(RPAREN184)


                # AST Rewrite
                # elements: formalParameterSection
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 476:5: -> ^( ARGDECLS ( formalParameterSection )+ )
                # ryter.g:476:8: ^( ARGDECLS ( formalParameterSection )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARGDECLS, "ARGDECLS")
                , root_1)

                # ryter.g:476:19: ( formalParameterSection )+
                if not (stream_formalParameterSection.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_formalParameterSection.hasNext():
                    self._adaptor.addChild(root_1, stream_formalParameterSection.nextTree())


                stream_formalParameterSection.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "formalParameterList"


    class formalParameterSection_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.formalParameterSection_return, self).__init__()

            self.tree = None





    # $ANTLR start "formalParameterSection"
    # ryter.g:479:1: formalParameterSection : ( parameterGroup | VAR ^ parameterGroup | FUNCTION ^ parameterGroup | PROCEDURE ^ parameterGroup );
    def formalParameterSection(self, ):
        retval = self.formalParameterSection_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VAR186 = None
        FUNCTION188 = None
        PROCEDURE190 = None
        parameterGroup185 = None
        parameterGroup187 = None
        parameterGroup189 = None
        parameterGroup191 = None

        VAR186_tree = None
        FUNCTION188_tree = None
        PROCEDURE190_tree = None

        try:
            try:
                # ryter.g:480:5: ( parameterGroup | VAR ^ parameterGroup | FUNCTION ^ parameterGroup | PROCEDURE ^ parameterGroup )
                alt37 = 4
                LA37 = self.input.LA(1)
                if LA37 == IDENT:
                    alt37 = 1
                elif LA37 == VAR:
                    alt37 = 2
                elif LA37 == FUNCTION:
                    alt37 = 3
                elif LA37 == PROCEDURE:
                    alt37 = 4
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # ryter.g:480:7: parameterGroup
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_parameterGroup_in_formalParameterSection4040)
                    parameterGroup185 = self.parameterGroup()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parameterGroup185.tree)



                elif alt37 == 2:
                    # ryter.g:481:7: VAR ^ parameterGroup
                    pass 
                    root_0 = self._adaptor.nil()


                    VAR186 = self.match(self.input, VAR, self.FOLLOW_VAR_in_formalParameterSection4048)
                    VAR186_tree = self._adaptor.createWithPayload(VAR186)
                    root_0 = self._adaptor.becomeRoot(VAR186_tree, root_0)



                    self._state.following.append(self.FOLLOW_parameterGroup_in_formalParameterSection4051)
                    parameterGroup187 = self.parameterGroup()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parameterGroup187.tree)



                elif alt37 == 3:
                    # ryter.g:482:7: FUNCTION ^ parameterGroup
                    pass 
                    root_0 = self._adaptor.nil()


                    FUNCTION188 = self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_formalParameterSection4059)
                    FUNCTION188_tree = self._adaptor.createWithPayload(FUNCTION188)
                    root_0 = self._adaptor.becomeRoot(FUNCTION188_tree, root_0)



                    self._state.following.append(self.FOLLOW_parameterGroup_in_formalParameterSection4062)
                    parameterGroup189 = self.parameterGroup()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parameterGroup189.tree)



                elif alt37 == 4:
                    # ryter.g:483:7: PROCEDURE ^ parameterGroup
                    pass 
                    root_0 = self._adaptor.nil()


                    PROCEDURE190 = self.match(self.input, PROCEDURE, self.FOLLOW_PROCEDURE_in_formalParameterSection4070)
                    PROCEDURE190_tree = self._adaptor.createWithPayload(PROCEDURE190)
                    root_0 = self._adaptor.becomeRoot(PROCEDURE190_tree, root_0)



                    self._state.following.append(self.FOLLOW_parameterGroup_in_formalParameterSection4073)
                    parameterGroup191 = self.parameterGroup()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parameterGroup191.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "formalParameterSection"


    class parameterGroup_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.parameterGroup_return, self).__init__()

            self.tree = None





    # $ANTLR start "parameterGroup"
    # ryter.g:486:1: parameterGroup : ids= identifierList COLON t= typeIdentifier -> ^( ARGDECL identifierList typeIdentifier ) ;
    def parameterGroup(self, ):
        retval = self.parameterGroup_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COLON192 = None
        ids = None
        t = None

        COLON192_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_typeIdentifier = RewriteRuleSubtreeStream(self._adaptor, "rule typeIdentifier")
        stream_identifierList = RewriteRuleSubtreeStream(self._adaptor, "rule identifierList")
        try:
            try:
                # ryter.g:487:5: (ids= identifierList COLON t= typeIdentifier -> ^( ARGDECL identifierList typeIdentifier ) )
                # ryter.g:487:7: ids= identifierList COLON t= typeIdentifier
                pass 
                self._state.following.append(self.FOLLOW_identifierList_in_parameterGroup4092)
                ids = self.identifierList()

                self._state.following.pop()
                stream_identifierList.add(ids.tree)


                COLON192 = self.match(self.input, COLON, self.FOLLOW_COLON_in_parameterGroup4094) 
                stream_COLON.add(COLON192)


                self._state.following.append(self.FOLLOW_typeIdentifier_in_parameterGroup4098)
                t = self.typeIdentifier()

                self._state.following.pop()
                stream_typeIdentifier.add(t.tree)


                # AST Rewrite
                # elements: typeIdentifier, identifierList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 488:5: -> ^( ARGDECL identifierList typeIdentifier )
                # ryter.g:488:8: ^( ARGDECL identifierList typeIdentifier )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARGDECL, "ARGDECL")
                , root_1)

                self._adaptor.addChild(root_1, stream_identifierList.nextTree())

                self._adaptor.addChild(root_1, stream_typeIdentifier.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "parameterGroup"


    class identifierList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.identifierList_return, self).__init__()

            self.tree = None





    # $ANTLR start "identifierList"
    # ryter.g:491:1: identifierList : identifier ( COMMA identifier )* -> ^( IDLIST ( identifier )+ ) ;
    def identifierList(self, ):
        retval = self.identifierList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA194 = None
        identifier193 = None
        identifier195 = None

        COMMA194_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # ryter.g:492:5: ( identifier ( COMMA identifier )* -> ^( IDLIST ( identifier )+ ) )
                # ryter.g:492:7: identifier ( COMMA identifier )*
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_identifierList4129)
                identifier193 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier193.tree)


                # ryter.g:492:18: ( COMMA identifier )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == COMMA) :
                        alt38 = 1


                    if alt38 == 1:
                        # ryter.g:492:20: COMMA identifier
                        pass 
                        COMMA194 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_identifierList4133) 
                        stream_COMMA.add(COMMA194)


                        self._state.following.append(self.FOLLOW_identifier_in_identifierList4135)
                        identifier195 = self.identifier()

                        self._state.following.pop()
                        stream_identifier.add(identifier195.tree)



                    else:
                        break #loop38


                # AST Rewrite
                # elements: identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 493:5: -> ^( IDLIST ( identifier )+ )
                # ryter.g:493:7: ^( IDLIST ( identifier )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(IDLIST, "IDLIST")
                , root_1)

                # ryter.g:493:16: ( identifier )+
                if not (stream_identifier.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_identifier.hasNext():
                    self._adaptor.addChild(root_1, stream_identifier.nextTree())


                stream_identifier.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "identifierList"


    class constList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.constList_return, self).__init__()

            self.tree = None





    # $ANTLR start "constList"
    # ryter.g:496:1: constList : constant ( COMMA constant )* -> ^( CONSTLIST ( constant )+ ) ;
    def constList(self, ):
        retval = self.constList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA197 = None
        constant196 = None
        constant198 = None

        COMMA197_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_constant = RewriteRuleSubtreeStream(self._adaptor, "rule constant")
        try:
            try:
                # ryter.g:497:5: ( constant ( COMMA constant )* -> ^( CONSTLIST ( constant )+ ) )
                # ryter.g:497:7: constant ( COMMA constant )*
                pass 
                self._state.following.append(self.FOLLOW_constant_in_constList4167)
                constant196 = self.constant()

                self._state.following.pop()
                stream_constant.add(constant196.tree)


                # ryter.g:497:16: ( COMMA constant )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == COMMA) :
                        alt39 = 1


                    if alt39 == 1:
                        # ryter.g:497:18: COMMA constant
                        pass 
                        COMMA197 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_constList4171) 
                        stream_COMMA.add(COMMA197)


                        self._state.following.append(self.FOLLOW_constant_in_constList4173)
                        constant198 = self.constant()

                        self._state.following.pop()
                        stream_constant.add(constant198.tree)



                    else:
                        break #loop39


                # AST Rewrite
                # elements: constant
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 498:5: -> ^( CONSTLIST ( constant )+ )
                # ryter.g:498:7: ^( CONSTLIST ( constant )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CONSTLIST, "CONSTLIST")
                , root_1)

                # ryter.g:498:19: ( constant )+
                if not (stream_constant.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_constant.hasNext():
                    self._adaptor.addChild(root_1, stream_constant.nextTree())


                stream_constant.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "constList"


    class resultType_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.resultType_return, self).__init__()

            self.tree = None





    # $ANTLR start "resultType"
    # ryter.g:501:1: resultType : typeIdentifier ;
    def resultType(self, ):
        retval = self.resultType_return()
        retval.start = self.input.LT(1)


        root_0 = None

        typeIdentifier199 = None


        try:
            try:
                # ryter.g:502:5: ( typeIdentifier )
                # ryter.g:502:7: typeIdentifier
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_typeIdentifier_in_resultType4205)
                typeIdentifier199 = self.typeIdentifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, typeIdentifier199.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "resultType"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.statement_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement"
    # ryter.g:505:1: statement : ( label COLON ^ unlabelledStatement | unlabelledStatement );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COLON201 = None
        label200 = None
        unlabelledStatement202 = None
        unlabelledStatement203 = None

        COLON201_tree = None

        try:
            try:
                # ryter.g:506:5: ( label COLON ^ unlabelledStatement | unlabelledStatement )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == NUM_INT) :
                    alt40 = 1
                elif ((AT <= LA40_0 <= BEGIN) or LA40_0 == CASE or (ELSE <= LA40_0 <= END) or LA40_0 == EXIT or LA40_0 == FOR or LA40_0 == GOTO or LA40_0 == IDENT or LA40_0 == IF or LA40_0 == REPEAT or LA40_0 == SEMI or LA40_0 == UNTIL or (WHILE <= LA40_0 <= WITH)) :
                    alt40 = 2
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae


                if alt40 == 1:
                    # ryter.g:506:7: label COLON ^ unlabelledStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_label_in_statement4222)
                    label200 = self.label()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, label200.tree)


                    COLON201 = self.match(self.input, COLON, self.FOLLOW_COLON_in_statement4224)
                    COLON201_tree = self._adaptor.createWithPayload(COLON201)
                    root_0 = self._adaptor.becomeRoot(COLON201_tree, root_0)



                    self._state.following.append(self.FOLLOW_unlabelledStatement_in_statement4227)
                    unlabelledStatement202 = self.unlabelledStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unlabelledStatement202.tree)



                elif alt40 == 2:
                    # ryter.g:507:7: unlabelledStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unlabelledStatement_in_statement4235)
                    unlabelledStatement203 = self.unlabelledStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unlabelledStatement203.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "statement"


    class unlabelledStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.unlabelledStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "unlabelledStatement"
    # ryter.g:510:1: unlabelledStatement : ( simpleStatement | structuredStatement );
    def unlabelledStatement(self, ):
        retval = self.unlabelledStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        simpleStatement204 = None
        structuredStatement205 = None


        try:
            try:
                # ryter.g:511:5: ( simpleStatement | structuredStatement )
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == AT or (ELSE <= LA41_0 <= END) or LA41_0 == EXIT or LA41_0 == GOTO or LA41_0 == IDENT or LA41_0 == SEMI or LA41_0 == UNTIL) :
                    alt41 = 1
                elif (LA41_0 == BEGIN or LA41_0 == CASE or LA41_0 == FOR or LA41_0 == IF or LA41_0 == REPEAT or (WHILE <= LA41_0 <= WITH)) :
                    alt41 = 2
                else:
                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae


                if alt41 == 1:
                    # ryter.g:511:7: simpleStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_simpleStatement_in_unlabelledStatement4252)
                    simpleStatement204 = self.simpleStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, simpleStatement204.tree)



                elif alt41 == 2:
                    # ryter.g:512:7: structuredStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_structuredStatement_in_unlabelledStatement4260)
                    structuredStatement205 = self.structuredStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, structuredStatement205.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unlabelledStatement"


    class exitStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.exitStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "exitStatement"
    # ryter.g:515:1: exitStatement : EXIT ^;
    def exitStatement(self, ):
        retval = self.exitStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EXIT206 = None

        EXIT206_tree = None

        try:
            try:
                # ryter.g:516:5: ( EXIT ^)
                # ryter.g:516:7: EXIT ^
                pass 
                root_0 = self._adaptor.nil()


                EXIT206 = self.match(self.input, EXIT, self.FOLLOW_EXIT_in_exitStatement4277)
                EXIT206_tree = self._adaptor.createWithPayload(EXIT206)
                root_0 = self._adaptor.becomeRoot(EXIT206_tree, root_0)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "exitStatement"


    class simpleStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.simpleStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "simpleStatement"
    # ryter.g:520:1: simpleStatement : ( assignmentStatement | procedureStatement | exitStatement | gotoStatement | emptyStatement );
    def simpleStatement(self, ):
        retval = self.simpleStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        assignmentStatement207 = None
        procedureStatement208 = None
        exitStatement209 = None
        gotoStatement210 = None
        emptyStatement211 = None


        try:
            try:
                # ryter.g:521:5: ( assignmentStatement | procedureStatement | exitStatement | gotoStatement | emptyStatement )
                alt42 = 5
                LA42 = self.input.LA(1)
                if LA42 == AT:
                    alt42 = 1
                elif LA42 == IDENT:
                    LA42_2 = self.input.LA(2)

                    if (LA42_2 == ASSIGN or LA42_2 == DOT or (LBRACK <= LA42_2 <= LBRACK2) or LA42_2 == POINTER) :
                        alt42 = 1
                    elif ((ELSE <= LA42_2 <= END) or LA42_2 == LPAREN or LA42_2 == SEMI or LA42_2 == UNTIL) :
                        alt42 = 2
                    else:
                        nvae = NoViableAltException("", 42, 2, self.input)

                        raise nvae


                elif LA42 == EXIT:
                    alt42 = 3
                elif LA42 == GOTO:
                    alt42 = 4
                elif LA42 == ELSE or LA42 == END or LA42 == SEMI or LA42 == UNTIL:
                    alt42 = 5
                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae


                if alt42 == 1:
                    # ryter.g:521:7: assignmentStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_assignmentStatement_in_simpleStatement4297)
                    assignmentStatement207 = self.assignmentStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignmentStatement207.tree)



                elif alt42 == 2:
                    # ryter.g:522:7: procedureStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_procedureStatement_in_simpleStatement4305)
                    procedureStatement208 = self.procedureStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, procedureStatement208.tree)



                elif alt42 == 3:
                    # ryter.g:523:7: exitStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_exitStatement_in_simpleStatement4313)
                    exitStatement209 = self.exitStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, exitStatement209.tree)



                elif alt42 == 4:
                    # ryter.g:524:7: gotoStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_gotoStatement_in_simpleStatement4321)
                    gotoStatement210 = self.gotoStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, gotoStatement210.tree)



                elif alt42 == 5:
                    # ryter.g:525:7: emptyStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_emptyStatement_in_simpleStatement4329)
                    emptyStatement211 = self.emptyStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, emptyStatement211.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "simpleStatement"


    class assignmentStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.assignmentStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "assignmentStatement"
    # ryter.g:528:1: assignmentStatement : variable ASSIGN ^ expression ;
    def assignmentStatement(self, ):
        retval = self.assignmentStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ASSIGN213 = None
        variable212 = None
        expression214 = None

        ASSIGN213_tree = None

        try:
            try:
                # ryter.g:529:5: ( variable ASSIGN ^ expression )
                # ryter.g:529:7: variable ASSIGN ^ expression
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_variable_in_assignmentStatement4346)
                variable212 = self.variable()

                self._state.following.pop()
                self._adaptor.addChild(root_0, variable212.tree)


                ASSIGN213 = self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignmentStatement4348)
                ASSIGN213_tree = self._adaptor.createWithPayload(ASSIGN213)
                root_0 = self._adaptor.becomeRoot(ASSIGN213_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_assignmentStatement4351)
                expression214 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression214.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assignmentStatement"


    class variable_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.variable_return, self).__init__()

            self.tree = None





    # $ANTLR start "variable"
    # ryter.g:532:1: variable : ( AT ^ identifier | identifier ) ( LBRACK ^ expression ( COMMA ! expression )* RBRACK !| LBRACK2 ^ expression ( COMMA ! expression )* RBRACK2 !| DOT ^ identifier | POINTER ^)* ;
    def variable(self, ):
        retval = self.variable_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AT215 = None
        LBRACK218 = None
        COMMA220 = None
        RBRACK222 = None
        LBRACK2223 = None
        COMMA225 = None
        RBRACK2227 = None
        DOT228 = None
        POINTER230 = None
        identifier216 = None
        identifier217 = None
        expression219 = None
        expression221 = None
        expression224 = None
        expression226 = None
        identifier229 = None

        AT215_tree = None
        LBRACK218_tree = None
        COMMA220_tree = None
        RBRACK222_tree = None
        LBRACK2223_tree = None
        COMMA225_tree = None
        RBRACK2227_tree = None
        DOT228_tree = None
        POINTER230_tree = None

        try:
            try:
                # ryter.g:533:5: ( ( AT ^ identifier | identifier ) ( LBRACK ^ expression ( COMMA ! expression )* RBRACK !| LBRACK2 ^ expression ( COMMA ! expression )* RBRACK2 !| DOT ^ identifier | POINTER ^)* )
                # ryter.g:533:7: ( AT ^ identifier | identifier ) ( LBRACK ^ expression ( COMMA ! expression )* RBRACK !| LBRACK2 ^ expression ( COMMA ! expression )* RBRACK2 !| DOT ^ identifier | POINTER ^)*
                pass 
                root_0 = self._adaptor.nil()


                # ryter.g:533:7: ( AT ^ identifier | identifier )
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == AT) :
                    alt43 = 1
                elif (LA43_0 == IDENT) :
                    alt43 = 2
                else:
                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae


                if alt43 == 1:
                    # ryter.g:533:9: AT ^ identifier
                    pass 
                    AT215 = self.match(self.input, AT, self.FOLLOW_AT_in_variable4370)
                    AT215_tree = self._adaptor.createWithPayload(AT215)
                    root_0 = self._adaptor.becomeRoot(AT215_tree, root_0)



                    self._state.following.append(self.FOLLOW_identifier_in_variable4373)
                    identifier216 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier216.tree)



                elif alt43 == 2:
                    # ryter.g:534:9: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_variable4384)
                    identifier217 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier217.tree)





                # ryter.g:536:7: ( LBRACK ^ expression ( COMMA ! expression )* RBRACK !| LBRACK2 ^ expression ( COMMA ! expression )* RBRACK2 !| DOT ^ identifier | POINTER ^)*
                while True: #loop46
                    alt46 = 5
                    LA46 = self.input.LA(1)
                    if LA46 == LBRACK:
                        alt46 = 1
                    elif LA46 == LBRACK2:
                        alt46 = 2
                    elif LA46 == DOT:
                        alt46 = 3
                    elif LA46 == POINTER:
                        alt46 = 4

                    if alt46 == 1:
                        # ryter.g:536:10: LBRACK ^ expression ( COMMA ! expression )* RBRACK !
                        pass 
                        LBRACK218 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_variable4403)
                        LBRACK218_tree = self._adaptor.createWithPayload(LBRACK218)
                        root_0 = self._adaptor.becomeRoot(LBRACK218_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_variable4406)
                        expression219 = self.expression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expression219.tree)


                        # ryter.g:536:29: ( COMMA ! expression )*
                        while True: #loop44
                            alt44 = 2
                            LA44_0 = self.input.LA(1)

                            if (LA44_0 == COMMA) :
                                alt44 = 1


                            if alt44 == 1:
                                # ryter.g:536:31: COMMA ! expression
                                pass 
                                COMMA220 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_variable4410)

                                self._state.following.append(self.FOLLOW_expression_in_variable4413)
                                expression221 = self.expression()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, expression221.tree)



                            else:
                                break #loop44


                        RBRACK222 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_variable4417)


                    elif alt46 == 2:
                        # ryter.g:537:9: LBRACK2 ^ expression ( COMMA ! expression )* RBRACK2 !
                        pass 
                        LBRACK2223 = self.match(self.input, LBRACK2, self.FOLLOW_LBRACK2_in_variable4428)
                        LBRACK2223_tree = self._adaptor.createWithPayload(LBRACK2223)
                        root_0 = self._adaptor.becomeRoot(LBRACK2223_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_variable4431)
                        expression224 = self.expression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expression224.tree)


                        # ryter.g:537:29: ( COMMA ! expression )*
                        while True: #loop45
                            alt45 = 2
                            LA45_0 = self.input.LA(1)

                            if (LA45_0 == COMMA) :
                                alt45 = 1


                            if alt45 == 1:
                                # ryter.g:537:31: COMMA ! expression
                                pass 
                                COMMA225 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_variable4435)

                                self._state.following.append(self.FOLLOW_expression_in_variable4438)
                                expression226 = self.expression()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, expression226.tree)



                            else:
                                break #loop45


                        RBRACK2227 = self.match(self.input, RBRACK2, self.FOLLOW_RBRACK2_in_variable4442)


                    elif alt46 == 3:
                        # ryter.g:538:9: DOT ^ identifier
                        pass 
                        DOT228 = self.match(self.input, DOT, self.FOLLOW_DOT_in_variable4453)
                        DOT228_tree = self._adaptor.createWithPayload(DOT228)
                        root_0 = self._adaptor.becomeRoot(DOT228_tree, root_0)



                        self._state.following.append(self.FOLLOW_identifier_in_variable4456)
                        identifier229 = self.identifier()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, identifier229.tree)



                    elif alt46 == 4:
                        # ryter.g:539:9: POINTER ^
                        pass 
                        POINTER230 = self.match(self.input, POINTER, self.FOLLOW_POINTER_in_variable4466)
                        POINTER230_tree = self._adaptor.createWithPayload(POINTER230)
                        root_0 = self._adaptor.becomeRoot(POINTER230_tree, root_0)




                    else:
                        break #loop46




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "variable"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # ryter.g:543:1: expression : simpleExpression ( ( EQUAL ^| NOT_EQUAL ^| LT ^| LE ^| GE ^| GT ^| IN ^) simpleExpression )* ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUAL232 = None
        NOT_EQUAL233 = None
        LT234 = None
        LE235 = None
        GE236 = None
        GT237 = None
        IN238 = None
        simpleExpression231 = None
        simpleExpression239 = None

        EQUAL232_tree = None
        NOT_EQUAL233_tree = None
        LT234_tree = None
        LE235_tree = None
        GE236_tree = None
        GT237_tree = None
        IN238_tree = None

        try:
            try:
                # ryter.g:544:5: ( simpleExpression ( ( EQUAL ^| NOT_EQUAL ^| LT ^| LE ^| GE ^| GT ^| IN ^) simpleExpression )* )
                # ryter.g:544:7: simpleExpression ( ( EQUAL ^| NOT_EQUAL ^| LT ^| LE ^| GE ^| GT ^| IN ^) simpleExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_simpleExpression_in_expression4493)
                simpleExpression231 = self.simpleExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, simpleExpression231.tree)


                # ryter.g:545:5: ( ( EQUAL ^| NOT_EQUAL ^| LT ^| LE ^| GE ^| GT ^| IN ^) simpleExpression )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == EQUAL or LA48_0 == GE or LA48_0 == GT or LA48_0 == IN or LA48_0 == LE or LA48_0 == LT or LA48_0 == NOT_EQUAL) :
                        alt48 = 1


                    if alt48 == 1:
                        # ryter.g:545:7: ( EQUAL ^| NOT_EQUAL ^| LT ^| LE ^| GE ^| GT ^| IN ^) simpleExpression
                        pass 
                        # ryter.g:545:7: ( EQUAL ^| NOT_EQUAL ^| LT ^| LE ^| GE ^| GT ^| IN ^)
                        alt47 = 7
                        LA47 = self.input.LA(1)
                        if LA47 == EQUAL:
                            alt47 = 1
                        elif LA47 == NOT_EQUAL:
                            alt47 = 2
                        elif LA47 == LT:
                            alt47 = 3
                        elif LA47 == LE:
                            alt47 = 4
                        elif LA47 == GE:
                            alt47 = 5
                        elif LA47 == GT:
                            alt47 = 6
                        elif LA47 == IN:
                            alt47 = 7
                        else:
                            nvae = NoViableAltException("", 47, 0, self.input)

                            raise nvae


                        if alt47 == 1:
                            # ryter.g:545:8: EQUAL ^
                            pass 
                            EQUAL232 = self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_expression4502)
                            EQUAL232_tree = self._adaptor.createWithPayload(EQUAL232)
                            root_0 = self._adaptor.becomeRoot(EQUAL232_tree, root_0)




                        elif alt47 == 2:
                            # ryter.g:545:17: NOT_EQUAL ^
                            pass 
                            NOT_EQUAL233 = self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_expression4507)
                            NOT_EQUAL233_tree = self._adaptor.createWithPayload(NOT_EQUAL233)
                            root_0 = self._adaptor.becomeRoot(NOT_EQUAL233_tree, root_0)




                        elif alt47 == 3:
                            # ryter.g:545:30: LT ^
                            pass 
                            LT234 = self.match(self.input, LT, self.FOLLOW_LT_in_expression4512)
                            LT234_tree = self._adaptor.createWithPayload(LT234)
                            root_0 = self._adaptor.becomeRoot(LT234_tree, root_0)




                        elif alt47 == 4:
                            # ryter.g:545:36: LE ^
                            pass 
                            LE235 = self.match(self.input, LE, self.FOLLOW_LE_in_expression4517)
                            LE235_tree = self._adaptor.createWithPayload(LE235)
                            root_0 = self._adaptor.becomeRoot(LE235_tree, root_0)




                        elif alt47 == 5:
                            # ryter.g:545:42: GE ^
                            pass 
                            GE236 = self.match(self.input, GE, self.FOLLOW_GE_in_expression4522)
                            GE236_tree = self._adaptor.createWithPayload(GE236)
                            root_0 = self._adaptor.becomeRoot(GE236_tree, root_0)




                        elif alt47 == 6:
                            # ryter.g:545:48: GT ^
                            pass 
                            GT237 = self.match(self.input, GT, self.FOLLOW_GT_in_expression4527)
                            GT237_tree = self._adaptor.createWithPayload(GT237)
                            root_0 = self._adaptor.becomeRoot(GT237_tree, root_0)




                        elif alt47 == 7:
                            # ryter.g:545:54: IN ^
                            pass 
                            IN238 = self.match(self.input, IN, self.FOLLOW_IN_in_expression4532)
                            IN238_tree = self._adaptor.createWithPayload(IN238)
                            root_0 = self._adaptor.becomeRoot(IN238_tree, root_0)






                        self._state.following.append(self.FOLLOW_simpleExpression_in_expression4536)
                        simpleExpression239 = self.simpleExpression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, simpleExpression239.tree)



                    else:
                        break #loop48




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "expression"


    class simpleExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.simpleExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "simpleExpression"
    # ryter.g:548:1: simpleExpression : term ( ( PLUS ^| MINUS ^| OR ^) term )* ;
    def simpleExpression(self, ):
        retval = self.simpleExpression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PLUS241 = None
        MINUS242 = None
        OR243 = None
        term240 = None
        term244 = None

        PLUS241_tree = None
        MINUS242_tree = None
        OR243_tree = None

        try:
            try:
                # ryter.g:549:5: ( term ( ( PLUS ^| MINUS ^| OR ^) term )* )
                # ryter.g:549:7: term ( ( PLUS ^| MINUS ^| OR ^) term )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_term_in_simpleExpression4556)
                term240 = self.term()

                self._state.following.pop()
                self._adaptor.addChild(root_0, term240.tree)


                # ryter.g:549:12: ( ( PLUS ^| MINUS ^| OR ^) term )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == MINUS or LA50_0 == OR or LA50_0 == PLUS) :
                        alt50 = 1


                    if alt50 == 1:
                        # ryter.g:549:14: ( PLUS ^| MINUS ^| OR ^) term
                        pass 
                        # ryter.g:549:14: ( PLUS ^| MINUS ^| OR ^)
                        alt49 = 3
                        LA49 = self.input.LA(1)
                        if LA49 == PLUS:
                            alt49 = 1
                        elif LA49 == MINUS:
                            alt49 = 2
                        elif LA49 == OR:
                            alt49 = 3
                        else:
                            nvae = NoViableAltException("", 49, 0, self.input)

                            raise nvae


                        if alt49 == 1:
                            # ryter.g:549:15: PLUS ^
                            pass 
                            PLUS241 = self.match(self.input, PLUS, self.FOLLOW_PLUS_in_simpleExpression4561)
                            PLUS241_tree = self._adaptor.createWithPayload(PLUS241)
                            root_0 = self._adaptor.becomeRoot(PLUS241_tree, root_0)




                        elif alt49 == 2:
                            # ryter.g:549:23: MINUS ^
                            pass 
                            MINUS242 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_simpleExpression4566)
                            MINUS242_tree = self._adaptor.createWithPayload(MINUS242)
                            root_0 = self._adaptor.becomeRoot(MINUS242_tree, root_0)




                        elif alt49 == 3:
                            # ryter.g:549:32: OR ^
                            pass 
                            OR243 = self.match(self.input, OR, self.FOLLOW_OR_in_simpleExpression4571)
                            OR243_tree = self._adaptor.createWithPayload(OR243)
                            root_0 = self._adaptor.becomeRoot(OR243_tree, root_0)






                        self._state.following.append(self.FOLLOW_term_in_simpleExpression4575)
                        term244 = self.term()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, term244.tree)



                    else:
                        break #loop50




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "simpleExpression"


    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.term_return, self).__init__()

            self.tree = None





    # $ANTLR start "term"
    # ryter.g:552:1: term : signedFactor ( ( STAR ^| SLASH ^| DIV ^| MOD ^| AND ^) signedFactor )* ;
    def term(self, ):
        retval = self.term_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STAR246 = None
        SLASH247 = None
        DIV248 = None
        MOD249 = None
        AND250 = None
        signedFactor245 = None
        signedFactor251 = None

        STAR246_tree = None
        SLASH247_tree = None
        DIV248_tree = None
        MOD249_tree = None
        AND250_tree = None

        try:
            try:
                # ryter.g:553:3: ( signedFactor ( ( STAR ^| SLASH ^| DIV ^| MOD ^| AND ^) signedFactor )* )
                # ryter.g:553:5: signedFactor ( ( STAR ^| SLASH ^| DIV ^| MOD ^| AND ^) signedFactor )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_signedFactor_in_term4593)
                signedFactor245 = self.signedFactor()

                self._state.following.pop()
                self._adaptor.addChild(root_0, signedFactor245.tree)


                # ryter.g:553:18: ( ( STAR ^| SLASH ^| DIV ^| MOD ^| AND ^) signedFactor )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == AND or LA52_0 == DIV or LA52_0 == MOD or (SLASH <= LA52_0 <= STAR)) :
                        alt52 = 1


                    if alt52 == 1:
                        # ryter.g:553:20: ( STAR ^| SLASH ^| DIV ^| MOD ^| AND ^) signedFactor
                        pass 
                        # ryter.g:553:20: ( STAR ^| SLASH ^| DIV ^| MOD ^| AND ^)
                        alt51 = 5
                        LA51 = self.input.LA(1)
                        if LA51 == STAR:
                            alt51 = 1
                        elif LA51 == SLASH:
                            alt51 = 2
                        elif LA51 == DIV:
                            alt51 = 3
                        elif LA51 == MOD:
                            alt51 = 4
                        elif LA51 == AND:
                            alt51 = 5
                        else:
                            nvae = NoViableAltException("", 51, 0, self.input)

                            raise nvae


                        if alt51 == 1:
                            # ryter.g:553:21: STAR ^
                            pass 
                            STAR246 = self.match(self.input, STAR, self.FOLLOW_STAR_in_term4598)
                            STAR246_tree = self._adaptor.createWithPayload(STAR246)
                            root_0 = self._adaptor.becomeRoot(STAR246_tree, root_0)




                        elif alt51 == 2:
                            # ryter.g:553:29: SLASH ^
                            pass 
                            SLASH247 = self.match(self.input, SLASH, self.FOLLOW_SLASH_in_term4603)
                            SLASH247_tree = self._adaptor.createWithPayload(SLASH247)
                            root_0 = self._adaptor.becomeRoot(SLASH247_tree, root_0)




                        elif alt51 == 3:
                            # ryter.g:553:38: DIV ^
                            pass 
                            DIV248 = self.match(self.input, DIV, self.FOLLOW_DIV_in_term4608)
                            DIV248_tree = self._adaptor.createWithPayload(DIV248)
                            root_0 = self._adaptor.becomeRoot(DIV248_tree, root_0)




                        elif alt51 == 4:
                            # ryter.g:553:45: MOD ^
                            pass 
                            MOD249 = self.match(self.input, MOD, self.FOLLOW_MOD_in_term4613)
                            MOD249_tree = self._adaptor.createWithPayload(MOD249)
                            root_0 = self._adaptor.becomeRoot(MOD249_tree, root_0)




                        elif alt51 == 5:
                            # ryter.g:553:52: AND ^
                            pass 
                            AND250 = self.match(self.input, AND, self.FOLLOW_AND_in_term4618)
                            AND250_tree = self._adaptor.createWithPayload(AND250)
                            root_0 = self._adaptor.becomeRoot(AND250_tree, root_0)






                        self._state.following.append(self.FOLLOW_signedFactor_in_term4622)
                        signedFactor251 = self.signedFactor()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, signedFactor251.tree)



                    else:
                        break #loop52




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "term"


    class signedFactor_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.signedFactor_return, self).__init__()

            self.tree = None





    # $ANTLR start "signedFactor"
    # ryter.g:556:1: signedFactor : ( PLUS ^| MINUS ^)? factor ;
    def signedFactor(self, ):
        retval = self.signedFactor_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PLUS252 = None
        MINUS253 = None
        factor254 = None

        PLUS252_tree = None
        MINUS253_tree = None

        try:
            try:
                # ryter.g:557:5: ( ( PLUS ^| MINUS ^)? factor )
                # ryter.g:557:7: ( PLUS ^| MINUS ^)? factor
                pass 
                root_0 = self._adaptor.nil()


                # ryter.g:557:7: ( PLUS ^| MINUS ^)?
                alt53 = 3
                LA53_0 = self.input.LA(1)

                if (LA53_0 == PLUS) :
                    alt53 = 1
                elif (LA53_0 == MINUS) :
                    alt53 = 2
                if alt53 == 1:
                    # ryter.g:557:8: PLUS ^
                    pass 
                    PLUS252 = self.match(self.input, PLUS, self.FOLLOW_PLUS_in_signedFactor4643)
                    PLUS252_tree = self._adaptor.createWithPayload(PLUS252)
                    root_0 = self._adaptor.becomeRoot(PLUS252_tree, root_0)




                elif alt53 == 2:
                    # ryter.g:557:14: MINUS ^
                    pass 
                    MINUS253 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_signedFactor4646)
                    MINUS253_tree = self._adaptor.createWithPayload(MINUS253)
                    root_0 = self._adaptor.becomeRoot(MINUS253_tree, root_0)






                self._state.following.append(self.FOLLOW_factor_in_signedFactor4651)
                factor254 = self.factor()

                self._state.following.pop()
                self._adaptor.addChild(root_0, factor254.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "signedFactor"


    class factor_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.factor_return, self).__init__()

            self.tree = None





    # $ANTLR start "factor"
    # ryter.g:560:1: factor : ( variable | LPAREN ! expression RPAREN !| functionDesignator | unsignedConstant | set | NOT ^ factor );
    def factor(self, ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LPAREN256 = None
        RPAREN258 = None
        NOT262 = None
        variable255 = None
        expression257 = None
        functionDesignator259 = None
        unsignedConstant260 = None
        set261 = None
        factor263 = None

        LPAREN256_tree = None
        RPAREN258_tree = None
        NOT262_tree = None

        try:
            try:
                # ryter.g:561:5: ( variable | LPAREN ! expression RPAREN !| functionDesignator | unsignedConstant | set | NOT ^ factor )
                alt54 = 6
                LA54 = self.input.LA(1)
                if LA54 == AT:
                    alt54 = 1
                elif LA54 == IDENT:
                    LA54_2 = self.input.LA(2)

                    if (LA54_2 == AND or (COLON <= LA54_2 <= COMMA) or (DIV <= LA54_2 <= DOWNTO) or (ELSE <= LA54_2 <= EQUAL) or LA54_2 == GE or LA54_2 == GT or LA54_2 == IN or (LBRACK <= LA54_2 <= LBRACK2) or LA54_2 == LE or (LT <= LA54_2 <= MOD) or LA54_2 == NOT_EQUAL or (OF <= LA54_2 <= OR) or (PLUS <= LA54_2 <= POINTER) or (RBRACK <= LA54_2 <= RBRACK2) or LA54_2 == RPAREN or LA54_2 == SEMI or (SLASH <= LA54_2 <= STAR) or (THEN <= LA54_2 <= TO) or LA54_2 == UNTIL) :
                        alt54 = 1
                    elif (LA54_2 == LPAREN) :
                        alt54 = 3
                    else:
                        nvae = NoViableAltException("", 54, 2, self.input)

                        raise nvae


                elif LA54 == LPAREN:
                    alt54 = 2
                elif LA54 == CHR or LA54 == NIL or LA54 == NUM_INT or LA54 == NUM_REAL or LA54 == STRING_LITERAL:
                    alt54 = 4
                elif LA54 == LBRACK or LA54 == LBRACK2:
                    alt54 = 5
                elif LA54 == NOT:
                    alt54 = 6
                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae


                if alt54 == 1:
                    # ryter.g:561:7: variable
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_variable_in_factor4668)
                    variable255 = self.variable()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, variable255.tree)



                elif alt54 == 2:
                    # ryter.g:562:7: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN256 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_factor4676)

                    self._state.following.append(self.FOLLOW_expression_in_factor4679)
                    expression257 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression257.tree)


                    RPAREN258 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_factor4681)


                elif alt54 == 3:
                    # ryter.g:563:7: functionDesignator
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_functionDesignator_in_factor4690)
                    functionDesignator259 = self.functionDesignator()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, functionDesignator259.tree)



                elif alt54 == 4:
                    # ryter.g:564:7: unsignedConstant
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unsignedConstant_in_factor4698)
                    unsignedConstant260 = self.unsignedConstant()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedConstant260.tree)



                elif alt54 == 5:
                    # ryter.g:565:7: set
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_in_factor4706)
                    set261 = self.set()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set261.tree)



                elif alt54 == 6:
                    # ryter.g:566:7: NOT ^ factor
                    pass 
                    root_0 = self._adaptor.nil()


                    NOT262 = self.match(self.input, NOT, self.FOLLOW_NOT_in_factor4714)
                    NOT262_tree = self._adaptor.createWithPayload(NOT262)
                    root_0 = self._adaptor.becomeRoot(NOT262_tree, root_0)



                    self._state.following.append(self.FOLLOW_factor_in_factor4717)
                    factor263 = self.factor()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, factor263.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "factor"


    class unsignedConstant_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.unsignedConstant_return, self).__init__()

            self.tree = None





    # $ANTLR start "unsignedConstant"
    # ryter.g:569:1: unsignedConstant : ( unsignedNumber | constantChr | string | NIL );
    def unsignedConstant(self, ):
        retval = self.unsignedConstant_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NIL267 = None
        unsignedNumber264 = None
        constantChr265 = None
        string266 = None

        NIL267_tree = None

        try:
            try:
                # ryter.g:570:5: ( unsignedNumber | constantChr | string | NIL )
                alt55 = 4
                LA55 = self.input.LA(1)
                if LA55 == NUM_INT or LA55 == NUM_REAL:
                    alt55 = 1
                elif LA55 == CHR:
                    alt55 = 2
                elif LA55 == STRING_LITERAL:
                    alt55 = 3
                elif LA55 == NIL:
                    alt55 = 4
                else:
                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae


                if alt55 == 1:
                    # ryter.g:570:7: unsignedNumber
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unsignedNumber_in_unsignedConstant4734)
                    unsignedNumber264 = self.unsignedNumber()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedNumber264.tree)



                elif alt55 == 2:
                    # ryter.g:571:7: constantChr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_constantChr_in_unsignedConstant4742)
                    constantChr265 = self.constantChr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constantChr265.tree)



                elif alt55 == 3:
                    # ryter.g:572:7: string
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_string_in_unsignedConstant4759)
                    string266 = self.string()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, string266.tree)



                elif alt55 == 4:
                    # ryter.g:573:7: NIL
                    pass 
                    root_0 = self._adaptor.nil()


                    NIL267 = self.match(self.input, NIL, self.FOLLOW_NIL_in_unsignedConstant4767)
                    NIL267_tree = self._adaptor.createWithPayload(NIL267)
                    self._adaptor.addChild(root_0, NIL267_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unsignedConstant"


    class functionDesignator_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.functionDesignator_return, self).__init__()

            self.tree = None





    # $ANTLR start "functionDesignator"
    # ryter.g:576:1: functionDesignator : id= identifier LPAREN args= parameterList RPAREN -> ^( FUNC_CALL $id $args) ;
    def functionDesignator(self, ):
        retval = self.functionDesignator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LPAREN268 = None
        RPAREN269 = None
        id = None
        args = None

        LPAREN268_tree = None
        RPAREN269_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_parameterList = RewriteRuleSubtreeStream(self._adaptor, "rule parameterList")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # ryter.g:577:5: (id= identifier LPAREN args= parameterList RPAREN -> ^( FUNC_CALL $id $args) )
                # ryter.g:577:7: id= identifier LPAREN args= parameterList RPAREN
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_functionDesignator4786)
                id = self.identifier()

                self._state.following.pop()
                stream_identifier.add(id.tree)


                LPAREN268 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_functionDesignator4788) 
                stream_LPAREN.add(LPAREN268)


                self._state.following.append(self.FOLLOW_parameterList_in_functionDesignator4792)
                args = self.parameterList()

                self._state.following.pop()
                stream_parameterList.add(args.tree)


                RPAREN269 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_functionDesignator4794) 
                stream_RPAREN.add(RPAREN269)


                # AST Rewrite
                # elements: args, id
                # token labels: 
                # rule labels: id, retval, args
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if id is not None:
                    stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id", id.tree)
                else:
                    stream_id = RewriteRuleSubtreeStream(self._adaptor, "token id", None)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                if args is not None:
                    stream_args = RewriteRuleSubtreeStream(self._adaptor, "rule args", args.tree)
                else:
                    stream_args = RewriteRuleSubtreeStream(self._adaptor, "token args", None)


                root_0 = self._adaptor.nil()
                # 578:5: -> ^( FUNC_CALL $id $args)
                # ryter.g:578:8: ^( FUNC_CALL $id $args)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(FUNC_CALL, "FUNC_CALL")
                , root_1)

                self._adaptor.addChild(root_1, stream_id.nextTree())

                self._adaptor.addChild(root_1, stream_args.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "functionDesignator"


    class parameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.parameterList_return, self).__init__()

            self.tree = None





    # $ANTLR start "parameterList"
    # ryter.g:581:1: parameterList : actualParameter ( COMMA actualParameter )* -> ^( ARGLIST ( actualParameter )+ ) ;
    def parameterList(self, ):
        retval = self.parameterList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA271 = None
        actualParameter270 = None
        actualParameter272 = None

        COMMA271_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_actualParameter = RewriteRuleSubtreeStream(self._adaptor, "rule actualParameter")
        try:
            try:
                # ryter.g:582:5: ( actualParameter ( COMMA actualParameter )* -> ^( ARGLIST ( actualParameter )+ ) )
                # ryter.g:582:7: actualParameter ( COMMA actualParameter )*
                pass 
                self._state.following.append(self.FOLLOW_actualParameter_in_parameterList4828)
                actualParameter270 = self.actualParameter()

                self._state.following.pop()
                stream_actualParameter.add(actualParameter270.tree)


                # ryter.g:582:23: ( COMMA actualParameter )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == COMMA) :
                        alt56 = 1


                    if alt56 == 1:
                        # ryter.g:582:25: COMMA actualParameter
                        pass 
                        COMMA271 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_parameterList4832) 
                        stream_COMMA.add(COMMA271)


                        self._state.following.append(self.FOLLOW_actualParameter_in_parameterList4834)
                        actualParameter272 = self.actualParameter()

                        self._state.following.pop()
                        stream_actualParameter.add(actualParameter272.tree)



                    else:
                        break #loop56


                # AST Rewrite
                # elements: actualParameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 583:5: -> ^( ARGLIST ( actualParameter )+ )
                # ryter.g:583:8: ^( ARGLIST ( actualParameter )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARGLIST, "ARGLIST")
                , root_1)

                # ryter.g:583:18: ( actualParameter )+
                if not (stream_actualParameter.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_actualParameter.hasNext():
                    self._adaptor.addChild(root_1, stream_actualParameter.nextTree())


                stream_actualParameter.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "parameterList"


    class set_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.set_return, self).__init__()

            self.tree = None





    # $ANTLR start "set"
    # ryter.g:586:1: set : ( LBRACK elementList RBRACK -> ^( SET ( elementList )? ) | LBRACK2 elementList RBRACK2 -> ^( SET ( elementList )? ) );
    def set(self, ):
        retval = self.set_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LBRACK273 = None
        RBRACK275 = None
        LBRACK2276 = None
        RBRACK2278 = None
        elementList274 = None
        elementList277 = None

        LBRACK273_tree = None
        RBRACK275_tree = None
        LBRACK2276_tree = None
        RBRACK2278_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")
        stream_RBRACK2 = RewriteRuleTokenStream(self._adaptor, "token RBRACK2")
        stream_LBRACK2 = RewriteRuleTokenStream(self._adaptor, "token LBRACK2")
        stream_elementList = RewriteRuleSubtreeStream(self._adaptor, "rule elementList")
        try:
            try:
                # ryter.g:587:5: ( LBRACK elementList RBRACK -> ^( SET ( elementList )? ) | LBRACK2 elementList RBRACK2 -> ^( SET ( elementList )? ) )
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == LBRACK) :
                    alt57 = 1
                elif (LA57_0 == LBRACK2) :
                    alt57 = 2
                else:
                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae


                if alt57 == 1:
                    # ryter.g:587:7: LBRACK elementList RBRACK
                    pass 
                    LBRACK273 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_set4867) 
                    stream_LBRACK.add(LBRACK273)


                    self._state.following.append(self.FOLLOW_elementList_in_set4869)
                    elementList274 = self.elementList()

                    self._state.following.pop()
                    stream_elementList.add(elementList274.tree)


                    RBRACK275 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_set4871) 
                    stream_RBRACK.add(RBRACK275)


                    # AST Rewrite
                    # elements: elementList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 587:34: -> ^( SET ( elementList )? )
                    # ryter.g:587:37: ^( SET ( elementList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(SET, "SET")
                    , root_1)

                    # ryter.g:587:43: ( elementList )?
                    if stream_elementList.hasNext():
                        self._adaptor.addChild(root_1, stream_elementList.nextTree())


                    stream_elementList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt57 == 2:
                    # ryter.g:588:7: LBRACK2 elementList RBRACK2
                    pass 
                    LBRACK2276 = self.match(self.input, LBRACK2, self.FOLLOW_LBRACK2_in_set4890) 
                    stream_LBRACK2.add(LBRACK2276)


                    self._state.following.append(self.FOLLOW_elementList_in_set4892)
                    elementList277 = self.elementList()

                    self._state.following.pop()
                    stream_elementList.add(elementList277.tree)


                    RBRACK2278 = self.match(self.input, RBRACK2, self.FOLLOW_RBRACK2_in_set4894) 
                    stream_RBRACK2.add(RBRACK2278)


                    # AST Rewrite
                    # elements: elementList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 588:35: -> ^( SET ( elementList )? )
                    # ryter.g:588:38: ^( SET ( elementList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(SET, "SET")
                    , root_1)

                    # ryter.g:588:44: ( elementList )?
                    if stream_elementList.hasNext():
                        self._adaptor.addChild(root_1, stream_elementList.nextTree())


                    stream_elementList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set"


    class elementList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.elementList_return, self).__init__()

            self.tree = None





    # $ANTLR start "elementList"
    # ryter.g:591:1: elementList : ( element ( COMMA ! element )* |);
    def elementList(self, ):
        retval = self.elementList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA280 = None
        element279 = None
        element281 = None

        COMMA280_tree = None

        try:
            try:
                # ryter.g:592:5: ( element ( COMMA ! element )* |)
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == AT or LA59_0 == CHR or LA59_0 == IDENT or (LBRACK <= LA59_0 <= LBRACK2) or LA59_0 == LPAREN or LA59_0 == MINUS or (NIL <= LA59_0 <= NOT) or (NUM_INT <= LA59_0 <= NUM_REAL) or LA59_0 == PLUS or LA59_0 == STRING_LITERAL) :
                    alt59 = 1
                elif ((RBRACK <= LA59_0 <= RBRACK2)) :
                    alt59 = 2
                else:
                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae


                if alt59 == 1:
                    # ryter.g:592:7: element ( COMMA ! element )*
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_element_in_elementList4920)
                    element279 = self.element()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, element279.tree)


                    # ryter.g:592:15: ( COMMA ! element )*
                    while True: #loop58
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if (LA58_0 == COMMA) :
                            alt58 = 1


                        if alt58 == 1:
                            # ryter.g:592:17: COMMA ! element
                            pass 
                            COMMA280 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_elementList4924)

                            self._state.following.append(self.FOLLOW_element_in_elementList4927)
                            element281 = self.element()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, element281.tree)



                        else:
                            break #loop58



                elif alt59 == 2:
                    # ryter.g:594:5: 
                    pass 
                    root_0 = self._adaptor.nil()



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "elementList"


    class element_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.element_return, self).__init__()

            self.tree = None





    # $ANTLR start "element"
    # ryter.g:596:1: element : expression ( DOTDOT ^ expression )? ;
    def element(self, ):
        retval = self.element_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DOTDOT283 = None
        expression282 = None
        expression284 = None

        DOTDOT283_tree = None

        try:
            try:
                # ryter.g:597:5: ( expression ( DOTDOT ^ expression )? )
                # ryter.g:597:7: expression ( DOTDOT ^ expression )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expression_in_element4953)
                expression282 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression282.tree)


                # ryter.g:597:18: ( DOTDOT ^ expression )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == DOTDOT) :
                    alt60 = 1
                if alt60 == 1:
                    # ryter.g:597:20: DOTDOT ^ expression
                    pass 
                    DOTDOT283 = self.match(self.input, DOTDOT, self.FOLLOW_DOTDOT_in_element4957)
                    DOTDOT283_tree = self._adaptor.createWithPayload(DOTDOT283)
                    root_0 = self._adaptor.becomeRoot(DOTDOT283_tree, root_0)



                    self._state.following.append(self.FOLLOW_expression_in_element4960)
                    expression284 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression284.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "element"


    class procedureStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.procedureStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "procedureStatement"
    # ryter.g:600:1: procedureStatement : id= identifier ( LPAREN args= parameterList RPAREN )? -> ^( PROC_CALL identifier ( parameterList )? ) ;
    def procedureStatement(self, ):
        retval = self.procedureStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LPAREN285 = None
        RPAREN286 = None
        id = None
        args = None

        LPAREN285_tree = None
        RPAREN286_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_parameterList = RewriteRuleSubtreeStream(self._adaptor, "rule parameterList")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # ryter.g:601:5: (id= identifier ( LPAREN args= parameterList RPAREN )? -> ^( PROC_CALL identifier ( parameterList )? ) )
                # ryter.g:601:7: id= identifier ( LPAREN args= parameterList RPAREN )?
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_procedureStatement4982)
                id = self.identifier()

                self._state.following.pop()
                stream_identifier.add(id.tree)


                # ryter.g:601:21: ( LPAREN args= parameterList RPAREN )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == LPAREN) :
                    alt61 = 1
                if alt61 == 1:
                    # ryter.g:601:23: LPAREN args= parameterList RPAREN
                    pass 
                    LPAREN285 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_procedureStatement4986) 
                    stream_LPAREN.add(LPAREN285)


                    self._state.following.append(self.FOLLOW_parameterList_in_procedureStatement4990)
                    args = self.parameterList()

                    self._state.following.pop()
                    stream_parameterList.add(args.tree)


                    RPAREN286 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_procedureStatement4992) 
                    stream_RPAREN.add(RPAREN286)





                # AST Rewrite
                # elements: parameterList, identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 602:5: -> ^( PROC_CALL identifier ( parameterList )? )
                # ryter.g:602:8: ^( PROC_CALL identifier ( parameterList )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROC_CALL, "PROC_CALL")
                , root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())

                # ryter.g:602:31: ( parameterList )?
                if stream_parameterList.hasNext():
                    self._adaptor.addChild(root_1, stream_parameterList.nextTree())


                stream_parameterList.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "procedureStatement"


    class actualParameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.actualParameter_return, self).__init__()

            self.tree = None





    # $ANTLR start "actualParameter"
    # ryter.g:605:1: actualParameter : expression ( COLON unsignedInteger )? ;
    def actualParameter(self, ):
        retval = self.actualParameter_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COLON288 = None
        expression287 = None
        unsignedInteger289 = None

        COLON288_tree = None

        try:
            try:
                # ryter.g:607:5: ( expression ( COLON unsignedInteger )? )
                # ryter.g:607:7: expression ( COLON unsignedInteger )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expression_in_actualParameter5032)
                expression287 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression287.tree)


                # ryter.g:607:18: ( COLON unsignedInteger )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == COLON) :
                    alt62 = 1
                if alt62 == 1:
                    # ryter.g:607:19: COLON unsignedInteger
                    pass 
                    COLON288 = self.match(self.input, COLON, self.FOLLOW_COLON_in_actualParameter5035)
                    COLON288_tree = self._adaptor.createWithPayload(COLON288)
                    self._adaptor.addChild(root_0, COLON288_tree)



                    self._state.following.append(self.FOLLOW_unsignedInteger_in_actualParameter5037)
                    unsignedInteger289 = self.unsignedInteger()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unsignedInteger289.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "actualParameter"


    class gotoStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.gotoStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "gotoStatement"
    # ryter.g:610:1: gotoStatement : GOTO ^ label ;
    def gotoStatement(self, ):
        retval = self.gotoStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        GOTO290 = None
        label291 = None

        GOTO290_tree = None

        try:
            try:
                # ryter.g:611:5: ( GOTO ^ label )
                # ryter.g:611:7: GOTO ^ label
                pass 
                root_0 = self._adaptor.nil()


                GOTO290 = self.match(self.input, GOTO, self.FOLLOW_GOTO_in_gotoStatement5056)
                GOTO290_tree = self._adaptor.createWithPayload(GOTO290)
                root_0 = self._adaptor.becomeRoot(GOTO290_tree, root_0)



                self._state.following.append(self.FOLLOW_label_in_gotoStatement5059)
                label291 = self.label()

                self._state.following.pop()
                self._adaptor.addChild(root_0, label291.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "gotoStatement"


    class emptyStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.emptyStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "emptyStatement"
    # ryter.g:614:1: emptyStatement :;
    def emptyStatement(self, ):
        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        try:
            try:
                # ryter.g:615:5: ()
                # ryter.g:616:5: 
                pass 
                root_0 = self._adaptor.nil()




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            finally:
                pass

        finally:
            pass
        return retval

    # $ANTLR end "emptyStatement"


    class empty_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.empty_return, self).__init__()

            self.tree = None





    # $ANTLR start "empty"
    # ryter.g:618:1: empty :;
    def empty(self, ):
        retval = self.empty_return()
        retval.start = self.input.LT(1)


        root_0 = None

        try:
            try:
                # ryter.g:619:5: ()
                # ryter.g:620:5: 
                pass 
                root_0 = self._adaptor.nil()




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            finally:
                pass

        finally:
            pass
        return retval

    # $ANTLR end "empty"


    class structuredStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.structuredStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "structuredStatement"
    # ryter.g:622:1: structuredStatement : ( compoundStatement | conditionalStatement | repetetiveStatement | withStatement );
    def structuredStatement(self, ):
        retval = self.structuredStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        compoundStatement292 = None
        conditionalStatement293 = None
        repetetiveStatement294 = None
        withStatement295 = None


        try:
            try:
                # ryter.g:623:5: ( compoundStatement | conditionalStatement | repetetiveStatement | withStatement )
                alt63 = 4
                LA63 = self.input.LA(1)
                if LA63 == BEGIN:
                    alt63 = 1
                elif LA63 == CASE or LA63 == IF:
                    alt63 = 2
                elif LA63 == FOR or LA63 == REPEAT or LA63 == WHILE:
                    alt63 = 3
                elif LA63 == WITH:
                    alt63 = 4
                else:
                    nvae = NoViableAltException("", 63, 0, self.input)

                    raise nvae


                if alt63 == 1:
                    # ryter.g:623:7: compoundStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_compoundStatement_in_structuredStatement5107)
                    compoundStatement292 = self.compoundStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, compoundStatement292.tree)



                elif alt63 == 2:
                    # ryter.g:624:7: conditionalStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_conditionalStatement_in_structuredStatement5115)
                    conditionalStatement293 = self.conditionalStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditionalStatement293.tree)



                elif alt63 == 3:
                    # ryter.g:625:7: repetetiveStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_repetetiveStatement_in_structuredStatement5123)
                    repetetiveStatement294 = self.repetetiveStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, repetetiveStatement294.tree)



                elif alt63 == 4:
                    # ryter.g:626:7: withStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_withStatement_in_structuredStatement5131)
                    withStatement295 = self.withStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, withStatement295.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "structuredStatement"


    class compoundStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.compoundStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "compoundStatement"
    # ryter.g:629:1: compoundStatement : BEGIN statements END -> ^( BLOCK ( statements )* ) ;
    def compoundStatement(self, ):
        retval = self.compoundStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BEGIN296 = None
        END298 = None
        statements297 = None

        BEGIN296_tree = None
        END298_tree = None
        stream_END = RewriteRuleTokenStream(self._adaptor, "token END")
        stream_BEGIN = RewriteRuleTokenStream(self._adaptor, "token BEGIN")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # ryter.g:630:5: ( BEGIN statements END -> ^( BLOCK ( statements )* ) )
                # ryter.g:630:7: BEGIN statements END
                pass 
                BEGIN296 = self.match(self.input, BEGIN, self.FOLLOW_BEGIN_in_compoundStatement5148) 
                stream_BEGIN.add(BEGIN296)


                self._state.following.append(self.FOLLOW_statements_in_compoundStatement5154)
                statements297 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements297.tree)


                END298 = self.match(self.input, END, self.FOLLOW_END_in_compoundStatement5162) 
                stream_END.add(END298)


                # AST Rewrite
                # elements: statements
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 633:9: -> ^( BLOCK ( statements )* )
                # ryter.g:633:12: ^( BLOCK ( statements )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BLOCK, "BLOCK")
                , root_1)

                # ryter.g:633:20: ( statements )*
                while stream_statements.hasNext():
                    self._adaptor.addChild(root_1, stream_statements.nextTree())


                stream_statements.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "compoundStatement"


    class statements_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.statements_return, self).__init__()

            self.tree = None





    # $ANTLR start "statements"
    # ryter.g:636:1: statements : statement ( SEMI ! statement )* ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMI300 = None
        statement299 = None
        statement301 = None

        SEMI300_tree = None

        try:
            try:
                # ryter.g:637:5: ( statement ( SEMI ! statement )* )
                # ryter.g:637:7: statement ( SEMI ! statement )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_statement_in_statements5197)
                statement299 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement299.tree)


                # ryter.g:637:17: ( SEMI ! statement )*
                while True: #loop64
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if (LA64_0 == SEMI) :
                        alt64 = 1


                    if alt64 == 1:
                        # ryter.g:637:19: SEMI ! statement
                        pass 
                        SEMI300 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statements5201)

                        self._state.following.append(self.FOLLOW_statement_in_statements5204)
                        statement301 = self.statement()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement301.tree)



                    else:
                        break #loop64




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "statements"


    class conditionalStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.conditionalStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "conditionalStatement"
    # ryter.g:640:1: conditionalStatement : ( ifStatement | caseStatement );
    def conditionalStatement(self, ):
        retval = self.conditionalStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ifStatement302 = None
        caseStatement303 = None


        try:
            try:
                # ryter.g:641:5: ( ifStatement | caseStatement )
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == IF) :
                    alt65 = 1
                elif (LA65_0 == CASE) :
                    alt65 = 2
                else:
                    nvae = NoViableAltException("", 65, 0, self.input)

                    raise nvae


                if alt65 == 1:
                    # ryter.g:641:7: ifStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_ifStatement_in_conditionalStatement5225)
                    ifStatement302 = self.ifStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, ifStatement302.tree)



                elif alt65 == 2:
                    # ryter.g:642:7: caseStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_caseStatement_in_conditionalStatement5233)
                    caseStatement303 = self.caseStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, caseStatement303.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "conditionalStatement"


    class ifStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.ifStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "ifStatement"
    # ryter.g:645:1: ifStatement : IF ^ expression THEN ! statement ( ELSE ! statement )? ;
    def ifStatement(self, ):
        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF304 = None
        THEN306 = None
        ELSE308 = None
        expression305 = None
        statement307 = None
        statement309 = None

        IF304_tree = None
        THEN306_tree = None
        ELSE308_tree = None

        try:
            try:
                # ryter.g:646:5: ( IF ^ expression THEN ! statement ( ELSE ! statement )? )
                # ryter.g:646:7: IF ^ expression THEN ! statement ( ELSE ! statement )?
                pass 
                root_0 = self._adaptor.nil()


                IF304 = self.match(self.input, IF, self.FOLLOW_IF_in_ifStatement5250)
                IF304_tree = self._adaptor.createWithPayload(IF304)
                root_0 = self._adaptor.becomeRoot(IF304_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_ifStatement5253)
                expression305 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression305.tree)


                THEN306 = self.match(self.input, THEN, self.FOLLOW_THEN_in_ifStatement5255)

                self._state.following.append(self.FOLLOW_statement_in_ifStatement5258)
                statement307 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement307.tree)


                # ryter.g:647:7: ( ELSE ! statement )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if (LA66_0 == ELSE) :
                    alt66 = 1
                if alt66 == 1:
                    # ryter.g:651:6: ELSE ! statement
                    pass 
                    ELSE308 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_ifStatement5288)

                    self._state.following.append(self.FOLLOW_statement_in_ifStatement5291)
                    statement309 = self.statement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement309.tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "ifStatement"


    class caseStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.caseStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "caseStatement"
    # ryter.g:655:1: caseStatement : CASE ^ expression OF ! caseListElement ( SEMI ! caseListElement )* ( SEMI !)? ( ELSE ! statements )? END !;
    def caseStatement(self, ):
        retval = self.caseStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CASE310 = None
        OF312 = None
        SEMI314 = None
        SEMI316 = None
        ELSE317 = None
        END319 = None
        expression311 = None
        caseListElement313 = None
        caseListElement315 = None
        statements318 = None

        CASE310_tree = None
        OF312_tree = None
        SEMI314_tree = None
        SEMI316_tree = None
        ELSE317_tree = None
        END319_tree = None

        try:
            try:
                # ryter.g:656:5: ( CASE ^ expression OF ! caseListElement ( SEMI ! caseListElement )* ( SEMI !)? ( ELSE ! statements )? END !)
                # ryter.g:656:7: CASE ^ expression OF ! caseListElement ( SEMI ! caseListElement )* ( SEMI !)? ( ELSE ! statements )? END !
                pass 
                root_0 = self._adaptor.nil()


                CASE310 = self.match(self.input, CASE, self.FOLLOW_CASE_in_caseStatement5316)
                CASE310_tree = self._adaptor.createWithPayload(CASE310)
                root_0 = self._adaptor.becomeRoot(CASE310_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_caseStatement5319)
                expression311 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression311.tree)


                OF312 = self.match(self.input, OF, self.FOLLOW_OF_in_caseStatement5321)

                self._state.following.append(self.FOLLOW_caseListElement_in_caseStatement5332)
                caseListElement313 = self.caseListElement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, caseListElement313.tree)


                # ryter.g:657:25: ( SEMI ! caseListElement )*
                while True: #loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == SEMI) :
                        LA67_1 = self.input.LA(2)

                        if (LA67_1 == CHR or LA67_1 == IDENT or LA67_1 == MINUS or (NUM_INT <= LA67_1 <= NUM_REAL) or LA67_1 == PLUS or LA67_1 == STRING_LITERAL) :
                            alt67 = 1




                    if alt67 == 1:
                        # ryter.g:657:27: SEMI ! caseListElement
                        pass 
                        SEMI314 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_caseStatement5336)

                        self._state.following.append(self.FOLLOW_caseListElement_in_caseStatement5339)
                        caseListElement315 = self.caseListElement()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, caseListElement315.tree)



                    else:
                        break #loop67


                # ryter.g:657:56: ( SEMI !)?
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == SEMI) :
                    alt68 = 1
                if alt68 == 1:
                    # ryter.g:657:56: SEMI !
                    pass 
                    SEMI316 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_caseStatement5344)




                # ryter.g:658:7: ( ELSE ! statements )?
                alt69 = 2
                LA69_0 = self.input.LA(1)

                if (LA69_0 == ELSE) :
                    alt69 = 1
                if alt69 == 1:
                    # ryter.g:658:9: ELSE ! statements
                    pass 
                    ELSE317 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_caseStatement5356)

                    self._state.following.append(self.FOLLOW_statements_in_caseStatement5359)
                    statements318 = self.statements()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statements318.tree)





                END319 = self.match(self.input, END, self.FOLLOW_END_in_caseStatement5370)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "caseStatement"


    class caseListElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.caseListElement_return, self).__init__()

            self.tree = None





    # $ANTLR start "caseListElement"
    # ryter.g:662:1: caseListElement : constList COLON ^ statement ;
    def caseListElement(self, ):
        retval = self.caseListElement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COLON321 = None
        constList320 = None
        statement322 = None

        COLON321_tree = None

        try:
            try:
                # ryter.g:663:5: ( constList COLON ^ statement )
                # ryter.g:663:7: constList COLON ^ statement
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_constList_in_caseListElement5388)
                constList320 = self.constList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, constList320.tree)


                COLON321 = self.match(self.input, COLON, self.FOLLOW_COLON_in_caseListElement5390)
                COLON321_tree = self._adaptor.createWithPayload(COLON321)
                root_0 = self._adaptor.becomeRoot(COLON321_tree, root_0)



                self._state.following.append(self.FOLLOW_statement_in_caseListElement5393)
                statement322 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement322.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "caseListElement"


    class repetetiveStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.repetetiveStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "repetetiveStatement"
    # ryter.g:666:1: repetetiveStatement : ( whileStatement | repeatStatement | forStatement );
    def repetetiveStatement(self, ):
        retval = self.repetetiveStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        whileStatement323 = None
        repeatStatement324 = None
        forStatement325 = None


        try:
            try:
                # ryter.g:667:5: ( whileStatement | repeatStatement | forStatement )
                alt70 = 3
                LA70 = self.input.LA(1)
                if LA70 == WHILE:
                    alt70 = 1
                elif LA70 == REPEAT:
                    alt70 = 2
                elif LA70 == FOR:
                    alt70 = 3
                else:
                    nvae = NoViableAltException("", 70, 0, self.input)

                    raise nvae


                if alt70 == 1:
                    # ryter.g:667:7: whileStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_whileStatement_in_repetetiveStatement5410)
                    whileStatement323 = self.whileStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, whileStatement323.tree)



                elif alt70 == 2:
                    # ryter.g:668:7: repeatStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_repeatStatement_in_repetetiveStatement5418)
                    repeatStatement324 = self.repeatStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, repeatStatement324.tree)



                elif alt70 == 3:
                    # ryter.g:669:7: forStatement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_forStatement_in_repetetiveStatement5426)
                    forStatement325 = self.forStatement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, forStatement325.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "repetetiveStatement"


    class whileStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.whileStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "whileStatement"
    # ryter.g:672:1: whileStatement : WHILE ^ expression DO ! statement ;
    def whileStatement(self, ):
        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE326 = None
        DO328 = None
        expression327 = None
        statement329 = None

        WHILE326_tree = None
        DO328_tree = None

        try:
            try:
                # ryter.g:673:5: ( WHILE ^ expression DO ! statement )
                # ryter.g:673:7: WHILE ^ expression DO ! statement
                pass 
                root_0 = self._adaptor.nil()


                WHILE326 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_whileStatement5443)
                WHILE326_tree = self._adaptor.createWithPayload(WHILE326)
                root_0 = self._adaptor.becomeRoot(WHILE326_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_whileStatement5446)
                expression327 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression327.tree)


                DO328 = self.match(self.input, DO, self.FOLLOW_DO_in_whileStatement5448)

                self._state.following.append(self.FOLLOW_statement_in_whileStatement5451)
                statement329 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement329.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "whileStatement"


    class repeatStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.repeatStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "repeatStatement"
    # ryter.g:676:1: repeatStatement : REPEAT ^ statements UNTIL ! expression ;
    def repeatStatement(self, ):
        retval = self.repeatStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REPEAT330 = None
        UNTIL332 = None
        statements331 = None
        expression333 = None

        REPEAT330_tree = None
        UNTIL332_tree = None

        try:
            try:
                # ryter.g:677:5: ( REPEAT ^ statements UNTIL ! expression )
                # ryter.g:677:7: REPEAT ^ statements UNTIL ! expression
                pass 
                root_0 = self._adaptor.nil()


                REPEAT330 = self.match(self.input, REPEAT, self.FOLLOW_REPEAT_in_repeatStatement5468)
                REPEAT330_tree = self._adaptor.createWithPayload(REPEAT330)
                root_0 = self._adaptor.becomeRoot(REPEAT330_tree, root_0)



                self._state.following.append(self.FOLLOW_statements_in_repeatStatement5471)
                statements331 = self.statements()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statements331.tree)


                UNTIL332 = self.match(self.input, UNTIL, self.FOLLOW_UNTIL_in_repeatStatement5473)

                self._state.following.append(self.FOLLOW_expression_in_repeatStatement5476)
                expression333 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression333.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "repeatStatement"


    class forStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.forStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "forStatement"
    # ryter.g:680:1: forStatement : FOR ^ identifier ASSIGN ! forList DO ! statement ;
    def forStatement(self, ):
        retval = self.forStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FOR334 = None
        ASSIGN336 = None
        DO338 = None
        identifier335 = None
        forList337 = None
        statement339 = None

        FOR334_tree = None
        ASSIGN336_tree = None
        DO338_tree = None

        try:
            try:
                # ryter.g:681:5: ( FOR ^ identifier ASSIGN ! forList DO ! statement )
                # ryter.g:681:7: FOR ^ identifier ASSIGN ! forList DO ! statement
                pass 
                root_0 = self._adaptor.nil()


                FOR334 = self.match(self.input, FOR, self.FOLLOW_FOR_in_forStatement5493)
                FOR334_tree = self._adaptor.createWithPayload(FOR334)
                root_0 = self._adaptor.becomeRoot(FOR334_tree, root_0)



                self._state.following.append(self.FOLLOW_identifier_in_forStatement5496)
                identifier335 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier335.tree)


                ASSIGN336 = self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_forStatement5498)

                self._state.following.append(self.FOLLOW_forList_in_forStatement5501)
                forList337 = self.forList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, forList337.tree)


                DO338 = self.match(self.input, DO, self.FOLLOW_DO_in_forStatement5503)

                self._state.following.append(self.FOLLOW_statement_in_forStatement5506)
                statement339 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement339.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "forStatement"


    class forList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.forList_return, self).__init__()

            self.tree = None





    # $ANTLR start "forList"
    # ryter.g:684:1: forList : initialValue ( TO ^| DOWNTO ^) finalValue ;
    def forList(self, ):
        retval = self.forList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TO341 = None
        DOWNTO342 = None
        initialValue340 = None
        finalValue343 = None

        TO341_tree = None
        DOWNTO342_tree = None

        try:
            try:
                # ryter.g:685:5: ( initialValue ( TO ^| DOWNTO ^) finalValue )
                # ryter.g:685:7: initialValue ( TO ^| DOWNTO ^) finalValue
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_initialValue_in_forList5523)
                initialValue340 = self.initialValue()

                self._state.following.pop()
                self._adaptor.addChild(root_0, initialValue340.tree)


                # ryter.g:685:20: ( TO ^| DOWNTO ^)
                alt71 = 2
                LA71_0 = self.input.LA(1)

                if (LA71_0 == TO) :
                    alt71 = 1
                elif (LA71_0 == DOWNTO) :
                    alt71 = 2
                else:
                    nvae = NoViableAltException("", 71, 0, self.input)

                    raise nvae


                if alt71 == 1:
                    # ryter.g:685:21: TO ^
                    pass 
                    TO341 = self.match(self.input, TO, self.FOLLOW_TO_in_forList5526)
                    TO341_tree = self._adaptor.createWithPayload(TO341)
                    root_0 = self._adaptor.becomeRoot(TO341_tree, root_0)




                elif alt71 == 2:
                    # ryter.g:685:27: DOWNTO ^
                    pass 
                    DOWNTO342 = self.match(self.input, DOWNTO, self.FOLLOW_DOWNTO_in_forList5531)
                    DOWNTO342_tree = self._adaptor.createWithPayload(DOWNTO342)
                    root_0 = self._adaptor.becomeRoot(DOWNTO342_tree, root_0)






                self._state.following.append(self.FOLLOW_finalValue_in_forList5535)
                finalValue343 = self.finalValue()

                self._state.following.pop()
                self._adaptor.addChild(root_0, finalValue343.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "forList"


    class initialValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.initialValue_return, self).__init__()

            self.tree = None





    # $ANTLR start "initialValue"
    # ryter.g:688:1: initialValue : expression ;
    def initialValue(self, ):
        retval = self.initialValue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expression344 = None


        try:
            try:
                # ryter.g:689:5: ( expression )
                # ryter.g:689:7: expression
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expression_in_initialValue5552)
                expression344 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression344.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "initialValue"


    class finalValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.finalValue_return, self).__init__()

            self.tree = None





    # $ANTLR start "finalValue"
    # ryter.g:692:1: finalValue : expression ;
    def finalValue(self, ):
        retval = self.finalValue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expression345 = None


        try:
            try:
                # ryter.g:693:5: ( expression )
                # ryter.g:693:7: expression
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expression_in_finalValue5569)
                expression345 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression345.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "finalValue"


    class withStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.withStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "withStatement"
    # ryter.g:696:1: withStatement : WITH ^ recordVariableList DO ! statement ;
    def withStatement(self, ):
        retval = self.withStatement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH346 = None
        DO348 = None
        recordVariableList347 = None
        statement349 = None

        WITH346_tree = None
        DO348_tree = None

        try:
            try:
                # ryter.g:697:5: ( WITH ^ recordVariableList DO ! statement )
                # ryter.g:697:7: WITH ^ recordVariableList DO ! statement
                pass 
                root_0 = self._adaptor.nil()


                WITH346 = self.match(self.input, WITH, self.FOLLOW_WITH_in_withStatement5586)
                WITH346_tree = self._adaptor.createWithPayload(WITH346)
                root_0 = self._adaptor.becomeRoot(WITH346_tree, root_0)



                self._state.following.append(self.FOLLOW_recordVariableList_in_withStatement5589)
                recordVariableList347 = self.recordVariableList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, recordVariableList347.tree)


                DO348 = self.match(self.input, DO, self.FOLLOW_DO_in_withStatement5591)

                self._state.following.append(self.FOLLOW_statement_in_withStatement5594)
                statement349 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement349.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "withStatement"


    class recordVariableList_return(ParserRuleReturnScope):
        def __init__(self):
            super(ryterParser.recordVariableList_return, self).__init__()

            self.tree = None





    # $ANTLR start "recordVariableList"
    # ryter.g:700:1: recordVariableList : variable ( COMMA ! variable )* ;
    def recordVariableList(self, ):
        retval = self.recordVariableList_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA351 = None
        variable350 = None
        variable352 = None

        COMMA351_tree = None

        try:
            try:
                # ryter.g:701:5: ( variable ( COMMA ! variable )* )
                # ryter.g:701:7: variable ( COMMA ! variable )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_variable_in_recordVariableList5611)
                variable350 = self.variable()

                self._state.following.pop()
                self._adaptor.addChild(root_0, variable350.tree)


                # ryter.g:701:16: ( COMMA ! variable )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == COMMA) :
                        alt72 = 1


                    if alt72 == 1:
                        # ryter.g:701:18: COMMA ! variable
                        pass 
                        COMMA351 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_recordVariableList5615)

                        self._state.following.append(self.FOLLOW_variable_in_recordVariableList5618)
                        variable352 = self.variable()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, variable352.tree)



                    else:
                        break #loop72




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "recordVariableList"



 

    FOLLOW_programHeading_in_program2242 = frozenset([11, 21, 39, 47, 50, 51, 70, 90, 95, 96])
    FOLLOW_INTERFACE_in_program2245 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_block_in_program2255 = frozenset([25])
    FOLLOW_DOT_in_program2263 = frozenset([1])
    FOLLOW_PROGRAM_in_programHeading2296 = frozenset([44])
    FOLLOW_identifier_in_programHeading2299 = frozenset([56, 81])
    FOLLOW_LPAREN_in_programHeading2302 = frozenset([44])
    FOLLOW_identifierList_in_programHeading2305 = frozenset([79])
    FOLLOW_RPAREN_in_programHeading2307 = frozenset([81])
    FOLLOW_SEMI_in_programHeading2312 = frozenset([1])
    FOLLOW_UNIT_in_programHeading2321 = frozenset([44])
    FOLLOW_identifier_in_programHeading2323 = frozenset([81])
    FOLLOW_SEMI_in_programHeading2325 = frozenset([1])
    FOLLOW_IDENT_in_identifier2341 = frozenset([1])
    FOLLOW_labelDeclarationPart_in_block2360 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_constantDefinitionPart_in_block2370 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_typeDefinitionPart_in_block2380 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_variableDeclarationPart_in_block2390 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_procedureAndFunctionDeclarationPart_in_block2400 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_usesUnitsPart_in_block2410 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_IMPLEMENTATION_in_block2420 = frozenset([11, 21, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_compoundStatement_in_block2437 = frozenset([1])
    FOLLOW_USES_in_usesUnitsPart2454 = frozenset([44])
    FOLLOW_identifierList_in_usesUnitsPart2457 = frozenset([81])
    FOLLOW_SEMI_in_usesUnitsPart2459 = frozenset([1])
    FOLLOW_LABEL_in_labelDeclarationPart2477 = frozenset([63])
    FOLLOW_label_in_labelDeclarationPart2480 = frozenset([18, 81])
    FOLLOW_COMMA_in_labelDeclarationPart2484 = frozenset([63])
    FOLLOW_label_in_labelDeclarationPart2487 = frozenset([18, 81])
    FOLLOW_SEMI_in_labelDeclarationPart2492 = frozenset([1])
    FOLLOW_unsignedInteger_in_label2510 = frozenset([1])
    FOLLOW_CONST_in_constantDefinitionPart2527 = frozenset([44])
    FOLLOW_constantDefinition_in_constantDefinitionPart2530 = frozenset([81])
    FOLLOW_SEMI_in_constantDefinitionPart2534 = frozenset([44])
    FOLLOW_constantDefinition_in_constantDefinitionPart2537 = frozenset([81])
    FOLLOW_SEMI_in_constantDefinitionPart2542 = frozenset([1])
    FOLLOW_identifier_in_constantDefinition2560 = frozenset([31])
    FOLLOW_EQUAL_in_constantDefinition2562 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_constant_in_constantDefinition2565 = frozenset([1])
    FOLLOW_CHR_in_constantChr2582 = frozenset([56])
    FOLLOW_LPAREN_in_constantChr2585 = frozenset([44, 63])
    FOLLOW_unsignedInteger_in_constantChr2589 = frozenset([79])
    FOLLOW_identifier_in_constantChr2591 = frozenset([79])
    FOLLOW_RPAREN_in_constantChr2594 = frozenset([1])
    FOLLOW_unsignedNumber_in_constant2612 = frozenset([1])
    FOLLOW_sign_in_constant2622 = frozenset([63, 64])
    FOLLOW_unsignedNumber_in_constant2626 = frozenset([1])
    FOLLOW_identifier_in_constant2645 = frozenset([1])
    FOLLOW_sign_in_constant2655 = frozenset([44])
    FOLLOW_identifier_in_constant2659 = frozenset([1])
    FOLLOW_string_in_constant2678 = frozenset([1])
    FOLLOW_constantChr_in_constant2686 = frozenset([1])
    FOLLOW_unsignedInteger_in_unsignedNumber2703 = frozenset([1])
    FOLLOW_unsignedReal_in_unsignedNumber2711 = frozenset([1])
    FOLLOW_NUM_INT_in_unsignedInteger2728 = frozenset([1])
    FOLLOW_NUM_REAL_in_unsignedReal2745 = frozenset([1])
    FOLLOW_STRING_LITERAL_in_string2783 = frozenset([1])
    FOLLOW_TYPE_in_typeDefinitionPart2800 = frozenset([44])
    FOLLOW_typeDefinition_in_typeDefinitionPart2803 = frozenset([81])
    FOLLOW_SEMI_in_typeDefinitionPart2807 = frozenset([44])
    FOLLOW_typeDefinition_in_typeDefinitionPart2810 = frozenset([81])
    FOLLOW_SEMI_in_typeDefinitionPart2815 = frozenset([1])
    FOLLOW_identifier_in_typeDefinition2834 = frozenset([31])
    FOLLOW_EQUAL_in_typeDefinition2838 = frozenset([8, 13, 15, 16, 36, 39, 44, 49, 56, 58, 63, 64, 67, 68, 69, 70, 76, 77, 82, 85, 86])
    FOLLOW_type_in_typeDefinition2851 = frozenset([1])
    FOLLOW_functionType_in_typeDefinition2861 = frozenset([1])
    FOLLOW_procedureType_in_typeDefinition2872 = frozenset([1])
    FOLLOW_FUNCTION_in_functionType2897 = frozenset([17, 56])
    FOLLOW_formalParameterList_in_functionType2901 = frozenset([17])
    FOLLOW_COLON_in_functionType2905 = frozenset([13, 15, 44, 49, 76, 85])
    FOLLOW_resultType_in_functionType2908 = frozenset([1])
    FOLLOW_PROCEDURE_in_procedureType2925 = frozenset([1, 56])
    FOLLOW_formalParameterList_in_procedureType2929 = frozenset([1])
    FOLLOW_simpleType_in_type2948 = frozenset([1])
    FOLLOW_structuredType_in_type2956 = frozenset([1])
    FOLLOW_pointerType_in_type2964 = frozenset([1])
    FOLLOW_scalarType_in_simpleType2981 = frozenset([1])
    FOLLOW_subrangeType_in_simpleType2989 = frozenset([1])
    FOLLOW_typeIdentifier_in_simpleType2998 = frozenset([1])
    FOLLOW_stringtype_in_simpleType3006 = frozenset([1])
    FOLLOW_LPAREN_in_scalarType3023 = frozenset([44])
    FOLLOW_identifierList_in_scalarType3025 = frozenset([79])
    FOLLOW_RPAREN_in_scalarType3027 = frozenset([1])
    FOLLOW_constant_in_subrangeType3059 = frozenset([26])
    FOLLOW_DOTDOT_in_subrangeType3061 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_constant_in_subrangeType3065 = frozenset([1])
    FOLLOW_identifier_in_typeIdentifier3098 = frozenset([1])
    FOLLOW_CHAR_in_typeIdentifier3106 = frozenset([1])
    FOLLOW_BOOLEAN_in_typeIdentifier3114 = frozenset([1])
    FOLLOW_INTEGER_in_typeIdentifier3122 = frozenset([1])
    FOLLOW_REAL_in_typeIdentifier3130 = frozenset([1])
    FOLLOW_STRING_in_typeIdentifier3138 = frozenset([1])
    FOLLOW_PACKED_in_structuredType3156 = frozenset([8, 16, 36, 44, 58, 63, 64, 68, 77, 82, 86])
    FOLLOW_unpackedStructuredType_in_structuredType3159 = frozenset([1])
    FOLLOW_unpackedStructuredType_in_structuredType3166 = frozenset([1])
    FOLLOW_arrayType_in_unpackedStructuredType3183 = frozenset([1])
    FOLLOW_recordType_in_unpackedStructuredType3191 = frozenset([1])
    FOLLOW_setType_in_unpackedStructuredType3199 = frozenset([1])
    FOLLOW_fileType_in_unpackedStructuredType3207 = frozenset([1])
    FOLLOW_subrangeType_in_unpackedStructuredType3215 = frozenset([1])
    FOLLOW_STRING_in_stringtype3233 = frozenset([56])
    FOLLOW_LPAREN_in_stringtype3236 = frozenset([44, 63, 64])
    FOLLOW_identifier_in_stringtype3240 = frozenset([79])
    FOLLOW_unsignedNumber_in_stringtype3242 = frozenset([79])
    FOLLOW_RPAREN_in_stringtype3245 = frozenset([1])
    FOLLOW_STRING_in_stringtype3255 = frozenset([53])
    FOLLOW_LBRACK2_in_stringtype3258 = frozenset([44, 63, 64])
    FOLLOW_identifier_in_stringtype3262 = frozenset([74])
    FOLLOW_unsignedNumber_in_stringtype3264 = frozenset([74])
    FOLLOW_RBRACK2_in_stringtype3267 = frozenset([1])
    FOLLOW_ARRAY_in_arrayType3286 = frozenset([52])
    FOLLOW_LBRACK_in_arrayType3289 = frozenset([13, 15, 16, 44, 49, 56, 58, 63, 64, 68, 76, 85, 86])
    FOLLOW_typeList_in_arrayType3292 = frozenset([73])
    FOLLOW_RBRACK_in_arrayType3294 = frozenset([65])
    FOLLOW_OF_in_arrayType3297 = frozenset([8, 13, 15, 16, 36, 44, 49, 56, 58, 63, 64, 67, 68, 69, 76, 77, 82, 85, 86])
    FOLLOW_componentType_in_arrayType3300 = frozenset([1])
    FOLLOW_ARRAY_in_arrayType3308 = frozenset([53])
    FOLLOW_LBRACK2_in_arrayType3311 = frozenset([13, 15, 16, 44, 49, 56, 58, 63, 64, 68, 76, 85, 86])
    FOLLOW_typeList_in_arrayType3314 = frozenset([74])
    FOLLOW_RBRACK2_in_arrayType3316 = frozenset([65])
    FOLLOW_OF_in_arrayType3319 = frozenset([8, 13, 15, 16, 36, 44, 49, 56, 58, 63, 64, 67, 68, 69, 76, 77, 82, 85, 86])
    FOLLOW_componentType_in_arrayType3322 = frozenset([1])
    FOLLOW_indexType_in_typeList3335 = frozenset([1, 18])
    FOLLOW_COMMA_in_typeList3339 = frozenset([13, 15, 16, 44, 49, 56, 58, 63, 64, 68, 76, 85, 86])
    FOLLOW_indexType_in_typeList3341 = frozenset([1, 18])
    FOLLOW_simpleType_in_indexType3370 = frozenset([1])
    FOLLOW_type_in_componentType3387 = frozenset([1])
    FOLLOW_RECORD_in_recordType3404 = frozenset([14, 44])
    FOLLOW_fieldList_in_recordType3407 = frozenset([30])
    FOLLOW_END_in_recordType3409 = frozenset([1])
    FOLLOW_fixedPart_in_fieldList3431 = frozenset([1, 81])
    FOLLOW_SEMI_in_fieldList3435 = frozenset([14])
    FOLLOW_variantPart_in_fieldList3439 = frozenset([1])
    FOLLOW_SEMI_in_fieldList3443 = frozenset([1])
    FOLLOW_variantPart_in_fieldList3458 = frozenset([1])
    FOLLOW_recordSection_in_fixedPart3507 = frozenset([1, 81])
    FOLLOW_SEMI_in_fixedPart3511 = frozenset([44])
    FOLLOW_recordSection_in_fixedPart3514 = frozenset([1, 81])
    FOLLOW_identifierList_in_recordSection3534 = frozenset([17])
    FOLLOW_COLON_in_recordSection3536 = frozenset([8, 13, 15, 16, 36, 44, 49, 56, 58, 63, 64, 67, 68, 69, 76, 77, 82, 85, 86])
    FOLLOW_type_in_recordSection3538 = frozenset([1])
    FOLLOW_CASE_in_variantPart3569 = frozenset([13, 15, 44, 49, 76, 85])
    FOLLOW_tag_in_variantPart3572 = frozenset([65])
    FOLLOW_OF_in_variantPart3574 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_variant_in_variantPart3577 = frozenset([1, 81])
    FOLLOW_SEMI_in_variantPart3581 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_variant_in_variantPart3584 = frozenset([1, 81])
    FOLLOW_SEMI_in_variantPart3588 = frozenset([1, 81])
    FOLLOW_identifier_in_tag3611 = frozenset([17])
    FOLLOW_COLON_in_tag3613 = frozenset([13, 15, 44, 49, 76, 85])
    FOLLOW_typeIdentifier_in_tag3617 = frozenset([1])
    FOLLOW_typeIdentifier_in_tag3640 = frozenset([1])
    FOLLOW_constList_in_variant3667 = frozenset([17])
    FOLLOW_COLON_in_variant3671 = frozenset([56])
    FOLLOW_LPAREN_in_variant3680 = frozenset([14, 44])
    FOLLOW_fieldList_in_variant3683 = frozenset([79])
    FOLLOW_RPAREN_in_variant3685 = frozenset([1])
    FOLLOW_SET_in_setType3703 = frozenset([65])
    FOLLOW_OF_in_setType3706 = frozenset([13, 15, 16, 44, 49, 56, 58, 63, 64, 68, 76, 85, 86])
    FOLLOW_simpleType_in_setType3709 = frozenset([1])
    FOLLOW_FILE_in_fileType3726 = frozenset([65])
    FOLLOW_OF_in_fileType3729 = frozenset([8, 13, 15, 16, 36, 44, 49, 56, 58, 63, 64, 67, 68, 69, 76, 77, 82, 85, 86])
    FOLLOW_type_in_fileType3732 = frozenset([1])
    FOLLOW_FILE_in_fileType3740 = frozenset([1])
    FOLLOW_POINTER_in_pointerType3757 = frozenset([13, 15, 44, 49, 76, 85])
    FOLLOW_typeIdentifier_in_pointerType3760 = frozenset([1])
    FOLLOW_VAR_in_variableDeclarationPart3778 = frozenset([44])
    FOLLOW_variableDeclaration_in_variableDeclarationPart3781 = frozenset([81])
    FOLLOW_SEMI_in_variableDeclarationPart3785 = frozenset([44])
    FOLLOW_variableDeclaration_in_variableDeclarationPart3788 = frozenset([81])
    FOLLOW_SEMI_in_variableDeclarationPart3793 = frozenset([1])
    FOLLOW_identifierList_in_variableDeclaration3811 = frozenset([17])
    FOLLOW_COLON_in_variableDeclaration3815 = frozenset([8, 13, 15, 16, 36, 44, 49, 56, 58, 63, 64, 67, 68, 69, 76, 77, 82, 85, 86])
    FOLLOW_type_in_variableDeclaration3820 = frozenset([1])
    FOLLOW_procedureOrFunctionDeclaration_in_procedureAndFunctionDeclarationPart3837 = frozenset([81])
    FOLLOW_SEMI_in_procedureAndFunctionDeclarationPart3839 = frozenset([1])
    FOLLOW_procedureDeclaration_in_procedureOrFunctionDeclaration3857 = frozenset([1])
    FOLLOW_functionDeclaration_in_procedureOrFunctionDeclaration3865 = frozenset([1])
    FOLLOW_PROCEDURE_in_procedureDeclaration3882 = frozenset([44])
    FOLLOW_identifier_in_procedureDeclaration3885 = frozenset([56, 81])
    FOLLOW_formalParameterList_in_procedureDeclaration3888 = frozenset([81])
    FOLLOW_SEMI_in_procedureDeclaration3892 = frozenset([11, 21, 38, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_block_in_procedureDeclaration3903 = frozenset([1])
    FOLLOW_directive_in_procedureDeclaration3907 = frozenset([1])
    FOLLOW_FUNCTION_in_functionDeclaration3930 = frozenset([44])
    FOLLOW_identifier_in_functionDeclaration3933 = frozenset([17, 56])
    FOLLOW_formalParameterList_in_functionDeclaration3936 = frozenset([17])
    FOLLOW_COLON_in_functionDeclaration3940 = frozenset([13, 15, 44, 49, 76, 85])
    FOLLOW_resultType_in_functionDeclaration3943 = frozenset([81])
    FOLLOW_SEMI_in_functionDeclaration3945 = frozenset([11, 21, 38, 39, 47, 51, 70, 90, 95, 96])
    FOLLOW_block_in_functionDeclaration3956 = frozenset([1])
    FOLLOW_directive_in_functionDeclaration3960 = frozenset([1])
    FOLLOW_FORWARD_in_directive3979 = frozenset([1])
    FOLLOW_LPAREN_in_formalParameterList3997 = frozenset([39, 44, 70, 96])
    FOLLOW_formalParameterSection_in_formalParameterList3999 = frozenset([79, 81])
    FOLLOW_SEMI_in_formalParameterList4003 = frozenset([39, 44, 70, 96])
    FOLLOW_formalParameterSection_in_formalParameterList4005 = frozenset([79, 81])
    FOLLOW_RPAREN_in_formalParameterList4010 = frozenset([1])
    FOLLOW_parameterGroup_in_formalParameterSection4040 = frozenset([1])
    FOLLOW_VAR_in_formalParameterSection4048 = frozenset([44])
    FOLLOW_parameterGroup_in_formalParameterSection4051 = frozenset([1])
    FOLLOW_FUNCTION_in_formalParameterSection4059 = frozenset([44])
    FOLLOW_parameterGroup_in_formalParameterSection4062 = frozenset([1])
    FOLLOW_PROCEDURE_in_formalParameterSection4070 = frozenset([44])
    FOLLOW_parameterGroup_in_formalParameterSection4073 = frozenset([1])
    FOLLOW_identifierList_in_parameterGroup4092 = frozenset([17])
    FOLLOW_COLON_in_parameterGroup4094 = frozenset([13, 15, 44, 49, 76, 85])
    FOLLOW_typeIdentifier_in_parameterGroup4098 = frozenset([1])
    FOLLOW_identifier_in_identifierList4129 = frozenset([1, 18])
    FOLLOW_COMMA_in_identifierList4133 = frozenset([44])
    FOLLOW_identifier_in_identifierList4135 = frozenset([1, 18])
    FOLLOW_constant_in_constList4167 = frozenset([1, 18])
    FOLLOW_COMMA_in_constList4171 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_constant_in_constList4173 = frozenset([1, 18])
    FOLLOW_typeIdentifier_in_resultType4205 = frozenset([1])
    FOLLOW_label_in_statement4222 = frozenset([17])
    FOLLOW_COLON_in_statement4224 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 78, 101, 102])
    FOLLOW_unlabelledStatement_in_statement4227 = frozenset([1])
    FOLLOW_unlabelledStatement_in_statement4235 = frozenset([1])
    FOLLOW_simpleStatement_in_unlabelledStatement4252 = frozenset([1])
    FOLLOW_structuredStatement_in_unlabelledStatement4260 = frozenset([1])
    FOLLOW_EXIT_in_exitStatement4277 = frozenset([1])
    FOLLOW_assignmentStatement_in_simpleStatement4297 = frozenset([1])
    FOLLOW_procedureStatement_in_simpleStatement4305 = frozenset([1])
    FOLLOW_exitStatement_in_simpleStatement4313 = frozenset([1])
    FOLLOW_gotoStatement_in_simpleStatement4321 = frozenset([1])
    FOLLOW_emptyStatement_in_simpleStatement4329 = frozenset([1])
    FOLLOW_variable_in_assignmentStatement4346 = frozenset([9])
    FOLLOW_ASSIGN_in_assignmentStatement4348 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_assignmentStatement4351 = frozenset([1])
    FOLLOW_AT_in_variable4370 = frozenset([44])
    FOLLOW_identifier_in_variable4373 = frozenset([1, 25, 52, 53, 69])
    FOLLOW_identifier_in_variable4384 = frozenset([1, 25, 52, 53, 69])
    FOLLOW_LBRACK_in_variable4403 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_variable4406 = frozenset([18, 73])
    FOLLOW_COMMA_in_variable4410 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_variable4413 = frozenset([18, 73])
    FOLLOW_RBRACK_in_variable4417 = frozenset([1, 25, 52, 53, 69])
    FOLLOW_LBRACK2_in_variable4428 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_variable4431 = frozenset([18, 74])
    FOLLOW_COMMA_in_variable4435 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_variable4438 = frozenset([18, 74])
    FOLLOW_RBRACK2_in_variable4442 = frozenset([1, 25, 52, 53, 69])
    FOLLOW_DOT_in_variable4453 = frozenset([44])
    FOLLOW_identifier_in_variable4456 = frozenset([1, 25, 52, 53, 69])
    FOLLOW_POINTER_in_variable4466 = frozenset([1, 25, 52, 53, 69])
    FOLLOW_simpleExpression_in_expression4493 = frozenset([1, 31, 41, 43, 48, 55, 57, 62])
    FOLLOW_EQUAL_in_expression4502 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_NOT_EQUAL_in_expression4507 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_LT_in_expression4512 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_LE_in_expression4517 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_GE_in_expression4522 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_GT_in_expression4527 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_IN_in_expression4532 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_simpleExpression_in_expression4536 = frozenset([1, 31, 41, 43, 48, 55, 57, 62])
    FOLLOW_term_in_simpleExpression4556 = frozenset([1, 58, 66, 68])
    FOLLOW_PLUS_in_simpleExpression4561 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_MINUS_in_simpleExpression4566 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_OR_in_simpleExpression4571 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_term_in_simpleExpression4575 = frozenset([1, 58, 66, 68])
    FOLLOW_signedFactor_in_term4593 = frozenset([1, 4, 23, 59, 83, 84])
    FOLLOW_STAR_in_term4598 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_SLASH_in_term4603 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_DIV_in_term4608 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_MOD_in_term4613 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_AND_in_term4618 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_signedFactor_in_term4622 = frozenset([1, 4, 23, 59, 83, 84])
    FOLLOW_PLUS_in_signedFactor4643 = frozenset([10, 16, 44, 52, 53, 56, 60, 61, 63, 64, 86])
    FOLLOW_MINUS_in_signedFactor4646 = frozenset([10, 16, 44, 52, 53, 56, 60, 61, 63, 64, 86])
    FOLLOW_factor_in_signedFactor4651 = frozenset([1])
    FOLLOW_variable_in_factor4668 = frozenset([1])
    FOLLOW_LPAREN_in_factor4676 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_factor4679 = frozenset([79])
    FOLLOW_RPAREN_in_factor4681 = frozenset([1])
    FOLLOW_functionDesignator_in_factor4690 = frozenset([1])
    FOLLOW_unsignedConstant_in_factor4698 = frozenset([1])
    FOLLOW_set_in_factor4706 = frozenset([1])
    FOLLOW_NOT_in_factor4714 = frozenset([10, 16, 44, 52, 53, 56, 60, 61, 63, 64, 86])
    FOLLOW_factor_in_factor4717 = frozenset([1])
    FOLLOW_unsignedNumber_in_unsignedConstant4734 = frozenset([1])
    FOLLOW_constantChr_in_unsignedConstant4742 = frozenset([1])
    FOLLOW_string_in_unsignedConstant4759 = frozenset([1])
    FOLLOW_NIL_in_unsignedConstant4767 = frozenset([1])
    FOLLOW_identifier_in_functionDesignator4786 = frozenset([56])
    FOLLOW_LPAREN_in_functionDesignator4788 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_parameterList_in_functionDesignator4792 = frozenset([79])
    FOLLOW_RPAREN_in_functionDesignator4794 = frozenset([1])
    FOLLOW_actualParameter_in_parameterList4828 = frozenset([1, 18])
    FOLLOW_COMMA_in_parameterList4832 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_actualParameter_in_parameterList4834 = frozenset([1, 18])
    FOLLOW_LBRACK_in_set4867 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 73, 86])
    FOLLOW_elementList_in_set4869 = frozenset([73])
    FOLLOW_RBRACK_in_set4871 = frozenset([1])
    FOLLOW_LBRACK2_in_set4890 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 74, 86])
    FOLLOW_elementList_in_set4892 = frozenset([74])
    FOLLOW_RBRACK2_in_set4894 = frozenset([1])
    FOLLOW_element_in_elementList4920 = frozenset([1, 18])
    FOLLOW_COMMA_in_elementList4924 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_element_in_elementList4927 = frozenset([1, 18])
    FOLLOW_expression_in_element4953 = frozenset([1, 26])
    FOLLOW_DOTDOT_in_element4957 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_element4960 = frozenset([1])
    FOLLOW_identifier_in_procedureStatement4982 = frozenset([1, 56])
    FOLLOW_LPAREN_in_procedureStatement4986 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_parameterList_in_procedureStatement4990 = frozenset([79])
    FOLLOW_RPAREN_in_procedureStatement4992 = frozenset([1])
    FOLLOW_expression_in_actualParameter5032 = frozenset([1, 17])
    FOLLOW_COLON_in_actualParameter5035 = frozenset([63])
    FOLLOW_unsignedInteger_in_actualParameter5037 = frozenset([1])
    FOLLOW_GOTO_in_gotoStatement5056 = frozenset([63])
    FOLLOW_label_in_gotoStatement5059 = frozenset([1])
    FOLLOW_compoundStatement_in_structuredStatement5107 = frozenset([1])
    FOLLOW_conditionalStatement_in_structuredStatement5115 = frozenset([1])
    FOLLOW_repetetiveStatement_in_structuredStatement5123 = frozenset([1])
    FOLLOW_withStatement_in_structuredStatement5131 = frozenset([1])
    FOLLOW_BEGIN_in_compoundStatement5148 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statements_in_compoundStatement5154 = frozenset([30])
    FOLLOW_END_in_compoundStatement5162 = frozenset([1])
    FOLLOW_statement_in_statements5197 = frozenset([1, 81])
    FOLLOW_SEMI_in_statements5201 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_statements5204 = frozenset([1, 81])
    FOLLOW_ifStatement_in_conditionalStatement5225 = frozenset([1])
    FOLLOW_caseStatement_in_conditionalStatement5233 = frozenset([1])
    FOLLOW_IF_in_ifStatement5250 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_ifStatement5253 = frozenset([88])
    FOLLOW_THEN_in_ifStatement5255 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_ifStatement5258 = frozenset([1, 29])
    FOLLOW_ELSE_in_ifStatement5288 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_ifStatement5291 = frozenset([1])
    FOLLOW_CASE_in_caseStatement5316 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_caseStatement5319 = frozenset([65])
    FOLLOW_OF_in_caseStatement5321 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_caseListElement_in_caseStatement5332 = frozenset([29, 30, 81])
    FOLLOW_SEMI_in_caseStatement5336 = frozenset([16, 44, 58, 63, 64, 68, 86])
    FOLLOW_caseListElement_in_caseStatement5339 = frozenset([29, 30, 81])
    FOLLOW_SEMI_in_caseStatement5344 = frozenset([29, 30])
    FOLLOW_ELSE_in_caseStatement5356 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statements_in_caseStatement5359 = frozenset([30])
    FOLLOW_END_in_caseStatement5370 = frozenset([1])
    FOLLOW_constList_in_caseListElement5388 = frozenset([17])
    FOLLOW_COLON_in_caseListElement5390 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_caseListElement5393 = frozenset([1])
    FOLLOW_whileStatement_in_repetetiveStatement5410 = frozenset([1])
    FOLLOW_repeatStatement_in_repetetiveStatement5418 = frozenset([1])
    FOLLOW_forStatement_in_repetetiveStatement5426 = frozenset([1])
    FOLLOW_WHILE_in_whileStatement5443 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_whileStatement5446 = frozenset([24])
    FOLLOW_DO_in_whileStatement5448 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_whileStatement5451 = frozenset([1])
    FOLLOW_REPEAT_in_repeatStatement5468 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statements_in_repeatStatement5471 = frozenset([94])
    FOLLOW_UNTIL_in_repeatStatement5473 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_expression_in_repeatStatement5476 = frozenset([1])
    FOLLOW_FOR_in_forStatement5493 = frozenset([44])
    FOLLOW_identifier_in_forStatement5496 = frozenset([9])
    FOLLOW_ASSIGN_in_forStatement5498 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_forList_in_forStatement5501 = frozenset([24])
    FOLLOW_DO_in_forStatement5503 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_forStatement5506 = frozenset([1])
    FOLLOW_initialValue_in_forList5523 = frozenset([27, 89])
    FOLLOW_TO_in_forList5526 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_DOWNTO_in_forList5531 = frozenset([10, 16, 44, 52, 53, 56, 58, 60, 61, 63, 64, 68, 86])
    FOLLOW_finalValue_in_forList5535 = frozenset([1])
    FOLLOW_expression_in_initialValue5552 = frozenset([1])
    FOLLOW_expression_in_finalValue5569 = frozenset([1])
    FOLLOW_WITH_in_withStatement5586 = frozenset([10, 44])
    FOLLOW_recordVariableList_in_withStatement5589 = frozenset([24])
    FOLLOW_DO_in_withStatement5591 = frozenset([10, 11, 14, 32, 37, 42, 44, 46, 63, 78, 101, 102])
    FOLLOW_statement_in_withStatement5594 = frozenset([1])
    FOLLOW_variable_in_recordVariableList5611 = frozenset([1, 18])
    FOLLOW_COMMA_in_recordVariableList5615 = frozenset([10, 44])
    FOLLOW_variable_in_recordVariableList5618 = frozenset([1, 18])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ryterLexer", ryterParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
