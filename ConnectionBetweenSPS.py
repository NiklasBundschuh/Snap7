import snap7.client 
from snap7.util import *
from snap7.types import *


def ReadMemory(plc, byte, bit, datatype):
    result = plc.read_area(areas['MK'], 0, byte, datatype)
    if datatype == S7WLBit:
        return get_bool(result,0,1)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return get_int(result,0)
    elif datatype == S7WLReal:
        return get_real(result,0) 
    elif datatype == S7WLDWord:
        return get_dword(result,0)
    else:
        return None

if __name__=="__main__":
    plc = snap7.client.Client()
    plc.connect('10.10.54.2', 0,1) #other IP address
    print:(ReadMemory(plc, 100, 0, S7WLReal))
    print:(ReadMemory (plc, 120, 0, S7WLWord))
    