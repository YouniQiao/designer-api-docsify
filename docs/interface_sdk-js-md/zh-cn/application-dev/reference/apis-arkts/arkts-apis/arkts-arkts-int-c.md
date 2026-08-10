# Int

Represents boxed int value and related operations

**继承/实现关系：** Int extends [Integral](arkts-arkts-numeric-integral-c.md) implements [Comparable<Int>](Comparable<Int>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Int extends Integral implements Comparable<Int>--><!--Device-unnamed-export class Int extends Integral implements Comparable<Int>-End-->

**系统能力：** SystemCapability.Utils.Lang

## add

```TypeScript
public add(other: Int): Int
```

Performs integral addition with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public add(other: Int): Int--><!--Device-Int-public add(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the addition. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the addition. |

## compareTo

```TypeScript
public compareTo(other: Int): int
```

Compares this instance to other Int object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public compareTo(other: Int): int--><!--Device-Int-public compareTo(other: Int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | Int object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | result of the comparison (-1, 0, or 1). |

## constructor

```TypeScript
constructor()
```

Constructs a new Int instance with initial value zero

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-constructor()--><!--Device-Int-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: int)
```

Constructs a new Int instance with provided initial value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-constructor(value: int)--><!--Device-Int-constructor(value: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | the initial value &lt;br&gt;The value should be an integer. |

## div

```TypeScript
public div(other: Int): Int
```

Performs integral division with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public div(other: Int): Int--><!--Device-Int-public div(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the division. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the division. |

## equals

```TypeScript
equals(other: Any): boolean
```

Compares this object with the specified object for equality.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-equals(other: Any): boolean--><!--Device-Int-equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | the object to compare with |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the specified object is equal to this object, false otherwise |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Int): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isGreaterEqualThan(other: Int): boolean--><!--Device-Int-public isGreaterEqualThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than or equal to provided. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Int): boolean
```

Checks if this instance value is greater than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isGreaterThan(other: Int): boolean--><!--Device-Int-public isGreaterThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than provided. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Int): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isLessEqualThan(other: Int): boolean--><!--Device-Int-public isLessEqualThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than or equal to provided. |

## isLessThan

```TypeScript
public isLessThan(other: Int): boolean
```

Checks if this instance value is less than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isLessThan(other: Int): boolean--><!--Device-Int-public isLessThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than provided. |

## mul

```TypeScript
public mul(other: Int): Int
```

Performs integral multiplication with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public mul(other: Int): Int--><!--Device-Int-public mul(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the multiplication. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): int
```

Parses from String an integer of specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static parseInt(s: string, r: int): int--><!--Device-Int-public static parseInt(s: string, r: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert. |
| r | int | 是 | the radix of conversion (2-36). &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the result of parsing. |

## sub

```TypeScript
public sub(other: Int): Int
```

Performs integral subtraction with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public sub(other: Int): Int--><!--Device-Int-public sub(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | right hand side of the subtraction. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toByte(): byte--><!--Device-Int-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: int): byte
```

Returns the primitive as byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toByte(value: int): byte--><!--Device-Int-public static toByte(value: int): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to cast. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | casted value. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toChar(): char--><!--Device-Int-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | value as char. |

## toChar

```TypeScript
public static toChar(value: int): char
```

Returns the primitive as char value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toChar(value: int): char--><!--Device-Int-public static toChar(value: int): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to cast. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | casted value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toDouble(): double--><!--Device-Int-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: int): double
```

Returns the primitive as double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toDouble(value: int): double--><!--Device-Int-public static toDouble(value: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to cast. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | casted value. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toFloat(): float--><!--Device-Int-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: int): float
```

Returns the primitive as float value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toFloat(value: int): float--><!--Device-Int-public static toFloat(value: int): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to cast. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | casted value. |

## toInt

```TypeScript
toInt(): int
```

Converts the value of this instance to an int

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-toInt(): int--><!--Device-Int-toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the int value represented by this instance |

## toInt

```TypeScript
static toInt(value: int): int
```

Returns the primitive int value directly

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-static toInt(value: int): int--><!--Device-Int-static toInt(value: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | the int value to return &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the same int value that was passed in |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

<!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toLong(): long--><!--Device-Int-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | value as long. |

## toLong

```TypeScript
public static toLong(value: int): long
```

Returns the primitive as long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toLong(value: int): long--><!--Device-Int-public static toLong(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to cast. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | casted value. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toShort(): short--><!--Device-Int-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: int): short
```

Returns the primitive as short value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toShort(value: int): short--><!--Device-Int-public static toShort(value: int): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to cast. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
static toString(v: int): string
```

Converts the specified int value to its string representation.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-static toString(v: int): string--><!--Device-Int-static toString(v: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | int | 是 | the int value to be converted &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation of the int value |

## toString

```TypeScript
toString(): string
```

Converts the value of this Int object to its string representation.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-toString(): string--><!--Device-Int-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation of this Int object's value |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string in the given radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toString(radix: int): string--><!--Device-Int-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | the radix to use. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(radix: double): string
```

Converts this object to a string in the given radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toString(radix: double): string--><!--Device-Int-public toString(radix: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | double | 是 | the radix to use. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 32
```

Size of this type in bits.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly BIT_SIZE: byte = 32--><!--Device-Int-public static readonly BIT_SIZE: byte = 32-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 4
```

Size of this type in bytes.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly BYTE_SIZE: byte = 4--><!--Device-Int-public static readonly BYTE_SIZE: byte = 4-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: int = 2147483647
```

Maximal value that this type can have as an integral.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly MAX_VALUE: int = 2147483647--><!--Device-Int-public static readonly MAX_VALUE: int = 2147483647-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: int = -2147483648
```

Minimal value that this type can have as an integral.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly MIN_VALUE: int = -2147483648--><!--Device-Int-public static readonly MIN_VALUE: int = -2147483648-End-->

**系统能力：** SystemCapability.Utils.Lang

