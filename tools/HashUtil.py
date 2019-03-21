HEX_PREFIX = "0x"
INT32_HEX_WIDTH = 8
INT64_HEX_WIDTH = 16


class HexString:
    def __init__(self, hex):
        self.__radix = 16
        self.__hex_hash = hex.lstrip(HEX_PREFIX)
        self.__supported_hex_width = [2, 4, 8, 16, 32, 64]

    def __to_int(self, hexStr):
        return int(hexStr, self.__radix)

    def split(self, width):
        #print(self.__hex_hash)
        result = list()
        count = int(len(self.__hex_hash)/width + 1)
        for i in range(count):
            if i == 0:
                result.insert(0, HEX_PREFIX + self.__hex_hash[-width:])
            else:
                f = self.__hex_hash[-((i+1)*width): -(i*width)]
                if len(f) > 0:
                    result.insert(0, HEX_PREFIX + f)

        return result

    def toBigInt(self):
        return self.__to_int(self.__hex_hash)

    def toInt64Fields(self):
        result = list()
        if len(self.__hex_hash) > INT64_HEX_WIDTH:
            fileds = self.split(INT64_HEX_WIDTH)
            #print(fileds)
            for fs in fileds:
                result.append(self.__to_int(fs))
        else:
            result.append(self.__to_int(self.__hex_hash))

        return result

    def toInt32Fields(self):
        result = list()
        if len(self.__hex_hash) > INT32_HEX_WIDTH:
            fileds = self.split(INT32_HEX_WIDTH)
            #print(fileds)
            for fs in fileds:
                result.append(self.__to_int(fs))
        else:
            result.append(self.__to_int(self.__hex_hash))

        return result

    @staticmethod
    def fromInt32Fields(int32_ls):
        hexPresentation = "0x"
        for int32 in int32_ls:
            hexPresentation += hex(int32).lstrip("0x")
        return hexPresentation

    @staticmethod
    def fromInt64Fields(int64_ls):
        hexPresentation = "0x"
        for int64 in int64_ls:
            hexPresentation += hex(int64).lstrip("0x")
        return hexPresentation
        return


def main():
    hs = HexString("0xf71582CCFcd5fEA5Af8324B0F0Efe470D4d4Ec09")
    print(hs.toBigInt())
    int64List = hs.toInt64Fields()
    int32List = hs.toInt32Fields()
    print(int64List)
    print(int32List)

    print(HexString.fromInt64Fields(int64List))
    print(HexString.fromInt32Fields(int32List))


if __name__ == '__main__':
    main()
