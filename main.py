while True:
    colors = {
        "червоний": (255, 0, 0),
        "зелений": (0, 255, 0),
        "синій": (0, 0, 255),
        "жовтий": (255, 255, 0),
        "помаранчевий": (255, 165, 0),
        "фіолетовий": (128, 0, 128),
        "чорний": (0, 0, 0),
        "білий": (255, 255, 255),
        "сірий": (169, 169, 169),
        "коричневий": (139, 69, 19)
    }

    color_name = input("Введіть назву кольору: ").lower()
    if color_name in colors:
        print(f"RGB код для кольору {color_name}: {colors[color_name]}")
    else:
        print("Колір не знайдено")
    a = input("Бажаєте ще дізнатись RGB кольору? якщо так натисніть y")
    if a != "y":
        exit()