import re
from main import MOV, SUBB, XRL, LCALL
from util import tool

output_file_path = "Test01-out.txt"




with open("Test01.txt") as f:
    with open(output_file_path, 'w') as text_file:
        for x in f:
            #print(x)
            x_split = re.split(r'[, ]+', x)
            x_split[-1] = x_split[-1].replace("\n", "")

            #print("x_split: ")
            #print(x_split)
            if x_split:
                print(x_split)
                if(x_split[0] == "MOV"):

                    for element in x_split:
                        #text_file.write(element + " ")
                        print("element: "+element+"\n")
                    if ("H" in x_split[1]) and ("H" in x_split[2]):
                        # MOV direct, direct --> 10000101src_direct dest_direct
                        MOV.direct_direct(x_split, text_file)
                        
                    elif ("@" in x_split[1]) and ("#" in x_split[2]):
                        # MOV @Ri, #imm --> 0111011i immediate
                        MOV.reg_imm(x_split, text_file)

                    elif ("R" in x_split[1]) and ("H" in x_split[2]):
                        #MOV Rn, direct --> 10101nnn direct
                        MOV.Rn_direct(x_split, text_file)
                                      
                elif(x_split[0] == "RET"):
                    machine_code = "00100010"
                    hex_machine_code = tool.bin_to_hex(machine_code)
                    print("machine code: "+hex_machine_code)
                    text_file.write(hex_machine_code+" ")
                    print("-------------------------------")

                elif x_split[0] == "SUBB":
                    if ("A" in x_split[1]) and ("@R" in x_split[2]):
                        SUBB.A_Ri(x_split, text_file)

                    else:
                        SUBB.A_Rn(x_split, text_file)

                elif(x_split[0] == "XRL"):
                    if ("H" in x_split[1]) and ("#" in x_split[2]):
                        XRL.direct_imm(x_split, text_file)

                    elif ("H" in x_split[1]) and ("A" in x_split[2]):
                        XRL.direct_A(x_split, text_file)
                
                elif(x_split[0] == "LCALL"):
                    
                    if (len(x_split[1]) == 16):
                        LCALL.normal(x_split, text_file)

                    else:
                        LCALL.abnormal(x_split, text_file)



                '''
                elif(x_split[0] == "INC"):
                    text_file.write("INC: ")
                    text_file.write(x)
                elif(x_split[0] == "JZ"):
                    text_file.write("JZ: ")
                    text_file.write(x)
                
                elif(x_split[0] == "RET"):
                    text_file.write("RET: ")
                    text_file.write(x)
'''
