# Byte

Represents boxed byte value and related operations

**Inheritance/Implementation:** Byte extends [Integral](arkts-arkts-numeric-integral-c.md) and implements Comparable<Byte>

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class Byte--><!--Device-unnamed-export class Byte-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## add

```TypeScript
public add(other: Byte): Byte
```

Performs integral addition of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public add(other: Byte): Byte--><!--Device-Byte-public add(other: Byte): Byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the addition. |

**Return value:**

| Type | Description |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of addition. |

## compareTo

```TypeScript
public compareTo(other: Byte): int
```

Compares this instance to other Byte object The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public compareTo(other: Byte): int--><!--Device-Byte-public compareTo(other: Byte): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Byte object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the comparison result. |

## constructor

```TypeScript
public constructor()
```

Constructs a new Byte instance with initial value zero

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public constructor()--><!--Device-Byte-public constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: byte)
```

Constructs a new Byte instance with provided initial value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public constructor(value: byte)--><!--Device-Byte-public constructor(value: byte)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | the initial value. |

## div

```TypeScript
public div(other: Byte): Byte
```

Performs integral division of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public div(other: Byte): Byte--><!--Device-Byte-public div(other: Byte): Byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the division. |

**Return value:**

| Type | Description |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Byte Returns false if type of provided object is not the same as this type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public equals(other: Any): boolean--><!--Device-Byte-public equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | object to be checked against. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if equal, false otherwise. |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Byte): boolean
```

Checks if this instance value is greater than or equal to value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public isGreaterEqualThan(other: Byte): boolean--><!--Device-Byte-public isGreaterEqualThan(other: Byte): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this instance is greater than or equal to other. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Byte): boolean
```

Checks if this instance value is greater than value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public isGreaterThan(other: Byte): boolean--><!--Device-Byte-public isGreaterThan(other: Byte): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this instance is greater than other. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Byte): boolean
```

Checks if this instance value is less than or equal to value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public isLessEqualThan(other: Byte): boolean--><!--Device-Byte-public isLessEqualThan(other: Byte): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this instance is less than or equal to other. |

## isLessThan

```TypeScript
public isLessThan(other: Byte): boolean
```

Checks if this instance value is less than value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public isLessThan(other: Byte): boolean--><!--Device-Byte-public isLessThan(other: Byte): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this instance is less than other. |

## mul

```TypeScript
public mul(other: Byte): Byte
```

Performs integral multiplication of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public mul(other: Byte): Byte--><!--Device-Byte-public mul(other: Byte): Byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the multiplication. |

**Return value:**

| Type | Description |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): byte
```

Parses a string to a byte value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static parseInt(s: string, r: int): byte--><!--Device-Byte-public static parseInt(s: string, r: int): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | The string to parse. |
| r | int | Yes | The radix of the string. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | The parsed byte value. |

## sub

```TypeScript
public sub(other: Byte): Byte
```

Performs integral subtraction of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public sub(other: Byte): Byte--><!--Device-Byte-public sub(other: Byte): Byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | Yes | Right hand side of the subtraction. |

**Return value:**

| Type | Description |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | the result of subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toByte(): byte--><!--Device-Byte-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | the byte value. |

## toByte

```TypeScript
public static toByte(value: byte): byte
```

Returns the primitive as byte value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toByte(value: byte): byte--><!--Device-Byte-public static toByte(value: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the byte value. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toChar(): char--><!--Device-Byte-public toChar(): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| char | the char value. |

## toChar

```TypeScript
public static toChar(value: byte): char
```

Returns the primitive as char value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toChar(value: byte): char--><!--Device-Byte-public static toChar(value: byte): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the char value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toDouble(): double--><!--Device-Byte-public toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | the double value. |

## toDouble

```TypeScript
public static toDouble(value: byte): double
```

Returns the primitive as double value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toDouble(value: byte): double--><!--Device-Byte-public static toDouble(value: byte): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the double value. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toFloat(): float--><!--Device-Byte-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | the float value. |

## toFloat

```TypeScript
public static toFloat(value: byte): float
```

Returns the primitive as float value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toFloat(value: byte): float--><!--Device-Byte-public static toFloat(value: byte): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| float | the float value. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toInt(): int--><!--Device-Byte-public toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the int value. |

## toInt

```TypeScript
public static toInt(value: byte): int
```

Returns the primitive as int value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toInt(value: byte): int--><!--Device-Byte-public static toInt(value: byte): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the int value. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | Intl.NumberFormatOptions | No | An object with some or all of the properties of the Intl.NumberFormat options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the elements of the array. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | No | An object with configuration properties. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the elements of the array. |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toLong(): long--><!--Device-Byte-public toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | the long value. |

## toLong

```TypeScript
public static toLong(value: byte): long
```

Returns the primitive as long value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toLong(value: byte): long--><!--Device-Byte-public static toLong(value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the long value. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toShort(): short--><!--Device-Byte-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | the short value. |

## toShort

```TypeScript
public static toShort(value: byte): short
```

Returns the primitive as short value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toShort(value: byte): short--><!--Device-Byte-public static toShort(value: byte): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the short value. |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toString(): string--><!--Device-Byte-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public static toString(v: byte): string
```

Converts the primitive to a string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static toString(v: byte): string--><!--Device-Byte-public static toString(v: byte): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | byte | Yes | value to be converted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toString(radix: int): string--><!--Device-Byte-public toString(radix: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | int | Yes | to use for conversion. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public toString(radix: double): string
```

Converts this object to a string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public toString(radix: double): string--><!--Device-Byte-public toString(radix: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | double | Yes | to use for conversion. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 8
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static BIT_SIZE: byte = 8--><!--Device-Byte-public static BIT_SIZE: byte = 8-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 1
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static BYTE_SIZE: byte = 1--><!--Device-Byte-public static BYTE_SIZE: byte = 1-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: byte = 127
```

Maximal value that this type can have as an integral.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static MAX_VALUE: byte = 127--><!--Device-Byte-public static MAX_VALUE: byte = 127-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: byte = -128
```

Minimal value that this type can have as an integral.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Byte-public static MIN_VALUE: byte = -128--><!--Device-Byte-public static MIN_VALUE: byte = -128-End-->

**System capability:** SystemCapability.Utils.Lang

