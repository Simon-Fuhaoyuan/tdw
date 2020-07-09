# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class AvatarKinematic(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAvatarKinematic(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = AvatarKinematic()
        x.Init(buf, n + offset)
        return x

    # AvatarKinematic
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # AvatarKinematic
    def Id(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AvatarKinematic
    def Position(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarKinematic
    def Rotation(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .Quaternion import Quaternion
            obj = Quaternion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarKinematic
    def Forward(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def AvatarKinematicStart(builder): builder.StartObject(4)
def AvatarKinematicAddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def AvatarKinematicAddPosition(builder, position): builder.PrependStructSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def AvatarKinematicAddRotation(builder, rotation): builder.PrependStructSlot(2, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(rotation), 0)
def AvatarKinematicAddForward(builder, forward): builder.PrependStructSlot(3, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(forward), 0)
def AvatarKinematicEnd(builder): return builder.EndObject()
