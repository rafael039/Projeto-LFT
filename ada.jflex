package cup.example;
import java_cup.runtime.ComplexSymbolFactory;
import java_cup.runtime.ComplexSymbolFactory.Location;
import java_cup.runtime.Symbol;
import java.lang.*;
import java.io.InputStreamReader;

%%

%class Lexer
%implements sym
%public
%unicode
%line
%column
%cup
%char
%{


    public Lexer(ComplexSymbolFactory sf, java.io.InputStream is){
		this(is);
        symbolFactory = sf;
    }
	public Lexer(ComplexSymbolFactory sf, java.io.Reader reader){
		this(reader);
        symbolFactory = sf;
    }

    private StringBuffer sb;
    private ComplexSymbolFactory symbolFactory = new ComplexSymbolFactory();
    private int csline,cscolumn;

    public Symbol symbol(String name, int code){
		return symbolFactory.newSymbol(name, code,
						new Location(yyline+1,yycolumn+1, yychar), // -yylength()
						new Location(yyline+1,yycolumn+yylength(), yychar+yylength())
				);
    }
    public Symbol symbol(String name, int code, String lexem){
	return symbolFactory.newSymbol(name, code,
						new Location(yyline+1, yycolumn +1, yychar),
						new Location(yyline+1,yycolumn+yylength(), yychar+yylength()), lexem);
    }

    protected void emit_warning(String message){
    	System.out.println("scanner warning: " + message + " at : 2 "+
    			(yyline+1) + " " + (yycolumn+1) + " " + yychar);
    }

    protected void emit_error(String message){
    	System.out.println("scanner error: " + message + " at : 2" +
    			(yyline+1) + " " + (yycolumn+1) + " " + yychar);
    }
%}

Newline    = \r | \n | \r\n
Whitespace = [ \t\f] | {Newline}
Number     = [0-9]+
Integer    = {Number}
character  = "'"  [^\r\n\t\f] "'"
string     = "\""  [^\r\n\t\f]* "\""
boolean    = "false" | "true"
float      = {Number} "." {Number}
Tipo       = "Integer" | "Character" | "String" | "Boolean" | "Float"
/* comments */
Comment            = "--" [^\r\n]* (\n | [^])
ident              = ([:jletter:] | "_" ) ([:jletterdigit:] | [:jletter:] | "_" )*

%eofval{
    return symbolFactory.newSymbol("EOF",sym.EOF);
%eofval}

%state CODESEG

%%

<YYINITIAL> {

  {Whitespace} {                              }
  "n"          { return symbolFactory.newSymbol("UMINUS", UMINUS); }
  "function"   { return symbolFactory.newSymbol("FUNCTION",FUNCTION); }
  "is"         { return symbolFactory.newSymbol("IS",IS); }
  "begin"      { return symbolFactory.newSymbol("BEGIN",BEGIN); }
  "end"        { return symbolFactory.newSymbol("END",END); }
  "if"         { return symbolFactory.newSymbol("IF",IF); }
  "then"       { return symbolFactory.newSymbol("THEN",THEN); }
  "else"       { return symbolFactory.newSymbol("ELSE",ELSE); }
  "for"        { return symbolFactory.newSymbol("FOR",FOR); }
  "loop"       { return symbolFactory.newSymbol("LOOP",LOOP); }
  "in"         { return symbolFactory.newSymbol("IN",IN); }
  "while"      { return symbolFactory.newSymbol("WHILE", WHILE); }
  "return"     { return symbolFactory.newSymbol("RETURN", RETURN); }
  "Puts"       { return symbolFactory.newSymbol("PUTS", PUTS); }
  "exit"       { return symbolFactory.newSymbol("EXIT", EXIT); }
  "true"       { return symbolFactory.newSymbol("TRUE", TRUE); }
  "false"      { return symbolFactory.newSymbol("FALSE", FALSE); }
  ".."         { return symbolFactory.newSymbol("PONTOS",PONTOS); }
  ","          { return symbolFactory.newSymbol("VIRGULA",VIRGULA); }
  ":"          { return symbolFactory.newSymbol("DOIS_PONTOS",DOIS_PONTOS); }
  "<"          { return symbolFactory.newSymbol("MENOR", MENOR); }
  ">"          { return symbolFactory.newSymbol("MAIOR", MAIOR); }
  "<="         { return symbolFactory.newSymbol("MENORIGUAL", MENORIGUAL); }
  ">="         { return symbolFactory.newSymbol("MAIORIGUAL", MAIORIGUAL); }
  ":="         { return symbolFactory.newSymbol("ATRIBUICAO",ATRIBUICAO); }
  "/="         { return symbolFactory.newSymbol("DIFERENTE",DIFERENTE); }
  "("          { return symbolFactory.newSymbol("LPAREN", LPAREN); }
  ")"          { return symbolFactory.newSymbol("RPAREN", RPAREN); }
  ";"          { return symbolFactory.newSymbol("SEMI", SEMI); }
  "+"          { return symbolFactory.newSymbol("PLUS", PLUS); }
  "-"          { return symbolFactory.newSymbol("MINUS", MINUS); }
  "*"          { return symbolFactory.newSymbol("TIMES", TIMES); }
  "/"          { return symbolFactory.newSymbol("BARRADIVISAO", BARRADIVISAO); }
  "'"          { return symbolFactory.newSymbol("ASPASSIMPLES", ASPASSIMPLES); }
  "\""       { return symbolFactory.newSymbol("ASPASDUPLAS", ASPASDUPLAS); }
  "="          { return symbolFactory.newSymbol("IGUALDADE", IGUALDADE); }
  "and"        { return symbolFactory.newSymbol("AND", AND); }
  "or"         { return symbolFactory.newSymbol("OR", OR); }
  "of"         { return symbolFactory.newSymbol("OF", OF); }
  "when"       { return symbolFactory.newSymbol("WHEN", WHEN); }
  "array"      { return symbolFactory.newSymbol("ARRAY", ARRAY); }
  {Comment}    {}
  {Tipo}       { return symbolFactory.newSymbol("TIPO", TIPO,yytext()); }
  {ident}      { return symbolFactory.newSymbol("IDENTIFICADOR", IDENTIFICADOR,yytext()); }
  {boolean}    { return symbolFactory.newSymbol("BOOLEAN",BOOLEAN,Boolean.getBoolean(yytext())); }
  {string}     { return symbolFactory.newSymbol("STRING",STRING,yytext()); }
  {character}  { return symbolFactory.newSymbol("CHARACTER", CHARACTER, yytext()); }
  {Integer}    { return symbolFactory.newSymbol("INTEGER", INTEGER, Integer.parseInt(yytext())); }
  {float}      { return symbolFactory.newSymbol("FLOAT", FLOAT, Double.parseDouble(yytext())); }
}



// error fallback
.|\n          { emit_warning("Unrecognized character '" +yytext()+"' -- ignored"); }
