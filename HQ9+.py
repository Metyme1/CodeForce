def produces_output(program):
    instructions = set("HQ9")

    for instruction in program:
        if instruction in instructions:
            return True

    return False


# Read the input program
program = input()

# Check if the program produces output
if produces_output(program):
    print("YES")
else:
    print("NO")
