import time

def run_program(program):
    cells = [0]
    max_length = 255
    max_value = 255
    curr_cell_num = 0
    output = []
    errors = []  # collect all errors here

    unlucky_numbers = {
        4, 14, 24, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 54, 64,
        74, 84, 94, 104, 105, 106, 107, 108, 109, 114, 124, 134, 140,
        141, 142, 143, 144, 145, 146, 147, 148, 149, 154, 164, 174, 184,
        194, 204, 205, 206, 207, 208, 209, 214, 224, 234, 240, 241, 242,
        243, 244, 245, 246, 247, 248, 249, 254
    }


    def exec_char(char):
        nonlocal curr_cell_num, cells, output

        if char == "n":
            time.sleep(0.1)
            curr_cell_num += 1
            cells.append(0)
            if curr_cell_num > max_length:
                curr_cell_num = 0
        elif char == "i":
            time.sleep(0.1)
            cells[curr_cell_num] += 1
            if cells[curr_cell_num] in unlucky_numbers:
                errors.append(f"TypeOver: NumError; That number ({cells[curr_cell_num]}) is unlucky in Chinese culture.")
            else:
                errors.append(f"TypeOver: NoError; Your program is completley fine I just wanted to annoy you.")
            if cells[curr_cell_num] > max_value:
                cells[curr_cell_num] = 0
        elif char == "p":
            time.sleep(0.1)
            output.append(str(cells[curr_cell_num]))
            print(cells[curr_cell_num])
            errors.append(f"TypeOver: NoError; Your program is completley fine I just wanted to annoy you.")
        elif char == "u":
            time.sleep(0.1)
            try:
                char_output = chr(cells[curr_cell_num])
                output.append(char_output)
                print(char_output, end='')
                errors.append(f"TypeOver: NoError; Your program is completley fine I just wanted to annoy you.")
            except ValueError:
                errors.append(f"TypeOver: Unicode Print Error; HEY YOU CANT JUST MAKE UP UR OWN UNICODE CODEPOINTS! '{cells[curr_cell_num]}' ISNT A THING! IF YOU WANT TO PRINT IT SO BADLY ASK THE UNICODE CONSORTIUM! D:<")
        elif char == "a":
            time.sleep(0.1)
            if cells[curr_cell_num] < 128:
                char_output = chr(cells[curr_cell_num])
                output.append(char_output)
                print(char_output, end='')
            else:
                errors.append(f"TypeOver: ASCII Print Error; YO '{cells[curr_cell_num]}' AINT ASCII SO DONT EVEN TRY!")
        else:
            errors.append(f"TypeOver: brother what in the react js is '{char}'")

    def parse_and_run_loop(body):
        nonlocal curr_cell_num, cells

        k = 0
        while k < len(body):
            c = body[k]
            if c == "c" and k + 1 < len(body) and body[k + 1] == "[":
                bracket_depth = 1
                inner_body = ""
                m = k + 2

                while m < len(body) and bracket_depth > 0:
                    if body[m] == "[":
                        bracket_depth += 1
                    elif body[m] == "]":
                        bracket_depth -= 1
                    if bracket_depth > 0:
                        inner_body += body[m]
                    m += 1

                if bracket_depth != 0:
                    errors.append("TypeOver: how DARE you mismatch those brackets in that nested loop >:(")
                    return

                k = m - 1

                while cells[curr_cell_num] != curr_cell_num:
                    parse_and_run_loop(inner_body)
            else:
                exec_char(c)
            k += 1

    i = 0
    while i < len(program):
        curr_char = program[i]

        if curr_char == "c":
            if i + 1 < len(program) and program[i + 1] == "[":
                loop_body = ""
                bracket_depth = 1
                j = i + 2

                while j < len(program) and bracket_depth > 0:
                    if program[j] == "[":
                        bracket_depth += 1
                    elif program[j] == "]":
                        bracket_depth -= 1
                    if bracket_depth > 0:
                        loop_body += program[j]
                    j += 1

                if bracket_depth != 0:
                    errors.append(f"TypeOver: how DARE you mismatch those brackets starting at {i}.")
                    break

                i = j - 1

                while cells[curr_cell_num] != curr_cell_num:
                    parse_and_run_loop(loop_body)
            else:
                next_char = program[i + 1] if i + 1 < len(program) else "EOF"
                errors.append(f'TypeOver: Loop Start Error at character {i}; Expected "[", found "{next_char}". I dont know what this means so figure it out yourself')
        elif curr_char == "[":
            if i == 0 or program[i - 1] != "c":
                errors.append(f'TypeOver: Loop Reference Error at character {i}; "[" without "c" before it. I dont know what this means so figure it out yourself')
        elif curr_char == "]":
            pass
        else:
            exec_char(curr_char)

        i += 1

    print()  # newline before errors
    for err in errors:
        print(err)

    print(f"\nFinal state: {cells}")
    return output, cells


print("TypeOver: an even worse version of Rollover")
run_program(input("YO ENTER YO CODE ALREADY:"))
