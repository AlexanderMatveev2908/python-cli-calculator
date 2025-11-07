from app.lib.calc import Calc
from app.lib.paperwork.context import Ctx


class StyleCLI:
    @classmethod
    def __title(cls: type["StyleCLI"]) -> None:
        side: str = "=" * 3
        emj: str = "🧮"
        ttl: str = f"{side} {emj} PYTHON CLI CALCULATOR {emj} {side}"

        print(ttl)

    @classmethod
    def __between_dashes(cls: type["StyleCLI"], txt: str) -> None:
        print("\t")

        side: str = "-" * 3
        print(f"{side} {txt} {side}")

    @classmethod
    def __menu_intro(cls: type["StyleCLI"]) -> None:
        print("Chose an operation:")

        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

    @classmethod
    def intro(cls: type["StyleCLI"]) -> None:
        cls.__title()
        cls.__menu_intro()

    @classmethod
    def num_choices(cls: type["StyleCLI"]) -> None:
        cls.__between_dashes("Enter your numbers")

    @classmethod
    def result(cls: type["StyleCLI"], ctx: Ctx) -> None:
        cls.__between_dashes("Result")

        res_calc: float | str = Calc.main(ctx)
        print(f"{ctx.arg_a} {ctx.op.value} {ctx.arg_b} = {res_calc}")
