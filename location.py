from util import tool
from Address import Data, MOVaddr, RETaddr, SUBBaddr, XRLaddr, LCALLaddr, INCaddr, JZaddr

output_file_path = "out/Test02-out.txt"
text_file = "test_file/Test02.txt"
log = "log/Test02-log.txt"

class Location:
    def label_location(x_split,  log):
        clean_op = tool.check_format(x_split[0])
        log.write("LABEL: " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += 0
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
        

        log.write("-----------------------------\n")

    def MOVdirect_direct_location(x_split,  log):
            clean_op = tool.check_format(x_split[0])
            log.write("OPCODE : " + clean_op + '\n')
            Data.current_addr_cnt = Data.next_addr_cnt
            Data.next_addr_cnt += MOVaddr.direct_direct_addr
            Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
            Data.addr_data.append(Data.addr_detail)
            log.write("addr detail: \n")
            log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
            log.write("opcode: " + Data.addr_detail[1] + '\n')
            log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
            log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def MOVreg_imm_location(x_split,  log):
        clean_op = tool.check_format(x_split[0])
        log.write("OPCODE : " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += MOVaddr.reg_imm_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def MOVRn_direct_location(x_split,  log):
        clean_op = tool.check_format(x_split[0])
        log.write("OPCODE : " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        
        Data.next_addr_cnt += MOVaddr.Rn_direct_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
        

    def SUBBA_Ri_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += SUBBaddr.A_Ri_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def SUBBA_Rn_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += SUBBaddr.A_Rn_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def XRLdirect_imm_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += XRLaddr.direct_imm_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)
        log.write("addr detail: ")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def XRLdirect_A_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += XRLaddr.direct_A_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def XRLA_direct_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += XRLaddr.A_direct_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def lcall_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += LCALLaddr.lcall_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def INCRi_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += INCaddr.Ri_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def INCRn_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += INCaddr.Rn_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def jz_location(x_split,  log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += JZaddr.jz_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def ret_location(x_split,  log):
        clean_op = x_split[0]
        log.write("OPCODE : " + x_split[0] + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.next_addr_cnt += RETaddr.ret_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        Data.addr_data.append(Data.addr_detail)

        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')