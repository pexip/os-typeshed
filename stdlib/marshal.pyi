from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from typing import Any

version: int

def dump(__value: Any, __file: SupportsWrite[bytes], __version: int = ...) -> None: ...
def load(__file: SupportsRead[bytes]) -> Any: ...
def dumps(__value: Any, __version: int = ...) -> bytes: ...
def loads(__bytes: ReadableBuffer) -> Any: ...