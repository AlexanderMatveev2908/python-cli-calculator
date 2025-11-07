from app.lib.dev.error import ErrApp
from app.lib.paperwork.context import Ctx
from app.lib.paperwork.op import OperationT


class Calc:
    @classmethod
    def __add(cls: type["Calc"], a: float, b: float) -> float:
        return a + b

    @classmethod
    def __sub(cls: type["Calc"], a: float, b: float) -> float:
        return a - b

    @classmethod
    def __mul(cls: type["Calc"], a: float, b: float) -> float:
        return a * b

    @classmethod
    def __div(cls: type["Calc"], a: float, b: float) -> float | str:
        return "❌ Division by zero not allowed" if b == 0 else a / b

    @classmethod
    def main(cls: type["Calc"], ctx: Ctx) -> float | str:
        match ctx.op:
            case OperationT.add:
                return cls.__add(ctx.arg_a, ctx.arg_b)
            case OperationT.sub:
                return cls.__sub(ctx.arg_a, ctx.arg_b)
            case OperationT.mul:
                return cls.__mul(ctx.arg_a, ctx.arg_b)
            case OperationT.div:
                return cls.__div(ctx.arg_a, ctx.arg_b)
            case _:
                raise ErrApp(f"unexpected operation => {ctx.op}")
