from app.lib.collector import Collector
from app.lib.error import ErrApp
from app.lib.style import StyleCLI


def main() -> None:
    StyleCLI.intro()

    ch: int = Collector.get_operation()

    print(ErrApp("something"))


if __name__ == "__main__":
    main()
