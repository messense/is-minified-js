#[macro_use]
extern crate pyo3;
extern crate might_be_minified;

use std::fs;
use pyo3::{PyResult, Python, ToPyErr};
use might_be_minified::analyze;


fn is_likely_minified(py: Python, path: &str) -> PyResult<bool> {
    let mut f = fs::File::open(path).map_err(|e| e.to_pyerr(py))?;
    let res = analyze(&mut f);
    Ok(res.is_likely_minified())
}

py_module_init!(is_minified_js, PyInit__is_minified_js, |py, m| {
    m.add(py, "__doc__", "Detecting minified javascript files")?;
    m.add(py, "is_likely_minified", py_fn!(py, is_likely_minified(path: &str)))?;
    Ok(())
});
