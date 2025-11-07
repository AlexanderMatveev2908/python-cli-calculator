from app.lib.error import ErrApp
from app.lib.types import ArgNumT, OperationT


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
            except Exception as err:
                ErrApp.err_log("Enter a valid integer/float number")
