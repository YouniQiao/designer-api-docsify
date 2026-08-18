# BigInt

JS BigInt API-compatible class.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class BigInt--><!--Device-unnamed-export class BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(value: BigInt): BigInt
```

Creates a new instance of BigInt from existing BigInt number

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-static $_invoke(value: BigInt): BigInt--><!--Device-BigInt-static $_invoke(value: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BigInt](arkts-na-bigint-c.md) | Yes | BigInt value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A new BigInt instance from existing BigInt number |

## $_invoke

```TypeScript
static $_invoke(value: long): BigInt
```

Creates a new instance of BigInt from existing Long number

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-static $_invoke(value: long): BigInt--><!--Device-BigInt-static $_invoke(value: long): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | BigInt value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A new BigInt instance from existing Long number |

## $_invoke

```TypeScript
static $_invoke(value: double): BigInt
```

Creates a new instance of BigInt from number instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-static $_invoke(value: double): BigInt--><!--Device-BigInt-static $_invoke(value: double): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | number value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A new BigInt instance from number instance |

## $_invoke

```TypeScript
static $_invoke(value: string): BigInt
```

Creates a new instance of BigInt from string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-static $_invoke(value: string): BigInt--><!--Device-BigInt-static $_invoke(value: string): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | string value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A new BigInt instance from string |

## $_invoke

```TypeScript
static $_invoke(value: boolean): BigInt
```

Creates a new instance of BigInt from boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-static $_invoke(value: boolean): BigInt--><!--Device-BigInt-static $_invoke(value: boolean): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | boolean value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A new BigInt instance from boolean |

## $_invoke

```TypeScript
static $_invoke(value: bigint | double | string | boolean): BigInt
```

Creates a new instance of BigInt from union of bigint/double/string/boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-static $_invoke(value: bigint | double | string | boolean): BigInt--><!--Device-BigInt-static $_invoke(value: bigint | double | string | boolean): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint \| double \| string \| boolean | Yes | source value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A new BigInt instance from union of bigint/double/string/boolean |

## asIntN

```TypeScript
public static asIntN(bits: long, num: BigInt): BigInt
```

Clamps a BigInt to a signed integer with the specified number of bits.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public static asIntN(bits: long, num: BigInt): BigInt--><!--Device-BigInt-public static asIntN(bits: long, num: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | long | Yes | The number of bits for the signed integer representation. |
| num | [BigInt](arkts-na-bigint-c.md) | Yes | The BigInt value to clamp. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A BigInt value clamped to the specified number of bits as a signed integer. |

## asUintN

```TypeScript
public static asUintN(bits: long, num: BigInt): BigInt
```

Clamps a BigInt to an unsigned integer with the specified number of bits.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public static asUintN(bits: long, num: BigInt): BigInt--><!--Device-BigInt-public static asUintN(bits: long, num: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | long | Yes | The number of bits for the unsigned integer representation. |
| num | [BigInt](arkts-na-bigint-c.md) | Yes | The BigInt value to clamp. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | A BigInt value clamped to the specified number of bits as an unsigned integer. |

## constructor

```TypeScript
constructor()
```

Creates a new `BigInt` instance with value 0.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor()--><!--Device-BigInt-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(d: byte)
```

Creates a new `BigInt` instance from a byte value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: byte)--><!--Device-BigInt-constructor(d: byte)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | byte | Yes | The byte value to convert. |

## constructor

```TypeScript
constructor(d: short)
```

Creates a new `BigInt` instance from a short value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: short)--><!--Device-BigInt-constructor(d: short)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | short | Yes | The short value to convert. |

## constructor

```TypeScript
constructor(d: int)
```

Creates a new `BigInt` instance from an int value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: int)--><!--Device-BigInt-constructor(d: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | int | Yes | The int value to convert. <br>The value should be an integer. |

## constructor

```TypeScript
constructor(d: long)
```

Creates a new `BigInt` instance from a long value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: long)--><!--Device-BigInt-constructor(d: long)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | long | Yes | The long value to convert. |

## constructor

```TypeScript
constructor(d: double)
```

Creates a new `BigInt` instance from a double value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: double)--><!--Device-BigInt-constructor(d: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | Yes | The double value to convert to BigInt. Must be an integer. |

## constructor

```TypeScript
constructor(d: string)
```

Creates a new `BigInt` instance from a string value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: string)--><!--Device-BigInt-constructor(d: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | string | Yes | The string value to convert to BigInt. |

## constructor

```TypeScript
constructor(d: boolean)
```

Creates a new `BigInt` instance from a boolean value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: boolean)--><!--Device-BigInt-constructor(d: boolean)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | boolean | Yes | The boolean value (true=1, false=0). |

