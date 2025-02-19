"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

from io import BytesIO
import struct

class command_lcmt(object):

    __slots__ = ["command"]

    __typenames__ = ["double"]

    __dimensions__ = [[4]]

    def __init__(self):
        self.command = [ 0.0 for dim0 in range(4) ]
        """ LCM Type: double[4] """

    def encode(self):
        buf = BytesIO()
        buf.write(command_lcmt._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>4d', *self.command[:4]))

    @staticmethod
    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != command_lcmt._get_packed_fingerprint():
            raise ValueError("Decode error")
        return command_lcmt._decode_one(buf)

    @staticmethod
    def _decode_one(buf):
        self = command_lcmt()
        self.command = struct.unpack('>4d', buf.read(32))
        return self

    @staticmethod
    def _get_hash_recursive(parents):
        if command_lcmt in parents: return 0
        tmphash = (0x507a292ea92a57d0) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _packed_fingerprint = None

    @staticmethod
    def _get_packed_fingerprint():
        if command_lcmt._packed_fingerprint is None:
            command_lcmt._packed_fingerprint = struct.pack(">Q", command_lcmt._get_hash_recursive([]))
        return command_lcmt._packed_fingerprint

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", command_lcmt._get_packed_fingerprint())[0]

