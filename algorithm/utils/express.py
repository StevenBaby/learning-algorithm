# coding=utf-8

operators = {
    '(': 0,
    ')': 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


def compile(nifix):
    num = ''
    ostack = []
    result = []
    for char in nifix:
        if char in ' ':
            continue
        if char in '0123456789':
            num += char
            continue
        if num:
            result.append(num)
            num = ''

        if char not in operators:
            raise ValueError(char)

        if not ostack or char == '(':
            ostack.append(char)
            continue
        if char == ')':
            while ostack and ostack[-1] != '(':
                result.append(ostack.pop())
            ostack.pop()
            continue

        if operators[ostack[-1]] < operators[char]:
            ostack.append(char)
            continue

        while ostack and operators[ostack[-1]] >= operators[char]:
            result.append(ostack.pop())
        ostack.append(char)

    if num:
        result.append(num)
    while ostack:
        result.append(ostack.pop())

    return result


def compute(postfix):
    result = None
    stack = []
    for item in postfix:
        if item not in operators:
            stack.append(item)
            continue

        second = stack.pop()
        first = stack.pop()
        result = eval(f'{first} {item} {second}')
        stack.append(result)

    return result


def main():
    string = '1 + 2 - 5 + (4 * 9) / 38 * 66 - 500 * 30'
    post = compile(string)
    print(post)
    print(compute(post), eval(string))


if __name__ == '__main__':
    main()
