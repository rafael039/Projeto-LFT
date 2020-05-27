
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ASSIGN BEGIN BOOLEAN CHAR COLON COMMA DIVIDE DOTDOT ELSE ELSIF END EQUAL FOR FUNCTION GREATERTHAN GREATERTHANEQUAL ID IF IN IS LESSTHAN LESSTHANEQUAL LOOP LPAREN MINUS NOTEQUAL NUMBER_EXPONENT NUMBER_FLOAT NUMBER_INT OF OR PLUS POWER PROCEDURE PUTS RETURN RPAREN SEMICOLON STRING THEN TIMES TYPE WHILEprogram : PROCEDURE ID IS decl body\n               | PROCEDURE ID IS body\n    subprogram : FUNCTION ID decl_param IS decl body\n                  | FUNCTION ID decl_param IS body\n     body : BEGIN cmd_loop END ID SEMICOLON\n     decl : var SEMICOLON decl_loop\n\t\t     | subprogram decl_loop\n     decl_loop : subprogram decl_loop\n                  | subprogram\n                  | var SEMICOLON decl_loop\n                  | var SEMICOLON\n     var : ID COMMA TYPE ASSIGN value\n\t\t\t| ID COLON TYPE\n\t\t\t| var_loop ID COLON TYPE\n\t\t\t| array\n     var_loop : var_loop ID COMMA\n               | ID COMMA\n     decl_param : LPAREN param RPAREN\n                  | LPAREN param RPAREN RETURN TYPE\n     param : ID COLON TYPE SEMICOLON param\n                | ID COLON TYPE SEMICOLON\n     function_call : ID LPAREN param_pass RPAREN SEMICOLON\n     function_call_exp : ID LPAREN param_pass RPAREN\n     param_pass : expression COMMA param_pass\n                   | expression\n     value : NUMBER_INT\n             | NUMBER_FLOAT\n             | NUMBER_EXPONENT\n             | BOOLEAN\n             | STRING\n             | CHAR\n     cmd : if_statement\n\t\t\t| repeat_statement\n\t\t\t| puts\n\t\t\t| return\n\t\t\t| assign\n\t\t\t| function_call\n    cmd_loop : cmd_loop cmd\n           | cmd\n     puts : PUTS LPAREN STRING RPAREN SEMICOLON\n     if_statement : IF expression THEN cmd_loop if_statement_loop\n     if_statement_loop : ELSIF expression cmd_loop if_statement_loop\n                          | ELSE expression cmd_loop END IF SEMICOLON\n                          | END IF SEMICOLON\n     repeat_statement : loop_statement\n                         | for_statement\n                         | while_statement\n     loop_statement : LOOP cmd_loop END LOOP\n     while_statement : WHILE expression NUMBER_INT LOOP cmd_loop END LOOP SEMICOLON\n     for_statement : FOR ID IN range LOOP cmd_loop END LOOP SEMICOLON\n     range : ID DOTDOT ID\n     assign : ID ASSIGN op_arithmetic SEMICOLON\n     expression : expression AND or_exp\n                   | or_exp\n     or_exp : or_exp OR comp_exp\n               | comp_exp\n     comp_exp : comp_exp comp_op op_arithmetic\n                 | op_arithmetic\n     comp_op : GREATERTHAN\n                | GREATERTHANEQUAL\n                | LESSTHAN\n                | LESSTHANEQUAL\n                | NOTEQUAL\n                | EQUAL\n     op_arithmetic : op_arithmetic PLUS factor\n                      | op_arithmetic MINUS factor\n                      | factor\n     factor : factor TIMES power\n               | factor DIVIDE power\n               | power\n     power : power POWER term\n              | term\n     term : ID\n             | function_call_exp\n             | LPAREN expression RPAREN\n     array : TYPE ID IS ARRAY LPAREN range RPAREN OF TYPE SEMICOLON\n     return : RETURN expression SEMICOLON\n    '
    
