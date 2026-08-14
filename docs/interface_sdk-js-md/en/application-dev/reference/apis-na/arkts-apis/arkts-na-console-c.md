# Console

A Console class that provides access to standard output and error streams. Supports printing various data types, timing operations, and indentation management.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-class Console--><!--Device-unnamed-class Console-End-->

**System capability:** SystemCapability.Utils.Lang

## assert

```TypeScript
assert(...vals: Any[]): void
```

Conditionally prints an error message if the assertion condition is false Condition is the first value in vals (if exist)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-assert(...vals: Any[]): void--><!--Device-Console-assert(...vals: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vals | Any[] | Yes | Values to be logged if condition is false. |

## count

```TypeScript
count(label?: string): void
```

Counts the number of times this method has been called with a specific label Prints the current count to stdout

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-count(label?: string): void--><!--Device-Console-count(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | The value to count |

## countReset

```TypeScript
countReset(label?: string): void
```

Resets the counter for a specific label

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-countReset(label?: string): void--><!--Device-Console-countReset(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | The value to resets the counter |

## debug

```TypeScript
debug(...vals: Any[]): void
```

Prints debug-level messages If first argument is a string it is treated as a format string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-debug(...vals: Any[]): void--><!--Device-Console-debug(...vals: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vals | Any[] | Yes | Variable number of values to be logged |

## dir

```TypeScript
dir(obj?: Any): void
```

Prints a formatted representation of an object to stdout Filters out properties containing 'field#' in their keys

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-dir(obj?: Any): void--><!--Device-Console-dir(obj?: Any): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | No | The object to inspect |

## dirxml

```TypeScript
dirxml(...obj: Any[]): void
```

Prints an XML representation of an object to stdout Currently outputs the object as-is

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-dirxml(...obj: Any[]): void--><!--Device-Console-dirxml(...obj: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any[] | Yes | The object to display as XML. |

## error

```TypeScript
error(...vals: Any[]): void
```

Prints error-level messages If first argument is a string it is treated as a format string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-error(...vals: Any[]): void--><!--Device-Console-error(...vals: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vals | Any[] | Yes | Variable number of values to be logged |

## getInstance

```TypeScript
public static getInstance(): Console
```

Gets the singleton instance of Console.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public static getInstance(): Console--><!--Device-Console-public static getInstance(): Console-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Console](arkts-na-console-c.md) | the singleton Console instance. |

## group

```TypeScript
group(...objs: Any[]): void
```

Starts a new logging group with optional label Increases indentation level for subsequent log messages

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-group(...objs: Any[]): void--><!--Device-Console-group(...objs: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| objs | Any[] | Yes | The object to starts a new logging group |

## groupCollapsed

```TypeScript
groupCollapsed(...objs: Any[]): void
```

Alias for group() method Creates a collapsed group in environments that support it

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-groupCollapsed(...objs: Any[]): void--><!--Device-Console-groupCollapsed(...objs: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| objs | Any[] | Yes | The object to creates a collapsed group |

## groupEnd

```TypeScript
groupEnd(): void
```

Ends the current logging group Decreases indentation level for subsequent log messages

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-groupEnd(): void--><!--Device-Console-groupEnd(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## info

```TypeScript
info(...vals: Any[]): void
```

Prints info-level messages If first argument is a string it is treated as a format string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-info(...vals: Any[]): void--><!--Device-Console-info(...vals: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vals | Any[] | Yes | Variable number of values to be logged |

## log

```TypeScript
log(i: boolean): void
```

Implementations for log primitive types to stdout

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: boolean): void--><!--Device-Console-log(i: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | boolean | Yes | The value to print to stdout |

## log

```TypeScript
log(i: byte): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: byte): void--><!--Device-Console-log(i: byte): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | byte | Yes | The value to print |

## log

```TypeScript
log(i: short): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: short): void--><!--Device-Console-log(i: short): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | short | Yes | The value to print |

## log

```TypeScript
log(i: char): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: char): void--><!--Device-Console-log(i: char): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | char | Yes | The value to print |

## log

```TypeScript
log(i: int): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: int): void--><!--Device-Console-log(i: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | int | Yes | The value to print <br>The value should be an integer. |

## log

```TypeScript
log(i: long): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: long): void--><!--Device-Console-log(i: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | long | Yes | The value to print |

## log

```TypeScript
log(i: float): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: float): void--><!--Device-Console-log(i: float): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | float | Yes | The value to print |

## log

```TypeScript
log(i: double): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: double): void--><!--Device-Console-log(i: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | double | Yes | The value to print |

## log

```TypeScript
log(i: string): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(i: string): void--><!--Device-Console-log(i: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | string | Yes | The value to print |

## log

```TypeScript
log(): void
```

log

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(): void--><!--Device-Console-log(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## log

```TypeScript
log(...vals: Any[]): void
```

Prints log-level messages If first argument is a string it is treated as a format string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-log(...vals: Any[]): void--><!--Device-Console-log(...vals: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vals | Any[] | Yes | Variable number of values to be logged |

## print

```TypeScript
public print(i: boolean): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: boolean): void--><!--Device-Console-public print(i: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | boolean | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: byte): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: byte): void--><!--Device-Console-public print(i: byte): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | byte | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: short): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: short): void--><!--Device-Console-public print(i: short): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | short | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: char): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: char): void--><!--Device-Console-public print(i: char): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | char | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: int): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: int): void--><!--Device-Console-public print(i: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | int | Yes | The value to print to stdout. <br>The value should be an integer. |

## print

```TypeScript
public print(i: long): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: long): void--><!--Device-Console-public print(i: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | long | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: float): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: float): void--><!--Device-Console-public print(i: float): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | float | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: double): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: double): void--><!--Device-Console-public print(i: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | double | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: string): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: string): void--><!--Device-Console-public print(i: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | string | Yes | The value to print to stdout. |

## print

```TypeScript
public print(i: Any): void
```

Implementations for printing primitive types to stdout without newline.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public print(i: Any): void--><!--Device-Console-public print(i: Any): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | Any | Yes | The value to print to stdout. |

## println

```TypeScript
public println(): void
```

Prints a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(): void--><!--Device-Console-public println(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## println

```TypeScript
public println(i: boolean): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: boolean): void--><!--Device-Console-public println(i: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | boolean | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: byte): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: byte): void--><!--Device-Console-public println(i: byte): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | byte | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: short): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: short): void--><!--Device-Console-public println(i: short): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | short | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: char): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: char): void--><!--Device-Console-public println(i: char): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | char | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: int): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: int): void--><!--Device-Console-public println(i: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | int | Yes | The value to print to stdout. <br>The value should be an integer. |

## println

```TypeScript
public println(i: long): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: long): void--><!--Device-Console-public println(i: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | long | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: float): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: float): void--><!--Device-Console-public println(i: float): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | float | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: double): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: double): void--><!--Device-Console-public println(i: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | double | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: string): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: string): void--><!--Device-Console-public println(i: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | string | Yes | The value to print to stdout. |

## println

```TypeScript
public println(i: Any): void
```

Prints a value followed by a newline to stdout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-public println(i: Any): void--><!--Device-Console-public println(i: Any): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| i | Any | Yes | The value to print to stdout. |

## table

```TypeScript
table(...data: Any[]): void
```

Displays an array of objects in tabular format Converts the data to a DataFrame and renders it

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-table(...data: Any[]): void--><!--Device-Console-table(...data: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Any[] | Yes | Array of objects to display as a table |

## time

```TypeScript
time(label?: string): void
```

Starts a timer with an optional label Used to track execution time between time() and timeEnd() calls

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-time(label?: string): void--><!--Device-Console-time(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | The key of timer |

## timeEnd

```TypeScript
timeEnd(label?: string): void
```

Stops a timer and logs its duration Removes the timer and prints a warning if it doesn't exist

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-timeEnd(label?: string): void--><!--Device-Console-timeEnd(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | The key of timer |

## timeLog

```TypeScript
timeLog(label?: string, ...arguments: Object[]): void
```

Logs the current duration of a running timer without stopping it Prints a warning if the specified timer doesn't exist.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-timeLog(label?: string, ...arguments: Object[]): void--><!--Device-Console-timeLog(label?: string, ...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | The key of timer |
| arguments | Object[] | Yes | Additional debugging information |

## trace

```TypeScript
trace(...data: Any[]): void
```

Prints the current stack trace with an optional label Skips the first stack frame (the trace call itself)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-trace(...data: Any[]): void--><!--Device-Console-trace(...data: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Any[] | Yes | Additional debugging information |

## warn

```TypeScript
warn(...vals: Any[]): void
```

Prints warn-level messages If first argument is a string it is treated as a format string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Console-warn(...vals: Any[]): void--><!--Device-Console-warn(...vals: Any[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vals | Any[] | Yes | Variable number of values to be logged |

