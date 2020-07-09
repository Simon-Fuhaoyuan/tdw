# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class VRRig(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVRRig(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = VRRig()
        x.Init(buf, n + offset)
        return x

    # VRRig
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # VRRig
    def Position(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VRRig
    def Rotation(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Quaternion import Quaternion
            obj = Quaternion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VRRig
    def Forward(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VRRig
    def LeftHand(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .SimpleTransform import SimpleTransform
            obj = SimpleTransform()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VRRig
    def RightHand(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .SimpleTransform import SimpleTransform
            obj = SimpleTransform()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VRRig
    def Head(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = o + self._tab.Pos
            from .SimpleTransform import SimpleTransform
            obj = SimpleTransform()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def VRRigStart(builder): builder.StartObject(6)
def VRRigAddPosition(builder, position): builder.PrependStructSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def VRRigAddRotation(builder, rotation): builder.PrependStructSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(rotation), 0)
def VRRigAddForward(builder, forward): builder.PrependStructSlot(2, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(forward), 0)
def VRRigAddLeftHand(builder, leftHand): builder.PrependStructSlot(3, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(leftHand), 0)
def VRRigAddRightHand(builder, rightHand): builder.PrependStructSlot(4, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(rightHand), 0)
def VRRigAddHead(builder, head): builder.PrependStructSlot(5, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(head), 0)
def VRRigEnd(builder): return builder.EndObject()
