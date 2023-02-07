name = input()


def normalize(name):
    new_name = ""
    if "é" in name:
        new_name = name.replace("é", "e")
    elif "ë" in name:
        new_name = name.replace("ë", "e")
    elif "á" in name:
        new_name = name.replace("á", "a")
    elif "å" in name:
        new_name = name.replace("å", "aa")
    elif "œ" in name:
        new_name = name.replace("œ", "oe")
    elif "æ" in name:
        new_name = name.replace("æ", "ae")

    return new_name


print(normalize(name))
