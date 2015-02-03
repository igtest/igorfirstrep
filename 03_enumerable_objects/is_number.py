def is_number(string):
    index = 0
    substring = ""
    if string.isdigit():
        return True
    if string[0] == '-':
        substring = string[1:]
    else:
        substring = string
    if '.' in substring:
        index = substring.index('.')
        substring = substring[:index] + substring[index + 1:]
    elif ',' in substring:
        index = substring.index(',')
        substring = substring[:index] + substring[index + 1:]
    if substring.isdigit():
        return True
    else:
        return False
