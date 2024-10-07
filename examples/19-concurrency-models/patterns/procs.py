#!/usr/bin/env python3

"""
Multiprocessing on a multicore machine using queues.
"""

# tag::PRIMES_PROC_TOP[]
import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count  # <1>
from multiprocessing import queues  # <2>

from primes import is_prime, PRIME_FIXTURE


class PrimeInputs(NamedTuple):
    n: int

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]  # <4>
ResultQueue = queues.SimpleQueue[PrimeResult]  # <5>


def run_single_processor(inputs: PrimeInputs) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(inputs.n)
    return PrimeResult(inputs.n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:  # <7>
    while inputs := jobs.get():  # <8>
        results.put(run_single_processor(inputs))  # <9>
    results.put(PrimeResult(0, False, 0.0))  # <10>

# def start_jobs(
#     procs: int, jobs: JobQueue, results: ResultQueue, 
#     args = list[PrimeInputs]
# ) -> None:
#     for n in args:
#         jobs.put(n)  # <12>
#     for _ in range(procs):
#         proc = Process(target=worker, args=(jobs, results))  # <13>
#         proc.start()  # <14>
#         jobs.put(0)  # <15>
# end::PRIMES_PROC_TOP[]

def report(procs: int, results: ResultQueue) -> int: # <6>
    checked = 0
    procs_done = 0
    while procs_done < procs:  # <7>
        n, prime, elapsed = results.get()  # <8>
        if n == 0:  # <9>
            procs_done += 1
        else:
            checked += 1  # <10>
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked


# tag::PRIMES_PROC_MAIN[]
def main() -> None:

    # check number of processors
    if len(sys.argv) < 2:
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])

    # Prepare inputs
    # Here you may be possibly reading from some input files
    inputs_list = [PrimeInputs(n=n) for n,_ in PRIME_FIXTURE]
    print(f'Computing {len(inputs_list)} items on {procs} processes')
    
    t0 = perf_counter()
    
    # create queues for jobs and results
    jobs: JobQueue = SimpleQueue() 
    results: ResultQueue = SimpleQueue()

    for inputs in inputs_list:
        jobs.put(inputs)  # <12>
    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))  # <13>
        proc.start()  # <14>
        jobs.put(0)  # <15>

    
    # start_jobs(procs, jobs, results, args=numbers)  # <3>
    checked = report(procs, results)  # <4>
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':


    main()
# end::PRIMES_PROC_MAIN[]