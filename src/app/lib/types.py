from enum import Enum
from typing import Literal, Optional, TypeVar


class OperationT(Enum):
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"
    ex = "_"

    @classmethod
    def from_choice(cls: type["OperationT"], choice: int) -> "OperationT":
        match choice:
            case 1:
                return cls.add
            case 2:
                return cls.sub
            case 3:
                return cls.mul
            case 4:
                return cls.div
            case 5:
                return cls.ex
            case _:
                raise Exception("❌ invalid choice")


T = TypeVar("T")
Nullable = Optional[T]


ArgNumT = Literal["First", "Second"]
