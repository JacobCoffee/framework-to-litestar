from rich import get_console

console = get_console()


def transform_decorators(code: str) -> str:
    """Transform FastAPI decorators to a Litestar decorator and add necessary imports.

    Args:
        code (str): The code to transform.
    """
    used_decorators = set()
    route_decorators = [
        "@app.delete",
        "@app.head",
        "@app.get",
        "@app.post",
        "@app.put",
        "@app.patch",
        "@app.options",  # Litestar does not have an options decorator
        "@app.trace",  # Litestar does not have a trace decorator
    ]

    for decorator in route_decorators:
        if decorator in code:
            if decorator in ["@app.options", "@app.trace"]:
                console.print(f"Litestar does not support the '{decorator}' decorator")
                code = code.replace(decorator, f"# TODO: Find a replacement for the '{decorator}' decorator")
            else:
                used_decorators.add(decorator[5:])
                code = code.replace(decorator, f"@{decorator[5:]}")

    if used_decorators:
        imports = ", ".join(used_decorators)
        import_statement = f"from litestar import {imports}\n\n"
        code = import_statement + code

    return code
