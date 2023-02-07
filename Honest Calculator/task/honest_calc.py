# write your code here

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = float(0)
result = float(0)
is_done = False


def is_one_digit(v):
    output = False
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    is_done = False
    print(msg_0)
    calc = input().split()
    x = calc[0]
    operator = calc[1]
    y = calc[2]

    if x == "M":
        x = str(memory)

    if y == "M":
        y = str(memory)

    if not x.replace(".", "").isnumeric() or not y.replace(".", "").isnumeric():
        print(msg_1)
    elif operator == "+":
        check(float(x), float(y), operator)
        result = float(x) + float(y)
    elif operator == "-":
        check(float(x), float(y), operator)
        result = float(x) - float(y)
    elif operator == "*":
        check(float(x), float(y), operator)
        result = float(x) * float(y)
    elif operator == "/":
        check(float(x), float(y), operator)
        if float(y) != 0:
            result = float(x) / float(y)
        else:
            print(msg_3)
            continue
    else:
        print(msg_2)

    print(str(result))

    while True:
        print(msg_4)
        ans = input()
        if ans == "y":
            if is_one_digit(float(result)):
                msg_index = 10
                while True:
                    print(msg_list[msg_index])
                    ans = input()
                    if ans == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                            continue
                        else:
                            memory = result
                            break
                    if ans == "n":
                        break
                    else:
                        continue
            else:
                memory = result
                break

            break
        elif ans == "n":
            break
        else:
            continue

    while True:
        print(msg_5)
        ans = input()
        if ans == "y":
            break
        elif ans == "n":
            is_done = True
            break

    if is_done:
        break
