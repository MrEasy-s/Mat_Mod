from typing import Optional, List, Union, Any

class Token:
    def __init__(self, value: str):
        self.value = value
    
    def __repr__(self):
        return f"Token({self.value!r})"

class Scanner:
    def __init__(self, input_stream: Any):
        self._input_stream = input_stream
    
    def scan(self) -> Token:
        line = self._input_stream.readline()
        return Token(line)

class ProgramNode:
    def __init__(self):
        self._children: List[ProgramNode] = []
    
    def get_source_position(self) -> (int, int):

        return (0, 0)
    
    def add(self, child: 'ProgramNode'):
        self._children.append(child)
    
    def remove(self, child: 'ProgramNode'):
        self._children.remove(child)
    
    def traverse(self, code_generator: 'CodeGenerator'):

        code_generator.visit(self)
        for child in self._children:
            child.traverse(code_generator)

class ProgramNodeBuilder:
    def __init__(self):
        self._node: Optional[ProgramNode] = None
    
    def new_variable(self, variable_name: str) -> ProgramNode:

        return ProgramNode()
    
    def new_assignment(self, variable: ProgramNode, expression: ProgramNode) -> ProgramNode:

        return ProgramNode()
    
    def new_return_statement(self, value: ProgramNode) -> ProgramNode:

        return ProgramNode()
    
    def new_condition(self, condition: ProgramNode, true_part: ProgramNode, false_part: ProgramNode) -> ProgramNode:

        return ProgramNode()
    
    def get_root_node(self) -> Optional[ProgramNode]:
        return self._node

class CodeGenerator:
    def __init__(self, output: Any):
        self._output = output
    
    def visit(self, node: ProgramNode):
        pass

class ExpressionNode(ProgramNode):
    def traverse(self, code_generator: CodeGenerator):
        code_generator.visit(self)
        for child in self._children:
            child.traverse(code_generator)

class RISCCodeGenerator(CodeGenerator):
    def visit(self, node: ProgramNode):
        pass

class Compiler:
    def __init__(self):
        pass
    
    def compile(self, input_stream: Any, output_stream: Any):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()
        parser.parse(scanner, builder)
        generator = RISCCodeGenerator(output_stream)
        parse_tree = builder.get_root_node()
        if parse_tree:
            parse_tree.traverse(generator)

class Parser:
    def __init__(self):
        pass
    
    def parse(self, scanner: Scanner, program_node_builder: ProgramNodeBuilder):
        pass

if __name__ == "__main__":
    import sys
    compiler = Compiler()
    compiler.compile(sys.stdin, sys.stdout)
