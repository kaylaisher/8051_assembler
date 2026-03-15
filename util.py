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

            if raw_format[-1] in (":"):
                raw_format = raw_format[:-1]
            
        return raw_format

    #print(check_format("#0B3H"))

    def dec_to_3bit_bin(n):
        bit2 = (n >> 2) & 1
        bit1 = (n >> 1) & 1
        bit0 = (n >> 0) & 1

        return f"{bit2}{bit1}{bit0}"

    def check_size(output):
        if len(output) == 1:
            output = "0" + output

        return output.upper()