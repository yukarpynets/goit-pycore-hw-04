def get_cats_info(path: str) -> list[dict]:
    """
    Legge un file con le informazioni sui gatti.

    path: percorso del file di testo. Ogni riga ha il formato
          'id,nome,età'.
    Restituisce una lista di dizionari con le chiavi
    'id', 'name' e 'age'. In caso di errore restituisce una lista vuota.
    """
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
        print(f"File non trovato: {path}")
        return []
    except ValueError:
        print("Il file contiene una riga in un formato non valido.")
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)