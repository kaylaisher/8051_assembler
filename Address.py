class MOVaddr:
    direct_direct_addr = 3
    reg_imm_addr = 2
    Rn_direct_addr = 2

class SUBBaddr:
    A_Ri_addr = 1
    A_Rn_addr = 1

class XRLaddr:
    direct_imm_addr = 3
    direct_A_addr = 2
    A_direct_addr = 2

class INCaddr:
    Ri_addr = 1
    Rn_addr = 1

class JZaddr:
    jz_addr = 2

class LCALLaddr:
    lcall_addr = 3

class RETaddr:
    ret_addr = 1

class Data:
    each_line = []
    addr_data = []
    addr_detail = []
    addr_index = 0
    current_addr_cnt = 0
    next_addr_cnt = 0


    