# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wifi_credential_specifics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wifi_credential_specifics.proto',
  package='sync_pb',
  serialized_pb='\n\x1fwifi_credential_specifics.proto\x12\x07sync_pb\"\xf9\x01\n\x17WifiCredentialSpecifics\x12\x0c\n\x04ssid\x18\x01 \x01(\x0c\x12\x46\n\x0esecurity_class\x18\x02 \x01(\x0e\x32..sync_pb.WifiCredentialSpecifics.SecurityClass\x12\x12\n\npassphrase\x18\x03 \x01(\x0c\"t\n\rSecurityClass\x12\x1a\n\x16SECURITY_CLASS_INVALID\x10\x00\x12\x17\n\x13SECURITY_CLASS_NONE\x10\x01\x12\x16\n\x12SECURITY_CLASS_WEP\x10\x02\x12\x16\n\x12SECURITY_CLASS_PSK\x10\x03\x42\x04H\x03`\x01')



_WIFICREDENTIALSPECIFICS_SECURITYCLASS = _descriptor.EnumDescriptor(
  name='SecurityClass',
  full_name='sync_pb.WifiCredentialSpecifics.SecurityClass',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SECURITY_CLASS_INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECURITY_CLASS_NONE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECURITY_CLASS_WEP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECURITY_CLASS_PSK', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=178,
  serialized_end=294,
)


_WIFICREDENTIALSPECIFICS = _descriptor.Descriptor(
  name='WifiCredentialSpecifics',
  full_name='sync_pb.WifiCredentialSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='sync_pb.WifiCredentialSpecifics.ssid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='security_class', full_name='sync_pb.WifiCredentialSpecifics.security_class', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passphrase', full_name='sync_pb.WifiCredentialSpecifics.passphrase', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WIFICREDENTIALSPECIFICS_SECURITYCLASS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=294,
)

_WIFICREDENTIALSPECIFICS.fields_by_name['security_class'].enum_type = _WIFICREDENTIALSPECIFICS_SECURITYCLASS
_WIFICREDENTIALSPECIFICS_SECURITYCLASS.containing_type = _WIFICREDENTIALSPECIFICS;
DESCRIPTOR.message_types_by_name['WifiCredentialSpecifics'] = _WIFICREDENTIALSPECIFICS

class WifiCredentialSpecifics(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WIFICREDENTIALSPECIFICS

  # @@protoc_insertion_point(class_scope:sync_pb.WifiCredentialSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003`\001')
# @@protoc_insertion_point(module_scope)
