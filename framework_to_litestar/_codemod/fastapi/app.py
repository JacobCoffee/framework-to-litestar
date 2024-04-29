"""Replace app instances."""


def transform_app_initialization(code: str) -> str:
    """Transform FastAPI app initialization to Litestar.

    Args:
        code (str): The code to transform.

    Returns:
        str: Code with transformed app initialization.
    """
    code = code.replace("from fastapi import FastAPI", "from litestar import Litestar")
    return code.replace("app = FastAPI(", "app = Litestar(")
