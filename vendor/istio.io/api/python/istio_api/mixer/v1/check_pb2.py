# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/v1/check.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from mixer.v1 import attributes_pb2 as mixer_dot_v1_dot_attributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/v1/check.proto',
  package='istio.mixer.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x14mixer/v1/check.proto\x12\x0eistio.mixer.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\x1a\x19mixer/v1/attributes.proto\"\xd0\x02\n\x0c\x43heckRequest\x12>\n\nattributes\x18\x01 \x01(\x0b\x32$.istio.mixer.v1.CompressedAttributesB\x04\xc8\xde\x1f\x00\x12\x19\n\x11global_word_count\x18\x02 \x01(\r\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x03 \x01(\t\x12>\n\x06quotas\x18\x04 \x03(\x0b\x32(.istio.mixer.v1.CheckRequest.QuotasEntryB\x04\xc8\xde\x1f\x00\x1a\x32\n\x0bQuotaParams\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\x12\x13\n\x0b\x62\x65st_effort\x18\x02 \x01(\x08\x1aW\n\x0bQuotasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.istio.mixer.v1.CheckRequest.QuotaParams:\x02\x38\x01\"\xc3\x05\n\rCheckResponse\x12L\n\x0cprecondition\x18\x02 \x01(\x0b\x32\x30.istio.mixer.v1.CheckResponse.PreconditionResultB\x04\xc8\xde\x1f\x00\x12?\n\x06quotas\x18\x03 \x03(\x0b\x32).istio.mixer.v1.CheckResponse.QuotasEntryB\x04\xc8\xde\x1f\x00\x1a\x98\x02\n\x12PreconditionResult\x12(\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xc8\xde\x1f\x00\x12;\n\x0evalid_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x17\n\x0fvalid_use_count\x18\x03 \x01(\x05\x12\x43\n\x15referenced_attributes\x18\x05 \x01(\x0b\x32$.istio.mixer.v1.ReferencedAttributes\x12\x37\n\x0froute_directive\x18\x06 \x01(\x0b\x32\x1e.istio.mixer.v1.RouteDirectiveJ\x04\x08\x04\x10\x05\x1a\xad\x01\n\x0bQuotaResult\x12;\n\x0evalid_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x16\n\x0egranted_amount\x18\x02 \x01(\x03\x12I\n\x15referenced_attributes\x18\x05 \x01(\x0b\x32$.istio.mixer.v1.ReferencedAttributesB\x04\xc8\xde\x1f\x00\x1aX\n\x0bQuotasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).istio.mixer.v1.CheckResponse.QuotaResult:\x02\x38\x01\"\xca\x02\n\x14ReferencedAttributes\x12\r\n\x05words\x18\x01 \x03(\t\x12T\n\x11\x61ttribute_matches\x18\x02 \x03(\x0b\x32\x33.istio.mixer.v1.ReferencedAttributes.AttributeMatchB\x04\xc8\xde\x1f\x00\x1a\x81\x01\n\x0e\x41ttributeMatch\x12\x0c\n\x04name\x18\x01 \x01(\x11\x12\x41\n\tcondition\x18\x02 \x01(\x0e\x32..istio.mixer.v1.ReferencedAttributes.Condition\x12\r\n\x05regex\x18\x03 \x01(\t\x12\x0f\n\x07map_key\x18\x04 \x01(\x11\"I\n\tCondition\x12\x19\n\x15\x43ONDITION_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x41\x42SENCE\x10\x01\x12\t\n\x05\x45XACT\x10\x02\x12\t\n\x05REGEX\x10\x03\"\x9e\x01\n\x0fHeaderOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12<\n\toperation\x18\x03 \x01(\x0e\x32).istio.mixer.v1.HeaderOperation.Operation\"0\n\tOperation\x12\x0b\n\x07REPLACE\x10\x00\x12\n\n\x06REMOVE\x10\x01\x12\n\n\x06\x41PPEND\x10\x02\"\xe1\x01\n\x0eRouteDirective\x12H\n\x19request_header_operations\x18\x01 \x03(\x0b\x32\x1f.istio.mixer.v1.HeaderOperationB\x04\xc8\xde\x1f\x00\x12I\n\x1aresponse_header_operations\x18\x02 \x03(\x0b\x32\x1f.istio.mixer.v1.HeaderOperationB\x04\xc8\xde\x1f\x00\x12\x1c\n\x14\x64irect_response_code\x18\x03 \x01(\r\x12\x1c\n\x14\x64irect_response_body\x18\x04 \x01(\tB#Z\x15istio.io/api/mixer/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,mixer_dot_v1_dot_attributes__pb2.DESCRIPTOR,])



