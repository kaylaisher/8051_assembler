import re
from main import MOV, SUBB, XRL, LCALL, INC, RET, JZ
from util import tool
from Address import Data
from location import Location

output_file_path = "out/Test01-out.txt"
log_file_path = "log/Test01-log.txt"
test_file_path = "test_file/Test01.txt"

print("...")


with open("test_file/Test01.txt") as f:
    with open(output_file_path, 'w') as text_file:
        with open(log_file_path, 'w') as log:
            
            # for y in f:
            #     x_split = re.split(r'[, ]+', x)
            #     x_split[-1] = x_split[-1].replace("\n", "")

            #     if x_split:


            for x in f:
                #log.write(x)
                x_split = re.split(r'[, ]+', x)
                x_split[-1] = x_split[-1].replace("\n", "")
                    

                #log.write("x_split: ")
                #log.write(x_split)
                if x_split:
                    log.write("element: \n")
                    for element in x_split:
                        log.write(element + '\n')
                    

                    if(":" in x_split[0]):
                       
                        Location.label_location(x_split, text_file, log)


                    elif(x_split[0] == "MOV"):

                        #for element in x_split:
                            #text_file.write(element + " ")
                            #log.write("element: "+element+"\n")
                        if ("H" in x_split[1]) and ("H" in x_split[2]):
                            
                            Location.MOVdirect_direct_location(x_split, text_file, log)
                            MOV.direct_direct(x_split, text_file, log)

                            
                        elif ("@" in x_split[1]) and ("#" in x_split[2]):
                            Location.MOVreg_imm_location(x_split, text_file, log)
                            MOV.reg_imm(x_split, text_file, log)

                        elif ("R" in x_split[1]) and ("H" in x_split[2]):
                            Location.MOVRn_direct_location(x_split, text_file, log)
                            MOV.Rn_direct(x_split, text_file, log)
                                        
                    elif(x_split[0] == "RET"):
                        Location.ret_location(x_split, text_file, log)
                        RET.ret(x_split, text_file, log)
                        

                    elif x_split[0] == "SUBB":
                        if ("A" in x_split[1]) and ("@R" in x_split[2]):
                            Location.SUBBA_Ri_location(x_split, text_file, log)
                            SUBB.A_Ri(x_split, text_file, log)

                        else:
                            Location.SUBBA_Rn_location(x_split, text_file, log)
                            SUBB.A_Rn(x_split, text_file, log)

                    elif(x_split[0] == "XRL"):
                        if ("H" in x_split[1]) and ("#" in x_split[2]):
                            Location.XRLdirect_imm_location(x_split, text_file, log)
                            XRL.direct_imm(x_split, text_file, log)

                        elif ("H" in x_split[1]) and ("A" in x_split[2]):
                            Location.XRLdirect_A_location(x_split, text_file, log)                            
                            XRL.direct_A(x_split, text_file, log)
                    
                        elif ("A" in x_split[1]) and ("H" in x_split[2]):
                            Location.XRLA_direct_location(x_split, text_file, log)
                            XRL.A_direct(x_split, text_file, log)


                    elif(x_split[0] == "LCALL"):
                        Location.lcall_location(x_split, text_file, log)
                        LCALL.lcall(x_split, text_file, log)

                    
                    elif(x_split[0] == "INC"):
                        if "@" in x_split[1]:
                            Location.INCRi_location(x_split, text_file, log)
                            INC.Ri(x_split, text_file, log)
                        
                        else:
                            Location.INCRn_location(x_split, text_file, log)
                            INC.Rn(x_split, text_file, log)


                        
                    elif(x_split[0] == "JZ"):
                        Location.jz_location(x_split, text_file, log)
                        JZ.jz(x_split, text_file, log)
                    
                
                    
    
                Data.addr_index += 1
