from typing import Any

SUPPORTED_FORMATS: Any

class ExcelReader:
    archive: Any
    valid_files: Any
    read_only: Any
    keep_vba: Any
    data_only: Any
    keep_links: Any
    shared_strings: Any
    def __init__(self, fn, read_only: bool = ..., keep_vba=..., data_only: bool = ..., keep_links: bool = ...) -> None: ...
    package: Any
    def read_manifest(self) -> None: ...
    def read_strings(self) -> None: ...
    parser: Any
    wb: Any
    def read_workbook(self) -> None: ...
    def read_properties(self) -> None: ...
    def read_theme(self) -> None: ...
    def read_chartsheet(self, sheet, rel) -> None: ...
    def read_worksheets(self) -> None: ...
    def read(self) -> None: ...

def load_workbook(filename, read_only: bool = ..., keep_vba=..., data_only: bool = ..., keep_links: bool = ...): ...
