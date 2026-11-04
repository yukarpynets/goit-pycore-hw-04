def total_salary(path: str) -> tuple[int, float]:
    
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, salary = line.split(",")
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"файл не знайдено: {path}")
        return 0, 0
    except ValueError:
        print("файл містить рядок у неправильному форматі.")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count
    return total, average


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")