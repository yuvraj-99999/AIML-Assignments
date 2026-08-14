# Iterators, Generators, Decorators & Context Managers

## Overview

In this session after learning about iterators, generators, decorators and context managers, this program was built to demonstrate all these concepts and how they work together.

The program demonstrates:

* Creating and using custom iterators
* Understanding generators and `yield`
* Creating and using decorators
* Measuring function execution time
* Working with context managers
* Creating custom context managers
* Handling exceptions using `__exit__()`
* Creating a timer using `@contextmanager`

## Concepts Covered

### Iterators

* A custom iterator is created using `__iter__()` and `__next__()`.
* `__next__()` returns one value at a time.
* `StopIteration` is raised when there are no more values.
* The iterator is used to iterate through a list of names.

### Generators

* Generators use `yield` to produce values one at a time.
* `yield` pauses the function and allows it to resume later.
* Generators are useful for lazy evaluation.
* Values are produced only when they are requested.

### Decorators

* A decorator is used to modify or extend the behavior of a function.
* The `@decorator` syntax is used to apply a decorator.
* A wrapper function is used to add additional behavior.
* The program also demonstrates a timing decorator that measures how long a function takes to execute.

### Context Managers

* Context managers are used to manage resources and handle cleanup.
* File handling is demonstrated using both manual file handling and the `with` statement.
* Manual file handling requires explicitly closing the file.
* The `with` statement automatically closes the file after the block finishes.

## Custom Context Manager

### `__enter__()` and `__exit__()`

A custom context manager is created using:

* `__enter__()` — runs when entering the `with` block.
* `__exit__()` — runs when leaving the `with` block.

The execution follows this order:

* Enter the context
* Execute `__enter__()`
* Execute the code inside the `with` block
* Execute `__exit__()`
* Leave the context

### Exception Handling

The `__exit__()` method can receive information about exceptions through:

* `exc_type` — stores the type of exception.
* `exc_value` — stores the exception details.
* `tb` — stores traceback information.

If no exception occurs, these values are `None`.

## Mini Project: Timer Context Manager

### Overview

The mini project creates a timer using the `@contextmanager` decorator from Python's `contextlib` module.

The timer measures how long a function takes to execute.

### Execution Flow

* The timer context manager starts.
* The current time is recorded.
* The context manager reaches `yield`.
* The context manager pauses.
* The function inside the `with` block is executed.
* The context manager resumes after the `with` block finishes.
* The `finally` block executes.
* The elapsed time is calculated.
* The execution time is displayed.

## Output

The timer displays the approximate execution time of the function.

For the demonstration function, which waits for two seconds, the output is approximately:

Time: 2.0000s

