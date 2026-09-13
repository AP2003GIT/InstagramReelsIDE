import sys

from codereels.app import CodeReelsApplication


def main() -> int:
    application = CodeReelsApplication(sys.argv)
    return application.run()


if __name__ == "__main__":
    raise SystemExit(main())

