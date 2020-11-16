
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTGTLEGENEQEQleft+-left*/leftDOTADDDOTSUBleftDOTMULDOTDIVrightUMINUSleft\'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GE GT ID IF INT LE LT MULASSIGN NEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction instructions : instruction instruction : assignment \';\'\n                   | control_instruction\n                   | print\n                   | block\n    print : PRINT expr \';\'\n             | PRINT boolean \';\'\n             | PRINT matrix_row \';\'\n    control_instruction : if\n                           | while\n                           | for\n                           | break\n                           | continue\n                           | return\n    break : BREAK \';\'continue : CONTINUE \';\'return : RETURN expr \';\'for : FOR ID \'=\' range instructionrange : expr \':\' expr while : WHILE \'(\' boolean \')\' instruction if : IF \'(\' boolean \')\' instruction\n          | IF \'(\' boolean \')\' instruction else\n    else : ELSE instruction\n    block : \'{\' instructions \'}\' assignment : id_part \'=\' expr\n                  | id_part \'=\' boolean\n                  | id_part ADDASSIGN expr\n                  | id_part SUBASSIGN expr\n                  | id_part MULASSIGN expr\n                  | id_part DIVASSIGN expr\n    id_part : ID \'[\' matrix_row \']\'\n               | ID\n    expr : \'(\' expr \')\'\n    boolean : expr LT expr\n               | expr GT expr\n               | expr LE expr\n               | expr GE expr\n               | expr NEQ expr\n               | expr EQ expr\n    expr : expr "\'"\n    expr : \'-\' expr %prec UMINUSexpr : expr DOTADD expr\n            | expr DOTSUB expr\n            | expr DOTMUL expr\n            | expr DOTDIV expr\n    expr : expr \'+\' expr\n            | expr \'-\' expr\n            | expr \'*\' expr\n            | expr \'/\' expr\n    expr : ID\n            | STRING\n            | FLOAT\n            | INT\n    expr : EYE \'(\' expr \')\'\n              | ZEROS \'(\' expr \')\'\n              | ONES \'(\' expr \')\'\n              | \'[\' matrix_rows \']\'\n    matrix_rows : matrix_rows \',\' \'[\' matrix_row \']\'\n                    | \'[\' matrix_row \']\'\n    matrix_row : matrix_row \',\' expr\n                   | expr\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,6,7,8,10,11,12,13,14,15,25,26,50,51,59,75,76,85,92,125,126,127,130,134,],[-3,0,-1,-2,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,-4,-6,-19,-20,-10,-11,-12,-28,-21,-25,-24,-22,-26,-27,]),'PRINT':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[16,16,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,16,-4,-6,-54,-55,-56,-57,16,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,16,16,16,-58,-59,-60,-25,-24,-22,-26,16,-23,-27,]),'{':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[17,17,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,17,-4,-6,-54,-55,-56,-57,17,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,17,17,17,-58,-59,-60,-25,-24,-22,-26,17,-23,-27,]),'ID':([0,3,4,6,7,8,10,11,12,13,14,15,16,17,21,24,25,26,27,28,29,30,31,35,36,37,38,39,40,45,46,47,48,50,51,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,82,83,85,91,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,124,125,126,127,128,130,131,132,134,],[18,18,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,37,18,49,37,-4,-6,37,37,37,37,37,37,37,-54,-55,-56,-57,18,37,37,37,-19,-20,-10,-44,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-11,-12,37,-45,37,37,37,37,-28,37,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,18,18,18,-58,-59,-60,37,-25,-24,-22,37,-26,18,-23,-27,]),'IF':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[19,19,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,19,-4,-6,-54,-55,-56,-57,19,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,19,19,19,-58,-59,-60,-25,-24,-22,-26,19,-23,-27,]),'WHILE':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[20,20,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,20,-4,-6,-54,-55,-56,-57,20,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,20,20,20,-58,-59,-60,-25,-24,-22,-26,20,-23,-27,]),'FOR':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[21,21,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,21,-4,-6,-54,-55,-56,-57,21,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,21,21,21,-58,-59,-60,-25,-24,-22,-26,21,-23,-27,]),'BREAK':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[22,22,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,22,-4,-6,-54,-55,-56,-57,22,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,22,22,22,-58,-59,-60,-25,-24,-22,-26,22,-23,-27,]),'CONTINUE':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[23,23,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,23,-4,-6,-54,-55,-56,-57,23,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,23,23,23,-58,-59,-60,-25,-24,-22,-26,23,-23,-27,]),'RETURN':([0,3,4,6,7,8,10,11,12,13,14,15,17,25,26,37,38,39,40,45,50,51,59,60,75,76,79,85,92,93,94,95,96,97,98,99,100,108,113,116,117,118,120,121,122,125,126,127,130,131,132,134,],[24,24,-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,24,-4,-6,-54,-55,-56,-57,24,-19,-20,-10,-44,-11,-12,-45,-28,-21,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,24,24,24,-58,-59,-60,-25,-24,-22,-26,24,-23,-27,]),'}':([4,6,7,8,10,11,12,13,14,15,25,26,45,50,51,59,75,76,85,92,125,126,127,130,134,],[-5,-7,-8,-9,-13,-14,-15,-16,-17,-18,-4,-6,85,-19,-20,-10,-11,-12,-28,-21,-25,-24,-22,-26,-27,]),';':([5,22,23,32,33,34,37,38,39,40,52,53,54,55,56,57,58,60,79,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,113,120,121,122,],[26,50,51,59,75,76,-54,-55,-56,-57,92,-29,-30,-31,-32,-33,-34,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-38,-39,-40,-41,-42,-43,-64,-37,-61,-58,-59,-60,]),'ELSE':([6,7,8,10,11,12,13,14,15,26,50,51,59,75,76,85,92,125,126,127,130,134,],[-7,-8,-9,-13,-14,-15,-16,-17,-18,-6,-19,-20,-10,-11,-12,-28,-21,131,-24,-22,-26,-27,]),'=':([9,18,49,115,],[27,-36,91,-35,]),'ADDASSIGN':([9,18,115,],[28,-36,-35,]),'SUBASSIGN':([9,18,115,],[29,-36,-35,]),'MULASSIGN':([9,18,115,],[30,-36,-35,]),'DIVASSIGN':([9,18,115,],[31,-36,-35,]),'(':([16,19,20,24,27,28,29,30,31,35,36,41,42,43,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[35,47,48,35,35,35,35,35,35,35,35,80,81,82,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'-':([16,24,27,28,29,30,31,32,35,36,37,38,39,40,46,47,48,52,53,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,80,81,82,83,87,89,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,124,128,132,],[36,36,36,36,36,36,36,66,36,36,-54,-55,-56,-57,36,36,36,66,66,66,66,66,66,-44,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,66,-45,36,36,36,36,66,66,36,-46,-47,-48,-49,-50,-51,-52,-53,66,66,66,66,66,66,66,-37,66,66,66,-61,66,-58,-59,-60,36,36,66,]),'STRING':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FLOAT':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'INT':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'EYE':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'ZEROS':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'ONES':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'[':([16,18,24,27,28,29,30,31,35,36,44,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,114,124,128,],[44,46,44,44,44,44,44,44,44,44,83,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,124,44,44,]),"'":([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[60,-54,-55,-56,-57,60,60,60,60,60,60,-44,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-37,60,60,60,-61,60,-58,-59,-60,60,]),'DOTADD':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[61,-54,-55,-56,-57,61,61,61,61,61,61,-44,61,-45,61,61,-46,-47,-48,-49,61,61,61,61,61,61,61,61,61,61,61,-37,61,61,61,-61,61,-58,-59,-60,61,]),'DOTSUB':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[62,-54,-55,-56,-57,62,62,62,62,62,62,-44,62,-45,62,62,-46,-47,-48,-49,62,62,62,62,62,62,62,62,62,62,62,-37,62,62,62,-61,62,-58,-59,-60,62,]),'DOTMUL':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[63,-54,-55,-56,-57,63,63,63,63,63,63,-44,63,-45,63,63,63,63,-48,-49,63,63,63,63,63,63,63,63,63,63,63,-37,63,63,63,-61,63,-58,-59,-60,63,]),'DOTDIV':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[64,-54,-55,-56,-57,64,64,64,64,64,64,-44,64,-45,64,64,64,64,-48,-49,64,64,64,64,64,64,64,64,64,64,64,-37,64,64,64,-61,64,-58,-59,-60,64,]),'+':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[65,-54,-55,-56,-57,65,65,65,65,65,65,-44,65,-45,65,65,-46,-47,-48,-49,-50,-51,-52,-53,65,65,65,65,65,65,65,-37,65,65,65,-61,65,-58,-59,-60,65,]),'*':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[67,-54,-55,-56,-57,67,67,67,67,67,67,-44,67,-45,67,67,-46,-47,-48,-49,67,67,-52,-53,67,67,67,67,67,67,67,-37,67,67,67,-61,67,-58,-59,-60,67,]),'/':([32,37,38,39,40,52,53,55,56,57,58,60,78,79,87,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,119,120,121,122,132,],[68,-54,-55,-56,-57,68,68,68,68,68,68,-44,68,-45,68,68,-46,-47,-48,-49,68,68,-52,-53,68,68,68,68,68,68,68,-37,68,68,68,-61,68,-58,-59,-60,68,]),'LT':([32,37,38,39,40,53,60,79,89,93,94,95,96,97,98,99,100,108,113,120,121,122,],[69,-54,-55,-56,-57,69,-44,-45,69,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,-58,-59,-60,]),'GT':([32,37,38,39,40,53,60,79,89,93,94,95,96,97,98,99,100,108,113,120,121,122,],[70,-54,-55,-56,-57,70,-44,-45,70,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,-58,-59,-60,]),'LE':([32,37,38,39,40,53,60,79,89,93,94,95,96,97,98,99,100,108,113,120,121,122,],[71,-54,-55,-56,-57,71,-44,-45,71,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,-58,-59,-60,]),'GE':([32,37,38,39,40,53,60,79,89,93,94,95,96,97,98,99,100,108,113,120,121,122,],[72,-54,-55,-56,-57,72,-44,-45,72,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,-58,-59,-60,]),'NEQ':([32,37,38,39,40,53,60,79,89,93,94,95,96,97,98,99,100,108,113,120,121,122,],[73,-54,-55,-56,-57,73,-44,-45,73,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,-58,-59,-60,]),'EQ':([32,37,38,39,40,53,60,79,89,93,94,95,96,97,98,99,100,108,113,120,121,122,],[74,-54,-55,-56,-57,74,-44,-45,74,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,-58,-59,-60,]),',':([32,34,37,38,39,40,60,79,84,86,87,93,94,95,96,97,98,99,100,107,108,112,113,120,121,122,123,129,133,],[-65,77,-54,-55,-56,-57,-44,-45,114,77,-65,-46,-47,-48,-49,-50,-51,-52,-53,-64,-37,77,-61,-58,-59,-60,-63,77,-62,]),')':([37,38,39,40,60,78,79,88,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,109,110,111,113,120,121,122,],[-54,-55,-56,-57,-44,108,-45,116,117,-46,-47,-48,-49,-50,-51,-52,-53,-38,-39,-40,-41,-42,-43,-37,120,121,122,-61,-58,-59,-60,]),']':([37,38,39,40,60,79,84,86,87,93,94,95,96,97,98,99,100,107,108,112,113,120,121,122,123,129,133,],[-54,-55,-56,-57,-44,-45,113,115,-65,-46,-47,-48,-49,-50,-51,-52,-53,-64,-37,123,-61,-58,-59,-60,-63,133,-62,]),':':([37,38,39,40,60,79,93,94,95,96,97,98,99,100,108,113,119,120,121,122,],[-54,-55,-56,-57,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-37,-61,128,-58,-59,-60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,17,],[3,45,]),'instruction':([0,3,17,45,116,117,118,131,],[4,25,4,25,125,126,127,134,]),'assignment':([0,3,17,45,116,117,118,131,],[5,5,5,5,5,5,5,5,]),'control_instruction':([0,3,17,45,116,117,118,131,],[6,6,6,6,6,6,6,6,]),'print':([0,3,17,45,116,117,118,131,],[7,7,7,7,7,7,7,7,]),'block':([0,3,17,45,116,117,118,131,],[8,8,8,8,8,8,8,8,]),'id_part':([0,3,17,45,116,117,118,131,],[9,9,9,9,9,9,9,9,]),'if':([0,3,17,45,116,117,118,131,],[10,10,10,10,10,10,10,10,]),'while':([0,3,17,45,116,117,118,131,],[11,11,11,11,11,11,11,11,]),'for':([0,3,17,45,116,117,118,131,],[12,12,12,12,12,12,12,12,]),'break':([0,3,17,45,116,117,118,131,],[13,13,13,13,13,13,13,13,]),'continue':([0,3,17,45,116,117,118,131,],[14,14,14,14,14,14,14,14,]),'return':([0,3,17,45,116,117,118,131,],[15,15,15,15,15,15,15,15,]),'expr':([16,24,27,28,29,30,31,35,36,46,47,48,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,80,81,82,83,91,124,128,],[32,52,53,55,56,57,58,78,79,87,89,89,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,87,119,87,132,]),'boolean':([16,27,47,48,],[33,54,88,90,]),'matrix_row':([16,46,83,124,],[34,86,112,129,]),'matrix_rows':([44,],[84,]),'range':([91,],[118,]),'else':([125,],[130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',28),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',32),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',36),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_1','Mparser.py',39),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',43),
  ('instruction -> assignment ;','instruction',2,'p_instruction','Mparser.py',46),
  ('instruction -> control_instruction','instruction',1,'p_instruction','Mparser.py',47),
  ('instruction -> print','instruction',1,'p_instruction','Mparser.py',48),
  ('instruction -> block','instruction',1,'p_instruction','Mparser.py',49),
  ('print -> PRINT expr ;','print',3,'p_print_instruction','Mparser.py',53),
  ('print -> PRINT boolean ;','print',3,'p_print_instruction','Mparser.py',54),
  ('print -> PRINT matrix_row ;','print',3,'p_print_instruction','Mparser.py',55),
  ('control_instruction -> if','control_instruction',1,'p_control_instruction','Mparser.py',59),
  ('control_instruction -> while','control_instruction',1,'p_control_instruction','Mparser.py',60),
  ('control_instruction -> for','control_instruction',1,'p_control_instruction','Mparser.py',61),
  ('control_instruction -> break','control_instruction',1,'p_control_instruction','Mparser.py',62),
  ('control_instruction -> continue','control_instruction',1,'p_control_instruction','Mparser.py',63),
  ('control_instruction -> return','control_instruction',1,'p_control_instruction','Mparser.py',64),
  ('break -> BREAK ;','break',2,'p_break_instruction','Mparser.py',68),
  ('continue -> CONTINUE ;','continue',2,'p_continue_instruction','Mparser.py',71),
  ('return -> RETURN expr ;','return',3,'p_return_instruction','Mparser.py',74),
  ('for -> FOR ID = range instruction','for',5,'p_for','Mparser.py',77),
  ('range -> expr : expr','range',3,'p_range_operator','Mparser.py',80),
  ('while -> WHILE ( boolean ) instruction','while',5,'p_while','Mparser.py',83),
  ('if -> IF ( boolean ) instruction','if',5,'p_if','Mparser.py',86),
  ('if -> IF ( boolean ) instruction else','if',6,'p_if','Mparser.py',87),
  ('else -> ELSE instruction','else',2,'p_else','Mparser.py',91),
  ('block -> { instructions }','block',3,'p_instructions_block','Mparser.py',95),
  ('assignment -> id_part = expr','assignment',3,'p_assignment','Mparser.py',98),
  ('assignment -> id_part = boolean','assignment',3,'p_assignment','Mparser.py',99),
  ('assignment -> id_part ADDASSIGN expr','assignment',3,'p_assignment','Mparser.py',100),
  ('assignment -> id_part SUBASSIGN expr','assignment',3,'p_assignment','Mparser.py',101),
  ('assignment -> id_part MULASSIGN expr','assignment',3,'p_assignment','Mparser.py',102),
  ('assignment -> id_part DIVASSIGN expr','assignment',3,'p_assignment','Mparser.py',103),
  ('id_part -> ID [ matrix_row ]','id_part',4,'p_id_index','Mparser.py',107),
  ('id_part -> ID','id_part',1,'p_id_index','Mparser.py',108),
  ('expr -> ( expr )','expr',3,'p_parentheses','Mparser.py',113),
  ('boolean -> expr LT expr','boolean',3,'p_relational_operators','Mparser.py',117),
  ('boolean -> expr GT expr','boolean',3,'p_relational_operators','Mparser.py',118),
  ('boolean -> expr LE expr','boolean',3,'p_relational_operators','Mparser.py',119),
  ('boolean -> expr GE expr','boolean',3,'p_relational_operators','Mparser.py',120),
  ('boolean -> expr NEQ expr','boolean',3,'p_relational_operators','Mparser.py',121),
  ('boolean -> expr EQ expr','boolean',3,'p_relational_operators','Mparser.py',122),
  ("expr -> expr '",'expr',2,'p_matrix_transposition','Mparser.py',126),
  ('expr -> - expr','expr',2,'p_expr_uminus','Mparser.py',130),
  ('expr -> expr DOTADD expr','expr',3,'p_matrix_operators','Mparser.py',133),
  ('expr -> expr DOTSUB expr','expr',3,'p_matrix_operators','Mparser.py',134),
  ('expr -> expr DOTMUL expr','expr',3,'p_matrix_operators','Mparser.py',135),
  ('expr -> expr DOTDIV expr','expr',3,'p_matrix_operators','Mparser.py',136),
  ('expr -> expr + expr','expr',3,'p_binary_operators','Mparser.py',140),
  ('expr -> expr - expr','expr',3,'p_binary_operators','Mparser.py',141),
  ('expr -> expr * expr','expr',3,'p_binary_operators','Mparser.py',142),
  ('expr -> expr / expr','expr',3,'p_binary_operators','Mparser.py',143),
  ('expr -> ID','expr',1,'p_expr_def','Mparser.py',147),
  ('expr -> STRING','expr',1,'p_expr_def','Mparser.py',148),
  ('expr -> FLOAT','expr',1,'p_expr_def','Mparser.py',149),
  ('expr -> INT','expr',1,'p_expr_def','Mparser.py',150),
  ('expr -> EYE ( expr )','expr',4,'p_matrix','Mparser.py',154),
  ('expr -> ZEROS ( expr )','expr',4,'p_matrix','Mparser.py',155),
  ('expr -> ONES ( expr )','expr',4,'p_matrix','Mparser.py',156),
  ('expr -> [ matrix_rows ]','expr',3,'p_matrix','Mparser.py',157),
  ('matrix_rows -> matrix_rows , [ matrix_row ]','matrix_rows',5,'p_matrix_rows','Mparser.py',161),
  ('matrix_rows -> [ matrix_row ]','matrix_rows',3,'p_matrix_rows','Mparser.py',162),
  ('matrix_row -> matrix_row , expr','matrix_row',3,'p_matrix_row','Mparser.py',166),
  ('matrix_row -> expr','matrix_row',1,'p_matrix_row','Mparser.py',167),
]