grammar NodeCode;

WS: [ \n\t\r]+ -> skip;
program: assignment*;

qualifier: 'input' | 'output';

assignment: qualifier? IDENTIFIER ('=' expr)?;

expr:
	IDENTIFIER										# var
	| NUMBER										# num
	| '(' expr ')'									# parenth
	| '!' expr										# lnot
	| '-' expr										# neg
	| IDENTIFIER '(' (expr (',' expr)*)? ','? ')'	# func
	| <assoc = right> expr op = ('==' | '!=') expr	# eq_ne
	| <assoc = right> expr '**' expr				# pow
	| expr op = ('*' | '/' | '%') expr				# mul_div_mod
	| expr op = ('+' | '-') expr					# add_sub
	| expr op = ('<' | '>' | '<=' | '>=') expr		# lt_gt_le_ge;

IDENTIFIER: [$a-zA-Z.\-_][$a-zA-Z.\-_0-9]*;
NUMBER: ([1-9][0-9]* | '0') ('.' [0-9]*)?
	| ([1-9][0-9]* | '0')? ('.' [0-9]*);