**[<--- Go back to piko::tools](https://github.com/pikotutorial/piko_tools)**

# Introduction

**_PyBedded_** is an experimental utility which allows user to write code for Arduino using Python. The purpose of this project **is not** to control Arduino board by a Python script hosted on a different machine. The purpose of **_PyBedded_** is to enable user to flash Arduino board with the actual logic written with Python, so that the board is independent from host.

# Quick start

## Installation

To install all the dependencies required by **_PyBedded_**, connect an Arduino board to your computer and run from the repository root:

```bash
./scripts/install.sh
```

## Basic usage

Assuming that you have _pybedded_ cloned at the same level as your script, the first thing you need to do is to import necessary types from the _pybedded_ module:

```python
from pybedded import *
```

Next, you must start a Python block of Arduino code using `ArduinoBoard` class. You must provide the port your Arduino is connected to and the specific board you're using, for example:

```python
with ArduinoBoard(port="/dev/ttyUSB0", board=Board.UNO):
```

Now, the entire logic that you write within this block, will be flashed to the Arduino board. Bellow you can see the traditional blink example:

```python
from pybedded import *

with ArduinoBoard("/dev/ttyUSB0", Board.UNO):
    def setup() -> None:
        pinMode(LED_BUILTIN, OUTPUT)

    def loop() -> None:
        digitalWrite(LED_BUILTIN, HIGH)
        delay(1000)
        digitalWrite(LED_BUILTIN, LOW)
        delay(1000)
```

Currently the project supports _almost_ all features present in the Arduino IDE examples. You can find these examples rewritten to Python in [examples folder](./examples/).

# Usage

There are certain rules that need to be followed when writing code with **_PyBedded_**. They are described in this chapter.

## Required code structure

Similarily as in Arduino IDE, the minimum code structure in the Arduino code block consists of `setup` and `loop` functions:

```python
def setup() -> None:
    pass

def loop() -> None:
    pass
```

## Variable definition
### Global variables

Global variables are defined as ordinary Python variables, but type annotations are required, for example:

```python
var: int = 12
```

If you want to modify the global variable definition inside `setup`, `loop` or any other user-defined function, you must mark it using Python's `global` keyword:

```python
var: int = 12

def setup() -> None:
    global var
    var += 1

def loop() -> None:
    global var
    var = 0
```

### Compile-time constants

Python is not a compiled programming language, so in order to support compile time constants (`#define` in C and C++), there needs to be a special mechanism which distinguishes them from the ordinary variables. **_PyBedded_** uses for that purpose a simple naming convention - if Python's variable name is uppercase, it will end up as a compile time constant:

```python
LED_PIN: int = 12
counter: int = 0
```

The above code is an equivalent of the following code in C/C++:

```cpp
#define LED_PIN 12
int counter = 0;
```

### Arrays

Arrays are defined using Python's `List` type. If you initialize your array with a specific value, you may omit the array size because it will be deduced from the number of elements:

```python
from typing import List

array: List[int] = [1, 2, 3, 4, 5]
```

However, if you declare an empty array, you must provide its size in the comment. Again, in Python there is nothing like size of the `List` specified upfront, so here another convention is used:

```python
array: List[int] = [] # size=12
```

What translates to the following code in C/C++:

```cpp
int array[12];
```

## Function definitions

You can define any function within Arduino code block using the ordinary Python syntax for function definition. Type annotations are mandatory, similarly as for the variables definition:

```python
def calibrate(sensor: str, time: int) -> int:
    return 0
```

## Pre-processor directives

To include some compile-time conditions into your code, user can user the following functions provided by **_PyBedded_**:
* `IFDEF("FLAG")` - equivalent of `#ifdef FLAG` in C/C++
* `IFNDEF("FLAG")` - equivalent of `#ifndef FLAG` in C/C++
* `ENDIF` - equivalent of `#endif` in C/C++

```python
IFDEF("SOME_FEATURE_FLAG")
    for i in range(10):
        print(i)
ENDIF()
```

## Core Arduino API

You can expect the core Arduino API to be already there (things like `analogRead`, `millis`, `Serial`, `constrain` etc.).

## External libraries

The following external libraries are currently supported:
* EEPROM
* Servo
* SoftwareSerial
* SPI
* LiquidCrystal
* SD
* Stepper
* Ethernet
* Keyboard
* Wire

You don't need to take care about including them in any way - if you use e.g. `SdVolume` type in your code, the proper `"SD.h"` header will be included before the compilation.

# Debugging

When initiating Arduino code block with `with ArduinoBoard(...)` you may notice that this class has 4 additional, optional constructor arguments in form of `bool` flags:
* `verbose`
* `compile`
* `upload`
* `clean_up`

```python
def __init__(self, port: str, board: Board, verbose: bool = False, compile: bool = True, upload: bool = True, clean_up: bool = True):
```

With these you can realize various debugging scenarios, for example:
* `verbose=True` - if enabled, **_PyBedded_** will print logs from all its underlying operations (mainly Python to C++ code conversion)
* `upload=False` - allows user to just compile the code, without attempting to upload it to the board
* `compile=False, upload=False, clean_up=False` - omits compilation and upload, but generates the C++ code and does not delete it afterwards what gives insight into what's actually being uploaded to the board
* `verbose=True, upload=False, clean_up=False` - detailed logs, followed by the compilation. The generated code is not removed, so can be investigated in case of e.g. compilation error.

# Limitations

At this stage of development, there are many known limitations that the user should be aware of:
* no support for classes/structures definitions
* compile-time constants require explicit type, although it is not used in the final code
* variables definitions and modifications must be done in a single line - although the below snippet is a perfectly valid Python code, it will not be properly converted by **_PyBedded_**:

```python
s: str = (f"this"
          f"is string")
x: int = 0
x += 1 + \
    12 + 48
```
* statements like `if` conditions or multi-argument function calls must be done in a single line - the following code will not be properly handled:

```python
if a and b and \
    c and d:
    pass
value: int = map(12, 0, 1023,
                 0, 255)
```
* no support for including other files - the whole program must be contained in a single script

# How to add support for the new library

To add support for some library which is currently not supported:
* add its API skeleton to some file
* expose all the useful types in the repo _root_ init file and _src_ init file
* add an example using the new API
* add that example to [examples script](./scripts/compile_examples.sh)
