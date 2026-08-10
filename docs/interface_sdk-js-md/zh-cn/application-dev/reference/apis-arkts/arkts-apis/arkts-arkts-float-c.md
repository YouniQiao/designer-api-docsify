# Float

Represents boxed float value and related operations.

**继承/实现关系：** Float extends [Floating](arkts-arkts-numeric-floating-c.md) implements [Comparable<Float>](Comparable<Float>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Float extends Floating implements Comparable<Float>--><!--Device-unnamed-export class Float extends Floating implements Comparable<Float>-End-->

**系统能力：** SystemCapability.Utils.Lang

## add

```TypeScript
public add(other: Float): Float
```

Performs floating point addition with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public add(other: Float): Float--><!--Device-Float-public add(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the addition. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the addition. |

## bitCastFromInt

```TypeScript
public static bitCastFromInt(bits: int): float
```

Converts bit representation to corresponding IEEE-754 floating point representation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static bitCastFromInt(bits: int): float--><!--Device-Float-public static bitCastFromInt(bits: int): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | int | 是 | bits to convert. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | converted value. |

## bitCastToInt

```TypeScript
public static bitCastToInt(val: float): int
```

Converts IEEE-754 floating point representation to corresponding bit representation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static bitCastToInt(val: float): int--><!--Device-Float-public static bitCastToInt(val: float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | value to convert. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | bit representation. |

## compare

```TypeScript
public static compare(lhs: float, rhs: float): boolean
```

Compares two floats to see if they differ by at most DELTA.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static compare(lhs: float, rhs: float): boolean--><!--Device-Float-public static compare(lhs: float, rhs: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | float | 是 | left-hand side float for comparison. |
| rhs | float | 是 | right-hand side float for comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if equal with respect to DELTA. |

## compareTo

```TypeScript
public compareTo(other: Float): int
```

Compares this instance to other Float object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public compareTo(other: Float): int--><!--Device-Float-public compareTo(other: Float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | Float object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | result of the comparison (-1, 0, or 1). |

## constructor

```TypeScript
public constructor()
```

Constructs a new Float instance with initial value zero.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public constructor()--><!--Device-Float-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: float)
```

Constructs a new Float instance with provided initial value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public constructor(value: float)--><!--Device-Float-public constructor(value: float)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | the initial value. |

## constructor

```TypeScript
public constructor(value: double)
```

Constructs a new Float instance with provided initial value (double type literal).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public constructor(value: double)--><!--Device-Float-public constructor(value: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | the initial value. |

## div

```TypeScript
public div(other: Float): Float
```

Performs floating point division with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public div(other: Float): Float--><!--Device-Float-public div(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the division. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the division. |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality with provided object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public equals(other: Any): boolean--><!--Device-Float-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | object to be checked against. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if equal, false otherwise. |

## isFinite

```TypeScript
public static isFinite(v: float): boolean
```

Checks if float is a finite floating point value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isFinite(v: float): boolean--><!--Device-Float-public static isFinite(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | the float to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is finite. |

## isFinite

```TypeScript
public isFinite(): boolean
```

Checks if the underlying float is a finite floating point value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isFinite(): boolean--><!--Device-Float-public isFinite(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying float is finite. |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Float): boolean
```

Checks if this instance value is greater than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isGreaterEqualThan(other: Float): boolean--><!--Device-Float-public isGreaterEqualThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than or equal to provided. |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Float): boolean
```

Checks if this instance value is greater than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isGreaterThan(other: Float): boolean--><!--Device-Float-public isGreaterThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than provided. |

## isInteger

```TypeScript
public static isInteger(v: float): boolean
```

Checks if float is similar to an integer value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isInteger(v: float): boolean--><!--Device-Float-public static isInteger(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | the float to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is similar to an integer. |

## isInteger

```TypeScript
public isInteger(): boolean
```

Checks if the underlying float is similar to an integer value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isInteger(): boolean--><!--Device-Float-public isInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying float is similar to an integer. |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Float): boolean
```

Checks if this instance value is less than or equal to value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isLessEqualThan(other: Float): boolean--><!--Device-Float-public isLessEqualThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than or equal to provided. |

## isLessThan

```TypeScript
public isLessThan(other: Float): boolean
```

Checks if this instance value is less than value of provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isLessThan(other: Float): boolean--><!--Device-Float-public isLessThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than provided. |

## isNaN

```TypeScript
public static isNaN(v: float): boolean
```

Checks if float is NaN.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isNaN(v: float): boolean--><!--Device-Float-public static isNaN(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | the float to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is NaN. |

## isNaN

```TypeScript
public isNaN(): boolean
```

Checks if the underlying float is NaN.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isNaN(): boolean--><!--Device-Float-public isNaN(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying float is NaN. |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: float): boolean
```

Checks if float is a safe integer value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isSafeInteger(v: float): boolean--><!--Device-Float-public static isSafeInteger(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | the float to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is a safe integer. |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

Checks if the underlying float is a safe integer value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isSafeInteger(): boolean--><!--Device-Float-public isSafeInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying float is a safe integer. |

## mul

```TypeScript
public mul(other: Float): Float
```

Performs floating point multiplication with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public mul(other: Float): Float--><!--Device-Float-public mul(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the multiplication. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the multiplication. |

## sub

```TypeScript
public sub(other: Float): Float
```

Performs floating point subtraction with provided instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public sub(other: Float): Float--><!--Device-Float-public sub(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | right hand side of the subtraction. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | result of the subtraction. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toByte(): byte--><!--Device-Float-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | value as byte. |

## toByte

```TypeScript
public static toByte(value: float): byte
```

Returns the primitive as byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toByte(value: float): byte--><!--Device-Float-public static toByte(value: float): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | casted value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toDouble(): double--><!--Device-Float-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | value as double. |

## toDouble

```TypeScript
public static toDouble(value: float): double
```

Returns the primitive as double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toDouble(value: float): double--><!--Device-Float-public static toDouble(value: float): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to cast. |

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

<!--Device-Float-public toFloat(): float--><!--Device-Float-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | value as float. |

## toFloat

```TypeScript
public static toFloat(value: float): float
```

Returns the primitive as float value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toFloat(value: float): float--><!--Device-Float-public static toFloat(value: float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | casted value. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toInt(): int--><!--Device-Float-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | value as int. |

## toInt

```TypeScript
public static toInt(value: float): int
```

Returns the primitive as int value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toInt(value: float): int--><!--Device-Float-public static toInt(value: float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | casted value. |

## toLocaleString

```TypeScript
public toLocaleString(): string
```

Converts this object to a locale-specific string representation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toLocaleString(): string--><!--Device-Float-public toLocaleString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the locale-specific conversion. |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toLong(): long--><!--Device-Float-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | value as long. |

## toLong

```TypeScript
public static toLong(value: float): long
```

Returns the primitive as long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toLong(value: float): long--><!--Device-Float-public static toLong(value: float): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to cast. |

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

<!--Device-Float-public toShort(): short--><!--Device-Float-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | value as short. |

## toShort

```TypeScript
public static toShort(value: float): short
```

Returns the primitive as short value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toShort(value: float): short--><!--Device-Float-public static toShort(value: float): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | casted value. |

## toString

```TypeScript
public static toString(f: float, r: int): string
```

Returns a string representation of float by radix r.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toString(f: float, r: int): string--><!--Device-Float-public static toString(f: float, r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| f | float | 是 | the float value. |
| r | int | 是 | the radix. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public static toString(f: float): string
```

Returns a string representation of float in base 10.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toString(f: float): string--><!--Device-Float-public static toString(f: float): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| f | float | 是 | the float value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## toString

```TypeScript
public toString(r: int): string
```

Converts this object to a string in the given radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toString(r: int): string--><!--Device-Float-public toString(r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | int | 是 | the radix. &lt;br&gt;The value should be an integer. |

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

<!--Device-Float-public toString(): string--><!--Device-Float-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 32
```

Size of this type in bits.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static BIT_SIZE: byte = 32--><!--Device-Float-public static BIT_SIZE: byte = 32-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 4
```

Size of this type in bytes.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static BYTE_SIZE: byte = 4--><!--Device-Float-public static BYTE_SIZE: byte = 4-End-->

**系统能力：** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static DELTA: float = Float.bitCastFromInt(0x34000000)
```

Minimal possible difference between two float values.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static DELTA: float = Float.bitCastFromInt(0x34000000)--><!--Device-Float-public static DELTA: float = Float.bitCastFromInt(0x34000000)-End-->

**系统能力：** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static EPSILON: float = Float.DELTA
```

Minimal possible difference between two float values.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static EPSILON: float = Float.DELTA--><!--Device-Float-public static EPSILON: float = Float.DELTA-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_SAFE_INTEGER

```TypeScript
public static MAX_SAFE_INTEGER: float = 16777215
```

Maximal integer value that can be used as a float without loss of precision.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static MAX_SAFE_INTEGER: float = 16777215--><!--Device-Float-public static MAX_SAFE_INTEGER: float = 16777215-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: float = 3.40282346638528860e+38
```

Maximal value that this type can have as a float.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static MAX_VALUE: float = 3.40282346638528860e+38--><!--Device-Float-public static MAX_VALUE: float = 3.40282346638528860e+38-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: float = 1.4e-45
```

Minimal value that this type can have as a float.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static MIN_VALUE: float = 1.4e-45--><!--Device-Float-public static MIN_VALUE: float = 1.4e-45-End-->

**系统能力：** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)
```

Represents the -Infinity value according to IEEE-754 specification.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)--><!--Device-Float-public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)-End-->

**系统能力：** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static NaN: float = Double.toFloat(0.0 / 0.0)
```

Represents the NaN value according to IEEE-754 specification.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static NaN: float = Double.toFloat(0.0 / 0.0)--><!--Device-Float-public static NaN: float = Double.toFloat(0.0 / 0.0)-End-->

**系统能力：** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)
```

Represents the +Infinity value according to IEEE-754 specification.

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)--><!--Device-Float-public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static PRECISION: byte = 24
```

Number of significant precision bits in this floating type.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static PRECISION: byte = 24--><!--Device-Float-public static PRECISION: byte = 24-End-->

**系统能力：** SystemCapability.Utils.Lang

## f

```TypeScript
f
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Float-f--><!--Device-Float-f-End-->

