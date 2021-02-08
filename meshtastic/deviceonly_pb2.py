# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deviceonly.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mesh_pb2 as mesh__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deviceonly.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\nDeviceOnlyH\003',
  serialized_pb=b'\n\x10\x64\x65viceonly.proto\x1a\nmesh.proto\"\xab\x02\n\x0b\x44\x65viceState\x12\x1b\n\x05radio\x18\x01 \x01(\x0b\x32\x0c.RadioConfig\x12\x1c\n\x07my_node\x18\x02 \x01(\x0b\x32\x0b.MyNodeInfo\x12\x14\n\x05owner\x18\x03 \x01(\x0b\x32\x05.User\x12\x1a\n\x07node_db\x18\x04 \x03(\x0b\x32\t.NodeInfo\x12\"\n\rreceive_queue\x18\x05 \x03(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07version\x18\x08 \x01(\r\x12$\n\x0frx_text_message\x18\x07 \x01(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07no_save\x18\t \x01(\x08\x12\x15\n\rdid_gps_reset\x18\x0b \x01(\x08\x12,\n\x12secondary_channels\x18\x0c \x03(\x0b\x32\x10.ChannelSettingsB#\n\x13\x63om.geeksville.meshB\nDeviceOnlyH\x03\x62\x06proto3'
  ,
  dependencies=[mesh__pb2.DESCRIPTOR,])




_DEVICESTATE = _descriptor.Descriptor(
  name='DeviceState',
  full_name='DeviceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='radio', full_name='DeviceState.radio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='my_node', full_name='DeviceState.my_node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='DeviceState.owner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_db', full_name='DeviceState.node_db', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receive_queue', full_name='DeviceState.receive_queue', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='DeviceState.version', index=5,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_text_message', full_name='DeviceState.rx_text_message', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_save', full_name='DeviceState.no_save', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='did_gps_reset', full_name='DeviceState.did_gps_reset', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_channels', full_name='DeviceState.secondary_channels', index=9,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=332,
)

_DEVICESTATE.fields_by_name['radio'].message_type = mesh__pb2._RADIOCONFIG
_DEVICESTATE.fields_by_name['my_node'].message_type = mesh__pb2._MYNODEINFO
_DEVICESTATE.fields_by_name['owner'].message_type = mesh__pb2._USER
_DEVICESTATE.fields_by_name['node_db'].message_type = mesh__pb2._NODEINFO
_DEVICESTATE.fields_by_name['receive_queue'].message_type = mesh__pb2._MESHPACKET
_DEVICESTATE.fields_by_name['rx_text_message'].message_type = mesh__pb2._MESHPACKET
_DEVICESTATE.fields_by_name['secondary_channels'].message_type = mesh__pb2._CHANNELSETTINGS
DESCRIPTOR.message_types_by_name['DeviceState'] = _DEVICESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