## constructor

```TypeScript
constructor(d: BigInt)
```

Creates a new `BigInt` instance by copying another BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(d: BigInt)--><!--Device-BigInt-constructor(d: BigInt)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | [BigInt](arkts-na-bigint-c.md) | Yes | The BigInt object to copy. |

## constructor

```TypeScript
constructor(v: FixedArray<int>, sign: int)
```

Creates a new `BigInt` instance from internal components.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-constructor(v: FixedArray<int>, sign: int)--><!--Device-BigInt-constructor(v: FixedArray<int>, sign: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | FixedArray&lt;int&gt; | Yes | The array of digits. |
| sign | int | Yes | The sign of the number. <br>The value should be an integer. |

## doubleValue

```TypeScript
public doubleValue(): double
```

Returns the value of an object as a double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public doubleValue(): double--><!--Device-BigInt-public doubleValue(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | The double value. |

## equals

```TypeScript
public equals(to: BigInt): boolean
```

Checks if this BigInt is equal to another BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public equals(to: BigInt): boolean--><!--Device-BigInt-public equals(to: BigInt): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| to | [BigInt](arkts-na-bigint-c.md) | Yes | The BigInt to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if equal, false otherwise. |

## equals

```TypeScript
equals(other: Any): boolean
```

Checks if this BigInt is equal to another value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-equals(other: Any): boolean--><!--Device-BigInt-equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | The value to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is a BigInt and equal to this BigInt, false otherwise. |

## fromULong

```TypeScript
public static fromULong(val: long): BigInt
```

Creates a BigInt from an unsigned long value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public static fromULong(val: long): BigInt--><!--Device-BigInt-public static fromULong(val: long): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | The unsigned long value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The new BigInt instance. |

## getLong

```TypeScript
public getLong(): long
```

Returns the value of an object as a long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public getLong(): long--><!--Device-BigInt-public getLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | The long value. |

## getULong

```TypeScript
public getULong(): long
```

Return current value clipped to unsigned long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public getULong(): long--><!--Device-BigInt-public getULong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | The unsigned long value. |

## negate

```TypeScript
public negate(): BigInt
```

Returns the negation of the BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public negate(): BigInt--><!--Device-BigInt-public negate(): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The negated value. |

## negative

```TypeScript
public negative(): boolean
```

Returns whether the BigInt is negative.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public negative(): boolean--><!--Device-BigInt-public negative(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if negative, false otherwise. |

## operatorAdd

```TypeScript
public operatorAdd(other: BigInt): BigInt
```

Adds another BigInt to this one.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorAdd(other: BigInt): BigInt--><!--Device-BigInt-public operatorAdd(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the addition. |

## operatorBitwiseAnd

```TypeScript
public operatorBitwiseAnd(other: BigInt): BigInt
```

Performs bitwise AND operation with another BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorBitwiseAnd(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseAnd(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The other BigInt. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the bitwise AND. |

## operatorBitwiseNot

```TypeScript
public operatorBitwiseNot(): BigInt
```

Performs bitwise NOT operation on the BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorBitwiseNot(): BigInt--><!--Device-BigInt-public operatorBitwiseNot(): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the bitwise NOT. |

## operatorBitwiseOr

```TypeScript
public operatorBitwiseOr(other: BigInt): BigInt
```

Performs bitwise OR operation with another BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorBitwiseOr(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseOr(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The other BigInt. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the bitwise OR. |

## operatorBitwiseXor

```TypeScript
public operatorBitwiseXor(other: BigInt): BigInt
```

Performs bitwise XOR operation with another BigInt.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorBitwiseXor(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseXor(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The other BigInt. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the bitwise XOR. |

## operatorDecrement

```TypeScript
public operatorDecrement(): BigInt
```

Decrements the BigInt value by 1.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorDecrement(): BigInt--><!--Device-BigInt-public operatorDecrement(): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The decremented value. |

## operatorDivide

```TypeScript
public operatorDivide(other: BigInt): BigInt
```

Divides this BigInt by another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorDivide(other: BigInt): BigInt--><!--Device-BigInt-public operatorDivide(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The divisor. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The quotient of the division. |

## operatorGreaterThan

```TypeScript
public operatorGreaterThan(other: BigInt): boolean
```

Checks if this BigInt is greater than another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorGreaterThan(other: BigInt): boolean--><!--Device-BigInt-public operatorGreaterThan(other: BigInt): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The value to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if this is greater than other, false otherwise. |

## operatorGreaterThanEqual

```TypeScript
public operatorGreaterThanEqual(other: BigInt): boolean
```

Checks if this BigInt is greater than or equal to another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorGreaterThanEqual(other: BigInt): boolean--><!--Device-BigInt-public operatorGreaterThanEqual(other: BigInt): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The value to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if this is greater than or equal to other, false otherwise. |

## operatorIncrement

```TypeScript
public operatorIncrement(): BigInt
```

Increments the BigInt value by 1.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorIncrement(): BigInt--><!--Device-BigInt-public operatorIncrement(): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The incremented value. |

## operatorLeftShift

```TypeScript
public operatorLeftShift(other: BigInt): BigInt
```

Shifts the BigInt to the left by a specified number of bits.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorLeftShift(other: BigInt): BigInt--><!--Device-BigInt-public operatorLeftShift(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The number of bits to shift. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The shifted BigInt. |

## operatorLessThan

```TypeScript
public operatorLessThan(other: BigInt): boolean
```

Checks if this BigInt is less than another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorLessThan(other: BigInt): boolean--><!--Device-BigInt-public operatorLessThan(other: BigInt): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The value to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if this is less than other, false otherwise. |

## operatorLessThanEqual

```TypeScript
public operatorLessThanEqual(other: BigInt): boolean
```

Checks if this BigInt is less than or equal to another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorLessThanEqual(other: BigInt): boolean--><!--Device-BigInt-public operatorLessThanEqual(other: BigInt): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The value to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if this is less than or equal to other, false otherwise. |

## operatorModule

```TypeScript
public operatorModule(other: BigInt): BigInt
```

Calculates the remainder of division of this BigInt by another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorModule(other: BigInt): BigInt--><!--Device-BigInt-public operatorModule(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The divisor. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The remainder. |

## operatorMultiply

```TypeScript
public operatorMultiply(other: BigInt): BigInt
```

Multiplies this BigInt by another.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorMultiply(other: BigInt): BigInt--><!--Device-BigInt-public operatorMultiply(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The multiplier. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the multiplication. |

## operatorRightShift

```TypeScript
public operatorRightShift(other: BigInt): BigInt
```

Shifts the BigInt to the right by a specified number of bits.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorRightShift(other: BigInt): BigInt--><!--Device-BigInt-public operatorRightShift(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The number of bits to shift. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The shifted BigInt. |

## operatorSubtract

```TypeScript
public operatorSubtract(other: BigInt): BigInt
```

Subtracts another BigInt from this one.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public operatorSubtract(other: BigInt): BigInt--><!--Device-BigInt-public operatorSubtract(other: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [BigInt](arkts-na-bigint-c.md) | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of the subtraction. |

## positive

```TypeScript
public positive(): boolean
```

Returns whether the BigInt is positive.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public positive(): boolean--><!--Device-BigInt-public positive(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if positive (including zero), false otherwise. |

## pow

```TypeScript
public pow(exponent: BigInt): BigInt
```

Returns the base to the exponent power.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public pow(exponent: BigInt): BigInt--><!--Device-BigInt-public pow(exponent: BigInt): BigInt-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exponent | [BigInt](arkts-na-bigint-c.md) | Yes | The exponent value. |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt](arkts-na-bigint-c.md) | The result of base^exponent. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

Converts a number to a string by using the current or specified locale.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string--><!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | [BigIntToLocaleStringOptions](arkts-na-bigint-biginttolocalestringoptions-i.md) | No | An object with some or all of the properties of the Intl.NumberFormat options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the BigInt formatted according to the locale and options. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

## toString

```TypeScript
public toString(): string
```

Converts the BigInt to a string in base 10.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public toString(): string--><!--Device-BigInt-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representation of the BigInt in base 10. |

## toString

```TypeScript
public toString(radix: int): string
```

Returns a string representation of the BigInt object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BigInt-public toString(radix: int): string--><!--Device-BigInt-public toString(radix: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | int | Yes | An integer in the range 2 through 36 specifying the base to use for representing numeric values. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the specified BigInt object. |

