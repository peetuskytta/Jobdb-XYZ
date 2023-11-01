#   Deletes consecutive "sym"-characters, except for one.
def del_doubles(sym, string) -> str:
    ret = ""
    prev_char = ""
    for char in string:
        if char != sym or char != prev_char:
                ret += char
                prev_char = char
    return ret

#   Function reads list of titles from file, turns them in to a string,
#   deletes unwanted newlines, converts certain symbols to URL-language
#   and then joins it with a proper URL-head to create a working URL.
def url_gen(filename: str, base: str) -> str:
    file = open(filename, "r")
    string = "".join(file)
    string = del_doubles("\n", string)
    if  string.startswith("\n"):
        string = string[1:]
    if  string.endswith("\n"):
        string = string[:-1]
    for symbol in "ö":
        string = string.replace(symbol, "%C3%B6")
    for symbol in "ä":
        string = string.replace(symbol, "%C3%A4")
    for symbol in " ":
        string = string.replace(symbol, "%20")
    for symbol in "\n":
        string = string.replace(symbol, "%3B")
    return (base + string)
