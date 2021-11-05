from typing import Any, Optional

from pandas.io.parsers.base_parser import ParserBase


class CParserWrapper(ParserBase):
    kwds: Any = ...
    unnamed_cols: Any = ...
    names: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    def __init__(self, src: Any, **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def set_error_bad_lines(self, status: Any) -> None: ...
    def read(self, nrows: Optional[Any] = ...) -> Any: ...