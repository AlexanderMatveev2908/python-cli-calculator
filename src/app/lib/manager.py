from app.lib.paperwork.op import OperationT


class Manager:
    @classmethod
    def bye(cls: type["Manager"]) -> None:
        print("Bye ✌🏼")
        exit(0)

    @classmethod
    def bye_if_bored(cls: type["Manager"], ch: OperationT) -> None:
        if ch.value == "_":
            cls.bye()
