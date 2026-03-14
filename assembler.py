import re

output_file_path = "Test01-out.txt"


def bin_to_hex(str):
    decimal_number = int(str, 2)
    hexadecimal_string = hex(decimal_number)
    return hexadecimal_string[2:]

def check_format(raw_format):
    if raw_format:
        if raw_format[0] in ("@"):
            raw_format = raw_format[2:]
        if raw_format[-1] in ("H"):
            raw_format = raw_format[:-1]
            if raw_format[0] == "0":
                raw_format = raw_format[1:]
        if raw_format[0] in ("#"):
            raw_format = raw_format[1:]
            if raw_format[0] == "0":
                raw_format = raw_format[1:]
        if raw_format[0] in ("R"):
            raw_format = raw_format[1:]

    return raw_format

#print(check_format("#0B3H"))




with open("Test01.txt") as f:
    with open(output_file_path, 'w') as text_file:
        for x in f:
            #print(x)
            x_split = re.split(r'[, ]+', x)
            x_split[-1] = x_split[-1].replace("\n", "")

            #print("x_split: ")
            #print(x_split)
            if x_split:
                
                if(x_split[0] == "MOV"):
                    for element in x_split:
                        #text_file.write(element + " ")
                        print("element: "+element+"\n")
                    if ("H" in x_split[1]) and ("H" in x_split[2]):
                        #hex_string = hex(decimal_number)
                        text_file.write(bin_to_hex("10000101")+" ")
                        print("machine code: "+ bin_to_hex("10000101") +"\n")
                        
                        text_file.write(check_format(x_split[2])+" ")
                        print("machine code: "+ check_format(x_split[2])+"\n")
                        
                        text_file.write(check_format(x_split[1])+" ")
                        print("machine code: "+ check_format(x_split[1])+"\n")
                        print("-------------------------------")

                    if ("@" in x_split[1]) and ("#" in x_split[2]):
                        #print("MOV @Ri, #imm: "+x_split[1])
                        decimal_machine_code = "0111011"+check_format(x_split[1])
                        print("decimal: "+decimal_machine_code)
                        #print("hexadecimal: "+bin_to_hex(decimal_machine_code))
                        hex_machine_code = bin_to_hex(decimal_machine_code)
                        text_file.write(hex_machine_code+" ")
                        print("machine code: "+ hex_machine_code+"\n")

                        text_file.write(check_format(x_split[2])+" ")
                        print("machine code: "+ check_format(x_split[2])+"\n")
                        
                        print("-------------------------------")

                    if ("R" in x_split[1]) and ("H" in x_split[2]):
                        decimal_machine_code = "10101"+check_format(x_split[1])
                        print("decimal machine code: "+decimal_machine_code)
                        hex_machine_code = bin_to_hex(decimal_machine_code)
                        print("hex machine code: "+hex_machine_code)
                        

                        print("-------------------------------")



'''        
                elif(x_split[0] == "SUBB" and len(x)>1):
                    text_file.write("SUBB: ")
                    text_file.write(x)
                elif(x_split[0] == "XRL"):
                    text_file.write("XRL: ")
                    text_file.write(x)
                elif(x_split[0] == "INC"):
                    text_file.write("INC: ")
                    text_file.write(x)
                elif(x_split[0] == "JZ"):
                    text_file.write("JZ: ")
                    text_file.write(x)
                elif(x_split[0] == "LCALL"):
                    text_file.write("LCALL: ")
                    text_file.write(x)
                elif(x_split[0] == "RET"):
                    text_file.write("RET: ")
                    text_file.write(x)
'''
