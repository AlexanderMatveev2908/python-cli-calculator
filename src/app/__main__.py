from app.lib.collector import Collector
from app.lib.paperwork.context import Ctx
from app.lib.manager import Manager
from app.lib.paperwork.op import OperationT
from app.lib.style import StyleCLI


def main() -> None:
    StyleCLI.intro()

    op: OperationT = Collector.get_operation()
    Manager.bye_if_bored(op)

    StyleCLI.num_choices()

    arg_a: float = Collector.num_choice("First")
    arg_b: float = Collector.num_choice("Second")

    ctx: Ctx = Ctx(op, arg_a, arg_b)

    StyleCLI.result(ctx)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\t")
        Manager.bye()
