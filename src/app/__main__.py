from app.lib.collector import Collector
from app.lib.manager import Manager
from app.lib.style import StyleCLI
from app.lib.types import OperationT


def main() -> None:
    StyleCLI.intro()

    op: OperationT = Collector.get_operation()
    Manager.bye_if_bored(op)

    StyleCLI.num_choices()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\t")
        Manager.bye()
