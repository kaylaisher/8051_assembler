from tool import tool

output_file_path = "Test01-out.txt"
text_file = "Test01.txt"

class MOV:

    def direct_direct(x_split, text_file):
        #with open(output_file_path, 'w') as text_file:

        text_file.write(tool.bin_to_hex("10000101")+" ")
        print("machine code: "+ tool.bin_to_hex("10000101") +"\n")
        
        text_file.write(tool.check_format(x_split[2])+" ")
        print("machine code: "+ tool.check_format(x_split[2])+"\n")
        
        text_file.write(tool.check_format(x_split[1])+" ")
        print("machine code: "+ tool.check_format(x_split[1])+"\n")
        print("-------------------------------")

    def reg_imm(x_split, text_file):
        #with open(output_file_path, 'w') as text_file:

        #print("MOV @Ri, #imm: "+x_split[1])
        decimal_machine_code = "0111011"+tool.check_format(x_split[1])
        print("decimal: "+decimal_machine_code)
        #print("hexadecimal: "+bin_to_hex(decimal_machine_code))
        hex_machine_code = tool.bin_to_hex(decimal_machine_code)
        text_file.write(hex_machine_code+" ")
        print("machine code: "+ hex_machine_code+"\n")

        text_file.write(tool.check_format(x_split[2])+" ")
        print("machine code: "+ tool.check_format(x_split[2])+"\n")
        
        print("-------------------------------")

    def Rn_direct(x_split, text_file):
        decimal_machine_code = "10101"+ tool.dec_to_3bit_bin(int(tool.check_format(x_split[1])))
        #print("decimal machine code: "+decimal_machine_code)
        hex_machine_code = tool.bin_to_hex(decimal_machine_code).upper()
        print("hex machine code: "+hex_machine_code)
        text_file.write(hex_machine_code+" ")
        print("machine code: " + tool.check_format(x_split[2]))
        text_file.write(tool.check_format(x_split[2])+" ")

        print("-------------------------------")

