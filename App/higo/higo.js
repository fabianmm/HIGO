Blockly.JavaScript['var_dec'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'var ' + dropdown_type + ' ' + value_var + ';\n';
  return code;
};

Blockly.JavaScript['single_name'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = text_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['function_dec'] = function(block) {
  var text_funcname = block.getFieldValue('FUNCNAME');
  var value_params = Blockly.JavaScript.valueToCode(block, 'PARAMS', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_statements = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
  // TODO: Assemble JavaScript into code variable.
  var code = 'function ' + text_funcname + ' ( ' + value_params + ' ) { ' + statements_statements + ' }\n';
  return code;
};

Blockly.JavaScript['assign'] = function(block) {
  var value_varname = Blockly.JavaScript.valueToCode(block, 'VARNAME', Blockly.JavaScript.ORDER_ATOMIC);
  var value_value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_varname + ' = ' + value_value + ';\n';
  return code;
};

Blockly.JavaScript['number'] = function(block) {
  var code = block.getFieldValue('NUM');
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['arith_operation'] = function(block) {
  var op = block.getFieldValue('OP');
  var operator;
  var order;
  if (op == "PLUS") {
    operator = ' + ';
    order = Blockly.JavaScript.ORDER_ADDITION;
  }
  else if (op == "MINUS") {
    operator = ' - ';
    order = Blockly.JavaScript.ORDER_SUBTRACTION;
  }
  else if (op == "TIMES") {
    operator = ' * ';
    order = Blockly.JavaScript.ORDER_MULTIPLICATION;
  }
  else if (op == "DIVIDE") {
    operator = ' / ';
    order = Blockly.JavaScript.ORDER_DIVISION;
  }

  var argument0 = Blockly.JavaScript.valueToCode(block, 'A', order) || '0';
  var argument1 = Blockly.JavaScript.valueToCode(block, 'B', order) || '0';
  var code;
  code = argument0 + operator + argument1;
  return [code, order];
};

Blockly.JavaScript['rel_op'] = function(block) {
  var op = block.getFieldValue('OP');
  var operator;
  var order;
  if (op == "GT") {
    operator = ' > ';
    order = Blockly.JavaScript.ORDER_RELATIONAL;
  }
  else if (op == "LT") {
    operator = ' < ';
    order = Blockly.JavaScript.ORDER_RELATIONAL;
  }
  else if (op == "GE") {
    operator = ' >= ';
    order = Blockly.JavaScript.ORDER_RELATIONAL;
  }
  else if (op == "LE") {
    operator = ' <= ';
    order = Blockly.JavaScript.ORDER_RELATIONAL;
  }
  else if (op == "EE") {
    operator = " == ";
    order = Blockly.JavaScript.ORDER_EQUALITY;
  }
  else if (op == "NE") {
    operator = " != ";
    order = Blockly.JavaScript.ORDER_EQUALITY;
  }

  var argument0 = Blockly.JavaScript.valueToCode(block, 'A', order) || '0';
  var argument1 = Blockly.JavaScript.valueToCode(block, 'B', order) || '0';
  var code;
  code = argument0 + operator + argument1;
  return [code, order];
};

Blockly.JavaScript['bool_op'] = function(block) {
  var op = block.getFieldValue('OP');
  var operator;
  var order;
  if (op == "AND") {
    operator = ' and ';
    order = Blockly.JavaScript.ORDER_AND;
  }
  else if (op == "OR") {
    operator = ' or ';
    order = Blockly.JavaScript.ORDER_AND;
  }

  var argument0 = Blockly.JavaScript.valueToCode(block, 'A', order) || '0';
  var argument1 = Blockly.JavaScript.valueToCode(block, 'B', order) || '0';
  var code;
  code = argument0 + operator + argument1;
  return [code, order];
};

Blockly.JavaScript['print'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'print(' + value_value + ');\n';
  return code;
};

Blockly.JavaScript['read'] = function(block) {
  var text_varname = block.getFieldValue('VARNAME');
  // TODO: Assemble JavaScript into code variable.
  var code = 'readto ( ' + text_varname + ' );\n';
  return code;
};

Blockly.JavaScript['if'] = function(block) {
  var code = '', branchCode, conditionCode;
  
  conditionCode = Blockly.JavaScript.valueToCode(block, 'EXP',
    Blockly.JavaScript.ORDER_NONE) || 'false';
  branchCode = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
  code = 'if (' + conditionCode + ') {\n' + branchCode + '}';

  if (block.getInput('ELSE')) {
    branchCode = Blockly.JavaScript.statementToCode(block, 'ELSE');
    code += ' else {\n' + branchCode + '}';
  }
  return code + '\n';
};

Blockly.JavaScript['if_else'] = function(block) {
  var code = '', branchCode, conditionCode, elseCode;
  
  conditionCode = Blockly.JavaScript.valueToCode(block, 'EXP',
    Blockly.JavaScript.ORDER_NONE) || 'false';
  branchCode = Blockly.JavaScript.statementToCode(block, 'IF_STATEMENT');
  elseCode = Blockly.JavaScript.statementToCode(block, 'ELSE_STATEMENT');
  code = 'if (' + conditionCode + ') {\n' + branchCode + '}' + '\nelse {\n' + elseCode + '}';
  return code + '\n';
};

Blockly.JavaScript['while'] = function(block) {
  var value_exp = Blockly.JavaScript.valueToCode(block, 'EXP', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_statements = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
  // TODO: Assemble JavaScript into code variable.
  var code = 'while (' + value_exp + ') {\n' + statements_statements + '}\n';
  return code;
};

Blockly.JavaScript['function_dec_return'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_funcname = block.getFieldValue('FUNCNAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_statements = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
  var value_return = Blockly.JavaScript.valueToCode(block, 'RETURN', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'function ' + dropdown_type + ' ' + text_funcname + '(' + value_name + '){\n' + statements_statements + '\nreturn ' + value_return + ';\n}\n';
  return code;
};

Blockly.JavaScript['void_func_call'] = function(block) {
  var text_funcname = block.getFieldValue('FUNCNAME');
  var value_params = Blockly.JavaScript.valueToCode(block, 'PARAMS', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_funcname + '(' + value_params + ');\n';
  return code;
};

Blockly.JavaScript['func_call_value'] = function(block) {
  var text_funcname = block.getFieldValue('FUNCNAME');
  var value_params = Blockly.JavaScript.valueToCode(block, 'PARAMS', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_funcname + '(' + value_params + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['not'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'not ' + value_value;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.LOGICAL_NOT];
};

Blockly.JavaScript['if_return'] = function(block) {
  var value_exp = Blockly.JavaScript.valueToCode(block, 'EXP', Blockly.JavaScript.ORDER_ATOMIC);
  var value_value = Blockly.JavaScript.valueToCode(block, 'VALUE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'if (' + value_exp + '){\nreturn ' + value_value + ';\n}\n';
  return code;
};

Blockly.JavaScript['multiple_names'] = function(block) {
  var value_a = Blockly.JavaScript.valueToCode(block, 'A', Blockly.JavaScript.ORDER_ATOMIC);
  var value_b = Blockly.JavaScript.valueToCode(block, 'B', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_a + ', ' + value_b;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['program'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = 'program ' + text_name + '{\n' +statements_name + '}';
  return code;
};

Blockly.JavaScript['list_dec'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var value_name = Blockly.JavaScript.valueToCode(block, 'name', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'list ' + dropdown_type + ' ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['list_add'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  var text_listname = block.getFieldValue('listname');
  // TODO: Assemble JavaScript into code variable.
  var code = text_listname + '.add(' + value_value + ');\n';
  return code;
};

Blockly.JavaScript['list_item'] = function(block) {
  var text_listname = block.getFieldValue('listname');
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_listname + '[' + value_value + ']';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['list_find'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  var text_listname = block.getFieldValue('listname');
  // TODO: Assemble JavaScript into code variable.
  var code = text_listname + '.find(' + value_value + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['list_remove'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_value + '.remove;\n';
  return code;
};

Blockly.JavaScript['list_sort'] = function(block) {
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_value + '.sort;\n';
  return code;
};