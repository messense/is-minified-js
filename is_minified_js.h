/* c bindings to the is-minified-js library */

#ifndef IS_MINIFIED_JS_H_INCLUDED
#define IS_MINIFIED_JS_H_INCLUDED

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

/*
 * Detecting minified javascript files
 */
bool is_likely_minified(const char *path);

#endif /* IS_MINIFIED_JS_H_INCLUDED */
