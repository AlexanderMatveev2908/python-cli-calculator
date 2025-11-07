class StyleCLI:
    @classmethod
    def __title(cls: type["StyleCLI"]) -> None:
        side: str = "=" * 3
        emj: str = "🧮"
        ttl: str = f"{side} {emj} PYTHON CLI CALCULATOR {emj} {side}"

        print(ttl)

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
        print("\t")

        side: str = "-" * 3
        print(f"{side} Enter your numbers {side}")
