# Float

Represents boxed float value and related operations.

**Inheritance/Implementation:** Float extends [Floating](arkts-arkts-numeric-floating-c.md) and implements Comparable<Float>

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class Float--><!--Device-unnamed-export class Float-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## add

```TypeScript
public add(other: Float): Float
```

Performs floating point addition with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public add(other: Float): Float--><!--Device-Float-public add(other: Float): Float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the addition. |

**Return value:**

| Type | Description |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the addition. |

## bitCastFromInt

```TypeScript
public static bitCastFromInt(bits: int): float
```

Converts bit representation to corresponding IEEE-754 floating point representation.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static bitCastFromInt(bits: int): float--><!--Device-Float-public static bitCastFromInt(bits: int): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | int | Yes | bits to convert. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| float | converted value. |

## bitCastToInt

```TypeScript
public static bitCastToInt(val: float): int
```

Converts IEEE-754 floating point representation to corresponding bit representation.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static bitCastToInt(val: float): int--><!--Device-Float-public static bitCastToInt(val: float): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | float | Yes | value to convert. |

**Return value:**

| Type | Description |
| --- | --- |
| int | bit representation. |

## compare

```TypeScript
public static compare(lhs: float, rhs: float): boolean
```

Compares two floats to see if they differ by at most DELTA.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static compare(lhs: float, rhs: float): boolean--><!--Device-Float-public static compare(lhs: float, rhs: float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lhs | float | Yes | left-hand side float for comparison. |
| rhs | float | Yes | right-hand side float for comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if equal with respect to DELTA. |

## compareTo

```TypeScript
public compareTo(other: Float): int
```

Compares this instance to other Float object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public compareTo(other: Float): int--><!--Device-Float-public compareTo(other: Float): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | Float object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | result of the comparison (-1, 0, or 1). |

## constructor

```TypeScript
public constructor()
```

Constructs a new Float instance with initial value zero.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public constructor()--><!--Device-Float-public constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: float)
```

Constructs a new Float instance with provided initial value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public constructor(value: float)--><!--Device-Float-public constructor(value: float)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | the initial value. |

## constructor

```TypeScript
public constructor(value: double)
```

Constructs a new Float instance with provided initial value (double type literal).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public constructor(value: double)--><!--Device-Float-public constructor(value: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | the initial value. |

## div

```TypeScript
public div(other: Float): Float
```

Performs floating point division with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public div(other: Float): Float--><!--Device-Float-public div(other: Float): Float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the division. |

**Return value:**

| Type | Description |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality with provided object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public equals(other: Any): boolean--><!--Device-Float-public equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | object to be checked against. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if equal, false otherwise. |

## isFinite

```TypeScript
public static isFinite(v: float): boolean
```

Checks if float is a finite floating point value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static isFinite(v: float): boolean--><!--Device-Float-public static isFinite(v: float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | float | Yes | the float to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is finite. |

## isFinite

```TypeScript
public isFinite(): boolean
```

Checks if the underlying float is a finite floating point value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isFinite(): boolean--><!--Device-Float-public isFinite(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying float is finite. |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Float): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isGreaterEqualThan(other: Float): boolean--><!--Device-Float-public isGreaterEqualThan(other: Float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than or equal to provided. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Float): boolean
```

