
import functools
from time import perf_counter
import rustfib

def _fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return _fibo(n - 1) + _fibo(n - 2)

def timeit(f, *args, **kwargs):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret = f(*args, **kwargs)
        end = perf_counter()
        print(f"{f.__name__}({', '.join(str(x) for x in args)}) took {end - start:.6f}s")
        return ret
    return wrapper

@timeit
def fibo(n):
    return _fibo(n)

@timeit
def rustfibo(n):
    return rustfib.fibo(n)

def main():
    n = 30
    assert fibo(n) == rustfibo(n)

    n = 40
    py_start = perf_counter()
    py_result = fibo(n)
    py_time = perf_counter() - py_start

    rust_start = perf_counter() 
    rust_result = rustfibo(n)
    rust_time = perf_counter() - rust_start
    assert py_result == rust_result
    print(f"Rust is {py_time / rust_time: .2f}x faster")

if __name__ == "__main__":
    main()