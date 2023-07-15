from time import sleep
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool


def processes_thing(idx: int) -> str:
    sleep(0.5)
    return f'{idx} {idx}'


def go_slow() -> list[str]:
    result = []
    for i in range(0, 10):
        val = processes_thing(i)
        result.append(val)
    return result


def book_it() -> list[str]:
    result = []
    with ProcessPoolExecutor() as executor:
        for val in executor.map(processes_thing, range(0, 10)):
            result.append(val)
    return result


def book_it_alt() -> list[str]:
    with Pool(10) as pool:
        return pool.map(processes_thing, range(0, 10))


def main():
    print('Going slow....')
    res = go_slow()
    print(res)

    print('')

    print('Going fast...')
    res = book_it()
    print(res)

    print('')

    print('Going fast with child processes...')
    res = book_it_alt()
    print(res)


if __name__ == '__main__':
    main()
