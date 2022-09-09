# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2
from . import config_pb2 as config__pb2
from . import device_metadata_pb2 as device__metadata__pb2
from . import mesh_pb2 as mesh__pb2
from . import module_config_pb2 as module__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64min.proto\x1a\rchannel.proto\x1a\x0c\x63onfig.proto\x1a\x15\x64\x65vice_metadata.proto\x1a\nmesh.proto\x1a\x13module_config.proto\"\xd5\n\n\x0c\x41\x64minMessage\x12\x1d\n\x13get_channel_request\x18\x01 \x01(\rH\x00\x12(\n\x14get_channel_response\x18\x02 \x01(\x0b\x32\x08.ChannelH\x00\x12\x1b\n\x11get_owner_request\x18\x03 \x01(\x08H\x00\x12#\n\x12get_owner_response\x18\x04 \x01(\x0b\x32\x05.UserH\x00\x12\x36\n\x12get_config_request\x18\x05 \x01(\x0e\x32\x18.AdminMessage.ConfigTypeH\x00\x12&\n\x13get_config_response\x18\x06 \x01(\x0b\x32\x07.ConfigH\x00\x12\x43\n\x19get_module_config_request\x18\x07 \x01(\x0e\x32\x1e.AdminMessage.ModuleConfigTypeH\x00\x12\x33\n\x1aget_module_config_response\x18\x08 \x01(\x0b\x32\r.ModuleConfigH\x00\x12!\n\x17get_all_channel_request\x18\t \x01(\x08H\x00\x12\x34\n*get_canned_message_module_messages_request\x18\n \x01(\x08H\x00\x12\x35\n+get_canned_message_module_messages_response\x18\x0b \x01(\tH\x00\x12%\n\x1bget_device_metadata_request\x18\x0c \x01(\rH\x00\x12\x37\n\x1cget_device_metadata_response\x18\r \x01(\x0b\x32\x0f.DeviceMetadataH\x00\x12\x1a\n\tset_owner\x18  \x01(\x0b\x32\x05.UserH\x00\x12\x1f\n\x0bset_channel\x18! \x01(\x0b\x32\x08.ChannelH\x00\x12\x1d\n\nset_config\x18\" \x01(\x0b\x32\x07.ConfigH\x00\x12*\n\x11set_module_config\x18# \x01(\x0b\x32\r.ModuleConfigH\x00\x12,\n\"set_canned_message_module_messages\x18$ \x01(\tH\x00\x12\x1c\n\x12\x63onfirm_set_config\x18@ \x01(\x08H\x00\x12#\n\x19\x63onfirm_set_module_config\x18\x41 \x01(\x08H\x00\x12\x1d\n\x13\x63onfirm_set_channel\x18\x42 \x01(\x08H\x00\x12\x1b\n\x11\x63onfirm_set_radio\x18\x43 \x01(\x08H\x00\x12\x18\n\x0e\x65xit_simulator\x18` \x01(\x08H\x00\x12\x18\n\x0ereboot_seconds\x18\x61 \x01(\x05H\x00\x12\x1a\n\x10shutdown_seconds\x18\x62 \x01(\x05H\x00\x12\x17\n\rfactory_reset\x18\x63 \x01(\x05H\x00\"\x95\x01\n\nConfigType\x12\x11\n\rDEVICE_CONFIG\x10\x00\x12\x13\n\x0fPOSITION_CONFIG\x10\x01\x12\x10\n\x0cPOWER_CONFIG\x10\x02\x12\x12\n\x0eNETWORK_CONFIG\x10\x03\x12\x12\n\x0e\x44ISPLAY_CONFIG\x10\x04\x12\x0f\n\x0bLORA_CONFIG\x10\x05\x12\x14\n\x10\x42LUETOOTH_CONFIG\x10\x06\"\xa6\x01\n\x10ModuleConfigType\x12\x0f\n\x0bMQTT_CONFIG\x10\x00\x12\x11\n\rSERIAL_CONFIG\x10\x01\x12\x13\n\x0f\x45XTNOTIF_CONFIG\x10\x02\x12\x17\n\x13STOREFORWARD_CONFIG\x10\x03\x12\x14\n\x10RANGETEST_CONFIG\x10\x04\x12\x14\n\x10TELEMETRY_CONFIG\x10\x05\x12\x14\n\x10\x43\x41NNEDMSG_CONFIG\x10\x06\x42\x11\n\x0fpayload_variantBG\n\x13\x63om.geeksville.meshB\x0b\x41\x64minProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3')



_ADMINMESSAGE = DESCRIPTOR.message_types_by_name['AdminMessage']
_ADMINMESSAGE_CONFIGTYPE = _ADMINMESSAGE.enum_types_by_name['ConfigType']
_ADMINMESSAGE_MODULECONFIGTYPE = _ADMINMESSAGE.enum_types_by_name['ModuleConfigType']
AdminMessage = _reflection.GeneratedProtocolMessageType('AdminMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADMINMESSAGE,
  '__module__' : 'admin_pb2'
  # @@protoc_insertion_point(class_scope:AdminMessage)
  })
_sym_db.RegisterMessage(AdminMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\013AdminProtosH\003Z!github.com/meshtastic/gomeshproto'
  _ADMINMESSAGE._serialized_start=101
  _ADMINMESSAGE._serialized_end=1466
  _ADMINMESSAGE_CONFIGTYPE._serialized_start=1129
  _ADMINMESSAGE_CONFIGTYPE._serialized_end=1278
  _ADMINMESSAGE_MODULECONFIGTYPE._serialized_start=1281
  _ADMINMESSAGE_MODULECONFIGTYPE._serialized_end=1447
# @@protoc_insertion_point(module_scope)
