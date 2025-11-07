from app.lib.collector import Collector
from app.lib.manager import Manager
from app.lib.style import StyleCLI


def main() -> None:
    StyleCLI.intro()

    ch: int = Collector.get_operation()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\t")
        Manager.bye()