Checks if this instance value is greater than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isGreaterThan(other: Float): boolean--><!--Device-Float-public isGreaterThan(other: Float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than provided. |

## isInteger

```TypeScript
public static isInteger(v: float): boolean
```

Checks if float is similar to an integer value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static isInteger(v: float): boolean--><!--Device-Float-public static isInteger(v: float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | float | Yes | the float to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is similar to an integer. |

## isInteger

```TypeScript
public isInteger(): boolean
```

Checks if the underlying float is similar to an integer value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isInteger(): boolean--><!--Device-Float-public isInteger(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying float is similar to an integer. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Float): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isLessEqualThan(other: Float): boolean--><!--Device-Float-public isLessEqualThan(other: Float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than or equal to provided. |

## isLessThan

```TypeScript
public isLessThan(other: Float): boolean
```

Checks if this instance value is less than value of provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isLessThan(other: Float): boolean--><!--Device-Float-public isLessThan(other: Float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than provided. |

## isNaN

```TypeScript
public static isNaN(v: float): boolean
```

Checks if float is NaN.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static isNaN(v: float): boolean--><!--Device-Float-public static isNaN(v: float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | float | Yes | the float to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is NaN. |

## isNaN

```TypeScript
public isNaN(): boolean
```

Checks if the underlying float is NaN.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isNaN(): boolean--><!--Device-Float-public isNaN(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying float is NaN. |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: float): boolean
```

Checks if float is a safe integer value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static isSafeInteger(v: float): boolean--><!--Device-Float-public static isSafeInteger(v: float): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | float | Yes | the float to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is a safe integer. |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

Checks if the underlying float is a safe integer value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public isSafeInteger(): boolean--><!--Device-Float-public isSafeInteger(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying float is a safe integer. |

## mul

```TypeScript
public mul(other: Float): Float
```

Performs floating point multiplication with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public mul(other: Float): Float--><!--Device-Float-public mul(other: Float): Float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the multiplication. |

**Return value:**

| Type | Description |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the multiplication. |

## sub

```TypeScript
public sub(other: Float): Float
```

Performs floating point subtraction with provided instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public sub(other: Float): Float--><!--Device-Float-public sub(other: Float): Float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | Yes | right hand side of the subtraction. |

**Return value:**

| Type | Description |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toByte(): byte--><!--Device-Float-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: float): byte
```

Returns the primitive as byte value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toByte(value: float): byte--><!--Device-Float-public static toByte(value: float): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | casted value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toDouble(): double--><!--Device-Float-public toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: float): double
```

Returns the primitive as double value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toDouble(value: float): double--><!--Device-Float-public static toDouble(value: float): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to cast. |

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

<!--Device-Float-public toFloat(): float--><!--Device-Float-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: float): float
```

Returns the primitive as float value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toFloat(value: float): float--><!--Device-Float-public static toFloat(value: float): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| float | casted value. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toInt(): int--><!--Device-Float-public toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | value as int. |

## toInt

```TypeScript
public static toInt(value: float): int
```

Returns the primitive as int value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toInt(value: float): int--><!--Device-Float-public static toInt(value: float): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| int | casted value. |

## toLocaleString

```TypeScript
public toLocaleString(): string
```

Converts this object to a locale-specific string representation.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toLocaleString(): string--><!--Device-Float-public toLocaleString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the locale-specific conversion. |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toLong(): long--><!--Device-Float-public toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | value as long. |

## toLong

```TypeScript
public static toLong(value: float): long
```

Returns the primitive as long value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toLong(value: float): long--><!--Device-Float-public static toLong(value: float): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to cast. |

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

<!--Device-Float-public toShort(): short--><!--Device-Float-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: float): short
```

Returns the primitive as short value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toShort(value: float): short--><!--Device-Float-public static toShort(value: float): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
public static toString(f: float, r: int): string
```

Returns a string representation of float by radix r.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toString(f: float, r: int): string--><!--Device-Float-public static toString(f: float, r: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| f | float | Yes | the float value. |
| r | int | Yes | the radix. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public static toString(f: float): string
```

Returns a string representation of float in base 10.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static toString(f: float): string--><!--Device-Float-public static toString(f: float): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| f | float | Yes | the float value. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public toString(r: int): string
```

Converts this object to a string in the given radix.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toString(r: int): string--><!--Device-Float-public toString(r: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| r | int | Yes | the radix. <br>The value should be an integer. |

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public toString(): string--><!--Device-Float-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 32
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static BIT_SIZE: byte = 32--><!--Device-Float-public static BIT_SIZE: byte = 32-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 4
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static BYTE_SIZE: byte = 4--><!--Device-Float-public static BYTE_SIZE: byte = 4-End-->

**System capability:** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static DELTA: float = Float.bitCastFromInt(0x34000000)
```

Minimal possible difference between two float values.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static DELTA: float = Float.bitCastFromInt(0x34000000)--><!--Device-Float-public static DELTA: float = Float.bitCastFromInt(0x34000000)-End-->

**System capability:** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static EPSILON: float = Float.DELTA
```

Minimal possible difference between two float values.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static EPSILON: float = Float.DELTA--><!--Device-Float-public static EPSILON: float = Float.DELTA-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_SAFE_INTEGER

```TypeScript
public static MAX_SAFE_INTEGER: float = 16777215
```

Maximal integer value that can be used as a float without loss of precision.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static MAX_SAFE_INTEGER: float = 16777215--><!--Device-Float-public static MAX_SAFE_INTEGER: float = 16777215-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: float = 3.40282346638528860e+38
```

Maximal value that this type can have as a float.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static MAX_VALUE: float = 3.40282346638528860e+38--><!--Device-Float-public static MAX_VALUE: float = 3.40282346638528860e+38-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: float = 1.4e-45
```

Minimal value that this type can have as a float.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static MIN_VALUE: float = 1.4e-45--><!--Device-Float-public static MIN_VALUE: float = 1.4e-45-End-->

**System capability:** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)
```

Represents the -Infinity value according to IEEE-754 specification.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)--><!--Device-Float-public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)-End-->

**System capability:** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static NaN: float = Double.toFloat(0.0 / 0.0)
```

Represents the NaN value according to IEEE-754 specification.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static NaN: float = Double.toFloat(0.0 / 0.0)--><!--Device-Float-public static NaN: float = Double.toFloat(0.0 / 0.0)-End-->

**System capability:** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)
```

Represents the +Infinity value according to IEEE-754 specification.

**Type:** float

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)--><!--Device-Float-public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)-End-->

**System capability:** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static PRECISION: byte = 24
```

Number of significant precision bits in this floating type.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float-public static PRECISION: byte = 24--><!--Device-Float-public static PRECISION: byte = 24-End-->

**System capability:** SystemCapability.Utils.Lang

## f

```TypeScript
f
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-Float-f--><!--Device-Float-f-End-->

