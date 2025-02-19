"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class body_control_data_lcmt(object):
    __slots__ = ["q", "qd", "timestamp_us"]

    def __init__(self):
        self.q = [ 0.0 for dim0 in range(29) ]
        self.qd = [ 0.0 for dim0 in range(29) ]
        self.timestamp_us = 0

    def encode(self):
        buf = BytesIO()
        buf.write(body_control_data_lcmt._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>29f', *self.q[:29]))
        buf.write(struct.pack('>29f', *self.qd[:29]))
        buf.write(struct.pack(">q", self.timestamp_us))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != body_control_data_lcmt._get_packed_fingerprint():
            raise ValueError("Decode error")
        return body_control_data_lcmt._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = body_control_data_lcmt()
        self.q = struct.unpack('>29f', buf.read(116))
        self.qd = struct.unpack('>29f', buf.read(116))
        self.timestamp_us = struct.unpack(">q", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if body_control_data_lcmt in parents: return 0
        tmphash = (0xfa781c9a388dfc5a) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if body_control_data_lcmt._packed_fingerprint is None:
            body_control_data_lcmt._packed_fingerprint = struct.pack(">Q", body_control_data_lcmt._get_hash_recursive([]))
        return body_control_data_lcmt._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

