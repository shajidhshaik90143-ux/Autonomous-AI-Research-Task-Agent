import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod
}


def calculate(expression):

    expression = expression.strip()

    try:

        tree = ast.parse(
            expression,
            mode="eval"
        )

        return _evaluate(tree.body)

    except Exception as error:

        return f"Calculation error: {error}"


def _evaluate(node):

    if isinstance(
        node,
        ast.Constant
    ):

        if isinstance(
            node.value,
            (int, float)
        ):

            return node.value

    if isinstance(
        node,
        ast.BinOp
    ):

        left = _evaluate(node.left)

        right = _evaluate(node.right)

        operator_function = OPERATORS.get(
            type(node.op)
        )

        if not operator_function:

            raise ValueError(
                "Unsupported operator"
            )

        return operator_function(
            left,
            right
        )

    if isinstance(
        node,
        ast.UnaryOp
    ):

        value = _evaluate(
            node.operand
        )

        if isinstance(
            node.op,
            ast.USub
        ):

            return -value

        if isinstance(
            node.op,
            ast.UAdd
        ):

            return value

    raise ValueError(
        "Invalid mathematical expression"
    )