_REFERENCEDATTRIBUTES_CONDITION = _descriptor.EnumDescriptor(
  name='Condition',
  full_name='istio.mixer.v1.ReferencedAttributes.Condition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONDITION_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABSENCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXACT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGEX', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1453,
  serialized_end=1526,
)
_sym_db.RegisterEnumDescriptor(_REFERENCEDATTRIBUTES_CONDITION)

_HEADEROPERATION_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='istio.mixer.v1.HeaderOperation.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REPLACE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPEND', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1639,
  serialized_end=1687,
)
_sym_db.RegisterEnumDescriptor(_HEADEROPERATION_OPERATION)


_CHECKREQUEST_QUOTAPARAMS = _descriptor.Descriptor(
  name='QuotaParams',
  full_name='istio.mixer.v1.CheckRequest.QuotaParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='istio.mixer.v1.CheckRequest.QuotaParams.amount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='best_effort', full_name='istio.mixer.v1.CheckRequest.QuotaParams.best_effort', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=394,
)

_CHECKREQUEST_QUOTASENTRY = _descriptor.Descriptor(
  name='QuotasEntry',
  full_name='istio.mixer.v1.CheckRequest.QuotasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.v1.CheckRequest.QuotasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.v1.CheckRequest.QuotasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=483,
)

_CHECKREQUEST = _descriptor.Descriptor(
  name='CheckRequest',
  full_name='istio.mixer.v1.CheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='istio.mixer.v1.CheckRequest.attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_word_count', full_name='istio.mixer.v1.CheckRequest.global_word_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deduplication_id', full_name='istio.mixer.v1.CheckRequest.deduplication_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quotas', full_name='istio.mixer.v1.CheckRequest.quotas', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKREQUEST_QUOTAPARAMS, _CHECKREQUEST_QUOTASENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=483,
)


_CHECKRESPONSE_PRECONDITIONRESULT = _descriptor.Descriptor(
  name='PreconditionResult',
  full_name='istio.mixer.v1.CheckResponse.PreconditionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='istio.mixer.v1.CheckResponse.PreconditionResult.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_duration', full_name='istio.mixer.v1.CheckResponse.PreconditionResult.valid_duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_use_count', full_name='istio.mixer.v1.CheckResponse.PreconditionResult.valid_use_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenced_attributes', full_name='istio.mixer.v1.CheckResponse.PreconditionResult.referenced_attributes', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route_directive', full_name='istio.mixer.v1.CheckResponse.PreconditionResult.route_directive', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=927,
)

_CHECKRESPONSE_QUOTARESULT = _descriptor.Descriptor(
  name='QuotaResult',
  full_name='istio.mixer.v1.CheckResponse.QuotaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid_duration', full_name='istio.mixer.v1.CheckResponse.QuotaResult.valid_duration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granted_amount', full_name='istio.mixer.v1.CheckResponse.QuotaResult.granted_amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenced_attributes', full_name='istio.mixer.v1.CheckResponse.QuotaResult.referenced_attributes', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=930,
  serialized_end=1103,
)

