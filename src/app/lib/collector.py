from typing import cast
from app.lib.dev.error import ErrApp
from app.lib.paperwork.op import OperationT
from app.lib.paperwork.types import ArgNumT, CalcAgainResT


class Collector:
    @classmethod
    def get_operation(cls) -> OperationT:
        while True:
            try:
                ch: str = input("Select an option (1-5): ").strip()
                num: int = int(ch)

                if 1 <= num <= 5:
                    return OperationT.from_choice(num)
                else:
                    ErrApp.err_log("Invalid choice. Enter a number between 1 and 5.")

            except Exception:
                ErrApp.err_log("☢️ Enter a valid integer.")

    @classmethod
    def num_choice(cls: type["Collector"], arg: ArgNumT) -> float:
        while True:
            try:
                ch: str = input(f"{arg} number: ").strip()
                num: float = float(ch)

                return num
            except Exception:
                ErrApp.err_log("Enter a valid integer/float number")

    @classmethod
    def again(cls: type["Collector"]) -> CalcAgainResT:

        msg_err: str = (
            "Please enter y if you want to calculate again or n if you want to exit"
        )

        while True:
            try:
                print("\t")

                res: str = input("Do you want to calculate again? ").strip().lower()

                allowed: list[CalcAgainResT] = ["y", "n"]
                if res in allowed:
                    return cast(CalcAgainResT, res)
                else:
                    ErrApp.err_log(msg_err)

            except Exception:
                ErrApp.err_log(msg_err)
