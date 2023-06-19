import logging
from typing import List

import asyncio
import argparse
import numpy as np
from grpc import aio

import grpc
import calculate_pb2
import calculate_pb2_grpc

logger = logging.getLogger("Client")


async def run(port: int, chunk: List[int]) -> tuple():
    logger.info(f"Sending request to {port} port")
    async with aio.insecure_channel(f"localhost:{port}") as channel:
        stub = calculate_pb2_grpc.SamplingVarianceStub(channel)
        calculation_task = await stub.PerformCalculation(
            calculate_pb2.SamplingVarianceRequest(chunk=chunk)
        )
    logger.info(
        f"Received values from {port} port: sum={calculation_task.sum}, sum_of_squares={calculation_task.sum_of_squares}"
    )
    return (calculation_task.sum, calculation_task.sum_of_squares)


async def main(ports: List[str], dataset: List[int]) -> float:
    global_sum = 0
    global_sum_of_squares = 0
    dataset_size = len(dataset)
    chunks = np.array_split(dataset, len(ports))
    args = dict(zip(ports, chunks))
    computed_chunks = await asyncio.gather(
        *(run(port, chunk) for port, chunk in args.items())
    )

    for computed_chunk in computed_chunks:
        global_sum += computed_chunk[0]
        global_sum_of_squares += computed_chunk[1]

    return (global_sum_of_squares / dataset_size) - (
        (global_sum * global_sum) / (dataset_size * dataset_size)
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--ports", nargs="+", help="<Required> Set flag", required=True
    )
    ports = parser.parse_args()

    dataset = np.array([i for i in range(1500)])
    result = asyncio.run(main(**ports.__dict__, dataset=dataset))
    logger.info(f"Final result of sampling variance: {result}")
