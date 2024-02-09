from multiprocessing import Pool, cpu_count
from time import time
import logging

logger = logging.getLogger()
stream_handler_s = logging.StreamHandler()
logger.addHandler(stream_handler_s)
logger.setLevel(logging.DEBUG)


def factorize(number: int) -> list[int]:
    res = []
    for i in range(1, number+1):
        if number % i == 0:
            res.append(i)
    return res


def factorize_optimized(number: int) -> list[int]:
    res = []
    for i in range(1, int(number ** 0.5)+1):
        if number % i == 0:
            res.append(i)
            if i != number // i:
                res.append(number // i)
    return sorted(res)


if __name__ == '__main__':
    
    numbers_list = [128, 255, 99999, 10651060, 12121212, 123435435, 123345563]

    logger.debug('\nTest with optimized function:')

    start1 = time()
    # [factorize_optimized(i) for i in numbers_list]
    for i in numbers_list:
        factorize_optimized(i)
    end1 = time()
    logger.debug(f'Sync time:  {end1 - start1}')

    with Pool(processes=cpu_count()) as pool:
        start2 = time()
        pool.map(factorize_optimized, numbers_list)
        end2 = time()
        logger.debug(f'Async time: {end2 - start2}')


    logger.debug('\nTest with not optimized function:')

    start3 = time()
    # [factorize(i) for i in numbers_list]
    for i in numbers_list:
        factorize(i)
    end3 = time()
    logger.debug(f'Sync time:  {end3 - start3}')

    with Pool(processes=cpu_count()) as pool:
        start4 = time()
        pool.map(factorize, numbers_list)
        end4 = time()
        logger.debug(f'Async time: {end4 - start4}')
