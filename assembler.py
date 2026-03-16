import re
from main import MOV, SUBB, XRL, LCALL, INC, RET, JZ
from util import tool
from Address import Data
from location import Location

output_file_path = "out/Test01-out.txt"
log_file_path = "log/Test01-log.txt"
test_file_path = "test_file/Test01.txt"


with open("test_file/Test01.txt") as f:
    with open(log_file_path, 'w') as log:
         for y in f:
            print(y)
            y_split = re.split(r'[, ]+', y)
            y_split[-1] = y_split[-1].replace("\n", "")
            if(y_split[0] == ''): y_split = y_split[1:]
            # print("y_split: ")
            # print(y_split)

            if y_split:
                
                # for element in y_split:
                #     log.write(element + 'here!\n')
                

                if(":" in y_split[0]):
                    Location.label_location(y_split, log)


                elif(y_split[0] == "MOV"):
                   
                    if ("H" in y_split[1]) and ("H" in y_split[2]):
                        Location.MOVdirect_direct_location(y_split, log)

                        
                    elif ("@" in y_split[1]) and ("#" in y_split[2]):
                        Location.MOVreg_imm_location(y_split, log)

                    elif ("R" in y_split[1]) and ("H" in y_split[2]):
                        # print("Hi!  ")
                        Location.MOVRn_direct_location(y_split, log)
                                    
                elif(y_split[0] == "RET"):
                    Location.ret_location(y_split, log)
                    

                elif(y_split[0] == "SUBB"):
                    if ("A" in y_split[1]) and ("@R" in y_split[2]):
                        Location.SUBBA_Ri_location(y_split, log)

                    else:
                        Location.SUBBA_Rn_location(y_split, log)

                elif(y_split[0] == "XRL"):
                    #print("XRL location---------")
                    if ("H" in y_split[1]) and ("#" in y_split[2]):
                        Location.XRLdirect_imm_location(y_split, log)

                    elif ("H" in y_split[1]) and ("A" in y_split[2]):
                        Location.XRLdirect_A_location(y_split, log)                            
                
                    elif ("A" in y_split[1]) and ("H" in y_split[2]):
                        Location.XRLA_direct_location(y_split, log)


                elif(y_split[0] == "LCALL"):
                    Location.lcall_location(y_split, log)

                
                elif(y_split[0] == "INC"):
                    #print("INC location---------")
                    if "@" in y_split[1]:
                        Location.INCRi_location(y_split, log)
                    
                    else:
                        Location.INCRn_location(y_split, log)

                elif(y_split[0] == "JZ"):
                    #print("JZ location-------")
                    Location.jz_location(y_split, log)

            Data.addr_index += 1
            # print(Data.addr_data)


with open("test_file/Test01.txt") as f:
    with open(output_file_path, 'w') as text_file:
        with open(log_file_path, 'w') as log:
            #print(Data.addr_data)
            for x in f:
                #log.write(x)
                x_split = re.split(r'[, ]+', x)
                x_split[-1] = x_split[-1].replace("\n", "")
                if(x_split[0] == ""): x_split = x_split[1:]
                # print("x_split: ")
                # print(x_split)

                #log.write("x_split: ")
                #log.write(x_split)
                if x_split:
                    log.write("element: \n")
                    for element in x_split:
                        log.write(element + '\n')
                    

                    if(x_split[0] == "MOV"):
                        # print("MOV main--------")
                       
                        if ("H" in x_split[1]) and ("H" in x_split[2]):
                            MOV.direct_direct(x_split, text_file, log)

                            
                        elif ("@" in x_split[1]) and ("#" in x_split[2]):
                            MOV.reg_imm(x_split, text_file, log)

                        elif ("R" in x_split[1]) and ("H" in x_split[2]):
                            MOV.Rn_direct(x_split, text_file, log)
                                        
                    elif(x_split[0] == "RET"):
                        RET.ret(x_split, text_file, log)
                        

                    elif x_split[0] == "SUBB":
                        # print("SUBB main----------")
                        if ("A" in x_split[1]) and ("@R" in x_split[2]):
                            SUBB.A_Ri(x_split, text_file, log)

                        else:
                            SUBB.A_Rn(x_split, text_file, log)

                    elif(x_split[0] == "XRL"):
                        # print("XRL main-------")
                        if ("H" in x_split[1]) and ("#" in x_split[2]):
                            XRL.direct_imm(x_split, text_file, log)

                        elif ("H" in x_split[1]) and ("A" in x_split[2]):
                            XRL.direct_A(x_split, text_file, log)
                    
                        elif ("A" in x_split[1]) and ("H" in x_split[2]):
                            XRL.A_direct(x_split, text_file, log)


                    elif(x_split[0] == "LCALL"):
                        LCALL.lcall(x_split, text_file, log)

                    
                    elif(x_split[0] == "INC"):
                        #print("Find INC")
                        # print("INC main-----------")
                        if "@" in x_split[1]:
                            INC.Ri(x_split, text_file, log)
                        
                        else:
                            # print("INC R7 is suppose to be here")
                            INC.Rn(x_split, text_file, log)

                        
                    elif(x_split[0] == "JZ"):
                        print("x_split: ")
                        print(x_split)
                        JZ.jz(x_split, text_file, log)
                #print("-----next line-----\n")
    