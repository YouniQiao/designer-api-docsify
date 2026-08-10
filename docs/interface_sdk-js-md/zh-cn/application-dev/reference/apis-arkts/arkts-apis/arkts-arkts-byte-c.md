# Byte

Represents boxed byte value and related operations

**继承/实现关系：** Byte extends [Integral](arkts-arkts-numeric-integral-c.md) implements [Comparable<Byte>](Comparable<Byte>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Byte extends Integral implements Comparable<Byte>--><!--Device-unnamed-export class Byte extends Integral implements Comparable<Byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

## add

```TypeScript
public add(other: Byte): Byte
```

Performs integral addition of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public add(other: Byte): Byte--><!--Device-Byte-public add(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the addition. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of addition. |

## compareTo

```TypeScript
public compareTo(other: Byte): int
```

Compares this instance to other Byte object The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public compareTo(other: Byte): int--><!--Device-Byte-public compareTo(other: Byte): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Byte object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the comparison result. |

## constructor

```TypeScript
public constructor()
```

Constructs a new Byte instance with initial value zero

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public constructor()--><!--Device-Byte-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: byte)
```

Constructs a new Byte instance with provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public constructor(value: byte)--><!--Device-Byte-public constructor(value: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | the initial value. |

## div

```TypeScript
public div(other: Byte): Byte
```

Performs integral division of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public div(other: Byte): Byte--><!--Device-Byte-public div(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the division. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Byte Returns false if type of provided object is not the same as this type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public equals(other: Any): boolean--><!--Device-Byte-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | object to be checked against. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if equal, false otherwise. |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Byte): boolean
```

Checks if this instance value is greater than or equal to value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isGreaterEqualThan(other: Byte): boolean--><!--Device-Byte-public isGreaterEqualThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this instance is greater than or equal to other. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Byte): boolean
```

Checks if this instance value is greater than value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isGreaterThan(other: Byte): boolean--><!--Device-Byte-public isGreaterThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this instance is greater than other. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Byte): boolean
```

Checks if this instance value is less than or equal to value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isLessEqualThan(other: Byte): boolean--><!--Device-Byte-public isLessEqualThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this instance is less than or equal to other. |

## isLessThan

```TypeScript
public isLessThan(other: Byte): boolean
```

Checks if this instance value is less than value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isLessThan(other: Byte): boolean--><!--Device-Byte-public isLessThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this instance is less than other. |

## mul

```TypeScript
public mul(other: Byte): Byte
```

Performs integral multiplication of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public mul(other: Byte): Byte--><!--Device-Byte-public mul(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the multiplication. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): byte
```

Parses a string to a byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static parseInt(s: string, r: int): byte--><!--Device-Byte-public static parseInt(s: string, r: int): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | The string to parse. |
| r | int | 是 | The radix of the string. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | The parsed byte value. |

## sub

```TypeScript
public sub(other: Byte): Byte
```

Performs integral subtraction of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public sub(other: Byte): Byte--><!--Device-Byte-public sub(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | Right hand side of the subtraction. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toByte(): byte--><!--Device-Byte-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the byte value. |

## toByte

```TypeScript
public static toByte(value: byte): byte
```

Returns the primitive as byte value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toByte(value: byte): byte--><!--Device-Byte-public static toByte(value: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the byte value. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toChar(): char--><!--Device-Byte-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the char value. |

## toChar

```TypeScript
public static toChar(value: byte): char
```

Returns the primitive as char value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toChar(value: byte): char--><!--Device-Byte-public static toChar(value: byte): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the char value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toDouble(): double--><!--Device-Byte-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the double value. |

## toDouble

```TypeScript
public static toDouble(value: byte): double
```

Returns the primitive as double value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toDouble(value: byte): double--><!--Device-Byte-public static toDouble(value: byte): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the double value. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toFloat(): float--><!--Device-Byte-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the float value. |

## toFloat

```TypeScript
public static toFloat(value: byte): float
```

Returns the primitive as float value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toFloat(value: byte): float--><!--Device-Byte-public static toFloat(value: byte): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the float value. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toInt(): int--><!--Device-Byte-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the int value. |

## toInt

```TypeScript
public static toInt(value: byte): int
```

Returns the primitive as int value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toInt(value: byte): int--><!--Device-Byte-public static toInt(value: byte): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the int value. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | Intl.NumberFormatOptions | 否 | An object with some or all of the properties of the Intl.NumberFormat options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the elements of the array. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | 否 | An object with configuration properties. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the elements of the array. |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toLong(): long--><!--Device-Byte-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the long value. |

## toLong

```TypeScript
public static toLong(value: byte): long
```

Returns the primitive as long value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toLong(value: byte): long--><!--Device-Byte-public static toLong(value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the long value. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toShort(): short--><!--Device-Byte-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the short value. |

## toShort

```TypeScript
public static toShort(value: byte): short
```

Returns the primitive as short value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toShort(value: byte): short--><!--Device-Byte-public static toShort(value: byte): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the short value. |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toString(): string--><!--Device-Byte-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public static toString(v: byte): string
```

Converts the primitive to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toString(v: byte): string--><!--Device-Byte-public static toString(v: byte): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | byte | 是 | value to be converted. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toString(radix: int): string--><!--Device-Byte-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | to use for conversion. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public toString(radix: double): string
```

Converts this object to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toString(radix: double): string--><!--Device-Byte-public toString(radix: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | double | 是 | to use for conversion. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 8
```

Size of this type in bits.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static BIT_SIZE: byte = 8--><!--Device-Byte-public static BIT_SIZE: byte = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 1
```

Size of this type in bytes.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static BYTE_SIZE: byte = 1--><!--Device-Byte-public static BYTE_SIZE: byte = 1-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: byte = 127
```

Maximal value that this type can have as an integral.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static MAX_VALUE: byte = 127--><!--Device-Byte-public static MAX_VALUE: byte = 127-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: byte = -128
```

Minimal value that this type can have as an integral.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static MIN_VALUE: byte = -128--><!--Device-Byte-public static MIN_VALUE: byte = -128-End-->

**系统能力：** SystemCapability.Utils.Lang

