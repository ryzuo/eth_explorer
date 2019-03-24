from decimal import *

HEX_PREFIX = "0x"
INT32_HEX_WIDTH = 8
INT64_HEX_WIDTH = 16

INT32_DEC_WIDTH = 10
INT64_DEC_WIDTH = 19


class HexString:
    def __init__(self, hex):
        self.__radix = 16
        self.__value = hex
        self.__hex_hash = hex.lstrip(HEX_PREFIX)
        self.__supported_hex_width = [2, 4, 8, 16, 32, 64]

    """
    def __set__(self, instance, value):
        if isinstance(value, int):
            self.__value = hex(value)
        elif isinstance(value, str) and value.startswith("0x"):
            self.__value = value
        else:
            self.__value = "0x0"

    def __get__(self, instance, value):
        return self.__value
    """

    def __to_int(self, hexStr):
        return int(hexStr, self.__radix)

    @property
    def value(self):
        return self.__value

    def split(self, width):
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

    def splitToInt32(self):
        result = list()
        bigint = self.__to_int(self.__hex_hash)
        bigintStr = str(bigint)
        count = int(len(bigintStr)/INT32_DEC_WIDTH + 1)
        for i in range(count):
            if i == 0:
                result.insert(0, bigintStr[-INT32_DEC_WIDTH:])
            else:
                f = bigintStr[-((i+1)*INT32_DEC_WIDTH): -(i*INT32_DEC_WIDTH)]
                if len(f) > 0:
                    result.insert(0, int(f))

        return result

    def splitToInt64(self):
        result = list()
        bigint = self.__to_int(self.__hex_hash)
        bigintStr = str(bigint)
        count = int(len(bigintStr)/INT64_DEC_WIDTH + 1)
        for i in range(count):
            if i == 0:
                result.insert(0, int(bigintStr[-INT64_DEC_WIDTH:]))
            else:
                f = bigintStr[-((i+1)*INT64_DEC_WIDTH): -(i*INT64_DEC_WIDTH)]
                if len(f) > 0:
                    result.insert(0, int(f))

        return result

    @property
    def integer(self):
        return self.__to_int(self.__hex_hash)

    def toDecimal(self, precision):
        bigint = int(self.__hex_hash, 16)
        print(bigint)
        getcontext().prec = precision
        dec = Decimal(bigint)/pow(10, precision)
        print(dec)
        #dec.

    @staticmethod
    def fromInt32Fields(int32_ls):
        hexRep = ""
        for int32 in int32_ls:
            int32Str = str(int32)
            int32Str = int32Str.zfill(INT32_DEC_WIDTH)
            hexRep += int32Str
        return HexString(hex(int(hexRep)))

    @staticmethod
    def fromInt64Fields(int64_ls):
        hexRep = ""
        for int64 in int64_ls:
            int64Str = str(int64)
            int64Str = int64Str.zfill(INT64_DEC_WIDTH)
            hexRep += int64Str
        return HexString(hex(int(hexRep)))

    @staticmethod
    def fromInteger(number):
        return HexString(hex(number))


def main():
    hs = HexString("0xf71582CCFcd5fEA5Af8324B0F0Efe470D4d4Ec09")
    #hs = HexString("0x535cd6a35508000")
    int64List = hs.splitToInt64()
    #int32List = hs.splitToInt32()
    print(int64List)
    #print(int32List)

    #print(hs.fromInt64Fields(int64List))
    #print(hs.fromInt32Fields(int32List))

    hs.toDecimal(18)


if __name__ == '__main__':
    main()
