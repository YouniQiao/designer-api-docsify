# Console

A Console class that provides access to standard output and error streams.Supports printing various data types, timing operations, and indentation management.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-class Console--><!--Device-unnamed-class Console-End-->

**系统能力：** SystemCapability.Utils.Lang

## assert

```TypeScript
assert(...vals: Any[]): void
```

Conditionally prints an error message if the assertion condition is false Condition is the first value in vals (if exist)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-assert(...vals: Any[]): void--><!--Device-Console-assert(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | Values to be logged if condition is false. |

## count

```TypeScript
count(label?: string): void
```

Counts the number of times this method has been called with a specific label Prints the current count to stdout

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-count(label?: string): void--><!--Device-Console-count(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | The value to count |

## countReset

```TypeScript
countReset(label?: string): void
```

Resets the counter for a specific label

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-countReset(label?: string): void--><!--Device-Console-countReset(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | The value to resets the counter |

## debug

```TypeScript
debug(...vals: Any[]): void
```

Prints debug-level messages If first argument is a string it is treated as a format string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-debug(...vals: Any[]): void--><!--Device-Console-debug(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | Variable number of values to be logged |

## dir

```TypeScript
dir(obj?: Any): void
```

Prints a formatted representation of an object to stdout Filters out properties containing 'field#' in their keys

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-dir(obj?: Any): void--><!--Device-Console-dir(obj?: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 否 | The object to inspect |

## dirxml

```TypeScript
dirxml(...obj: Any[]): void
```

Prints an XML representation of an object to stdout Currently outputs the object as-is

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-dirxml(...obj: Any[]): void--><!--Device-Console-dirxml(...obj: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any[] | 是 | The object to display as XML. |

## error

```TypeScript
error(...vals: Any[]): void
```

Prints error-level messages If first argument is a string it is treated as a format string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-error(...vals: Any[]): void--><!--Device-Console-error(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | Variable number of values to be logged |

## getInstance

```TypeScript
public static getInstance(): Console
```

Gets the singleton instance of Console.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public static getInstance(): Console--><!--Device-Console-public static getInstance(): Console-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Console](arkts-arkts-console-c.md) | the singleton Console instance. |

## group

```TypeScript
group(...objs: Any[]): void
```

Starts a new logging group with optional label Increases indentation level for subsequent log messages

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-group(...objs: Any[]): void--><!--Device-Console-group(...objs: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objs | Any[] | 是 | The object to starts a new logging group |

## groupCollapsed

```TypeScript
groupCollapsed(...objs: Any[]): void
```

Alias for group() method Creates a collapsed group in environments that support it

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-groupCollapsed(...objs: Any[]): void--><!--Device-Console-groupCollapsed(...objs: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objs | Any[] | 是 | The object to creates a collapsed group |

## groupEnd

```TypeScript
groupEnd(): void
```

Ends the current logging group Decreases indentation level for subsequent log messages

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-groupEnd(): void--><!--Device-Console-groupEnd(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## info

```TypeScript
info(...vals: Any[]): void
```

Prints info-level messages If first argument is a string it is treated as a format string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-info(...vals: Any[]): void--><!--Device-Console-info(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | Variable number of values to be logged |

## log

```TypeScript
log(i: boolean): void
```

Implementations for log primitive types to stdout

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: boolean): void--><!--Device-Console-log(i: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | The value to print to stdout |

## log

```TypeScript
log(i: byte): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: byte): void--><!--Device-Console-log(i: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | The value to print |

## log

```TypeScript
log(i: short): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: short): void--><!--Device-Console-log(i: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | The value to print |

## log

```TypeScript
log(i: char): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: char): void--><!--Device-Console-log(i: char): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | The value to print |

## log

```TypeScript
log(i: int): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: int): void--><!--Device-Console-log(i: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | The value to print &lt;br&gt;The value should be an integer. |

## log

```TypeScript
log(i: long): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: long): void--><!--Device-Console-log(i: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | The value to print |

## log

```TypeScript
log(i: float): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: float): void--><!--Device-Console-log(i: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | The value to print |

## log

```TypeScript
log(i: double): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: double): void--><!--Device-Console-log(i: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | The value to print |

## log

```TypeScript
log(i: string): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: string): void--><!--Device-Console-log(i: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | string | 是 | The value to print |

## log

```TypeScript
log(): void
```

log

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(): void--><!--Device-Console-log(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## log

```TypeScript
log(...vals: Any[]): void
```

Prints log-level messages If first argument is a string it is treated as a format string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(...vals: Any[]): void--><!--Device-Console-log(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | Variable number of values to be logged |

## print

```TypeScript
public print(i: boolean): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: boolean): void--><!--Device-Console-public print(i: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: byte): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: byte): void--><!--Device-Console-public print(i: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: short): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: short): void--><!--Device-Console-public print(i: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: char): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: char): void--><!--Device-Console-public print(i: char): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: int): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: int): void--><!--Device-Console-public print(i: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | The value to print to stdout. &lt;br&gt;The value should be an integer. |

## print

```TypeScript
public print(i: long): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: long): void--><!--Device-Console-public print(i: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: float): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: float): void--><!--Device-Console-public print(i: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: double): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: double): void--><!--Device-Console-public print(i: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: string): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: string): void--><!--Device-Console-public print(i: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | string | 是 | The value to print to stdout. |

## print

```TypeScript
public print(i: Any): void
```

Implementations for printing primitive types to stdout without newline.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: Any): void--><!--Device-Console-public print(i: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | Any | 是 | The value to print to stdout. |

## println

```TypeScript
public println(): void
```

Prints a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(): void--><!--Device-Console-public println(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## println

```TypeScript
public println(i: boolean): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: boolean): void--><!--Device-Console-public println(i: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: byte): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: byte): void--><!--Device-Console-public println(i: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: short): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: short): void--><!--Device-Console-public println(i: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: char): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: char): void--><!--Device-Console-public println(i: char): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: int): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: int): void--><!--Device-Console-public println(i: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | The value to print to stdout. &lt;br&gt;The value should be an integer. |

## println

```TypeScript
public println(i: long): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: long): void--><!--Device-Console-public println(i: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: float): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: float): void--><!--Device-Console-public println(i: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: double): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: double): void--><!--Device-Console-public println(i: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: string): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: string): void--><!--Device-Console-public println(i: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | string | 是 | The value to print to stdout. |

## println

```TypeScript
public println(i: Any): void
```

Prints a value followed by a newline to stdout.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: Any): void--><!--Device-Console-public println(i: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | Any | 是 | The value to print to stdout. |

## table

```TypeScript
table(...data: Any[]): void
```

Displays an array of objects in tabular format Converts the data to a DataFrame and renders it

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-table(...data: Any[]): void--><!--Device-Console-table(...data: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Any[] | 是 | Array of objects to display as a table |

## time

```TypeScript
time(label?: string): void
```

Starts a timer with an optional label Used to track execution time between time() and timeEnd() calls

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-time(label?: string): void--><!--Device-Console-time(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | The key of timer |

## timeEnd

```TypeScript
timeEnd(label?: string): void
```

Stops a timer and logs its duration Removes the timer and prints a warning if it doesn't exist

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-timeEnd(label?: string): void--><!--Device-Console-timeEnd(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | The key of timer |

## timeLog

```TypeScript
timeLog(label?: string, ...arguments: Object[]): void
```

Logs the current duration of a running timer without stopping it Prints a warning if the specified timer doesn't exist.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-timeLog(label?: string, ...arguments: Object[]): void--><!--Device-Console-timeLog(label?: string, ...arguments: Object[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | The key of timer |
| arguments | Object[] | 是 | Additional debugging information |

## trace

```TypeScript
trace(...data: Any[]): void
```

Prints the current stack trace with an optional label Skips the first stack frame (the trace call itself)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-trace(...data: Any[]): void--><!--Device-Console-trace(...data: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Any[] | 是 | Additional debugging information |

## warn

```TypeScript
warn(...vals: Any[]): void
```

Prints warn-level messages If first argument is a string it is treated as a format string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-warn(...vals: Any[]): void--><!--Device-Console-warn(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | Variable number of values to be logged |

