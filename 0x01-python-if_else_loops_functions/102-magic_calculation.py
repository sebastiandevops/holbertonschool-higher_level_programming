#!/usr/bin/python3
def magic_calculation(a, b, c):
    bytecode = dis.code_info(magic_calculation)
    for instr in bytecode:
        print(instr.opname)
        return bytecode
