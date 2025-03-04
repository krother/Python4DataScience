# SPDX-FileCopyrightText: 2021 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="accounts.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0e\x61\x63\x63ounts.proto"3\n\x07\x41\x63\x63ount\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x02 \x01(\t"M\n\x14\x43reateAccountRequest\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t"0\n\x13\x43reateAccountResult\x12\x19\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x08.Account"/\n\x12GetAccountsRequest\x12\x19\n\x07\x61\x63\x63ount\x18\x01 \x03(\x0b\x32\x08.Account".\n\x11GetAccountsResult\x12\x19\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x08.Account2\x82\x01\n\x08\x41\x63\x63ounts\x12<\n\rCreateAccount\x12\x15.CreateAccountRequest\x1a\x14.CreateAccountResult\x12\x38\n\x0bGetAccounts\x12\x13.GetAccountsRequest\x1a\x12.GetAccountsResult0\x01\x62\x06proto3',
)


_ACCOUNT = _descriptor.Descriptor(
    name="Account",
    full_name="Account",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="account_id",
            full_name="Account.account_id",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="account_name",
            full_name="Account.account_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=18,
    serialized_end=69,
)


_CREATEACCOUNTREQUEST = _descriptor.Descriptor(
    name="CreateAccountRequest",
    full_name="CreateAccountRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="account_name",
            full_name="CreateAccountRequest.account_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="CreateAccountRequest.password",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="email",
            full_name="CreateAccountRequest.email",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=71,
    serialized_end=148,
)


_CREATEACCOUNTRESULT = _descriptor.Descriptor(
    name="CreateAccountResult",
    full_name="CreateAccountResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="account",
            full_name="CreateAccountResult.account",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=150,
    serialized_end=198,
)


_GETACCOUNTSREQUEST = _descriptor.Descriptor(
    name="GetAccountsRequest",
    full_name="GetAccountsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="account",
            full_name="GetAccountsRequest.account",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=200,
    serialized_end=247,
)


_GETACCOUNTSRESULT = _descriptor.Descriptor(
    name="GetAccountsResult",
    full_name="GetAccountsResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="account",
            full_name="GetAccountsResult.account",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=249,
    serialized_end=295,
)

_CREATEACCOUNTRESULT.fields_by_name["account"].message_type = _ACCOUNT
_GETACCOUNTSREQUEST.fields_by_name["account"].message_type = _ACCOUNT
_GETACCOUNTSRESULT.fields_by_name["account"].message_type = _ACCOUNT
DESCRIPTOR.message_types_by_name["Account"] = _ACCOUNT
DESCRIPTOR.message_types_by_name["CreateAccountRequest"] = _CREATEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name["CreateAccountResult"] = _CREATEACCOUNTRESULT
DESCRIPTOR.message_types_by_name["GetAccountsRequest"] = _GETACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name["GetAccountsResult"] = _GETACCOUNTSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType(
    "Account",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACCOUNT,
        "__module__": "accounts_pb2"
        # @@protoc_insertion_point(class_scope:Account)
    },
)
_sym_db.RegisterMessage(Account)

CreateAccountRequest = _reflection.GeneratedProtocolMessageType(
    "CreateAccountRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEACCOUNTREQUEST,
        "__module__": "accounts_pb2"
        # @@protoc_insertion_point(class_scope:CreateAccountRequest)
    },
)
_sym_db.RegisterMessage(CreateAccountRequest)

CreateAccountResult = _reflection.GeneratedProtocolMessageType(
    "CreateAccountResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEACCOUNTRESULT,
        "__module__": "accounts_pb2"
        # @@protoc_insertion_point(class_scope:CreateAccountResult)
    },
)
_sym_db.RegisterMessage(CreateAccountResult)

GetAccountsRequest = _reflection.GeneratedProtocolMessageType(
    "GetAccountsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETACCOUNTSREQUEST,
        "__module__": "accounts_pb2"
        # @@protoc_insertion_point(class_scope:GetAccountsRequest)
    },
)
_sym_db.RegisterMessage(GetAccountsRequest)

GetAccountsResult = _reflection.GeneratedProtocolMessageType(
    "GetAccountsResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETACCOUNTSRESULT,
        "__module__": "accounts_pb2"
        # @@protoc_insertion_point(class_scope:GetAccountsResult)
    },
)
_sym_db.RegisterMessage(GetAccountsResult)


_ACCOUNTS = _descriptor.ServiceDescriptor(
    name="Accounts",
    full_name="Accounts",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=298,
    serialized_end=428,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateAccount",
            full_name="Accounts.CreateAccount",
            index=0,
            containing_service=None,
            input_type=_CREATEACCOUNTREQUEST,
            output_type=_CREATEACCOUNTRESULT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetAccounts",
            full_name="Accounts.GetAccounts",
            index=1,
            containing_service=None,
            input_type=_GETACCOUNTSREQUEST,
            output_type=_GETACCOUNTSRESULT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ACCOUNTS)

DESCRIPTOR.services_by_name["Accounts"] = _ACCOUNTS

# @@protoc_insertion_point(module_scope)
