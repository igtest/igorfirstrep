def is_number(string):
    index = 0
    subString = ""
    if string.isdigit():
        return True
    if string[0] == '-':
        subString = string[1:]
    else:
        subString = string
    if '.' in subString:
        index = subString.index('.')
        subString = subString[:index] + subString[index+1:]
    elif ',' in subString:
        index = subString.index(',')
        subString = subString[:index] + subString[index+1:]
    if subString.isdigit():
        return True
    else:
        return False
