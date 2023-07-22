def error_response(number1, number2, operator, problems):
    try:
        int(number1)
    except:
        return "Error: Opperands must only contain digits."
    try:
        int(number2)
    except:
        return "Error: Opperands must only contain digits."
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""


def arithmetic_arranger(problems, ans_needed = False):
    start = True
    padd = "    "
    line1 = line2 = line3 = line4 = ""
    try:
        if len(problems) > 5:    #to show error if more than 5 problems are recieved
            raise BaseException
    except:
        return "Error: Too many expressions listed."
    for prob in problems: #will add all the given values in the plane
        prb_items = prob.split()
        number1 = prb_items[0]
        operator = prb_items[1]
        number2 = prb_items[2]
        err = error_response(number1, number2, operator, problems)
        if err != "":
            return err
        num1 = int(number1)
        num2 = int(number2)
        leng = max(len(number1),len(number2))
        if start == True:
            line1 += number1.rjust(leng + 2)
            line2 += operator + " " + number2.rjust(leng)
            line3 += '-' * (leng + 2)
            if ans_needed == True:
                if operator == '+':
                    line4 += str(num1 + num2).rjust(leng + 2)
                else:
                    line4 += str(num1 - num2).rjust(leng + 2)
            start = False
        else:
            line1 += number1.rjust(leng+6)
            line2 += operator.rjust(5) + " " + number2.rjust(leng)
            line3 += '-' * (leng + 2)
            if ans_needed == True:
                if operator == '+':
                    line4 += padd + str(num1 + num2).rjust(leng+2)
                else:
                    line4 += padd + str(num1 - num2).rjust(leng+2)
    if ans_needed == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])