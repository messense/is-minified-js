#![feature(proc_macro)]
extern crate pyo3;
extern crate might_be_minified;

use std::fs;
use pyo3::prelude::*;
use might_be_minified::analyze;


/// Detecting minified javascript files
#[py::modinit(_is_minified_js)]
fn init_module(py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "is_likely_minified")]
    fn is_likely_minified(_py: Python, path: String) -> PyResult<bool> {
        let mut f = fs::File::open(path)?;
        let res = analyze(&mut f);
        Ok(res.is_likely_minified())
    }

    Ok(())
}
