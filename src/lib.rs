use cpython::{ PyResult, Python, py_module_initializer, py_fn};

py_module_initializer!(rustfib, |py, m| {
    m.add(py, "__doc__", "This module is rust")?;
    m.add(py, "fibo", py_fn!(py, fibo(val: i64)))?;
    Ok(())
});


fn _fibo(n: i64) -> i64 {
    if n == 1 {
        1
    } else if n == 0 {
        0
    } else {
        _fibo(n - 1) + _fibo(n - 2)
    }
}

pub fn fibo(_: Python, val: i64) -> PyResult<i64> {
    let out = _fibo(val);
    Ok(out)
}



