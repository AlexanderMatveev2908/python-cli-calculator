from typing import Literal, Optional, TypeVar


T = TypeVar("T")
Nullable = Optional[T]


ArgNumT = Literal["First", "Second"]

CalcAgainResT = Literal["y", "n"]
