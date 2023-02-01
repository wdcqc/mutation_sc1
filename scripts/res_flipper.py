import os, struct, argparse
from common import SCUnit

def flip_units(fn, ofn, root):
    with open(os.path.join(root, fn), "rb") as fp:
        data = fp.read()
            
    ofs = data.find(b'DIM ')
    assert ofs == data.rfind(b'DIM '), 'multiple DIM sections'
    assert data[ofs + 4 : ofs + 8] == b'\x04\x00\x00\x00', 'wrong DIM length'
    
    dim = struct.unpack("<HH", data[ofs + 8 : ofs + 12])
    map_x = dim[0] * 32
    map_y = dim[1] * 32
            
    ofs = data.find(b'UNIT')
    assert ofs == data.rfind(b'UNIT'), 'multiple UNIT sections'

    data_len, = struct.unpack("<I", data[ofs + 4 : ofs + 8])

    assert data_len % 36 == 0, data_len
    unit_count = data_len // 36
    data_units = [struct.unpack("<I6H4BIHHII", data[ofs + 8 + i * 36 : ofs + 8 + (1+i) * 36]) for i in range(unit_count)]

    units = [SCUnit(u) for u in data_units]
    units_flipped = [SCUnit(u) for u in data_units]
    
    for u in units_flipped:
        if u.owner >= 8:
            u.x = map_x - u.x

    units = units + units_flipped
        
    new_chk_data = data[: ofs + 4] + struct.pack('<I', len(units) * 36) + b''.join(u.data() for u in units) + data[ofs + 8 + unit_count * 36 :]
    
    with open(os.path.join(root, ofn), "wb") as fp:
        fp.write(new_chk_data)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "unit flipper, sort of like house flipper")
    parser.add_argument("--path", "-p", type=str, default = r".", help = "path to chk files")
    parser.add_argument("infile", type=str, help = "input chk file")
    parser.add_argument("outfile", type=str, help = "output chk file")
    args = parser.parse_args()

    flip_units(args.infile, args.outfile, args.path)