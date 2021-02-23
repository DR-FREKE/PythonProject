def hackerrankInString(s):
    string_constant = 'hackerrank'
    empty = ""
    for x in s:
        if x in string_constant:
            empty += x
    print(empty)


hackerrankInString('hereiamstackerrank')
