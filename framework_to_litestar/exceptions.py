"""FTL Exceptions."""

__all__ = ("CodemodeNotFoundError",)


class _FTLException(Exception):  # noqa: N818
    """Base exception for FTL."""


class CodemodeNotFoundError(_FTLException):
    """Raised when no codemods are found in the specified module."""
