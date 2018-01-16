import struct


class BinaryReader(object):

    def __init__(self, path):
        self._path = path
        self.fh = open(self._path, mode='rb')

    def read_7bit_encoded_int32(self):
        integer = 0
        shift = 0
        while True:
            current = struct.unpack('B', self.fh.read(1))[0]
            integer |= ((current & 0x7F) << shift)
            if (current & 128 == 0):
                break
            shift += 7
        return integer

    def read_int16(self):
        return struct.unpack('h', self.fh.read(2))[0]

    def read_int32(self):
        return struct.unpack('i', self.fh.read(4))[0]

    def read_double(self):
        return struct.unpack('d', self.fh.read(8))[0]

    def read_string(self):
        length = self.read_7bit_encoded_int32()
        return struct.unpack('%ds' % length, self.fh.read(length))[0]
