from util import tool
from Address import Data, MOVaddr, RETaddr, SUBBaddr, XRLaddr, LCALLaddr, INCaddr, JZaddr

output_file_path = "Test03-out.txt"
text_file = "Test03.txt"
log = "Test03-log.txt"

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


    def Rn_direct(x_split, text_file, log):
        decimal_machine_code = "10101"+ tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        #log.write("decimal machine code: "+decimal_machine_code)
        hex_machine_code = tool.check_size(tool.bin_to_hex(decimal_machine_code))
        log.write("hex machine code: " + hex_machine_code + '\n')
        text_file.write(hex_machine_code + " ")
        log.write("machine code: " + tool.check_format(x_split[2]) + '\n')
        text_file.write(tool.check_size(tool.check_format(x_split[2])) + " ")

        log.write("-------------------------------\n")


class SUBB:
    def A_Ri(x_split, text_file, log):
        binary_machine_code = "1001011" + tool.check_format(x_split[2])
        hex_machine_code = tool.bin_to_hex(binary_machine_code)
        log.write("machine code: " + hex_machine_code + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")

        log.write("-------------------------------\n")


    def A_Rn(x_split, text_file, log):
        binary_machine_code = "10011" + str(tool.dec_to_3bit_bin(int(tool.check_format(x_split[2]))))
        #log.write("bin machine code: " + binary_machine_code)
        
        hex_machine_code = tool.bin_to_hex(binary_machine_code)
        log.write("machine code: " + hex_machine_code + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")
        log.write("-------------------------------\n")


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



    def direct_A(x_split, text_file, log):
        first_machine_code = tool.bin_to_hex("01100010")
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[1])
        log.write("machine code: " + second_machine_code + "\n")
        text_file.write(tool.check_size(second_machine_code) + " ")
        
        log.write("-------------------------------\n")


    def A_direct(x_split, text_file, log):
        first_machine_code = tool.bin_to_hex("01100101")
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[2])
        log.write("machine code: " + second_machine_code + '\n')
        text_file.write(tool.check_size(second_machine_code) + " ")
        log.write("-------------------------------\n")


class LCALL:
    def lcall(x_split, text_file, log):
        first_machine_code = tool.check_format(tool.bin_to_hex("00010010"))
        log.write("machine code: " + first_machine_code + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")

        #print(x_split)
        for address_detail in Data.addr_data:
        
            # print(Data.addr_data)
            if len(address_detail) >1 and  x_split[1] == address_detail[1]:
                
                label_location = address_detail[2]
                break
        # label_location = int(label_location, 16)
        print("label location: ")
        label_location = f"{label_location:04X}"
        print(label_location)
        second_machine_code = tool.check_size(label_location[0:1])
        print("second machine code: " + second_machine_code)
        log.write("machine code: " + tool.check_size(second_machine_code) + '\n')
        text_file.write(tool.check_size(second_machine_code) + " ")
        
        third_machine_code = tool.check_size(label_location[2:])
        print("third machine code: " + third_machine_code)
        log.write("machine code: " + tool.check_size(third_machine_code) + '\n')
        text_file.write(tool.check_size(third_machine_code) + " ")

        log.write("-------------------------------\n")


class INC:
    def Ri(x_split, text_file, log):
        bin_machine_code = "0000011" + tool.check_format(x_split[1])
        hex_machine_code = tool.bin_to_hex(bin_machine_code)
        log.write("machine code: " + tool.check_size(hex_machine_code) + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")
        log.write("-------------------------------\n")


    def Rn(x_split, text_file, log):
        bin_machine_code = "00001" + tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        hex_machine_code = tool.bin_to_hex(bin_machine_code)
        log.write("machine code: " + tool.check_size(hex_machine_code) + '\n')
        text_file.write(tool.check_size(hex_machine_code) + " ")
        log.write("-------------------------------\n")


class JZ:
    def jz(x_split, text_file, log):
        first_machine_code = "01100000"
        first_machine_code = tool.bin_to_hex(first_machine_code)
        log.write("machine code: " + tool.check_size(first_machine_code) + '\n')
        text_file.write(tool.check_size(first_machine_code) + " ")
        
        print("x_split: ")
        print(x_split)
        #print(Data.addr_data)
        for address_detail1 in Data.addr_data:
            #print("HERE!")
            # print("address detail: ")
            # print(address_detail1)
            if x_split[1] == address_detail1[1]:
                # print("address detail: ")
                # print(address_detail1)
                label_location = address_detail1[2]
                print("Find label: ")
                print(label_location)
                break

        for address_detail2 in Data.addr_data:
            #print(Data.addr_data)
            if len(address_detail2) >1 and  address_detail2[1] == "JZ":
                next_addr = address_detail2[3]
                break
        
       
        offset = label_location - next_addr  

        offset_hex = offset & 0xFF   

        if offset < 0:
            offset_hex = offset + 0xFF + 1  
            #print(hex(offset_hex).upper()[2:])  # 0xf2
            offset = hex(offset_hex).upper()[2:]
        second_machine_code = tool.check_size(str(offset).upper())
        log.write("second machine code: ")
        log.write(second_machine_code)
        log.write('\n')
        print("second machine code: " + second_machine_code)
        text_file.write(second_machine_code + " ")

        log.write("-----------------------------\n")


class RET:
    def ret(x_split, text_file, log):
        machine_code = "00100010"
        hex_machine_code = tool.bin_to_hex(machine_code)
        log.write("machine code: " + hex_machine_code + '\n')
        text_file.write(hex_machine_code+" ")
        log.write("-------------------------------\n")
