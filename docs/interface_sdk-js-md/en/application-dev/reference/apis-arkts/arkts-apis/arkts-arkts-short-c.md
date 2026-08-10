# Short

Represents boxed short value and related operations

**Inheritance/Implementation:** Short extends [Integral](arkts-arkts-numeric-integral-c.md) and implements [Comparable<Short>](Comparable<Short>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class Short extends Integral implements Comparable<Short>--><!--Device-unnamed-export class Short extends Integral implements Comparable<Short>-End-->

**System capability:** SystemCapability.Utils.Lang

## add

```TypeScript
public add(other: Short): Short
```

Performs integral addition of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public add(other: Short): Short--><!--Device-Short-public add(other: Short): Short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the addition. |

**Return value:**

| Type | Description |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the addition. |

## compareTo

```TypeScript
public compareTo(other: Short): int
```

Compares this instance to other Short object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public compareTo(other: Short): int--><!--Device-Short-public compareTo(other: Short): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Short object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | result of the comparison, -1 if this instance is less than provided object, 0 if equal, 1 if greater. |

## constructor

```TypeScript
public constructor()
```

Constructs a new Short instance with initial value zero.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public constructor()--><!--Device-Short-public constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: short)
```

Constructs a new Short instance with provided initial value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public constructor(value: short)--><!--Device-Short-public constructor(value: short)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | the initial value. |

## div

```TypeScript
public div(other: Short): Short
```

Performs integral division of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public div(other: Short): Short--><!--Device-Short-public div(other: Short): Short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the division. |

**Return value:**

| Type | Description |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Short.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public equals(other: Any): boolean--><!--Device-Short-public equals(other: Any): boolean-End-->

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
public isGreaterEqualThan(other: Short): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public isGreaterEqualThan(other: Short): boolean--><!--Device-Short-public isGreaterEqualThan(other: Short): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than or equal to provided, false otherwise. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Short): boolean
```

Checks if this instance value is greater than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public isGreaterThan(other: Short): boolean--><!--Device-Short-public isGreaterThan(other: Short): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than provided, false otherwise. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Short): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public isLessEqualThan(other: Short): boolean--><!--Device-Short-public isLessEqualThan(other: Short): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than or equal to provided, false otherwise. |

## isLessThan

```TypeScript
public isLessThan(other: Short): boolean
```

Checks if this instance value is less than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public isLessThan(other: Short): boolean--><!--Device-Short-public isLessThan(other: Short): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than provided, false otherwise. |

## mul

```TypeScript
public mul(other: Short): Short
```

Performs integral multiplication of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public mul(other: Short): Short--><!--Device-Short-public mul(other: Short): Short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the multiplication. |

**Return value:**

| Type | Description |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): short
```

Parses from string an integer of specified radix.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static parseInt(s: string, r: int): short--><!--Device-Short-public static parseInt(s: string, r: int): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert. |
| r | int | Yes | the radix of conversion; should be [2, 36]; 0 assumed to be 10. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the result of parsing. |

## sub

```TypeScript
public sub(other: Short): Short
```

Performs integral subtraction of this instance with provided one, returns the result as new instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public sub(other: Short): Short--><!--Device-Short-public sub(other: Short): Short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Short](arkts-arkts-short-c.md) | Yes | Right hand side of the subtraction. |

**Return value:**

| Type | Description |
| --- | --- |
| [Short](arkts-arkts-short-c.md) | Result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance as byte.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toByte(): byte--><!--Device-Short-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: short): byte
```

Returns the primitive as byte value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toByte(value: short): byte--><!--Device-Short-public static toByte(value: short): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toChar(): char--><!--Device-Short-public toChar(): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| char | value as char. |

## toChar

```TypeScript
public static toChar(value: short): char
```

Returns the primitive as char value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toChar(value: short): char--><!--Device-Short-public static toChar(value: short): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toDouble(): double--><!--Device-Short-public toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: short): double
```

Returns the primitive as double value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toDouble(value: short): double--><!--Device-Short-public static toDouble(value: short): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toFloat(): float--><!--Device-Short-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: short): float
```

Returns the primitive as float value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toFloat(value: short): float--><!--Device-Short-public static toFloat(value: short): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toInt(): int--><!--Device-Short-public toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | value as int. |

## toInt

```TypeScript
public static toInt(value: short): int
```

Returns the primitive as int value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toInt(value: short): int--><!--Device-Short-public static toInt(value: short): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
public toLong(): long
```

Returns value of this instance as long.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toLong(): long--><!--Device-Short-public toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | value as long. |

## toLong

```TypeScript
public static toLong(value: short): long
```

Returns the primitive as long value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toLong(value: short): long--><!--Device-Short-public static toLong(value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| long | casted value. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance as short.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toShort(): short--><!--Device-Short-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: short): short
```

Returns the primitive as short value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toShort(value: short): short--><!--Device-Short-public static toShort(value: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
public static toString(v: short): string
```

Converts the primitive to a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static toString(v: short): string--><!--Device-Short-public static toString(v: short): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | short | Yes | value to be converted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toString(): string--><!--Device-Short-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string with specified radix.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toString(radix: int): string--><!--Device-Short-public toString(radix: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | int | Yes | the radix of conversion. &lt;br&gt;The value should be an integer. |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public toString(radix: double): string--><!--Device-Short-public toString(radix: double): string-End-->

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
public static BIT_SIZE: byte = 16
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static BIT_SIZE: byte = 16--><!--Device-Short-public static BIT_SIZE: byte = 16-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 2
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static BYTE_SIZE: byte = 2--><!--Device-Short-public static BYTE_SIZE: byte = 2-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: short = 32767
```

Maximal value that this type can have as a short.

**Type:** short

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static MAX_VALUE: short = 32767--><!--Device-Short-public static MAX_VALUE: short = 32767-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: short = -32768
```

Minimal value that this type can have as a short.

**Type:** short

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Short-public static MIN_VALUE: short = -32768--><!--Device-Short-public static MIN_VALUE: short = -32768-End-->

**System capability:** SystemCapability.Utils.Lang

