from dataclasses import dataclass

from app.lib.paperwork.op import OperationT


@dataclass
class Ctx:
    op: OperationT
    arg_a: float
    arg_b: float
