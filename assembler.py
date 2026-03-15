import re
from main import MOV, SUBB, XRL, LCALL, INC, RET
from util import tool
from Address import MOVaddr, SUBBaddr, XRLaddr, INCaddr, JZaddr, LCALLaddr, RETaddr, Data

output_file_path = "Test01-out.txt"
log_file_path = "log.txt"


with open("Test01.txt") as f:
    with open(output_file_path, 'w') as text_file:
        with open(log_file_path, 'w') as log:
            
            for x in f:
                #log.write(x)
                x_split = re.split(r'[, ]+', x)
                x_split[-1] = x_split[-1].replace("\n", "")

                #log.write("x_split: ")
                #log.write(x_split)
                if x_split:
                    for element in x_split:
                        log.write(element + '\n')

                    if(":" in x_split[0]):
                        clean_op = tool.check_format(x_split[0])
                        log.write("LABEL: " + clean_op)
                        Data.current_addr_cnt = Data.next_addr_cnt
                        Data.addr_data.append(Data.addr_detail)
                        Data.next_addr_cnt += 0
                        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                        
                        log.write("addr detail: \n")
                        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
                        log.write("opcode: " + Data.addr_detail[1] + '\n')
                        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
                        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
                        

                        log.write("-----------------------------")


                    elif(x_split[0] == "MOV"):

                        #for element in x_split:
                            #text_file.write(element + " ")
                            #log.write("element: "+element+"\n")
                        if ("H" in x_split[1]) and ("H" in x_split[2]):
                            # MOV direct, direct --> 10000101src_direct dest_direct
                            clean_op = tool.check_format(x_split[0])
                            log.write("OPCODE : " + clean_op)
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += MOVaddr.direct_direct_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            

                            MOV.direct_direct(x_split, text_file)

                            
                        elif ("@" in x_split[1]) and ("#" in x_split[2]):
                            # MOV @Ri, #imm --> 0111011i immediate
                            clean_op = tool.check_format(x_split[0])
                            log.write("OPCODE : " + clean_op)
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += MOVaddr.reg_imm_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            MOV.reg_imm(x_split, text_file)

                        elif ("R" in x_split[1]) and ("H" in x_split[2]):
                            #MOV Rn, direct --> 10101nnn direct
                            clean_op = tool.check_format(x_split[0])
                            log.write("OPCODE : " + clean_op)
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += MOVaddr.Rn_direct_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            MOV.Rn_direct(x_split, text_file)
                                        
                    elif(x_split[0] == "RET"):
                        clean_op = x_split[0]
                        log.write("OPCODE : " + x_split[0])
                        Data.current_addr_cnt = Data.next_addr_cnt
                        Data.addr_data.append(Data.addr_detail)
                        Data.next_addr_cnt += RETaddr.ret_addr
                        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                        
                        log.write("addr detail: ")
                        log.write("addr index: " + str(Data.addr_detail[0]))
                        log.write("opcode: " + Data.addr_detail[1])
                        log.write("current addr: " + str(Data.addr_detail[2]))
                        log.write("next addr: " + str(Data.addr_detail[3]))
                        RET.ret(x_split, text_file)
                        

                    elif x_split[0] == "SUBB":
                        if ("A" in x_split[1]) and ("@R" in x_split[2]):
                            clean_op = x_split[0]
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += SUBBaddr.A_Ri_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            SUBB.A_Ri(x_split, text_file)

                        else:
                            clean_op = x_split[0]
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += SUBBaddr.A_Rn_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            SUBB.A_Rn(x_split, text_file)

                    elif(x_split[0] == "XRL"):
                        if ("H" in x_split[1]) and ("#" in x_split[2]):
                            clean_op = x_split[0]
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += XRLaddr.direct_imm_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            XRL.direct_imm(x_split, text_file)

                        elif ("H" in x_split[1]) and ("A" in x_split[2]):
                            clean_op = x_split[0]
                            Data.current_addr_cnt = Data.next_addr_cnt
                            Data.addr_data.append(Data.addr_detail)
                            Data.next_addr_cnt += XRLaddr.direct_A_addr
                            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
                            
                            log.write("addr detail: ")
                            log.write("addr index: " + str(Data.addr_detail[0]))
                            log.write("opcode: " + Data.addr_detail[1])
                            log.write("current addr: " + str(Data.addr_detail[2]))
                            log.write("next addr: " + str(Data.addr_detail[3]))
                            
                            XRL.direct_A(x_split, text_file)
                    
                        elif ("A" in x_split[1]) and ("H" in x_split[2]):
                            XRL.A_direct(x_split, text_file)

                    elif(x_split[0] == "LCALL"):
                        
                        if (len(x_split[1]) == 16):
                            LCALL.lcall(x_split, text_file)

                    
                    elif(x_split[0] == "INC"):
                        if "@" in x_split[1]:
                            INC.Ri(x_split, text_file)
                        
                        else:
                            INC.Rn(x_split, text_file)

                    Data.addr_index += 1

                        
    '''
                    elif(x_split[0] == "JZ"):
                        JZ.offset(x_split, text_file)
                    
                    elif(x_split[0] == "RET"):
                        RET.ret(x_split, text_file)
    '''