_CHECKRESPONSE_QUOTASENTRY = _descriptor.Descriptor(
  name='QuotasEntry',
  full_name='istio.mixer.v1.CheckResponse.QuotasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.v1.CheckResponse.QuotasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.v1.CheckResponse.QuotasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1105,
  serialized_end=1193,
)

_CHECKRESPONSE = _descriptor.Descriptor(
  name='CheckResponse',
  full_name='istio.mixer.v1.CheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='precondition', full_name='istio.mixer.v1.CheckResponse.precondition', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quotas', full_name='istio.mixer.v1.CheckResponse.quotas', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKRESPONSE_PRECONDITIONRESULT, _CHECKRESPONSE_QUOTARESULT, _CHECKRESPONSE_QUOTASENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=1193,
)


_REFERENCEDATTRIBUTES_ATTRIBUTEMATCH = _descriptor.Descriptor(
  name='AttributeMatch',
  full_name='istio.mixer.v1.ReferencedAttributes.AttributeMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.mixer.v1.ReferencedAttributes.AttributeMatch.name', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='istio.mixer.v1.ReferencedAttributes.AttributeMatch.condition', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regex', full_name='istio.mixer.v1.ReferencedAttributes.AttributeMatch.regex', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_key', full_name='istio.mixer.v1.ReferencedAttributes.AttributeMatch.map_key', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1322,
  serialized_end=1451,
)

_REFERENCEDATTRIBUTES = _descriptor.Descriptor(
  name='ReferencedAttributes',
  full_name='istio.mixer.v1.ReferencedAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='istio.mixer.v1.ReferencedAttributes.words', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute_matches', full_name='istio.mixer.v1.ReferencedAttributes.attribute_matches', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REFERENCEDATTRIBUTES_ATTRIBUTEMATCH, ],
  enum_types=[
    _REFERENCEDATTRIBUTES_CONDITION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1196,
  serialized_end=1526,
)


_HEADEROPERATION = _descriptor.Descriptor(
  name='HeaderOperation',
  full_name='istio.mixer.v1.HeaderOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.mixer.v1.HeaderOperation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.v1.HeaderOperation.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='istio.mixer.v1.HeaderOperation.operation', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEADEROPERATION_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1529,
  serialized_end=1687,
)


_ROUTEDIRECTIVE = _descriptor.Descriptor(
  name='RouteDirective',
  full_name='istio.mixer.v1.RouteDirective',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_header_operations', full_name='istio.mixer.v1.RouteDirective.request_header_operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_header_operations', full_name='istio.mixer.v1.RouteDirective.response_header_operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direct_response_code', full_name='istio.mixer.v1.RouteDirective.direct_response_code', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direct_response_body', full_name='istio.mixer.v1.RouteDirective.direct_response_body', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1690,
  serialized_end=1915,
)

