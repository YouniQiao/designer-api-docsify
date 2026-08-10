# BigInt

JS BigInt API-compatible class.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class BigInt--><!--Device-unnamed-export class BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(value: BigInt): BigInt
```

Creates a new instance of BigInt from existing BigInt number

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: BigInt): BigInt--><!--Device-BigInt-static $_invoke(value: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 | BigInt value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A new BigInt instance from existing BigInt number |

## $_invoke

```TypeScript
static $_invoke(value: long): BigInt
```

Creates a new instance of BigInt from existing Long number

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: long): BigInt--><!--Device-BigInt-static $_invoke(value: long): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | BigInt value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A new BigInt instance from existing Long number |

## $_invoke

```TypeScript
static $_invoke(value: double): BigInt
```

Creates a new instance of BigInt from number instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: double): BigInt--><!--Device-BigInt-static $_invoke(value: double): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | number value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A new BigInt instance from number instance |

## $_invoke

```TypeScript
static $_invoke(value: string): BigInt
```

Creates a new instance of BigInt from string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: string): BigInt--><!--Device-BigInt-static $_invoke(value: string): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | string value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A new BigInt instance from string |

## $_invoke

```TypeScript
static $_invoke(value: boolean): BigInt
```

Creates a new instance of BigInt from boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: boolean): BigInt--><!--Device-BigInt-static $_invoke(value: boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | boolean value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A new BigInt instance from boolean |

## $_invoke

```TypeScript
static $_invoke(value: bigint | double | string | boolean): BigInt
```

Creates a new instance of BigInt from union of bigint/double/string/boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: bigint | double | string | boolean): BigInt--><!--Device-BigInt-static $_invoke(value: bigint | double | string | boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint \| double \| string \| boolean | 是 | source value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A new BigInt instance from union of bigint/double/string/boolean |

## asIntN

```TypeScript
public static asIntN(bits: long, num: BigInt): BigInt
```

Clamps a BigInt to a signed integer with the specified number of bits.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public static asIntN(bits: long, num: BigInt): BigInt--><!--Device-BigInt-public static asIntN(bits: long, num: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | long | 是 | The number of bits for the signed integer representation. |
| num | [BigInt](arkts-arkts-bigint-c.md) | 是 | The BigInt value to clamp. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A BigInt value clamped to the specified number of bits as a signed integer. |

## asUintN

```TypeScript
public static asUintN(bits: long, num: BigInt): BigInt
```

Clamps a BigInt to an unsigned integer with the specified number of bits.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public static asUintN(bits: long, num: BigInt): BigInt--><!--Device-BigInt-public static asUintN(bits: long, num: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | long | 是 | The number of bits for the unsigned integer representation. |
| num | [BigInt](arkts-arkts-bigint-c.md) | 是 | The BigInt value to clamp. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | A BigInt value clamped to the specified number of bits as an unsigned integer. |

## constructor

```TypeScript
constructor()
```

Creates a new `BigInt` instance with value 0.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor()--><!--Device-BigInt-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(d: byte)
```

