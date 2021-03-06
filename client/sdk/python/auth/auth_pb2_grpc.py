# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from auth import auth_pb2 as auth_dot_auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/auth.Auth/Generate',
                request_serializer=auth_dot_auth__pb2.GenerateRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.GenerateResponse.FromString,
                )
        self.Inspect = channel.unary_unary(
                '/auth.Auth/Inspect',
                request_serializer=auth_dot_auth__pb2.InspectRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.InspectResponse.FromString,
                )
        self.Token = channel.unary_unary(
                '/auth.Auth/Token',
                request_serializer=auth_dot_auth__pb2.TokenRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.TokenResponse.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Inspect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Token(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=auth_dot_auth__pb2.GenerateRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.GenerateResponse.SerializeToString,
            ),
            'Inspect': grpc.unary_unary_rpc_method_handler(
                    servicer.Inspect,
                    request_deserializer=auth_dot_auth__pb2.InspectRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.InspectResponse.SerializeToString,
            ),
            'Token': grpc.unary_unary_rpc_method_handler(
                    servicer.Token,
                    request_deserializer=auth_dot_auth__pb2.TokenRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.TokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Generate',
            auth_dot_auth__pb2.GenerateRequest.SerializeToString,
            auth_dot_auth__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Inspect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Inspect',
            auth_dot_auth__pb2.InspectRequest.SerializeToString,
            auth_dot_auth__pb2.InspectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Token(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Token',
            auth_dot_auth__pb2.TokenRequest.SerializeToString,
            auth_dot_auth__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AccountsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/auth.Accounts/List',
                request_serializer=auth_dot_auth__pb2.ListAccountsRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.ListAccountsResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/auth.Accounts/Delete',
                request_serializer=auth_dot_auth__pb2.DeleteAccountRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.DeleteAccountResponse.FromString,
                )
        self.ChangeSecret = channel.unary_unary(
                '/auth.Accounts/ChangeSecret',
                request_serializer=auth_dot_auth__pb2.ChangeSecretRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.ChangeSecretResponse.FromString,
                )


class AccountsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=auth_dot_auth__pb2.ListAccountsRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.ListAccountsResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=auth_dot_auth__pb2.DeleteAccountRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.DeleteAccountResponse.SerializeToString,
            ),
            'ChangeSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeSecret,
                    request_deserializer=auth_dot_auth__pb2.ChangeSecretRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.ChangeSecretResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Accounts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Accounts(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Accounts/List',
            auth_dot_auth__pb2.ListAccountsRequest.SerializeToString,
            auth_dot_auth__pb2.ListAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Accounts/Delete',
            auth_dot_auth__pb2.DeleteAccountRequest.SerializeToString,
            auth_dot_auth__pb2.DeleteAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Accounts/ChangeSecret',
            auth_dot_auth__pb2.ChangeSecretRequest.SerializeToString,
            auth_dot_auth__pb2.ChangeSecretResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RulesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/auth.Rules/Create',
                request_serializer=auth_dot_auth__pb2.CreateRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.CreateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/auth.Rules/Delete',
                request_serializer=auth_dot_auth__pb2.DeleteRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.DeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/auth.Rules/List',
                request_serializer=auth_dot_auth__pb2.ListRequest.SerializeToString,
                response_deserializer=auth_dot_auth__pb2.ListResponse.FromString,
                )


class RulesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RulesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=auth_dot_auth__pb2.CreateRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.CreateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=auth_dot_auth__pb2.DeleteRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.DeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=auth_dot_auth__pb2.ListRequest.FromString,
                    response_serializer=auth_dot_auth__pb2.ListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Rules', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Rules(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Rules/Create',
            auth_dot_auth__pb2.CreateRequest.SerializeToString,
            auth_dot_auth__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Rules/Delete',
            auth_dot_auth__pb2.DeleteRequest.SerializeToString,
            auth_dot_auth__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Rules/List',
            auth_dot_auth__pb2.ListRequest.SerializeToString,
            auth_dot_auth__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
