"""Console script for ppw_20240107_slug."""

import fire


def help() -> None:
    print("ppw_20240107_slug")
    print("=" * len("ppw_20240107_slug"))
    print("Skeleton project created by Python Project Wizard (ppw)")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