Creates a new `BigInt` instance from a byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: byte)--><!--Device-BigInt-constructor(d: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | byte | 是 | The byte value to convert. |

## constructor

```TypeScript
constructor(d: short)
```

Creates a new `BigInt` instance from a short value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: short)--><!--Device-BigInt-constructor(d: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | short | 是 | The short value to convert. |

## constructor

```TypeScript
constructor(d: int)
```

Creates a new `BigInt` instance from an int value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: int)--><!--Device-BigInt-constructor(d: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | int | 是 | The int value to convert. &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
constructor(d: long)
```

Creates a new `BigInt` instance from a long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: long)--><!--Device-BigInt-constructor(d: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | long | 是 | The long value to convert. |

## constructor

```TypeScript
constructor(d: double)
```

Creates a new `BigInt` instance from a double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: double)--><!--Device-BigInt-constructor(d: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | The double value to convert to BigInt. Must be an integer. |

## constructor

```TypeScript
constructor(d: string)
```

Creates a new `BigInt` instance from a string value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: string)--><!--Device-BigInt-constructor(d: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | string | 是 | The string value to convert to BigInt. |

## constructor

```TypeScript
constructor(d: boolean)
```

Creates a new `BigInt` instance from a boolean value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: boolean)--><!--Device-BigInt-constructor(d: boolean)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | boolean | 是 | The boolean value (true=1, false=0). |

## constructor

```TypeScript
constructor(d: BigInt)
```

Creates a new `BigInt` instance by copying another BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: BigInt)--><!--Device-BigInt-constructor(d: BigInt)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | [BigInt](arkts-arkts-bigint-c.md) | 是 | The BigInt object to copy. |

## constructor

```TypeScript
constructor(v: FixedArray<int>, sign: int)
```

Creates a new `BigInt` instance from internal components.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(v: FixedArray<int>, sign: int)--><!--Device-BigInt-constructor(v: FixedArray<int>, sign: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | FixedArray&lt;int&gt; | 是 | The array of digits. |
| sign | int | 是 | The sign of the number. &lt;br&gt;The value should be an integer. |

## doubleValue

```TypeScript
public doubleValue(): double
```

Returns the value of an object as a double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public doubleValue(): double--><!--Device-BigInt-public doubleValue(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | The double value. |

## equals

```TypeScript
public equals(to: BigInt): boolean
```

Checks if this BigInt is equal to another BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public equals(to: BigInt): boolean--><!--Device-BigInt-public equals(to: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| to | [BigInt](arkts-arkts-bigint-c.md) | 是 | The BigInt to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if equal, false otherwise. |

## equals

```TypeScript
equals(other: Any): boolean
```

Checks if this BigInt is equal to another value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-equals(other: Any): boolean--><!--Device-BigInt-equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | The value to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value is a BigInt and equal to this BigInt, false otherwise. |

## fromULong

```TypeScript
public static fromULong(val: long): BigInt
```

Creates a BigInt from an unsigned long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public static fromULong(val: long): BigInt--><!--Device-BigInt-public static fromULong(val: long): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | The unsigned long value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The new BigInt instance. |

## getLong

```TypeScript
public getLong(): long
```

Returns the value of an object as a long

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public getLong(): long--><!--Device-BigInt-public getLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The long value. |

## getULong

```TypeScript
public getULong(): long
```

Return current value clipped to unsigned long

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public getULong(): long--><!--Device-BigInt-public getULong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The unsigned long value. |

## negate

```TypeScript
public negate(): BigInt
```

Returns the negation of the BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public negate(): BigInt--><!--Device-BigInt-public negate(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The negated value. |

## negative

```TypeScript
public negative(): boolean
```

Returns whether the BigInt is negative.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public negative(): boolean--><!--Device-BigInt-public negative(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if negative, false otherwise. |

## operatorAdd

```TypeScript
public operatorAdd(other: BigInt): BigInt
```

Adds another BigInt to this one.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorAdd(other: BigInt): BigInt--><!--Device-BigInt-public operatorAdd(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the addition. |

## operatorBitwiseAnd

```TypeScript
public operatorBitwiseAnd(other: BigInt): BigInt
```

Performs bitwise AND operation with another BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseAnd(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseAnd(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The other BigInt. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the bitwise AND. |

## operatorBitwiseNot

```TypeScript
public operatorBitwiseNot(): BigInt
```

Performs bitwise NOT operation on the BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseNot(): BigInt--><!--Device-BigInt-public operatorBitwiseNot(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the bitwise NOT. |

## operatorBitwiseOr

```TypeScript
public operatorBitwiseOr(other: BigInt): BigInt
```

Performs bitwise OR operation with another BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseOr(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseOr(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The other BigInt. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the bitwise OR. |

## operatorBitwiseXor

```TypeScript
public operatorBitwiseXor(other: BigInt): BigInt
```

Performs bitwise XOR operation with another BigInt.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseXor(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseXor(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The other BigInt. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the bitwise XOR. |

## operatorDecrement

```TypeScript
public operatorDecrement(): BigInt
```

Decrements the BigInt value by 1.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorDecrement(): BigInt--><!--Device-BigInt-public operatorDecrement(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The decremented value. |

## operatorDivide

```TypeScript
public operatorDivide(other: BigInt): BigInt
```

Divides this BigInt by another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorDivide(other: BigInt): BigInt--><!--Device-BigInt-public operatorDivide(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The divisor. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The quotient of the division. |

## operatorGreaterThan

```TypeScript
public operatorGreaterThan(other: BigInt): boolean
```

Checks if this BigInt is greater than another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorGreaterThan(other: BigInt): boolean--><!--Device-BigInt-public operatorGreaterThan(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if this is greater than other, false otherwise. |

## operatorGreaterThanEqual

```TypeScript
public operatorGreaterThanEqual(other: BigInt): boolean
```

Checks if this BigInt is greater than or equal to another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorGreaterThanEqual(other: BigInt): boolean--><!--Device-BigInt-public operatorGreaterThanEqual(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if this is greater than or equal to other, false otherwise. |

## operatorIncrement

```TypeScript
public operatorIncrement(): BigInt
```

Increments the BigInt value by 1.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorIncrement(): BigInt--><!--Device-BigInt-public operatorIncrement(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The incremented value. |

## operatorLeftShift

```TypeScript
public operatorLeftShift(other: BigInt): BigInt
```

Shifts the BigInt to the left by a specified number of bits.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorLeftShift(other: BigInt): BigInt--><!--Device-BigInt-public operatorLeftShift(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The number of bits to shift. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The shifted BigInt. |

## operatorLessThan

```TypeScript
public operatorLessThan(other: BigInt): boolean
```

Checks if this BigInt is less than another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorLessThan(other: BigInt): boolean--><!--Device-BigInt-public operatorLessThan(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if this is less than other, false otherwise. |

## operatorLessThanEqual

```TypeScript
public operatorLessThanEqual(other: BigInt): boolean
```

Checks if this BigInt is less than or equal to another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorLessThanEqual(other: BigInt): boolean--><!--Device-BigInt-public operatorLessThanEqual(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if this is less than or equal to other, false otherwise. |

## operatorModule

```TypeScript
public operatorModule(other: BigInt): BigInt
```

Calculates the remainder of division of this BigInt by another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorModule(other: BigInt): BigInt--><!--Device-BigInt-public operatorModule(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The divisor. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The remainder. |

## operatorMultiply

```TypeScript
public operatorMultiply(other: BigInt): BigInt
```

Multiplies this BigInt by another.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorMultiply(other: BigInt): BigInt--><!--Device-BigInt-public operatorMultiply(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The multiplier. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the multiplication. |

## operatorRightShift

```TypeScript
public operatorRightShift(other: BigInt): BigInt
```

Shifts the BigInt to the right by a specified number of bits.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorRightShift(other: BigInt): BigInt--><!--Device-BigInt-public operatorRightShift(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The number of bits to shift. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The shifted BigInt. |

## operatorSubtract

```TypeScript
public operatorSubtract(other: BigInt): BigInt
```

Subtracts another BigInt from this one.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorSubtract(other: BigInt): BigInt--><!--Device-BigInt-public operatorSubtract(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of the subtraction. |

## positive

```TypeScript
public positive(): boolean
```

Returns whether the BigInt is positive.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public positive(): boolean--><!--Device-BigInt-public positive(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if positive (including zero), false otherwise. |

## pow

```TypeScript
public pow(exponent: BigInt): BigInt
```

Returns the base to the exponent power.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public pow(exponent: BigInt): BigInt--><!--Device-BigInt-public pow(exponent: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exponent | [BigInt](arkts-arkts-bigint-c.md) | 是 | The exponent value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | The result of base^exponent. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

Converts a number to a string by using the current or specified locale.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string--><!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | [BigIntToLocaleStringOptions](arkts-arkts-bigint-biginttolocalestringoptions-i.md) | 否 | An object with some or all of the properties of the Intl.NumberFormat options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the BigInt formatted according to the locale and options. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

## toString

```TypeScript
public toString(): string
```

Converts the BigInt to a string in base 10.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toString(): string--><!--Device-BigInt-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representation of the BigInt in base 10. |

## toString

```TypeScript
public toString(radix: int): string
```

Returns a string representation of the BigInt object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toString(radix: int): string--><!--Device-BigInt-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | An integer in the range 2 through 36 specifying the base to use for representing numeric values. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the specified BigInt object. |

