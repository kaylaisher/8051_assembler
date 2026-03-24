class tool:

    def bin_to_hex(str):
        decimal_number = int(str, 2)
        hexadecimal_string = hex(decimal_number)
        return hexadecimal_string[2:]

    def check_format(raw_format):
        if raw_format:
            if raw_format[0] in ("@"):
                raw_format = raw_format[2:]
            if raw_format[-1] in ("H"):
                raw_format = raw_format[:-1]
                if raw_format[0] == "0":
                    raw_format = raw_format[1:]
            if raw_format[0] in ("#"):
                raw_format = raw_format[1:]
                if raw_format[0] == "0":
                    raw_format = raw_format[1:]
            if raw_format[0] in ("R"):
                if raw_format[-1] in (":"):
                    return raw_format
                else:
                    raw_format = raw_format[1:]
            if raw_format[0] in ("X"):
                raw_format = raw_format[1:]

            if raw_format[-1] in (":"):
                raw_format = raw_format[:-1]
            
        return raw_format

    #print(check_format("#0B3H"))

    def dec_to_3bit_bin(n):
        bit2 = (n >> 2) & 1
        bit1 = (n >> 1) & 1
        bit0 = (n >> 0) & 1

        return f"{bit2}{bit1}{bit0}"
    
    def dec_to_16bit_bin(n):
        bit15 = (n >> 15) & 1
        bit14 = (n >> 14) & 1
        bit13 = (n >> 13) & 1
        bit12 = (n >> 12) & 1
        bit11 = (n >> 11) & 1
        bit10 = (n >> 10) & 1
        bit9 = (n >> 9) & 1
        bit8 = (n >> 8) & 1
        bit7 = (n >> 7) & 1
        bit6 = (n >> 6) & 1
        bit5 = (n >> 5) & 1
        bit4 = (n >> 4) & 1
        bit3 = (n >> 3) & 1
        bit2 = (n >> 2) & 1
        bit1 = (n >> 1) & 1
        bit0 = (n >> 0) & 1

        return f"{bit15}{bit14}{bit13}{bit12}{bit11}{bit10}{bit9}{bit8}{bit7}{bit6}{bit5}{bit4}{bit3}{bit2}{bit1}{bit0}"

    def check_size(output):
        if len(output) == 1:
            output = "0" + output
        if len(output) > 2:
            output = output[-2:-1]

        return output.upper()
    
    def offset(label_location, current_location):
        result = label_location - current_location
        if result < 0:
            result = (abs(result)^0xFF) + 1
            result = f"{result:02X}"
            result = result.upper()

        return result