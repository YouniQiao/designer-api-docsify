# Long

Represents boxed long value and related operations.

**继承/实现关系：** Long extends [Integral](arkts-arkts-numeric-integral-c.md) implements [Comparable<Long>](Comparable<Long>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Long extends Integral implements Comparable<Long>--><!--Device-unnamed-export class Long extends Integral implements Comparable<Long>-End-->

**系统能力：** SystemCapability.Utils.Lang

## add

```TypeScript
public add(other: Long): Long
```

Performs integral addition of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public add(other: Long): Long--><!--Device-Long-public add(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the addition. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the addition. |

## compareTo

```TypeScript
public compareTo(other: Long): int
```

Compares this instance to other Long object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public compareTo(other: Long): int--><!--Device-Long-public compareTo(other: Long): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Long object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | result of the comparison, -1 if this instance is less than provided object, 0 if equal, 1 if greater. |

## constructor

```TypeScript
constructor()
```

Constructs a new Long instance with initial value zero

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-constructor()--><!--Device-Long-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long)
```

Constructs a new Long instance with provided initial value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-constructor(value: long)--><!--Device-Long-constructor(value: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | the initial value |

## div

```TypeScript
public div(other: Long): Long
```

Performs integral division of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public div(other: Long): Long--><!--Device-Long-public div(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the division. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Long.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public equals(other: Any): boolean--><!--Device-Long-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | object to be checked against. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if provided object and this instance have same value, false otherwise. |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Long): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isGreaterEqualThan(other: Long): boolean--><!--Device-Long-public isGreaterEqualThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than or equal to provided, false otherwise. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Long): boolean
```

Checks if this instance value is greater than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isGreaterThan(other: Long): boolean--><!--Device-Long-public isGreaterThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than provided, false otherwise. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Long): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isLessEqualThan(other: Long): boolean--><!--Device-Long-public isLessEqualThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than or equal to provided, false otherwise. |

## isLessThan

```TypeScript
public isLessThan(other: Long): boolean
```

Checks if this instance value is less than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isLessThan(other: Long): boolean--><!--Device-Long-public isLessThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than provided, false otherwise. |

## mul

```TypeScript
public mul(other: Long): Long
```

Performs integral multiplication of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public mul(other: Long): Long--><!--Device-Long-public mul(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the multiplication. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): long
```

Parses from String an integer of specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static parseInt(s: string, r: int): long--><!--Device-Long-public static parseInt(s: string, r: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert. |
| r | int | 是 | the radix of conversion; should be [2, 36]; 0 assumed to be 10. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the result of parsing. |

## sub

```TypeScript
public sub(other: Long): Long
```

Performs integral subtraction of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public sub(other: Long): Long--><!--Device-Long-public sub(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | Right hand side of the subtraction. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance as byte.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toByte(): byte--><!--Device-Long-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: long): byte
```

Returns the primitive as byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toByte(value: long): byte--><!--Device-Long-public static toByte(value: long): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | casted value. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance as char.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toChar(): char--><!--Device-Long-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | value as char. |

## toChar

```TypeScript
public static toChar(value: long): char
```

Returns the primitive as char value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toChar(value: long): char--><!--Device-Long-public static toChar(value: long): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | casted value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance as double.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toDouble(): double--><!--Device-Long-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: long): double
```

Returns the primitive as double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toDouble(value: long): double--><!--Device-Long-public static toDouble(value: long): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | casted value. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance as float.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toFloat(): float--><!--Device-Long-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: long): float
```

Returns the primitive as float value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toFloat(value: long): float--><!--Device-Long-public static toFloat(value: long): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | casted value. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance as int.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toInt(): int--><!--Device-Long-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | value as int. |

## toInt

```TypeScript
public static toInt(value: long): int
```

Returns the primitive as int value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toInt(value: long): int--><!--Device-Long-public static toInt(value: long): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | casted value. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | Intl.NumberFormatOptions | 否 | An object with some or all of the properties of the Intl.NumberFormat options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the locale-specific conversion |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | 否 | An object with some or all of the properties of the Intl.NumberFormat options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the locale-specific conversion |

## toLong

```TypeScript
toLong(): long
```

Returns value of this instance

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-toLong(): long--><!--Device-Long-toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | value as long |

## toLong

```TypeScript
static toLong(value: long): long
```

Returns the primitive as long value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-static toLong(value: long): long--><!--Device-Long-static toLong(value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | casted value |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance as short.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toShort(): short--><!--Device-Long-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: long): short
```

Returns the primitive as short value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toShort(value: long): short--><!--Device-Long-public static toShort(value: long): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
static toString(v: long): string
```

Converts the primitive to a string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-static toString(v: long): string--><!--Device-Long-static toString(v: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | long | 是 | value to be converted |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion |

## toString

```TypeScript
toString(): string
```

Converts this object to a string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-toString(): string--><!--Device-Long-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | Input parameter error. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string with specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toString(radix: int): string--><!--Device-Long-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | the radix of conversion. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(radix: double): string
```

Converts this object to a string with specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toString(radix: double): string--><!--Device-Long-public toString(radix: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | double | 是 | the radix of conversion. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 64
```

Size of this type in bits.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static BIT_SIZE: byte = 64--><!--Device-Long-public static BIT_SIZE: byte = 64-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 8
```

Size of this type in bytes.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static BYTE_SIZE: byte = 8--><!--Device-Long-public static BYTE_SIZE: byte = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: long = 9223372036854775807
```

Maximal value that this type can have as a long.

**类型：** long

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static MAX_VALUE: long = 9223372036854775807--><!--Device-Long-public static MAX_VALUE: long = 9223372036854775807-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: long = -9223372036854775808
```

Minimal value that this type can have as a long.

**类型：** long

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static MIN_VALUE: long = -9223372036854775808--><!--Device-Long-public static MIN_VALUE: long = -9223372036854775808-End-->

**系统能力：** SystemCapability.Utils.Lang

