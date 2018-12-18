extern crate might_be_minified;

use std::fs;
use std::ffi::CStr;
use std::os::raw::c_char;
use might_be_minified::analyze;


/// Detecting minified javascript files
#[no_mangle]
pub unsafe extern "C" fn is_likely_minified(path: *const c_char) -> bool {
    let c_path = CStr::from_ptr(path);
    let mut f = fs::File::open(c_path.to_str().expect("Invalid path")).expect("open file failed");
    let res = analyze(&mut f);
    res.is_likely_minified()
}
