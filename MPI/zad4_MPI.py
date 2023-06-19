from typing import List
import numpy as np
from mpi4py import MPI


def sampling_variance_MPI(observations: List, obs_size: int) -> float:
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    if rank == 0:
        sendbuf = np.array(observations)

        # count: the size of each sub-task
        ave, res = divmod(sendbuf.size, size)
        count = [ave + 1 if p < res else ave for p in range(size)]
        count = np.array(count, dtype=int)

    else:
        sendbuf = None
        # initialize count on worker processes
        count = np.zeros(size, dtype=int)
        
    # broadcast count
    comm.Bcast(count, root=0)

    # initialize recvbuf on all processes
    recvbuf = np.zeros(count[rank], dtype=int)

    comm.Scatterv(sendbuf, recvbuf, root=0)

    partial_sum = np.zeros(1, dtype=int)
    partial_sum_of_squares = np.zeros(1, dtype=int)
    partial_sum[0] = sum(recvbuf)
    partial_sum_of_squares[0] = sum([i*i for i in recvbuf])

    total_sum = np.zeros(1, dtype=int)
    total_sum_of_squares = np.zeros(1, dtype=int)
    comm.Reduce(partial_sum, total_sum, op=MPI.SUM, root=0)
    comm.Reduce(partial_sum_of_squares, total_sum_of_squares, op=MPI.SUM, root=0)
    if comm.Get_rank() == 0:
        return (total_sum_of_squares[0] / obs_size) - ((total_sum[0] * total_sum[0]) / (obs_size * obs_size))


if __name__ == '__main__':
    observations = [i for i in range(1500)]
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    result = sampling_variance_MPI(observations=observations, obs_size= len(observations))
    
    if rank == 0:
        print(result)


    
        
