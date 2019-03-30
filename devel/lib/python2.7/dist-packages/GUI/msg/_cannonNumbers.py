# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from GUI/cannonNumbers.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class cannonNumbers(genpy.Message):
  _md5sum = "b96d3a629a34dfd2040e80b4afc99711"
  _type = "GUI/cannonNumbers"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 r1
float64 r2
float64 r3
float64 l
float64 vol
float64 weight
"""
  __slots__ = ['r1','r2','r3','l','vol','weight']
  _slot_types = ['float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       r1,r2,r3,l,vol,weight

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(cannonNumbers, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.r1 is None:
        self.r1 = 0.
      if self.r2 is None:
        self.r2 = 0.
      if self.r3 is None:
        self.r3 = 0.
      if self.l is None:
        self.l = 0.
      if self.vol is None:
        self.vol = 0.
      if self.weight is None:
        self.weight = 0.
    else:
      self.r1 = 0.
      self.r2 = 0.
      self.r3 = 0.
      self.l = 0.
      self.vol = 0.
      self.weight = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6d().pack(_x.r1, _x.r2, _x.r3, _x.l, _x.vol, _x.weight))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 48
      (_x.r1, _x.r2, _x.r3, _x.l, _x.vol, _x.weight,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6d().pack(_x.r1, _x.r2, _x.r3, _x.l, _x.vol, _x.weight))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 48
      (_x.r1, _x.r2, _x.r3, _x.l, _x.vol, _x.weight,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d