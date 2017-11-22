// Blockly.Blocks['var_dec'] = {
//     init: function() {
//       this.appendValueInput("var")
//           .setCheck(null)
//           .appendField("var")
//           .appendField(new Blockly.FieldDropdown([["int","INT"], ["decimal","DECIMAL"], ["bool","BOOL"]]), "TYPE");
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(90);
//    this.setTooltip("var");
//    this.setHelpUrl("var");
//     }
//   };
  
//   Blockly.Blocks['single_name'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldTextInput("name"), "NAME");
//       this.setOutput(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['multiple_names'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldTextInput("name"), "NAME1")
//           .appendField(",")
//           .appendField(new Blockly.FieldTextInput("name"), "NAME2");
//       this.setOutput(true, null);
//       this.setColour(195);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['program'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField("program")
//           .appendField(new Blockly.FieldTextInput("name"), "NAME");
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(300);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['function_dec'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField("function void")
//           .appendField(new Blockly.FieldTextInput("name"), "FUNCNAME")
//           .appendField("(");
//       this.appendValueInput("PARAMS")
//           .setCheck(null);
//       this.appendDummyInput()
//           .appendField(")");
//       this.appendStatementInput("STATEMENTS")
//           .setCheck(null);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['assign'] = {
//     init: function() {
//       this.appendValueInput("VALUE")
//           .setCheck(null)
//           .appendField(new Blockly.FieldTextInput("variable"), "VARNAME")
//           .appendField("=");
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['number'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldNumber(0), "NUM");
//       this.setOutput(true, "Number");
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['arith_operation'] = {
//     init: function() {
//       this.appendValueInput("A")
//           .setCheck("Number");
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldDropdown([["+","PLUS"], ["-","MINUS"], ["*","TIMES"], ["/","DIVIDE"]]), "OP");
//       this.appendValueInput("B")
//           .setCheck("Number");
//       this.setInputsInline(true);
//       this.setOutput(true, "Number");
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['rel_op'] = {
//     init: function() {
//       this.appendValueInput("A")
//           .setCheck("Number");
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldDropdown([[">","GT"], ["<","LT"], [">=","GE"], ["<=","LE"], ["==","EE"], ["!=","NE"]]), "OP");
//       this.appendValueInput("B")
//           .setCheck("Number");
//       this.setInputsInline(true);
//       this.setOutput(true, "Boolean");
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['bool_op'] = {
//     init: function() {
//       this.appendValueInput("A")
//           .setCheck("Boolean");
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldDropdown([["and","AND"], ["or","OR"]]), "OP");
//       this.appendValueInput("B")
//           .setCheck("Boolean");
//       this.setOutput(true, "Boolean");
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['print'] = {
//     init: function() {
//       this.appendValueInput("VALUE")
//           .setCheck(null)
//           .appendField("print");
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['read'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField("read to")
//           .appendField(new Blockly.FieldTextInput("variable"), "VARNAME");
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['if'] = {
//     init: function() {
//       this.appendValueInput("EXP")
//           .setCheck("Boolean")
//           .appendField("if");
//       this.appendStatementInput("STATEMENTS")
//           .setCheck(null);
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['if_else'] = {
//     init: function() {
//       this.appendValueInput("EXP")
//           .setCheck("Boolean")
//           .appendField("if");
//       this.appendStatementInput("IF_STATEMENT")
//           .setCheck(null);
//       this.appendDummyInput()
//           .appendField("else");
//       this.appendStatementInput("ELSE_STATEMENT")
//           .setCheck(null);
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['while'] = {
//     init: function() {
//       this.appendValueInput("EXP")
//           .setCheck("Boolean")
//           .appendField("while");
//       this.appendStatementInput("STATEMENTS")
//           .setCheck(null);
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['function_dec_return'] = {
//     init: function() {
//       this.appendValueInput("NAME")
//           .setCheck(null)
//           .appendField("function")
//           .appendField(new Blockly.FieldDropdown([["int","INT"], ["decimal","DECIMAL"], ["bool","BOOL"]]), "TYPE")
//           .appendField(new Blockly.FieldTextInput("name"), "FUNCNAME")
//           .appendField("(");
//       this.appendDummyInput()
//           .appendField(")");
//       this.appendStatementInput("STATEMENTS")
//           .setCheck(null);
//       this.appendValueInput("RETURN")
//           .setCheck(null)
//           .setAlign(Blockly.ALIGN_RIGHT)
//           .appendField("return");
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['void_func_call'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldTextInput("function"), "FUNCNAME")
//           .appendField("(");
//       this.appendValueInput("PARAMS")
//           .setCheck(null);
//       this.appendDummyInput()
//           .appendField(")");
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['func_call_value'] = {
//     init: function() {
//       this.appendDummyInput()
//           .appendField(new Blockly.FieldTextInput("function"), "FUNCNAME")
//           .appendField("(");
//       this.appendValueInput("PARAMS")
//           .setCheck(null);
//       this.appendDummyInput()
//           .appendField(")");
//       this.setInputsInline(true);
//       this.setOutput(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
  
//   Blockly.Blocks['not'] = {
//     init: function() {
//       this.appendValueInput("VALUE")
//           .setCheck("Boolean")
//           .appendField("not");
//       this.setInputsInline(true);
//       this.setOutput(true, "Boolean");
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };
//   Blockly.Blocks['if_return'] = {
//     init: function() {
//       this.appendValueInput("EXP")
//           .setCheck("Boolean")
//           .appendField("if");
//       this.appendValueInput("VALUE")
//           .setCheck(null)
//           .appendField("return");
//       this.setInputsInline(true);
//       this.setPreviousStatement(true, null);
//       this.setNextStatement(true, null);
//       this.setColour(230);
//    this.setTooltip("");
//    this.setHelpUrl("");
//     }
//   };

Blockly.defineBlocksWithJsonArray([{
    "type": "var_dec",
    "message0": "var %1 %2",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "TYPE",
        "options": [
          [
            "int",
            "INT"
          ],
          [
            "decimal",
            "DECIMAL"
          ],
          [
            "bool",
            "BOOL"
          ]
        ]
      },
      {
        "type": "input_value",
        "name": "var"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 285,
    "tooltip": "var",
    "helpUrl": "var"
  },
  {
    "type": "single_name",
    "message0": "%1",
    "args0": [
      {
        "type": "field_input",
        "name": "NAME",
        "text": "name"
      }
    ],
    "output": null,
    "colour": 180,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "multiple_names",
    "message0": "%1 , %2 %3",
    "args0": [
      {
        "type": "input_value",
        "name": "A",
        "check": "String"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "B",
        "check": "String"
      }
    ],
    "output": null,
    "colour": 180,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "program",
    "message0": "program %1 %2 %3",
    "args0": [
      {
        "type": "field_input",
        "name": "NAME",
        "text": "name"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_statement",
        "name": "NAME"
      }
    ],
    "previousStatement": null,
    "colour": 270,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "function_dec",
    "message0": "function void %1 ( %2 %3 ) %4 %5",
    "args0": [
      {
        "type": "field_input",
        "name": "FUNCNAME",
        "text": "name"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "PARAMS"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_statement",
        "name": "STATEMENTS"
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 90,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "assign",
    "message0": "%1 = %2",
    "args0": [
      {
        "type": "input_value",
        "name": "VARNAME"
      },
      {
        "type": "input_value",
        "name": "VALUE"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 30,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "number",
    "message0": "%1",
    "args0": [
      {
        "type": "field_number",
        "name": "NUM",
        "value": 0
      }
    ],
    "output": "Number",
    "colour": 240,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "arith_operation",
    "message0": "%1 %2 %3 %4",
    "args0": [
      {
        "type": "input_value",
        "name": "A",
        "check": "Number"
      },
      {
        "type": "field_dropdown",
        "name": "OP",
        "options": [
          [
            "+",
            "PLUS"
          ],
          [
            "-",
            "MINUS"
          ],
          [
            "*",
            "TIMES"
          ],
          [
            "/",
            "DIVIDE"
          ]
        ]
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "B",
        "check": "Number"
      }
    ],
    "inputsInline": true,
    "output": "Number",
    "colour": 240,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "rel_op",
    "message0": "%1 %2 %3 %4",
    "args0": [
      {
        "type": "input_value",
        "name": "A",
        "check": "Number"
      },
      {
        "type": "field_dropdown",
        "name": "OP",
        "options": [
          [
            ">",
            "GT"
          ],
          [
            "<",
            "LT"
          ],
          [
            ">=",
            "GE"
          ],
          [
            "<=",
            "LE"
          ],
          [
            "==",
            "EE"
          ],
          [
            "!=",
            "NE"
          ]
        ]
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "B",
        "check": "Number"
      }
    ],
    "inputsInline": true,
    "output": "Boolean",
    "colour": 240,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "bool_op",
    "message0": "%1 %2 %3 %4",
    "args0": [
      {
        "type": "input_value",
        "name": "A",
        "check": "Boolean"
      },
      {
        "type": "field_dropdown",
        "name": "OP",
        "options": [
          [
            "and",
            "AND"
          ],
          [
            "or",
            "OR"
          ]
        ]
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "B",
        "check": "Boolean"
      }
    ],
    "output": "Boolean",
    "colour": 240,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "print",
    "message0": "print %1",
    "args0": [
      {
        "type": "input_value",
        "name": "VALUE"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 30,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "read",
    "message0": "read to %1",
    "args0": [
      {
        "type": "field_input",
        "name": "VARNAME",
        "text": "variable"
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 30,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "if",
    "message0": "if %1 %2",
    "args0": [
      {
        "type": "input_value",
        "name": "EXP",
        "check": "Boolean"
      },
      {
        "type": "input_statement",
        "name": "STATEMENTS"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 315,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "if_else",
    "message0": "if %1 %2 else %3 %4",
    "args0": [
      {
        "type": "input_value",
        "name": "EXP",
        "check": "Boolean"
      },
      {
        "type": "input_statement",
        "name": "IF_STATEMENT"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_statement",
        "name": "ELSE_STATEMENT"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 315,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "while",
    "message0": "while %1 %2",
    "args0": [
      {
        "type": "input_value",
        "name": "EXP",
        "check": "Boolean"
      },
      {
        "type": "input_statement",
        "name": "STATEMENTS"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 315,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "function_dec_return",
    "message0": "function %1 %2 ( %3 ) %4 %5 return %6",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "TYPE",
        "options": [
          [
            "int",
            "int"
          ],
          [
            "decimal",
            "decimal"
          ],
          [
            "bool",
            "bool"
          ]
        ]
      },
      {
        "type": "field_input",
        "name": "FUNCNAME",
        "text": "name"
      },
      {
        "type": "input_value",
        "name": "NAME"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_statement",
        "name": "STATEMENTS"
      },
      {
        "type": "input_value",
        "name": "RETURN",
        "align": "RIGHT"
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 90,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "void_func_call",
    "message0": "%1 ( %2 %3 )",
    "args0": [
      {
        "type": "field_input",
        "name": "FUNCNAME",
        "text": "function"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "PARAMS"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 90,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "func_call_value",
    "message0": "%1 ( %2 %3 )",
    "args0": [
      {
        "type": "field_input",
        "name": "FUNCNAME",
        "text": "function"
      },
      {
        "type": "input_dummy"
      },
      {
        "type": "input_value",
        "name": "PARAMS"
      }
    ],
    "inputsInline": true,
    "output": null,
    "colour": 90,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "not",
    "message0": "not %1",
    "args0": [
      {
        "type": "input_value",
        "name": "VALUE",
        "check": "Boolean"
      }
    ],
    "inputsInline": true,
    "output": "Boolean",
    "colour": 240,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "if_return",
    "message0": "if %1 return %2",
    "args0": [
      {
        "type": "input_value",
        "name": "EXP",
        "check": "Boolean"
      },
      {
        "type": "input_value",
        "name": "VALUE"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 90,
    "tooltip": "",
    "helpUrl": ""
  },
  {
    "type": "list_dec",
    "message0": "list %1 %2",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "TYPE",
        "options": [
          [
            "int",
            "int"
          ],
          [
            "decimal",
            "decimal"
          ],
          [
            "bool",
            "bool"
          ]
        ]
      },
      {
        "type": "input_value",
        "name": "name"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 0,
    "tooltip": "var",
    "helpUrl": "var"
  },
  {
    "type": "list_add",
    "message0": "add %1 to %2",
    "args0": [
      {
        "type": "input_value",
        "name": "value"
      },
      {
        "type": "field_input",
        "name": "listname",
        "text": "list"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 0,
    "tooltip": "var",
    "helpUrl": "var"
  },
  {
    "type": "list_item",
    "message0": "%1 at %2",
    "args0": [
      {
        "type": "field_input",
        "name": "listname",
        "text": "list"
      },
      {
        "type": "input_value",
        "name": "value",
        "check": "Number"
      }
    ],
    "inputsInline": true,
    "output": null,
    "colour": 0,
    "tooltip": "var",
    "helpUrl": "var"
  },
  {
    "type": "list_find",
    "message0": "find %1 in %2",
    "args0": [
      {
        "type": "input_value",
        "name": "value"
      },
      {
        "type": "field_input",
        "name": "listname",
        "text": "list"
      }
    ],
    "inputsInline": true,
    "output": null,
    "colour": 0,
    "tooltip": "var",
    "helpUrl": "var"
  },
  {
    "type": "list_remove",
    "message0": "remove %1",
    "args0": [
      {
        "type": "input_value",
        "name": "value"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 0,
    "tooltip": "var",
    "helpUrl": "var"
  },
  {
    "type": "list_sort",
    "message0": "sort %1",
    "args0": [
      {
        "type": "input_value",
        "name": "value"
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "colour": 0,
    "tooltip": "var",
    "helpUrl": "var"
  }]);