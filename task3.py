import sys
from pathlib import Path

from colorama import Fore, Style


def print_directory_tree(path: Path, indent: str = "") -> None:
   
    try:
        items = sorted(path.iterdir())
    except PermissionError:
        print(f"{indent}{Fore.RED}Доступ заборонено: {path.name}{Style.RESET_ALL}")
        return

    for item in items:
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            print_directory_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main() -> None:
   
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Використання: python3 task3.py <шлях_до_директорії>{Style.RESET_ALL}")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Шлях не існує: {path}{Style.RESET_ALL}")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Шлях не є директорією: {path}{Style.RESET_ALL}")
        return

    print(f"{Fore.BLUE}📦 {path.name}{Style.RESET_ALL}")
    print_directory_tree(path, "    ")


if __name__ == "__main__":
    main()