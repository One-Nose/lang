from lark import Lark, LarkError
from lark.indenter import Indenter


class BlockIndenter(Indenter):
    NL_type = '_NL'  # type: ignore
    OPEN_PAREN_types = []  # type: ignore
    CLOSE_PAREN_types = []  # type: ignore
    INDENT_type = '_INDENT'  # type: ignore
    DEDENT_type = '_DEDENT'  # type: ignore
    tab_len = 4  # type: ignore


if __name__ == '__main__':
    try:
        grammar = Lark.open(  # type: ignore
            'grammar.lark', parser='lalr', postlex=BlockIndenter()
        )
    except LarkError as e:
        print(e)
        exit()

    with open('source') as file:
        text = file.read()

    with open('output', 'w') as file:
        try:
            tree = grammar.parse(text)
        except LarkError as e:
            print(e)
            exit()

        file.write(tree.pretty())

        print('Parsed successfully')
