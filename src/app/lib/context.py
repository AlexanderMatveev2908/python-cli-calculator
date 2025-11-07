from dataclasses import dataclass
from app.lib.types import OperationT


@dataclass
class Ctx:
    op: OperationT
    arg_a: int
    arg_b: int
