#Free_Code_Camp final test solution

#Produces error response based on criteria set in the assignment
def exception_handling(opperand1, opperand2, operator):
    # Only digit exception
    try:
        int(opperand1)
    except:
        return "Error: opperands must only contain digits."
    try:
        int(opperand2)
    except:
        return "Error: opperands must only contain digits."
    # More than 4 digit opp. exception
    try:
        if len(opperand1) > 4 or len(opperand2) > 4:
            raise BaseException
    except:
        return "Error: opperands canoppt be more than four digits."
    # Operator must be + | - exception.
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""

#Creates an output for expressions, and outputs solutions upon request
def arithmetic_arranger(problems,  total_needed=False):
    start = True
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    for prb in problems:
        prb_items = prb.split()
        opperand1 = prb_items[0]  
        operator = prb_items[1]       
        opperand2 = prb_items[2]
        exp = exception_handling(opperand1, opperand2, operator)
        if exp != "":
            return exp
        opp1 = int(opperand1)
        opp2 = int(opperand2)
        space = max(len(opperand1), len(opperand2))
        if start == True:
            line1 += opperand1.rjust(space + 2)
            line2 += operator + ' ' + opperand2.rjust(space)
            line3 += '-' * (space + 2)
            if total_needed == True:
                if operator == '+':
                    line4 += str(opp1 + opp2).rjust(space + 2)
                else:
                    line4 += str(opp1 - opp2).rjust(space + 2)
            start = False
        else:
            line1 += opperand1.rjust(space + 6)
            line2 += operator.rjust(5) + ' ' + opperand2.rjust(space)
            line3 += side_space + '-' * (space + 2)
            if total_needed == True:
                if operator == '+':
                    line4 += side_space + str(opp1 + opp2).rjust(space + 2)
                else:
                    line4 += side_space + str(opp1 - opp2).rjust(space + 2)
    if total_needed == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3

#Creates a dictionary of lists for strings splitting by whitespace, and names them dynamically   
def dict_maker(items):
    itms = dict()
    for i in range(len(items)):
        key=("list_"+str(i+1))
        for item in items:
            item = items[i]
            value = item.split()
        itms.update({key:value})
    print(itms)

dict_maker(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "56 + 73"])
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])