from dataclasses import dataclass
from app.lib.types import Nullable, OperationT


@dataclass
class Ctx:
    op: OperationT
    arg_a: float
    arg_b: float
