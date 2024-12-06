import customtkinter as ctk
import ast
import operator

def calc(p, colors):
    wid = p.winfo_screenwidth() / 200 + 30
    hig = p.winfo_screenheight() / 200 + 30

    # Operators supported for evaluation
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod
    }

    def eval_expression(expression):
        """Safely evaluate a mathematical expression using ast."""
        try:
            # Parse the expression into an AST
            tree = ast.parse(expression, mode='eval')
            return evaluate_ast(tree.body)
        except Exception as e:
            raise ValueError("Invalid expression")

    def evaluate_ast(node):
        """Recursively evaluate the AST."""
        if isinstance(node, ast.BinOp):
            left = evaluate_ast(node.left)
            right = evaluate_ast(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate_ast(node.operand)
            if isinstance(node.op, ast.UAdd):  # Unary +
                return operand
            elif isinstance(node.op, ast.USub):  # Unary -
                return -operand
        else:
            raise ValueError("Unsupported operation")

    def update_entry(value):
        """Append value to the entry field."""
        current = entry.get()
        entry.delete(0, "end")
        entry.insert(0, current + str(value))

    def clear_entry():
        """Clear the entry field."""
        entry.delete(0, "end")

    def calculate():
        """Evaluate the expression in the entry field."""
        try:
            expression = entry.get()
            result = eval_expression(expression)
            entry.delete(0, "end")
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, "end")
            entry.insert(0, "Error")

    entry = ctk.CTkEntry(p, width=wid * 5, height=hig)
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    # Define the calculator buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 5, 0), ('^', 5, 1), ('%', 5, 2), ('(', 5, 3),
        (')', 6, 0)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            ctk.CTkButton(p, text=text, command=calculate, width=wid, height=hig).grid(row=row, column=col, padx=5, pady=5)
        elif text == 'C':
            ctk.CTkButton(p, text=text, command=clear_entry, width=wid, height=hig).grid(row=row, column=col, padx=5, pady=5)
        else:
            ctk.CTkButton(p, text=text, command=lambda t=text: update_entry(t), width=wid, height=hig).grid(row=row, column=col, padx=5, pady=5)
