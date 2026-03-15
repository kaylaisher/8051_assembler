from util import tool

output_file_path = "Test01-out.txt"
text_file = "Test01.txt"

class MOV:

    def direct_direct(x_split, text_file):
        #with open(output_file_path, 'w') as text_file:

        text_file.write(tool.check_size(tool.bin_to_hex("10000101"))+" ")
        print("machine code: "+ tool.bin_to_hex("10000101") )
        
        text_file.write(tool.check_size(tool.check_format(x_split[2]))+" ")
        print("machine code: "+ tool.check_format(x_split[2]))
        
        text_file.write(tool.check_size(tool.check_format(x_split[1]))+" ")
        print("machine code: "+ tool.check_format(x_split[1]))
        print("-------------------------------")

    def reg_imm(x_split, text_file):
        #with open(output_file_path, 'w') as text_file:

        #print("MOV @Ri, #imm: "+x_split[1])
        decimal_machine_code = "0111011"+tool.check_format(x_split[1])
        #print("decimal: " + decimal_machine_code)
        #print("hexadecimal: "+bin_to_hex(decimal_machine_code))
        hex_machine_code = tool.bin_to_hex(decimal_machine_code)
        text_file.write(tool.check_size(hex_machine_code) +" ")
        print("machine code: "+ hex_machine_code+"\n")

        text_file.write(tool.check_size(tool.check_format(x_split[2])) + " ")
        print("machine code: "+ tool.check_format(x_split[2])+"\n")
        
        print("-------------------------------")

    def Rn_direct(x_split, text_file):
        decimal_machine_code = "10101"+ tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        #print("decimal machine code: "+decimal_machine_code)
        hex_machine_code = tool.check_size(tool.bin_to_hex(decimal_machine_code))
        print("hex machine code: " + hex_machine_code)
        text_file.write(hex_machine_code + " ")
        print("machine code: " + tool.check_format(x_split[2]))
        text_file.write(tool.check_size(tool.check_format(x_split[2])) + " ")

        print("-------------------------------")

class SUBB:
    def A_Ri(x_split, text_file):
        binary_machine_code = "1001011" + tool.check_format(x_split[2])
        hex_machine_code = tool.bin_to_hex(binary_machine_code)
        print("machine code: " + hex_machine_code)
        text_file.write(tool.check_size(hex_machine_code) + " ")

        print("-------------------------------")

    def A_Rn(x_split, text_file):
        binary_machine_code = "10011" + str(tool.dec_to_3bit_bin(int(tool.check_format(x_split[2]))))
        #print("bin machine code: " + binary_machine_code)
        
        hex_machine_code = tool.bin_to_hex(binary_machine_code)
        print("machine code: " + hex_machine_code)
        text_file.write(tool.check_size(hex_machine_code) + " ")
        print("-------------------------------")
        
class XRL:
    def direct_imm(x_split, text_file):
        first_machine_code = tool.bin_to_hex("01100011")
        print("machine code: " + first_machine_code)
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[1])
        print("machine code: " + second_machine_code)
        text_file.write(tool.check_size(second_machine_code) + " ")

        third_machine_code = tool.check_format(x_split[2])
        print("machine code: " + third_machine_code)
        text_file.write(tool.check_size(third_machine_code) + " ")
        print("-------------------------------")


    def direct_A(x_split, text_file):
        first_machine_code = tool.bin_to_hex("01100010")
        print("machine code: " + first_machine_code)
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[1])
        print("machine code: " + second_machine_code + " ")
        text_file.write(tool.check_size(second_machine_code) + " ")
        
        print("-------------------------------")

    def A_direct(x_split, text_file):
        first_machine_code = tool.bin_to_hex("01100101")
        print("machine code: " + first_machine_code)
        text_file.write(tool.check_size(first_machine_code) + " ")

        second_machine_code = tool.check_format(x_split[2])
        print("machine code: " + second_machine_code)
        text_file.write(tool.check_size(second_machine_code) + " ")
        print("-------------------------------")

class LCALL:
    def lcall(x_split, text_file):
        first_machine_code = tool.check_format(tool.bin_to_hex("00010010"))
        print("machine code: " + first_machine_code)
        text_file.write(tool.check_size(first_machine_code) + " ")

        for address_detail in Assembler.addr_data:
            if x_split[2] == address_detail[1]:
                print("call location: ")
                print(address_detail)
                break
            
        # second_machine_code = 
        # print("machine code: " + tool.check_size(second_machine_code))
        # text_file.write(tool.check_size(second_machine_code) + " ")
        
        # third_machine_code = 
        # print("machine code: " + tool.check_size(third_machine_code))
        # text_file.write(tool.check_size(third_machine_code) + " ")

        print("-------------------------------")


    def abnormal(x_split, text_file):
        first_machine_code = tool.check_format(tool.bin_to_hex("00010010"))
        print("machine code: " + tool.check_size(first_machine_code))
        text_file.write(tool.check_size(first_machine_code) + " ")
        
        second_machine_code = "00"
        print("machine code: " + tool.check_size(second_machine_code))
        text_file.write(tool.check_size(second_machine_code) + " ")
        
        third_machine_code = "00"
        print("machine code: " + tool.check_size(third_machine_code))
        text_file.write(tool.check_size(third_machine_code) + " ")

        print("-------------------------------")

class INC:
    def Ri(x_split, text_file):
        bin_machine_code = "0000011" + tool.check_format(x_split[1])
        hex_machine_code = tool.bin_to_hex(bin_machine_code)
        print("machine code: " + tool.check_size(hex_machine_code))
        text_file.write(tool.check_size(hex_machine_code) + " ")
        print("-------------------------------")


    def Rn(x_split, text_file):
        bin_machine_code = "00001" + tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        hex_machine_code = tool.bin_to_hex(bin_machine_code)
        print("machine code: " + tool.check_size(hex_machine_code))
        text_file.write(tool.check_size(hex_machine_code) + " ")
        print("-------------------------------")
'''
class JZ:
'''

class RET:
    def ret(x_split, text_file):
        machine_code = "00100010"
        hex_machine_code = tool.bin_to_hex(machine_code)
        print("machine code: "+hex_machine_code)
        text_file.write(hex_machine_code+" ")
        print("-------------------------------")