_CHECKREQUEST_QUOTAPARAMS.containing_type = _CHECKREQUEST
_CHECKREQUEST_QUOTASENTRY.fields_by_name['value'].message_type = _CHECKREQUEST_QUOTAPARAMS
_CHECKREQUEST_QUOTASENTRY.containing_type = _CHECKREQUEST
_CHECKREQUEST.fields_by_name['attributes'].message_type = mixer_dot_v1_dot_attributes__pb2._COMPRESSEDATTRIBUTES
_CHECKREQUEST.fields_by_name['quotas'].message_type = _CHECKREQUEST_QUOTASENTRY
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['valid_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['referenced_attributes'].message_type = _REFERENCEDATTRIBUTES
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['route_directive'].message_type = _ROUTEDIRECTIVE
_CHECKRESPONSE_PRECONDITIONRESULT.containing_type = _CHECKRESPONSE
_CHECKRESPONSE_QUOTARESULT.fields_by_name['valid_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CHECKRESPONSE_QUOTARESULT.fields_by_name['referenced_attributes'].message_type = _REFERENCEDATTRIBUTES
_CHECKRESPONSE_QUOTARESULT.containing_type = _CHECKRESPONSE
_CHECKRESPONSE_QUOTASENTRY.fields_by_name['value'].message_type = _CHECKRESPONSE_QUOTARESULT
_CHECKRESPONSE_QUOTASENTRY.containing_type = _CHECKRESPONSE
_CHECKRESPONSE.fields_by_name['precondition'].message_type = _CHECKRESPONSE_PRECONDITIONRESULT
_CHECKRESPONSE.fields_by_name['quotas'].message_type = _CHECKRESPONSE_QUOTASENTRY
_REFERENCEDATTRIBUTES_ATTRIBUTEMATCH.fields_by_name['condition'].enum_type = _REFERENCEDATTRIBUTES_CONDITION
_REFERENCEDATTRIBUTES_ATTRIBUTEMATCH.containing_type = _REFERENCEDATTRIBUTES
_REFERENCEDATTRIBUTES.fields_by_name['attribute_matches'].message_type = _REFERENCEDATTRIBUTES_ATTRIBUTEMATCH
_REFERENCEDATTRIBUTES_CONDITION.containing_type = _REFERENCEDATTRIBUTES
_HEADEROPERATION.fields_by_name['operation'].enum_type = _HEADEROPERATION_OPERATION
_HEADEROPERATION_OPERATION.containing_type = _HEADEROPERATION
_ROUTEDIRECTIVE.fields_by_name['request_header_operations'].message_type = _HEADEROPERATION
_ROUTEDIRECTIVE.fields_by_name['response_header_operations'].message_type = _HEADEROPERATION
DESCRIPTOR.message_types_by_name['CheckRequest'] = _CHECKREQUEST
DESCRIPTOR.message_types_by_name['CheckResponse'] = _CHECKRESPONSE
DESCRIPTOR.message_types_by_name['ReferencedAttributes'] = _REFERENCEDATTRIBUTES
DESCRIPTOR.message_types_by_name['HeaderOperation'] = _HEADEROPERATION
DESCRIPTOR.message_types_by_name['RouteDirective'] = _ROUTEDIRECTIVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), dict(

  QuotaParams = _reflection.GeneratedProtocolMessageType('QuotaParams', (_message.Message,), dict(
    DESCRIPTOR = _CHECKREQUEST_QUOTAPARAMS,
    __module__ = 'mixer.v1.check_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckRequest.QuotaParams)
    ))
  ,

  QuotasEntry = _reflection.GeneratedProtocolMessageType('QuotasEntry', (_message.Message,), dict(
    DESCRIPTOR = _CHECKREQUEST_QUOTASENTRY,
    __module__ = 'mixer.v1.check_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckRequest.QuotasEntry)
    ))
  ,
  DESCRIPTOR = _CHECKREQUEST,
  __module__ = 'mixer.v1.check_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckRequest)
  ))
_sym_db.RegisterMessage(CheckRequest)
_sym_db.RegisterMessage(CheckRequest.QuotaParams)
_sym_db.RegisterMessage(CheckRequest.QuotasEntry)

CheckResponse = _reflection.GeneratedProtocolMessageType('CheckResponse', (_message.Message,), dict(

  PreconditionResult = _reflection.GeneratedProtocolMessageType('PreconditionResult', (_message.Message,), dict(
    DESCRIPTOR = _CHECKRESPONSE_PRECONDITIONRESULT,
    __module__ = 'mixer.v1.check_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckResponse.PreconditionResult)
    ))
  ,

  QuotaResult = _reflection.GeneratedProtocolMessageType('QuotaResult', (_message.Message,), dict(
    DESCRIPTOR = _CHECKRESPONSE_QUOTARESULT,
    __module__ = 'mixer.v1.check_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckResponse.QuotaResult)
    ))
  ,

  QuotasEntry = _reflection.GeneratedProtocolMessageType('QuotasEntry', (_message.Message,), dict(
    DESCRIPTOR = _CHECKRESPONSE_QUOTASENTRY,
    __module__ = 'mixer.v1.check_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckResponse.QuotasEntry)
    ))
  ,
  DESCRIPTOR = _CHECKRESPONSE,
  __module__ = 'mixer.v1.check_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.CheckResponse)
  ))
