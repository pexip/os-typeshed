import collections.abc as _abc
from typing import Any

def normalize_locale(name): ...
def resolve_locale_filename(name): ...
def exists(name): ...
def locale_identifiers(): ...
def load(name, merge_inherited: bool = ...): ...
def merge(dict1, dict2) -> None: ...

class Alias:
    keys: Any
    def __init__(self, keys) -> None: ...
    def resolve(self, data): ...

class LocaleDataDict(_abc.MutableMapping):
    base: Any
    def __init__(self, data, base: Any | None = ...) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def copy(self): ...
