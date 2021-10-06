from time import time
from multiprocessing import Pool


def factorize(*number):
    data = []
    for num in number:
        factors = factorize_one(num)
        data.append(factors)

    return data


def factorize_one(num):

    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)

    return factors


if __name__ == '__main__':

    start = time()

    with Pool() as pool:
        res = pool.map(factorize, (128, 255, 99999, 10651060))

    print(f'results: {time() - start:.2}s')
