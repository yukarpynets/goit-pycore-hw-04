def get_cats_info(path: str) -> list[dict]:
    
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"файл не знайдено: {path}")
        return []
    except ValueError:
        print("файл містить рядок у неправильному форматі.")
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)