def add_s(verb):
    if verb == "have":
        return "has"
    # сюда — проверка окончаний s / sh / ch / x / o → + "es"
    # сюда — проверка y (с согласной перед ней) → "ies"
    return verb + "s"


for v in ["read", "think", "fly", "dance", "have", "finish", "play"]:
    print(v, "->", add_s(v), sep="")
