from util import tool
from Address import Data, MOVaddr, RETaddr, SUBBaddr, XRLaddr, LCALLaddr, INCaddr, JZaddr

output_file_path = "Test01-out.txt"
text_file = "Test01.txt"
log = "log.txt"

class LABEL:
    def label_location(x_split, text_file, log):
        clean_op = tool.check_format(x_split[0])
        log.write("LABEL: " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += 0
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
        

        log.write("-----------------------------\n")

class MOV:

    def direct_direct(x_split, text_file, log):
        #with open(output_file_path, 'w') as text_file:

        text_file.write(tool.check_size(tool.bin_to_hex("10000101"))+" ")
        log.write("machine code: "+ tool.bin_to_hex("10000101") + '\n')
        
        text_file.write(tool.check_size(tool.check_format(x_split[2]))+" ")
        log.write("machine code: "+ tool.check_format(x_split[2]) + '\n')
        
        text_file.write(tool.check_size(tool.check_format(x_split[1]))+" ")
        log.write("machine code: "+ tool.check_format(x_split[1]) + '\n')
        log.write("-------------------------------\n")

    def direct_direct_location(x_split, text_file, log):
        clean_op = tool.check_format(x_split[0])
        log.write("OPCODE : " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += MOVaddr.direct_direct_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def reg_imm(x_split, text_file, log):
        #with open(output_file_path, 'w') as text_file:

        #log.write("MOV @Ri, #imm: "+x_split[1])
        decimal_machine_code = "0111011"+tool.check_format(x_split[1])
        #log.write("decimal: " + decimal_machine_code)
        #log.write("hexadecimal: "+bin_to_hex(decimal_machine_code))
        hex_machine_code = tool.bin_to_hex(decimal_machine_code)
        text_file.write(tool.check_size(hex_machine_code) +" ")
        log.write("machine code: "+ hex_machine_code+"\n")

        text_file.write(tool.check_size(tool.check_format(x_split[2])) + " ")
        log.write("machine code: "+ tool.check_format(x_split[2])+"\n")
        
        log.write("-------------------------------\n")

    def reg_imm_location(x_split, text_file, log):
        clean_op = tool.check_format(x_split[0])
        log.write("OPCODE : " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += MOVaddr.reg_imm_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def Rn_direct(x_split, text_file, log):
        decimal_machine_code = "10101"+ tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        #log.write("decimal machine code: "+decimal_machine_code)
        hex_machine_code = tool.check_size(tool.bin_to_hex(decimal_machine_code))
        log.write("hex machine code: " + hex_machine_code + '\n')
        text_file.write(hex_machine_code + " ")
        log.write("machine code: " + tool.check_format(x_split[2]) + '\n')
        text_file.write(tool.check_size(tool.check_format(x_split[2])) + " ")

        log.write("-------------------------------\n")

    def Rn_direct_location(x_split, text_file, log):
        clean_op = tool.check_format(x_split[0])
        log.write("OPCODE : " + clean_op + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += MOVaddr.Rn_direct_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

class SUBB:
    def A_Ri(x_split, text_file, log):
        binary_machine_code = "1001011" + tool.check_format(x_split[2])
        hex_machine_code = tool.bin_to_hex(binary_machine_code)
        log.write("machine code: " + hex_machine_code + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")

        log.write("-------------------------------\n")

    def A_Ri_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += SUBBaddr.A_Ri_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def A_Rn(x_split, text_file, log):
        binary_machine_code = "10011" + str(tool.dec_to_3bit_bin(int(tool.check_format(x_split[2]))))
        #log.write("bin machine code: " + binary_machine_code)
        
        hex_machine_code = tool.bin_to_hex(binary_machine_code)
        log.write("machine code: " + hex_machine_code + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")
        log.write("-------------------------------\n")

    def A_Rn_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += SUBBaddr.A_Rn_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

class XRL:
    def direct_imm(x_split, text_file, log):
        first_machine_code = tool.bin_to_hex("01100011")
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[1])
        log.write("machine code: " + second_machine_code + '\n')
        text_file.write(tool.check_size(second_machine_code) + " ")

        third_machine_code = tool.check_format(x_split[2])
        log.write("machine code: " + third_machine_code + '\n')
        text_file.write(tool.check_size(third_machine_code) + " ")
        log.write("-------------------------------\n")

    def direct_imm_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += XRLaddr.direct_imm_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: ")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')


    def direct_A(x_split, text_file, log):
        first_machine_code = tool.bin_to_hex("01100010")
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[1])
        log.write("machine code: " + second_machine_code + "\n")
        text_file.write(tool.check_size(second_machine_code) + " ")
        
        log.write("-------------------------------\n")

    def direct_A_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += XRLaddr.direct_A_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def A_direct(x_split, text_file, log):
        first_machine_code = tool.bin_to_hex("01100101")
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[2])
        log.write("machine code: " + second_machine_code + '\n')
        text_file.write(tool.check_size(second_machine_code) + " ")
        log.write("-------------------------------\n")

    def A_direct_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += XRLaddr.A_direct_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

class LCALL:
    def lcall(x_split, text_file, log):
        first_machine_code = tool.check_format(tool.bin_to_hex("00010010"))
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        #print(Data.addr_data)
        #print(x_split)
        for address_detail in Data.addr_data:
            #print(Data.addr_data)
            if len(address_detail) >1 and  x_split[1] == address_detail[1]:
                #log.write("call location: \n")
                #print("call location: ")
                #log.write(address_detail )
                #print(address_detail)
                label_location = address_detail[2]
                break
        label_location = tool.dec_to_16bit_bin(label_location)
        #print("label location: " + label_location)
        second_machine_code = tool.check_size(label_location[8:15])
        print("second machine code: " + second_machine_code)
        log.write("machine code: " + tool.check_size(second_machine_code) + '\n')
        text_file.write(tool.check_size(second_machine_code) + " ")
        
        third_machine_code = tool.check_size(label_location[0:7])
        print("third machine code: " + third_machine_code)
        log.write("machine code: " + tool.check_size(third_machine_code) + '\n')
        text_file.write(tool.check_size(third_machine_code) + " ")

        log.write("-------------------------------\n")

    def lcall_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += LCALLaddr.lcall_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

class INC:
    def Ri(x_split, text_file, log):
        bin_machine_code = "0000011" + tool.check_format(x_split[1])
        hex_machine_code = tool.bin_to_hex(bin_machine_code)
        log.write("machine code: " + tool.check_size(hex_machine_code) + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")
        log.write("-------------------------------\n")

    def Ri_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += INCaddr.Ri_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

    def Rn(x_split, text_file, log):
        bin_machine_code = "00001" + tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        hex_machine_code = tool.bin_to_hex(bin_machine_code)
        log.write("machine code: " + tool.check_size(hex_machine_code) + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")
        log.write("-------------------------------\n")

    def Rn_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += INCaddr.Rn_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

class JZ:
    def jz(x_split, text_file, log):
        first_machine_code = "01100000"
        first_machine_code = tool.bin_to_hex(first_machine_code)
        log.write("machine code: " + tool.check_size(first_machine_code) + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")
        
        print(Data.addr_data)
        for address_detail in Data.addr_data:
            #print(Data.addr_data)
            if len(address_detail) >1 and  x_split[1] == address_detail[1]:
                log.write("call location: \n")
                print("call location: ")
                print(address_detail)
                label_location = address_detail[2]
                break

        
        print("label location: ")
        print(label_location)
        print("next location: ")
        print(Data.next_addr_cnt)        
        
        offset = int(label_location) - Data.next_addr_cnt + 0xff + 0x01
        offset = hex(offset)
        second_machine_code = offset.upper()
        second_machine_code = second_machine_code[2:]
        print("second machine code: ")
        print(second_machine_code)
        text_file.write(second_machine_code + " ")

    def jz_location(x_split, text_file, log):
        clean_op = x_split[0]
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += JZaddr.jz_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')

class RET:
    def ret(x_split, text_file, log):
        machine_code = "00100010"
        hex_machine_code = tool.bin_to_hex(machine_code)
        log.write("machine code: " + hex_machine_code + '\n')
        text_file.write(hex_machine_code+" ")
        log.write("-------------------------------\n")

    def ret_location(x_split, text_file, log):
        clean_op = x_split[0]
        log.write("OPCODE : " + x_split[0] + '\n')
        Data.current_addr_cnt = Data.next_addr_cnt
        Data.addr_data.append(Data.addr_detail)
        Data.next_addr_cnt += RETaddr.ret_addr
        Data.addr_detail = [Data.addr_index, clean_op, Data.current_addr_cnt, Data.next_addr_cnt]
        
        log.write("addr detail: \n")
        log.write("addr index: " + str(Data.addr_detail[0]) + '\n')
        log.write("opcode: " + Data.addr_detail[1] + '\n')
        log.write("current addr: " + str(Data.addr_detail[2]) + '\n')
        log.write("next addr: " + str(Data.addr_detail[3]) + '\n')
