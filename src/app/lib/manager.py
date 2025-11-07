class Manager:
    @classmethod
    def bye(cls: type["Manager"]) -> None:
        print("Bye ✌🏼")
        exit(0)
