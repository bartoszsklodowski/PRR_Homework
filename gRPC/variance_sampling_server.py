from concurrent import futures
import logging
import argparse

import grpc
import calculate_pb2
import calculate_pb2_grpc

logger = logging.getLogger(__name__)


class SamplingVariancer(calculate_pb2_grpc.SamplingVarianceServicer):
    def PerformCalculation(self, request, context):
        sum = 0
        sum_of_squares = 0
        for i in request.chunk:
            sum += i
            sum_of_squares += i * i
        logger.info(f"Perform calculation on port: {port.port}")
        return calculate_pb2.SamplingVarianceReply(
            sum=sum, sum_of_squares=sum_of_squares
        )


def serve(port: str) -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculate_pb2_grpc.add_SamplingVarianceServicer_to_server(
        SamplingVariancer(), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    logger.info(f"Server started, listening on port: {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", type=str, help="<Required> Set flag", required=True
    )
    port = parser.parse_args()
    serve(port.port)
