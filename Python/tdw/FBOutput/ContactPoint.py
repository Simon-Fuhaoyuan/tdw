# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class ContactPoint(object):
    __slots__ = ['_tab']

    # ContactPoint
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # ContactPoint
    def Normal(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 0)
        return obj

    # ContactPoint
    def Point(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 12)
        return obj


def CreateContactPoint(builder, normal_x, normal_y, normal_z, point_x, point_y, point_z):
    builder.Prep(4, 24)
    builder.Prep(4, 12)
    builder.PrependFloat32(point_z)
    builder.PrependFloat32(point_y)
    builder.PrependFloat32(point_x)
    builder.Prep(4, 12)
    builder.PrependFloat32(normal_z)
    builder.PrependFloat32(normal_y)
    builder.PrependFloat32(normal_x)
    return builder.Offset()
