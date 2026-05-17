# Python Basics

> *Click &#9733; if you like the project. Your contributions are heartily ♡ welcome.*

<br>

## Table of Contents

* [Introduction](#-1-introduction):  (Python compilation, bytecode, and VMs)
* [Data Types](#-2-data-types): Data Types & Built-in Scalar Types
* [Dictionary](#-3-dictionary): Hash maps, hash collisions, and Python 3.6+ ordering
* [Operators](#-4-operators): Operators & Bitwise Operations
* [Control Flow Statements](#-5-control-flow-statements): Control Flow Statements & Optimization
* [Core Data Structures](#-6-core-data-structures): Lists, Tuples, Sets, Deques
* [Functions](#-7-functions): Scope, LEGB rule, args/kwargs, closures
* [Lambda Functions](#-8-lambda-functions): Lambda Functions & Functional Programming Patterns
* [Modules and Packages](#-9-modules-and-packages): Import system, sys.modules, namespace packages
* [Object-Oriented Programming](#-10-object-oriented-programming): MRO, C3 Linearization, Descriptors, Metaclasses
* [Exception Handling](#-11-exception-handling): EAFP vs LBYL, custom exceptions, traceback overhead
* [File Handling](#-12-file-handling): Streams, text vs binary
* [Memory Management](#-13-memory-management): Object allocation, PyMalloc, small object caching
* [Garbage Collector](#-14-garbage-collector): Reference counting, generational collection, cyclic references
* [Mutable vs Immutable](#-15-mutable-vs-immutable): Hashability, identity vs equality, side-effects
* [Iterators and Generators](#-16-iterators-and-generators): Iteration protocol, lazy evaluation, memory efficiency
* [Decorators](#-17-decorators): Function decorators, class decorators, functools.wraps, stateful decorators
* [Context Managers](#-18-context-managers): Context management protocol, contextlib, resource management
* [Concurrency and Parallelism](#-19-concurrency-and-parallelism): Threading, Multiprocessing, Asyncio, Event loop, GIL
* [Testing and Debugging](#-20-testing-and-debugging): Unittest, Pytest fixtures, Mocking, profiling with cProfile
* [Miscellaneous](#-21-miscellaneous): Dunder methods, Typing/Type hinting, slots optimization

**Python for AI & Data Science**

* [Numerical Computing](#-22-numerical-computing): NumPy arrays, vectorisation
* [Data Manipulation](#-23-data-manipulation): Pandas DataFrames, Series
* [Data Visualisation](#-24-data-visualisation): Matplotlib, Seaborn
* [Machine Learning Libraries](#-25-machine-learning-libraries): Scikit-Learn
* [Deep Learning Frameworks](#-26-deep-learning-frameworks): PyTorch, TensorFlow
* [Model Evaluation Metrics](#-27-model-evaluation-metrics): Precision, Recall, F1

<br>


## # 1. Introduction

<br>

## Q. What is Python?

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),

software development,

mathematics,

system scripting.

## Q. What can Python do?

Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

## Q. When is using Python the "right choice" for a project?

Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.

Python is a high-level general-purpose programming language that can be applied to many different classes of problems.

The language comes with a large standard library that covers areas such as string processing like regular expressions, Unicode, calculating differences between files, Internet protocols like HTTP, FTP, SMTP, XML-RPC, POP, IMAP, CGI programming, software engineering like unit testing, logging, profiling, parsing Python code, and operating system interfaces like system calls, file systems, TCP/IP sockets.

Although likes and dislikes are highly personal, a developer who is "worth his or her salt" will highlight features of the Python language that are generally considered advantageous (which also helps answer the question of what Python is "particularly good for". Some of the more common valid answers to this question include:

- Ease of use and ease of refactoring, thanks to the flexibility of Python\'s syntax, which makes it especially useful for rapid prototyping.
- More compact code, thanks again to Python\'s syntax, along with a wealth of functionally-rich Python libraries (distributed freely with most Python language implementations).
- A dynamically-typed and strongly-typed language, offering the rare combination of code flexibility while at the same time avoiding pesky implicit-type-conversion bugs.
- It\'s free and open source! Need we say more?

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are some drawbacks of the Python language?

The two most common valid answers to this question are:

- The Global Interpreter Lock (GIL). CPython (the most common Python implementation) is not fully thread safe. In order to support multi-threaded Python programs, CPython provides a global lock that must be held by the current thread before it can safely access Python objects. As a result, no matter how many threads or processors are present, only one thread is ever being executed at any given time. In comparison, it is worth noting that the PyPy implementation discussed earlier in this article provides a stackless mode that supports micro-threads for massive concurrency.
- Execution speed. Python can be slower than compiled languages since it is interpreted. (Well, sort of. See our earlier discussion on this topic.)

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. We know Python is all the rage these days. But to be truly accepting of a great technology, you must know its pitfalls as well?

Of course. To be truly yourself, you must be accepting of your flaws. Only then can you move forward to work on them. Python has its flaws too:

Python\'s interpreted nature imposes a speed penalty on it. While Python is great for a lot of things, it is weak in mobile computing, and in browsers.

Being dynamically-typed, Python uses duck-typing (If it looks like a duck, it must be a duck). This can raise runtime errors.

Python has underdeveloped database access layers. This renders it a less-than-perfect choice for huge database applications.

And even after these pitfalls, of course. Being easy makes it addictive. Once a Python-coder, always a Python coder.

So while it has problems, it is also a wonderful tool for a lot of things.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are the key differences between Python 2 and 3?

- Text and Data instead of Unicode and 8-bit strings. Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings. The biggest ramification of this is that any attempt to mix text and data in Python 3.0 raises a TypeError (to combine the two safely, you must decode bytes or encode Unicode, but you need to know the proper encoding, e.g. UTF-8)

- This addresses a longstanding pitfall for naïve Python programmers. In Python 2, mixing Unicode and 8-bit data would work if the string happened to contain only 7-bit (ASCII) bytes, but you would get UnicodeDecodeError if it contained non-ASCII values. Moreover, the exception would happen at the combination point, not at the point at which the non-ASCII characters were put into the str object. This behavior was a common source of confusion and consternation for neophyte Python programmers.

- `print` function. The print statement has been replaced with a print() function

- `xrange` – buh-bye. xrange() no longer exists (range() now behaves like xrange() used to behave, except it works with values of arbitrary size)

API changes:

- `zip()`, `map()` and `filter()` all now return iterators instead of lists.
- `dict.keys()`, `dict.items()` and `dict.values()` now return 'views' instead of lists.
- `dict.iterkeys()`, `dict.iteritems()` and `dict.itervalues()` are no longer supported.
- Comparison operators. The ordering comparison operators (<, <=, >=, >) now raise a TypeError exception when the operands don\'t have a meaningful natural ordering. Some examples of the ramifications of this include:
- Expressions like 1 < '', 0 > None or len <= len are no longer valid
- None < None now raises a TypeError instead of returning False
- Sorting a heterogeneous list no longer makes sense.
- All the elements must be comparable to each other

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are some key differences to bear in mind when coding in Python vs. Java?

Disclaimer #1. The differences between Java and Python are numerous and would likely be a topic worthy of its own (lengthy) post. Below is just a brief sampling of some key differences between the two languages.

Disclaimer #2. The intent here is not to launch into a religious battle over the merits of Python vs. Java (as much fun as that might be!). Rather, the question is really just geared at seeing how well the developer understands some practical differences between the two languages. The list below therefore deliberately avoids discussing the arguable advantages of Python over Java from a programming productivity perspective.

- With the above two disclaimers in mind, here is a sampling of some key differences to bear in mind when coding in Python vs. Java:

    - Dynamic vs static typing: One of the biggest differences between the two languages is that Java is restricted to static typing whereas Python supports dynamic typing of variables.

    - Static vs. class methods: A static method in Java does not translate to a Python class method.
    - In Python, calling a class method involves an additional  
      memory allocation that calling a static method or function
      does not.
    - In Java, dotted names (e.g., foo.bar.method) are looked
      up by the compiler, so at runtime it really doesn\'t matter
      how many of them you have. In Python, however, the lookups
      occur at runtime, so "each dot counts".
    
    - Method overloading: Whereas Java requires explicit specification of multiple same-named functions with different signatures, the same can be accomplished in Python with a single function that includes optional arguments with default values if not specified by the caller.

    - Single vs. double quotes. Whereas the use of single quotes vs. double quotes has significance in Java, they can be used interchangeably in Python (but no, it won\'t allow beginnning the same string with a double quote and trying to end it with a single quote, or vice versa!).

    - Getters and setters (not!). Getters and setters in Python are superfluous; rather, you should use the 'property' built-in (that\'s what it\'s for!). In Python, getters and setters are a waste of both CPU and programmer time.

    - Classes are optional. Whereas Java requires every function to be defined in the context of an enclosing class definition, Python has no such requirement.

    - Indentation matters… in Python. This bites many a newbie Python programmer.

    The Big Picture

    - An expert knowledge of Python extends well beyond the technical minutia of the language. A Python expert will have an in-depth understanding and appreciation of Python\'s benefits as well as its limitations. Accordingly, here are some sample questions that can help assess this dimension of a candidate\'s expertise:

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are the key features of Python?  

If it makes for an introductory language to programming, Python must mean something. These are its qualities:
>
- Interpreted.
- Dynamically-typed.
- Object-oriented
- Concise and simple
- Free
- Has a large community

## Q. How is a .pyc file different from a .py file?

While both files hold bytecode, .pyc is the compiled version of a Python file. It has platform-independent bytecode. Hence, we can execute it on any platform that supports the .pyc format. Python automatically generates it to improve performance(in terms of load time, not speed).

## Q. How does the Python version numbering scheme work?

Python versions are numbered A.B.C or A.B.

A is the major version number. It is only incremented for major changes in the language.

B is the minor version number, incremented for less earth-shattering changes.

C is the micro-level. It is incremented for each bug fix release.
Not all releases are bug fix releases. 

In the run-up to a new major release, 'A' series of development releases are made denoted as alpha, beta, or release candidate.

Alphas are early releases in which interfaces aren\'t finalized yet; it\'s not unexpected to see an interface change between two alpha releases.

Betas are more stable, preserving existing interfaces but possibly adding new modules, and release candidates are frozen, making no changes except as needed to fix critical bugs.

Alpha, beta and release candidate versions have an additional suffix.

The suffix for an alpha version is "aN" for some small number N,

The suffix for a beta version is "bN" for some small number N,

And the suffix for a release candidate version is "cN" for some small number N.

In other words, all versions labeled 2.0aN precede the versions labeled 2.0bN, which precede versions labeled 2.0cN, and those precede 2.0.

You may also find version numbers with a "+" suffix, e.g. "2.2+". These are unreleased versions, built directly from the subversion trunk. In practice, after a final minor release is made, the subversion trunk is incremented to the next minor version, which becomes the "a0" version, e.g. "2.4a0".

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What Are The Implementation In Python Program?

Python program can be implemented by two ways
>
    1. Interactive Mode (Submit statement by statement explicitly)
    2. Batch Mode (Writing all statements and submit all statements)

In Interactive mode python command shell is required. It is available in installation of python cell.

In Interactive mode is not suitable for developing the projects & Applications

Interactive mode is used for predefined function and programs.
Example: 

```py
X=1000
Y=2000
X+Y
3000
Quit(X+Y)
```
X, Y is not find.
Interactive  mode is unfit for looping purpose.

Interactive Mode:
The concept of submitting one by one python statements explicitly in the python interpreter is known as "Interactive Mode"
In Order to submit the one by one python statements explicitly to the python interpreter we use python command line shell.
Python command line shell is present in python software
We can open the python command line shell by executing python command on command prompt or terminal
Example:
c:/users/mindmajix>python   
`3+4`   
7   

`'mindmajix'*3`     
'mindmajix mindmajix mindmajix'     

`x=1000`    
`y=2000`    
`x+y`   
3000    
Quit    
x+y     
c:/users/sailu>python
Error: name 'X' not defined

Batch Mode:     
In the concept of writing the group of python statements in a file, save the file with extension .py and submit that entire file to the python interpreter is known as Batch Mode.      

In Order to develop the python files we use editors or IDE\'s
Different editors are notepad, notepad++, edit+,nano, VI, gedil and so on.      
Open the notepad and write the following code:

Example: 

```py
X=1000
Y=2000
print(x+y, x-y, x*y)
```
Save the file in D drive mindmajix python folder with the demo.py
Open command prompt and execute following commands:

Python D:/mindmajix python/Demo.py

3000

-1000

2000.000

Save another method if we correctly set the path

D:

D:/>cd "mindmajix python"

D:/mindmajix Python>python Demo.py      
`3000`      
`-1000`     
`2000.000`

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What Are Applications of Python?

Applications of Python

- Automation App    
- Data Analytics 	       
- Scientific App 
- Web App 	
- Web Scrapping 
- Test Cases 	
- Network with IOT 
- Admin Script 	
- GUI 	 
- Gaming 	 
- Animation 	

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Mention five benefits of using Python?

- Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc.
- Python does not require explicit memory management as the interpreter itself allocates the memory to newvariables and free them automatically
- Provide easy readability due to use of square brackets
- Easy-to-learn for beginners
- Having the built-in data types saves programming time and effort from declaring variables

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Is Python interpreted or compiled?

As noted in Why Are There So Many Pythons?, this is, frankly, a bit of a trick question in that it is malformed. Python itself is nothing more than an interface definition (as is true with any language specification) of which there are multiple implementations. Accordingly, the question of whether "Python" is interpreted or compiled does not apply to the Python language itself; rather, it applies to each specific implementation of the Python specification.

Further complicating the answer to this question is the fact that, in the case of CPython (the most common Python implementation), the answer really is "sort of both". Specifically, with CPython, code is first compiled and then interpreted. More precisely, it is not precompiled to native machine code, but rather to bytecode. While machine code is certainly faster, bytecode is more portable and secure. The bytecode is then interpreted in the case of CPython (or both interpreted and compiled to optimized machine code at runtime in the case of PyPy).

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are some alternative implementations to CPython? When and why might you use them?

One of the more prominent alternative implementations is Jython, a Python implementation written in Java that utilizes the Java Virtual Machine (JVM). While CPython produces bytecode to run on the CPython VM, Jython produces Java bytecode to run on the JVM.

Another is IronPython, written in C# and targeting the .NET stack. IronPython runs on Microsoft\'s Common Language Runtime (CLR).

As also pointed out in Why Are There So Many Pythons?, it is entirely possible to survive without ever touching a non-CPython implementation of Python, but there are advantages to be had from switching, most of which are dependent on your technology stack.

Another noteworthy alternative implementation is PyPy whose key features include:

- Speed. Thanks to its Just-in-Time (JIT) compiler, Python programs often run faster on PyPy.
- Memory usage. Large, memory-hungry Python programs might end up taking less space with PyPy than they do in CPython.
- Compatibility. PyPy is highly compatible with existing python code. It supports cffi and can run popular Python libraries like Twisted and Django.
- Sandboxing. PyPy provides the ability to run untrusted code in a fully secure way.
- Stackless mode. PyPy comes by default with support for stackless mode, providing micro-threads for massive concurrency.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Is Python a compiled language?

Python is **both compiled and interpreted**. CPython (the reference implementation) compiles source code to platform-independent **bytecode** (`.pyc` files stored in `__pycache__`), which is then executed by the Python Virtual Machine (PVM). It is not compiled to native machine code (unlike C/C++), which is why we call it "interpreted" in common usage.

```py
import dis
import py_compile

# Compile a source file to bytecode manually
py_compile.compile("hello.py")  # produces __pycache__/hello.cpython-3x.pyc

# Inspect bytecode of a function
def add(a: int, b: int) -> int:
    return a + b

dis.dis(add)
# Output (example):
#   2           0 RESUME                   0
#   3           2 LOAD_FAST                0 (a)
#               4 LOAD_FAST                1 (b)
#               6 BINARY_OP               0 (+)
#              10 RETURN_VALUE
```

**Alternatives:**
- **PyPy**: JIT-compiles bytecode to native machine code at runtime — typically 3–5× faster than CPython for CPU-bound workloads.
- **Cython**: Transpiles Python-like code to C extensions for near-native performance.

**Use Case:** A fintech platform migrated a CPU-bound risk calculation engine from CPython to PyPy, reducing processing time from 45s to 9s with zero code changes, leveraging PyPy\'s JIT compilation.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Why Python instead of Scala on Spark when Scala has better performance?

| Factor | Python (PySpark) | Scala (native Spark) |
|--------|-----------------|---------------------|
| Raw CPU performance | Slower (GIL, serialization overhead) | Faster (JVM, no serialization) |
| Data science ecosystem | Excellent (pandas, NumPy, scikit-learn, PyTorch) | Limited |
| Developer productivity | High | Medium |
| DataFrame/SQL API | Near-identical via PySpark | Native |
| ML integrations | MLflow, Hugging Face, sklearn | MLlib |
| Hiring pool | Much larger | Smaller |

The performance gap has significantly narrowed because:
1. **PySpark DataFrames/SQL** execute entirely on the JVM — Python is only used for the driver, not the executors.
2. **Apache Arrow** (PySpark 3.0+) enables zero-copy columnar data transfer between JVM and Python, eliminating most serialization overhead.
3. **Pandas UDFs / Vectorized UDFs** use Arrow to process batches in pandas, achieving near-JVM performance for custom transformations.

```py
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, col
from pyspark.sql.types import DoubleType
import pandas as pd

spark = SparkSession.builder.appName("example").getOrCreate()

df = spark.range(1_000_000).toDF("value")

# Vectorized UDF — Arrow-backed, runs at near-native speed
@pandas_udf(DoubleType())
def square_udf(series: pd.Series) -> pd.Series:
    return series ** 2

result = df.withColumn("squared", square_udf(col("value")))
result.show(5)
# No Python serialization per-row — entire Arrow batch processed at once
```

**Use Case:** A data science team at an e-commerce company chose PySpark over Scala Spark to reuse their existing `scikit-learn` feature engineering pipelines and `pandas` data validation logic, cutting migration effort by ~70% while keeping 95% of Scala\'s throughput for DataFrame operations.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Python?

Python is a **high-level, interpreted, dynamically-typed, multi-paradigm, general-purpose programming language** created by Guido van Rossum and first released in 1991. It emphasizes code readability and developer productivity through its clean syntax and extensive standard library.

**Key characteristics:**

| Property | Detail |
|----------|--------|
| Paradigm | Object-oriented, functional, procedural, imperative |
| Typing | Dynamic (types checked at runtime) + optional static typing via `mypy` |
| Memory | Automatic (reference counting + cyclic GC) |
| Execution | CPython: source → bytecode → PVM interpretation |
| License | PSF License (permissive open source) |
| Current version | CPython 3.13 (as of 2025) |

```py
# Python's philosophy is captured in the "Zen of Python"
import this

# Demonstrates multi-paradigm nature:

# 1. Procedural
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

# 2. Object-oriented
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    def __repr__(self) -> str:
        return f"Temperature({self._celsius}°C / {self.fahrenheit}°F)"

# 3. Functional
from functools import reduce
temps_c = [0, 20, 37, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
above_boiling = list(filter(lambda t: t > 212, temps_f))
print(above_boiling)  # [212.0... only 100°C qualifies at 212°F]

t = Temperature(37)
print(t)  # Temperature(37°C / 98.6°F)
```

**Use Case:** Python serves as the lingua franca of data science and ML engineering — TensorFlow, PyTorch, scikit-learn, pandas, and Apache Spark all offer Python-first APIs, making Python the single language teams use across data exploration, model training, API serving, and infrastructure automation.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Describe some features of Python.

| Feature | Description |
|---------|-------------|
| **Interpreted** | Executed via CPython bytecode VM — no manual compile step |
| **Dynamically typed** | Variable types resolved at runtime; `mypy` adds optional static typing |
| **Garbage collected** | Reference counting + cyclic GC; no manual `malloc`/`free` |
| **Multi-paradigm** | OOP, functional, procedural, and imperative styles all supported |
| **Extensive stdlib** | 200+ modules covering I/O, networking, math, concurrency, testing |
| **Duck typing** | Interface defined by available methods, not class hierarchy |
| **First-class functions** | Functions are objects; can be passed, stored, returned |
| **Interactive REPL** | Rapid prototyping via `python` shell or Jupyter notebooks |
| **Cross-platform** | Runs on Linux, macOS, Windows, and embedded systems |
| **Readable syntax** | Enforced indentation, minimal boilerplate, PEP 8 style guide |

```py
# First-class functions + duck typing example
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

double = lambda x: x * 2
print(apply_twice(double, 3))   # 12

# Dynamic typing
x = 42
x = "now I'm a string"   # valid — name x rebound to a new object
x = [1, 2, 3]            # valid again
```

**Use Case:** Python\'s multi-paradigm nature lets a data engineering team write functional pipeline transformations (`map`/`filter`/`reduce`), OOP domain models, and procedural scripts all within the same codebase without language switching.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How does Python execute code?

Python\'s execution pipeline has six stages:

```
Source (.py)
    ↓  tokenizer (tokenize.py)
Tokens
    ↓  parser (PEG parser, Python 3.9+)
Abstract Syntax Tree (AST)
    ↓  compiler (compile.c)
Bytecode (.pyc cached in __pycache__)
    ↓  CPython Virtual Machine (ceval.c — eval loop)
Result
```

```py
import ast
import dis
import py_compile

source_code = """
def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)
"""

# Stage 1: Parse to AST
tree = ast.parse(source_code)
print(ast.dump(tree, indent=2))

# Stage 2: Compile AST to code object
code_obj = compile(source_code, "<string>", "exec")

# Stage 3: Inspect bytecode
exec(code_obj)
import sys
func = sys._getframe().f_locals.get("factorial") or eval("factorial")

# Disassemble bytecode of the compiled function
def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)

dis.dis(factorial)
# Shows RESUME, LOAD_FAST, COMPARE_OP, RETURN_VALUE, BINARY_OP, CALL, etc.

# Stage 4: .pyc caching
py_compile.compile("myscript.py")  # writes __pycache__/myscript.cpython-3x.pyc
```

**Key points:**
- `.pyc` bytecode is cached to skip re-parsing on subsequent runs (speed up import time, not execution speed)
- The eval loop in `ceval.c` dispatches on opcode using a `switch` statement (CPython 3.11 uses specializing adaptive interpreter)
- PyPy replaces the eval loop with a tracing JIT compiler

**Use Case:** A Django application with hundreds of modules benefits from `.pyc` caching — on cold start, only changed modules are re-compiled, reducing startup time from ~2s to ~0.3s in production containers.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the difference between Python 2.7+ and Python 3?

Python 3 (released 2008, Python 2 EOL January 2020) introduced breaking changes to fix long-standing design flaws. Python 2 is **no longer supported**.

| Feature | Python 2.7 | Python 3.x |
|---------|-----------|-----------|
| `print` | statement: `print "x"` | function: `print("x")` |
| Integer division | `5/2 == 2` (truncates) | `5/2 == 2.5`; use `5//2` for floor |
| `str` default | bytes (ASCII) | Unicode (UTF-8) |
| `unicode` type | separate `u"..."` | all strings are unicode |
| `range()` | returns a list | returns a lazy range object |
| `dict.keys()` | returns list | returns a view |
| `input()` | evaluates input (= py3 `eval(input())`) | returns string safely |
| Exception syntax | `except E, e:` | `except E as e:` |
| `super()` | `super(ClassName, self)` | `super()` (no args) |
| Type hints | limited (PEP 484, backported) | full native support |
| `async`/`await` | not available | native (3.5+) |
| f-strings | not available | native (3.6+) |
| `__future__` | needed for many py3 features | built-in |

```py
# Division behaviour difference
# Python 2: 5 / 2 == 2
# Python 3: 5 / 2 == 2.5
print(5 / 2)    # 2.5  (Python 3)
print(5 // 2)   # 2    (floor division in both)

# String handling
s = "café"
print(type(s))          # <class 'str'> — always unicode in Python 3
print(len(s))           # 4 (characters, not bytes)
print(len(s.encode()))  # 5 (UTF-8 bytes — 'é' = 2 bytes)

# range is lazy in Python 3
r = range(1_000_000)
print(type(r))    # <class 'range'> — O(1) memory

# super() simplified
class Base:
    def hello(self) -> str: return "base"

class Child(Base):
    def hello(self) -> str:
        return super().hello() + " child"  # no args needed in Python 3
```

**Use Case:** Migrating a legacy Python 2 data pipeline to Python 3 fixes silent data corruption where `b"bytes" / str` string mixing caused undetected encoding bugs — Python 3\'s strict bytes/str separation forces explicit encoding at system boundaries.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Is Python compiled? If yes, how? If not, how?

**Both** — Python is compiled to bytecode, then interpreted. It is **not** compiled to native machine code (unless using PyPy\'s JIT or tools like Cython/Nuitka).

**Execution pipeline:**
```
.py source → (tokenize → parse → AST → compile) → .pyc bytecode → CPython VM
```

```py
import dis
import py_compile
import pathlib

# Python compiles source to .pyc automatically on import
# Inspect the bytecode of a function
def add(a: int, b: int) -> int:
    return a + b

dis.dis(add)
# RESUME           0
# LOAD_FAST        0 (a)
# LOAD_FAST        1 (b)
# BINARY_OP        0 (+)
# RETURN_VALUE

# Compile a file manually → writes __pycache__/example.cpython-3x.pyc
py_compile.compile("example.py")

# Inspect the .pyc header
pyc = next(pathlib.Path("__pycache__").glob("*.pyc"), None)
if pyc:
    data = pyc.read_bytes()
    import struct
    magic   = data[:4].hex()
    mtime   = struct.unpack("<I", data[8:12])[0]
    print(f"magic={magic}, source_mtime={mtime}")

# The bytecode is not machine code — it targets the CPython VM stack
# Proof: the same .pyc runs on any OS with a matching CPython version
import sys
print(sys.implementation.name)   # cpython
print(sys.version)
```

**Comparison:**

| Property | Python (CPython) | Java | C |
|----------|-----------------|------|---|
| Compiled to | bytecode (.pyc) | bytecode (.class) | native binary |
| Executed by | CPython VM | JVM | OS directly |
| JIT | No (PyPy: yes) | Yes (HotSpot) | N/A |
| Cross-platform | Yes | Yes | Requires recompile |

**Use Case:** A deployment pipeline precompiles all `.py` files to `.pyc` during the Docker image build step using `python -m compileall -q src/`. This speeds up container cold starts by ~30% by skipping re-parsing on every deployment.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What does dynamically / duck typed mean?

**Dynamic typing:** Variable types are checked at **runtime**, not compile time. A name can be rebound to any type at any time — the name carries no type information itself; the *object* has a type.

**Duck typing:** "If it walks like a duck and quacks like a duck, it\'s a duck." Python does not check *what class* an object is — it only checks whether the object has the required method or attribute. Formal class inheritance is not required.

```py
# Dynamic typing — same name, different types at runtime
x = 42
print(type(x))    # <class 'int'>
x = "hello"
print(type(x))    # <class 'str'>
x = [1, 2, 3]
print(type(x))    # <class 'list'>

# Duck typing — anything with .read() works
import io

def count_lines(file_like) -> int:
    """Works with any object that has a .read() method."""
    return file_like.read().count("\n")

# Works with a real file
# with open("data.txt") as f:
#     print(count_lines(f))

# Also works with StringIO — no shared base class required
fake_file = io.StringIO("line1\nline2\nline3\n")
print(count_lines(fake_file))    # 3

# Protocol / structural typing (PEP 544) — formalize duck typing
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None: print("drawing circle")

class Square:
    def draw(self) -> None: print("drawing square")

def render(shape: Drawable) -> None:
    shape.draw()   # duck typed — no inheritance from Drawable needed

render(Circle())   # drawing circle
render(Square())   # drawing square
```

**Dynamic vs Static typing:**

| | Dynamic (Python) | Static (Java, TypeScript) |
|--|------------------|--------------------------|
| Type check | Runtime | Compile time |
| Flexibility | High | Lower |
| Early error detection | No (use mypy) | Yes |
| Refactoring safety | Lower | Higher |

**Use Case:** A data pipeline\'s `transform(obj)` function works on DataFrame rows, Pydantic models, and plain dicts equally — as long as each has the expected field access pattern. This eliminates wrapper adapters and lets the pipeline consume multiple data sources without modification.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. When would I not use Python?

Python is an excellent general-purpose language but has known limitations where other tools are more appropriate:

| Scenario | Reason | Better Alternative |
|----------|--------|--------------------|
| **CPU-bound computation** | GIL limits true thread parallelism; interpreted bytecode is slow | C, C++, Rust, Julia |
| **Mobile apps** | No first-class Android/iOS runtime | Kotlin, Swift, Flutter (Dart) |
| **Real-time / embedded systems** | GC pauses, no deterministic latency | C, C++, Rust, MicroPython |
| **Browser front-end** | Not a native browser language | JavaScript, TypeScript, WASM |
| **High-frequency trading** | Microsecond latency requirements, GC pauses | C++, Java, FPGA |
| **Memory-constrained IoT** | Runtime overhead too large | C, Rust, MicroPython |
| **Type-safe large teams** | Dynamic typing makes large-scale refactoring risky | TypeScript, Go, Kotlin |

```py
# Demonstrating the GIL limitation — threads don't speed up CPU work
import threading
import time

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

# Multi-threaded — NOT faster for CPU work due to GIL
start = time.perf_counter()
threads = [threading.Thread(target=cpu_task, args=(5_000_000,)) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
threaded_time = time.perf_counter() - start

# Use multiprocessing to bypass GIL
from multiprocessing import Pool
start = time.perf_counter()
with Pool(4) as pool:
    pool.map(cpu_task, [5_000_000] * 4)
mp_time = time.perf_counter() - start

print(f"Threads: {threaded_time:.2f}s  Multiprocessing: {mp_time:.2f}s")
# Multiprocessing is ~4x faster (true parallelism)
```

**When Python is still used despite these limitations:**
- Numpy/Pandas offload heavy computation to C extensions, bypassing the GIL
- `asyncio` handles thousands of I/O-bound concurrent connections efficiently
- Cython / PyPy / numba can make hot paths as fast as C

**Use Case:** A fintech company uses Python for data analytics and ML model training but writes the order matching engine in C++ with microsecond latency, exposing Python bindings via `ctypes` for integration and testing.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is DRY, and how can I apply it through OOP or FP?

**DRY (Don\'t Repeat Yourself):** Every piece of knowledge or logic should have a **single authoritative representation** in the codebase. Duplication means two places to update and two places to introduce bugs.

```py
# BAD — validation logic repeated in 3 places
def create_user(name: str, email: str) -> dict:
    if not name or len(name) < 2:
        raise ValueError("Name too short")
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"name": name, "email": email}

def update_user(user_id: int, name: str, email: str) -> dict:
    if not name or len(name) < 2:      # duplicated!
        raise ValueError("Name too short")
    if "@" not in email:               # duplicated!
        raise ValueError("Invalid email")
    return {"id": user_id, "name": name, "email": email}

# GOOD — DRY via OOP (extract to a class)
class UserValidator:
    @staticmethod
    def validate_name(name: str) -> str:
        if not name or len(name) < 2:
            raise ValueError(f"Name too short: {name!r}")
        return name.strip()

    @staticmethod
    def validate_email(email: str) -> str:
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError(f"Invalid email: {email!r}")
        return email.lower()

def create_user_dry(name: str, email: str) -> dict:
    return {
        "name":  UserValidator.validate_name(name),
        "email": UserValidator.validate_email(email),
    }

def update_user_dry(user_id: int, name: str, email: str) -> dict:
    return {
        "id":    user_id,
        "name":  UserValidator.validate_name(name),
        "email": UserValidator.validate_email(email),
    }

# GOOD — DRY via FP (higher-order function / decorator)
from functools import wraps
from typing import Callable

def validate_positive(func: Callable) -> Callable:
    """Decorator: ensures all numeric arguments are positive."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Expected positive number, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_tax(income: float, rate: float) -> float:
    return income * rate

@validate_positive
def calculate_discount(price: float, pct: float) -> float:
    return price * (1 - pct / 100)
```

**DRY strategies:**
- **Functions** — extract repeated logic into a single callable
- **Classes / inheritance** — share behaviour through base classes
- **Mixins** — reusable capabilities without deep hierarchy
- **Decorators** — apply cross-cutting concerns (logging, validation, retries) once
- **Templates / generics** — parameterize type differences

**Use Case:** A microservices platform DRYs up HTTP retry logic with a single `@retry(max_attempts=3, backoff=2.0)` decorator applied to all outbound API calls — changing the retry strategy requires editing one decorator, not every service client.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. When would I use Python?

Python excels in domains where developer productivity, readability, and ecosystem richness matter more than raw execution speed:

| Domain | Why Python | Key Libraries |
|--------|-----------|--------------|
| **Data science / ML** | NumPy/Pandas, rich ecosystem | numpy, pandas, scikit-learn, PyTorch, TensorFlow |
| **Web development** | Rapid development, batteries included | Django, FastAPI, Flask |
| **Scripting / automation** | Readable syntax, OS integration | subprocess, pathlib, fabric |
| **DevOps / infrastructure** | Cloud SDKs, IaC tools | boto3, Ansible, Terraform CDK |
| **Data engineering / ETL** | Spark PySpark API, Airflow, connectors | pyspark, apache-airflow, dbt |
| **API / microservices** | Async support, fast iteration | FastAPI, aiohttp, httpx |
| **Testing** | Expressive assertions, fixtures | pytest, hypothesis |
| **CLI tools** | Simple argument parsing | click, typer, argparse |
| **Scientific computing** | SciPy, symbolic math | scipy, sympy, matplotlib |

```py
# Example: Python in all these roles in a single data pipeline

# 1. Scripting — read config
import pathlib, json
config = json.loads(pathlib.Path("config.json").read_text())

# 2. Data engineering — transform
import csv
from io import StringIO
raw = "name,score\nAlice,95\nBob,87"
reader = csv.DictReader(StringIO(raw))
records = [{"name": r["name"], "score": int(r["score"])} for r in reader]

# 3. Data science — analyse
scores = [r["score"] for r in records]
mean   = sum(scores) / len(scores)
print(f"Mean score: {mean}")   # 91.0

# 4. Web API — serve results (FastAPI pattern)
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/scores")
# def get_scores() -> list[dict]: return records

# 5. Testing
assert mean == 91.0, "Unexpected mean"
print("All assertions passed")
```

**Use Case:** A startup uses Python end-to-end: Airflow for ETL orchestration, FastAPI for the REST backend, pandas for analytics, pytest for CI testing, and boto3 for AWS infrastructure — a single language team covers the full stack.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Give examples of Python frameworks.

| Category | Framework | Key Strengths |
|----------|-----------|--------------|
| **Full-stack web** | Django | ORM, admin panel, auth, batteries-included |
| **Micro/async web** | FastAPI | Auto OpenAPI, type hints, async-first, high performance |
| **Micro web** | Flask | Lightweight, flexible, easy to learn |
| **Async web** | aiohttp | Full async HTTP client + server |
| **Data pipeline** | Apache Airflow | DAG-based scheduling, rich operator ecosystem |
| **ML / Deep learning** | PyTorch, TensorFlow | Neural network training, GPU acceleration |
| **Data manipulation** | pandas | DataFrame API for tabular data |
| **Scientific** | SciPy / NumPy | Numerical computation, signal processing |
| **Testing** | pytest | Fixtures, parametrize, plugin ecosystem |
| **CLI** | Click / Typer | Decorator-based CLI with type hints |
| **ORM** | SQLAlchemy | Database-agnostic ORM + core SQL |
| **Task queue** | Celery | Distributed task execution |

```py
# FastAPI — modern async REST API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="User API", version="1.0.0")

class User(BaseModel):
    id: int
    name: str
    email: str

users_db: dict[int, User] = {
    1: User(id=1, name="Alice", email="alice@example.com"),
}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# Run with: uvicorn main:app --reload
# Auto-generated docs at: http://localhost:8000/docs

# pytest — expressive testing
import pytest

def add(a: int, b: int) -> int:
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected
```

**Use Case:** A company\'s production stack uses Django for the customer-facing portal (ORM, admin, auth), FastAPI for internal microservices (high-throughput async endpoints), Airflow for nightly ETL jobs, and Celery for async email/notification tasks — all Python, all interoperating.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How is Python interpreted?

Python\'s interpretation process has distinct stages. "Interpreted" means source code is never compiled to native machine code — it is instead compiled to **bytecode** which a software VM (the CPython interpreter loop) executes instruction by instruction.

```
Source code (.py)
  ↓  1. Tokenizer — splits text into tokens (keywords, operators, literals)
Token stream
  ↓  2. Parser — builds Abstract Syntax Tree (PEG grammar, Python 3.9+)
AST
  ↓  3. Compiler — converts AST to bytecode (list of stack-machine opcodes)
Code object (.pyc cached in __pycache__)
  ↓  4. Eval loop (ceval.c) — CPython VM executes opcode by opcode
Result
```

```py
import ast
import dis
import tokenize
import io

source = "result = (2 + 3) * 10"

# Stage 1: Tokenize
tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
for tok in tokens:
    print(tok)
# TokenInfo(type=1 (NAME), string='result', ...)
# TokenInfo(type=54 (OP), string='=', ...)  etc.

# Stage 2: Parse to AST
tree = ast.parse(source)
print(ast.dump(tree, indent=2))

# Stage 3: Compile to bytecode
code = compile(source, "<string>", "exec")
dis.dis(code)
# LOAD_CONST    1 (2)
# LOAD_CONST    2 (3)
# BINARY_OP     0 (+)
# LOAD_CONST    3 (10)
# BINARY_OP     5 (*)
# STORE_NAME    0 (result)

# Stage 4: Execute
exec(code)
# result = 50 in the executed namespace
```

**Key CPython details:**
- The eval loop in `Python/ceval.c` dispatches on each opcode (switch table)
- CPython 3.11+ uses a **specializing adaptive interpreter** — frequently executed opcodes get specialized variants (e.g., `LOAD_ATTR_MODULE` instead of generic `LOAD_ATTR`)
- `.pyc` files cache stages 1–3; only stage 4 runs on subsequent imports
- PyPy replaces the eval loop with a **tracing JIT** that compiles hot paths to machine code

**Use Case:** A platform engineering team sets `PYTHONDONTWRITEBYTECODE=0` in their Docker builds and precompiles all `.py` files with `python -m compileall` during image build, shaving 400ms off cold-start time for serverless Lambda functions.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Dynamic Typing?

Dynamic typing means **type information is attached to objects at runtime, not to variables at compile time**. A variable name is just a label that can be rebound to any object of any type at any point.

```py
# The variable 'x' has no type — only the object it points to has a type
x = 42
print(type(x).__name__)   # int

x = "hello"               # rebind — no error, no type declaration
print(type(x).__name__)   # str

x = [1, 2, 3]
print(type(x).__name__)   # list

# Type is checked AT RUNTIME, not before execution
def add(a, b):
    return a + b           # works for int, float, str, list...

print(add(1, 2))           # 3
print(add("foo", "bar"))   # foobar
print(add([1], [2]))       # [1, 2]

# Runtime type error — only caught when the bad line is actually reached
def risky(value):
    if value > 0:
        return value * 2
    else:
        return value + "oops"   # TypeError only raised if value <= 0

print(risky(5))    # 10 — fine
# print(risky(-1)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Optional static typing via mypy — adds compile-time checking WITHOUT
# changing runtime behaviour
def typed_add(a: int, b: int) -> int:
    return a + b

# mypy would flag: typed_add("x", "y")  — but Python still runs it
```

**Benefits:** Flexibility, rapid prototyping, less boilerplate.  
**Drawbacks:** Type errors surface at runtime; harder to refactor large codebases (use `mypy` / `pyright` to compensate).

**Use Case:** A data science notebook exploits dynamic typing to reuse the same variable name across exploration phases (`data = load_csv()` → `data = clean(data)` → `data = aggregate(data)`) without ceremony — then `mypy` is added to the production export path for safety.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Justify this statement: Everything is an object in Python.

In Python, **every value — integers, strings, functions, classes, modules, `None`, `True`** — is a first-class object. This means everything has: a type (`type()`), an identity (`id()`), attributes, and can be assigned to a variable, passed to a function, or stored in a collection.

```py
import inspect

# Integers are objects
x = 42
print(type(x))          # <class 'int'>
print(id(x))            # memory address
print(x.bit_length())   # 6  — integers have methods!

# Functions are objects
def greet(name: str) -> str:
    return f"Hello, {name}"

print(type(greet))           # <class 'function'>
print(greet.__name__)        # 'greet'
greet_alias = greet          # assign function to variable
print(greet_alias("Alice"))  # Hello, Alice

# Functions can be stored in collections
operations = [abs, str, type, len]
print([op(42) for op in operations])  # [42, '42', <class 'int'>, ...]

# Classes are objects (instances of 'type')
class Dog:
    pass

print(type(Dog))    # <class 'type'>  — Dog itself is an object
print(id(Dog))      # memory address of the class object

# None is an object
print(type(None))   # <class 'NoneType'>
print(id(None))     # always the same — singleton

# Modules are objects
import os
print(type(os))           # <class 'module'>
print(os.__file__)        # path to os.py

# Even types (classes) have methods inherited from object
print(dir(42))       # list of all methods on int
print(isinstance(42, object))       # True
print(isinstance(greet, object))    # True
print(isinstance(int, object))      # True — class itself is an object
```

**Implication:** Because everything is an object, Python enables true first-class functions, decorators, metaclasses, introspection, and dynamic behaviour that would require special syntax in other languages.

**Use Case:** A plugin framework stores user-provided callables (functions, class instances with `__call__`, lambdas) in a `dict[str, Callable]` registry — possible only because Python treats all of them as first-class objects with a uniform interface.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the difference between Python and Java?

| Aspect | Python | Java |
|--------|--------|------|
| **Typing** | Dynamic (optional static via mypy) | Static (compile-time) |
| **Compilation** | Bytecode (.pyc) + VM | Bytecode (.class) + JVM with JIT |
| **Syntax** | Concise, indentation-based | Verbose, brace-based |
| **OOP** | Multi-paradigm (OOP, FP, procedural) | Primarily OOP |
| **Memory** | GC (ref counting + cyclic) | GC (generational) |
| **Concurrency** | GIL limits CPU threads; asyncio for I/O | True multi-threading, no GIL |
| **Performance** | Slower (CPython); PyPy/numba for speed | Faster (JIT compilation) |
| **Primary use** | Data science, scripting, web, automation | Enterprise backend, Android, big data |
| **Null safety** | `None` + `Optional[T]` typing | `null` — NullPointerException risk |
| **Entry point** | Top-level script or `if __name__ == "__main__"` | `public static void main(String[] args)` |

```py
# Python: concise — less boilerplate
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def greet(self) -> str:
        return f"Hello, I'm {self.name}, age {self.age}"

p = Person("Alice", 30)
print(p.greet())
```

```java
// Java equivalent — much more verbose
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String greet() {
        return "Hello, I'm " + name + ", age " + age;
    }

    // + getters, setters, equals, hashCode, toString...
}
```

**When to choose Python:** Prototyping, ML/DS, scripting, small-to-medium web APIs.  
**When to choose Java:** High-throughput enterprise services, Android, large team type-safety requirements.

**Use Case:** A fintech firm writes its ML risk models in Python (pandas, scikit-learn) but the core transaction processing engine in Java (Spring Boot) for JIT performance and strict type safety — connecting them via a REST/gRPC boundary.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 2. Data Types

<br>

## Q. How do I convert a number to a string?

To convert, e.g., the number 144 to the string '144', use the built-in function str(). If you want a hexadecimal or octal representation, use the built-in functions hex() or oct(). For fancy formatting, use the % operator on strings, e.g. "%04d" % 144 yields '0144' and "%.3f" % (1/3.0) yields '0.333'. See the library reference manual for details.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Does Python support strongly for regular expressions?

Yes, Python Supports Regular Expressions Well. `re` is an in-buit library for the same. There is a lot of other languages that have good support to RegEx- Perl, Awk, Sed, Java etc.

Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the re module. Using this little language, you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as "Does this string match the pattern?", or "Is there a match for the pattern anywhere in this string?". You can also use REs to modify a string or to split it apart in various ways.

Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C. For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a certain way in order to produce bytecode that runs faster. Optimization isn\'t covered in this document, because it requires that you have a good understanding of the matching engine\'s internals.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you perform pattern matching in Python? Explain.

Regular Expressions/REs/ regexes enable us to specify expressions that can match specific "parts" of a given string. For instance, we can define a regular expression to match a single character or a digit, a telephone number, or an email address, etc. The Python\'s "re" module provides regular expression patterns and was introduce from later versions of Python 2.5. "re" module is providing methods for search text strings, or replacing text strings along with methods for splitting text strings based on the pattern defined.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Write a regular expression that will accept an email id. Use the `re` module.

Ans.

```py
import re   
e = re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$' 'JaiRameshwar@gmail.com')
e.group()
```

'Ramayanwashere@gmail.com'

To brush up on regular expressions, check Regular Expressions in Python.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

### _Garbage Collector & Memory Manager_

## Q. Explain split(), sub(), subn() methods of `re` module in Python.  

- To modify the strings, Python\'s "re" module is providing 3 methods. They are:   
    - split() – uses a regex pattern to "split" a given string into a list.
    - sub() – finds all substrings where the regex pattern matches and then replace them with a different string.
    - subn() – it is similar to sub() and also returns the new string along with the no. of replacements.

## Q. Which of the following is an invalid statement?

a) abc = 1,000,000  
b) a b c = 1000 2000 3000
c) a,b,c = 1000, 2000, 3000
d) a_b_c = 1,000,000
Answer: b

## Q. What is the output of the following?

```py
try: 
    if '1' != 1: 
        raise
```

a) some Error has occured
b) some Error has not occured
c) invalid code
d) none of the above

Answer: C

## Q. What is the output of the following?

```py
x = ['ab', 'cd']
print(len(map(list, x)))
```

A TypeError occurs as map has no len().

## Q. What is the output of the following?

```py
x = ['ab', 'cd']
print(len(list(map(list, x))))
```

The length of each string is 2.

## Q. Write a Python function that checks whether a passed string is palindrome Or not?

Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam , saas, nun.

```py
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) – 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False

    left_pos += 1
    right_pos -= 1
    return True
print(isPalindrome('aza'))
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain join() and split() in Python?

`.join([])` It takes any iterables into this method. Join method is used to concatenate the elements of any list. `join()` lets us join characters from a string together by a character we specify.

```py
','.join('12345')
```

'1,2,3,4,5'

`split()` lets us split a string around the character we specify.

```py
'1,2,3,4,5'.split(',')
```

['1', '2', '3', '4', '5']

## Q. Is Python case-sensitive?

A language is case-sensitive if it distinguishes between identifiers like myname and Myname. In other words, it cares about case- lowercase or uppercase. Let\'s try this with Python.

```py
myname='Ramayan'
Myname
```

Traceback (most recent call last):
File "<pyshell#3>", line 1, in <module> Myname
NameError: name 'Myname' is not defined

As you can see, this raised a NameError. This means that Python is indeed case-sensitive.

- How long can an identifier be in Python?

In Python, an identifier can be of any length. Apart from that, there are certain rules we must follow to name one:     
>   
    - It can only begin with an underscore or a character from A-Z or a-z.
    - The rest of it can contain anything from the following: A-Z/a-z/_/0-9.
    - Python is case-sensitive, as we discussed in the previous question.
    - Keywords cannot be used as identifiers.

Python has the following keywords:  
`and     def     False	import	not	True`   
`as      del     finally	in	    or	try`    
`assert	elif	for	    is	    pass	while`  
`break	else	from	lambda	print	with `  
`class	except	global	None	raise	yield`  
`continue	exec	if	nonlocal	return`	

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you remove the leading whitespace in a string?

Leading whitespace in a string is the whitespace in a string before the first non-whitespace character. To remove it from a string, we use the method `lstrip()`.

```py
'   Ram '.lstrip()
```

'Ram   '

As you can see, this string had both leading and trailing whitespaces. lstrip() stripped the string of the leading whitespace. If we want to strip the trailing whitespace instead, we use rstrip().

```py
'   Ram '.rstrip()
```

'   Ram'

- How would you convert a string into lowercase?

We use the lower() method for this.

```py
'Ramayan'.lower()
```

'ramayan'

To convert it into uppercase, then, we use upper().

```py
'Ramayan'.upper()
```

'RAMAYAN'

Also, to check if a string is in all uppercase or all lowercase, we use the methods isupper() and islower().

```py
'Ramayan'.isupper()
```

False

```py
'Ramayan'.isupper()
```

True

```py
'Ramayan'.islower()
```

True

```py
'$hrir@m'.islower()
```

True

```py
'$HRIR@M'.isupper()
```

True

So, characters like @ and $ will suffice for both cases.

Also, istitle() will tell us if a string is in title case.

```py
'Arrested Development'.istitle()
```

True

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What data types does Python support?

Python provides us with five kinds of data types:

```py
     a=7.0
     title="Ramayan\'s Book"
     colors=['red','green','blue']
     type(colors)
        <class 'list'>
     name=('Ramayan','Sharma')
     name[0]='Avery'
        Traceback (most recent call last):
        File "<pyshell#129>, line 1, in <module> name[0]='Avery'
        TypeError: 'tuple' object does not support item assignment
     squares={1:1,2:4,3:9,4:16,5:25}
     type(squares)
        <class 'dict'>
     type({})
        <class 'dict'>
     squares={x:x**2 for x in range(1,6)}
     squares
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Q. What is a docstring?

A docstring is a documentation string that we use to explain what a construct does. We place it as the first thing under a function, class, or a method, to describe what it does. We declare a docstring using three sets of single or double quotes.

```py
def sayhi():
    """
    The function prints Hi
    """
    print("Hi")

sayhi()
``` 

Hi

To get a function\'s docstring, we use its `__doc__` attribute.

```py
sayhi.__doc__
```

'\n\tThis function prints Hi\n\t'

A docstring, unlike a comment, is retained at runtime.

## Q. What is slicing?

These are the types of basic Python interview questions for freshers.

Slicing is a technique that allows us to retrieve only a part of a list, tuple, or string. For this, we use the slicing operator [].

```py
     (1,2,3,4,5)[2:4]
        (3, 4)
     [7,6,8,5,9][2:]
        [8, 5, 9]
     'Hello'[:-1]
        'Hell'
```

## Q. What is a namedtuple?

A namedtuple will let us access a tuple\'s elements using a name/label. We use the function namedtuple() for this, and import it from collections.

```py
 from collections import namedtuple
 result=namedtuple('result','Physics Chemistry Maths') #format
 Ramayan=result(Physics=86,Chemistry=95,Maths=86) #declaring the tuple
 Ramayan.Chemistry
```
`95`

As you can see, it let us access the marks in Chemistry using the Chemistry attribute of object Ramayan.

## Q. How would you declare a comment in Python?

Unlike languages like C++, Python does not have multiline comments. All it has is octothorpe (#). Anything following a hash is considered a comment, and the interpreter ignores it.

     #line 1 of comment
     #line 2 of comment

In fact, you can place a comment anywhere in your code. You can use it to explain your code.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you convert a string into an int in Python?

If a string contains only numerical characters, you can convert it into an integer using the int() function.

     int('227')

227

Let\'s check the types:

     type('227')

<class \'str'>

     type(int('227'))

 <class 'int'>

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you take input in Python?

For taking input from user, we have the function input(). In Python 2, we had another function raw_input().

The input() function takes, as an argument, the text to be displayed for the task:

     a=input('Enter a number')

Enter a number7

But if you have paid attention, you know that it takes input in the form of a string.

     type(a)

<class \'str'>

Multiplying this by 2 gives us this:

     a*=2
     a

'77'

So, what if we need to work on an integer instead?

We use the int() function for this.

     a=int(input('Enter a number'))

Enter a number7

Now when we multiply it by 2, we get this:

     a*=2
     a

`14`

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a frozen set in Python?

Answer these type of Python Interview Questions with Examples.

First, let\'s discuss what a set is. A set is a collection of items, where there cannot be any duplicates. A set is also unordered.

     myset={1,3,2,2}
     myset

`{1, 2, 3}`

This means that we cannot index it.

     myset[0]

Traceback (most recent call last):  
File "<pyshell#197>", line 1, in <module> myset[0]  
TypeError: \'set' object does not support indexing

However, a set is mutable. A frozen set is immutable. This means we cannot change its values. This also makes it eligible to be used as a key for a dictionary.

     myset=frozenset([1,3,2,2])
     myset
    
  frozenset({1, 2, 3})
    
     type(myset)
  <class 'frozenset'>

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How will you capitalize the first letter of a string?

Simply using the method capitalize().

     'Ramayan'.capitalize()

'Ramayan'

     type(str.capitalize)

<class 'method_descriptor'>

However, it will let other characters be.

     '$hrir@m'.capitalize()

'$HRIR@M'

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How will you check if all characters in a string are alphanumeric?

For this, we use the method isalnum().

     'Ramayan123'.isalnum()

True

     'Ramayan123!'.isalnum()

False

Other methods that we have include:

     '123.3'.isdigit()

False

     '123'.isnumeric()

True

     'Ramayan'.islower()

True

     'Ramayan'.isupper()

False

     'Ramayan'.istitle()

True

     '   '.isspace()

True

     '123F'.isdecimal()

False

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the concatenation?

This is very basic Python Interview Question, try not to make any mistake in this.

Concatenation is joining two sequences. We use the + operator for this.

     '32'+'32'
   '3232'

     [1,2,3]+[4,5,6]
   [1, 2, 3, 4, 5, 6]

     (2,3)+(4)
   `Traceback (most recent call last): `    
   `File "<pyshell#256>", line 1, in <module> (2,3)+(4)`    
   `TypeError: can only concatenate tuple (not "int") to tuple`

Here, 4 is considered an int. Let\'s do this again.

     (2,3)+(4,)  # (obj,) is way to declare single empty
    (2, 3, 4)

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How will you find, in a string, the first word that rhymes with 'cake'?

For our purpose, we will use the function search(), and then use group() to get the output.

     import re
     rhyme=re.search('.ake','I would make a cake, but I hate to bake')
     rhyme.group()

'make'

And as we know, the function search() stops at the first match. Hence, we have our first rhyme to 'cake'.

## Q. How do you calculate the length of a string?

This is simple. We call the function len() on the string we want to calculate the length of.

     len('Adi Shakara')

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What does the following code output?

     def extendList(val, list=[]):
          list.append(val)
          return list
     list1 = extendList(10)
     list2 = extendList(123,[])
     list3 = extendList('a')
     list1,list2,list3

Ans. ([10, 'a'], [123], [10, 'a'])

You'd expect the output to be something like this:

([10],[123],['a'])

Well, this is because the list argument does not initialize to its default value ([]) every time we make a call to the function. Once we define the function, it creates a new list. Then, whenever we call it again without a list argument, it uses the same list. This is because it calculates the expressions in the default arguments when we define the function, not when we call it.

Let\'s revise the Basis of Python Programming

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are The Data Types Supports in Python Language?   

- Numbers- Numbers use to hold numerical values.
- Strings- A string is a sequence of characters.  We declare it using single or double quotes.   
- Lists- A list is an ordered collection of values, and we declare it using square brackets.
- Tuples- A tuple, like a list, is an ordered collection of values. The difference. However, is that a tupleis immutable. This means that we cannot change a value in it.
- Dictionary- A dictionary is a data structure that holds key-value pairs. We declare it using curly braces.
- We can also use a dictionary comprehension:

Numbers:
    Int
    Float
    Complex
Boolean
Operational:
    Strings
    List
    Tuple
    Set
    Dictionary

Every data type in python language is internally implemented as a class. Python language data types are categorized into two types.

They are:

Fundamental Types
Collection Types

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

### _Control Flow_

## Q. In Python what is slicing?

A mechanism to select a range of items from sequence types like list, tuple, strings etc. is known as slicing.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How you can convert a number to a string?

In order to convert a number into a string, use the inbuilt function str(). If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().

## Q. What are some built-in types in Python?

```py
import sys

# Numeric types
i: int = 42                    # arbitrary precision integer
f: float = 3.14159             # IEEE 754 double (64-bit)
c: complex = 2 + 3j            # complex number
b: bool = True                 # subclass of int (True==1, False==0)

# Text / Bytes
s: str = "hello"               # immutable Unicode sequence (PEP 393)
by: bytes = b"hello"           # immutable byte sequence
ba: bytearray = bytearray(b"x")# mutable byte sequence

# Collections
lst: list = [1, "a", 3.0]     # ordered, mutable, heterogeneous
tpl: tuple = (1, "a", 3.0)    # ordered, immutable
dct: dict = {"key": "value"}  # hash map, insertion-ordered (3.7+)
st: set = {1, 2, 3}           # unordered, unique, mutable
fs: frozenset = frozenset({1}) # unordered, unique, immutable/hashable

# Singleton types
n = None                       # NoneType — single instance
e = ...                        # Ellipsis — used in type hints & numpy
ni = NotImplemented            # returned by comparison dunder methods

print(type(True).__mro__)      # (<class 'bool'>, <class 'int'>, <class 'object'>)
print(sys.getsizeof(True))     # 28 bytes (bool is int subclass)
print(isinstance(True, int))   # True
```

**Use Case:** Understanding that `bool` is a subclass of `int` prevents subtle bugs — a function accepting `int` will silently accept `True`/`False`. Teams enforcing strict APIs use `isinstance(val, int) and not isinstance(val, bool)` for explicit integer validation.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are bindings — what does it mean for a value to be bound to a variable?

In Python, **variables are names (bindings) that reference objects** — they are not containers that hold values. Assignment (`=`) creates a binding between a name and an object in the current namespace (a dictionary). The object itself exists independently; multiple names can reference the same object.

```py
import sys

# Binding: name 'x' points to the integer object 42
x = 42
print(id(x))           # memory address of the int object 42

# Rebinding: x now points to a new string object; 42 is unchanged
x = "hello"
print(id(x))           # different address

# Aliasing: both names reference the SAME list object
a = [1, 2, 3]
b = a                  # b is an alias for a, not a copy
b.append(4)
print(a)               # [1, 2, 3, 4] — mutated through b

# Check if two names point to the same object
print(a is b)          # True (same identity)
print(a == b)          # True (same value — would also be True for equal copies)

# Multiple bindings to same small integer (cache proof)
x = 100; y = 100
print(x is y)          # True — same cached int object

# Checking refcount
sys.getrefcount(a)     # number of bindings pointing to the list object

# del unbinds the name, not necessarily the object
del b
print(a)               # still [1, 2, 3, 4] — object lives on via 'a'
```

**Use Case:** Understanding bindings vs copies prevents data corruption in distributed processing — when passing a `dict` config to multiple worker functions, each worker receives a binding to the same object. Modifying it in one worker unexpectedly affects others; a `copy.deepcopy()` creates an independent object instead.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a Unicode string?

A **Unicode string** is a sequence of **Unicode code points** — an international standard covering 149,000+ characters across all writing systems, symbols, and emoji. In Python 3, **all `str` objects are Unicode** by default. The encoding (e.g., UTF-8, UTF-16) only matters when converting to/from `bytes`.

```py
# Python 3: str IS Unicode
greeting = "こんにちは"        # Japanese — 5 code points
emoji = "Python 🐍"
arabic = "مرحبا"

print(len(greeting))     # 5 — counts code points, not bytes
print(len(greeting.encode("utf-8")))  # 15 — 3 bytes per CJK character

# Code point inspection
for ch in "café":
    print(f"{ch!r}  U+{ord(ch):04X}  {ch.encode('utf-8').hex()}")
# 'c'  U+0063  63
# 'a'  U+0061  61
# 'f'  U+0066  66
# 'é'  U+00E9  c3a9  (2-byte UTF-8 sequence)

# Encoding: str → bytes
text = "résumé"
utf8_bytes  = text.encode("utf-8")
latin_bytes = text.encode("latin-1")
print(utf8_bytes)    # b'r\xc3\xa9sum\xc3\xa9'
print(latin_bytes)   # b'r\xe9sum\xe9'

# Decoding: bytes → str
print(utf8_bytes.decode("utf-8"))   # résumé

# Normalization (NFC vs NFD)
import unicodedata
e_composed   = "\u00e9"          # é as single code point (NFC)
e_decomposed = "e\u0301"         # e + combining accent (NFD)
print(e_composed == e_decomposed)                   # False!
print(unicodedata.normalize("NFC", e_decomposed) == e_composed)  # True
```

**Use Case:** A global SaaS application normalizes all user-submitted strings to NFC Unicode before storing them, preventing duplicate user records where `café` (composed form) and `cafe\u0301` (decomposed form) would compare as unequal strings despite looking identical.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain indexing and slicing.

**Indexing** accesses a single element by position (0-based; negative indices count from the end). **Slicing** extracts a sub-sequence using `[start:stop:step]`.

```py
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#      0   1   2   3   4   5   6   7   8
#     -9  -8  -7  -6  -5  -4  -3  -2  -1

# Indexing
print(lst[0])    # 10  — first element
print(lst[-1])   # 90  — last element
print(lst[-3])   # 70  — third from end

# Slicing: [start:stop:step] — stop is EXCLUSIVE
print(lst[2:5])      # [30, 40, 50]   start=2, stop=5
print(lst[:3])       # [10, 20, 30]   from beginning
print(lst[6:])       # [70, 80, 90]   to end
print(lst[::2])      # [10, 30, 50, 70, 90]  every 2nd
print(lst[::-1])     # [90, 80, 70, 60, 50, 40, 30, 20, 10]  reversed
print(lst[1:8:3])    # [20, 50, 80]   start=1, stop=8, step=3

# Strings — same rules
s = "Python"
print(s[0])      # 'P'
print(s[-1])     # 'n'
print(s[1:4])    # 'yth'
print(s[::-1])   # 'nohtyP'

# Slice assignment (mutable sequences only)
lst[1:3] = [200, 300]
print(lst)   # [10, 200, 300, 40, 50, 60, 70, 80, 90]

lst[::2] = [0] * 5   # replace every even index
print(lst)

# slice object — reusable named slice
HEADER = slice(None, 3)
DATA   = slice(3, -1)
row = [1, 2, 3, 4, 5, 6, 7]
print(row[HEADER])   # [1, 2, 3]
print(row[DATA])     # [4, 5, 6]
```

**Use Case:** A data ingestion service parses fixed-width records using named `slice` objects (`ACCOUNT_NO = slice(0, 8)`, `AMOUNT = slice(8, 16)`) — replacing magic index numbers with readable identifiers and making format changes a one-line update.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 3. Dictionary

<br>

## Q. How is the Implementation of Python\'s dictionaries done?

Python dictionary needs to be declared first:
`dict = {}`

Key value pair can be added as:
`dict[key] = value`
or
`objDict.update({key:value})`

Remove element by:  
`dict.pop(key)`

Remove all:
`objDict.clear()`

A hash value of the key is computed using a hash function, The hash value addresses a location in an array of "buckets" or "collision lists" which contains the (key , value) pair.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a dictionary in Python?

The built-in datatypes in Python is called dictionary. It defines one-to-one relationship between keys and values. Dictionaries contain pair of keys and their corresponding values. Dictionaries are indexed by keys.

Let\'s take an example:

The following example contains some keys. Country, Capital & PM. Their corresponding values are India, Delhi and Modi respectively.

`dict={'Country':'India','Capital':'Delhi','PM':'Modi'}`

`print dict[Country]`

```py
roots={25:5,16:4,9:3,4:2,1:1}
type(roots)
```

<class 'dict;>

```py
roots[9]
```

3

A dictionary is mutable, and we can also use a comprehension to create it.

```py
roots={x**2:x for x in range(5,0,-1)}
roots
```

{25: 5, 16: 4, 9: 3, 4: 2, 1: 1}

## Q. How do you get a list of all the keys in a dictionary?

Be specific in these type of Python Interview Questions and Answers.

For this, we use the function keys().

```py
mydict={'a':1,'b':2,'c':3,'e':5}
mydict.keys()
print(dict_keys)
```

(['a', 'b', 'c', 'e'])

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the Dictionary?

- Dictionary objects can be created by using curly braces{} or by calling dictionary function.

- Dictionary objects are mutable objects.

- Dictionary represents key value base.

- Each key value pair of Dictionary is known as a item.

- Dictionary keys must be immutable.

- Dictionary values can be mutable or immutable.

- Duplicate keys are not allowed but values can be duplicate.

- Insertion order is not preserved.

- Heterogeneous keys and heterogeneous values are allowed.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you create a dictionary?

```py
# Method 1: Dict literal
user: dict[str, Any] = {"name": "Alice", "age": 30, "active": True}

# Method 2: dict() constructor with keyword arguments
config = dict(host="localhost", port=5432, db="prod")

# Method 3: dict() from list of (key, value) pairs
pairs = dict([("a", 1), ("b", 2), ("c", 3)])

# Method 4: Dict comprehension
word_len: dict[str, int] = {w: len(w) for w in ["python", "java", "rust"]}

# Method 5: dict.fromkeys() — initialize all keys to same value
counters: dict[str, int] = dict.fromkeys(["hits", "misses", "errors"], 0)
print(counters)   # {'hits': 0, 'misses': 0, 'errors': 0}

# Method 6: Merging dicts (Python 3.9+ | operator)
defaults = {"timeout": 30, "retries": 3}
overrides = {"timeout": 60}
merged = defaults | overrides    # {'timeout': 60, 'retries': 3}

# Key operations
d = {"a": 1, "b": 2, "c": 3}
print(d.get("z", 0))             # 0 — safe get with default
d.setdefault("d", 4)             # inserts only if key absent
print(list(d.keys()))            # dict_keys view — O(1) iteration
print("b" in d)                  # O(1) hash lookup

# Nested access safely
from collections import defaultdict
nested: defaultdict = defaultdict(lambda: defaultdict(int))
nested["user_1"]["clicks"] += 1
```

**Use Case:** A caching layer in a web service uses a `dict` as an in-memory LRU cache (backed by `collections.OrderedDict` or `functools.lru_cache`) for O(1) average-case lookups of pre-computed API responses, reducing database round-trips by 80%.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain `dict`.

A Python `dict` is a **hash map** — a mutable, unordered (insertion-ordered since Python 3.7+) collection of key-value pairs with O(1) average-case lookup, insertion, and deletion.

```py
from collections import defaultdict, Counter, OrderedDict
from typing import Any

# Creation
d: dict[str, Any] = {"name": "Alice", "age": 30, "active": True}

# Access patterns
print(d["name"])             # 'Alice' — KeyError if missing
print(d.get("city", "N/A")) # 'N/A' — safe get with default
d.setdefault("score", 0)    # insert only if key absent
print(d)

# Iteration — all O(n)
for key in d:                  print(key)           # keys
for key, val in d.items():     print(key, val)      # key-value pairs
for val in d.values():         print(val)           # values

# Comprehension
squares = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}

# Merging (Python 3.9+)
defaults = {"timeout": 30, "retries": 3}
overrides = {"timeout": 60}
merged = defaults | overrides    # {'timeout': 60, 'retries': 3}

# Useful dict subclasses
word_count: defaultdict[str, int] = defaultdict(int)
for word in "the cat sat on the mat".split():
    word_count[word] += 1
print(dict(word_count))   # {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}

counter = Counter("abracadabra")
print(counter.most_common(3))   # [('a', 5), ('b', 2), ('r', 2)]

# Time complexity
import timeit
n = 100_000
lst = list(range(n)); s = set(range(n)); d2 = dict.fromkeys(range(n))
t_list = timeit.timeit(lambda: 99999 in lst, number=10000)
t_set  = timeit.timeit(lambda: 99999 in s,   number=10000)
t_dict = timeit.timeit(lambda: 99999 in d2,  number=10000)
print(f"list: {t_list:.4f}s  set: {t_set:.6f}s  dict: {t_dict:.6f}s")
# dict and set are ~100-1000x faster than list for membership
```

**Internal mechanics:**
- Uses open addressing with pseudorandom probing
- Load factor ~2/3 — resizes (doubles) when exceeded
- Keys must be **hashable** (immutable): `str`, `int`, `tuple`, `frozenset`
- `dict` remembers insertion order (CPython 3.6+ impl detail, 3.7+ language spec)

**Use Case:** An API gateway caches authentication tokens in a `dict` keyed by `user_id`, providing O(1) token validation for every request without hitting the database — reducing auth latency from 50ms to <1ms.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you create a dictionary that preserves the order of pairs?

Since **Python 3.7+**, the built-in `dict` **preserves insertion order** as part of the language specification. For Python 3.6 (CPython implementation detail) and older, use `collections.OrderedDict`.

```py
from collections import OrderedDict

# Python 3.7+ — plain dict preserves insertion order
d = {}
d["z"] = 1
d["a"] = 2
d["m"] = 3
print(list(d.keys()))   # ['z', 'a', 'm'] — insertion order preserved

# Dict literal also preserves order
config = {
    "host":     "localhost",
    "port":     5432,
    "database": "prod",
    "user":     "app",
}
print(list(config.keys()))   # ['host', 'port', 'database', 'user']

# OrderedDict — useful for equality-by-order comparison
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print(od1 == od2)   # False — order matters for OrderedDict

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)     # True — order doesn't matter for plain dict equality

# OrderedDict.move_to_end() — LRU cache implementation
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._cache: OrderedDict = OrderedDict()
        self._cap = capacity

    def get(self, key: str):
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)   # mark as recently used
        return self._cache[key]

    def put(self, key: str, value) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._cap:
            self._cache.popitem(last=False)   # evict least recently used

cache = LRUCache(3)
cache.put("a", 1); cache.put("b", 2); cache.put("c", 3)
cache.get("a")      # moves 'a' to end
cache.put("d", 4)   # evicts 'b' (least recently used)
print(list(cache._cache.keys()))   # ['c', 'a', 'd']
```

**Use Case:** A configuration loader builds an `OrderedDict` from a YAML file to preserve the human-authored key order — when the config is serialised back to YAML for diff review, keys appear in the same order as the original, making change reviews readable.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Can you use a mutable data structure as a key in a dictionary?

**No.** Dictionary keys must be **hashable**, and all mutable built-in types (`list`, `dict`, `set`) are **not hashable**. Attempting to use them raises `TypeError`.

**Rule:** Hashable = immutable structure + consistent `__hash__`. `hash(x) == hash(y)` whenever `x == y`.

**Use Case:** A graph algorithm caches computed shortest paths using `frozenset({source, destination})` as a dict key — symmetric pairs `(A→B)` and `(B→A)` map to the same cache entry, halving cache misses.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 4. Operators

<br>

## Q. Explain the //, %, and ** operators in Python.

The // operator performs floor division. It will return the integer part of the result on division.

```py
7//2
```
`3`
Normal division would return 3.5 here.

Similarly, **performs exponentiation. a**b returns the value of a raised to the power b.

```py
2**10
```

1024

Finally, % is for modulus. This gives us the value left after the highest achievable division.

```py
13 % 7
```

6

```py
3.5 % 1.5
```

0.5

## Q. How many kinds of operators do we have in Python? Explain arithmetic operators.

This type of Python Interview Questions and Answers can decide your knowledge in Python. Answer the Python Interview Questions with some good Examples.

Here in Python, we have 7 kinds of operators: arithmetic, relational assignment, logical, membership, identity, and bitwise.

We have seven arithmetic operators. These allow us to perform arithmetic operations on values:

Addition (+) This adds two values.

```py
7+8
7-8
7*8
7/8  # 0.875
7//8 # 0
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain relational operators in Python?

Relational operators compare values.

>    - Less than (<) If the value on the left is lesser, it returns True.

```py
'hi'<'Hi'
```

False

    Greater than (>) If the value on the left is greater, it returns True.

     1.1 + 2.2 > 3.3

True

This is because of the flawed floating-point arithmetic in Python, due to hardware dependencies.

    Less than or equal to (<=) If the value on the left is lesser than or equal to, it returns True.

     3.0 <= 3

True

    Greater than or equal to (>=) If the value on the left is greater than or equal to, it returns True.

     True >= False

True

    Equal to (==) If the two values are equal, it returns True.

     {1,3,2,2} == {1,2,3}

True

    Not equal to (!=) If the two values are unequal, it returns True.

     True!=0.1

True

     False!=0.1

True

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are assignment operators in Python?

This one is an Important Interview question in Python Interview.

We can combine all arithmetic operators with the assignment symbol.

     a = 7
     a += 1
     a

8

     a -= 1
     a

7

     a*=2
     a

14

     a/=2
     a

7.0

     a**=2
     a

49.0

     a//=3
     a

16.0

     a%=4
     a

0.0

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain logical operators in Python.

We have three logical operators- and, or, not.

     False and True

False

     7<7 or True

True

     not 2==2

False

## Q. What are membership, operators?

With the operators 'in' and 'not in', we can confirm if a value is a member in another.

    'me' in 'disappointment'
True
 
    'us' not in 'disappointment'
True

## Q. Explain identity operators in Python.

This is one of the very commonly asked Python Interview Questions and answers it with examples.
The operators 'is' and 'is not' tell us if two values have the same identity.

    10 is '10'
False

    True is not False

True

## Q. Finally, tell us about bitwise operators in Python.

These operate on values bit by bit.

    AND (&) This performs & on each bit pair.

     0b110 & 0b010

2

    OR (|) This performs | on each bit pair.

     3|2

3

    XOR (^) This performs an exclusive-OR operation on each bit pair.

     3^2

1

    Binary One\'s Complement (~) This returns the one\'s complement of a value.

     ~2

-3

    Binary Left-Shift (<<) This shifts the bits to the left by the specified amount.

     1<<2

4

Here, 001 was shifted to the left by two places to get 100, which is binary for 4.

    Binary Right-Shift (>>)

     4>>2

1

For more insight on operators, refer to Operators in Python.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you work with numbers other than those in the decimal number system?

With Python, it is possible to type numbers in binary, octal, and hexadecimal.

    Binary numbers are made of 0 and 1. To type in binary, we use the prefix 0b or 0B.

     int(0b1010)

10

To convert a number into its binary form, we use bin().

     bin(0xf)

'0b1111'

    Octal numbers may have digits from 0 to 7. We use the prefix 0o or 0O.

     oct(8)

'0o10'

    Hexadecimal numbers may have digits from 0 to 15. We use the prefix 0x or 0X.

     hex(16)

'0x10'

     hex(15)

'0xf'

## Q. Mention the use of // operator in Python?

It is a Floor Divisionoperator , which is used for dividing two operands with the result as quotient showing only digits before the decimal point. For instance, 10//5 = 2 and 10.0//5.0 = 2.0.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 5. Control Flow Statements

<br>

## Q. What is the built-in function used in Python to iterate over a sequence of numbers?

Syntax: `range(start,end,step count)`

Ex: 

```py
a = range(1,10,2)
print (a)
```
Output: 
`[1, 3, 5, 7, 9]`

If using to iterate

```py
for i in range(1,10):
    print (i)
```

Output:

>
    1
    2
    3
    4
    5
    6
    7
    8
    9

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the statement that can be used in Python if a statement is required syntactically but the program requires no action?

`pass` keyword is used to do nothing but it fulfill the syntactical requirements.

```py
try x[10]:
    print(x)
except:
    pass
```

Use `pass` keyword over there like:

```py
if a > 0:
    print("Hello")
else:
    pass
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain the ternary operator in Python?

Unlike C++, we don\'t have ?: in Python, but we have this:

[on true] if [expression] else [on false]

If the expression is True, the statement under [on true] is executed. Else, that under [on false] is executed.

Below is how you would use it:
ex 1.

```py
a,b=2,3
min=a if a<b else b
print(min)
```

Ans: 2

ex 2.

```py
print("Hi") if a<b else print("Bye")
```

Ans: Hi

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the pass statement in Python?

There may be times in our code when we haven\'t decided what to do yet, but we must type something for it to be syntactically correct. In such a case, we use the pass statement.

```py
def func(*args):
    pass 
```

Similarly, the break statement breaks out of a loop.

```py
for i in range(7):
    if i==3: break
        print(i)
```

0   
1   
2

Finally, the continue statement skips to the next iteration.

```py
for i in range(7):
    if i==3: continue
        print(i)
```
0   
1   
2   
4   
5   
6

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. If you are ever stuck in an infinite loop, how will you break out of it?

For this, we press Ctrl+C. This interrupts the execution. Let\'s create an infinite loop to demonstrate this.

    def counterfunc(n):
        while(n==7):print(n)
    counterfunc(7)

7   
7   
7   
7   
.   
.   
.   
.   
.   
Traceback (most recent call last):  
File "<pyshell#332>", line 1, in <module> counterfunc(7)    
File "<pyshell#331>", line 2, in counterfunc    
while(n==7):print(n)    
KeyboardInterrupt

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How many arguments can the range() function take?

Ans. The range() function in Python can take up to 3 arguments. Let\'s see this one by one.

a. One argument

When we pass only one argument, it takes it as the stop value. Here, the start value is 0, and the step value is +1.

     list(range(5))

[0, 1, 2, 3, 4]

     list(range(-5))

[]

     list(range(0))

[]

b. Two arguments

When we pass two arguments, the first one is the start value, and the second is the stop value.

     list(range(2,7))

[2, 3, 4, 5, 6]

     list(range(7,2))

[]

     list(range(-3,4))

[-3, -2, -1, 0, 1, 2, 3]

c. Three arguments

Here, the first argument is the start value, the second is the stop value, and the third is the step value.

     list(range(2,9,2))

[2, 4, 6, 8]

     list(range(9,2,-1))

[9, 8, 7, 6, 5, 4, 3]

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain Control flow statements.

By default python program execution starts from first line, execute each and every statements only once and transactions the program if the last statement of the program execution is over.
Control flow statements are used to disturb the normal flow of the execution of the program.

## Q. What are the two major loop statements?

`for and while`

## Q. Under what circumstances would one use a  `while` statement rather than `for`?

The while statement is used for simple repetitive looping and the for statement is used when one wishes to iterate through a list of items, such as database records, characters in a string, etc.

## Q. What happens if output an `else` statement after after block?

The code in the else block is executed after the for loop completes, unless a break is encountered in the for loop execution. in which case the else block is not executed.

## Q. Explain the use of break and continue in Python looping.

The break statement stops execution of the current loop. and transfers control to the next block. The continue statement ends the current block\'s execution and jumps to the next iteration of the loop.

## Q. When would you use a continue statement in a for loop?

When processing a particular item was complete; to move on to the next, without executing further processing in the block. The continue statement says, "I'm done processing this item, move on to the next item."

## Q. When would you use a break statement in a for loop?

When the loop has served its purpose. As an example. after finding the item in a list searched for, there is no need to keep looping. The break statement says, I'm done in this loop; move on to the next block of code."

## Q. What is the structure of a for loop?

for in : … The ellipsis represents a code block to be executed, once for each item in the sequence. Within the block the item is available as the current item from the entire list.

## Q. What is the structure of a while loop?

while : … The ellipsis represents a code block to be executed. until the condition becomes false. The condition is an expression that is considered true unless it evaluates to o, null or false.

## Q. Use a for loop and illustrate how you would define and print the characters in a string out, one per line.

```py
myString = "I Love Python"
for myChar hi myString:
    print(myChar)
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Given the string "I LoveQPython" use afor loop and illustrate printing each character tip to, but not including the Q.

```py
inyString = "I Love Pijtlzon"
for myCizar in myString:    
    fmyC'har ==
    break
print(myChar)
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Given the string "I Love Python" print out each character except for the spaces, using a for loop.

```py
inyString = I Love Python"
for myCizar in myString:
fmyChar == '' '':
continue
print myChar
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

### _Data Types_

## Q. for loop is implemented in python language as follows:

```py
for element in iterable:
    iter-obj=iter(iterable)
    while true:
        try:
            element=next(iter_obj)
        except(slop iteration)
            break
```
For loop takes the given object, convert that object in the form of iterable object & gets the one by one element form the iterable object.

While getting the one by value element from the iterable object if stop iteration exception is raised then for loop internally handle that exception

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is pass in Python?

Pass means, no-operation Python statement, or in other words it is a place holder in compound statement, where there should be a blank left and nothing has to be written there.

## # 6. Core Data Structures

<br>

## Q. Is it possible to assign multiple var to values in list?

The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code. So instead of doing this:

```py
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2] 
```

Do this:

```js
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Write a sorting algorithm for a numerical dataset in Python?

The following code can be used to sort a list in Python:

```py
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print(list)
```

## Q. How will you remove last object from a list?

`list.pop(obj=list[-1])` − Removes and returns last object or obj from list.

## Q. What are negative indexes and why are they used?

Python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index and so forth. For negative index, (-1) is the last index and (-2) is the second last index and so forth.

The sequences in Python are indexed and it consists of the positive as well as negative numbers. The numbers that are positive uses '0' that is uses as first index and '1' as the second index and the process goes on like that.

The index for the negative number starts from '-1' that represents the last index in the sequence and '-2' as the penultimate index and the sequence carries forward like the positive number.

The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1]. The negative index is also used to show the index to represent the string in correct order.

Let\'s take a list for this.

```py
mylist=[0,1,2,3,4,5,6,7,8]
```

A negative index, unlike a positive one, begins searching from the right.

```py
mylist[-3]
```

6

This also helps with slicing from the back:

```py
mylist[-6:-1]
```

[3, 4, 5, 6, 7]

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How many kinds of sequences are supported by Python? What are they?

Python supports 7 sequence types. They are str, list, tuple, unicode, byte array, xrange, and buffer. where xrange is deprecated in python 3.5.X.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?  
  
25

## Q. Differentiate between append() and extend() methods.?

Both append() and extend() methods are the methods of list. These methods are used to add the elements at the end of the list.

`append(element)` – adds the given element at the end of the list which has called this method.      
 `extend(another-list)` – adds the elements of another-list at the end of the list which is called the extend method.

## Q. Which of the following is not the correct syntax for creating a set?

a) set([[1,2],[3,4]])
b) set([1,2,2,3,4])
c) set((1,2,3,4))
d) {1,2,3,4}

A.
Explanation : The argument given for the set must be an iterable.

## Q. Write a Python program to calculate the sum of a list of numbers?

```py
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
print(list_sum([2, 4, 5, 6, 7]))
```

Sample Output: 24

## Q. How would you randomize the contents of a list in-place?

For this, we'll import the function `shuffle()` from the module `random`.

```py
from random import shuffle
shuffle(mylist)
mylist
```

[3, 4, 8, 0, 5, 7, 6, 2, 1]

## Q. What is tuple unpacking?

First, let\'s discuss tuple packing. It is a way to pack a set of values into a tuple.

```py
mytuple=3,4,5
mytuple
```

(3, 4, 5)

This packs 3, 4, and 5 into mytuple.

Now, we will unpack the values from the tuple into variables x, y, and z.

```py
x,y,z=mytuple
x+y+z
```

## Q. What is a Tuple?

- Tuple Objects can be created by using parenthesis or by calling tuple function or by assigning multiple values to a single variable
- Tuple objects are immutable objects
- Incision order is preserved

- Duplicate elements are allowed

- Heterogeneous elements are allowed

- Tuple supports both positive and negative indexing

- The elements of the tuple can be mutable or immutable

```py
#Example:
x=()
print(x)
print(type(x))
print(len(x))
y-tuple()
print(y)
print(type(y))
print(len(y))
z=10,20
print(z)
print(type(z))
print(len(z))
p=(10,20,30,40,50,10,20,10) Insertion & duplicate
print(p)
q=(100, 123.123, True, "mindmajix") Heterogeneous
print(q)
Output:
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is List Comprehensions feature of Python used for?

List comprehensions help to create and manage lists in a simpler and clearer way than using `map()`, `filter()` and `lambda`. Each list comprehension consists of an expression followed by a for clause, then zero or more for or if clauses.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are lambda expressions, list comprehensions and generator expressions?

**Lambda expressions**

are a shorthand technique for creating single line, anonymous functions. Their simple, inline nature often – though not always – leads to more readable and concise code than the alternative of formal function declarations. On the other hand, their terse inline nature, by definition, very much limits what they are capable of doing and their applicability. Being anonymous and inline, the only way to use the same lambda function in multiple locations in your code is to specify it redundantly.

**List comprehensions**

provide a concise syntax for creating lists. List comprehensions are commonly used to make lists where each element is the result of some operation(s) applied to each member of another sequence or iterable. They can also be used to create a subsequence of those elements whose members satisfy a certain condition. In Python, list comprehensions provide an alternative to using the built-in map() and filter() functions.

As the applied usage of lambda expressions and list comprehensions can overlap, opinions vary widely as to when and where to use one vs. the other. One point to bear in mind, though, is that a list comprehension executes somewhat faster than a comparable solution using map and lambda (some quick tests yielded a performance difference of roughly 10%). This is because calling a lambda function creates a new stack frame while the expression in the list comprehension is evaluated without doing so.

**Generator expressions** 

are syntactically and functionally similar to list comprehensions but there are some fairly significant differences between the ways the two operate and, accordingly, when each should be used. In a nutshell, iterating over a generator expression or list comprehension will essentially do the same thing, but the list comprehension will create the entire list in memory first while the generator expression will create the items on the fly as needed. Generator expressions can therefore be used for very large (and even infinite) sequences and their lazy (i.e., on demand) generation of values results in improved performance and lower memory usage. It is worth noting, though, that the standard Python list methods can be used on the result of a list comprehension, but not directly on that of a generator expression.

- Consider the two approaches below for initializing an array and the arrays that will result. How will the resulting arrays differ and why should you use one initialization approach vs. the other?

```py
 # INITIALIZING AN ARRAY -- METHOD 1
...
 x = [[1,2,3,4]] * 3
 x
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


 # INITIALIZING AN ARRAY -- METHOD 2
...
 y = [[1,2,3,4] for _ in range(3)]
 y
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

 # WHICH METHOD SHOULD YOU USE AND WHY?
```

**Ans:**

While both methods appear at first blush to produce the same result, there is an extremely significant difference between the two. Method 2 produces, as you would expect, an array of 3 elements, each of which is itself an independent 4-element array. In method 1, however, the members of the array all point to the same object. This can lead to what is most likely unanticipated and undesired behavior as shown below.

```py
# MODIFYING THE x ARRAY FROM THE PRIOR CODE SNIPPET:
x[0][3] = 99
x
[[1, 2, 3, 99], [1, 2, 3, 99], [1, 2, 3, 99]]

# UH-OH, DON'T THINK YOU WANTED THAT TO HAPPEN!
...
# MODIFYING THE y ARRAY FROM THE PRIOR CODE SNIPPET:
y[0][3] = 99
y
[[1, 2, 3, 99], [1, 2, 3, 4], [1, 2, 3, 4]]
# THAT\'s MORE LIKE WHAT YOU EXPECTED!
...
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What will be printed out by the second append() statement below?

```py
def append(list=[]):
    # append the length of a list to the list
    list.append(len(list))
    return list

append(['a','b'])
['a', 'b', 2]
```
append()  # calling with no arg uses default list value of [][0]

append()  # but what happens when we AGAIN call append with no arg?

**Ans:**

When the default value for a function argument is an expression, the expression is evaluated only once, not every time the function is called. Thus, once the list argument has been initialized to an empty array, subsequent calls to append without any argument specified will continue to use the same array to which list was originally initialized. This will therefore yield the following, presumably unexpected, behavior:

append() # first call with no arg uses default list value of [][0]
append() # but then look what happens...[0, 1]
append() # successive calls keep extending the same default list!
[0, 1, 2]
append()  # and so on, and so on, and so on...
[0, 1, 2, 3]

- How might one modify the implementation of the `append` method in the previous question to avoid the undesirable behavior described there?

The following alternative implementation of the append method would be one of a number of ways to avoid the undesirable behavior described in the answer to the previous question:

```py
def append(list=None):
    if list is None:
        list = []
        # append the length of a list to the list
        list.append(len(list))
        return list
append()
[0]
append()
[0]
```
Q: How can you swap the values of two variables with a single line of Python code?

Consider this simple example:
```
 x = 'X'
 y = 'Y'
```
In many other languages, swapping the values of x and y requires that you to do the following:
```
tmp = x
x = y
y = tmp
x, y
('Y', 'X')
```

But in Python, makes it possible to do the swap with a single line of code (thanks to implicit tuple packing and unpacking) as follows:
```
x,y = y,x
x,y
('Y', 'X')
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What will be printed out by the last statement below?

```py
flist = []
for i in range(3):
    flist.append(lambda: i)

[f() for f in flist]   # what will this print out?
```
In any closure in Python, variables are bound by name. Thus, the above line of code will print out the following:   
[2, 2, 2]   
Presumably not what the author of the above code intended?

A workaround is to either create a separate function or to pass the args by name; e.g.

```py
flist = []
for i in range(3):  
    flist.append(lambda i = i : i)

[f() for f in flist]
[0, 1, 2]
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you reverse a list?

There are three main approaches, each with different trade-offs:

| Method | In-place | Returns new list | Time | Space |
|--------|----------|-----------------|------|-------|
| `list.reverse()` | Yes | No (`None`) | O(n) | O(1) |
| `reversed()` | No | Iterator | O(1) | O(1) |
| Slice `[::-1]` | No | New list | O(n) | O(n) |

```py
from typing import TypeVar

T = TypeVar("T")

numbers: list[int] = [1, 2, 3, 4, 5]

# Method 1: In-place mutation (most memory-efficient for large lists)
numbers.reverse()
print(numbers)          # [5, 4, 3, 2, 1]

# Method 2: Slice — creates a new reversed copy
original = [1, 2, 3, 4, 5]
reversed_copy = original[::-1]
print(reversed_copy)    # [5, 4, 3, 2, 1]
print(original)         # [1, 2, 3, 4, 5]  (unchanged)

# Method 3: reversed() iterator — lazy, best for one-pass iteration
for item in reversed([1, 2, 3, 4, 5]):
    print(item, end=" ")  # 5 4 3 2 1
```

**Use Case:** In a data pipeline processing time-series records, `reversed()` is used to iterate over rows newest-first without copying the entire dataset into memory — critical when processing millions of records.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you merge two sorted lists?

The optimal approach uses `heapq.merge()` which runs in O(n + m) time and O(1) extra space (lazy iterator). A manual two-pointer approach is also O(n + m) but builds the result eagerly.

```py
import heapq
from typing import Iterator

# Method 1: heapq.merge — lazy O(1) space iterator (preferred for large lists)
list_a: list[int] = [1, 3, 5, 7, 9]
list_b: list[int] = [2, 4, 6, 8, 10]

merged: Iterator[int] = heapq.merge(list_a, list_b)
print(list(merged))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Method 2: Two-pointer — O(n + m) time, O(n + m) space
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    result: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

**Use Case:** In a distributed search engine, each shard returns a sorted list of ranked results. `heapq.merge()` lazily merges all shard results to produce a globally sorted feed without loading all results into memory.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Tell me some data structures in Python?

Python\'s built-in and standard-library data structures cover most algorithmic needs:

| Structure | Module | Ordered | Mutable | Unique | Avg Lookup |
|-----------|--------|---------|---------|--------|------------|
| `list` | built-in | Yes | Yes | No | O(n) |
| `tuple` | built-in | Yes | No | No | O(n) |
| `dict` | built-in | Yes (3.7+) | Yes | Keys only | O(1) |
| `set` | built-in | No | Yes | Yes | O(1) |
| `frozenset` | built-in | No | No | Yes | O(1) |
| `deque` | `collections` | Yes | Yes | No | O(1) ends |
| `defaultdict` | `collections` | Yes | Yes | Keys only | O(1) |
| `OrderedDict` | `collections` | Yes | Yes | Keys only | O(1) |
| `namedtuple` | `collections` | Yes | No | No | O(1) |
| `Counter` | `collections` | Yes | Yes | Keys only | O(1) |
| `heapq` (min-heap) | `heapq` | Partial | Yes | No | O(log n) push/pop |

```py
from collections import deque, defaultdict, Counter, namedtuple
import heapq

# deque — O(1) append/pop from both ends (unlike list's O(n) left operations)
queue: deque[int] = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print(queue)            # deque([0, 1, 2, 3, 4])

# Counter — frequency map
word_freq = Counter(["python", "java", "python", "rust", "python"])
print(word_freq.most_common(2))  # [('python', 3), ('java', 1)]

# namedtuple — immutable record with named fields (memory-efficient vs class)
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)         # 3 4

# heapq — min-heap for priority queue
tasks: list[tuple[int, str]] = []
heapq.heappush(tasks, (2, "medium priority"))
heapq.heappush(tasks, (1, "high priority"))
heapq.heappush(tasks, (3, "low priority"))
print(heapq.heappop(tasks))   # (1, 'high priority')
```

**Use Case:** A real-time leaderboard service uses `heapq` to maintain the top-K scores efficiently (O(log K) per insert), `Counter` for aggregating player event frequencies, and `deque` as a circular buffer for a sliding-window activity feed.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is List Comprehension? Show with example.

A list comprehension is a concise, readable syntax for creating a new list by applying an expression to each item in an iterable, with an optional filter condition. It is faster than an equivalent `for` loop because the iteration happens internally in C (CPython).

**Syntax:** `[expression for item in iterable if condition]`

```py
# Basic: square numbers 0–9
squares: list[int] = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With filter: even squares only
even_squares: list[int] = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Nested: flatten a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat: list[int] = [cell for row in matrix for cell in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# String processing: extract valid emails from raw strings
raw_data = ["alice@example.com", "not-an-email", "bob@corp.io", "bad@@test"]
valid_emails: list[str] = [
    addr.strip().lower()
    for addr in raw_data
    if "@" in addr and addr.count("@") == 1
]
print(valid_emails)  # ['alice@example.com', 'bob@corp.io']

# Dict comprehension variant
word_lengths: dict[str, int] = {word: len(word) for word in ["python", "java", "rust"]}
print(word_lengths)  # {'python': 6, 'java': 4, 'rust': 4}

# Set comprehension — unique first letters
first_letters: set[str] = {word[0] for word in ["apple", "ant", "banana", "avocado"]}
print(first_letters)  # {'a', 'b'}
```

**Performance:** List comprehensions are typically **1.5–2× faster** than equivalent `for` loops because they avoid repeated attribute lookups for `list.append`.

**Use Case:** A data ingestion pipeline uses list comprehensions to transform and filter 100K raw JSON records into clean domain objects in a single readable expression, replacing a 15-line `for` loop and reducing code review friction.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you create a list?

```py
from typing import Any

# Method 1: List literal (most common)
numbers: list[int] = [1, 2, 3, 4, 5]

# Method 2: list() constructor
from_tuple: list[int] = list((10, 20, 30))
from_range: list[int] = list(range(5))         # [0, 1, 2, 3, 4]
from_str: list[str] = list("abc")              # ['a', 'b', 'c']

# Method 3: List comprehension (preferred for transformations)
squares: list[int] = [x ** 2 for x in range(10)]

# Method 4: Multiplication (shallow copy — beware with mutable elements)
zeros: list[int] = [0] * 5                    # [0, 0, 0, 0, 0]

# Method 5: Empty list and append
result: list[Any] = []
result.append("a")
result.extend([1, 2])
print(result)   # ['a', 1, 2]

# Key operations and complexity
lst = [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()                    # O(n log n) in-place Timsort
print(lst[2:5])               # O(k) slicing — [3, 4, 5]
print(4 in lst)               # O(n) linear search
lst.insert(0, 0)              # O(n) — shifts all elements
lst.pop()                     # O(1) — remove from end
lst.pop(0)                    # O(n) — remove from front (use deque instead)
```

**Use Case:** A recommendation engine collects candidate items into a `list`, sorts them by score with a custom `key` function (`list.sort(key=lambda x: x.score, reverse=True)`), and slices the top-K results — leveraging Python\'s Timsort which is O(n log n) worst-case but O(n) for nearly-sorted data.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a list comprehension? Why would you use one?

A list comprehension creates a list by evaluating an expression for each element of an iterable, with an optional filter. It is more readable and ~1.5–2× faster than an equivalent `for` loop because the loop runs in C internally and avoids `list.append` attribute lookup overhead.

**Use it when:** creating a new list from a transformation/filter in one readable line.  
**Avoid it when:** logic is complex (multiple conditions, side effects, nested 3+ levels).

```py
# Why faster: no append() call overhead per iteration
import timeit

# For loop version
def squares_loop(n: int) -> list[int]:
    result = []
    for x in range(n):
        result.append(x ** 2)
    return result

# List comprehension version
def squares_comp(n: int) -> list[int]:
    return [x ** 2 for x in range(n)]

t_loop = timeit.timeit(lambda: squares_loop(1000), number=10000)
t_comp = timeit.timeit(lambda: squares_comp(1000), number=10000)
print(f"Loop: {t_loop:.3f}s  Comprehension: {t_comp:.3f}s")
# Comprehension is typically ~40% faster

# Real-world example: parse and clean CSV-like data
raw_records = [
    "  alice , 30 , engineer  ",
    "  bob , 25 , designer  ",
    "  ,  , ",          # invalid row
]

cleaned: list[dict[str, str]] = [
    {"name": parts[0], "age": parts[1], "role": parts[2]}
    for record in raw_records
    if (parts := [f.strip() for f in record.split(",")]) and all(parts)
]
print(cleaned)
# [{'name': 'alice', 'age': '30', 'role': 'engineer'}, {'name': 'bob', ...}]
```

**Use Case:** An ETL pipeline processes 500K JSON records from S3 with a single list comprehension to extract, validate, and normalize fields, making the transformation self-documenting and testable as a pure function.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is list/dict comprehension?

**Comprehensions** are concise, readable expressions that create a new collection by applying a transformation and optional filter to an iterable — all in one line. They run faster than equivalent `for` loops because the loop body executes in C.

```py
# List comprehension: [expression for item in iterable if condition]
squares   = [x ** 2 for x in range(10)]
evens     = [x for x in range(20) if x % 2 == 0]
cleaned   = [s.strip().lower() for s in ["  Alice ", "BOB", " Charlie"]]

print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(evens)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(cleaned)   # ['alice', 'bob', 'charlie']

# Nested list comprehension (flatten 2D → 1D)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [val for row in matrix for val in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict comprehension: {key_expr: val_expr for item in iterable if condition}
word_lengths = {word: len(word) for word in ["python", "java", "rust"]}
inverted     = {v: k for k, v in {"a": 1, "b": 2, "c": 3}.items()}
print(word_lengths)   # {'python': 6, 'java': 4, 'rust': 4}
print(inverted)       # {1: 'a', 2: 'b', 3: 'c'}

# Set comprehension (unique values)
unique_lengths = {len(w) for w in ["hi", "hello", "hey", "howdy"]}
print(unique_lengths)   # {2, 5}

# Generator expression (lazy — use when you don't need a list)
total = sum(x ** 2 for x in range(1_000_000))   # O(1) memory

# When to AVOID comprehensions
# BAD — multiple conditions + side effects: use a regular for loop
# result = [
#     (process(item), log(item))   # side effect inside comprehension
#     for item in items
#     if validate(item) and item.active and item.score > threshold
# ]
```

**Performance tip:** List comprehensions are ~1.3–2× faster than `for`+`append` loops.

**Use Case:** A Kafka consumer normalizes incoming JSON messages with a dict comprehension: `{k.lower().replace("-", "_"): str(v).strip() for k, v in raw.items()}` — transforming keys and values in one readable expression before schema validation.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to make an array in Python?

Python has three main ways to create array-like structures, each with different trade-offs:

```py
# 1. Built-in list — flexible, heterogeneous, dynamic size
lst: list[int] = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)    # [1, 2, 3, 4, 5, 6]

# 2. array module — typed, memory-efficient, homogeneous (like C arrays)
import array
int_arr = array.array("i", [1, 2, 3, 4, 5])  # 'i' = signed int
dbl_arr = array.array("d", [1.1, 2.2, 3.3])  # 'd' = double
print(int_arr)              # array('i', [1, 2, 3, 4, 5])
print(int_arr.itemsize)     # 4 bytes per element (vs 28 for Python int)
int_arr.append(6)
print(int_arr.tolist())     # [1, 2, 3, 4, 5, 6]

# 3. numpy array — vectorized math, multi-dimensional, C-speed
import numpy as np
np_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(np_arr * 2)           # [2 4 6 8 10] — element-wise, no loop needed
print(np_arr.mean())        # 3.0
print(np_arr.sum())         # 15

# 2D array (matrix)
matrix = np.zeros((3, 4), dtype=np.float64)   # 3 rows × 4 cols
print(matrix.shape)         # (3, 4)

# numpy operations (no Python loop)
a = np.arange(1_000_000, dtype=np.float64)
b = np.arange(1_000_000, dtype=np.float64)
c = a + b   # vectorized — ~100× faster than list + for loop

# Type codes for array.array
# 'b' = signed char, 'B' = unsigned char
# 'h' = short, 'i' = int, 'l' = long
# 'f' = float, 'd' = double
```

| | `list` | `array.array` | `numpy.ndarray` |
|-|--------|--------------|----------------|
| Typed | No | Yes | Yes |
| Multi-dim | No | No | Yes |
| Math ops | Manual | Manual | Vectorized |
| Memory | High | Low | Low–Medium |
| Speed | Slow | Medium | Fast (C) |

**Use Case:** A signal processing service stores 10M ADC samples in `numpy.ndarray(dtype=np.int16)` — 20 MB instead of ~280 MB for a Python list — and applies FFT with `np.fft.fft()` in milliseconds using BLAS/LAPACK internally.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. When to use `list` / `tuple` / `set` / `dict`?

| Structure | Ordered | Mutable | Duplicates | Key-value | Use when |
|-----------|---------|---------|------------|-----------|----------|
| `list` | Yes | Yes | Yes | No | Ordered, changeable sequence |
| `tuple` | Yes | No | Yes | No | Fixed record, dict key, return multiple values |
| `set` | No | Yes | No | No | Membership test, deduplication, set operations |
| `frozenset` | No | No | No | No | Immutable set, hashable (dict key) |
| `dict` | Yes (3.7+) | Yes | Keys: No | Yes | Key→value mapping, O(1) lookup |

```py
# list — ordered, mutable sequence
pipeline_steps: list[str] = ["extract", "transform", "load"]
pipeline_steps.append("validate")   # add at end — O(1)

# tuple — immutable record; can be a dict key
point = (3.0, 4.0)         # coordinates — immutable pair
rgb   = (255, 128, 0)      # fixed-size record
cache: dict[tuple, int] = {point: 1}   # tuple as dict key (hashable!)

# Multiple return values (naturally a tuple)
def min_max(values: list[float]) -> tuple[float, float]:
    return min(values), max(values)

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)   # 1 9

# set — fast membership, deduplication, set algebra
seen:    set[str] = set()
visited: set[str] = {"a", "b", "c"}
new:     set[str] = {"b", "c", "d", "e"}

print("a" in visited)         # True — O(1) hash lookup
print(visited & new)          # {'b', 'c'}  — intersection
print(visited | new)          # {'a', 'b', 'c', 'd', 'e'}  — union
print(visited - new)          # {'a'}  — difference

# Remove duplicates from a list (preserving order via dict trick)
dupes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = list(dict.fromkeys(dupes))
print(unique)   # [3, 1, 4, 5, 9, 2, 6]

# dict — named fields, O(1) lookup
user: dict[str, object] = {"id": 1, "name": "Alice", "active": True}
print(user.get("role", "viewer"))   # safe get with default
```

**Use Case:** A URL deduplication stage uses a `set` to track seen URLs (O(1) lookup), stores extracted data as named `dict` records, passes immutable `(source_id, record_id)` tuples as task identifiers to Celery (hashable, safe to use as cache keys), and collects ordered results in a `list`.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. When to use list comprehensions and when to avoid them?

**Use list comprehensions when:**
- Creating a new list from a transformation or filter in one line
- The expression is simple enough to read at a glance
- You want the performance benefit (~1.5–2× faster than `for`+`append`)

**Avoid list comprehensions when:**
- Logic is complex (nested 3+ levels, multiple conditions, side effects)
- The result is not needed as a list (use a generator expression instead)
- Debugging is hard (comprehensions can\'t have breakpoints mid-expression)

```py
import timeit

data = range(1000)

# GOOD: simple, readable transformation
squares = [x ** 2 for x in data]

# GOOD: filter + transform
even_squares = [x ** 2 for x in data if x % 2 == 0]

# GOOD: replace map/filter
cleaned = [s.strip().lower() for s in ["  Alice ", "BOB", " Carol "]]

# GOOD: flatten one level
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [v for row in matrix for v in row]

# AVOID: deeply nested — unreadable
# BAD:
nested = [
    (i, j, k)
    for i in range(3)
    for j in range(3)
    for k in range(3)
    if i != j != k
]
# Use itertools.product() or a regular for loop instead

# AVOID: side effects inside comprehension
import logging
# BAD:
# results = [process(item) for item in items if log_and_validate(item)]
# Use a for loop when you need side effects

# AVOID: large intermediate list you'll only iterate once — use generator
# BAD:
total = sum([x ** 2 for x in range(1_000_000)])   # builds full list in memory
# GOOD:
total = sum(x ** 2 for x in range(1_000_000))     # generator expression, O(1) memory

# Performance proof
t_loop = timeit.timeit(
    "r=[]; [r.append(x**2) for x in range(1000)]", number=10000
)
t_comp = timeit.timeit(
    "[x**2 for x in range(1000)]", number=10000
)
print(f"loop: {t_loop:.3f}s  comp: {t_comp:.3f}s")
# comprehension is ~40% faster
```

**Rule of thumb:** If it fits naturally on one line and is easy to read, use a comprehension. If you need `if/elif/else` chains, multiple side effects, or more than two nested `for` clauses — write a regular `for` loop.

**Use Case:** A data pipeline uses list comprehensions for field extraction (`[r["id"] for r in rows]`) but switches to explicit `for` loops for multi-step transformations that require logging, error handling, and conditional branching per record.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the difference between a `tuple` and a `list`? Where will you use each?

| | `list` | `tuple` |
|--|--------|---------|
| Mutability | Mutable | Immutable |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Memory | Larger (over-allocates) | Smaller (fixed) |
| Hashable | No | Yes (if all elements are) |
| Can be dict key | No | Yes |
| Iteration speed | Slightly slower | Slightly faster |
| Intended semantics | Homogeneous sequence | Heterogeneous record |

```py
import sys

# Memory comparison
lst = list(range(10))
tpl = tuple(range(10))
print(sys.getsizeof(lst))   # 184 bytes (over-allocated)
print(sys.getsizeof(tpl))   # 136 bytes (exact)

# list — ordered, changeable sequence (homogeneous items)
tasks: list[str] = ["extract", "transform", "load"]
tasks.append("validate")
tasks[0] = "fetch"

# tuple — fixed record (heterogeneous, positional meaning)
point   = (3.0, 4.0)           # 2D coordinate — positions have meaning
person  = ("Alice", 30, "SWE") # (name, age, role) — named positions

# Named tuple for readability
from collections import namedtuple
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    age: int
    role: str

emp = Employee("Bob", 28, "DevOps")
print(emp.name)    # Bob
print(emp[0])      # Bob (also index-accessible)

# Tuple as dict key — list cannot be
location_cache: dict[tuple[float, float], str] = {}
location_cache[(51.5074, -0.1278)] = "London"
location_cache[(48.8566, 2.3522)]  = "Paris"

# Tuple unpacking — clean multiple assignment
x, y, z = (1, 2, 3)
first, *rest = (10, 20, 30, 40)
print(first, rest)   # 10 [20, 30, 40]

# Swap using tuple
a, b = 1, 2
a, b = b, a    # (b, a) tuple — no temp variable needed
print(a, b)    # 2 1
```

**When to use:**
- `list` — when you need to add, remove, or sort items (shopping cart, pipeline steps)
- `tuple` — when the structure is fixed (coordinates, database rows, function return values, dict keys)

**Use Case:** A geospatial service stores cached reverse-geocoding results in `dict[tuple[float, float], str]` — using `(lat, lon)` tuples as hashable keys — and returns coordinate results as `tuple[float, float]` to signal immutability to callers.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 7. Functions

<br>

## Q. What are `*args`, `**kwargs` ?

In cases when we don\'t know how many arguments will be passed to a function, like when we want to pass a list or a tuple of values, we use `*args`.

```py
def func(*args):
    for i in args:
        print(i)  

func(3,2,1,4,7)
```
3   
2   
1   
4   
7

`**kwargs` takes keyword arguments when we don\'t know how many there will be:

```py
def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])

func(a=1,b=2,c=7)
```
a.1     
b.2     
c.7

The words `args` and `kwargs` are a convention, and we can use anything in their place.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How can I pass optional or keyword parameters from one function to another?

Collect the arguments using the * and ** specifier in the function\'s parameter list; this gives you the positional arguments as a tuple and the keyword arguments as a dictionary. You can then pass these arguments when calling another function by using `*` and `**` :

```py
def f(x, *tup, **kwargs):
    kwargs['width']='14.3c'
    g(x, *tup, **kwargs) 
```

In the unlikely case that you care about Python versions older than 2.0, use 'apply': 

```python
def f(x, *tup, **kwargs):
    kwargs['width']='14.3c'
    apply(g, (x,)+tup, kwargs)
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are higher ordered functions?

You have two choices: you can use nested scopes or you can use callable objects. For example, suppose you wanted to define linear(a,b) which returns a function f(x) that computes the value a*x+b.
`Using nested scopes:`

```py
def linear(a,b): 
    def result(x): 
        return a*x + b 
            return result
```

Or

`using a callable object:`

```py
class linear: 
    def __init__(self, a, b):
        self.a, self.b = a,b 
        def __call__(self, x): 
            return self.a * x + self.b 
```

In both cases:

`taxes = linear(0.3,2)` gives a callable object where 

`taxes(10e6) == 0.3 * 10e6 + 2. `

The callable object approach has the disadvantage that it is a bit slower and results in slightly longer code. However, note that a collection of callables can share their signature via inheritance: 

```py
class exponential(linear): 
    __init__ inherited
    def __call__(self, x):
        return self.a * (x ** self.b) 
```

Object can encapsulate state for several methods:

```py
class counter: 
    value = 0 
    def set(self, x): 
        self.value = x 
    def up(self): 
        self.value=self.value+1 
    def down(self): 
        self.value=self.value-1 
        count = counter() 

inc, dec, reset = count.up, count.down, count.set 
```

Here inc(), dec() and reset() act like functions which share the same counting variable.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain help() and dir() functions in Python?

The help() function displays the documentation string and help for its argument.

```py
import copy
help(copy.copy)
```

Help on function copy in module copy: copy(x)
Shallow copy operation on arbitrary Python objects.
See the module\'s __doc__ string for more info.
The dir() function displays all the members of an object(any kind).

```py
dir(copy.copy)

['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

### _**Dictionary**_

## Q. What is a closure in Python?

In Python, a closure is a function object that has access to variables in its enclosing lexical scope, even when the function is called outside that scope. In other words, a closure allows a function to remember and access the values of the variables in the environment where it was created, even if those variables are no longer in scope when the function is called.

Closures are created when a nested function references a value from its enclosing function. The enclosing function returns the nested function, which maintains a reference to the enclosed value. The enclosed value is stored in the closure, which is attached to the nested function object.

Here\'s an example of a closure in Python:

```py
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)  # Output: 15
```

```py
def A(x):
    def B():
        print(x)
    return B

A(7)()
```

7

## Q. Why are identifier names with a leading underscore disparaged?

Since Python does not have a concept of private variables, it is a convention to use leading underscores to declare a variable private. This is why we mustn\'t do that to variables we do not want to make private.

## Q. How can you declare multiple assignments in one statement?

There are two ways to do this:

```py
     a,b,c=3,4,5     #This assigns 3, 4, and 5 to a, b, and c resp.
     a = b = c =3         #This assigns 3 to a, b, and c
```

## Q. What is a function?

When we want to execute a sequence of statements, we can give it a name. Let\'s define a function to take two numbers and return the greater number.

```py
def greater(a,b):
    return a is a>b else b
greater(3,3.5)
```

`3.5`

You can create your own function or use one of Python\'s many built-in functions.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is recursion?

Recursion is a programming technique in which a function calls itself to solve a problem. The idea is to break down a complex problem into smaller, simpler problems and solve them in a recursive manner until the base case is reached. The base case is a condition that stops the recursion and returns a value.

A common example of a recursive function is the factorial function, which calculates the product of all positive integers up to a given number. Here\'s an example of a recursive factorial function in Python:

```py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

```py
def facto(n):
    if n==1: return 1   
        return n*facto(n-1)

facto(4)
```
`24`

## Q. What does the function zip() do?

One of the less common functions with beginners, zip() returns an iterator of tuples.

     list(zip(['a','b','c'],[1,2,3]))

[('a', 1), ('b', 2), ('c', 3)]

Here, it pairs items from the two lists, and creates tuples with those. But it doesn\'t have to be lists.

    list(zip(('a','b','c'),(1,2,3)))

[('a', 1), ('b', 2), ('c', 3)]

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a Counter in Python?

Ans.  The function Counter() from the module 'collections'. It counts the number of occurrences of the elements of a container.

    from collections import Counter
    Counter([1,3,2,1,4,2,1,3,1])

Counter({1: 4, 3: 2, 2: 2, 4: 1})

Python provides us with a range of ways and methods to work with a Counter. Read Python Counter.

## Q. Explain the use of the 'nonlocal' keyword in Python.

Ans.  First, let\'s discuss the local and global scope. By example, a variable defined inside a function is local to that function. Another variable defined outside any other scope is global to the function.

Suppose we have nested functions. We can read a variable in an enclosing scope from inside he inner function, but cannot make a change to it. For that, we must declare it nonlocal inside the function. First, let\'s see this without the nonlocal keyword.

     def outer():
        a=7
        def inner():
            print(a)
        inner()
     outer()

7 

     def outer():
        a=7
        def inner():
            print(a)
            a+=1
            print(a)
        inner()

     outer()

Traceback (most recent call last):  
File "<pyshell#462>", line 1, in <module> outer()
File "<pyshell#461>", line 7, in outer inner()
File "<pyshell#461>", line 4, in inner print(a)
UnboundLocalError: local variable 'a' referenced before assignment

So now, let\'s try doing this with the 'nonlocal' keyword:

     def outer():
        a=7
        def inner():
            nonlocal a
            print(a)
            a+=1
            print(a)

inner()

     outer()

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the global keyword?

Ans.  Like we saw in the previous question, the global keyword lets us deal with, inside any scope, the global version of a variable.

The problem:

     a=7
     def func():
        print(a)
        a+=1
        print(a)

The solution:

     a=7
     def func():
        global a
        print(a)
        a+=1
        print(a)
     func()

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Mention what are the rules for local and global variables in Python?

Local variables: If a variable is assigned a new value anywhere within the function\'s body, it\'s assumed to be local.

Global variables: Those variables that are only referenced inside a function are implicitly global.

## Q. How can you share global variables across modules?

To share global variables across modules within a single program, create a special module. Import the config module in all modules of your application. The module will be available as a global variable across modules.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How can you return multiple values from a function?

In Python, you can return multiple values from a function by packing them into a tuple or a list. Here\'s an example using a tuple:

```py
def get_user_info(user_id):
    # ... do some work to retrieve user info ...
    name = "John Doe"
    email = "johndoe@example.com"
    age = 35
    return name, email, age

# call the function and unpack the returned values
user_name, user_email, user_age = get_user_info(123)

# print the values
print(user_name)   # Output: John Doe
print(user_email)  # Output: johndoe@example.com
print(user_age)    # Output: 35
```

In this example, the `get_user_info` function returns three values (`name`, `email`, and `age`) as a tuple. When the function is called, the returned tuple is unpacked into individual variables (`user_name`, `user_email`, and `user_age`) using tuple unpacking syntax. The variables can then be used as needed.

You can also return multiple values as a list or any other iterable. For example:

```py
def get_user_info(user_id):
    # ... do some work to retrieve user info ...
    name = "John Doe"
    email = "johndoe@example.com"
    age = 35
    return [name, email, age]

# call the function and unpack the returned values
user_info = get_user_info(123)
user_name, user_email, user_age = user_info

# print the values
print(user_name)   # Output: John Doe
print(user_email)  # Output: johndoe@example.com
print(user_age)    # Output: 35
```

In this example, the get_user_info function returns a list instead of a tuple, and the returned values are unpacked into variables using list unpacking syntax.

## Q. What is the fastest way to swap the values bound to two variables?

In Python, the fastest way to swap the values bound to two variables is to use tuple unpacking, like this:

```py
a, b = b, a
```

In this code, the values of a and b are swapped by creating a tuple of the values in reverse order ((`b`, `a`)) and unpacking them into the variables a and b. The assignment is performed simultaneously, which makes this method faster than using a temporary variable, which requires an additional assignment.

For example:

```py
a = 5
b = 10

# swap the values using tuple unpacking
a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5
```

In this example, the values of `a` and `b` are swapped using tuple unpacking, and the final output shows that the values have indeed been swapped.

## Q. Do functions return something even if there is not a `return` statement?

Yes. In Python, every function returns a value. If no `return` statement is present (or `return` is used without a value), the function implicitly returns `None`.

```py
def greet(name: str) -> None:
    print(f"Hello, {name}")

result = greet("Alice")
print(result)   # Output: None
print(type(result))  # Output: <class 'NoneType'>
```

**Use Case:** This behaviour is relied upon in API validation helpers — a function that validates input and raises exceptions on failure is called for its side effects, not its return value. The caller checks `if validate(data) is None` to confirm successful validation.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to pass optional or keyword arguments.

Python supports four argument types: positional, default (optional), `*args` (variadic positional), and `**kwargs` (variadic keyword).

```py
from typing import Any

# Default arguments — make parameter optional
def greet(name: str, greeting: str = "Hello", punct: str = "!") -> str:
    return f"{greeting}, {name}{punct}"

print(greet("Alice"))                       # Hello, Alice!
print(greet("Bob", greeting="Hi"))          # Hi, Bob!
print(greet("Eve", "Hey", "."))             # Hey, Eve.

# *args — variable number of positional arguments
def total(*values: float) -> float:
    return sum(values)

print(total(1, 2, 3, 4))   # 10.0

# **kwargs — variable number of keyword arguments
def build_url(base: str, **params: Any) -> str:
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{query}" if query else base

print(build_url("https://api.example.com", page=1, limit=20, sort="desc"))
# https://api.example.com?page=1&limit=20&sort=desc

# Combining all types (order matters: positional, *args, keyword-only, **kwargs)
def create_record(
    table: str,             # positional
    *fields: str,           # variadic positional
    schema: str = "public", # keyword-only (after *)
    **metadata: Any,        # variadic keyword
) -> dict:
    return {"table": table, "fields": fields, "schema": schema, **metadata}

rec = create_record("users", "id", "name", "email", schema="app", version=2)
print(rec)
# {'table': 'users', 'fields': ('id', 'name', 'email'), 'schema': 'app', 'version': 2}

# Unpacking when calling
def add(a: int, b: int, c: int) -> int:
    return a + b + c

args = [1, 2, 3]
kwargs = {"a": 10, "b": 20, "c": 30}
print(add(*args))      # 6   — unpack list as positional args
print(add(**kwargs))   # 60  — unpack dict as keyword args
```

**Use Case:** A REST client wrapper accepts `**query_params` so callers can pass any API-supported filter without updating the function signature for every new parameter — future-proofing the interface while keeping calls readable.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the use of `enumerate()` in Python?

`enumerate()` wraps an iterable and yields `(index, value)` pairs, eliminating the need for a manual counter variable. It is O(1) memory (returns a lazy iterator) and supports a `start` parameter to control the starting index.

```py
fruits = ["apple", "banana", "cherry", "date"]

# Without enumerate — error-prone manual counter
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate — Pythonic, cleaner
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
# 3 date

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
# 4. date

# Building indexed structures
index_map = {fruit: i for i, fruit in enumerate(fruits)}
print(index_map)   # {'apple': 0, 'banana': 1, 'cherry': 2, 'date': 3}

# Tracking position while modifying (safe pattern)
data = [3, -1, 4, -1, 5, 9, -2]
for i, val in enumerate(data):
    if val < 0:
        data[i] = 0   # replace negatives in-place using index

print(data)   # [3, 0, 4, 0, 5, 9, 0]

# Works with any iterable
for line_no, line in enumerate(open("README.md"), start=1):
    if "TODO" in line:
        print(f"Line {line_no}: {line.rstrip()}")
        break
```

**Use Case:** A CSV validator uses `enumerate(rows, start=2)` (header is row 1) to report validation errors with their exact spreadsheet line number: `"Row 47: missing required field 'email'"` — without any manual counter.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Namespace vs scope?

**Namespace:** A mapping (dictionary) from names to objects. Examples: `locals()`, `globals()`, a class body, a module, `builtins`.

**Scope:** The region of source code where a namespace is *directly accessible* without qualification. Python resolves names using the **LEGB rule**: Local → Enclosing → Global → Built-in.

```py
# Global namespace
MODULE_CONST = "global"

def outer():
    # Enclosing namespace
    enclosing_var = "enclosing"

    def inner():
        # Local namespace
        local_var = "local"

        # LEGB lookup order:
        print(local_var)      # L — local
        print(enclosing_var)  # E — enclosing
        print(MODULE_CONST)   # G — global
        print(len)            # B — built-in

    inner()

outer()

# global and nonlocal keywords modify outer scopes
counter = 0

def increment():
    global counter          # modify global, not create a local shadow
    counter += 1

increment()
print(counter)   # 1

def make_counter():
    count = 0

    def inc():
        nonlocal count      # modify enclosing scope variable
        count += 1
        return count

    return inc

c = make_counter()
print(c())   # 1
print(c())   # 2

# Inspect namespaces at runtime
def show_namespaces():
    x = 10
    print("locals:", locals())
    print("globals keys:", list(globals().keys())[:5])

show_namespaces()

# Class body has its own namespace (but NOT a scope for nested functions)
class Config:
    DEBUG = True
    DB_URL = "postgres://..."
    # Inside a method, Config.DEBUG — must qualify with class name
```

**Key distinction:**
- **Namespace** = the dictionary itself (data structure)
- **Scope** = the textual region where a namespace is searched automatically

**Use Case:** A plugin system uses `globals()` to dynamically register handler functions by name at import time, and `locals()` to safely evaluate template expressions in a restricted namespace — separating the framework\'s global namespace from per-render local context.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you create a Python function?

```py
from typing import Optional

# 1. Basic function
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!

# 2. Default arguments
def power(base: float, exponent: int = 2) -> float:
    return base ** exponent

print(power(3))       # 9.0
print(power(3, 3))    # 27.0

# 3. *args and **kwargs
def summarize(*args: float, label: str = "Total", **meta) -> dict:
    return {"label": label, "sum": sum(args), "count": len(args), **meta}

print(summarize(1, 2, 3, label="Score", unit="pts"))
# {'label': 'Score', 'sum': 6, 'count': 3, 'unit': 'pts'}

# 4. Return multiple values (returns a tuple)
def min_max(values: list[float]) -> tuple[float, float]:
    return min(values), max(values)

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)   # 1 9

# 5. Lambda — anonymous single-expression function
square = lambda x: x ** 2
print(square(7))   # 49

# 6. Nested functions and closures
def make_multiplier(factor: int):
    def multiply(x: float) -> float:
        return x * factor      # closes over 'factor'
    return multiply

triple = make_multiplier(3)
print(triple(10))   # 30.0

# 7. Decorator
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_call
def add(a: int, b: int) -> int:
    return a + b

add(2, 3)
# Calling add
# add returned 5

# 8. Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

**Use Case:** A data transformation library exposes its API entirely as plain functions with type annotations, enabling `mypy` static analysis, easy unit testing (`assert transform(input) == expected`), and simple composition via `functools.partial` and `compose`.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How does a function return values?

A function returns a value using the `return` statement. Python allows returning multiple values (as a tuple), returning early, and using generators to yield values lazily.

```py
# 1. Single return value
def square(n: float) -> float:
    return n ** 2

# 2. Multiple return values — actually returns a tuple
def divmod_custom(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b   # quotient and remainder

quotient, remainder = divmod_custom(17, 5)
print(quotient, remainder)   # 3, 2

raw = divmod_custom(17, 5)
print(type(raw))   # <class 'tuple'>

# 3. Early return (guard clauses)
def safe_sqrt(n: float) -> float | None:
    if n < 0:
        return None       # early exit
    return n ** 0.5

# 4. Return a function (closure / higher-order)
def make_adder(n: int):
    def adder(x: int) -> int:
        return x + n
    return adder           # return a function object

add5 = make_adder(5)
print(add5(10))   # 15

# 5. Return a complex object
from dataclasses import dataclass

@dataclass
class ParseResult:
    success: bool
    value: float | None
    error: str | None = None

def parse_number(s: str) -> ParseResult:
    try:
        return ParseResult(success=True, value=float(s))
    except ValueError as e:
        return ParseResult(success=False, value=None, error=str(e))

r = parse_number("3.14")
print(r)   # ParseResult(success=True, value=3.14, error=None)

# 6. Generator — yield instead of return (lazy values)
def even_range(n: int):
    for i in range(n):
        if i % 2 == 0:
            yield i        # yields one at a time, not all at once

print(list(even_range(10)))   # [0, 2, 4, 6, 8]
```

**Use Case:** An API handler returns a `dataclass` `Result(ok, data, error)` from every service call — callers pattern-match on `result.ok` rather than catching exceptions, making error handling explicit and the happy path obvious.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What happens when a function does not have a `return` statement?

A function without a `return` statement (or with a bare `return`) implicitly returns `None`. This is by design — Python always returns an object; `None` is the sentinel for "no meaningful value".

```py
def greet(name: str) -> None:
    print(f"Hello, {name}!")

result = greet("Alice")   # prints "Hello, Alice!"
print(result)              # None
print(type(result))        # <class 'NoneType'>

# Bare return also returns None
def process(value: int) -> int | None:
    if value < 0:
        return          # same as: return None
    return value * 2

print(process(-1))    # None
print(process(5))     # 10

# Common pitfall — accidentally using the return value of a mutating method
lst = [3, 1, 2]
sorted_lst = lst.sort()    # list.sort() returns None (in-place)
print(sorted_lst)          # None  ← BUG! should use sorted(lst)

# Fix:
sorted_lst = sorted(lst)   # sorted() returns a new list
print(sorted_lst)          # [1, 2, 3]

# Type checkers (mypy) will warn if you assign None to a typed variable
def no_return():
    x = 1 + 1   # computes but discards

val = no_return()
# mypy: error: "no_return" does not return a value (it only ever returns None)

# None check pattern
def find(items: list, target) -> int | None:
    for i, item in enumerate(items):
        if item == target:
            return i
    # falls off end — returns None

idx = find([1, 2, 3], 99)
if idx is None:
    print("Not found")
```

**Use Case:** A data validation function returns `None` on success and a `ValidationError` (or error string) on failure — callers check `if error := validate(data): handle(error)`, making the "no return = success" contract explicit.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 8. Lambda Functions

<br>

## Q. What is lambda? What are Lambda Functions ?

A function which doesn\'t contain any name is known as a anonymous function lambda function, Lambda function we can assign to the variable & we can call the lambda function through the variable.

Syntax:
`Lambda arguments:expression`


It is a single expression anonymous function often used as inline function. A lambda form in python does not have statements as it is used to make new function object and then return them at runtime. 

The lambda operator is used to create anonymous functions. It is mostly used in cases where one wishes to pass functions as parameters. or assign them to variable names.

When we want a function with a single expression, we can define it anonymously. A lambda expression may take input and returns a value. To define the above function as a lambda expression, we type the following code in the interpreter:

```py
(lambda a,b:a if a>b else b)(3,3.5)
```

`3.5`

Here, a and b are the inputs.   
`a if a > b else b` is the expression to return. 
The arguments are 3 and 3.5.

It is possible to not have any inputs here.

`(lambda :print("Hi"))()`

Hi

Example:

```py
myfunction = lambda x:x*x     
a = myfunction(10)        
print(a)
```

Output: 100

- Why can\'t lambda forms in Python contain statements?

Lambdas evaluates at run time and these do not need statements
Lambda is a anonymous function, which does not have a name and no fixed number of arguments. Represented by keyword lambda followed by statement.

Ex:

```py
add = lambda a,b: a+b
add(2,3)
```

output:
`5`

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is map function in Python?

Map function executes the function given as the first argument on all the elements of the iterable given as the second argument. If the function given takes in more than 1 arguments, then many iterables are given. #Follow the link to know more similar functions

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Name few methods that are used to implement Functionally Oriented Programming in Python?

Python supports methods (called iterators in Python3), such as filter(), map(), and reduce(), that are very useful when you need to iterate over the items in a list, create a dictionary, or extract a subset of a list.

- `filter()` – enables you to extract a subset of values based on conditional logic.
- `map()` – it is a built-in function that applies the function to each item in an iterable.
- `reduce()` – repeatedly performs a pair-wise reduction on a sequence until a single value is computed.

## Q. Explain a few methods to implement Functionally Oriented Programming in Python.

Sometimes, when we want to iterate over a list, a few methods come in handy.    

 `filter()`: Filter lets us filter in some values based on conditional logic.

```py 
list(filter(lambda x:x>5,range(8)))
```

 Ans: [6, 7]
 `map()`: Map applies a function to every element in an iterable.

```py 
list(map(lambda x:x**2,range(8)))
```

 Ans: [0, 1, 4, 9, 16, 25, 36, 49]
 
`reduce()`: Reduce repeatedly reduces a sequence pair-wise until we reach a single value
 
```py 
 from functools import reduce
 reduce(lambda x,y:x-y,[1,2,3,4,5])
```

 Ans: -13

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain the difference between `map()`, `reduce()`, and `filter()`?

All three are higher-order functions from functional programming that operate on iterables:

| Function | Operation | Returns | Python 3 |
|----------|-----------|---------|----------|
| `map(f, iterable)` | Apply `f` to each element | `map` iterator | Built-in |
| `filter(pred, iterable)` | Keep elements where `pred` is truthy | `filter` iterator | Built-in |
| `reduce(f, iterable)` | Fold elements into single value using `f` | single value | `functools.reduce` |

```py
from functools import reduce
from typing import Callable

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — transform each element (lazy iterator)
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter — select elements matching predicate (lazy iterator)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)     # [2, 4, 6, 8, 10]

# reduce — aggregate to single value
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(total)     # 55

product = reduce(lambda acc, x: acc * x, numbers, 1)
print(product)   # 3628800

# Chained pipeline (functional composition)
result = reduce(
    lambda acc, x: acc + x,
    filter(lambda x: x % 2 == 0,
    map(lambda x: x ** 2, numbers))
)
print(result)    # sum of squares of evens: 4+16+36+64+100 = 220

# Modern Pythonic equivalent (often more readable)
result2 = sum(x ** 2 for x in numbers if x % 2 == 0)
print(result2)   # 220
```

**Performance note:** `map()` and `filter()` return lazy iterators in Python 3 — no intermediate list is allocated. `reduce()` is O(n) regardless.

**Use Case:** A data transformation service uses `map()` to normalize 1M user records (lowercase, strip), `filter()` to remove invalid entries, and `reduce()` to compute aggregate statistics — all in a single memory-efficient pipeline without materializing intermediate collections.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How can you implement functional programming and why would you?

Functional programming (FP) treats computation as the evaluation of pure functions, avoiding shared state and mutable data. Python supports FP through `map`, `filter`, `functools.reduce`, closures, higher-order functions, and immutable data.

**Why use it?**
- Predictable, testable pure functions (no side effects)
- Composable pipelines
- Easier parallelization (no shared state)
- Concise transformations on collections

```py
from functools import reduce, partial
from itertools import chain, starmap
from typing import Callable, TypeVar

T = TypeVar("T")

# 1. Pure functions — no side effects, same input → same output
def add(a: int, b: int) -> int:
    return a + b

# 2. Higher-order functions
def compose(*funcs: Callable) -> Callable:
    """Compose functions right to left: compose(f, g)(x) == f(g(x))"""
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

double   = lambda x: x * 2
add_one  = lambda x: x + 1
square   = lambda x: x ** 2

transform = compose(double, add_one, square)   # double(add_one(square(x)))
print(transform(3))   # double(add_one(9)) = double(10) = 20

# 3. Partial application
multiply = lambda x, y: x * y
triple = partial(multiply, 3)
print(list(map(triple, [1, 2, 3, 4])))   # [3, 6, 9, 12]

# 4. Functional pipeline using generators
orders = [
    {"product": "A", "qty": 5,  "price": 10.0, "active": True},
    {"product": "B", "qty": 2,  "price": 50.0, "active": False},
    {"product": "C", "qty": 10, "price": 5.0,  "active": True},
]

total_revenue = reduce(
    lambda acc, order: acc + order["qty"] * order["price"],
    filter(lambda o: o["active"], orders),
    0.0,
)
print(f"Total: £{total_revenue:.2f}")   # £100.00
```

**Use Case:** A billing engine implements its pricing logic as pure functions composed into a pipeline: `apply_discount → add_tax → round_to_pence`. Each step is independently unit-testable, and the whole pipeline can be parallelized with `concurrent.futures.ProcessPoolExecutor` safely because there is no shared mutable state.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain `map()`, `filter()`, `reduce()`, and `lambda`.

```py
from functools import reduce

# lambda — anonymous function: lambda args: expression
square  = lambda x: x ** 2
add     = lambda x, y: x + y
print(square(5))      # 25
print(add(3, 4))      # 7

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(func, iterable) — apply func to each element → lazy iterator
doubled    = list(map(lambda x: x * 2, numbers))
str_nums   = list(map(str, numbers))
print(doubled)    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter(predicate, iterable) — keep elements where predicate is True → lazy
evens      = list(filter(lambda x: x % 2 == 0, numbers))
positives  = list(filter(None, [-1, 0, 2, 0, 5]))  # None = truthiness check
print(evens)       # [2, 4, 6, 8, 10]
print(positives)   # [-1, 2, 5]  wait — [-1 is truthy!] → [-1, 2, 5]

# reduce(func, iterable, initial) — fold to single value
total   = reduce(lambda acc, x: acc + x, numbers, 0)
product = reduce(lambda acc, x: acc * x, numbers, 1)
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(total)    # 55
print(product)  # 3628800
print(maximum)  # 10

# Chained functional pipeline
result = reduce(
    lambda acc, x: acc + x,            # sum
    filter(lambda x: x % 2 == 0,       # only evens
    map(lambda x: x ** 2, numbers))    # squared
)
print(result)   # 4+16+36+64+100 = 220

# Pythonic equivalent (often more readable)
result2 = sum(x ** 2 for x in numbers if x % 2 == 0)
print(result2)   # 220

# When to use lambda vs def
# lambda: single expression, used inline (sort key, map/filter callbacks)
data = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
data.sort(key=lambda d: d["age"])   # lambda as sort key
print([d["name"] for d in data])    # ['Alice', 'Bob']
```

**Use Case:** A recommendation engine scores items with `map()` (compute scores), filters with `filter()` (remove below threshold), and reduces with `reduce()` (aggregate final ranking score) — three composable, testable steps replacing a monolithic scoring loop.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are `map()`, `filter()`, and `reduce()` functions?

All three are higher-order functions that operate on iterables without explicit `for` loops:

| Function | What it does | Returns | Module |
|----------|-------------|---------|--------|
| `map(f, it)` | Apply `f` to every element | lazy `map` iterator | built-in |
| `filter(pred, it)` | Keep elements where `pred` is `True` | lazy `filter` iterator | built-in |
| `reduce(f, it, init)` | Fold elements into a single value | single value | `functools` |

```py
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — transform each element
doubled   = list(map(lambda x: x * 2, numbers))
as_str    = list(map(str, numbers))
print(doubled)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter — select elements matching predicate
evens     = list(filter(lambda x: x % 2 == 0, numbers))
non_zero  = list(filter(None, [0, 1, 2, 0, 3]))   # None = truthiness
print(evens)     # [2, 4, 6, 8, 10]

# reduce — accumulate to single value
total   = reduce(lambda acc, x: acc + x, numbers, 0)    # 55
product = reduce(lambda acc, x: acc * x, numbers, 1)    # 3628800
maximum = reduce(lambda a, b: a if a > b else b, numbers)  # 10

# Chained pipeline — sum of squares of even numbers
result = reduce(
    lambda acc, x: acc + x,
    filter(lambda x: x % 2 == 0,
    map(lambda x: x ** 2, numbers))
)
print(result)   # 220  (4+16+36+64+100)

# Pythonic equivalent (generator expression — often more readable)
result2 = sum(x ** 2 for x in numbers if x % 2 == 0)
print(result2)  # 220
```

**Use Case:** A pricing engine uses `map()` to apply a discount function to all products, `filter()` to remove items below minimum margin, and `reduce()` to compute the cart total — three composable, independently testable steps.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 9. Modules and Packages

<br>

## Q. How do I find the current module name?

A module can find out its own module name by looking at the predefined global variable `__name__`. If this has the value `'__main__'`, the program is running as a script. Many modules that are usually used by importing them also provide a command-line interface or a self-test, and only execute this code after checking `__name__`: 

```py
def main():
    print('Running test...')
if __name__ == '__main__':
    main() 
```

`__import__('x.y.z')`
returns Try: `__import__('x.y.z').y.z` 

```py
# For more realistic situations, you may have to do something like:
m = __import__(s) 
	for i in s.split(".")[1:]: m = getattr(m, i) 
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do I access a module written in Python from C?

You can get a pointer to the module object as follows:

`module = PyImport_ImportModule("");`

If the module hasn\'t been imported yet (i.e. it is not yet present in sys.modules), this initializes the module; otherwise it simply returns the value of ``sys.modules[""]``. Note that it doesn\'t enter the module into any namespace -- it only ensures it has been initialized and is stored in sys.modules. You can then access the module\'s attributes (i.e. any name defined in the module) as follows: attr = PyObject_GetAttrString(module, ""); Calling PyObject_SetAttrString() to assign to variables in the module also works.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you create your own package in Python?

It overrides the any initialization from an inherited class and is called when the class is instantiated.

We know that a package may contain sub-packages and modules. A module is nothing but Python code.
To create a package of our own, we create a directory and create a file `__init__.py` in it. We leave it empty. Then, in that package, we create a module(s) with whatever code we want. For a detailed explanation with pictures, refer to Python Packages.

## Q. What is the purpose of PYTHONSTARTUP, PYTHONCASEOK, PYTHONHOME & PYTHONPATH environment variables?

- PYTHONSTARTUP − It contains the path of an initialization file containing Python source code. It is executed every time you start the interpreter. It is named as .pythonrc.py in Unix and it contains commands that load utilities or modify PYTHONPATH. 
    
- PYTHONCASEOK − It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. Set this variable to any value to activate it.
    
- PYTHONHOME − It is an alternative module search path. It is usually embedded in the PYTHONSTARTUP or PYTHONPATH directories to make switching module libraries easy.
    
- PYTHONPATH − It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by the Python installer.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a Python module?

A module is a Python script that generally contains import statements, functions, classes and variable definitions, and Python runnable code and it "lives" file with a '.py' extension. zip files and DLL files can also be modules.Inside the module, you can refer to the module name as a string that is stored in the global variable name .

## Q. Name the File-related modules in Python?

Python provides libraries / modules with functions that enable you to manipulate text files and binary fileson file system. Using them you can create files, update their contents, copy, and delete files. The librariesare : os, os.path, and shutil.

Here,   
`os` and `os.path` – modules include functions for accessing the filesystem   
`shutil` – module enables you to copy and delete the files.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the PYTHONPATH variable?

PYTHONPATH is the variable that tells the interpreter where to locate the module files imported into a program. Hence, it must include the Python source library directory and the directories containing Python source code. You can manually set PYTHONPATH, but usually, the Python installer will preset it.

## Q. Where is math.py (socket.py, regex.py, etc.) source file?

If you can\'t find a source file for a module, it may be a built-in or dynamically loaded module implemented in C, C++ or other compiled language. In this case you may not have the source file or it may be something like mathmodule.c, somewhere in a C source directory (not on the Python Path). There are (at least) three kinds of modules in Python:

- Modules written in Python (.py);
- Modules written in C and dynamically loaded (.dll, .pyd, .so, .sl, etc);
- Modules written in C and linked with the interpreter; to get a list of these, type;
Import sys print sys.builtin_module_names;

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to Search Path of Modules?

By default python interpreter search for the imported modules in the following locations:

- Current directory (main module location)
- Environment variable path
- Installation dependent directory
- If the imported module is not found in the any one of the above locations. Then python interpreter giveserror.
- Built-in attributes of a module:
- By default for each and every python module some properties are added internally and we call thoseproperties as a built-in-attribute of a module

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are the Packages?

Package is nothing but a folder or dictionary which represents collection of modules.

A package can also contain sub packages.

We can import the modules of the package by using package 
name.module name or name.subpackage name.module name

## Q. OS Module

OS Module is a predefined module and which provides various functions and methods to perform the operating system related activities, such as creating the files, removing the files, creating the directories removing the directories, executing the operating system related commands, etc.
Example:

```py
import os
cwd=os.getwd()
print("1", cwd)
os.chdir("samples")
print("2", os.getcwd())
os.chdir(os.pardir)
print("3",os.getcwd())
```
Output:

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is module and package in Python?

In Python, module is the way to structure program. Each Python program file is a module, which imports other modules like objects and attributes.

The folder of Python program is a package of modules. A package can have modules or subfolders.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Should I import an entire module?

It depends on the use case. The two forms have different trade-offs:

| Form | Memory | Namespace | Lazy load | Recommendation |
|------|--------|-----------|-----------|----------------|
| `import module` | Full module loaded | Explicit: `module.func()` | No | Preferred for clarity |
| `from module import name` | Full module still loaded | Direct: `func()` | No | Good for frequently used names |
| `from module import *` | Full module loaded | Pollutes namespace | No | **Avoid** (except `__init__.py` re-exports) |

```py
# Recommended — explicit, avoids name collisions
import os
import json
import pathlib

path = pathlib.Path("/tmp/data.json")
data = json.loads(path.read_text())

# Good — importing specific names you use many times
from datetime import datetime, timezone
from collections import defaultdict

ts = datetime.now(tz=timezone.utc)

# Bad — wildcard import pollutes namespace and hides dependencies
# from os.path import *   # now 'join', 'exists', 'split' are in scope — unclear origin

# Conditional / lazy import — for optional heavy dependencies
def load_data(path: str):
    try:
        import pandas as pd          # deferred — only imported when needed
    except ImportError:
        raise ImportError("pandas is required: pip install pandas")
    return pd.read_csv(path)

# Aliased import — standard for well-known libraries
import numpy as np
import pandas as pd

arr = np.array([1, 2, 3])

# Relative import inside a package
# from .models import User       # import from sibling module
# from ..utils import helpers    # import from parent package
```

**Best practices:**
- `import module` keeps origin clear (`os.path.join` vs `join`)
- `from module import name` is fine for commonly used symbols (`datetime`, `Path`)
- Never use `from module import *` in application code
- Defer heavy imports (`tensorflow`, `pandas`) to avoid slow startup when the feature is optional

**Use Case:** A microservice with optional ML inference defers `import torch` inside the prediction function — the service starts in <200ms for health checks, and only pays the 4-second PyTorch load cost when an inference request actually arrives.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How are modules used in a Python program?

A **module** is any `.py` file. Python finds modules on `sys.path`. You import modules to reuse code across files.

```py
# ── Creating a module ──────────────────────────────────────────────
# math_utils.py
PI = 3.14159265358979

def circle_area(r: float) -> float:
    return PI * r * r

def circle_perimeter(r: float) -> float:
    return 2 * PI * r

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

# ── Importing ──────────────────────────────────────────────────────
import math_utils                        # whole module — use math_utils.PI
from math_utils import circle_area       # single name
from math_utils import PI, Vector2D      # multiple names
import math_utils as mu                  # alias

print(math_utils.circle_area(5))
print(circle_area(5))                    # same result
print(mu.PI)

# ── Standard library modules ───────────────────────────────────────
import os, sys, json, pathlib, datetime, collections, itertools, functools

# os — OS interaction
print(os.getcwd())
print(os.environ.get("PATH", ""))

# pathlib — file system
p = pathlib.Path("README.md")
if p.exists():
    print(p.stat().st_size, "bytes")

# json — serialization
data = {"key": "value", "num": 42}
print(json.dumps(data, indent=2))

# ── Package (directory with __init__.py) ──────────────────────────
# mypackage/
#   __init__.py        ← makes it a package
#   database.py
#   models/
#       __init__.py
#       user.py

# from mypackage import database
# from mypackage.models.user import User

# ── Inspecting modules ────────────────────────────────────────────
import math
print(dir(math))           # list all names in module
print(math.__file__)       # path to module file
print(math.__doc__[:50])   # module docstring
```

**Use Case:** A microservice organises code into `src/api/`, `src/services/`, and `src/repositories/` packages — each layer imports only what it needs via explicit relative imports, enforcing architectural boundaries and making unit testing straightforward.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 10. Object-Oriented Programming

<br>

## Q. How do I call a method defined in a base class from a derived class that overrides it?

If you\'re using new-style classes, use the built-in `super()` function:

```py
class Derived(Base):
    def meth (self): 
       super(Derived, self).meth() 
```

If you\'re using classic classes: For a class definition such as 
`class Derived(Base):` ... you can call method meth() defined in Base (or one of Base\'s base classes) as Base.meth(self,arguments). Here, Base.meth is an unbound method, so you need to provide the self argument.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How can I organize my code to make it easier to change the base class?

You could define an alias for the base class, assign the real base class to it before your class definition, and use the alias throughout your class. Then all you have to change is the value assigned to the alias. Incidentally, this trick is also handy if you want to decide dynamically (e.g. depending on availability of resources) which base class to use. 

Example: BaseAlias = class Derived(BaseAlias): def meth(self): BaseAlias.meth(self).

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain Inheritance in Python with an example?

When one class inherits from another, it is said to be the child/ derived/sub class inheriting from the parent/base/super class. It inherits/gains all members (attributes and methods). Inheritance lets us reuse our code, and also makes it easier to create and maintain applications.

Inheritance allows One class to gain all the members(say attributes and methods) of another class. Inheritance provides code reusability,makes it easier to create and maintain an application. The class from which we are inheriting is called super-class and the class that is inherited is called a derived/child class.

- They are different types of inheritance supported by Python:

    - Single Inheritance – where a derived class acquires the members of a single super class.
    
        _OR_
    
    - Single Inheritance- A class inherits from a single base class. 
    
    - Multi-level inheritance – a derived class d1 in inherited from base class base1, and d2 is inherited from base2.

        _OR_
    - Multilevel Inheritance- A class inherits from a base class, which in turn, inherits from another base class.
    
    - Hierarchical inheritance – from one base class you can inherit any number of child classes

        _OR_
    - Hierarchical Inheritance- Multiple classes inherit from a single base class.  

    - Multiple inheritance – a derived class is inherited from more than one base class.

        _OR_
    - Multiple Inheritance- A class inherits from multiple base classes.
 
    - Hybrid Inheritance- Hybrid inheritance is a combination of two or more types of inheritance.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Hierarchical Inheritance?

The concept of inheriting the properties from one class into multiple classes separately is known as hierarchical inheritance.

Example:

```py
class x(object):    
    def m1(self):       
        print("in m1 of x")

class y(x):     
    def m2(self):   
        print("in m2 of y")

class z(x): 
    def m3(self):   
        print("in m3 of z")
y1=y()
y1.m1()
y1.m2()
a=y1.--hash--()
print(a)
z1=z()
z1.m1()
z1.m3()
b=z1.hash--()
print(b)
```

Output:

```py
M m1 of X 
In m2 of Y
2337815
In m1 of X
In m3 of Z
2099735
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?

Ans. In our article on Multiple Inheritance in Python, we discussed Method Resolution Order (MRO). C does not contain its own version of func(). Since the interpreter searches in a left-to-right fashion, it finds the method in A, and does not go to look for it in B.

## Q. Which methods/functions do we use to determine the type of instance and inheritance?

Ans. Here, we talk about three methods/functions- `type(), isinstance() and issubclass()`.

a. `type()`: This tells us the type of object we\'re working with.

    type(3)
<class 'int'>

    type(False)

<class 'bool'>

    type(lambda :print("Hi"))

<class 'function'>

    type(type)

<class \'type'>

b. isinstance()

This takes in two arguments- a value and a type. If the value is of the kind of the specified type, it returns True. Else, it returns False.

     isinstance(3,int)
True

     isinstance((1),tuple)
False

     isinstance((1,),tuple)
True

c. issubclass()

This takes two classes as arguments. If the first one inherits from the second, it returns True. Else, it returns False.

     class A: pass
     class B(A): pass
     issubclass(B,A)
True

     issubclass(A,B)
False

## Q. Is Python object oriented? what is object oriented programming?

Yes. Python is Object Oriented Programming language. OOP is the programming paradigm based on classes and instances of those classes called objects. The features of OOP are: Encapsulation, Data Abstraction, Inheritance, Polymorphism.

## Q. Does Python supports interfaces like in Java? Discuss?

Python does not provide interfaces like in Java. Abstract Base Class (ABC) and its feature are provided by the Python\'s "abc" module. Abstract Base Class is a mechanism for specifying what methods must be implemented by its implementation subclasses. The use of ABC'c provides a sort of "understanding" about methods and their expected behaviour. This module was made available from Python 2.7 version onwards.

## Q. What are Accessors, mutators, @property?

Accessors and mutators are often called getters and setters in languages like "Java". For example, if x is a property of a user-defined class, then the class would have methods called setX() and getX(). Python has an @property 'decorator' that allows you to ad getters and setters in order to access the attribute of the class.

## Q. What are accessors, mutators, and @property?

Ans. What we call getters and setters in languages like Java, we term accessors and mutators in Python. In Java, if we have a user-defined class with a property 'x', we have methods like getX() and setX(). In Python, we have @property, which is syntactic sugar for property(). This lets us get and set variables without compromising on the conventions. For a detailed explanation on property, refer to Python property.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What do you mean by overriding methods?

Ans. Suppose class B inherits from class A. Both have the method sayhello()- to each, their own version. B overrides the sayhello() of class A. So, when we create an object of class B, it calls the version that class B has.

```py
class A:
    def sayhello(self):
        print("Hello, I'm A")
class B(A):
    def sayhello(self):
        print("Hello, I'm B")
a=A()
b=B()
a.sayhello()
```
Hello, I\'m A

```py
b.sayhello()
```
Hello, I'm B

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the Difference Between Methods & Constructors?

Methods 	
- Method name can be any name.
- With respect to one object one method can be called for 'n' members of lines 	
- Methods are used to represent business logic to perform the operations

Constructor
- Constructor will be executed automatically whenever we create a object.
- With respect to one object one constructor can be executed only once
- Constructors are used to define & initialize the non static variable

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the Encapsulation?

The concept of binding or grouping related data members along with its related functionalities is known as a Encapsulation.

## Q. How are instance variables different from class variables?

| Aspect | Instance Variable | Class Variable |
|--------|------------------|----------------|
| Defined in | `__init__` (or any method) via `self.x` | Class body, outside methods |
| Scope | Per-object — each instance has its own copy | Shared across all instances |
| Access | `self.x` or `instance.x` | `ClassName.x` or `self.x` (via MRO) |
| Mutation | Affects only that instance | Affects all instances (if mutated on the class) |

```py
class Employee:
    company: str = "Acme Corp"          # class variable — shared
    _headcount: int = 0                  # class variable — shared counter

    def __init__(self, name: str, salary: float) -> None:
        self.name = name                 # instance variable
        self.salary = salary             # instance variable
        Employee._headcount += 1

    @classmethod
    def headcount(cls) -> int:
        return cls._headcount

emp1 = Employee("Alice", 90_000)
emp2 = Employee("Bob", 75_000)

print(Employee.company)       # "Acme Corp"
print(emp1.company)           # "Acme Corp" — reads class variable via MRO
print(Employee.headcount())   # 2

# DANGER: assigning via instance SHADOWS the class variable, not mutates it
emp1.company = "New Corp"
print(emp1.company)           # "New Corp" — instance now has its own copy
print(emp2.company)           # "Acme Corp" — class variable untouched
print(Employee.company)       # "Acme Corp"

# DANGER with mutable class variables — all instances share the SAME list
class BadExample:
    items: list = []           # shared mutable default — antipattern!

a = BadExample()
b = BadExample()
a.items.append(1)
print(b.items)                 # [1] — b was mutated too!

# FIX: use None default and initialize in __init__
class GoodExample:
    def __init__(self) -> None:
        self.items: list = []  # each instance gets its own list
```

**Use Case:** A request-counting middleware uses a class variable `RequestCounter.total` as an atomic counter shared across all instances, while each instance tracks its own `self.request_id` — demonstrating the correct split between shared state and per-request state.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Method Resolution Order (MRO)?

MRO is the **deterministic order** in which Python searches for a method or attribute through a class hierarchy. Python 3 uses the **C3 Linearization algorithm** (also called C3 superclass linearization), which guarantees:
- A class always appears before its parents
- Parent order from the class definition is preserved
- Monotonicity (no class appears before a class it inherits from)

```py
# Diamond inheritance problem
class A:
    def method(self) -> str:
        return "A"

class B(A):
    def method(self) -> str:
        return "B"

class C(A):
    def method(self) -> str:
        return "C"

class D(B, C):    # multiple inheritance
    pass

d = D()
print(d.method())        # "B" — follows MRO

# View the MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
print([cls.__name__ for cls in D.__mro__])
# ['D', 'B', 'C', 'A', 'object']

# super() follows MRO — not just the immediate parent
class Base:
    def greet(self) -> str:
        return "Hello from Base"

class Left(Base):
    def greet(self) -> str:
        return f"Left -> {super().greet()}"

class Right(Base):
    def greet(self) -> str:
        return f"Right -> {super().greet()}"

class Child(Left, Right):
    def greet(self) -> str:
        return f"Child -> {super().greet()}"

print(Child().greet())
# Child -> Left -> Right -> Hello from Base
# super() in Left calls Right (not Base directly) — cooperative MRO
```

**Use Case:** Django\'s class-based views (e.g., `CreateView(LoginRequiredMixin, CreateView)`) rely on C3 MRO to ensure mixins are applied in the correct order — `LoginRequiredMixin.dispatch()` runs before `CreateView.dispatch()`, enforcing authentication.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is multiple inheritance and when should you use it?

**Multiple inheritance** allows a class to inherit from more than one parent class, acquiring all their attributes and methods. Python resolves method lookup order using the **C3 MRO** algorithm, and `super()` cooperatively chains calls through the full MRO.

**Use it when:**
- Composing orthogonal behaviours (mixins): `class View(LoginRequiredMixin, PermissionMixin, BaseView)`
- The "mixin" pattern — small, focused classes that add a single capability
- A class genuinely *is-a* multiple types

**Avoid it when:**
- Classes share overlapping state (use composition instead)
- Hierarchy becomes a diamond of unrelated classes

```py
# Mixin pattern — the idiomatic use of multiple inheritance
class LogMixin:
    def log(self, msg: str) -> None:
        print(f"[{self.__class__.__name__}] {msg}")

class SerializeMixin:
    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

class TimestampMixin:
    from datetime import datetime
    created_at: str = ""

    def set_timestamp(self) -> None:
        from datetime import datetime
        self.created_at = datetime.utcnow().isoformat()

# Combine mixins into a concrete class
class Order(LogMixin, SerializeMixin, TimestampMixin):
    def __init__(self, order_id: str, amount: float) -> None:
        self.order_id = order_id
        self.amount = amount
        self.set_timestamp()

    def process(self) -> None:
        self.log(f"Processing order {self.order_id}")

o = Order("ORD-001", 99.99)
o.process()
print(o.to_dict())
# {'order_id': 'ORD-001', 'amount': 99.99, 'created_at': '2025-...'}

# MRO shows resolution order
print([cls.__name__ for cls in Order.__mro__])
# ['Order', 'LogMixin', 'SerializeMixin', 'TimestampMixin', 'object']
```

**Use Case:** Django\'s class-based views compose `LoginRequiredMixin`, `PermissionRequiredMixin`, and `generic.ListView` via multiple inheritance — each mixin adds one cross-cutting concern (auth, permissions, rendering) without modifying the base class.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a metaclass?

A **metaclass** is the class of a class — it controls how classes themselves are created. When Python executes a `class` statement, it calls the metaclass to construct the class object. `type` is the default metaclass for all Python classes.

The metaclass receives: `(name, bases, namespace)` and returns a new class object. Custom metaclasses allow you to intercept and modify class creation.

```py
# type IS the metaclass of all classes
print(type(int))    # <class 'type'>
print(type(str))    # <class 'type'>
print(type(type))   # <class 'type'>  — type is its own metaclass

# Custom metaclass
class SingletonMeta(type):
    """Metaclass that enforces the Singleton pattern on any class."""
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabasePool(metaclass=SingletonMeta):
    def __init__(self, size: int = 5) -> None:
        self.size = size
        print(f"Pool created with size {size}")

pool1 = DatabasePool(5)   # "Pool created with size 5"
pool2 = DatabasePool(10)  # silent — returns existing instance
print(pool1 is pool2)     # True

# Metaclass that auto-registers subclasses
class PluginMeta(type):
    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:  # skip the base class itself
            PluginMeta.registry[name] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    pass

class CSVPlugin(Plugin):   pass
class JSONPlugin(Plugin):  pass

print(PluginMeta.registry)
# {'CSVPlugin': <class 'CSVPlugin'>, 'JSONPlugin': <class 'JSONPlugin'>}
```

> **When to use:** Metaclasses are rarely needed. Prefer class decorators or `__init_subclass__` for most cases. Use metaclasses only when you need to intercept *class creation itself* (ORMs, plugin systems, API schema generation).

**Use Case:** SQLAlchemy\'s `DeclarativeMeta` metaclass scans class attributes at definition time to build the ORM mapping, table schema, and column metadata — enabling `class User(Base): id = Column(Integer)` syntax without any explicit registration call.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are properties and what is the point?

A **property** is a descriptor that turns method calls into attribute access syntax. It lets you add validation, computed values, or lazy loading **without breaking the public API** — callers use `obj.x` regardless of whether `x` is a plain attribute or a property.

`@property` adds a getter; `@x.setter` / `@x.deleter` add write/delete access.

```py
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius   # private backing attribute

    @property
    def celsius(self) -> float:
        """Getter — called on `obj.celsius`"""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Setter — called on `obj.celsius = value`"""
        if value < -273.15:
            raise ValueError(f"Temperature {value}°C below absolute zero")
        self._celsius = value

    @celsius.deleter
    def celsius(self) -> None:
        del self._celsius

    @property
    def fahrenheit(self) -> float:
        """Computed / read-only property — no setter"""
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15


t = Temperature(100)
print(t.celsius)      # 100 (getter)
print(t.fahrenheit)   # 212.0 (computed, no backing attribute)
t.celsius = 0         # setter with validation
print(t.kelvin)       # 273.15

try:
    t.celsius = -300  # raises ValueError
except ValueError as e:
    print(e)

# t.fahrenheit = 500  # AttributeError: can't set attribute (no setter)
```

**Why not just make it a plain attribute?**
- Plain attributes expose internal representation
- Changing from attribute to method later *breaks* all callers (`obj.x` → `obj.x()`)
- Properties maintain `obj.x` syntax while adding logic invisibly

**Use Case:** A REST API model class uses `@property` for `full_name = f"{first} {last}"` and a `password` setter that automatically hashes input with `bcrypt` — the API surface remains clean attribute access while security logic is enforced transparently.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is polymorphism, and when would I use it?

**Polymorphism** means "many forms" — the same interface (method name / operator) behaves differently depending on the object\'s type. Python supports two kinds:

- **Duck typing polymorphism:** Any object with the right method works, regardless of class hierarchy
- **Subtype polymorphism:** Subclasses override a parent method — callers use the parent type

```py
from abc import ABC, abstractmethod
from typing import Protocol

# 1. Subtype polymorphism — classic OOP
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w, self.h = w, h
    def area(self) -> float:
        return self.w * self.h
    def perimeter(self) -> float:
        return 2 * (self.w + self.h)

def print_shape_info(shape: Shape) -> None:
    print(f"{type(shape).__name__}: area={shape.area():.2f}, "
          f"perimeter={shape.perimeter():.2f}")

shapes: list[Shape] = [Circle(5), Rectangle(4, 6), Circle(2)]
for s in shapes:
    print_shape_info(s)   # same call, different behaviour

# 2. Duck typing polymorphism — no inheritance needed
class Renderer:
    def render(self, template: str) -> str:
        return f"<html>{template}</html>"

class EmailRenderer:
    def render(self, template: str) -> str:
        return f"Subject: {template}"

def send_notification(renderer, msg: str) -> None:
    print(renderer.render(msg))   # works for any object with .render()

send_notification(Renderer(), "Hello")
send_notification(EmailRenderer(), "Hello")  # no common base class needed
```

**When to use:**
- Processing collections of mixed-but-related types (shapes, payment methods, file handlers)
- Plugin/strategy patterns where behaviour varies at runtime
- Any time you want to add new types without modifying existing code (Open/Closed Principle)

**Use Case:** A report generation service stores a list of `ReportSection` objects (charts, tables, text blocks). Calling `section.render(canvas)` on each produces correct output without the caller knowing the concrete type — adding a new `MapSection` requires zero changes to the rendering loop.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a class and what is `self`?

A **class** is a blueprint for creating objects, bundling data (attributes) and behaviour (methods) together. An **instance** is a concrete object created from a class.

`self` is a **reference to the current instance** — the first parameter of every instance method. Python passes it automatically when you call `instance.method()`; you name it `self` by convention (not a keyword).

```py
class BankAccount:
    # Class variable — shared by all instances
    bank_name: str = "PyBank"
    _total_accounts: int = 0

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # self refers to the new instance being constructed
        self.owner = owner           # instance variable
        self._balance = balance      # private instance variable
        BankAccount._total_accounts += 1

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount     # self refers to THIS account

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"

    @classmethod
    def total_accounts(cls) -> int:   # cls = the class itself
        return cls._total_accounts

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

# Creating instances — __init__ called automatically
alice = BankAccount("Alice", 1000.0)
bob   = BankAccount("Bob")           # balance defaults to 0.0

# self is passed automatically — alice is 'self' in deposit()
alice.deposit(500)
print(alice.get_balance())   # 1500.0

# Both instances are independent
bob.deposit(200)
print(bob.get_balance())     # 200.0

print(BankAccount.total_accounts())  # 2
print(repr(alice))   # BankAccount(owner='Alice', balance=1500.00)
```

**Why `self` is explicit:** Unlike Java/C++ `this`, Python\'s explicit `self` makes it immediately clear that a method accesses instance state — improving readability and enabling the method-as-function duality (`BankAccount.deposit(alice, 500)` is valid).

**Use Case:** An e-commerce order system models `Order` as a class — each instance holds its own `items`, `status`, and `customer_id`, while shared business rules (tax rate, currency) live as class variables or static methods.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain `isinstance()`

`isinstance(object, classinfo)` returns `True` if `object` is an instance of `classinfo` or any of its subclasses. It is **type-hierarchy aware** — unlike `type(x) == SomeClass` which only matches the exact type.

```py
# Basic usage
print(isinstance(42, int))         # True
print(isinstance(42, float))       # False
print(isinstance(True, int))       # True — bool IS a subclass of int
print(isinstance("hi", (int, str))) # True — second arg can be a tuple of types

# Hierarchy awareness
class Animal: pass
class Dog(Animal): pass
class GoldenRetriever(Dog): pass

gr = GoldenRetriever()
print(isinstance(gr, GoldenRetriever))   # True
print(isinstance(gr, Dog))               # True — subclass check
print(isinstance(gr, Animal))            # True — transitive
print(isinstance(gr, str))               # False

# type() vs isinstance() — key difference
print(type(True) == int)         # False — exact type match only
print(isinstance(True, int))     # True  — hierarchy-aware

# Using with Abstract Base Classes
from collections.abc import Mapping, Sequence, Iterable

print(isinstance({}, Mapping))         # True
print(isinstance([], Sequence))        # True
print(isinstance("abc", Sequence))     # True
print(isinstance(range(5), Iterable))  # True

# Practical: safe attribute access
def process(value: object) -> str:
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, (int, float)):
        return f"{value:.2f}"
    elif isinstance(value, list):
        return ", ".join(str(v) for v in value)
    else:
        return repr(value)

print(process("hello"))   # HELLO
print(process(3.14))      # 3.14
print(process([1, 2, 3])) # 1, 2, 3
```

**Use Case:** A serialization library uses `isinstance(value, Mapping)` rather than `isinstance(value, dict)` so it correctly handles `OrderedDict`, `defaultdict`, and custom `Mapping` subclasses — making the serializer work with any dict-like object.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are static methods, class methods, and instance methods?

| Method type | First param | Access | Decorator | Use when |
|-------------|-------------|--------|-----------|----------|
| Instance method | `self` (instance) | Instance + class state | (none) | Needs access to instance data |
| Class method | `cls` (class) | Class state only | `@classmethod` | Alternative constructors, factory methods |
| Static method | (none) | Neither | `@staticmethod` | Utility functions logically grouped with the class |

```py
from datetime import datetime

class User:
    _count: int = 0

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.created_at = datetime.utcnow()
        User._count += 1

    # Instance method — has access to self (instance attributes)
    def greet(self) -> str:
        return f"Hi, I'm {self.name} <{self.email}>"

    def is_active(self) -> bool:
        age_days = (datetime.utcnow() - self.created_at).days
        return age_days < 365

    # Class method — receives class, not instance
    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Alternative constructor — factory pattern."""
        return cls(name=data["name"], email=data["email"])

    @classmethod
    def count(cls) -> int:
        return cls._count

    # Static method — no self or cls; logically belongs here
    @staticmethod
    def validate_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1]

# Usage
u1 = User("Alice", "alice@example.com")
u2 = User.from_dict({"name": "Bob", "email": "bob@example.com"})

print(u1.greet())                      # Hi, I'm Alice <alice@example.com>
print(User.count())                    # 2
print(User.validate_email("bad"))      # False
print(User.validate_email("a@b.com"))  # True

# Static methods can also be called on instances (but class is cleaner)
print(u1.validate_email("test@x.io")) # True
```

**Use Case:** An ORM `Model` class uses `@classmethod` `from_row(cls, row)` as a factory to construct model instances from database cursor rows — enabling `User.from_row(row)` without exposing the internal column mapping to callers.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Difference between new-style and old-style classes.

This distinction only matters for **Python 2**. In Python 3 all classes are new-style.

| Feature | Old-style (Python 2 only) | New-style (Python 2.2+ / Python 3 all) |
|---------|--------------------------|---------------------------------------|
| Declaration | `class Foo:` | `class Foo(object):` or just `class Foo:` in Py3 |
| Base class | No implicit base | Implicitly inherits from `object` |
| MRO algorithm | Depth-first (DFS), left to right | C3 Linearization |
| `super()` | Broken in diamond inheritance | Works correctly |
| `type(instance)` | `<type 'instance'>` | `<class '__main__.Foo'>` |
| Descriptors, `__slots__`, properties | Not fully supported | Fully supported |

```py
# Python 3 — ALL classes are new-style automatically
class Animal:         # implicitly: class Animal(object):
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

class PoliceDog(Dog):
    def speak(self) -> str:
        return super().speak() + "! (police)"  # super() works correctly

# Verify new-style
print(PoliceDog.__bases__)              # (<class '__main__.Dog'>,)
print(PoliceDog.__mro__)                # correct C3 order
print(isinstance(PoliceDog(), object))  # True — inherits from object

# object gives all classes built-in methods
d = Dog()
print(dir(d))   # __init__, __str__, __repr__, __eq__, __hash__, etc.

# In Python 2 (for reference — do NOT write this)
# class OldStyle:          pass   # old-style — no object base
# class NewStyle(object):  pass   # new-style (must be explicit in Py2)
```

**Practical implication today:** Always use `class Foo:` in Python 3 — it\'s new-style. If maintaining Python 2 legacy code, add `(object)` explicitly to ensure new-style behaviour.

**Use Case:** A Django migration from Python 2 to 3 required removing redundant `(object)` from hundreds of model class definitions — a safe, automated change since Python 3 makes them equivalent.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are Metaclasses?

A **metaclass** is the class of a class — it controls how class objects are created and can intercept attribute access, method definition, and subclass registration at class creation time. `type` is the default metaclass for all Python classes.

```py
# type is the metaclass of all classes
print(type(int))     # <class 'type'>
print(type(list))    # <class 'type'>
print(type(type))    # <class 'type'>  — type is its own metaclass

# Custom metaclass — intercepts class creation
class ValidatedMeta(type):
    """Ensure all public methods have type annotations."""

    def __new__(mcs, name: str, bases: tuple, namespace: dict):
        for attr_name, attr_val in namespace.items():
            if callable(attr_val) and not attr_name.startswith("_"):
                annotations = getattr(attr_val, "__annotations__", {})
                if "return" not in annotations:
                    raise TypeError(
                        f"{name}.{attr_name}() is missing a return type annotation"
                    )
        return super().__new__(mcs, name, bases, namespace)

class MyService(metaclass=ValidatedMeta):
    def greet(self, name: str) -> str:   # OK — has return annotation
        return f"Hello, {name}"

    # def bad_method(self): pass   # Would raise TypeError at class definition!

# __init_subclass__ — simpler alternative for subclass hooks (Python 3.6+)
class PluginBase:
    _registry: dict[str, type] = {}

    def __init_subclass__(cls, plugin_name: str = "", **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            PluginBase._registry[plugin_name] = cls

class CSVPlugin(PluginBase, plugin_name="csv"):
    def process(self): pass

class JSONPlugin(PluginBase, plugin_name="json"):
    def process(self): pass

print(PluginBase._registry)
# {'csv': <class 'CSVPlugin'>, 'json': <class 'JSONPlugin'>}
```

> **When to use:** Metaclasses are for framework authors. For application code, prefer `__init_subclass__`, class decorators, or `dataclasses`. Use metaclasses only when you need to control *how class objects themselves are constructed*.

**Use Case:** SQLAlchemy\'s `DeclarativeMeta` scans each model class body at definition time to register column descriptors, build table metadata, and wire up the ORM mapper — all happening before any instance is ever created.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a descriptor?

A **descriptor** is any object that defines `__get__`, `__set__`, or `__delete__` and is assigned as a class attribute. Python calls these methods automatically when the attribute is accessed on an instance, enabling properties, methods, `classmethod`, `staticmethod`, and custom validation attributes.

```py
from typing import Any

# Data descriptor — defines both __get__ and __set__
class TypedAttribute:
    """Descriptor that enforces a type on assignment."""

    def __init__(self, name: str, expected_type: type) -> None:
        self._name = name
        self._type = expected_type

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = name   # called automatically at class creation

    def __get__(self, obj: Any, objtype: type = None) -> Any:
        if obj is None:
            return self   # accessed on class, not instance
        return obj.__dict__.get(self._name)

    def __set__(self, obj: Any, value: Any) -> None:
        if not isinstance(value, self._type):
            raise TypeError(
                f"{self._name} must be {self._type.__name__}, "
                f"got {type(value).__name__}"
            )
        obj.__dict__[self._name] = value

class Product:
    name  = TypedAttribute("name",  str)
    price = TypedAttribute("price", float)
    stock = TypedAttribute("stock", int)

    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name  = name    # triggers TypedAttribute.__set__
        self.price = price
        self.stock = stock

p = Product("Widget", 9.99, 100)
print(p.name)    # Widget

try:
    p.price = "expensive"   # raises TypeError
except TypeError as e:
    print(e)   # price must be float, got str

# Non-data descriptor — only __get__ (e.g., functions / methods)
class LazyProperty:
    """Compute once, cache on instance."""
    def __init__(self, func):
        self._func = func
        self.__doc__ = func.__doc__

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        value = self._func(obj)
        obj.__dict__[self._attr] = value   # cache — shadows descriptor
        return value

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @LazyProperty
    def area(self) -> float:
        import math
        print("computing area...")
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area)   # "computing area..." then 78.54...
print(c.area)   # no print — cached in instance __dict__
```

**Use Case:** Django\'s ORM `Field` objects (e.g., `CharField`, `IntegerField`) are descriptors — `model.field_name` triggers `__get__` which queries the deferred value, and assignment triggers `__set__` which validates and stores the value before `save()`.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is MRO (Method Resolution Order)?

**MRO** is the deterministic order in which Python searches a class hierarchy to resolve a method or attribute lookup. Python 3 uses the **C3 Linearization algorithm**, which guarantees:
1. A class always appears before its parents
2. Left-to-right order of parents in the class definition is preserved
3. Monotonicity — no class appears after one of its superclasses

```py
# Diamond inheritance — the classic MRO challenge
class A:
    def method(self) -> str: return "A"

class B(A):
    def method(self) -> str: return "B"

class C(A):
    def method(self) -> str: return "C"

class D(B, C):   # diamond: D → B → C → A → object
    pass

print(D().method())   # "B" — first in MRO

# Inspect MRO
print([cls.__name__ for cls in D.__mro__])
# ['D', 'B', 'C', 'A', 'object']

# super() cooperatively follows MRO
class Base:
    def process(self) -> list:
        return ["Base"]

class Left(Base):
    def process(self) -> list:
        return ["Left"] + super().process()   # calls Right, not Base directly

class Right(Base):
    def process(self) -> list:
        return ["Right"] + super().process()

class Child(Left, Right):
    def process(self) -> list:
        return ["Child"] + super().process()

print(Child().process())
# ['Child', 'Left', 'Right', 'Base']
# MRO: Child → Left → Right → Base → object

# Mixin pattern relying on MRO
class LogMixin:
    def save(self) -> None:
        print(f"[LOG] Saving {self.__class__.__name__}")
        super().save()   # calls next in MRO

class Model:
    def save(self) -> None:
        print("Model.save()")

class User(LogMixin, Model):   # LogMixin.save() → Model.save()
    pass

User().save()
# [LOG] Saving User
# Model.save()
```

**Use Case:** Django\'s class-based views depend on MRO so that `LoginRequiredMixin` (placed first) has its `dispatch()` called before the view\'s `dispatch()`, intercepting unauthenticated requests without modifying `DetailView` at all.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How is a Python class created?

```py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import ClassVar

# 1. Basic class with __init__
class Rectangle:
    # Class variable — shared by all instances
    shape_type: ClassVar[str] = "rectangle"

    def __init__(self, width: float, height: float) -> None:
        self.width  = width    # instance variable
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle): return NotImplemented
        return self.width == other.width and self.height == other.height

r = Rectangle(4, 6)
print(r.area())       # 24.0
print(repr(r))        # Rectangle(width=4, height=6)

# 2. Inheritance
class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)   # delegate to parent

    def __repr__(self) -> str:
        return f"Square(side={self.width})"

s = Square(5)
print(s.area())       # 25.0
print(isinstance(s, Rectangle))  # True

# 3. dataclass — auto-generates __init__, __repr__, __eq__
@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"
    _history: list = field(default_factory=list, repr=False)

    def distance_to(self, other: Point) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))   # 5.0
print(p2)                    # Point(x=3, y=4, label='origin')
```

**Use Case:** A domain model layer defines `@dataclass` classes (`Order`, `LineItem`, `Customer`) with type annotations — getting `__repr__`, `__eq__`, and `__init__` for free while keeping the model readable and `mypy`-checked.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How is a Python class instantiated?

Instantiation calls the **metaclass** (`type.__call__`) which first calls `__new__` (allocate memory, return the new object) then `__init__` (initialize the object). The result is the fully constructed instance.

```py
class Connection:
    def __new__(cls, *args, **kwargs):
        print(f"__new__: allocating {cls.__name__}")
        instance = super().__new__(cls)  # allocate memory
        return instance

    def __init__(self, host: str, port: int) -> None:
        print(f"__init__: initializing with {host}:{port}")
        self.host = host
        self.port = port

    def __repr__(self) -> str:
        return f"Connection({self.host!r}, {self.port})"

# Instantiation — calls __new__ then __init__
conn = Connection("localhost", 5432)
# __new__: allocating Connection
# __init__: initializing with localhost:5432
print(conn)   # Connection('localhost', 5432)

# Multiple instances are independent objects
conn2 = Connection("db.prod", 5432)
print(conn is conn2)    # False — different objects
print(id(conn), id(conn2))

# Singleton via __new__
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.debug = False
            self._initialized = True

cfg1 = Config()
cfg2 = Config()
print(cfg1 is cfg2)   # True — same object

# Named constructors (alternative instantiation patterns)
from datetime import date

d1 = date(2025, 6, 15)        # standard __init__
d2 = date.today()             # classmethod factory
d3 = date.fromisoformat("2025-06-15")  # another classmethod

print(type(d1) is type(d2) is type(d3))  # True — all date instances
```

**Use Case:** An ORM `Session` factory uses `__new__` to return an existing session from the pool instead of creating a new object, making `Session()` syntax act as a transparent pool checkout without callers knowing about pooling.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 11. Exception Handling

<br>

## Q. Explain the use of try: except: raise, and finally:

Try, except and finally blocks are used in Python error handling. Code is executed in the try block until an error occurs. One can use a generic except block, which will receive control after all errors, or one can use specific exception handling blocks for various error types. Control is transferred to the appropriate except block. In all cases, the finally block is executed. Raise may be used to raise your own exceptions.

## Q. Illustrate the proper use of Python error handling.

Code Example:

    try:    
        ….#This can be any code
    except:
        …# error handling code goes here
    finally:
        …# code that will be executed regardless of exception handling goes here.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are the Runtime Errors?

The errors which occurs after starting the execution of the programs are known as runtime errors. Runtime errors can occur because of:

    Invalid Input
    Invalid Logic
    Memory issues
    Hardware failures and so on

With respect to every reason which causes to runtime error correspoing runtime error representation class is available
Runtime error representation classes technically we call as a exception classes.
While executing the program if any runtime error is occur corresponding runtime error representation class object is created
Creating runtime error representation class object is technically known as a rising exception
While executing the program if any exception is raised, then internally python interpreter verify any code is implemented to handle raised exception or not
If code is not implemented to handle raised exception then program will be terminated abnormally

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Abnormal Termination?

The concept of terminating the program in the middle of its execution without executing last statement of the main module is known as a abnormal termination
Abnormal termination is undesirable situation in programming languages.

## Q. What is `try` Block?

A block which is preceded by the try keyword is known as a try block
Syntax:
try{
   //statements that may cause an exception
}

The statements which causes to run time errors and other statements which depends on the execution of run time errors statements are recommended to represent in try block
While executing try block statement if any exception is raised then immediately try block identifies that exception, receive that exception and forward that exception to except block without executing remaining statements to try block.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What happens if you have an error in an `__init__` statement?

If `__init__` raises an exception, the object construction **fails**. `__new__` has already allocated memory for the object, but since `__init__` did not complete, the partially-constructed object is not returned to the caller — the exception propagates instead. Python\'s garbage collector will eventually reclaim the allocated memory via reference counting.

```py
class DatabaseConnection:
    _instances: list["DatabaseConnection"] = []

    def __init__(self, host: str, port: int) -> None:
        if not (1 <= port <= 65535):
            raise ValueError(f"Invalid port: {port}")
        if not host:
            raise ValueError("Host cannot be empty")

        # If an error occurs here, __init__ partially ran
        self.host = host
        self.port = port
        self._connection = self._connect()   # might raise ConnectionError
        DatabaseConnection._instances.append(self)  # only reached if no error

    def _connect(self):
        # Simulate connection failure
        raise ConnectionError(f"Cannot reach {self.host}:{self.port}")

# Test: error in validation
try:
    conn = DatabaseConnection("localhost", 99999)
except ValueError as e:
    print(f"ValueError: {e}")  # Invalid port: 99999
    # conn is never bound — the object does not exist

# Test: error mid-init (after self.host assigned but before append)
try:
    conn2 = DatabaseConnection("db.prod", 5432)
except ConnectionError as e:
    print(f"ConnectionError: {e}")
    # DatabaseConnection._instances is still empty — append never ran

print(DatabaseConnection._instances)  # []
```

**Key takeaway:** Always use `try/except` or `contextlib.ExitStack` in `__init__` to clean up resources (file handles, sockets) if later steps fail — Python does not call `__del__` on the partially-constructed object reliably.

**Use Case:** A connection pool factory wraps `__init__` errors to ensure that failed connection attempts are logged and retried without leaving zombie objects registered in the pool registry.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What happens in Python if you try to divide by zero?

Integer or float division by zero raises `ZeroDivisionError`. The `//` (floor division) and `%` (modulo) operators also raise it. The only exception: `float('inf') / 0` does not raise — it follows IEEE 754 and returns `inf`.

```py
# Integer division by zero
try:
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")   # integer division or modulo by zero

# Float division by zero
try:
    result = 10.0 / 0.0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")   # float division by zero

# Modulo by zero
try:
    result = 7 % 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")   # integer division or modulo by zero

# Safe division utility
def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Return numerator/denominator, or default if denominator is zero."""
    if denominator == 0:
        return default
    return numerator / denominator

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # 0.0

# In numpy, division by zero produces inf/nan (not an exception)
import numpy as np
arr = np.array([1.0, 2.0, 0.0])
with np.errstate(divide="ignore", invalid="ignore"):
    result = np.array([1.0, 2.0]) / arr[:2]
```

**Use Case:** A financial analytics system wraps all division operations in `safe_divide()` to handle missing or zero-denominator data gracefully, returning `None` instead of crashing — critical for ratio metrics like conversion rate where denominators can be zero.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to handle exceptions?

Python uses `try / except / else / finally` blocks. The `else` clause runs only if no exception was raised; `finally` always runs (cleanup).

```py
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught: {e}")

# Multiple except clauses (most specific first)
def parse_config(path: str) -> dict:
    try:
        text = Path(path).read_text(encoding="utf-8")
        import json
        return json.loads(text)
    except FileNotFoundError:
        logger.error("Config file not found: %s", path)
        return {}
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in %s: %s", path, e)
        return {}
    except PermissionError as e:
        raise RuntimeError(f"Cannot read {path}") from e   # chained exception

# else — runs only when no exception occurred
def divide(a: float, b: float) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        print("Division succeeded")   # only runs if no exception
        return result
    finally:
        print("Always runs — cleanup here")   # always executes

# Custom exception hierarchy
class AppError(Exception):
    """Base exception for this application."""

class ValidationError(AppError):
    def __init__(self, field: str, message: str) -> None:
        self.field = field
        super().__init__(f"{field}: {message}")

class DatabaseError(AppError):
    pass

# Catching base class catches all subclasses
try:
    raise ValidationError("email", "invalid format")
except AppError as e:
    print(f"App error: {e}")   # email: invalid format

# Re-raising
try:
    int("not a number")
except ValueError:
    logger.warning("Bad input received")
    raise    # re-raise the same exception with original traceback

# Exception groups (Python 3.11+)
# try:
#     ...
# except* ValueError as eg:
#     for exc in eg.exceptions: handle(exc)
```

**Use Case:** A payment service wraps all third-party API calls with specific `except` clauses: `RequestTimeout` triggers a retry, `AuthError` raises a `PaymentDeclinedError` for the caller, and `finally` always releases the connection back to the pool.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are the different types of exceptions in Python?

Python exceptions form a hierarchy rooted at `BaseException`. Most user-facing exceptions inherit from `Exception`.

```
BaseException
├── SystemExit              # sys.exit()
├── KeyboardInterrupt       # Ctrl+C
├── GeneratorExit           # generator.close()
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError       # list[99] out of range
    │   └── KeyError         # dict["missing"]
    ├── ValueError           # right type, wrong value: int("abc")
    ├── TypeError            # wrong type: 1 + "a"
    ├── AttributeError       # obj.no_such_attr
    ├── NameError            # undefined variable
    │   └── UnboundLocalError
    ├── OSError (IOError, EnvironmentError)
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   ├── TimeoutError
    │   └── ConnectionError
    │       ├── ConnectionRefusedError
    │       └── ConnectionResetError
    ├── RuntimeError
    │   └── RecursionError
    ├── StopIteration
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── MemoryError
    ├── NotImplementedError
    └── AssertionError       # failed assert statement
```

```py
# Triggering common exceptions
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

try:
    lst = [1, 2, 3]; _ = lst[10]
except IndexError as e:
    print(f"IndexError: {e}")

try:
    d = {"a": 1}; _ = d["z"]
except KeyError as e:
    print(f"KeyError: {e}")

try:
    int("not a number")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    open("/etc/shadow")
except PermissionError as e:
    print(f"PermissionError: {e}")

# Catching base class catches all subclasses
try:
    {}["missing"]
except LookupError as e:        # catches both KeyError and IndexError
    print(f"LookupError: {type(e).__name__}: {e}")
```

**Use Case:** A data ingestion service catches `LookupError` for missing fields, `ValueError` for bad formats, and `OSError` for file access problems — each mapped to a specific retry or dead-letter strategy in the error handler.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to write your own custom exception handling?

Define a class hierarchy inheriting from `Exception` (or a more specific built-in), add context attributes, and catch at the appropriate granularity.

```py
# Custom exception hierarchy
class AppError(Exception):
    """Base exception — catch-all for this application."""

class ValidationError(AppError):
    def __init__(self, field: str, message: str, value=None) -> None:
        self.field = field
        self.value = value
        super().__init__(f"[{field}] {message} (got: {value!r})")

class DatabaseError(AppError):
    def __init__(self, operation: str, cause: Exception) -> None:
        self.operation = operation
        super().__init__(f"DB error during '{operation}'")
        self.__cause__ = cause    # explicit exception chaining

class NotFoundError(AppError):
    def __init__(self, resource: str, identifier) -> None:
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} not found: {identifier!r}")

# Using the custom exceptions
def get_user(user_id: int) -> dict:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValidationError("user_id", "Must be a positive integer", user_id)
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    if user_id not in users:
        raise NotFoundError("User", user_id)
    return users[user_id]

def fetch_and_save(user_id: int) -> None:
    try:
        user = get_user(user_id)
        print(f"Found: {user}")
    except ValidationError as e:
        print(f"Validation failed — field={e.field}, value={e.value}")
    except NotFoundError as e:
        print(f"Not found — {e.resource} id={e.identifier}")
    except AppError as e:
        print(f"General app error: {e}")
    finally:
        print("Cleanup always runs")

fetch_and_save(1)    # Found: {'name': 'Alice'}
fetch_and_save(99)   # Not found — User id=99
fetch_and_save(-5)   # Validation failed — field=user_id, value=-5

# Exception chaining (raise X from Y)
try:
    try:
        int("bad")
    except ValueError as e:
        raise DatabaseError("insert", e) from e
except DatabaseError as e:
    print(e)
    print(f"Caused by: {e.__cause__}")
```

**Use Case:** A REST API defines `ValidationError`, `AuthorizationError`, and `NotFoundError` — each mapped in an exception handler middleware to HTTP 400, 403, and 404 responses with structured JSON error bodies, keeping business logic clean of HTTP concerns.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Why does exception handling have a `finally` block?

The `finally` block **always executes** — whether the `try` block succeeded, raised an exception that was caught, raised one that wasn\'t caught, or even executed a `return`/`break`/`continue`. Its purpose is **guaranteed cleanup** of resources (file handles, database connections, locks).

```py
import threading

# finally runs even when an exception is raised and NOT caught
def risky_operation():
    lock = threading.Lock()
    lock.acquire()
    try:
        print("Doing work...")
        result = 10 / 2      # success path
        return result
    except ZeroDivisionError:
        print("Caught division error")
        return None
    finally:
        lock.release()       # ALWAYS runs — prevents deadlock
        print("Lock released (finally)")

print(risky_operation())
# Doing work...
# Lock released (finally)
# 5.0

# finally runs even with return in try
def demo_return():
    try:
        return "from try"    # return is delayed until finally finishes
    finally:
        print("finally ran before returning")
        # return "from finally"  # this would OVERRIDE the try return!

print(demo_return())
# finally ran before returning
# from try

# Practical: file I/O cleanup (the manual way — use `with` in production)
f = None
try:
    f = open("data.txt", "w")
    f.write("hello")
    int("bad")                # raises ValueError
except ValueError as e:
    print(f"Error: {e}")
finally:
    if f:
        f.close()             # file is closed regardless of exception
        print("File closed")

# else + finally together
def read_file(path: str) -> str:
    try:
        text = open(path).read()
    except FileNotFoundError:
        return ""
    else:
        print("Read succeeded")   # only if no exception
        return text
    finally:
        print("Cleanup (always)")  # always
```

**Rule:**
- `else` — runs only when **no exception** occurred
- `finally` — runs **always**, exception or not

**Use Case:** A database transaction wrapper uses `finally` to always call `connection.close()` — even if the application raises an unhandled exception mid-transaction, the connection is returned to the pool and no resources leak.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What happens if an error occurs that is not handled in the `except` block?

If an exception is raised and no matching `except` clause handles it, it **propagates up the call stack** frame by frame until either a handler is found or it reaches the top level. At the top level, Python prints the full **traceback** and terminates the program (or thread).

```py
import traceback
import sys

def level_3() -> None:
    raise ValueError("Something went wrong at level 3")

def level_2() -> None:
    level_3()   # no try/except here — exception propagates up

def level_1() -> None:
    try:
        level_2()
    except TypeError:
        print("Caught TypeError")  # won't match — exception is ValueError
    # ValueError is NOT caught — propagates further

# Unhandled exception terminates the program with a traceback:
# Traceback (most recent call last):
#   File "...", line X, in <module>
#   File "...", line X, in level_1
#   File "...", line X, in level_2
#   File "...", line X, in level_3
# ValueError: Something went wrong at level 3

# Install a global exception handler to log before crash
def global_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    print("UNHANDLED EXCEPTION — logging before exit:")
    traceback.print_exception(exc_type, exc_value, exc_traceback)

sys.excepthook = global_handler

# In threads, unhandled exceptions terminate only THAT thread (not the process)
import threading

def bad_thread():
    raise RuntimeError("Thread crashed")

t = threading.Thread(target=bad_thread)
t.start()
t.join()
print("Main thread continues")   # still runs — thread crash is isolated

# Threading.excepthook (Python 3.8+) — catch unhandled thread exceptions
def thread_exception_handler(args):
    print(f"Thread exception: {args.exc_type.__name__}: {args.exc_value}")

threading.excepthook = thread_exception_handler
```

**Propagation rules:**
1. Exception travels up the call stack looking for a matching `except`
2. `finally` blocks run at each frame during unwinding (cleanup is guaranteed)
3. If no handler found → `sys.excepthook` → traceback printed → process exits with code 1
4. In threads → only that thread terminates; `threading.excepthook` catches it

**Use Case:** A web framework installs a global `sys.excepthook` that serializes the full traceback to a structured JSON log and sends it to Sentry — ensuring every unhandled exception is captured even when the server crashes.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 12. File Handling

<br>

## Q.  How do I copy a file? How to copy object in Python? Diff between shallow copy and deep copy? 

The shutil module contains a `copyfile()` function.

A deep copy copies an object into another. This means that if you make a change to a copy of an object, it won\'t affect the original object. In Python, we use the function deepcopy() for this, and we import the module copy. We use it like:

```py
import copy
b = copy.deepcopy (a)
```

A shallow copy, however, copies one object\'s reference to another. So, if we make a change in the copy, it will affect the original object. For this, we have the function `copy()`, we use it like:

```py
b = copy.copy(a)
```

- Differentiate between lists and tuples.

The major difference is that a list is mutable, but a tuple is immutable. Examples:

```py

```

Traceback (most recent call last):
File "<pyshell#97>", line 1, in <module> mytuple[1]=2

TypeError: \'tuple' object does not support item assignment

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory?

Let us first write a multiple line solution and then convert it to one liner code.

 ```py
with open(SOME_LARGE_FILE) as fh:
    count = 0
    text = fh.read()    
for character in text:
    if character.isupper():
        count += 1
```

## Q. How to display the contents of text file in reverse order?How will you reverse a list?

 `list.reverse()` − Reverses objects of list in place, convert the given file into a list. Reverse the list by using `reversed()`.    
   E.g.:     
   ```py    
   for line in reversed(list(open("file-name","r"))):
        print(line)
   ```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Write a Python program to read a random line from a file.

```py
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
    print(random_line('test.txt'))
```

## Q. Write a Python program to count the number of lines in a text file?

```py
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

print("Number of lines in the file: ",file_lengthy("test.txt"))
```

## Q. Write Python logic to count the number of capital letters in a file?

```py
import os
os.chdir('C:\\Users\\lifei\\Desktop')
with open('Today.txt') as today:
    count = 0
    for i in today.read():
        if i.isupper():
            count+=1
    print(count)
```

26

## Q. What functions or methods will you use to delete a file in Python?

Ans. For this, we may use remove() or unlink().

     import os
     os.chdir('C:\\Users\\lifei\\Desktop')
     os.remove(\'try.py')
    

When we go and check our Desktop, the file is gone. Let\'s go make it again so we can delete it again using unlink().

     os.unlink(\'try.py')
    

Both functions are the same, but unlink is the traditional Unix name for it.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is File Handling?

File is a named location on the disk, which stores the data in permanent manner.
Python language provides various functions and methods to provide the communication between python programs and files.
Python programs can open the file, perform the read or write operations on the file and close the file
We can open the files by calling open function of built-in-modules
At the time of opening the file, we have to specify the mode of the file
Mode of the file indicates for what purpose the file is going to be opened(r,w,a,b)

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain how to delete a file in Python?

By using a command os.remove (filename) or os.unlink(filename)

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you count the lines in a file?

```py
from pathlib import Path

file_path = Path("data.txt")

# Method 1: Generator expression — O(1) memory, reads line by line
with open(file_path, "r", encoding="utf-8") as f:
    line_count = sum(1 for _ in f)
print(f"Lines: {line_count}")

# Method 2: len(readlines()) — loads entire file into memory (avoid for large files)
with open(file_path, "r", encoding="utf-8") as f:
    line_count = len(f.readlines())

# Method 3: enumerate — useful when you also need the last line number
with open(file_path, "r", encoding="utf-8") as f:
    for line_count, _ in enumerate(f, start=1):
        pass
print(f"Lines: {line_count}")
```

**Use Case:** A log monitoring service counts lines in rotating log files every minute using the generator approach to check ingestion rate (lines/sec) without loading multi-GB log files into memory.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to access a file on a Linux server using Python?

There are three main approaches depending on protocol:

```py
# Method 1: Paramiko (SSH/SFTP) — most common for secure remote file access
import paramiko
from pathlib import Path

def download_remote_file(
    hostname: str,
    username: str,
    key_path: str,
    remote_path: str,
    local_path: str,
) -> None:
    """Download a file from a remote Linux server over SFTP."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())  # secure: reject unknown hosts
    try:
        client.connect(
            hostname=hostname,
            username=username,
            key_filename=key_path,
            timeout=10,
        )
        with client.open_sftp() as sftp:
            sftp.get(remote_path, local_path)
            print(f"Downloaded {remote_path} → {local_path}")
    finally:
        client.close()

# Usage
download_remote_file(
    hostname="10.0.0.5",
    username="deploy",
    key_path="/home/user/.ssh/id_rsa",
    remote_path="/var/log/app/app.log",
    local_path="/tmp/app.log",
)


# Method 2: Execute remote commands and capture output
def read_remote_file_content(hostname: str, username: str, key_path: str, remote_path: str) -> str:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    client.connect(hostname=hostname, username=username, key_filename=key_path)
    try:
        _, stdout, stderr = client.exec_command(f"cat {remote_path}")
        return stdout.read().decode("utf-8")
    finally:
        client.close()


# Method 3: Mount via sshfs (OS-level), then use normal file I/O
# $ sshfs user@host:/remote/path /mnt/remote
with open("/mnt/remote/data.csv", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

> **Security Note:** Always use `RejectPolicy` (not `AutoAddPolicy`) for SSH host key verification to prevent man-in-the-middle attacks.

**Use Case:** A DevOps automation script uses `paramiko` to pull the last 1000 lines of application logs from 50 production servers in parallel using `concurrent.futures.ThreadPoolExecutor`, aggregating them for a centralized error dashboard.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain all the file processing modes supported by Python.

```py
from pathlib import Path

# Mode reference
# ┌──────┬────────┬────────┬────────┬─────────────────────────────┐
# │ Mode │ Read   │ Write  │ Create │ Notes                        │
# ├──────┼────────┼────────┼────────┼─────────────────────────────┤
# │ 'r'  │ Yes    │ No     │ No     │ Default; error if not exists │
# │ 'w'  │ No     │ Yes    │ Yes    │ Truncates existing file      │
# │ 'a'  │ No     │ Yes    │ Yes    │ Appends; preserves content   │
# │ 'x'  │ No     │ Yes    │ Yes    │ Exclusive create; error if   │
# │      │        │        │        │ file exists                  │
# │ 'r+' │ Yes    │ Yes    │ No     │ Read+write; no truncate      │
# │ 'w+' │ Yes    │ Yes    │ Yes    │ Read+write; truncates        │
# │ 'a+' │ Yes    │ Yes    │ Yes    │ Read+append                  │
# └──────┴────────┴────────┴────────┴─────────────────────────────┘
# Append 'b' for binary mode: 'rb', 'wb', 'ab', 'rb+', 'wb+'

# 'r' — read text (default)
# with open("data.txt", "r", encoding="utf-8") as f:
#     content = f.read()       # whole file
#     line = f.readline()      # one line
#     lines = f.readlines()    # list of lines

# 'w' — write text (creates or truncates)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.writelines(["Line 2\n", "Line 3\n"])

# 'a' — append (safe for log files)
with open("app.log", "a", encoding="utf-8") as f:
    f.write("2025-06-15 INFO: service started\n")

# 'x' — exclusive create (fails if file exists — safe for atomic create)
try:
    with open("new_file.txt", "x", encoding="utf-8") as f:
        f.write("Created fresh")
except FileExistsError:
    print("File already exists — not overwritten")

# 'r+' — read and write without truncating
with open("output.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    f.seek(0)               # rewind to start
    f.write(content.upper())

# 'rb' / 'wb' — binary mode (images, PDFs, pickles)
with open("output.txt", "rb") as f:
    raw: bytes = f.read()
    print(raw[:20])

# Pathlib equivalents (preferred in modern Python)
p = Path("data.json")
p.write_text('{"key": "value"}', encoding="utf-8")  # 'w'
text = p.read_text(encoding="utf-8")                 # 'r'
p.write_bytes(b"\x89PNG\r\n")                        # 'wb'
```

**Use Case:** A log rotation service opens log files in `'a'` mode so concurrent writers can safely append without overwriting each other, and `'x'` mode to atomically create a new rotation lock file — failing fast if another process already claimed it.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 13. Memory Management

<br>

## Q. How is memory managed in Python?

Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter. Like other programming language python also has garbage collector which will take care of memory management in python.Python also have an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space. The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.

Python has a private heap space to hold all objects and data structures. Being programmers, we cannot access it; it is the interpreter that manages it. But with the core API, we can access some tools. The Python memory manager controls the allocation. 

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How will you check memory leak on Linux?

There are several tools and techniques that can be used to check for memory leaks on Linux:

- Valgrind: Valgrind is a powerful memory debugging tool that can be used to detect memory leaks, among other issues. It works by running the program in a simulated environment that tracks all memory allocations and deallocations, and generates a detailed report of any errors or leaks that it finds.

- LeakSanitizer (LSan): LSan is a lightweight tool that is built into the Clang and GCC compilers. It can be used to detect memory leaks at runtime by instrumenting the code with memory tracking code. When a leak is detected, LSan generates a report that includes the stack trace of the leaking allocation.

- AddressSanitizer (ASan): ASan is another tool built into the Clang and GCC compilers. It can be used to detect a wide range of memory errors, including memory leaks, buffer overflows, and use-after-free errors. Like LSan, ASan instruments the code with memory tracking code and generates a report when an error is detected.

- /proc/meminfo: The /proc/meminfo file contains information about the system\'s memory usage, including the total amount of memory, the amount of free memory, and the amount of memory used by each process. By monitoring the values in this file over time, it may be possible to detect a memory leak by looking for a steady increase in the amount of memory used by a particular process.

- ps and top: The ps and top commands can be used to monitor the system\'s memory usage and identify processes that are consuming large amounts of memory. By monitoring the memory usage of a particular process over time, it may be possible to detect a memory leak by looking for a steady increase in the amount of memory used by that process.

In general, detecting and diagnosing memory leaks can be a complex and time-consuming process. It often requires a combination of tools and techniques, as well as a deep understanding of the code and the system\'s memory usage patterns.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the importance of reference counting?

In Python, reference counting is a technique used for automatic memory management. It involves keeping track of the number of references to an object and automatically deallocating the object when there are no more references to it.

The importance of reference counting in Python can be summarized as follows:

- Automatic memory management: Reference counting allows Python to automatically manage memory without requiring explicit memory allocation or deallocation by the programmer. This simplifies programming and reduces the risk of memory leaks and other memory-related bugs.

- Efficient memory management: By deallocating objects as soon as they are no longer needed, reference counting helps to minimize the amount of memory used by a program. This is especially important for long-running programs or programs that work with large data sets.

- Improved performance: Because Python uses reference counting to manage memory, it can often achieve better performance than other languages that use garbage collection or other memory management techniques. This is because reference counting can be faster and more predictable than other methods, especially for small or short-lived objects.

- Object lifetime management: Reference counting ensures that objects are deallocated as soon as they are no longer needed, which helps to avoid problems such as dangling pointers or use-after-free errors. This helps to ensure the correctness and reliability of Python programs.

Overall, reference counting is a key feature of Python\'s automatic memory management system, and it plays an important role in ensuring that Python programs are both efficient and reliable.

## Q. What is the size of an integer in Python?

Unlike C/Java where `int` is fixed at 4 bytes, Python integers have **arbitrary precision** — they grow as needed. CPython uses a `PyLongObject` struct. A small integer takes **28 bytes** minimum (`sys.getsizeof(0)`), and size grows with magnitude. CPython also maintains a **small integer cache** for values in `[-5, 256]`, reusing the same object rather than allocating new ones.

```py
import sys

print(sys.getsizeof(0))        # 24 bytes (Python 3.11+)
print(sys.getsizeof(1))        # 28 bytes
print(sys.getsizeof(2**30))    # 32 bytes
print(sys.getsizeof(2**60))    # 36 bytes
print(sys.getsizeof(2**90))    # 40 bytes — grows with digit count

# Small integer cache demo
a = 256
b = 256
print(a is b)   # True — same cached object

a = 257
b = 257
print(a is b)   # False — different objects (outside cache range)

# Python handles arbitrarily large integers natively
big = 2 ** 10000
print(type(big))  # <class 'int'>
```

**Use Case:** Cryptographic libraries (e.g., RSA key generation) rely on Python\'s arbitrary-precision integers to perform modular exponentiation with 2048-bit or 4096-bit numbers natively, without any overflow concerns.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How does Python manage memory?

CPython uses a three-layer memory management system:

1. **Reference Counting** — Every object has a `ob_refcnt` field. When it drops to zero, memory is freed immediately. Handles ~99% of objects.
2. **Cyclic Garbage Collector** (`gc` module) — Handles reference cycles (e.g., `a.ref = b; b.ref = a`). Uses generational collection across 3 generations (thresholds: 700, 10, 10 by default).
3. **PyMalloc Arena Allocator** — For objects ≤ 512 bytes, CPython uses its own allocator (bypassing `malloc`) organized as: Arenas (256 KB) → Pools (4 KB) → Blocks (8–512 bytes in 8-byte increments).

```py
import sys
import gc

# Check reference count
x = [1, 2, 3]
print(sys.getrefcount(x))   # 2 (one for x, one for getrefcount arg)

y = x
print(sys.getrefcount(x))   # 3

del y
print(sys.getrefcount(x))   # 2 again

# Force garbage collection of cyclic references
class Node:
    def __init__(self) -> None:
        self.next: "Node | None" = None

a = Node()
b = Node()
a.next = b
b.next = a   # cycle!
del a, b

collected = gc.collect()    # manually trigger GC
print(f"Collected {collected} objects")

# Inspect GC thresholds
print(gc.get_threshold())   # (700, 10, 10)
```

**Use Case:** A long-running data processing service tuned `gc.set_threshold(1000, 15, 15)` to reduce GC pauses on throughput-sensitive workloads, and used `__slots__` on hot objects to reduce per-instance memory from ~264 bytes to ~56 bytes.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How will you measure memory on a Linux server?

```py
import subprocess
import pathlib
import os

# 1. /proc/meminfo — kernel memory counters
def read_meminfo() -> dict[str, int]:
    """Parse /proc/meminfo into a dict of kilobyte values."""
    info = {}
    for line in pathlib.Path("/proc/meminfo").read_text().splitlines():
        parts = line.split()
        if len(parts) >= 2:
            info[parts[0].rstrip(":")] = int(parts[1])
    return info

# mem = read_meminfo()
# print(f"Total:     {mem['MemTotal'] // 1024} MB")
# print(f"Free:      {mem['MemFree'] // 1024} MB")
# print(f"Available: {mem['MemAvailable'] // 1024} MB")
# print(f"Cached:    {mem['Cached'] // 1024} MB")
# print(f"Swap used: {(mem['SwapTotal'] - mem['SwapFree']) // 1024} MB")

# 2. /proc/self/status — memory of the current process
def process_memory_kb() -> dict[str, int]:
    info = {}
    for line in pathlib.Path("/proc/self/status").read_text().splitlines():
        if line.startswith(("VmRSS:", "VmPeak:", "VmSize:")):
            key, val = line.split(":", 1)
            info[key.strip()] = int(val.strip().split()[0])
    return info

# 3. psutil — cross-platform, most Pythonic
import psutil

def memory_report() -> dict:
    vm   = psutil.virtual_memory()
    swap = psutil.swap_memory()
    proc = psutil.Process(os.getpid())

    return {
        "system": {
            "total_gb":     round(vm.total     / 1e9, 2),
            "available_gb": round(vm.available / 1e9, 2),
            "used_pct":     vm.percent,
        },
        "swap": {
            "total_gb": round(swap.total / 1e9, 2),
            "used_pct": swap.percent,
        },
        "this_process": {
            "rss_mb":   round(proc.memory_info().rss  / 1e6, 1),
            "vms_mb":   round(proc.memory_info().vms  / 1e6, 1),
            "pct":      round(proc.memory_percent(), 2),
        },
    }

# print(memory_report())

# 4. tracemalloc — trace Python object allocations
import tracemalloc

tracemalloc.start()

# Code to profile
data = [list(range(1000)) for _ in range(100)]

snapshot = tracemalloc.take_snapshot()
top = snapshot.statistics("lineno")[:5]
for stat in top:
    print(stat)   # file:line: size KB

# 5. Shell commands (via subprocess)
commands = {
    "free -h":                 "human-readable RAM + swap summary",
    "vmstat -s":               "virtual memory stats",
    "cat /proc/meminfo":       "kernel memory breakdown",
    "ps aux --sort=-%mem | head -10": "top 10 memory processes",
    "smem -r -k | head -10":  "proportional set size (PSS) per process",
}
```

**Memory metrics to monitor:**

| Metric | What it means |
|--------|--------------|
| `MemTotal` | Physical RAM |
| `MemAvailable` | RAM available without swapping |
| `Cached` | Disk cache (reclaimable) |
| `SwapUsed` | Swap in use — indicates memory pressure |
| `VmRSS` | Resident Set Size — actual RAM used by process |
| `VmSize` | Virtual memory size (includes mapped files) |

**Use Case:** A production ML inference service runs `psutil.Process().memory_info().rss` as a Prometheus gauge — alerting when RSS exceeds 80% of the container memory limit, triggering a graceful restart before the OOM killer terminates the pod.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 14. Garbage Collector

<br>

## Q. What is Garbage Collection?

The concept of removing unused or unreferenced objects from the memory location is known as a Garbage Collection. While executing the program, if garbage collection takes place then more memory space is available for the program and rest of the program execution becomes faster.

Garbage collector is a predefined program, which removes the unused or unreferenced objects from the memory location.

Any object reference count becomes zero then we call that object as a unused or unreferenced object Then no.of reference variables which are pointing the object is known as a reference count of the object.

While executing the python program if any object reference count becomes zero, then internally python interpreter calls the garbage collector and garbage collector will remove that object from memory location.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Why isn\'t all memory freed when Python exits?

Objects referenced from the global namespaces of Python modules are not always deallocated when Python exits. This may happen if there are circular references. There are also certain bits of memory ...

## Q. Whenever you exit Python, is all memory de-allocated?

The answer here is no. The modules with circular references to other objects, or to objects referenced from global namespaces, aren\'t always freed on exiting Python.
Plus, it is impossible to de-allocate portions of memory reserved by the C library.

Whenever Python exits, especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freed.It is impossible to de-allocate those portions of memory that are reserved by the C library.On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other object.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 15. Mutable vs Immutable

<br>

## Q. What Are The Types of Objects Support in Python Language?

Python supports are two types are of objects. They are:

Immutable built-in types:

    Strings
    Tuples
    Numbers

Mutable built-in types:

    List
    Sets
    Dictionaries

- Immutable Objects

    The objects which doesn\'t allow to modify the contents of those objects are known as 'Immutable Objects'
    
    Before creating immutable objects with some content python interpreter verifies is already any object is available. In memory location with same content or not.
    
    If already object is not available then python interpreter creates new objects with that content and store that object address two reference variable.
    
    If already object is present in memory location with the same content creating new objects already existing object address will be given to the reference variable.

    _Program:_

```py
i=1000
print(i)
print(type(i))
print(id(i))
j=2000
print(j)
print(type(j))
print(id(j))
x=3000
print(x)
print(type(x))
print(id(x))
y=3000
print(y)
print(type(y))
print(id(y))
```

    `int, float, complex, bool, str, tuple` are immutable objects

    Immutable objects performance is high.

    Applying iterations on Immutable objects takes less time.
    
    All fundamentals types represented classes objects and tuple class objects are immutable objects.

- Mutable Objects:
    1. The Objects which allows to modify the contents of those objects are known as 'Mutable Objects'
    2. We can create two different mutable objects with same content

    Program:

    ```py
    x=[10,20,30]
    print(x)
    print(type(x))
    print(id(x))
    y=[10,20,30]
    print(y)
    print(type(y))
    print(id(y))
    ```

    Output:

    `List, set, dict` classes objects are mutable objects
    
    Mutable objects performance is low when compared to immutable objects   
    Applying Iterations mutable objects takes huge time

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Python is Call by Value or Call by Reference? How are arguments passed by value or by reference?

Everything in Python is an object and all variables hold references to the objects. The references values are according to the functions; as a result you cannot change the value of the references. However, you can change the objects if it is mutable.

## Q. Explain parameter-passing mechanism in python?

- To pass its parameters to a function, Python uses pass-by-reference. If you change a parameter within a function, the change reflects in the calling function. This is its default behavior.

- However, when we pass literal arguments like strings, numbers, or tuples, they pass by value. This is because they are immutable.

## Q. How can you copy an object in Python?

To copy an object in Python, you can try copy.copy () or copy.deepcopy() for the general case. You cannot copy all objects but most of them.

## Q. Is a tuple mutable or immutable?

Tuples are **immutable** — you cannot add, remove, or replace elements after creation. However, if a tuple *contains* a mutable object (like a list), that inner object can be mutated.

```py
# Immutable — cannot reassign elements
point = (10, 20)
try:
    point[0] = 99           # raises TypeError
except TypeError as e:
    print(e)  # 'tuple' object does not support item assignment

# But a tuple holding a mutable object: the container is immutable, contents are not
record = (1, [2, 3], "hello")
record[1].append(4)         # allowed — mutating the list inside
print(record)               # (1, [2, 3, 4], 'hello')

# Tuples are hashable ONLY when all elements are hashable
hashable_tuple = (1, 2, 3)
print(hash(hashable_tuple))     # valid

unhashable_tuple = (1, [2, 3])
try:
    hash(unhashable_tuple)      # raises TypeError
except TypeError as e:
    print(e)  # unhashable type: 'list'

# Performance: tuple creation is faster than list
import timeit
print(timeit.timeit("(1,2,3,4,5)", number=10_000_000))   # ~0.07s
print(timeit.timeit("[1,2,3,4,5]", number=10_000_000))   # ~0.45s
```

**Use Case:** Database record rows returned by `psycopg2` are tuples — immutability guarantees that row data is not accidentally mutated between the fetch and the business logic layer, and their hashability allows rows to be used as dictionary keys for deduplication.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 16. Iterators and Generators

<br>

## Q. In Python what are iterators?

In Python, iterators are used to iterate a group of elements, containers like list.

## Q. What are generators in Python?

The way of implementing iterators are known as generators. It is a normal function except that it yields expression in the function.    
Python generator produces a sequence of values to iterate on. This way, it is kind of an iterable. We define a function that 'yields' values one by one, and then use a for loop to iterate on it.
```
    def squares(n):
        i=1
        while(i<=n):
            yield i**2
            i+=1
    for i in squares(7):
        print(i)
```

1   
4   
9   
16  
25  
36  
49

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. So, what is an iterator, then?

An iterator returns one object at a time to iterate on. To create an iterator, we use the iter() function.

    odds=iter([1,3,5])

Then, we call the next() function on it every time we want an object.

     next(odds)
1

     next(odds)
3

     next(odds)
5

And now, when we call it again, it raises a StopIteration exception. This is because it has reached the end of the values to iterate on.

     next(odds)

    Traceback (most recent call last):
    File "<pyshell#295>", line 1, in <module> next(odds)
    StopIteration

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain generators and iterators in python?

- They do, but there are subtle differences:

- For a generator, we create a function. For an iterator, we use in-built functions `iter()` and `next()`.
- For a generator, we use the keyword 'yield' to yield/return an object at a time.
- A generator may have as many 'yield' statements as you want.
- A generator will save the states of the local variables every time 'yield' will pause the loop. 
- An iterator does not use local variables; it only needs an iterable to iterate on.
- Using a class, you can implement your own iterator, but not a generator.
- Generators are fast, compact, and simpler.
- Iterators are more memory-efficient.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a generator? What can it be used for?

A generator is a function that uses `yield` to produce values **lazily** — one at a time, on demand — rather than computing and storing all values at once. It implements the iterator protocol automatically (provides `__iter__` and `__next__`). Execution is **suspended** at each `yield` and **resumed** on the next `next()` call, preserving local state.

```py
from typing import Generator, Iterator
import sys

# Generator function — produces Fibonacci numbers lazily
def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:            # infinite sequence — memory safe!
        yield a
        a, b = b, a + b

# Only the current value is in memory at any time
gen = fibonacci()
first_10 = [next(gen) for _ in range(10)]
print(first_10)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Memory comparison
list_version  = [x ** 2 for x in range(1_000_000)]   # ~8 MB
gen_version   = (x ** 2 for x in range(1_000_000))    # ~120 bytes

print(sys.getsizeof(list_version))  # ~8,697,456 bytes
print(sys.getsizeof(gen_version))   # 120 bytes

# Generator pipeline — process without loading everything into memory
def read_large_file(path: str) -> Generator[str, None, None]:
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()

def filter_errors(lines: Iterator[str]) -> Generator[str, None, None]:
    for line in lines:
        if "ERROR" in line:
            yield line

def parse_log_entry(lines: Iterator[str]) -> Generator[dict, None, None]:
    for line in lines:
        parts = line.split(" ", 3)
        if len(parts) == 4:
            yield {"timestamp": parts[0], "level": parts[1], "msg": parts[3]}

# Chained pipeline — O(1) memory regardless of file size
# pipeline = parse_log_entry(filter_errors(read_large_file("app.log")))
```

**Use Case:** A log aggregation service uses a generator pipeline to process 10 GB log files line-by-line through filter → parse → enrich stages, keeping memory usage constant at ~50 MB regardless of file size — impossible with a list-based approach.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are Generators?

Generators are functions that produce a sequence of values **lazily** using the `yield` keyword. When called, they return a **generator object** (which is both an iterator and an iterable) without executing the function body. Each call to `next()` resumes execution until the next `yield`.

```py
from typing import Generator
import sys

# Simple generator
def countdown(n: int) -> Generator[int, None, None]:
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2
print(next(gen))   # 1
# next(gen) would raise StopIteration

# yield also receives values via send()
def accumulator() -> Generator[float, float, str]:
    total = 0.0
    while True:
        value = yield total   # yield current total, receive next value
        if value is None:
            break
        total += value
    return f"Final: {total}"

acc = accumulator()
next(acc)              # prime the generator
print(acc.send(10))    # 10.0
print(acc.send(20))    # 30.0
print(acc.send(5))     # 35.0

# Memory efficiency
list_1m   = [x for x in range(1_000_000)]   # ~8.5 MB
gen_1m    = (x for x in range(1_000_000))   # 120 bytes
print(sys.getsizeof(list_1m))   # ~8,697,456
print(sys.getsizeof(gen_1m))    # 120
```

**Use Case:** A streaming data processor uses generators to read records from S3 in chunks, parse them, and yield validated domain objects — the entire pipeline runs in constant memory regardless of dataset size.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are Iterators?

An **iterator** is any object that implements the **iterator protocol**: `__iter__()` (returns `self`) and `__next__()` (returns the next value or raises `StopIteration`). Iterators maintain their position in a sequence between calls.

```py
from typing import Iterator

# Custom iterator class
class NumberRange:
    """Yields integers from start to stop (exclusive), step by step."""

    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        self._current = start
        self._stop = stop
        self._step = step

    def __iter__(self) -> "NumberRange":
        return self   # iterator returns itself

    def __next__(self) -> int:
        if self._current >= self._stop:
            raise StopIteration
        value = self._current
        self._current += self._step
        return value

# Usage
rng = NumberRange(0, 10, 2)
print(list(rng))   # [0, 2, 4, 6, 8]

# All for loops use the iterator protocol internally
for n in NumberRange(1, 4):
    print(n)   # 1, 2, 3

# Built-in iterators
it: Iterator[int] = iter([10, 20, 30])
print(next(it))   # 10
print(next(it))   # 20

# Key distinction: iterable vs iterator
lst = [1, 2, 3]          # iterable — has __iter__ but NOT __next__
it  = iter(lst)           # iterator — has both __iter__ and __next__
print(hasattr(lst, "__next__"))   # False
print(hasattr(it,  "__next__"))   # True
```

**Use Case:** A paginated API client implements an iterator that fetches the next page lazily on each `next()` call, enabling `for record in api_client:` syntax while deferring HTTP requests until needed.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Can a generator be used to create iterators? Give an example.

Yes. **Every generator is an iterator** — generators automatically implement both `__iter__` and `__next__`, satisfying the iterator protocol. A generator function is the most concise way to create a custom iterator.

```py
from typing import Iterator, Generator

# Generator automatically IS an iterator
def even_numbers(limit: int) -> Generator[int, None, None]:
    n = 0
    while n < limit:
        yield n
        n += 2

gen = even_numbers(10)

# __iter__ returns self — it IS an iterator
print(gen.__iter__() is gen)    # True

# __next__ advances the generator
print(next(gen))   # 0
print(next(gen))   # 2
print(next(gen))   # 4

# Equivalent class-based iterator (more verbose, same behaviour)
class EvenNumbers:
    def __init__(self, limit: int) -> None:
        self._n = 0
        self._limit = limit

    def __iter__(self) -> "EvenNumbers":
        return self

    def __next__(self) -> int:
        if self._n >= self._limit:
            raise StopIteration
        value = self._n
        self._n += 2
        return value

# Both behave identically in a for loop
for n in even_numbers(10):
    print(n, end=" ")   # 0 2 4 6 8

for n in EvenNumbers(10):
    print(n, end=" ")   # 0 2 4 6 8
```

**Use Case:** A data pipeline replaces verbose iterator classes with generator functions to stream database query results row-by-row, reducing boilerplate from ~20 lines of iterator class code to 3 lines of generator code with identical memory behaviour.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Can iterators be used to create generators?

No — iterators and generators are **different** constructs. You can consume an iterator inside a generator (using `yield` in a loop), but an iterator class itself is not a generator. Generators are a special type of iterator created via `yield`.

```py
# An iterator cannot become a generator just by being used inside one
class Counter:
    def __init__(self, stop: int) -> None:
        self._val = 0; self._stop = stop
    def __iter__(self): return self
    def __next__(self) -> int:
        if self._val >= self._stop: raise StopIteration
        v = self._val; self._val += 1; return v

# But you CAN wrap an iterator inside a generator function
def filtered_counter(stop: int, predicate) -> "Generator":
    for value in Counter(stop):      # consuming iterator inside generator
        if predicate(value):
            yield value

for n in filtered_counter(10, lambda x: x % 3 == 0):
    print(n, end=" ")   # 0 3 6 9

# Key differences
counter = Counter(3)
print(type(counter))                   # <class '__main__.Counter'>
print(hasattr(counter, "send"))        # False — not a generator
print(hasattr(counter, "throw"))       # False — not a generator
print(hasattr(counter, "gi_frame"))    # False — no generator frame

gen = filtered_counter(3, lambda x: True)
print(type(gen))                       # <class 'generator'>
print(hasattr(gen, "send"))            # True
print(hasattr(gen, "gi_frame"))        # True
```

**Key distinction:** Generators have additional methods (`send()`, `throw()`, `close()`) that iterators don\'t — enabling coroutine-style communication and cooperative cancellation.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are iterators and generators?

**Iterator:** An object implementing `__iter__()` and `__next__()`. Maintains traversal state. Raises `StopIteration` when exhausted.

**Generator:** A special iterator created with a `yield` statement. Suspends and resumes execution, preserving local variable state between `yield` points.

| Aspect | Iterator (class) | Generator (function) |
|--------|-----------------|---------------------|
| Creation | Class with `__iter__`/`__next__` | Function with `yield` |
| State storage | Instance attributes | Execution frame (automatic) |
| `send()` / coroutine | No | Yes |
| Memory for infinite seq | Manual | Automatic |
| Code size | Verbose | Concise |

```py
# Both solve the same problem — generator is simpler
def fib_gen():          # generator
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class FibIter:          # iterator class equivalent
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self): return self
    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

from itertools import islice
print(list(islice(fib_gen(), 8)))    # [0, 1, 1, 2, 3, 5, 8, 13]
print(list(islice(FibIter(), 8)))    # [0, 1, 1, 2, 3, 5, 8, 13]
```

**Use Case:** An ETL system uses generator pipelines for memory-efficient processing and class-based iterators for external pagination APIs where explicit state reset (`iter(obj)`) is needed.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What does the `yield` statement do?

`yield` **suspends** a generator function\'s execution and **returns a value** to the caller. The function\'s local state (variables, instruction pointer) is preserved. The next call to `next()` (or iteration) **resumes** from immediately after the `yield`.

```py
from typing import Generator

def step_by_step() -> Generator[str, None, None]:
    print("Step 1")
    yield "first value"    # suspend here, return "first value"
    print("Step 2")
    yield "second value"   # suspend again
    print("Step 3")
    # function ends → StopIteration raised automatically

gen = step_by_step()

val = next(gen)            # prints "Step 1", val = "first value"
print(f"Got: {val}")
val = next(gen)            # prints "Step 2", val = "second value"
print(f"Got: {val}")
# next(gen) would print "Step 3" then raise StopIteration

# yield with send() — bidirectional communication
def echo_double() -> Generator[float, float, None]:
    while True:
        received = yield          # receive a value from send()
        yield received * 2        # yield the doubled result

gen2 = echo_double()
next(gen2)              # prime the generator to the first yield
print(gen2.send(5))     # 10.0
next(gen2)              # advance to the next receive yield
print(gen2.send(7))     # 14.0

# yield from — delegate to sub-generator
def chain(*iterables):
    for it in iterables:
        yield from it   # yields each element of it directly

print(list(chain([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]
```

**Use Case:** An async web framework (like `asyncio`) builds coroutines on top of `yield`/`yield from` — each `await` suspension point is ultimately a `yield` that hands control back to the event loop, enabling thousands of concurrent I/O operations on a single thread.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a generator? Why would I use one?

A **generator** is a function that uses `yield` to produce values **lazily** — one at a time, on demand. Calling a generator function returns a **generator object** (an iterator); execution only starts on the first `next()` call.

**Why use a generator?**

| Reason | Benefit |
|--------|---------|
| **Memory efficiency** | Constant memory regardless of sequence length |
| **Infinite sequences** | Can model streams with no defined end |
| **Pipeline composition** | Chain generators without intermediate lists |
| **Lazy evaluation** | Compute only what is consumed |
| **Coroutines** | `send()` enables bidirectional data flow |

```py
import sys
from typing import Generator, Iterator

# Problem: process a 10 GB log file
# BAD — loads everything into memory
def bad_approach(path: str) -> list[str]:
    with open(path) as f:
        return [line for line in f if "ERROR" in line]  # may OOM

# GOOD — constant memory generator pipeline
def read_lines(path: str) -> Generator[str, None, None]:
    with open(path, encoding="utf-8") as f:
        yield from f

def filter_errors(lines: Iterator[str]) -> Generator[str, None, None]:
    for line in lines:
        if "ERROR" in line:
            yield line.strip()

def parse_error(lines: Iterator[str]) -> Generator[dict, None, None]:
    for line in lines:
        parts = line.split(" ", 2)
        if len(parts) >= 3:
            yield {"ts": parts[0], "svc": parts[1], "msg": parts[2]}

# Entire pipeline: O(1) memory regardless of file size
# pipeline = parse_error(filter_errors(read_lines("app.log")))
# for record in pipeline:
#     send_to_alert_system(record)

# Memory comparison
list_million = [x ** 2 for x in range(1_000_000)]
gen_million  = (x ** 2 for x in range(1_000_000))
print(sys.getsizeof(list_million))   # ~8,697,456 bytes
print(sys.getsizeof(gen_million))    # 120 bytes
```

**Use Case:** A Kafka consumer service uses a generator to yield deserialized messages from a partition indefinitely, feeding them into a processing pipeline without ever accumulating a backlog in memory — critical for high-throughput event streaming.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is `yield`?

`yield` pauses a generator function\'s execution, returns the yielded value to the caller, and **preserves all local state** so execution can resume from the same point on the next `next()` call. It transforms a regular function into a **generator function**.

```py
from typing import Generator

# yield — suspends execution, returns value, resumes on next()
def countdown(n: int) -> Generator[int, None, None]:
    print(f"Starting at {n}")
    while n > 0:
        yield n          # pause here, return n
        n -= 1           # resume here on next call
    print("Done!")

gen = countdown(3)
print(next(gen))   # prints "Starting at 3", returns 3
print(next(gen))   # returns 2
print(next(gen))   # returns 1
# next(gen) → prints "Done!", raises StopIteration

# yield from — delegate to another iterable
def chain_iters(*iterables):
    for it in iterables:
        yield from it   # yields each item from it directly

print(list(chain_iters([1, 2], [3, 4], [5])))  # [1, 2, 3, 4, 5]

# yield with send() — bidirectional coroutine
def running_average() -> Generator[float, float, None]:
    total, count = 0.0, 0
    while True:
        value = yield (total / count if count else 0.0)
        total += value
        count += 1

avg = running_average()
next(avg)               # prime — advance to first yield
print(avg.send(10))     # 10.0
print(avg.send(20))     # 15.0
print(avg.send(30))     # 20.0
```

**`yield` vs `return`:**
| | `return` | `yield` |
|--|----------|---------|
| Terminates function | Yes | No (suspends) |
| State preserved | No | Yes |
| Creates generator | No | Yes |
| Can call multiple times | Yes (restart) | Yes (resume) |

**Use Case:** A streaming CSV writer uses `yield` to produce one formatted row at a time, allowing an HTTP response to stream to the client incrementally rather than buffering all rows in memory before sending.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 17. Decorators

<br>

## Q. What is a decorator? How do I define my own?

Ans. A decorator is a function that adds functionality to another function without modifying it. It wraps another function to add functionality to it. A Python decorator is a specific change that we make in Python syntax to alter functions easily.

```py
def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$")
        func()
            print("$$$$$$$$$$$$$$$$$")
    return wrap

@decor
def sayhi():
    print("Hi")

sayhi()
```
$$$$$$$$$$$$$$$$$
Hi  
$$$$$$$$$$$$$$$$$

Decorators are an example of metaprogramming, where one part of the code tries to change another. For more on decorators, read Python Decorators.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Why use function decorators? Give an example.

A decorator is essentially a callable Python object that is used to modify or extend a function or class definition. 

One of the beauties of decorators is that a single decorator definition can be applied to multiple functions (or classes). Much can thereby be accomplished with decorators that would otherwise require lots of boilerplate (or even worse redundant!) code. 

Flask, for example, uses decorators as the mechanism for adding new endpoints to a web application. Examples of some of the more common uses of decorators include adding synchronization, type enforcement,logging, or pre/post conditions to a class or function.

2. Basic Python Programming Interview Questions

Below are some Basic Python Programming Interview Questions and answers for freshers.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 18. Context Managers

<br>

## Q. Explain the use "with" statement in python?

- In python generally "with" statement is used to open a file, process the data present in the file, and also to close the file without calling a close() method. "with" statement makes the exception handling simpler by providing cleanup activities.

General form of with:

```py
with open("filename", "mode") as file-var:
```

processing statements
Note: no need to close the file by calling close() upon file-var.close()

## Q. What is the `with` statement and its usage?

The `with` statement is Python\'s **context manager** protocol. It guarantees setup and teardown code runs correctly — even if an exception is raised — replacing verbose `try/finally` blocks.

An object used with `with` must implement `__enter__` (setup, returns resource) and `__exit__` (cleanup, receives exception info).

```py
from contextlib import contextmanager, suppress
import threading

# 1. File I/O — file always closed, even on exception
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world")
# f.close() called automatically

# 2. Database transaction pattern
class Transaction:
    def __enter__(self):
        print("BEGIN TRANSACTION")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is None:
            print("COMMIT")
        else:
            print(f"ROLLBACK — {exc_val}")
        return False   # False = don't suppress exceptions

with Transaction() as tx:
    print("Doing work...")
    # raise ValueError("oops")  # would trigger ROLLBACK

# 3. Multiple context managers on one line
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("file A"); b.write("file B")

# 4. @contextmanager — create context manager from a generator
@contextmanager
def timer(label: str):
    import time
    start = time.perf_counter()
    try:
        yield                          # body of the with block runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed * 1000:.2f}ms")

with timer("heavy computation"):
    total = sum(range(10_000_000))

# 5. Suppress specific exceptions
with suppress(FileNotFoundError):
    import os
    os.remove("nonexistent.txt")   # silently ignored

# 6. Threading lock
lock = threading.Lock()
with lock:
    print("thread-safe section")   # lock released even on exception
```

**Use Case:** A database connection pool uses a `with` context manager to check out a connection, run the query, and return the connection to the pool in `__exit__` — ensuring no connections leak even if a query raises an unhandled exception.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 19. Concurrency and Parallelism

<br>

## Q. What is multithreading?

It means running several different programs at the same time concurrently by invoking multiple threads. Multiple threads within a process refer the data space with main thread and they can communicate with each other to share information more easily.Threads are light-weight processes and have less memory overhead. Threads can be used just for quick task like calculating results and also running other processes in the background while the main program is running.

Thread Is a functionality or logic which can execute simultaneously along with the other part of the program.
Thread is a light weight process.
Any program which is under execution is known as process.
We can define the threads in python by overwriting run method of thread class.
Thread class is a predefined class which is defined in threading module.
Thread in module is a predefined module.
If we call the run method directly the logic of the run method will be executed as a normal method logic.
In order to execute the logic of the run method as a we use start method of thread class.
Example

```py
import threading
class x (threading.Thread):
      def run(self):
         for p in range(1, 101):
              print(p)
class y (threading.Thread):
      def run(self):
           for q in range(1, 101):
              print(q)
x1=x()
y1=y()
x1.start()
y1.start()
```

A thread is a lightweight process and multithreading allows us to execute multiple threads at once. As you know, Python is a multithreaded language. It has a multithreading package. The GIL (Global Interpreter Lock) ensures that a single thread executes at a time. A thread holds the GIL and does a little work before passing it on to the next thread. This makes for an illusion of parallel execution. But in reality, it is just threaded taking turns at the CPU. Of course, all the passing around adds overhead to the execution.

## Q. Why do not my signal handlers work?

The most common problem is that the signal handler is declared with the wrong argument list. It is called as:
handler (signum, frame)
So it should be declared with two arguments:
def handler(signum, frame):

## Q. Why is that none of my threads are not running? How can I make it work?

As soon as the main thread exits, all threads are killed. Your main thread is running too quickly, giving the threads no time to do any work.
A simple fix is to add a sleep to the end of the program that\'s long enough for all the threads to finish:

```py
import threading, time
def thread_task(name, n):
for i in range(n): print name, i
for i in range(10)
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Threads Life Cycle?

Threads Life Cycle

- Creating the object of a class which is overwriting run method of thread class is known as a creating thread.
- Whenever thread is created then we call thread is in new state or birth state thread.
- Whenever we call the start method on the new state threads then those threads will be forwarded for scheduling.
- The threads which are forwarded for scheduling are known as ready state threads
- Whenever scheduling time occurs, ready state thread starts execution.
- The threads which are executing are known as running state threads
Whenever sleep fun or join methods are called on the running state threads then immediately those threads will wait.
- The threads which are waiting are known as waiting state threads
Whenever waiting time is over or specified thread execution is over - then immediately waiting state threads are forwarded for scheduling.
- If running state threads execution is over then immediately those threads execution will be terminated
 -The threads which execution is terminated are known as dead state threads.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is scheduling?

Among multiple threads:     
- which thread as to start the execution first,     
- How much time the thread as to execute after allocated time 
  is over,      
- which thread as to continue the execution next this comes under scheduling. Scheduling is highly dynamic

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Does Python provide thread-safe multi-threading?

Python\'s threading module provides OS-level threads, but the **Global Interpreter Lock (GIL)** in CPython ensures only **one thread executes Python bytecode at a time**. This makes individual built-in operations thread-safe but does **not** protect compound operations.

```py
import threading
import time

# GIL: threads don't speed up CPU-bound work
counter = 0

def increment(n: int) -> None:
    global counter
    for _ in range(n):
        counter += 1    # NOT atomic — read-modify-write can interleave!

# Race condition demonstration
counter = 0
threads = [threading.Thread(target=increment, args=(100_000,)) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"Expected: 500000  Got: {counter}")   # likely < 500000!

# Fix: use a Lock
counter = 0
lock = threading.Lock()

def safe_increment(n: int) -> None:
    global counter
    for _ in range(n):
        with lock:
            counter += 1

counter = 0
threads = [threading.Thread(target=safe_increment, args=(100_000,)) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"Safe result: {counter}")   # always 500000

# Fix: use threading.local() for per-thread state
local_data = threading.local()

def worker(value: int) -> None:
    local_data.result = value * 2    # per-thread — no sharing
    time.sleep(0.01)
    print(f"Thread result: {local_data.result}")

# GIL is released during I/O — threads ARE useful for I/O-bound tasks
import urllib.request

def fetch(url: str) -> None:
    with urllib.request.urlopen(url, timeout=5) as resp:
        print(f"{url}: {resp.status}")

# For CPU-bound parallelism, use multiprocessing (bypasses GIL)
from multiprocessing import Pool
with Pool(4) as pool:
    results = pool.map(lambda x: x ** 2, range(10))
```

**Thread-safe primitives:**
- `threading.Lock`, `RLock`, `Semaphore` — mutual exclusion
- `threading.Event`, `Condition` — coordination
- `queue.Queue` — thread-safe FIFO (use this for producer-consumer)

**Use Case:** A web scraper uses `threading.Thread` with `queue.Queue` to fetch 1000 URLs concurrently (I/O-bound — GIL released during network wait), cutting total time from 500s to ~3s, while `Lock` protects the shared results dictionary.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What do you mean by non-blocking I/O?

**Blocking I/O** pauses the current thread until an operation completes (read from socket, write to file). **Non-blocking I/O** returns immediately — either with data or with an indication that the operation is not yet ready — allowing the same thread to handle other tasks in the meantime.

Python\'s `asyncio` module implements non-blocking I/O via an **event loop** and `async/await` coroutines.

```py
import asyncio
import time

# Blocking (synchronous) — each request waits before starting the next
def blocking_fetch(url: str) -> str:
    import urllib.request
    with urllib.request.urlopen(url, timeout=5) as resp:
        return resp.read(100).decode()

# Sequential — total time ≈ sum of individual times
# start = time.perf_counter()
# for url in urls: blocking_fetch(url)
# print(time.perf_counter() - start)   # ~N × latency

# Non-blocking (async) — event loop multiplexes I/O waits
import aiohttp   # pip install aiohttp

async def async_fetch(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()   # yields control to event loop while waiting

async def fetch_all(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [async_fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)   # all run concurrently

# asyncio basics
async def producer() -> None:
    for i in range(3):
        await asyncio.sleep(0.1)   # non-blocking sleep — yields to event loop
        print(f"produced {i}")

async def consumer() -> None:
    for i in range(3):
        await asyncio.sleep(0.15)
        print(f"consumed {i}")

async def main() -> None:
    # Both coroutines interleave on a SINGLE thread
    await asyncio.gather(producer(), consumer())

asyncio.run(main())

# asyncio.Queue for async producer-consumer
async def async_pipeline() -> None:
    queue: asyncio.Queue[int] = asyncio.Queue(maxsize=10)

    async def produce():
        for i in range(5):
            await queue.put(i)
        await queue.put(None)   # sentinel

    async def consume():
        while True:
            item = await queue.get()
            if item is None:
                break
            print(f"Processing {item}")

    await asyncio.gather(produce(), consume())

asyncio.run(async_pipeline())
```

**Blocking vs Non-blocking:**

| | Blocking | Non-blocking (asyncio) |
|--|---------|----------------------|
| Thread per request | Yes | No — single thread |
| Memory | High (thread stacks) | Low |
| CPU-bound | Use `multiprocessing` | Not suitable |
| I/O-bound | Thread pool (limited) | Best choice |

**Use Case:** A FastAPI microservice handles 10,000 concurrent WebSocket connections on a single thread using `asyncio` — each `await` on a database query or HTTP call yields to the event loop, which services other connections during the wait.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## # 20. Testing and Debugging

<br>

## Q. How do you debug a program in Python? Answer in brief.

Ans.  To debug a Python program, we use the 
module. This is the Python debugger; we will discuss it in a tutorial soon. If we start a program using pdb, it will let us step through the code.

## Q. List some pdb commands.

Some pdb commands include-
>
    <b> — Add breakpoint
    <c> — Resume execution
    <s> — Debug step by step
    <n> — Move to next line
    <l> — List source code
    <p> — Print an expression

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What command do we use to debug a Python program?

Ans.  To start debugging, we first open the command prompt, and get to the location the file is at.

Microsoft Windows [Version 10.0.16299.248]

(c) 2017 Microsoft Corporation. All rights reserved.

 

C:\Users\lifei> cd Desktop

C:\Users\lifei\Desktop>

Then, we run the following command (for file try.py):

C:\Users\lifei\Desktop>python -m pdb try.py

> c:\users\lifei\desktop\try.py(1)<module>()

-> for i in range(5):

(Pdb)

Then, we can start debugging.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are the tools that help to find bugs or perform static analysis?

PyChecker is a static analysis tool that detects the bugs in Python source code and warns about the style and complexity of the bug. Pylint is another tool that verifies whether the module meets the coding standard.

## Q. What is unittest in Python? What\'s your approach to unit testing in Python?

A unit testing framework in Python is known as unittest. It supports sharing of setups, automation testing, shutdown code for tests, aggregation of tests into collections etc.

The most fundamental answer to this question centers around Python\'s unittest testing framework. Basically, if a candidate doesn\'t mention unittest when answering this question, that should be a huge red flag.

`unittest` supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework. The unittest module provides classes that make it easy to support these qualities for a set of tests.

Assuming that the candidate does mention unittest (if they don\'t, you may just want to end the interview right then and there!), you should also ask them to describe the key elements of the unittest framework; namely, test fixtures, test cases, test suites and test runners.

A more recent addition to the unittest framework is mock. mock allows you to replace parts of your system under test with mock objects and make assertions about how they are to be used. mock is now part of the Python standard library, available as unittest.mock in Python 3.3 onwards.

The value and power of mock are well explained in An Introduction to Mocking in Python. As noted therein, system calls are prime candidates for mocking: whether writing a script to eject a CD drive, a web server which removes antiquated cache files from /tmp, or a socket server which binds to a TCP port, these calls all feature undesired side-effects in the context of unit tests. Similarly, keeping your unit-tests efficient and performant means keeping as much "slow code" as possible out of the automated test runs, namely filesystem and network access.

[Note: This question is for Python developers who are also experienced in Java.]

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you perform unit-testing on your Python code?

Ans.  For this purpose, we have the module unittest in Python. It has the following members:
>
- FunctionTestCase
- SkipTest
- TestCase
- TestLoader
- TestResult
- TestSuite
- TextTestResult
- TextTestRunner
- defaultTestLoader
- expectedFailure
- findTestCases
- getTestCaseNames
- installHandler
- main
- makeSuite
- registerResult
- removeHandler
- removeResult
- skip
- skipIf
- skipUnless

Below are some Advanced Python Programming Interview Questions For Experienced. I recommend freshers to also refer these interview questions for advanced knowledge.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do I test a Python program or component?

Python comes with two testing frameworks:
The documentation test module finds examples in the documentation strings for a module and runs them, comparing the output with the expected output given in the documentation string.

The unittest moduleis a fancier testing framework modeled on Java and Smalltalk testing frameworks.

For testing, it helps to write the program so that it may be easily tested by using good modular design. Your program should have almost all functionality encapsulated in either functions or class methods. And this sometimes has the surprising and delightful effect of making the program run faster because local variable accesses are faster than global accesses.

Furthermore the program should avoid depending on mutating global variables, since this makes testing much more difficult to do.
The "global main logic" of your program may be as simple as:

if __name__=="__main__":    
    main_logic()

at the bottom of the main module of your program.
Once your program is organized as a tractable collection of functions and class behaviors, you should write test functions that exercise the behaviors.

A test suite can be associated with each module which automates a sequence of tests.

You can make coding much more pleasant by writing your test functions in parallel with the "production code", since this makes it easy to find bugs and even design flaws earlier.

"Support modules" that are not intended to be the main module of a program may include a self-test of the module.

if __name__ == "__main__":
    self_test()

Even programs that interact with complex external interfaces may be tested when the external interfaces are unavailable by using "fake" interfaces implemented in Python.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

### FLASK

## # 21. Miscellaneous

<br>

## Q. What will be the output of the code below?

```py
List = ['a', 'b', 'c', 'd', 'e']
print(list[10:])
```

- TypeError: \'type' object is not subscriptable
if proper name given,it will print [].

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a method?

A method is a function on some object x that you normally call as x.name(arguments...). Methods are defined as functions inside the class definition:

```py
class C: 
    def meth (self, arg): 
        return arg*2 + self.attribute
```

## Q. What is `__slots__` and when is it useful?

In Python, every class can have instance attributes. By default Python uses a `dict` to store an object\'s instance attributes. This is really helpful as it allows setting arbitrary new attributes at runtime.

However, for small classes with known attributes it might be a bottleneck. The `dict` wastes a lot of RAM. Python can\'t just allocate a static amount of memory at object creation to store all the attributes. Therefore it sucks a lot of RAM if you create a lot of objects. The usage of `__slots__` to tell Python not to use a `dict`, and only allocate space for a fixed set of attributes.

**Example:**

**1. Object without slots:**

```py
class MyClass(object):
      def __init__(self, *args, **kwargs):
                self.a = 1
                self.b = 2
  
if __name__ == "__main__":
     instance = MyClass()
     print(instance.__dict__)
```

**2. Object with slots:**

```py
class MyClass(object):
      __slots__=['a', 'b']
      def __init__(self, *args, **kwargs):
                self.a = 1
                self.b = 2
  
if __name__ == "__main__":
     instance = MyClass()
     print(instance.__slots__)
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Monkey patching ? Give example ?

Dynamically modifying a class or module at run-time.

```py
class A:
    def func(self):
        print("Hi")
    def monkey(self):
        print "Hi, monkey"
    m.A.func = monkey
    a = m.A()
    a.func()
```

Hi, monkey

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain serialization and deserialization / Pickling and unpicking?

Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.

To create portable serialized representations of Python objects, we have the module 'pickle'. It accepts a Python object (remember, everything in Python is an object). It then converts it into a string representation and uses the dump() function to dump it into a file. We call this pickling. In contrast, retrieving objects from this stored string representation is termed 'unpickling'.

The pickle module implements binary protocols for serializing and deserializing a Python object structure. "Pickling" is the process whereby a Python object hierarchy is converted into a byte stream, and "unpickling" is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as `serialization`, `marshalling`, or `flattening`; however, to avoid confusion, the terms used here are `pickling` and `unpickling`.

```py
import json
json_string = json.dumps([1, 2, 3, "a", "b"])
print(json_string)
        
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b"])
print(pickle.loads(pickled_string))
```

Reference:

[1]   https://www.sanfoundry.com/python-questions-answers-pickle-module/
[2]   https://docs.python-guide.org/scenarios/serialization/

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to open a file c:\scores.txt for writing?

``fileWriter = open("c:\\scores.txt", "w")``

## Q. What is TkInter?

TkInter is Python library. It is a toolkit for GUI development. It provides support for various GUI tools or widgets (such as buttons, labels, text boxes, radio buttons, etc) that are used in GUI applications. The common attributes of them include Dimensions, Colors, Fonts, Cursors, etc.

## Q. How to retrieve data from a table in MySQL database through Python code?

```py
#import MySQLdb module as : 
import MySQLdb

#establish a connection to the database.
db = MySQLdb.connect("host"="local host", "database-user"="user-name", "password"="password","database-name"="database")

#initialize the cursor variable upon the established connection: 
c1 = db.cursor()

#retrieve the information by defining a required query string.
s = "Select * from dept"

#fetch the data using fetch() methods and print it. 
data = c1.fetch(s)

#close the database connection. 
db.close()
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you generate a random number in Python?

This kind of Python interview Questions and Answers can Prove your depth of knowledge.

To generate a random number, we import the function random() from the module random.

     from random import random
     random()

`0.7931961644126482`

Let\'s call for help on this.

     help(random)

Help on built-in function random:

`random(…)` method of random.Random instance

`random() -> x` in the interval [0, 1).

This means that it will return a random number equal to or greater than 0, and less than 1.

We can also use the function randint(). It takes two arguments to indicate a range from which to return a random integer.
```
     from random import randint
     randint(2,7)
```
6
```
     randint(2,7)
```
5

     randint(2,7)

7

     randint(2,7)

6

     randint(2,7)

2

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. With Python, how do you find out which directory you are currently in?

To find this, we use the function/method getcwd(). We import it from the module os.

     import os
     os.getcwd()

'C:\\Users\\lifei\\AppData\\Local\\Programs\\Python\\Python36-32'

     type(os.getcwd)

<class 'builtin_function_or_method'>

We can also change the current working directory with chdir().

     os.chdir('C:\\Users\\lifei\\Desktop')
     os.getcwd()

'C:\\Users\\lifei\\Desktop'

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Tkinter?

Tkinter is a famous Python library with which you can craft a GUI. It provides support for different GUI tools and widgets like buttons, labels, text boxes, radio buttons, and more. These tools and widgets have attributes like dimensions, colors, fonts, colors, and more.

You can also import the tkinter module.

     import tkinter
     top=tkinter.Tk()

This will create a new window for you:

This creates a window with the title 'My Game'. You can position your widgets on this.

Follow this link to know more about Python Libraries

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you make a Python script executable on Unix?

Ans. For this to happen, two conditions must be met:

The script file\'s mode must be executable
The first line must begin with a hash(#). An  example of this will be: #!/usr/local/bin/python

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Differentiate between the append() and extend() methods of a list.

Ans. The methods append() and extend() work on lists. While append()adds an element to the end of the list, extend adds another list to the end of a list.

Let\'s take two lists.

    list1,list2=[1,2,3],[5,6,7,8]

This is how append() works:

    list1.append(4)
    list1

[1, 2, 3, 4]

And this is how extend() works:

    list1.extend(list2)
    list1

[1, 2, 3, 4, 5, 6, 7, 8]

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is JSON? Describe in brief how you\'d convert JSON data into Python data?

Ans. JSON stands for JavaScript Object Notation. It is a highly popular data format, and it stores data into NoSQL databases. JSON is generally built on the following two structures:

    A collection of <name,value> pairs
    An ordered list of values.

Python supports JSON parsers. In fact, JSON-based data is internally represented as a dictionary in Python. To convert JSON data into Python data, we use the load() function from the JSON module.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you execute a Python Script?

From the command line, type python .py or pythonx.y
.py where the x.y is the version of the Python interpreter desired.
Learn how to use Python, from beginner basics to advanced techniques, with online video tutorials taught by industry experts. Enroll for Free Python Training Demo!

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a namespace in Python?

In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched, to get corresponding object.

A namespace is a collection of names. It maps names to corresponding objects. When different namespaces contain objects with the same names, this avoids any name collisions. Internally, a namespace is implemented as a Python dictionary.

On starting the interpreter, it creates a namespace for as long as we don\'t exit. We have local namespaces, global namespaces, and a built-in namespace.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain the differences between local and global namespaces.

Local namespaces are created within a function. when that function is called. Global name spaces are created when the program starts.

## Q. Name the four main types of namespaces in Python?

Global, Local, Module and Class namespaces.

## Q. When would you use triple quotes as a delimiter?

Triple quotes ''"" or '" are string delimiters that can span multiple lines in Python. Triple quotes are usually used when spanning multiple lines, or enclosing a string that has a mix of single and double quotes contained therein.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to use GUI that comes with Python to test your code?

That is just an editor and a graphical version of the interactive shell. You write or load code and run it, or type it into the shell.
There is no automated testing.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do I make a Python script executable on UNIX?

You need to do two things:
The script file\'s mode must be executable and the first line must begin with "#!" followed by the path of the Python interpreter. 
- The first is done by executing chmod +x scriptfile or perhaps chmod 755 \'script' file.
- The second can be done in a number of ways.

The most straightforward way is to write:   
`#!/usr/local/bin/python`

as the very first line of your file, using the pathname for where the Python interpreter is installed on your platform. If you would like the script to be independent of where the Python interpreter lives, you can use the "env" program. Almost all UNIX variants support the following, assuming the python interpreter is in a directory on the users $PATH:

`#! /usr/bin/env python`

Don\'t do this for CGI scripts. The __$PATH__ variable for CGI scripts is often minimal, so you need to use the actual absolute pathname of the interpreter. Occasionally, a user\'s environment is so full that the /usr/bin/env program fails; or there\'s no env program at all. In that case, you can try the following hack (due to Alex Rezinsky):

```py
#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""
```
The minor disadvantage is that this defines the script\'s `__doc__`string. However, you can fix that by adding:  
`__doc__ = """…Whatever…"""`

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do I find undefined g++ symbols __builtin_new or __pure_virtual?

To dynamically load g++ extension modules, you must: 
Recompile Python
Re-link it using g++ (change LINKCC in the python Modules Makefile)
Link your extension module using g++ (e.g., "g++ -shared -o mymodule.so mymodule.o").

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do I send mail from a Python script?

Use the standard library module smtplib. Here\'s a very simple interactive mail sender that uses it. This method will work on any host that supports an SMTP listener.

```py
import sys, smtplib
fromaddr = raw_input("From: ")
toaddrs = raw_input("To: ").split(',')
print "Enter message, end with ^D:"
msg = "
while 1:
    line = sys.stdin.readline()
    if not line:
        break

msg = msg + line

# The actual mail send
server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
```
A UNIX-only alternative uses send mail. The location of the send mail program varies between systems; sometimes it is /usr/lib/sendmail, sometime /usr/sbin/sendmail. The send mail manual page will help you out. Here\'s some sample code:

```py
SENDMAIL = "/usr/sbin/sendmail" # sendmail location
import os
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write("To: receiver@example.comn")
p.write("Subject: testn")
p.write("n") # blank line separating headers from body
p.write("Some textn")
p.write("some more textn")
sts = p.close()
if sts != 0:
    print ("Sendmail exit status", sts)
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How can I mimic CGI form submission (METHOD=POST)? I would like to retrieve web pages that are the result of posting a form.

Yes. Here is a simple example that uses httplib:

```py
#!/usr/local/bin/python
import httplib, sys, time

### build the query string
qs = "First=Josephine&MI=Q&Last=Public"

### connect and send the server a path
httpobj = httplib.HTTP('www.some-server.out-there', 80)
httpobj.putrequest('POST', '/cgi-bin/some-cgi-script')

### now generate the rest of the HTTP headers…
httpobj.putheader('Accept', '*/*')
httpobj.putheader('Connection', 'Keep-Alive')
httpobj.putheader('Content-type', 'application/x-www-form-urlencoded')
httpobj.putheader('Content-length', '%d' % len(qs))
httpobj.endheaders()
httpobj.send(qs)

### find out what the server said in response…
reply, msg, hdrs = httpobj.getreply()
if reply != 200:
sys.stdout.write(httpobj.getfile().read())
```
Note that in general for URL-encoded POST operations, query strings must be quoted by using urllib.quote(). For example to send name="Guy Steele, Jr.":

```py
from urllib import quote
x = quote("Guy Steele, Jr.")
print(x)
'Guy%20Steele,%20Jr.'
 query_string = "name="+x
 query_string
'name=Guy%20Steele,%20Jr.'
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Executing DML Commands Through Python Programs?

DML (Data Modification Language) Commands are used to modify the data of the database objects
Whenever we execute DML Commands the records are going to be modified temporarily.

Whenever we run "rollback" command the modified records will come back to its original state.

To modify the records of the database objects permanently we use "commit" command

After executing the commit command even though we execute "rollback" command, the modified records will not come back to its original state.

Create the emp1 table in the database by using following command    
`Create table emp1 as select * from emp;`

Whenever we run the DML commands through the python program, then the no.of records which are modified because of that command will be stored into the rowcount attribute of cursor object.     
After executing the DML Command through the python program we have to call commit method of cursor object.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

### _Multithreading_

## Q. How Python is interpreted?

Python language is an interpreted language. Python program runs directly from the source code. It converts the source code that is written by the programmer into an intermediate language, which is again translated into machine language that has to be executed.

## Q. Explain how can you make a Python Script executable on Unix?

To make a Python Script executable on Unix, you need to do two things,

    Script file\'s mode must be executable and
    the first line must begin with # ( #!/usr/local/bin/python)

## Q. Explain how can you generate random numbers in Python?

To generate random numbers in Python, you need to import command as

```py
import random
random.random()
```

This returns a random floating point number in the range (0,1)

- Explain how can you access a module written in Python from C?

You can access a module written in Python from C by following method,

Module = =PyImport_ImportModule("<modulename>");

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Mention the use of the split function in Python?

The use of the split function in Python is that it breaks a string into shorter strings using the defined separator. It gives a list of all words present in the string.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Mention what is the difference between Django, Pyramid, and Flask?

Flask is a "microframework" primarily build for a small application with simpler requirements. In flask, you have to use external libraries. Flask is ready to use.

Pyramid are build for larger applications. It provides flexibility and lets the developer use the right tools for their project. The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.

Like Pyramid, Django can also used for larger applications. It includes an ORM.

- You are having multiple Memcache servers running Python, in which one of the memcacher server fails, and it has your data, will it ever try to get key data from that one failed server?

The data in the failed server won\'t get removed, but there is a provision for auto-failure, which you can configure for multiple nodes. Fail-over can be triggered during any kind of socket or Memcached server level errors and not during normal client errors like adding an existing key, etc.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain how you can minimize the Memcached server outages in your Python Development?

- When one instance fails, several of them goes down, this will put larger load on the database server when lost data is reloaded as client make a request. To avoid this, if your code has been written to minimize cache stampedes then it will leave a minimal impact
- Another way is to bring up an instance of Memcached on a new machine using the lost machines IP address
- Code is another option to minimize server outages as it gives you the liberty to change the Memcached server list with minimal work
-  Setting timeout value is another option that some Memcached clients implement for Memcached server outage. When your Memcached server goes down, the client will keep trying to send a request till the time-out limit is reached

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain what is Dogpile effect? How can you prevent this effect?

Dogpile effect is referred to the event when cache expires, and websites are hit by the multiple requests made by the client at the same time.  
This effect can be prevented by using semaphore lock. In this system when value expires, first process acquires the lock and starts generating new value.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain how Memcached should not be used in your Python project?

Memcached common misuse is to use it as a data store, and not as a cache. Never use Memcached as the only source of the information you need to run your application. Data should always be available through another source as well. Memcached is just a key or value store and cannot perform query over the data or iterate over the contents to extract information.

Memcached does not offer any form of security either in encryption or authentication

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is Flask & its benefits?

Python Flask, as we've previously discussed, is a web microframework for Python. It is based on the '`Werkzeug`, `Jinja 2` and good intentions' BSD license. Two of its dependencies are Werkzeug and Jinja2. This means that it has around no dependencies on external libraries. Due to this, we can call it a light framework. A session uses a signed cookie to allow the user to look at and modify session contents. It will remember information from one request to another. However, to modify a session, the user must have the secret key `Flask.secret_key`.

Flask is a web micro framework for Python based on "Werkzeug, Jinja 2 and good intentions" BSD licensed. Werkzeug and jingja are two of its dependencies.

Flask is part of the micro-framework. Which means it will have little to no dependencies on external libraries. It makes the framework light while there is little dependency to update and less security bugs.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Mention what is Flask-WTF and what are their features?

Flask-WTF offers simple integration with WTForms. Features include for Flask WTF are
   >
    Integration with wtforms
    Secure form with csrf token
    Global csrf protection
    Internationalization integration
    Recaptcha supporting
    File upload that works with Flask Uploads

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain what is the common way for the Flask script to work?

The common way for the flask script to work is

    Either it should be the import path for your application
    Or the path to a Python file

## Q. Explain how you can access sessions in Flask?

A session basically allows you to remember information from one request to another. In a flask, it uses a signed cookie so the user can look at the session contents and modify. The user can modify the session if only it has the secret key Flask.secret_key.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Is Flask an MVC model and if yes give an example showing MVC pattern for your application?

Basically, Flask is a minimalistic framework which behaves same as MVC framework. So MVC is a perfect fit for Flask, and the pattern for MVC we will consider for the following example

from flask import Flask
app = Flask(_name_)
@app.route("/")
def hello():
    return "Hello World"
app.run(debug = True)
	
In this code your,

Configuration part will be

    from flask import Flask
    app = Flask(_name_)

View part will be

    @app.route("/")
    def hello():
        return "Hello World"

While your model or main part will be

    app.run(debug = True)

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain database connection in Python Flask?

Best database for flask is MySQL. Flask supports database powered application (RDBS). Such system requires creating a schema, which requires piping the shema.sql file into a sqlite3 command. So you need to install `sqlite3` command in order to create or initiate the database in Flask. Flask allows to request database in three ways

   - `before_request()`: They are called before a request and pass no arguments.     
   - `after_request()`: They are called after a request and pass the response that will be sent to the client.   
   - `teardown_request()`: They are called in situation when exception is raised, and response are not guaranteed. They are called after the response been constructed. They are not allowed to modify the request, and their values are ignored.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## How will you sort result of student whose marks are unknown to you based on their roll numbers? 

Using bubble sort.

## Q. What are the standard Python libraries commonly used?

| Category | Libraries |
|----------|-----------|
| OS & File System | `os`, `sys`, `pathlib`, `shutil`, `glob` |
| Data Structures | `collections`, `heapq`, `bisect`, `array` |
| Functional | `functools`, `itertools`, `operator` |
| Serialization | `json`, `pickle`, `csv`, `xml`, `configparser` |
| Networking | `socket`, `http`, `urllib`, `ftplib`, `smtplib` |
| Concurrency | `threading`, `multiprocessing`, `asyncio`, `concurrent.futures` |
| Date & Time | `datetime`, `time`, `calendar`, `zoneinfo` |
| Logging | `logging` |
| Testing | `unittest`, `unittest.mock`, `doctest` |
| Regex | `re` |
| Math | `math`, `statistics`, `decimal`, `fractions`, `random` |

```py
from collections import defaultdict, Counter
from itertools import groupby
from functools import lru_cache
import pathlib, logging, json

# defaultdict — avoids KeyError on missing keys
word_groups: defaultdict[str, list[str]] = defaultdict(list)
for word in ["apple", "ant", "ball", "banana"]:
    word_groups[word[0]].append(word)
print(dict(word_groups))  # {'a': ['apple', 'ant'], 'b': ['ball', 'banana']}

# lru_cache — memoization for expensive pure functions
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
```

**Use Case:** A data engineering team uses `collections.defaultdict` + `itertools.groupby` to aggregate streaming event logs by user session without third-party dependencies, keeping the Lambda function package under 10 MB.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are serialization formats in Python?

Serialization converts a Python object into a byte stream or string for storage or transmission. Deserialization reverses this.

| Format | Module | Human-readable | Cross-language | Speed |
|--------|--------|---------------|---------------|-------|
| JSON | `json` | Yes | Yes | Fast |
| Pickle | `pickle` | No | Python only | Fast |
| CSV | `csv` | Yes | Yes | Medium |
| XML | `xml`, `lxml` | Yes | Yes | Slow |
| MessagePack | `msgpack` | No | Yes | Very fast |
| Protocol Buffers | `protobuf` | No | Yes | Very fast |
| YAML | `yaml` (PyYAML) | Yes | Yes | Slow |

```py
import json
import pickle
import csv
from io import StringIO

# JSON — best for APIs and config files
data = {"user": "alice", "score": 98, "tags": ["python", "backend"]}
json_str = json.dumps(data, indent=2)
restored = json.loads(json_str)
print(restored["user"])  # alice

# Pickle — Python-native, supports any object (NEVER unpickle untrusted data)
with open("model.pkl", "wb") as f:
    pickle.dump(data, f)
with open("model.pkl", "rb") as f:
    loaded = pickle.load(f)

# CSV — for tabular data
output = StringIO()
writer = csv.DictWriter(output, fieldnames=["user", "score"])
writer.writeheader()
writer.writerow({"user": "alice", "score": 98})
print(output.getvalue())
```

> **Security Warning:** Never use `pickle.load()` on data from untrusted sources — it can execute arbitrary code during deserialization.

**Use Case:** A machine learning platform serializes trained `scikit-learn` models with `pickle` for internal storage, but exposes model metadata via JSON for the REST API, keeping concerns separated by format suitability.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What version of Azure Data Factory are you using?

Azure Data Factory (ADF) **V2** is the current and only actively supported version (V1 reached end-of-support in 2018). ADF V2 key capabilities include:

- **Data Flows** (Mapping & Wrangling) — visual ETL with Spark-based execution
- **Triggers** — Schedule, Tumbling Window, Storage Event, Custom Event
- **Integration Runtimes** — Azure IR, Self-Hosted IR, SSIS IR
- **ARM/Bicep templates** for CI/CD deployments
- **Git integration** — Azure DevOps or GitHub for source control
- **Managed Virtual Network** — private endpoint connectivity

```py
# Interacting with ADF V2 via Python SDK (azure-mgmt-datafactory)
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import CreateRunResponse

subscription_id = "your-subscription-id"
resource_group = "my-rg"
factory_name = "my-adf"
pipeline_name = "IngestPipeline"

credential = DefaultAzureCredential()
adf_client = DataFactoryManagementClient(credential, subscription_id)

# Trigger a pipeline run programmatically
run_response: CreateRunResponse = adf_client.pipelines.create_run(
    resource_group_name=resource_group,
    factory_name=factory_name,
    pipeline_name=pipeline_name,
    parameters={"source_date": "2026-05-17"},
)
print(f"Pipeline run ID: {run_response.run_id}")

# Poll run status
import time
while True:
    run = adf_client.pipeline_runs.get(resource_group, factory_name, run_response.run_id)
    print(f"Status: {run.status}")
    if run.status in ("Succeeded", "Failed", "Cancelled"):
        break
    time.sleep(15)
```

**Use Case:** A data platform team uses ADF V2 with Self-Hosted IR to move data from on-premises SQL Server to Azure Data Lake Gen2, triggered by Azure Event Grid file-arrival events, with Python SDK used in CI/CD pipelines to deploy and monitor ADF runs automatically.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to execute Java code from Python?

```py
import subprocess
import os
from pathlib import Path

def compile_and_run_java(java_file: Path, *args: str) -> tuple[str, str, int]:
    """
    Compile and run a Java source file, returning (stdout, stderr, return_code).
    Requires JDK installed and `javac`/`java` on PATH.
    """
    class_dir = java_file.parent

    # Step 1: Compile
    compile_result = subprocess.run(
        ["javac", "-d", str(class_dir), str(java_file)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if compile_result.returncode != 0:
        return "", compile_result.stderr, compile_result.returncode

    # Step 2: Run — derive class name from filename (Java convention)
    class_name = java_file.stem
    run_result = subprocess.run(
        ["java", "-cp", str(class_dir), class_name, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )
    return run_result.stdout, run_result.stderr, run_result.returncode


# Example usage
java_source = Path("/tmp/Hello.java")
java_source.write_text(
    'public class Hello {\n'
    '    public static void main(String[] args) {\n'
    '        System.out.println("Hello from Java: " + args[0]);\n'
    '    }\n'
    '}\n'
)

stdout, stderr, code = compile_and_run_java(java_source, "PythonCaller")
print(f"Output: {stdout.strip()}")   # Hello from Java: PythonCaller
print(f"Return code: {code}")        # 0
```

> **Security Note:** Never pass user-provided strings directly to `subprocess` commands — use argument lists (not `shell=True`) to prevent shell injection.

**Use Case:** A polyglot CI/CD pipeline uses Python as the orchestration layer to compile, test, and execute Java microservices during integration testing, capturing their stdout/stderr for structured test reporting.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to find PID of a process and how much resources it is taking on Linux?

```py
import os
import psutil  # pip install psutil
from typing import Iterator

# Method 1: Find PID of current process
current_pid: int = os.getpid()
print(f"Current PID: {current_pid}")

# Method 2: Find PID(s) by process name using psutil
def find_pids_by_name(process_name: str) -> list[int]:
    """Return all PIDs whose name matches the given string."""
    return [
        proc.pid
        for proc in psutil.process_iter(["pid", "name"])
        if process_name.lower() in proc.info["name"].lower()
    ]

pids = find_pids_by_name("python")
print(f"Python PIDs: {pids}")

# Method 3: Detailed resource usage for a specific PID
def get_process_resources(pid: int) -> dict:
    """Return CPU%, memory, open files, threads for a given PID."""
    try:
        proc = psutil.Process(pid)
        proc.cpu_percent(interval=None)   # prime the counter
        import time; time.sleep(0.1)

        mem_info = proc.memory_info()
        return {
            "pid": pid,
            "name": proc.name(),
            "status": proc.status(),
            "cpu_percent": proc.cpu_percent(interval=0.1),
            "memory_rss_mb": mem_info.rss / (1024 ** 2),
            "memory_vms_mb": mem_info.vms / (1024 ** 2),
            "memory_percent": proc.memory_percent(),
            "num_threads": proc.num_threads(),
            "open_files": len(proc.open_files()),
            "connections": len(proc.net_connections()),
        }
    except psutil.NoSuchProcess:
        return {}

stats = get_process_resources(current_pid)
for key, value in stats.items():
    print(f"  {key}: {value}")

# Method 4: Top N processes by memory consumption
def top_processes_by_memory(n: int = 5) -> list[dict]:
    procs = [
        proc.as_dict(attrs=["pid", "name", "memory_percent", "cpu_percent"])
        for proc in psutil.process_iter(["pid", "name", "memory_percent", "cpu_percent"])
        if proc.info["memory_percent"] is not None
    ]
    return sorted(procs, key=lambda p: p["memory_percent"], reverse=True)[:n]

print(top_processes_by_memory())
```

**Linux CLI equivalents:** `ps aux | grep <name>`, `top -p <pid>`, `cat /proc/<pid>/status`, `/proc/<pid>/smaps`

**Use Case:** A production monitoring agent runs as a sidecar container, using `psutil` to emit process-level CPU and RSS memory metrics to Prometheus every 15 seconds, alerting when any single process exceeds 80% of available memory.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are tools for data ingestion?

Data ingestion tools move data from sources into storage/processing systems. They fall into several categories:

| Category | Tools | Best For |
|----------|-------|----------|
| **Message Queues / Streaming** | Apache Kafka, AWS Kinesis, Azure Event Hubs, Google Pub/Sub | Real-time event streams |
| **Batch ETL / Pipeline** | Apache Airflow, Azure Data Factory, AWS Glue, dbt | Scheduled batch ingestion |
| **Log / Event Collection** | Logstash (ELK), Fluentd, Filebeat, Vector | Log aggregation |
| **Change Data Capture (CDC)** | Debezium, AWS DMS, Striim | DB replication / CDC |
| **File Transfer** | Apache NiFi, Airbyte, Fivetran | File-based & API connectors |
| **Python Libraries** | `kafka-python`, `boto3`, `azure-eventhub`, `apache-beam` | Custom pipelines |

```py
# Example: Producing messages to Apache Kafka using kafka-python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    acks="all",           # strongest durability guarantee
    retries=3,
    max_in_flight_requests_per_connection=1,  # ensure ordering
)

event = {"user_id": "u123", "action": "purchase", "amount": 49.99}
future = producer.send("user-events", value=event, key=b"u123")
record_metadata = future.get(timeout=10)
print(f"Sent to {record_metadata.topic}:{record_metadata.partition} @ {record_metadata.offset}")
producer.flush()
producer.close()
```

**Use Case:** A ride-sharing platform ingests 2M GPS location updates per minute using Apache Kafka as the ingestion backbone, with Kafka Streams for real-time ETA computation and a Spark Structured Streaming job writing aggregated trip data to Delta Lake every 30 seconds.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is inheritance?

Inheritance is an OOP mechanism where a **child class** acquires the attributes and methods of one or more **parent classes**, enabling code reuse, specialization, and the Liskov Substitution Principle. Python supports single, multiple, and multilevel inheritance.

```py
from abc import ABC, abstractmethod
from typing import ClassVar

# Base class (abstract)
class Animal(ABC):
    species_count: ClassVar[int] = 0

    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self._sound = sound
        Animal.species_count += 1

    @abstractmethod
    def speak(self) -> str:
        ...

    def describe(self) -> str:
        return f"I am {self.name}"

# Single inheritance
class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name, "woof")   # call parent __init__
        self.breed = breed

    def speak(self) -> str:             # implement abstract method
        return f"{self.name} says {self._sound}!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}"

# Multilevel inheritance
class GuideDog(Dog):
    def guide(self) -> str:
        return f"{self.name} guides its owner safely"

d = Dog("Rex", "Labrador")
print(d.speak())        # Rex says woof!
print(d.describe())     # I am Rex (inherited from Animal)

g = GuideDog("Buddy", "Golden Retriever")
print(g.guide())        # Buddy guides its owner safely
print(g.fetch("ball"))  # Buddy fetches the ball (inherited from Dog)

# isinstance checks hierarchy
print(isinstance(g, GuideDog))  # True
print(isinstance(g, Dog))       # True
print(isinstance(g, Animal))    # True
```

**Use Case:** A payment processing system uses an abstract `PaymentProcessor` base class enforcing a `process(amount)` interface. Concrete subclasses `StripeProcessor`, `PayPalProcessor`, and `BankTransferProcessor` implement it differently — new providers are added without modifying existing code (Open/Closed Principle).

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Differentiate between `append()` and `extend()` methods of a list.

| Method | Action | Argument | Time | Result on `[1,2]` |
|--------|--------|----------|------|-------------------|
| `append(x)` | Adds `x` as a **single element** | Any object | O(1) amortized | `[1, 2, [3, 4]]` if x=`[3,4]` |
| `extend(iterable)` | Adds **each element** of iterable | Any iterable | O(k) where k=len(iterable) | `[1, 2, 3, 4]` if x=`[3,4]` |

```py
# append — adds the argument as ONE new element
lst1 = [1, 2, 3]
lst1.append([4, 5])     # the list [4, 5] becomes a single element
print(lst1)             # [1, 2, 3, [4, 5]]
print(len(lst1))        # 4

# extend — unpacks iterable and adds each element
lst2 = [1, 2, 3]
lst2.extend([4, 5])     # 4 and 5 added as separate elements
print(lst2)             # [1, 2, 3, 4, 5]
print(len(lst2))        # 5

# extend works with any iterable
lst3 = [1, 2]
lst3.extend("abc")      # extends with individual characters
print(lst3)             # [1, 2, 'a', 'b', 'c']

lst3.extend(range(3))
print(lst3)             # [1, 2, 'a', 'b', 'c', 0, 1, 2]

# += operator uses extend semantics, not append
lst4 = [1, 2]
lst4 += [3, 4]          # equivalent to lst4.extend([3, 4])
print(lst4)             # [1, 2, 3, 4]

# Performance: extend is more efficient than repeated append in a loop
import timeit
t1 = timeit.timeit("lst=[]; [lst.append(i) for i in range(1000)]", number=10000)
t2 = timeit.timeit("lst=[]; lst.extend(range(1000))", number=10000)
print(f"append loop: {t1:.3f}s  extend: {t2:.3f}s")  # extend ~3x faster
```

**Use Case:** A web scraper collects page results in batches; `extend()` merges each batch into the master results list efficiently, while `append()` would wrap each batch in a nested list, requiring flattening later.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Explain `ctypes` and why you would use them?

`ctypes` is Python\'s built-in **foreign function interface (FFI)** library. It allows Python to call functions in compiled C shared libraries (`.so` on Linux, `.dll` on Windows, `.dylib` on macOS), pass C data types, and access C memory directly — without writing a C extension module.

**When to use:**
- Call existing C/C++ libraries that have no Python wrapper
- Access OS-level APIs
- Achieve near-C performance for CPU-intensive routines
- Interface with hardware drivers or system calls

```py
import ctypes
import ctypes.util
import sys

# Load the C standard library
if sys.platform == "win32":
    libc = ctypes.CDLL("msvcrt.dll")
else:
    libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Call C's printf
libc.printf(b"Hello from C: %d\n", ctypes.c_int(42))

# Define argument and return types for type safety
libc.strlen.argtypes = [ctypes.c_char_p]
libc.strlen.restype  = ctypes.c_size_t
print(libc.strlen(b"hello"))   # 5

# Define a C struct
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

p = Point(3.0, 4.0)
print(f"Point({p.x}, {p.y})")

# Load a custom shared library (example)
# lib = ctypes.CDLL("./my_fast_lib.so")
# lib.fast_sum.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
# lib.fast_sum.restype = ctypes.c_double
# arr = (ctypes.c_double * 5)(1.0, 2.0, 3.0, 4.0, 5.0)
# print(lib.fast_sum(arr, 5))   # 15.0

# Access raw memory (advanced)
buf = ctypes.create_string_buffer(10)
buf.value = b"Hello"
print(buf.raw)   # b'Hello\x00\x00\x00\x00\x00'
```

> **Security Note:** `ctypes` bypasses Python\'s memory safety — incorrect pointer arithmetic or type mismatches can cause segfaults or memory corruption. Always specify `argtypes` and `restype`.

**Use Case:** A real-time image processing service calls a highly optimized C++ computer vision library via `ctypes` to apply SIMD-accelerated filters on video frames, achieving 200 FPS — impossible with pure Python.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How do you go about packaging Python code?

Python packaging means bundling code so others can install it via `pip`. The modern standard uses **`pyproject.toml`** (PEP 517/518/621) with a build backend such as `hatchling`, `setuptools`, or `flit`.

```
my_package/
├── pyproject.toml          # build metadata & dependencies
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
└── README.md
```

```toml
# pyproject.toml
[build-system]
requires      = ["hatchling"]
build-backend = "hatchling.build"

[project]
name    = "my-package"
version = "1.0.0"
description = "Example package"
readme  = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev  = ["pytest", "mypy", "ruff"]

[project.scripts]
my-cli = "my_package.cli:main"   # console entry point
```

```py
# src/my_package/__init__.py
from .core import greet
__version__ = "1.0.0"
__all__ = ["greet"]

# src/my_package/core.py
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

```bash
# Build distribution files
pip install build
python -m build          # creates dist/my_package-1.0.0.tar.gz + .whl

# Publish to PyPI
pip install twine
twine upload dist/*

# Install locally (editable mode for development)
pip install -e ".[dev]"
```

**Key files:**
- `pyproject.toml` — replaces `setup.py` / `setup.cfg`
- `src/` layout — prevents accidental imports of uninstalled code during tests
- `.whl` (wheel) — binary distribution, faster to install than sdist

**Use Case:** A data science team packages shared feature engineering utilities as an internal PyPI package, enabling all microservices to `pip install internal-features==2.3.1` with pinned versions — eliminating copy-paste drift between 12 separate repos.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What does `__some_variable__` (dunder / magic attribute) mean?

Names surrounded by double underscores (`__name__`) are called **dunder** (double-underscore) names or **magic attributes/methods**. Python reserves this naming convention for the interpreter\'s own protocol methods and special attributes. You should never invent your own `__custom__` names — that namespace belongs to Python.

```py
# Dunder methods define how objects respond to built-in operations
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:               # repr(v)
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:                # str(v) / print(v)
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":  # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self) -> int:                # len(v)
        return 2

    def __eq__(self, other: object) -> bool: # v1 == v2
        if not isinstance(other, Vector): return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:               # hash(v), use in sets/dicts
        return hash((self.x, self.y))

    def __bool__(self) -> bool:              # bool(v), if v:
        return self.x != 0 or self.y != 0

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # (4, 6)  — calls __add__
print(len(v1))    # 2       — calls __len__
print(repr(v1))   # Vector(1, 2) — calls __repr__

# Common special attributes
print(__name__)             # '__main__' when run directly, else module name
print(Vector.__doc__)       # class docstring
print(Vector.__dict__)      # namespace dict of the class
print(v1.__class__.__name__) # 'Vector'
```

**Common dunders:**

| Dunder | Triggered by |
|--------|-------------|
| `__init__` | `ClassName()` |
| `__str__` | `str()`, `print()` |
| `__repr__` | `repr()`, REPL display |
| `__len__` | `len()` |
| `__iter__` / `__next__` | `for` loops |
| `__enter__` / `__exit__` | `with` statement |
| `__getitem__` | `obj[key]` |
| `__call__` | `obj()` |

**Use Case:** A DataFrame-like class overrides `__getitem__`, `__setitem__`, `__len__`, and `__iter__` to give users a familiar `df["column"]` and `for row in df:` interface, with custom memory-mapped storage underneath.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the difference between `str()` and `repr()`?

| | `str()` | `repr()` |
|--|---------|---------|
| **Purpose** | Human-readable, display | Unambiguous, developer/debug |
| **Ideal reader** | End users | Developers |
| **Goal** | Pretty / concise | Reproducible (`eval(repr(x)) == x` when possible) |
| **Fallback** | Falls back to `__repr__` | No fallback |
| **Used by** | `print()`, f-strings `{x}` | REPL, `!r` format, `logging` |

```py
from datetime import datetime

dt = datetime(2025, 6, 15, 12, 30)
print(str(dt))    # 2025-06-15 12:30:00      — readable
print(repr(dt))   # datetime.datetime(2025, 6, 15, 12, 30) — reproducible

# Custom class: implement both
class Money:
    def __init__(self, amount: float, currency: str = "GBP") -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:,.2f}"   # user-facing

    def __repr__(self) -> str:
        return f"Money({self.amount!r}, {self.currency!r})"  # debug

m = Money(1234.5)
print(str(m))    # GBP 1,234.50
print(repr(m))   # Money(1234.5, 'GBP')

# f-string format specifiers
print(f"{m}")    # GBP 1,234.50    — uses __str__
print(f"{m!r}")  # Money(1234.5, 'GBP') — uses __repr__
print(f"{m!s}")  # GBP 1,234.50    — explicitly __str__

# Why repr matters for strings (shows quotes, escapes)
s = "hello\nworld"
print(str(s))    # hello\nworld  (newline rendered)
print(repr(s))   # 'hello\\nworld'  (escape shown — unambiguous)
```

**Use Case:** A logging framework uses `repr()` to record all variable values in exception tracebacks — `Money(1234.5, 'GBP')` in the log is immediately copy-pasteable to a Python REPL for debugging, whereas `GBP 1,234.50` is ambiguous and unrepresentable.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are Middlewares?

**Middleware** is code that sits between the incoming request and the application handler (or between the response and the client), forming a processing pipeline. Each middleware wraps the next, processing the request on the way in and the response on the way out.

In Python web frameworks:
- **Django:** `MIDDLEWARE` list in settings — each class implements `__call__`
- **FastAPI / Starlette:** `@app.middleware("http")` or `add_middleware()`
- **WSGI:** Callables that wrap a WSGI app

```py
# WSGI-style middleware (framework-agnostic)
from typing import Callable
import time

# Type aliases for WSGI
Environ = dict
StartResponse = Callable
WSGIApp = Callable[[Environ, StartResponse], list[bytes]]

class TimingMiddleware:
    def __init__(self, app: WSGIApp) -> None:
        self.app = app

    def __call__(self, environ: Environ, start_response: StartResponse):
        start = time.perf_counter()
        result = self.app(environ, start_response)
        duration = time.perf_counter() - start
        print(f"Request took {duration * 1000:.2f}ms")
        return result

# FastAPI / Starlette middleware
from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.middleware("http")
async def add_correlation_id(request: Request, call_next) -> Response:
    import uuid
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    response = await call_next(request)      # pass to next middleware / handler
    response.headers["X-Correlation-ID"] = correlation_id
    return response

@app.middleware("http")
async def log_requests(request: Request, call_next) -> Response:
    print(f"→ {request.method} {request.url.path}")
    response = await call_next(request)
    print(f"← {response.status_code}")
    return response

# Middleware chain: log_requests → add_correlation_id → route handler
```

**Common middleware responsibilities:**
- Authentication / authorization
- Request logging and tracing
- Rate limiting
- CORS headers
- Response compression
- Request body validation

**Use Case:** A microservice uses three middleware layers: `AuthMiddleware` (validates JWT), `RateLimitMiddleware` (100 req/min per user), and `TracingMiddleware` (injects OpenTelemetry spans) — all added to the pipeline in `main.py` without touching any route handler.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to generate random numbers?

```py
import random
import secrets
import numpy as np

# ── random module (PRNG — Mersenne Twister, NOT cryptographically secure) ──

# Integer in [a, b] inclusive
print(random.randint(1, 10))

# Float in [0.0, 1.0)
print(random.random())

# Float in [a, b)
print(random.uniform(1.5, 9.5))

# Random choice from a sequence
colours = ["red", "green", "blue"]
print(random.choice(colours))

# Multiple choices (with replacement)
print(random.choices(colours, weights=[1, 2, 3], k=5))

# Sample without replacement
deck = list(range(1, 53))
hand = random.sample(deck, k=5)

# Shuffle in-place
random.shuffle(deck)

# Reproducible results — set seed
random.seed(42)
print([random.randint(1, 100) for _ in range(5)])
# [1, 82, 15, 4, 95] — always the same with seed=42

# Gaussian distribution
print(random.gauss(mu=0, sigma=1))

# ── secrets module (CSPRNG — cryptographically secure) ──
print(secrets.randbelow(100))        # int in [0, 100)
print(secrets.randbits(16))          # random 16-bit integer
token = secrets.token_hex(32)        # 64-char hex string (256-bit)
url_token = secrets.token_urlsafe(16)# URL-safe base64 token
print(token)

# ── numpy random (vectorized, reproducible with Generator) ──
rng = np.random.default_rng(seed=42)  # modern API (replaces np.random.*)
print(rng.integers(1, 100, size=5))   # array of 5 random ints
print(rng.standard_normal(size=(3, 3)))  # 3×3 matrix of N(0,1)
```

> **Security note:** Always use `secrets` for tokens, passwords, OTPs, and anything security-sensitive. `random` is predictable if the seed is known.

**Use Case:** An A/B testing service uses `random.seed(user_id)` to deterministically assign users to experiment groups (same user always gets same variant), while `secrets.token_urlsafe(32)` generates the secure session tokens for those same users.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is `virtualenv`?

A **virtual environment** is an isolated Python environment with its own interpreter, `pip`, and installed packages — completely separate from the system Python. This prevents dependency conflicts between projects.

Python 3.3+ includes `venv` (stdlib); `virtualenv` is a faster third-party alternative with more features.

```bash
# Create a virtual environment (stdlib venv)
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Your prompt changes: (.venv) $

# Install packages — isolated to this environment
pip install fastapi uvicorn pandas

# Freeze dependencies
pip freeze > requirements.txt

# Deactivate
deactivate

# Delete — just remove the folder
rm -rf .venv
```

```py
# Verify you're in a virtual environment
import sys
print(sys.prefix)          # /path/to/.venv
print(sys.base_prefix)     # /usr/local/python3.x  (system Python)
print(sys.prefix == sys.base_prefix)  # False — we're in a venv

# Modern alternative: pyenv + virtualenv managed by pyenv-virtualenv
# Even more modern: uv (extremely fast resolver, drop-in pip replacement)
# uv venv && uv pip install fastapi
```

**Directory structure:**
```
.venv/
├── bin/          # python, pip executables (Scripts/ on Windows)
├── lib/
│   └── python3.x/
│       └── site-packages/   # installed packages live here
└── pyvenv.cfg   # records base Python version
```

**Best practices:**
- Never commit `.venv/` to version control (add to `.gitignore`)
- Commit `requirements.txt` or `pyproject.toml` instead
- Use `requirements.txt` for applications; `pyproject.toml` for libraries

**Use Case:** A CI/CD pipeline creates a fresh `.venv` on every build run, installs pinned `requirements.txt`, and runs tests — guaranteeing reproducible, conflict-free builds regardless of what else is installed on the build agent.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is a context processor?

In **Django**, a context processor is a function that receives an `HttpRequest` and returns a `dict` of variables that are **automatically injected into every template context**. They are configured in `settings.py` under `TEMPLATES[...]['OPTIONS']['context_processors']`.

```py
# myapp/context_processors.py

from django.http import HttpRequest

def site_settings(request: HttpRequest) -> dict:
    """Injects site-wide settings into every template."""
    return {
        "SITE_NAME": "MyApp",
        "SUPPORT_EMAIL": "support@myapp.io",
        "MAINTENANCE_MODE": False,
    }

def user_notifications(request: HttpRequest) -> dict:
    """Injects unread notification count for authenticated users."""
    if not request.user.is_authenticated:
        return {"unread_count": 0}
    # Import here to avoid circular imports
    from notifications.models import Notification
    count = Notification.objects.filter(
        user=request.user, read=False
    ).count()
    return {"unread_count": count}
```

```python
# settings.py — register the context processors
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "myapp.context_processors.site_settings",     # custom
            "myapp.context_processors.user_notifications", # custom
        ],
    },
}]
```

```html
<!-- base.html — variables available in ALL templates automatically -->
<title>{{ SITE_NAME }}</title>
<span>{{ unread_count }} notifications</span>
```

> **Outside Django:** The term "context processor" generally means middleware or a request hook that enriches a context/request object with shared data before handlers execute.

**Use Case:** An enterprise Django portal uses a context processor to inject the current user\'s `active_tenant`, `feature_flags`, and `branding_config` into every template render — eliminating repetitive `context.update(...)` calls across 200+ views.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are `exec()` and `eval()`?

Both execute dynamically-generated Python code. `eval()` evaluates a **single expression** and returns its value. `exec()` executes **statements** (full code blocks) and returns `None`.

```py
# eval — single expression, returns value
result = eval("2 ** 10 + 5")
print(result)   # 1029

# eval with custom namespace (safer — restrict accessible names)
safe_globals = {"__builtins__": {}}   # no built-ins
safe_locals  = {"x": 10, "y": 20}
print(eval("x + y", safe_globals, safe_locals))   # 30
# eval("open('file')", safe_globals, safe_locals)  # NameError — open not available

# exec — execute statements, returns None
code = """
def multiply(a, b):
    return a * b

result = multiply(6, 7)
"""
namespace: dict = {}
exec(code, namespace)
print(namespace["result"])        # 42
print(namespace["multiply"](3, 4))  # 12

# compile() + exec — for repeated execution (compile once)
compiled = compile("x * x", "<string>", "eval")
for x in range(5):
    print(eval(compiled, {"x": x}))   # 0, 1, 4, 9, 16
```

> ⚠️ **Security warning:** NEVER pass untrusted user input to `eval()` or `exec()`. Even with `__builtins__: {}` restrictions can be bypassed. Use `ast.literal_eval()` for safe evaluation of literal expressions from untrusted sources.

```py
import ast

# SAFE — only evaluates Python literals (str, int, float, list, dict, tuple, bool, None)
user_input = "[1, 2, 3, {'key': 'value'}]"
safe_data = ast.literal_eval(user_input)
print(safe_data)   # [1, 2, 3, {'key': 'value'}]

# ast.literal_eval raises ValueError for non-literals
# ast.literal_eval("__import__('os').system('rm -rf /')")  # ValueError
```

**Use Case:** A rule engine uses `exec()` to dynamically compile and cache user-defined business rule scripts at startup (compile-once), then `eval()` with a restricted namespace to evaluate them against transaction records — achieving configurable logic without code deployment.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How to pass command-line arguments?

Python provides three standard ways: `sys.argv` (raw), `argparse` (stdlib, recommended), and `click`/`typer` (third-party, decorator-based).

```py
#!/usr/bin/env python3
# cli_example.py

import argparse
import sys

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Process a data file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Positional argument — required
    parser.add_argument("input_file", help="Path to input CSV")

    # Optional flag with value
    parser.add_argument(
        "--output", "-o",
        default="output.csv",
        help="Path to output file",
    )

    # Integer option with validation
    parser.add_argument(
        "--batch-size",
        type=int,
        default=1000,
        metavar="N",
        help="Records per batch",
    )

    # Boolean flag
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    # Enum-like choices
    parser.add_argument(
        "--format",
        choices=["csv", "json", "parquet"],
        default="csv",
    )

    args = parser.parse_args()

    if args.verbose:
        print(f"Processing {args.input_file}")
        print(f"Output: {args.output}")
        print(f"Batch size: {args.batch_size}")
        print(f"Format: {args.format}")

if __name__ == "__main__":
    main()
```

```bash
# Usage
python cli_example.py data.csv --output results.csv --batch-size 500 --verbose --format json
python cli_example.py --help   # auto-generated help text

# sys.argv — raw access (not recommended for production CLIs)
# python script.py arg1 arg2
# sys.argv = ['script.py', 'arg1', 'arg2']
```

```py
# Typer — modern, type-hint-driven CLI (third-party)
import typer

app = typer.Typer()

@app.command()
def process(
    input_file: str,
    output: str = "output.csv",
    batch_size: int = 1000,
    verbose: bool = False,
) -> None:
    if verbose:
        typer.echo(f"Processing {input_file}")

if __name__ == "__main__":
    app()
```

**Use Case:** A data engineering CLI tool uses `argparse` with `--env`, `--dry-run`, and `--config` flags, enabling both interactive use and automated invocation in Airflow BashOperator tasks with deterministic, documentable options.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What are `ord()` and `chr()`?

`ord(char)` returns the **Unicode code point** (integer) of a single character. `chr(code_point)` is the inverse — it returns the **character** for a given code point. Together they enable character-level arithmetic.

```py
# ord — character to code point
print(ord("A"))    # 65
print(ord("a"))    # 97
print(ord("0"))    # 48
print(ord("€"))    # 8364
print(ord("🐍"))   # 128013

# chr — code point to character
print(chr(65))     # 'A'
print(chr(97))     # 'a'
print(chr(8364))   # '€'

# Character arithmetic
print(chr(ord("A") + 1))   # 'B'
print(chr(ord("a") + 25))  # 'z'

# Caesar cipher using ord/chr
def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shifted = (ord(ch) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(ch)
    return "".join(result)

print(caesar_cipher("Hello, World!", 13))  # Uryyb, Jbeyq! (ROT13)
print(caesar_cipher("Uryyb, Jbeyq!", 13))  # Hello, World!

# Alphabet generation
alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
print(alphabet[:5])   # ['a', 'b', 'c', 'd', 'e']

# Check character ranges efficiently
def is_ascii_printable(ch: str) -> bool:
    return 32 <= ord(ch) <= 126
```

**Use Case:** A data masking service encodes sensitive identifiers by shifting each character\'s code point with a key-based offset (`ord(ch) + key % 26`) — a simple, reversible transformation that obscures values in test datasets without external crypto dependencies.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Difference between `input()` and `raw_input()`?

This distinction only applies to **Python 2**. In Python 3, `raw_input()` was **renamed to `input()`**.

| | Python 2 `raw_input()` | Python 2 `input()` | Python 3 `input()` |
|--|----------------------|---------------------|-------------------|
| Returns | `str` (raw text) | Evaluated result of `eval(text)` | `str` (raw text) |
| Safe | Yes | **No** — executes arbitrary code | Yes |
| Equivalent in Py3 | `input()` | `eval(input())` | N/A |

```py
# Python 3 — input() always returns a string
name = input("Enter your name: ")
print(type(name))   # <class 'str'>

# Must convert manually for numeric input
age_str = input("Enter your age: ")
age = int(age_str)      # explicit conversion — safe
print(age + 1)

# Safe pattern with error handling
def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value > 0:
                return value
            print("Must be positive.")
        except ValueError:
            print(f"Not a valid integer: {raw!r}")

# Python 2 equivalent reference (DO NOT use input() in Python 2)
# raw_input("Enter: ")  → str  (safe)
# input("Enter: ")      → eval(raw_input("Enter: "))  (dangerous — executes code!)

# In Python 3, eval(input()) is the intentional equivalent of Python 2 input()
# But NEVER use this on untrusted data — use ast.literal_eval() instead
import ast

safe_value = ast.literal_eval(input("Enter a list like [1,2,3]: ") or "[1]")
print(safe_value, type(safe_value))
```

**Use Case:** Migrating a Python 2 CLI tool to Python 3 requires replacing all `raw_input()` calls with `input()` and auditing all `input()` calls (which evaluated code in Py2) to add explicit type conversion — preventing a security regression.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. Why do we write `if __name__ == "__main__"` in a Python script?

When Python runs a file, it sets the module-level `__name__` variable:
- To `"__main__"` if the file is **run directly** (`python script.py`)
- To the **module name** if the file is **imported** (`import script`)

The guard `if __name__ == "__main__":` ensures that certain code (usually the program entry point) **only executes when the file is run directly**, not when it is imported as a module.

```py
# utils.py
import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

def circle_perimeter(radius: float) -> float:
    return 2 * math.pi * radius

print(f"__name__ in utils.py = {__name__!r}")

if __name__ == "__main__":
    # This block only runs when executed as: python utils.py
    # It does NOT run when: import utils
    print("Running as script — quick test:")
    print(f"Area of r=5: {circle_area(5):.2f}")
    print(f"Perimeter of r=5: {circle_perimeter(5):.2f}")
```

```py
# main.py — imports the module
import utils   # __name__ in utils.py = 'utils'  (guard block skipped)

print(utils.circle_area(3))   # 28.27...
```

```bash
$ python utils.py
# __name__ in utils.py = '__main__'
# Running as script — quick test:
# Area of r=5: 78.54
```

**Why it matters:**
- Allows a module to be both importable (library) and directly executable (script)
- Prevents side effects (print, `sys.exit()`, network calls) from triggering on import
- Required for `multiprocessing` on Windows (workers re-import the main module)

**Use Case:** A data pipeline module defines reusable ETL functions at the top level and uses the `__main__` guard for a self-test run that seeds a local database — CI runs `python etl.py` for smoke tests, while Airflow imports the same module\'s functions into DAG tasks without triggering the seed.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is PEP 8?

**PEP 8** (Python Enhancement Proposal 8) is the official **style guide for Python code**. It defines conventions for formatting, naming, and structuring Python code to maximise readability and consistency across the ecosystem.

**Key rules:**

```py
# ── Indentation ──────────────────────────────────────────────────
# Use 4 spaces per indent (never tabs)
def good_function():
    if True:
        pass

# ── Line length ──────────────────────────────────────────────────
# Max 79 characters for code, 72 for docstrings
# Wrap long lines with parentheses (not backslash)
result = (
    some_long_variable_name
    + another_long_variable_name
    + yet_another_one
)

# ── Imports ──────────────────────────────────────────────────────
# Standard library → third-party → local, each group separated by blank line
import os
import sys

import requests   # third-party

from mymodule import helper   # local

# ── Naming conventions ───────────────────────────────────────────
my_variable = 1             # snake_case for variables and functions
MY_CONSTANT = 42            # UPPER_SNAKE_CASE for constants
ClassName = None            # PascalCase for classes
_private_var = "private"    # leading underscore = private
__name_mangled = "mangled"  # double underscore = name mangling
__dunder__ = None           # double underscore both sides = reserved

def calculate_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height

class BankAccount:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance: float = 0.0   # protected

# ── Whitespace ───────────────────────────────────────────────────
x = 1                   # spaces around = in assignment
y = x + 1               # spaces around operators
lst = [1, 2, 3]         # no space before colon in slices
d = {"a": 1}            # space after colon in dict

f(arg1, arg2)           # no space inside function call parens
lst[1:3]                # no spaces in slice

# ── Blank lines ──────────────────────────────────────────────────
# 2 blank lines between top-level definitions
# 1 blank line between methods inside a class

# ── Tools that enforce PEP 8 ─────────────────────────────────────
# ruff        — extremely fast linter + formatter (recommended)
# black       — opinionated formatter
# flake8      — linter
# isort       — import sorter
# mypy        — type checker (PEP 484)
```

**Use Case:** A team of 20 engineers enforces PEP 8 via `ruff` in pre-commit hooks and CI — every PR is automatically formatted before review, eliminating style discussions and reducing code review time by focusing on logic rather than whitespace.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What parameters should you check when a server is down?

When diagnosing a server outage, check these layers in order from infrastructure to application:

```py
import subprocess
import socket
import os
import pathlib
import shutil

def run(cmd: str) -> str:
    """Run a shell command and return output."""
    result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=10)
    return result.stdout.strip()

# 1. Connectivity — can we reach the host?
def check_ping(host: str) -> bool:
    result = subprocess.run(
        ["ping", "-c", "2", host],
        capture_output=True, text=True, timeout=10
    )
    return result.returncode == 0

# 2. Port availability — is the service port open?
def check_port(host: str, port: int, timeout: float = 3.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

# 3. System resources
def check_resources() -> dict:
    return {
        "load_avg":  os.getloadavg(),            # (1m, 5m, 15m)
        "disk_free": shutil.disk_usage("/"),     # .free bytes
        "cpu_count": os.cpu_count(),
    }

# 4. Process status
def check_process(name: str) -> bool:
    result = subprocess.run(
        ["pgrep", "-x", name], capture_output=True
    )
    return result.returncode == 0

# 5. Log analysis — last N error lines
def tail_logs(log_path: str, n: int = 50) -> list[str]:
    p = pathlib.Path(log_path)
    if not p.exists():
        return [f"Log file not found: {log_path}"]
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    return [l for l in lines[-n:] if "ERROR" in l or "FATAL" in l]

# Comprehensive health check report
def server_health_report(host: str, port: int) -> dict:
    return {
        "ping":          check_ping(host),
        "port_open":     check_port(host, port),
        "resources":     check_resources(),
        "app_running":   check_process("python"),
        "recent_errors": tail_logs("/var/log/app/error.log", n=20),
    }
```

**Checklist:**

| Layer | Check | Tool |
|-------|-------|------|
| Network | ping, traceroute | `ping`, `traceroute` |
| DNS | name resolution | `nslookup`, `dig` |
| Port | TCP connect | `telnet`, `nc`, `ss -tlnp` |
| CPU | load average | `uptime`, `top`, `htop` |
| Memory | free RAM, OOM killer | `free -h`, `dmesg | grep -i oom` |
| Disk | space, I/O wait | `df -h`, `iostat` |
| Process | service running | `ps aux`, `systemctl status` |
| Logs | errors, tracebacks | `journalctl`, `tail -f app.log` |
| DB / deps | connection pool | app health endpoint |

**Use Case:** A Python-based monitoring agent runs `server_health_report()` every 60 seconds and publishes metrics to Prometheus — alerting on-call engineers via PagerDuty when `port_open` is `False` or load average exceeds 8.

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

**Python for AI & Data Science**

## # 22. Numerical Computing

<br>

## Q. How to get indices of N maximum values in a NumPy array?

We can get the indices of N maximum values in a NumPy array using the below code:

```py
import numpy as np
arr = np.array([1, 3, 2, 4, 5])
print(arr.argsort()[-3:][::-1])
```

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. What is the difference between NumPy and SciPy?

In an ideal world, NumPy would contain nothing but the array data type and the most basic operations: indexing, sorting, reshaping, basic element wise functions, et cetera. All numerical code would reside in SciPy. However, one of NumPy\'s important goals is compatibility, so NumPy tries to retain all features supported by either of its predecessors. Thus NumPy contains some linear algebra functions, even though these more properly belong in SciPy. In any case, SciPy contains more fully-featured versions of the linear algebra modules, as well as many other numerical algorithms. If you are doing scientific computing with python, you should probably install both NumPy and SciPy. Most new features belong in SciPy rather than NumPy.

## Q. Name few Python modules for Statistical, Numerical and scientific computations ?

`numPy` – this module provides an array/matrix type, and it is useful for doing computations on arrays.   
`scipy` – this module provides methods for doing numeric integrals, solving differential equations, etc     
`pylab` – is a module for generating and saving plots

## Q. What is NumPy? Is it better than a list?

Python Programming Interview Questions - Numpy vs List

Python Programming Interview Questions – Numpy vs List

Ans.  NumPy, a Python package, has made its place in the world of scientific computing. It can deal with large data sizes, and also has a powerful N-dimensional array object along with a set of advanced functions.

Yes, a NumPy array is better than a Python list. This is in the following ways:

    It is more compact.
    It is more convenient.
    It Is more efficiently.
    It is easier to read and write items with NumPy.

Read our latest tutorial on Python NumPy

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>

## Q. How would you create an empty NumPy array?

Ans.  To create an empty array with NumPy, we have two options:

a. Option 1

     import numpy
     numpy.array([])

array([], dtype=float64)

b. Option 2

     numpy.empty(shape=(0,0))

array([], shape=(0, 0), dtype=float64)

<div align="right">
    <b><a href="#table-of-contents">↥ back to top</a></b>
</div>