_sym_db.RegisterMessage(CheckResponse)
_sym_db.RegisterMessage(CheckResponse.PreconditionResult)
_sym_db.RegisterMessage(CheckResponse.QuotaResult)
_sym_db.RegisterMessage(CheckResponse.QuotasEntry)

ReferencedAttributes = _reflection.GeneratedProtocolMessageType('ReferencedAttributes', (_message.Message,), dict(

  AttributeMatch = _reflection.GeneratedProtocolMessageType('AttributeMatch', (_message.Message,), dict(
    DESCRIPTOR = _REFERENCEDATTRIBUTES_ATTRIBUTEMATCH,
    __module__ = 'mixer.v1.check_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.ReferencedAttributes.AttributeMatch)
    ))
  ,
  DESCRIPTOR = _REFERENCEDATTRIBUTES,
  __module__ = 'mixer.v1.check_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.ReferencedAttributes)
  ))
_sym_db.RegisterMessage(ReferencedAttributes)
_sym_db.RegisterMessage(ReferencedAttributes.AttributeMatch)

HeaderOperation = _reflection.GeneratedProtocolMessageType('HeaderOperation', (_message.Message,), dict(
  DESCRIPTOR = _HEADEROPERATION,
  __module__ = 'mixer.v1.check_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.HeaderOperation)
  ))
_sym_db.RegisterMessage(HeaderOperation)

RouteDirective = _reflection.GeneratedProtocolMessageType('RouteDirective', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEDIRECTIVE,
  __module__ = 'mixer.v1.check_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.RouteDirective)
  ))
_sym_db.RegisterMessage(RouteDirective)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\025istio.io/api/mixer/v1\310\341\036\000\250\342\036\000\360\341\036\000'))
_CHECKREQUEST_QUOTASENTRY.has_options = True
_CHECKREQUEST_QUOTASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CHECKREQUEST.fields_by_name['attributes'].has_options = True
_CHECKREQUEST.fields_by_name['attributes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CHECKREQUEST.fields_by_name['quotas'].has_options = True
_CHECKREQUEST.fields_by_name['quotas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['status'].has_options = True
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['status']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['valid_duration'].has_options = True
_CHECKRESPONSE_PRECONDITIONRESULT.fields_by_name['valid_duration']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_CHECKRESPONSE_QUOTARESULT.fields_by_name['valid_duration'].has_options = True
_CHECKRESPONSE_QUOTARESULT.fields_by_name['valid_duration']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_CHECKRESPONSE_QUOTARESULT.fields_by_name['referenced_attributes'].has_options = True
_CHECKRESPONSE_QUOTARESULT.fields_by_name['referenced_attributes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CHECKRESPONSE_QUOTASENTRY.has_options = True
_CHECKRESPONSE_QUOTASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CHECKRESPONSE.fields_by_name['precondition'].has_options = True
_CHECKRESPONSE.fields_by_name['precondition']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CHECKRESPONSE.fields_by_name['quotas'].has_options = True
_CHECKRESPONSE.fields_by_name['quotas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_REFERENCEDATTRIBUTES.fields_by_name['attribute_matches'].has_options = True
_REFERENCEDATTRIBUTES.fields_by_name['attribute_matches']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_ROUTEDIRECTIVE.fields_by_name['request_header_operations'].has_options = True
_ROUTEDIRECTIVE.fields_by_name['request_header_operations']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_ROUTEDIRECTIVE.fields_by_name['response_header_operations'].has_options = True
_ROUTEDIRECTIVE.fields_by_name['response_header_operations']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
