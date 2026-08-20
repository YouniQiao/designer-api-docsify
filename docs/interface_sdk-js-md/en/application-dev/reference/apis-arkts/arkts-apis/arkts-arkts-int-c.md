# Int

Represents boxed int value and related operations

**Inheritance/Implementation:** Int extends [Integral](arkts-arkts-numeric-integral-c.md) and implements Comparable<Int>

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export class Int--><!--Device-unnamed-export class Int-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## add

```TypeScript
public add(other: Int): Int
```

Performs integral addition with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public add(other: Int): Int--><!--Device-Int-public add(other: Int): Int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the addition. |

**Return value:**

| Type | Description |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the addition. |

## compareTo

```TypeScript
public compareTo(other: Int): int
```

Compares this instance to other Int object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public compareTo(other: Int): int--><!--Device-Int-public compareTo(other: Int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | Int object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | result of the comparison (-1, 0, or 1). |

## constructor

```TypeScript
constructor()
```

Constructs a new Int instance with initial value zero

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-constructor()--><!--Device-Int-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: int)
```

Constructs a new Int instance with provided initial value

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-constructor(value: int)--><!--Device-Int-constructor(value: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | the initial value <br>The value should be an integer. |

## div

```TypeScript
public div(other: Int): Int
```

Performs integral division with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public div(other: Int): Int--><!--Device-Int-public div(other: Int): Int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the division. |

**Return value:**

| Type | Description |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the division. |

## equals

```TypeScript
equals(other: Any): boolean
```

Compares this object with the specified object for equality.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-equals(other: Any): boolean--><!--Device-Int-equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | the object to compare with |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the specified object is equal to this object, false otherwise |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Int): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public isGreaterEqualThan(other: Int): boolean--><!--Device-Int-public isGreaterEqualThan(other: Int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than or equal to provided. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Int): boolean
```

Checks if this instance value is greater than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public isGreaterThan(other: Int): boolean--><!--Device-Int-public isGreaterThan(other: Int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than provided. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Int): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public isLessEqualThan(other: Int): boolean--><!--Device-Int-public isLessEqualThan(other: Int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than or equal to provided. |

## isLessThan

```TypeScript
public isLessThan(other: Int): boolean
```

Checks if this instance value is less than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public isLessThan(other: Int): boolean--><!--Device-Int-public isLessThan(other: Int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than provided. |

## mul

```TypeScript
public mul(other: Int): Int
```

Performs integral multiplication with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public mul(other: Int): Int--><!--Device-Int-public mul(other: Int): Int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the multiplication. |

**Return value:**

| Type | Description |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the multiplication. |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): int
```

Parses from String an integer of specified radix.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static parseInt(s: string, r: int): int--><!--Device-Int-public static parseInt(s: string, r: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert. |
| r | int | Yes | the radix of conversion (2-36). <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the result of parsing. |

## sub

```TypeScript
public sub(other: Int): Int
```

Performs integral subtraction with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public sub(other: Int): Int--><!--Device-Int-public sub(other: Int): Int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | Yes | right hand side of the subtraction. |

**Return value:**

| Type | Description |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toByte(): byte--><!--Device-Int-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: int): byte
```

Returns the primitive as byte value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static toByte(value: int): byte--><!--Device-Int-public static toByte(value: int): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to cast. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | casted value. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toChar(): char--><!--Device-Int-public toChar(): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| char | value as char. |

## toChar

```TypeScript
public static toChar(value: int): char
```

Returns the primitive as char value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static toChar(value: int): char--><!--Device-Int-public static toChar(value: int): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to cast. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| char | casted value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toDouble(): double--><!--Device-Int-public toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: int): double
```

Returns the primitive as double value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static toDouble(value: int): double--><!--Device-Int-public static toDouble(value: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to cast. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| double | casted value. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toFloat(): float--><!--Device-Int-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: int): float
```

Returns the primitive as float value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static toFloat(value: int): float--><!--Device-Int-public static toFloat(value: int): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to cast. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| float | casted value. |

## toInt

```TypeScript
toInt(): int
```

Converts the value of this instance to an int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-toInt(): int--><!--Device-Int-toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the int value represented by this instance |

## toInt

```TypeScript
static toInt(value: int): int
```

Returns the primitive int value directly

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-static toInt(value: int): int--><!--Device-Int-static toInt(value: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | the int value to return <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the same int value that was passed in |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toLong(): long--><!--Device-Int-public toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | value as long. |

## toLong

```TypeScript
public static toLong(value: int): long
```

Returns the primitive as long value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static toLong(value: int): long--><!--Device-Int-public static toLong(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to cast. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | casted value. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toShort(): short--><!--Device-Int-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: int): short
```

Returns the primitive as short value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static toShort(value: int): short--><!--Device-Int-public static toShort(value: int): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to cast. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
static toString(v: int): string
```

Converts the specified int value to its string representation.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-static toString(v: int): string--><!--Device-Int-static toString(v: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | int | Yes | the int value to be converted <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation of the int value |

## toString

```TypeScript
toString(): string
```

Converts the value of this Int object to its string representation.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-toString(): string--><!--Device-Int-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation of this Int object's value |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string in the given radix.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toString(radix: int): string--><!--Device-Int-public toString(radix: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | int | Yes | the radix to use. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## toString

```TypeScript
public toString(radix: double): string
```

Converts this object to a string in the given radix.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public toString(radix: double): string--><!--Device-Int-public toString(radix: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | double | Yes | the radix to use. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 32
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static readonly BIT_SIZE: byte = 32--><!--Device-Int-public static readonly BIT_SIZE: byte = 32-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 4
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static readonly BYTE_SIZE: byte = 4--><!--Device-Int-public static readonly BYTE_SIZE: byte = 4-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: int = 2147483647
```

Maximal value that this type can have as an integral.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static readonly MAX_VALUE: int = 2147483647--><!--Device-Int-public static readonly MAX_VALUE: int = 2147483647-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: int = -2147483648
```

Minimal value that this type can have as an integral.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Int-public static readonly MIN_VALUE: int = -2147483648--><!--Device-Int-public static readonly MIN_VALUE: int = -2147483648-End-->

**System capability:** SystemCapability.Utils.Lang

