def produces_output(program):
    instructions = set("HQ9")

    for instruction in program:
        if instruction in instructions:
            return True

    return False


program = input()

if produces_output(program):
    print("YES")
else:
    print("NO")