_lr_action_items = {'PROCEDURE':([0,],[2,]),'$end':([1,7,17,112,],[0,-2,-1,-5,]),'ID':([2,4,9,10,11,12,14,15,18,19,22,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,47,48,49,50,51,53,54,55,56,57,58,59,60,61,64,69,71,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,98,102,112,113,115,116,117,118,119,120,121,122,123,124,126,128,131,132,134,137,139,140,141,143,144,145,146,147,149,152,153,156,160,161,162,163,168,171,174,176,],[3,5,5,23,40,41,42,-17,5,5,23,-39,-32,-33,-34,-35,-36,-37,59,-45,-46,-47,59,23,65,59,5,74,-38,59,59,-54,-56,-58,-67,-70,-72,-73,-74,59,23,-16,104,23,59,59,59,-59,-60,-61,-62,-63,-64,59,59,59,59,59,59,-77,129,5,-5,-52,59,23,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,23,129,-4,-22,-41,59,59,-23,-40,155,23,23,-3,23,23,23,104,23,23,-44,-42,-49,-50,-43,]),'IS':([3,40,70,135,159,],[4,67,102,-18,-19,]),'BEGIN':([4,6,19,20,45,46,47,73,102,112,133,134,149,],[10,10,-9,-7,-6,-8,-11,-10,10,-5,10,-4,-3,]),'FUNCTION':([4,9,18,19,47,102,112,134,149,],[14,14,14,14,14,14,-5,-4,-3,]),'TYPE':([4,9,15,16,18,19,47,68,102,112,134,136,149,150,166,],[11,11,43,44,11,11,11,101,11,-5,-4,151,-3,159,172,]),'COMMA':([5,41,53,54,55,56,57,58,59,60,77,117,118,119,120,121,122,123,124,126,143,],[15,69,-54,-56,-58,-67,-70,-72,-73,-74,115,-53,-55,-57,-65,-66,-68,-69,-71,-75,-23,]),'COLON':([5,41,104,],[16,68,136,]),'SEMICOLON':([8,13,21,44,53,54,55,56,57,58,59,60,63,74,75,101,105,106,107,108,109,110,111,114,117,118,119,120,121,122,123,124,126,127,143,151,154,165,170,172,173,175,],[18,-15,47,-13,-54,-56,-58,-67,-70,-72,-73,-74,96,112,113,-14,-12,-26,-27,-28,-29,-30,-31,137,-53,-55,-57,-65,-66,-68,-69,-71,-75,144,-23,160,163,171,174,175,176,-76,]),'IF':([10,22,24,25,26,27,28,29,30,32,33,34,37,49,53,54,55,56,57,58,59,60,64,78,96,113,116,117,118,119,120,121,122,123,124,126,128,131,137,139,142,143,144,146,147,152,153,156,161,162,163,168,169,171,174,176,],[31,31,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,31,-38,-54,-56,-58,-67,-70,-72,-73,-74,31,31,-77,-52,31,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,31,-22,-41,154,-23,-40,31,31,31,31,31,31,31,-44,-42,173,-49,-50,-43,]),'PUTS':([10,22,24,25,26,27,28,29,30,32,33,34,37,49,53,54,55,56,57,58,59,60,64,78,96,113,116,117,118,119,120,121,122,123,124,126,128,131,137,139,143,144,146,147,152,153,156,161,162,163,168,171,174,176,],[35,35,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,35,-38,-54,-56,-58,-67,-70,-72,-73,-74,35,35,-77,-52,35,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,35,-22,-41,-23,-40,35,35,35,35,35,35,35,-44,-42,-49,-50,-43,]),'RETURN':([10,22,24,25,26,27,28,29,30,32,33,34,37,49,53,54,55,56,57,58,59,60,64,78,96,113,116,117,118,119,120,121,122,123,124,126,128,131,135,137,139,143,144,146,147,152,153,156,161,162,163,168,171,174,176,],[36,36,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,36,-38,-54,-56,-58,-67,-70,-72,-73,-74,36,36,-77,-52,36,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,36,150,-22,-41,-23,-40,36,36,36,36,36,36,36,-44,-42,-49,-50,-43,]),'LOOP':([10,22,24,25,26,27,28,29,30,32,33,34,37,49,53,54,55,56,57,58,59,60,64,78,96,97,99,113,116,117,118,119,120,121,122,123,124,126,128,130,131,137,139,143,144,146,147,152,153,155,156,157,161,162,163,164,168,171,174,176,],[37,37,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,37,-38,-54,-56,-58,-67,-70,-72,-73,-74,37,37,-77,128,131,-52,37,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,146,37,-22,-41,-23,-40,37,37,37,37,-51,37,165,37,37,-44,170,-42,-49,-50,-43,]),'FOR':([10,22,24,25,26,27,28,29,30,32,33,34,37,49,53,54,55,56,57,58,59,60,64,78,96,113,116,117,118,119,120,121,122,123,124,126,128,131,137,139,143,144,146,147,152,153,156,161,162,163,168,171,174,176,],[38,38,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,38,-38,-54,-56,-58,-67,-70,-72,-73,-74,38,38,-77,-52,38,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,38,-22,-41,-23,-40,38,38,38,38,38,38,38,-44,-42,-49,-50,-43,]),'WHILE':([10,22,24,25,26,27,28,29,30,32,33,34,37,49,53,54,55,56,57,58,59,60,64,78,96,113,116,117,118,119,120,121,122,123,124,126,128,131,137,139,143,144,146,147,152,153,156,161,162,163,168,171,174,176,],[39,39,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,39,-38,-54,-56,-58,-67,-70,-72,-73,-74,39,39,-77,-52,39,-53,-55,-57,-65,-66,-68,-69,-71,-75,-48,39,-22,-41,-23,-40,39,39,39,39,39,39,39,-44,-42,-49,-50,-43,]),'END':([22,24,25,26,27,28,29,30,32,33,34,49,64,96,113,116,128,137,139,144,147,156,161,162,163,168,171,174,176,],[48,-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,-38,97,-77,-52,142,-48,-22,-41,-40,157,164,142,169,-44,-42,-49,-50,-43,]),'ASSIGN':([23,43,],[50,72,]),'LPAREN':([23,31,35,36,39,42,50,51,59,61,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,100,115,140,141,],[51,61,62,61,61,71,61,61,93,61,61,61,61,-59,-60,-61,-62,-63,-64,61,61,61,61,61,61,132,61,61,61,]),'ELSIF':([24,25,26,27,28,29,30,32,33,34,49,96,113,116,128,137,139,144,161,163,168,171,174,176,],[-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,-38,-77,-52,140,-48,-22,-41,-40,140,-44,-42,-49,-50,-43,]),'ELSE':([24,25,26,27,28,29,30,32,33,34,49,96,113,116,128,137,139,144,161,163,168,171,174,176,],[-39,-32,-33,-34,-35,-36,-37,-45,-46,-47,-38,-77,-52,141,-48,-22,-41,-40,141,-44,-42,-49,-50,-43,]),'THEN':([52,53,54,55,56,57,58,59,60,117,118,119,120,121,122,123,124,126,143,],[78,-54,-56,-58,-67,-70,-72,-73,-74,-53,-55,-57,-65,-66,-68,-69,-71,-75,-23,]),'AND':([52,53,54,55,56,57,58,59,60,63,66,77,94,117,118,119,120,121,122,123,124,126,143,152,153,],[79,-54,-56,-58,-67,-70,-72,-73,-74,79,79,79,79,-53,-55,-57,-65,-66,-68,-69,-71,-75,-23,79,79,]),'NUMBER_INT':([53,54,55,56,57,58,59,60,66,72,117,118,119,120,121,122,123,124,126,143,],[-54,-56,-58,-67,-70,-72,-73,-74,99,106,-53,-55,-57,-65,-66,-68,-69,-71,-75,-23,]),'RPAREN':([53,54,55,56,57,58,59,60,76,77,94,95,103,117,118,119,120,121,122,123,124,125,126,138,143,148,155,160,167,],[-54,-56,-58,-67,-70,-72,-73,-74,114,-25,126,127,135,-53,-55,-57,-65,-66,-68,-69,-71,143,-75,-24,-23,158,-51,-21,-20,]),'OR':([53,54,55,56,57,58,59,60,117,118,119,120,121,122,123,124,126,143,],[80,-56,-58,-67,-70,-72,-73,-74,80,-55,-57,-65,-66,-68,-69,-71,-75,-23,]),'GREATERTHAN':([54,55,56,57,58,59,60,118,119,120,121,122,123,124,126,143,],[82,-58,-67,-70,-72,-73,-74,82,-57,-65,-66,-68,-69,-71,-75,-23,]),'GREATERTHANEQUAL':([54,55,56,57,58,59,60,118,119,120,121,122,123,124,126,143,],[83,-58,-67,-70,-72,-73,-74,83,-57,-65,-66,-68,-69,-71,-75,-23,]),'LESSTHAN':([54,55,56,57,58,59,60,118,119,120,121,122,123,124,126,143,],[84,-58,-67,-70,-72,-73,-74,84,-57,-65,-66,-68,-69,-71,-75,-23,]),'LESSTHANEQUAL':([54,55,56,57,58,59,60,118,119,120,121,122,123,124,126,143,],[85,-58,-67,-70,-72,-73,-74,85,-57,-65,-66,-68,-69,-71,-75,-23,]),'NOTEQUAL':([54,55,56,57,58,59,60,118,119,120,121,122,123,124,126,143,],[86,-58,-67,-70,-72,-73,-74,86,-57,-65,-66,-68,-69,-71,-75,-23,]),'EQUAL':([54,55,56,57,58,59,60,118,119,120,121,122,123,124,126,143,],[87,-58,-67,-70,-72,-73,-74,87,-57,-65,-66,-68,-69,-71,-75,-23,]),'PLUS':([55,56,57,58,59,60,75,119,120,121,122,123,124,126,143,],[88,-67,-70,-72,-73,-74,88,88,-65,-66,-68,-69,-71,-75,-23,]),'MINUS':([55,56,57,58,59,60,75,119,120,121,122,123,124,126,143,],[89,-67,-70,-72,-73,-74,89,89,-65,-66,-68,-69,-71,-75,-23,]),'TIMES':([56,57,58,59,60,120,121,122,123,124,126,143,],[90,-70,-72,-73,-74,90,90,-68,-69,-71,-75,-23,]),'DIVIDE':([56,57,58,59,60,120,121,122,123,124,126,143,],[91,-70,-72,-73,-74,91,91,-68,-69,-71,-75,-23,]),'POWER':([57,58,59,60,122,123,124,126,143,],[92,-72,-73,-74,92,92,-71,-75,-23,]),'STRING':([62,72,],[95,110,]),'IN':([65,],[98,]),'ARRAY':([67,],[100,]),'NUMBER_FLOAT':([72,],[107,]),'NUMBER_EXPONENT':([72,],[108,]),'BOOLEAN':([72,],[109,]),'CHAR':([72,],[111,]),'DOTDOT':([129,],[145,]),'OF':([158,],[166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decl':([4,102,],[6,133,]),'body':([4,6,102,133,],[7,17,134,149,]),'var':([4,9,18,19,47,102,],[8,21,21,21,21,8,]),'subprogram':([4,9,18,19,47,102,],[9,19,19,19,19,9,]),'var_loop':([4,9,18,19,47,102,],[12,12,12,12,12,12,]),'array':([4,9,18,19,47,102,],[13,13,13,13,13,13,]),'decl_loop':([9,18,19,47,],[20,45,46,73,]),'cmd_loop':([10,37,78,131,146,152,153,],[22,64,116,147,156,161,162,]),'cmd':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[24,49,24,49,24,49,24,24,49,24,24,49,49,49,]),'if_statement':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'repeat_statement':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'puts':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'return':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'assign':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'function_call':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'loop_statement':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'for_statement':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'while_statement':([10,22,37,64,78,116,131,146,147,152,153,156,161,162,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'expression':([31,36,39,51,61,93,115,140,141,],[52,63,66,77,94,77,77,152,153,]),'or_exp':([31,36,39,51,61,79,93,115,140,141,],[53,53,53,53,53,117,53,53,53,53,]),'comp_exp':([31,36,39,51,61,79,80,93,115,140,141,],[54,54,54,54,54,54,118,54,54,54,54,]),'op_arithmetic':([31,36,39,50,51,61,79,80,81,93,115,140,141,],[55,55,55,75,55,55,55,55,119,55,55,55,55,]),'factor':([31,36,39,50,51,61,79,80,81,88,89,93,115,140,141,],[56,56,56,56,56,56,56,56,56,120,121,56,56,56,56,]),'power':([31,36,39,50,51,61,79,80,81,88,89,90,91,93,115,140,141,],[57,57,57,57,57,57,57,57,57,57,57,122,123,57,57,57,57,]),'term':([31,36,39,50,51,61,79,80,81,88,89,90,91,92,93,115,140,141,],[58,58,58,58,58,58,58,58,58,58,58,58,58,124,58,58,58,58,]),'function_call_exp':([31,36,39,50,51,61,79,80,81,88,89,90,91,92,93,115,140,141,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'decl_param':([42,],[70,]),'param_pass':([51,93,115,],[76,125,138,]),'comp_op':([54,118,],[81,81,]),'param':([71,160,],[103,167,]),'value':([72,],[105,]),'range':([98,132,],[130,148,]),'if_statement_loop':([116,161,],[139,168,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROCEDURE ID IS decl body','program',5,'p_program','parser.py',9),
  ('program -> PROCEDURE ID IS body','program',4,'p_program','parser.py',10),
  ('subprogram -> FUNCTION ID decl_param IS decl body','subprogram',6,'p_subprogram','parser.py',14),
  ('subprogram -> FUNCTION ID decl_param IS body','subprogram',5,'p_subprogram','parser.py',15),
  ('body -> BEGIN cmd_loop END ID SEMICOLON','body',5,'p_body','parser.py',19),
  ('decl -> var SEMICOLON decl_loop','decl',3,'p_decl','parser.py',23),
  ('decl -> subprogram decl_loop','decl',2,'p_decl','parser.py',24),
  ('decl_loop -> subprogram decl_loop','decl_loop',2,'p_decl_loop','parser.py',28),
  ('decl_loop -> subprogram','decl_loop',1,'p_decl_loop','parser.py',29),
  ('decl_loop -> var SEMICOLON decl_loop','decl_loop',3,'p_decl_loop','parser.py',30),
  ('decl_loop -> var SEMICOLON','decl_loop',2,'p_decl_loop','parser.py',31),
  ('var -> ID COMMA TYPE ASSIGN value','var',5,'p_var','parser.py',35),
  ('var -> ID COLON TYPE','var',3,'p_var','parser.py',36),
  ('var -> var_loop ID COLON TYPE','var',4,'p_var','parser.py',37),
  ('var -> array','var',1,'p_var','parser.py',38),
  ('var_loop -> var_loop ID COMMA','var_loop',3,'p_var_loop','parser.py',42),
  ('var_loop -> ID COMMA','var_loop',2,'p_var_loop','parser.py',43),
  ('decl_param -> LPAREN param RPAREN','decl_param',3,'p_decl_param','parser.py',47),
  ('decl_param -> LPAREN param RPAREN RETURN TYPE','decl_param',5,'p_decl_param','parser.py',48),
  ('param -> ID COLON TYPE SEMICOLON param','param',5,'p_param','parser.py',52),
  ('param -> ID COLON TYPE SEMICOLON','param',4,'p_param','parser.py',53),
  ('function_call -> ID LPAREN param_pass RPAREN SEMICOLON','function_call',5,'p_function_call','parser.py',62),
  ('function_call_exp -> ID LPAREN param_pass RPAREN','function_call_exp',4,'p_function_call_exp','parser.py',66),
  ('param_pass -> expression COMMA param_pass','param_pass',3,'p_param_pass','parser.py',70),
  ('param_pass -> expression','param_pass',1,'p_param_pass','parser.py',71),
  ('value -> NUMBER_INT','value',1,'p_value','parser.py',82),
  ('value -> NUMBER_FLOAT','value',1,'p_value','parser.py',83),
  ('value -> NUMBER_EXPONENT','value',1,'p_value','parser.py',84),
  ('value -> BOOLEAN','value',1,'p_value','parser.py',85),
  ('value -> STRING','value',1,'p_value','parser.py',86),
  ('value -> CHAR','value',1,'p_value','parser.py',87),
  ('cmd -> if_statement','cmd',1,'p_cmd','parser.py',91),
  ('cmd -> repeat_statement','cmd',1,'p_cmd','parser.py',92),
  ('cmd -> puts','cmd',1,'p_cmd','parser.py',93),
  ('cmd -> return','cmd',1,'p_cmd','parser.py',94),
  ('cmd -> assign','cmd',1,'p_cmd','parser.py',95),
  ('cmd -> function_call','cmd',1,'p_cmd','parser.py',96),
  ('cmd_loop -> cmd_loop cmd','cmd_loop',2,'p_cmd_loop','parser.py',100),
  ('cmd_loop -> cmd','cmd_loop',1,'p_cmd_loop','parser.py',101),
  ('puts -> PUTS LPAREN STRING RPAREN SEMICOLON','puts',5,'p_puts','parser.py',105),
  ('if_statement -> IF expression THEN cmd_loop if_statement_loop','if_statement',5,'p_if_statement','parser.py',109),
  ('if_statement_loop -> ELSIF expression cmd_loop if_statement_loop','if_statement_loop',4,'p_if_statement_loop','parser.py',113),
  ('if_statement_loop -> ELSE expression cmd_loop END IF SEMICOLON','if_statement_loop',6,'p_if_statement_loop','parser.py',114),
  ('if_statement_loop -> END IF SEMICOLON','if_statement_loop',3,'p_if_statement_loop','parser.py',115),
  ('repeat_statement -> loop_statement','repeat_statement',1,'p_repeat_statement','parser.py',119),
  ('repeat_statement -> for_statement','repeat_statement',1,'p_repeat_statement','parser.py',120),
  ('repeat_statement -> while_statement','repeat_statement',1,'p_repeat_statement','parser.py',121),
  ('loop_statement -> LOOP cmd_loop END LOOP','loop_statement',4,'p_loop_statement','parser.py',125),
  ('while_statement -> WHILE expression NUMBER_INT LOOP cmd_loop END LOOP SEMICOLON','while_statement',8,'p_while_statement','parser.py',129),
  ('for_statement -> FOR ID IN range LOOP cmd_loop END LOOP SEMICOLON','for_statement',9,'p_for_statement','parser.py',133),
  ('range -> ID DOTDOT ID','range',3,'p_range','parser.py',137),
  ('assign -> ID ASSIGN op_arithmetic SEMICOLON','assign',4,'p_assign','parser.py',141),
  ('expression -> expression AND or_exp','expression',3,'p_expression','parser.py',145),
  ('expression -> or_exp','expression',1,'p_expression','parser.py',146),
  ('or_exp -> or_exp OR comp_exp','or_exp',3,'p_or_exp','parser.py',150),
  ('or_exp -> comp_exp','or_exp',1,'p_or_exp','parser.py',151),
  ('comp_exp -> comp_exp comp_op op_arithmetic','comp_exp',3,'p_comp_exp','parser.py',155),
  ('comp_exp -> op_arithmetic','comp_exp',1,'p_comp_exp','parser.py',156),
  ('comp_op -> GREATERTHAN','comp_op',1,'p_comp_op','parser.py',165),
  ('comp_op -> GREATERTHANEQUAL','comp_op',1,'p_comp_op','parser.py',166),
  ('comp_op -> LESSTHAN','comp_op',1,'p_comp_op','parser.py',167),
  ('comp_op -> LESSTHANEQUAL','comp_op',1,'p_comp_op','parser.py',168),
  ('comp_op -> NOTEQUAL','comp_op',1,'p_comp_op','parser.py',169),
  ('comp_op -> EQUAL','comp_op',1,'p_comp_op','parser.py',170),
  ('op_arithmetic -> op_arithmetic PLUS factor','op_arithmetic',3,'p_op_arithmetic','parser.py',174),
  ('op_arithmetic -> op_arithmetic MINUS factor','op_arithmetic',3,'p_op_arithmetic','parser.py',175),
  ('op_arithmetic -> factor','op_arithmetic',1,'p_op_arithmetic','parser.py',176),
  ('factor -> factor TIMES power','factor',3,'p_factor','parser.py',180),
  ('factor -> factor DIVIDE power','factor',3,'p_factor','parser.py',181),
  ('factor -> power','factor',1,'p_factor','parser.py',182),
  ('power -> power POWER term','power',3,'p_power','parser.py',186),
  ('power -> term','power',1,'p_power','parser.py',187),
  ('term -> ID','term',1,'p_term','parser.py',197),
  ('term -> function_call_exp','term',1,'p_term','parser.py',198),
  ('term -> LPAREN expression RPAREN','term',3,'p_term','parser.py',199),
  ('array -> TYPE ID IS ARRAY LPAREN range RPAREN OF TYPE SEMICOLON','array',10,'p_array','parser.py',203),
  ('return -> RETURN expression SEMICOLON','return',3,'p_return','parser.py',207),
]
