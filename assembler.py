import re
from main import MOV, SUBB, XRL, LCALL, INC, RET, JZ, LABEL
from util import tool
from Address import Data

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
                        # clean_op = tool.check_format(x_split[0])
                        # log.write("LABEL: " + clean_op + '\n')
                        # Data.current_addr_cnt = Data.next_addr_cnt
                        # Data.addr_data.append(Data.addr_detail)
                        # Data.next_addr_cnt += 0
                        # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                        
                        # log.write("addr detail: \n")
                        # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                        # log.write("opcode: " + Data.addr_detail[1] + '\n')
                        # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                        # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                        

                        # log.write("-----------------------------\n")
                        LABEL.label_location(x_split, text_file, log)


                    elif(x_split[0] == "MOV"):

                        #for element in x_split:
                            #text_file.write(element + " ")
                            #log.write("element: "+element+"\n")
                        if ("H" in x_split[1]) and ("H" in x_split[2]):
                            # MOV direct, direct --> 10000101src_direct dest_direct
                            # clean_op = tool.check_format(x_split[0])
                            # log.write("OPCODE : " + clean_op + '\n')
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += MOVaddr.direct_direct_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            
                            MOV.direct_direct_location(x_split, text_file, log)
                            MOV.direct_direct(x_split, text_file, log)

                            
                        elif ("@" in x_split[1]) and ("#" in x_split[2]):
                            # MOV @Ri, #imm --> 0111011i immediate
                            # clean_op = tool.check_format(x_split[0])
                            # log.write("OPCODE : " + clean_op + '\n')
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += MOVaddr.reg_imm_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            MOV.reg_imm_location(x_split, text_file, log)
                            MOV.reg_imm(x_split, text_file, log)

                        elif ("R" in x_split[1]) and ("H" in x_split[2]):
                            #MOV Rn, direct --> 10101nnn direct
                            # clean_op = tool.check_format(x_split[0])
                            # log.write("OPCODE : " + clean_op + '\n')
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += MOVaddr.Rn_direct_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            MOV.Rn_direct_location(x_split, text_file, log)
                            MOV.Rn_direct(x_split, text_file, log)
                                        
                    elif(x_split[0] == "RET"):
                        # clean_op = x_split[0]
                        # log.write("OPCODE : " + x_split[0] + '\n')
                        # Data.current_addr_cnt = Data.next_addr_cnt
                        # Data.addr_data.append(Data.addr_detail)
                        # Data.next_addr_cnt += RETaddr.ret_addr
                        # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                        
                        # log.write("addr detail: \n")
                        # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                        # log.write("opcode: " + Data.addr_detail[1] + '\n')
                        # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                        # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                        RET.ret_location(x_split, text_file, log)
                        RET.ret(x_split, text_file, log)
                        

                    elif x_split[0] == "SUBB":
                        if ("A" in x_split[1]) and ("@R" in x_split[2]):
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += SUBBaddr.A_Ri_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            SUBB.A_Ri_location(x_split, text_file, log)
                            SUBB.A_Ri(x_split, text_file, log)

                        else:
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += SUBBaddr.A_Rn_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            SUBB.A_Rn_location(x_split, text_file, log)
                            SUBB.A_Rn(x_split, text_file, log)

                    elif(x_split[0] == "XRL"):
                        if ("H" in x_split[1]) and ("#" in x_split[2]):
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += XRLaddr.direct_imm_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: ")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            XRL.direct_imm_location(x_split, text_file, log)
                            XRL.direct_imm(x_split, text_file, log)

                        elif ("H" in x_split[1]) and ("A" in x_split[2]):
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += XRLaddr.direct_A_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            XRL.direct_A_location(x_split, text_file, log)                            
                            XRL.direct_A(x_split, text_file, log)
                    
                        elif ("A" in x_split[1]) and ("H" in x_split[2]):
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += XRLaddr.A_direct_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            XRL.A_direct_location(x_split, text_file, log)
                            XRL.A_direct(x_split, text_file, log)


                    elif(x_split[0] == "LCALL"):
                        # clean_op = x_split[0]
                        # Data.current_addr_cnt = Data.next_addr_cnt
                        # Data.addr_data.append(Data.addr_detail)
                        # Data.next_addr_cnt += LCALLaddr.lcall_addr
                        # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                        
                        # log.write("addr detail: \n")
                        # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                        # log.write("opcode: " + Data.addr_detail[1] + '\n')
                        # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                        # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                        LCALL.lcall_location(x_split, text_file, log)
                        LCALL.lcall(x_split, text_file, log)

                    
                    elif(x_split[0] == "INC"):
                        if "@" in x_split[1]:
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += INCaddr.Ri_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            INC.Ri_location(x_split, text_file, log)
                            INC.Ri(x_split, text_file, log)
                        
                        else:
                            # clean_op = x_split[0]
                            # Data.current_addr_cnt = Data.next_addr_cnt
                            # Data.addr_data.append(Data.addr_detail)
                            # Data.next_addr_cnt += INCaddr.Rn_addr
                            # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            # log.write("addr detail: \n")
                            # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                            # log.write("opcode: " + Data.addr_detail[1] + '\n')
                            # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                            # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                            INC.Rn_location(x_split, text_file, log)
                            INC.Rn(x_split, text_file, log)


                        
                    elif(x_split[0] == "JZ"):
                        # clean_op = x_split[0]
                        # Data.current_addr_cnt = Data.next_addr_cnt
                        # Data.addr_data.append(Data.addr_detail)
                        # Data.next_addr_cnt += JZaddr.jz_addr
                        # Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                        
                        # log.write("addr detail: \n")
                        # log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                        # log.write("opcode: " + Data.addr_detail[1] + '\n')
                        # log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                        # log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                        JZ.jz_location(x_split, text_file, log)
                        JZ.jz(x_split, text_file, log)
                    
                
                    
    
                Data.addr_index += 1
