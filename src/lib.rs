#![feature(proc_macro)]
extern crate pyo3;
extern crate might_be_minified;

use std::fs;
use pyo3::{py, PyResult, Python, ToPyErr, PyModule};
use might_be_minified::analyze;


#[py::modinit(_is_minified_js)]
fn init_module(py: Python, m: &PyModule) -> PyResult<()> {
    m.add(py, "__doc__", "Detecting minified javascript files")?;

    #[pyfn(m, "is_likely_minified")]
    fn is_likely_minified(py: Python, path: String) -> PyResult<bool> {
        let mut f = fs::File::open(path).map_err(|e| e.to_pyerr(py))?;
        let res = analyze(&mut f);
        Ok(res.is_likely_minified())
    }

    Ok(())
}
