from dataclasses import dataclass, field


DATA = '220D4B80491FE6FBDCDA61F23F1D9B763004A7C128012F9DA88CE27B000B30F4804D49CD515380352100763DC5E8EC000844338B10B667A1E60094B7BE8D600ACE774DF39DD364979F67A9AC0D1802B2A41401354F6BF1DC0627B15EC5CCC01694F5BABFC00964E93C95CF080263F0046741A740A76B704300824926693274BE7CC880267D00464852484A5F74520005D65A1EAD2334A700BA4EA41256E4BBBD8DC0999FC3A97286C20164B4FF14A93FD2947494E683E752E49B2737DF7C4080181973496509A5B9A8D37B7C300434016920D9EAEF16AEC0A4AB7DF5B1C01C933B9AAF19E1818027A00A80021F1FA0E43400043E174638572B984B066401D3E802735A4A9ECE371789685AB3E0E800725333EFFBB4B8D131A9F39ED413A1720058F339EE32052D48EC4E5EC3A6006CC2B4BE6FF3F40017A0E4D522226009CA676A7600980021F1921446700042A23C368B713CC015E007324A38DF30BB30533D001200F3E7AC33A00A4F73149558E7B98A4AACC402660803D1EA1045C1006E2CC668EC200F4568A5104802B7D004A53819327531FE607E118803B260F371D02CAEA3486050004EE3006A1E463858600F46D8531E08010987B1BE251002013445345C600B4F67617400D14F61867B39AA38018F8C05E430163C6004980126005B801CC0417080106005000CB4002D7A801AA0062007BC0019608018A004A002B880057CEF5604016827238DFDCC8048B9AF135802400087C32893120401C8D90463E280513D62991EE5CA543A6B75892CB639D503004F00353100662FC498AA00084C6485B1D25044C0139975D004A5EB5E52AC7233294006867F9EE6BA2115E47D7867458401424E354B36CDAFCAB34CBC2008BF2F2BA5CC646E57D4C62E41279E7F37961ACC015B005A5EFF884CBDFF10F9BFF438C014A007D67AE0529DED3901D9CD50B5C0108B13BAFD6070'


@dataclass
class BasePacket:
    version: int
    type_id: int


@dataclass
class LiteralPacket(BasePacket):
    value: int
    length: int

    def compute(self):
        return self.value

@dataclass
class OperatorPacket(BasePacket):
    length_type: int
    sub_length: int
    length: int
    subpackages: list[BasePacket] = field(default_factory=list)

    def compute(self):
        match self.type_id:
            case 0:
                return sum(s.compute() for s in self.subpackages)
            case 1:
                res = 1
                for p in self.subpackages:
                    res *= p.compute()
                return res
            case 2:
                return min(s.compute() for s in self.subpackages)
            case 3:
                return max(s.compute() for s in self.subpackages)
            case 5:
                return self.subpackages[0].compute() > self.subpackages[1].compute()
            case 6:
                return self.subpackages[0].compute() < self.subpackages[1].compute()
            case 7:
                return self.subpackages[0].compute() == self.subpackages[1].compute()
            case _:
                raise Exception('Not an operator package')


def to_binary(data):
    x = int(data, 16)
    s = f'{x:b}'
    s = '0' * ((4 - (len(s) % 4)) % 4) + s
    return s


def decode_header(bits):
    return int(bits[:3], 2), int(bits[3:6], 2)


def decode_packet(bits):
    version, type_id = decode_header(bits)
    if type_id == 4:
        return decode_literal(bits)
    else:
        return decode_operator(bits)


def decode_literal(bits):
    v, t = decode_header(bits)
    trunc = bits[6:]
    nums = []
    i = 0
    while True:
        j = i * 5
        nums.append(trunc[j+1: j+5])
        if trunc[j] == '0':
            break
        i += 1
    return LiteralPacket(v, t, int(''.join(nums), 2), i*5+11)


def decode_operator(bits):
    v, t = decode_header(bits)
    trunc = bits[6:]
    length_bit = int(trunc[0], 2)
    sub = []
    this_length = 7
    if length_bit == 0:
        this_length += 15
        sub_length = int(trunc[1:16], 2)
        decode_packet(trunc[16:])
        i = 0
        while i < sub_length:
            packet = decode_packet(trunc[16+i:])
            i += packet.length
            sub.append(packet)
        this_length += i
    elif length_bit == 1:
        this_length += 11
        sub_length = int(trunc[1:12], 2)
        inc = 0
        for i in range(sub_length):
            packet = decode_packet(trunc[12+inc:])
            sub.append(packet)
            this_length += packet.length
            inc += packet.length
    return OperatorPacket(v, t, length_bit, sub_length, this_length, sub)


def sum_version_numbers(packet):
    acc = packet.version
    if isinstance(packet, OperatorPacket):  # This also can be done with inheritance
        for p in packet.subpackages:
            acc += sum_version_numbers(p)
    return acc


def compute_equation(packet):
    acc = packet.version
    if isinstance(packet, OperatorPacket):
        for p in packet.subpackages:
            acc += sum_version_numbers(p)
    return acc


def main():
    data = to_binary(DATA)
    top_packet = decode_packet(data)
    total = sum_version_numbers(top_packet)
    print(total)
    # Task 2
    res = top_packet.compute()
    print(res)


if __name__ == '__main__':
    main()
