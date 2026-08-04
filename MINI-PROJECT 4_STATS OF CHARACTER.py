full_dot = '●'
empty_dot = '○'

def create_character(name, strength,intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    stats = [strength,intelligence, charisma]

    for s in stats:
        if not isinstance(s, int):
            return "All stats should be integers"
        if s < 1:
            return "All stats should be no less than 1"
        if s > 4:
            return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"


    str_line = f"STR {full_dot * strength}{empty_dot * (10- strength)}"
    int_line = f"INT {full_dot * intelligence}{empty_dot * (10- intelligence)}"
    cha_line = f"CHA {full_dot * charisma}{empty_dot * (10- charisma)}"

    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"


print(create_character('ren', 4, 2, 1))


        
