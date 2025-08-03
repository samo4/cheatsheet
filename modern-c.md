---
title: "Notes on modern C"
author: "Samo F."
date: "2025"
bibliography: modern-c.bib
link-citations: true
nocite: "@*"
---

reread: https://floooh.github.io/2019/09/27/modern-c-for-cpp-peeps.html

# Pointers

When used for a declaration, a star indicates a pointer; when not used as a declaration, a star indicates the value of the pointer.

Example:

```c
int *p; // p is a pointer to an int
*p = 5; // dereference p to set the value it points to
int x = *p; // dereference p to get the value it points to
```

## Variables and structs

```c
typedef struct { // use typedef to avoid writing struct Point everywhere
    int x, y;
} point;

point p1;
p1.x = 10; p1.y = 20;

point p2 = { .x = 10, .y = 20 };
```

And then you can also initialize structs within structs:

```c
typedef struct {
    point p1, p2;
    int arr[3]; // array of 3 ints
    char *label;
} line;
line l = {
    .p1 = { .x = 10, .y = 20 },
    .p2 = { .x = 30, .y = 40 },
    .arr[0] = 1,
    // 2 is implicitly set to 0
    .arr[2] = 3,
    .label = "line 1"
};
```

## Random points to remember

- `void bla(void)` and `void bla()` are not (exactly) the same; the first one takes no arguments, while the second one can take any number of arguments.

# C11 additions

## Static assertions

```c
#include <assert.h>
_Static_assert(sizeof(int) == 4, "int must be 4 bytes");
```

## Generic functions

```c
float minf(float a, float b);
double mini(int a, int b);

#define min(x, y) _Generic((x), float: minf(x, y), int: mini(x, y))

```

# Awesome Macros

```c
#define macro_var(name) concat(name, __LINE__)
#define defer(start, end) for ( \
    int macro_var(_i_) = (start, 0); \
    !macro_var(_i_); \
    (macro_var(_i_) += 1), end) \

defer(being(), end()) {

}

#define profile defer(profile_start(), profile_end())
profile {
    // code to profile
}

```

# API design

The old way is to add output parameters.

Instead pass the parameters by value and return a struct with the result.

```c
typedef struct {
    int x, y;
} vector;

vector add_vectors(vector a, vector b) {
    vector result = { a.x + b.x, a.y + b.y };
    return result;
}

vector v = add_vectors(v1, (vector) { .x = 10, .y = 20 });

```

A lot people use `typedef struct vec2 {...} vec2;` to declare a struct, which has a benefit that vec2 can be referred to as `struct vec2` or `vec2`.

Returning errors: return a struct with an error code and the result.

# Building

- do single header file library where you enable implementation in exactly one file.
- freehosted libraries: don't use system functions; and if you do pass what's needed as function pointers.

# String handling

- avoid standard library functions like `strcpy`, `strcat`, etc.

Try this:

```c
typedef struct {
    char *data;
    size_t length;
} str;

//  then create a proper buffer struct with allocator:

typedef struct {
    str *strings;
    size_t count;
    size_t capacity;
    allocattor_t allocator;
} str_buf;

str_buf str_buf_create(isize_t size, allocator_t allocator);
void str_buf_append(str_buf*, const char *s);
```

# Generics

https://github.com/nothings/stb/blob/master/stb_ds.h

# References
