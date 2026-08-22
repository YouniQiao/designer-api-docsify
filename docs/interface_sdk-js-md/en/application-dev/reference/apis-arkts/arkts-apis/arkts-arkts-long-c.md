# Long

Represents boxed long value and related operations.

**Inheritance/Implementation:** Long extends [Integral](arkts-arkts-numeric-integral-c.md) and implements Comparable<Long>

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-unnamed-export class Long--><!--Device-unnamed-export class Long-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## add

```TypeScript
public add(other: Long): Long
```

Performs integral addition of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public add(other: Long): Long--><!--Device-Long-public add(other: Long): Long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the addition. |

**Return value:**

| Type | Description |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the addition. |

## compareTo

```TypeScript
public compareTo(other: Long): int
```

Compares this instance to other Long object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public compareTo(other: Long): int--><!--Device-Long-public compareTo(other: Long): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Long object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | result of the comparison, -1 if this instance is less than provided object, 0 if equal, 1 if greater. |

## constructor

```TypeScript
constructor()
```

Constructs a new Long instance with initial value zero

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-constructor()--><!--Device-Long-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long)
```

Constructs a new Long instance with provided initial value

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-constructor(value: long)--><!--Device-Long-constructor(value: long)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | the initial value |

## div

```TypeScript
public div(other: Long): Long
```

Performs integral division of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public div(other: Long): Long--><!--Device-Long-public div(other: Long): Long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the division. |

**Return value:**

| Type | Description |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Long.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public equals(other: Any): boolean--><!--Device-Long-public equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | object to be checked against. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if provided object and this instance have same value, false otherwise. |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Long): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public isGreaterEqualThan(other: Long): boolean--><!--Device-Long-public isGreaterEqualThan(other: Long): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than or equal to provided, false otherwise. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Long): boolean
```

Checks if this instance value is greater than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public isGreaterThan(other: Long): boolean--><!--Device-Long-public isGreaterThan(other: Long): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than provided, false otherwise. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Long): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public isLessEqualThan(other: Long): boolean--><!--Device-Long-public isLessEqualThan(other: Long): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than or equal to provided, false otherwise. |

## isLessThan

```TypeScript
public isLessThan(other: Long): boolean
```

Checks if this instance value is less than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public isLessThan(other: Long): boolean--><!--Device-Long-public isLessThan(other: Long): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than provided, false otherwise. |

## mul

```TypeScript
public mul(other: Long): Long
```

Performs integral multiplication of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public mul(other: Long): Long--><!--Device-Long-public mul(other: Long): Long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the multiplication. |

**Return value:**

| Type | Description |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): long
```

Parses from String an integer of specified radix.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static parseInt(s: string, r: int): long--><!--Device-Long-public static parseInt(s: string, r: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert. |
| r | int | Yes | the radix of conversion; should be [2, 36]; 0 assumed to be 10. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the result of parsing. |

## sub

```TypeScript
public sub(other: Long): Long
```

Performs integral subtraction of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public sub(other: Long): Long--><!--Device-Long-public sub(other: Long): Long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | Yes | Right hand side of the subtraction. |

**Return value:**

| Type | Description |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | Result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance as byte.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toByte(): byte--><!--Device-Long-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: long): byte
```

Returns the primitive as byte value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static toByte(value: long): byte--><!--Device-Long-public static toByte(value: long): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | casted value. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance as char.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toChar(): char--><!--Device-Long-public toChar(): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| char | value as char. |

## toChar

```TypeScript
public static toChar(value: long): char
```

Returns the primitive as char value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static toChar(value: long): char--><!--Device-Long-public static toChar(value: long): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| char | casted value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance as double.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toDouble(): double--><!--Device-Long-public toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: long): double
```

Returns the primitive as double value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static toDouble(value: long): double--><!--Device-Long-public static toDouble(value: long): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| double | casted value. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance as float.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toFloat(): float--><!--Device-Long-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: long): float
```

Returns the primitive as float value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static toFloat(value: long): float--><!--Device-Long-public static toFloat(value: long): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| float | casted value. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance as int.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toInt(): int--><!--Device-Long-public toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | value as int. |

## toInt

```TypeScript
public static toInt(value: long): int
```

Returns the primitive as int value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static toInt(value: long): int--><!--Device-Long-public static toInt(value: long): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| int | casted value. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | Intl.NumberFormatOptions | No | An object with some or all of the properties of the Intl.NumberFormat options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the locale-specific conversion |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | No | An object with some or all of the properties of the Intl.NumberFormat options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the locale-specific conversion |

## toLong

```TypeScript
toLong(): long
```

Returns value of this instance

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-toLong(): long--><!--Device-Long-toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | value as long |

## toLong

```TypeScript
static toLong(value: long): long
```

Returns the primitive as long value

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-static toLong(value: long): long--><!--Device-Long-static toLong(value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast |

**Return value:**

| Type | Description |
| --- | --- |
| long | casted value |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance as short.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toShort(): short--><!--Device-Long-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: long): short
```

Returns the primitive as short value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static toShort(value: long): short--><!--Device-Long-public static toShort(value: long): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
static toString(v: long): string
```

Converts the primitive to a string

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-static toString(v: long): string--><!--Device-Long-static toString(v: long): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | long | Yes | value to be converted |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion |

## toString

```TypeScript
toString(): string
```

Converts this object to a string

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-toString(): string--><!--Device-Long-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | Input parameter error. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string with specified radix.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toString(radix: int): string--><!--Device-Long-public toString(radix: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | int | Yes | the radix of conversion. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(radix: double): string
```

Converts this object to a string with specified radix.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public toString(radix: double): string--><!--Device-Long-public toString(radix: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | double | Yes | the radix of conversion. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 64
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static BIT_SIZE: byte = 64--><!--Device-Long-public static BIT_SIZE: byte = 64-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 8
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static BYTE_SIZE: byte = 8--><!--Device-Long-public static BYTE_SIZE: byte = 8-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: long = 9223372036854775807
```

Maximal value that this type can have as a long.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static MAX_VALUE: long = 9223372036854775807--><!--Device-Long-public static MAX_VALUE: long = 9223372036854775807-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: long = -9223372036854775808
```

Minimal value that this type can have as a long.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Long-public static MIN_VALUE: long = -9223372036854775808--><!--Device-Long-public static MIN_VALUE: long = -9223372036854775808-End-->

**System capability:** SystemCapability.Utils.Lang

