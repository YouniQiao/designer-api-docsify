# Short

Represents boxed short value and related operations

**继承/实现关系：** Short extends [Integral](arkts-arkts-numeric-integral-c.md) implements [Comparable<Short>](Comparable<Short>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Short extends Integral implements Comparable<Short>--><!--Device-unnamed-export class Short extends Integral implements Comparable<Short>-End-->

**系统能力：** SystemCapability.Utils.Lang

## add

```TypeScript
public add(other: Short): Short
```

Performs integral addition of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public add(other: Short): Short--><!--Device-Short-public add(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the addition. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the addition. |

## compareTo

```TypeScript
public compareTo(other: Short): int
```

Compares this instance to other Short object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public compareTo(other: Short): int--><!--Device-Short-public compareTo(other: Short): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Short object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | result of the comparison, -1 if this instance is less than provided object, 0 if equal, 1 if greater. |

## constructor

```TypeScript
public constructor()
```

Constructs a new Short instance with initial value zero.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public constructor()--><!--Device-Short-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: short)
```

Constructs a new Short instance with provided initial value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public constructor(value: short)--><!--Device-Short-public constructor(value: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | the initial value. |

## div

```TypeScript
public div(other: Short): Short
```

Performs integral division of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public div(other: Short): Short--><!--Device-Short-public div(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the division. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Short.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public equals(other: Any): boolean--><!--Device-Short-public equals(other: Any): boolean-End-->

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
public isGreaterEqualThan(other: Short): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isGreaterEqualThan(other: Short): boolean--><!--Device-Short-public isGreaterEqualThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than or equal to provided, false otherwise. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Short): boolean
```

Checks if this instance value is greater than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isGreaterThan(other: Short): boolean--><!--Device-Short-public isGreaterThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than provided, false otherwise. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Short): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isLessEqualThan(other: Short): boolean--><!--Device-Short-public isLessEqualThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than or equal to provided, false otherwise. |

## isLessThan

```TypeScript
public isLessThan(other: Short): boolean
```

Checks if this instance value is less than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isLessThan(other: Short): boolean--><!--Device-Short-public isLessThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than provided, false otherwise. |

## mul

```TypeScript
public mul(other: Short): Short
```

Performs integral multiplication of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public mul(other: Short): Short--><!--Device-Short-public mul(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the multiplication. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): short
```

Parses from string an integer of specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static parseInt(s: string, r: int): short--><!--Device-Short-public static parseInt(s: string, r: int): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert. |
| r | int | 是 | the radix of conversion; should be [2, 36]; 0 assumed to be 10. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the result of parsing. |

## sub

```TypeScript
public sub(other: Short): Short
```

Performs integral subtraction of this instance with provided one, returns the result as new instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public sub(other: Short): Short--><!--Device-Short-public sub(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | 是 | Right hand side of the subtraction. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance as byte.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toByte(): byte--><!--Device-Short-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: short): byte
```

Returns the primitive as byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toByte(value: short): byte--><!--Device-Short-public static toByte(value: short): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

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

<!--Device-Short-public toChar(): char--><!--Device-Short-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | value as char. |

## toChar

```TypeScript
public static toChar(value: short): char
```

Returns the primitive as char value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toChar(value: short): char--><!--Device-Short-public static toChar(value: short): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

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

<!--Device-Short-public toDouble(): double--><!--Device-Short-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: short): double
```

Returns the primitive as double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toDouble(value: short): double--><!--Device-Short-public static toDouble(value: short): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

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

<!--Device-Short-public toFloat(): float--><!--Device-Short-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: short): float
```

Returns the primitive as float value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toFloat(value: short): float--><!--Device-Short-public static toFloat(value: short): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

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

<!--Device-Short-public toInt(): int--><!--Device-Short-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | value as int. |

## toInt

```TypeScript
public static toInt(value: short): int
```

Returns the primitive as int value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toInt(value: short): int--><!--Device-Short-public static toInt(value: short): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

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

<!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

<!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
public toLong(): long
```

Returns value of this instance as long.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toLong(): long--><!--Device-Short-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | value as long. |

## toLong

```TypeScript
public static toLong(value: short): long
```

Returns the primitive as long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toLong(value: short): long--><!--Device-Short-public static toLong(value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | casted value. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance as short.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toShort(): short--><!--Device-Short-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: short): short
```

Returns the primitive as short value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toShort(value: short): short--><!--Device-Short-public static toShort(value: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
public static toString(v: short): string
```

Converts the primitive to a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toString(v: short): string--><!--Device-Short-public static toString(v: short): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | short | 是 | value to be converted. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toString(): string--><!--Device-Short-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string with specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toString(radix: int): string--><!--Device-Short-public toString(radix: int): string-End-->

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

<!--Device-Short-public toString(radix: double): string--><!--Device-Short-public toString(radix: double): string-End-->

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
public static BIT_SIZE: byte = 16
```

Size of this type in bits.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static BIT_SIZE: byte = 16--><!--Device-Short-public static BIT_SIZE: byte = 16-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 2
```

Size of this type in bytes.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static BYTE_SIZE: byte = 2--><!--Device-Short-public static BYTE_SIZE: byte = 2-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: short = 32767
```

Maximal value that this type can have as a short.

**类型：** short

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static MAX_VALUE: short = 32767--><!--Device-Short-public static MAX_VALUE: short = 32767-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: short = -32768
```

Minimal value that this type can have as a short.

**类型：** short

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static MIN_VALUE: short = -32768--><!--Device-Short-public static MIN_VALUE: short = -32768-End-->

**系统能力：** SystemCapability.Utils.Lang

