# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculate_pb2 as calculate__pb2


class SamplingVarianceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PerformCalculation = channel.unary_unary(
                '/SamplingVariance/PerformCalculation',
                request_serializer=calculate__pb2.SamplingVarianceRequest.SerializeToString,
                response_deserializer=calculate__pb2.SamplingVarianceReply.FromString,
                )


class SamplingVarianceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PerformCalculation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SamplingVarianceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PerformCalculation': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformCalculation,
                    request_deserializer=calculate__pb2.SamplingVarianceRequest.FromString,
                    response_serializer=calculate__pb2.SamplingVarianceReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SamplingVariance', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SamplingVariance(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PerformCalculation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SamplingVariance/PerformCalculation',
            calculate__pb2.SamplingVarianceRequest.SerializeToString,
            calculate__pb2.SamplingVarianceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)