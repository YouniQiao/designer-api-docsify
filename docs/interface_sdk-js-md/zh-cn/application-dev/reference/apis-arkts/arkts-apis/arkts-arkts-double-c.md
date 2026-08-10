# Double

Represents boxed double value and related operations

**继承/实现关系：** Double extends [Floating](arkts-arkts-numeric-floating-c.md) implements [Comparable<Double>](Comparable<Double>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Double extends Floating implements Comparable<Double>--><!--Device-unnamed-export class Double extends Floating implements Comparable<Double>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(): Double
```

Creates a new instance of a Double

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static $_invoke(): Double--><!--Device-Double-static $_invoke(): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | A new Double instance |

## $_invoke

```TypeScript
static $_invoke(value: string | Double | BigInt | undefined | null): Double
```

Creates a new instance of a Double

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static $_invoke(value: string | Double | BigInt | undefined | null): Double--><!--Device-Double-static $_invoke(value: string | Double | BigInt | undefined | null): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| Double \| BigInt \| undefined \| null | 是 | The value to be converted to a number. Can be a string, number, or BigInt (optional). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | A new Double instance |

## add

```TypeScript
public add(other: Double): Double
```

Performs floating point addition of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public add(other: Double): Double--><!--Device-Double-public add(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the addition. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | Result of the addition |

## bitCastFromLong

```TypeScript
public static bitCastFromLong(bits: long): double
```

Converts bit representation to corresponding IEEE-754 floating point representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static bitCastFromLong(bits: long): double--><!--Device-Double-public static bitCastFromLong(bits: long): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | long | 是 | bits to convert. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | converted value |

## bitCastToLong

```TypeScript
public static bitCastToLong(val: double): long
```

Converts IEEE-754 floating point representation to corresponding bit representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static bitCastToLong(val: double): long--><!--Device-Double-public static bitCastToLong(val: double): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | double | 是 | value to convert. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | bit representation |

## compare

```TypeScript
public static compare(lhs: double, rhs: double): boolean
```

compare(double, double) checks if two doubles are differs no more than by Double.DELTA

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static compare(lhs: double, rhs: double): boolean--><!--Device-Double-public static compare(lhs: double, rhs: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | double | 是 | left-hand side double for comparison. |
| rhs | double | 是 | right-hand side double for comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if lhs and rhs are equal with respect to Double.DELTA |

## compareTo

```TypeScript
public compareTo(other: Double): int
```

Compares this instance to other Double object The result is less than 0 if this instance lesser than provided object0 if they are equal and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public compareTo(other: Double): int--><!--Device-Double-public compareTo(other: Double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Double object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | if the cur value > the other reutrn 0,otherwise return -1 |

## constructor

```TypeScript
constructor()
```

Constructs a new Double instance with initial value zero

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor()--><!--Device-Double-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: double)
```

Constructs a new Double instance with provided initial value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor(value: double)--><!--Device-Double-constructor(value: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | the initial value |

## constructor

```TypeScript
constructor(value: BigInt)
```

Constructs a new Double instance from BigInt

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor(value: BigInt)--><!--Device-Double-constructor(value: BigInt)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 |  |

## constructor

```TypeScript
constructor(value: string)
```

Constructs a new Double instance from string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor(value: string)--><!--Device-Double-constructor(value: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | string that may contain a number |

## div

```TypeScript
public div(other: Double): Double
```

Performs floating point division of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public div(other: Double): Double--><!--Device-Double-public div(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the division. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | Result of the division |

## equals

```TypeScript
equals(other: Any): boolean
```

Checks for equality this instance with provided object,treated as a Double Returns false if type of provided object is not the same as this type

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-equals(other: Any): boolean--><!--Device-Double-equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | object to be checked against |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if provided object and this instance have same value, false otherwise Returns false if type of provided object is not the same as this type |

## isFinite

```TypeScript
static isFinite(v: double): boolean
```

isFinite(double) checks if double is a floating point value (not a NaN or infinity)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static isFinite(v: double): boolean--><!--Device-Double-static isFinite(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | the double to test |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is a floating point value |

## isFinite

```TypeScript
isFinite(): boolean
```

isFinite() checks if the underlying double is a floating point value (not a NaN or infinity)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-isFinite(): boolean--><!--Device-Double-isFinite(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying double is a floating point value |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Double): boolean
```

Checks if this instance value is greater than or equal to value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isGreaterEqualThan(other: Double): boolean--><!--Device-Double-public isGreaterEqualThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than or equal to provided, false otherwise |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Double): boolean
```

Checks if this instance value is greater than value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isGreaterThan(other: Double): boolean--><!--Device-Double-public isGreaterThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is greater than provided, false otherwise |

## isInteger

```TypeScript
public static isInteger(v: double): boolean
```

Checks if double is similar to an integer value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static isInteger(v: double): boolean--><!--Device-Double-public static isInteger(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | the double to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is similar to an integer value |

## isInteger

```TypeScript
public isInteger(): boolean
```

Checks if the underlying double is similar to an integer value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isInteger(): boolean--><!--Device-Double-public isInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying double is similar to an integer value |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Double): boolean
```

Checks if this instance value is less than or equal to value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isLessEqualThan(other: Double): boolean--><!--Device-Double-public isLessEqualThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than or equal to provided, false otherwise |

## isLessThan

```TypeScript
public isLessThan(other: Double): boolean
```

Checks if this instance value is less than value of provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isLessThan(other: Double): boolean--><!--Device-Double-public isLessThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this value is less than provided, false otherwise |

## isNaN

```TypeScript
static isNaN(v: double): boolean
```

isNaN(double) checks if double is NaN (not a number)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static isNaN(v: double): boolean--><!--Device-Double-static isNaN(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | the double to test |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is NaN |

## isNaN

```TypeScript
isNaN(): boolean
```

isNaN() checks if the underlying double is NaN (not a number)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-isNaN(): boolean--><!--Device-Double-isNaN(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying double is NaN |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: double): boolean
```

Checks if double is a safe integer value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static isSafeInteger(v: double): boolean--><!--Device-Double-public static isSafeInteger(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | the double to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the argument is integer ans less than MAX_SAFE_INTEGER |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

Checks if double is a safe integer value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isSafeInteger(): boolean--><!--Device-Double-public isSafeInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying double is a safe integer |

## mul

```TypeScript
public mul(other: Double): Double
```

Performs floating point multiplication of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public mul(other: Double): Double--><!--Device-Double-public mul(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the multiplication. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | Result of the multiplication |

## parseFloat

```TypeScript
static parseFloat(s: string): double
```

parseFloat(String) converts std.core.String to double If arg is '+Infinity', 'Infinity' or '-Infinity', return value is `inf` or `-inf` respectively.If arg is '+0' or '-0', return value is 0 or -0.If arg has leading zeroes, it's ignored: '0001.5' -> 1.5, '-0001.5' -> -1.5If arg starts from '.', leading zero is implied: '.5' -> 0.5, '-.5' -> -0.5If arg successfully parsed, trailing non-digits ignored: '-.6ffg' -> -0.6If arg can not be parsed into a number, NaN is returned

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseFloat(s: string): double--><!--Device-Double-static parseFloat(s: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the result of conversion |

## parseInt

```TypeScript
static parseInt(s: string): double
```

parseInt(String) parses from String an integer of radix 10

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseInt(s: string): double--><!--Device-Double-static parseInt(s: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the result of parsing |

## parseInt

```TypeScript
static parseInt(s: string, r: int): double
```

parseInt(String, int) parses from String an integer of specified radix If args ('10', 1) -> thrown ArgumentOutOfRangeError, ('10', 37) -> thrown ArgumentOutOfRangeError If args ('10', 2) -> 2If args ('10', 10) -> 10, ('10', 0) -> 10If args ('ff', 16) -> 255etc.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseInt(s: string, r: int): double--><!--Device-Double-static parseInt(s: string, r: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert |
| r | int | 是 | the radix of conversion; should be [2, 36]; 0 assumed to be 10 &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the result of parsing |

## parseInt

```TypeScript
static parseInt(s: string, r: double): double
```

parseInt(String, double) parses from String an integer of specified radix If args ('10', 1) -> thrown ArgumentOutOfRangeError, ('10', 37) -> thrown ArgumentOutOfRangeError If args ('10', 2) -> 2If args ('10', 10) -> 10, ('10', 0) -> 10If args ('ff', 16) -> 255etc.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseInt(s: string, r: double): double--><!--Device-Double-static parseInt(s: string, r: double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | the string to convert |
| r | double | 是 | the radix of conversion; should be [2, 36]; 0 assumed to be 10 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the result of parsing |

## sub

```TypeScript
public sub(other: Double): Double
```

Performs floating point subtraction of this instance with provided one, returns the result as new instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public sub(other: Double): Double--><!--Device-Double-public sub(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | Right hand side of the subtraction. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | Result of the subtraction |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toByte(): byte--><!--Device-Double-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | return the current value convert byte value |

## toByte

```TypeScript
public static toByte(value: double): byte
```

Returns the primitive as byte value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toByte(value: double): byte--><!--Device-Double-public static toByte(value: double): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte |  |

## toDouble

```TypeScript
toDouble(): double
```

Returns value of this instance

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-toDouble(): double--><!--Device-Double-toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | return the current value convert double value |

## toDouble

```TypeScript
static toDouble(value: double): double
```

Returns the primitive as double value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static toDouble(value: double): double--><!--Device-Double-static toDouble(value: double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to cast |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double |  |

## toExponential

```TypeScript
public toExponential(): string
```

toExponential() returns std.core.string representing the underlying double in exponential notation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toExponential(): string--><!--Device-Double-public toExponential(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the result of conversion |

## toExponential

```TypeScript
public toExponential(d?: double): string
```

toExponential() returns std.core.String representing the underlying double in exponential notation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toExponential(d?: double): string--><!--Device-Double-public toExponential(d?: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the result of conversion |

## toExponentialWithNoDigit

```TypeScript
public toExponentialWithNoDigit(): string
```

toExponential(double) returns std.core.string representing the underlying double in exponential notation If d = new Double(0.25); d.toExponential(2) -> '2.50e-1'If d = new Double(0.25); d.toExponential(2.5) -> '2.50e-1'If d = new Double(0.25); d.toExponential(1) -> '2.5e-1'If d = new Double(12345.01); d.toExponential(10) -> '1.2345010000e+4'If d = new Double(NaN); d.toExponential(10) -> 'NaN';If d = new Double(Double.POSITIVE_INFINITY); d.toExponential(10) -> 'Infinity'; '-Infinity' for negative

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toExponentialWithNoDigit(): string--><!--Device-Double-public toExponentialWithNoDigit(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the result of conversion |

## toFixed

```TypeScript
public toFixed(): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFixed(): string--><!--Device-Double-public toFixed(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toFixed

```TypeScript
public toFixed(d?: double): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFixed(d?: double): string--><!--Device-Double-public toFixed(d?: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toFixedImpl

```TypeScript
public toFixedImpl(d: double): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation If d = new Double(0.1); d.toFixed(0) -> '0'If d = new Double(0.7); d.toFixed(0) -> '1'If d = new Double(0.12345); d.toFixed(1) -> '0.1'If d = new Double(0.12345); d.toFixed(3) -> '0.123'If d = new Double(Double.POSITIVE_INFINITY); d.toFixed(3) -> 'Infinity'If d = new Double(Double.NaN); d.toFixed(3) -> 'NaN'If d = new Double(0.25); d.toFixed(200) -> thrown ArgumentOutOfRangeError

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFixedImpl(d: double): string--><!--Device-Double-public toFixedImpl(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | fixed size (integer part); must be in [0, 100]. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the result of conversion |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFloat(): float--><!--Device-Double-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | return the current value convert float value |

## toFloat

```TypeScript
public static toFloat(value: double): float
```

Returns the primitive as float value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toFloat(value: double): float--><!--Device-Double-public static toFloat(value: double): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float |  |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toInt(): int--><!--Device-Double-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return the current value convert int value |

## toInt

```TypeScript
public static toInt(value: double): int
```

Returns the primitive as int value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toInt(value: double): int--><!--Device-Double-public static toInt(value: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int |  |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

<!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toLong(): long--><!--Device-Double-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | return the current value convert long value |

## toLong

```TypeScript
public static toLong(value: double): long
```

Returns the primitive as long value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toLong(value: double): long--><!--Device-Double-public static toLong(value: double): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long |  |

## toPrecision

```TypeScript
public toPrecision(d: double): string
```

toPrecision(double) returns std.core.string representing the underlying double on the specified precision If d = new Double(0.25); d.toPrecision(4) -> '0.2500'If d = new Double(1.01); d.toPrecision(4.7) -> '1.010'If d = new Double(0.25); d.toPrecision(0) -> thrown ArgumentOutOfRangeError If d = new Double(12345.123455); d.toPrecision(10) -> '12345.12346'

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toPrecision(d: double): string--><!--Device-Double-public toPrecision(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | precision (rounded to nearest integer); must be in [1, 100]. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the result of conversion |

## toPrecision

```TypeScript
public toPrecision(): string
```

toPrecision() returns std.core.string representing the underlying double in exponential notation  basically, if toPrecision called with no argument it's just toString according to spec

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toPrecision(): string--><!--Device-Double-public toPrecision(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the result of conversion |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toShort(): short--><!--Device-Double-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | return the current value convert short value |

## toShort

```TypeScript
public static toShort(value: double): short
```

Returns the primitive as short value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toShort(value: double): short--><!--Device-Double-public static toShort(value: double): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short |  |

## toString

```TypeScript
public static toString(d: double, r: int): string
```

toString(d: double, r: int): string -- returns a string representation of d by radix r

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toString(d: double, r: int): string--><!--Device-Double-public static toString(d: double, r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 |  |
| r | int | 是 | &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | return the string value |

## toString

```TypeScript
public static toString(d: double): string
```

Converts the specified double-precision floating-point value to its string representation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toString(d: double): string--><!--Device-Double-public static toString(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | return the string value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toString

```TypeScript
public toString(r: int): string
```

Converts the specified double-precision floating-point value to its string representation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toString(r: int): string--><!--Device-Double-public toString(r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | int | 是 | &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | return the string value |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toString(): string--><!--Device-Double-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | return the string value |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 64
```

Size of this type in bits.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly BIT_SIZE: byte = 64--><!--Device-Double-public static readonly BIT_SIZE: byte = 64-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 8
```

Size of this type in bytes.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly BYTE_SIZE: byte = 8--><!--Device-Double-public static readonly BYTE_SIZE: byte = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)
```

Minimal possible difference between two double values.For double (IEEE-754 binary64) it is 2^(-52) and its bit representation is 0x3cb0000000000000.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)--><!--Device-Double-public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)-End-->

**系统能力：** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static readonly EPSILON: double = Double.DELTA
```

Minimal possible difference between two double values.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly EPSILON: double = Double.DELTA--><!--Device-Double-public static readonly EPSILON: double = Double.DELTA-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_SAFE_INTEGER

```TypeScript
public static readonly MAX_SAFE_INTEGER: double = 9007199254740991
```

Maximal integer value that can be used as a double without loss of precision.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MAX_SAFE_INTEGER: double = 9007199254740991--><!--Device-Double-public static readonly MAX_SAFE_INTEGER: double = 9007199254740991-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: double = 1.7976931348623157e+308
```

Maximal value that this type can have as a double.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MAX_VALUE: double = 1.7976931348623157e+308--><!--Device-Double-public static readonly MAX_VALUE: double = 1.7976931348623157e+308-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_SAFE_INTEGER

```TypeScript
public static readonly MIN_SAFE_INTEGER: double = -9007199254740991
```

Minimal integer value that can be used as a double without loss of precision.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MIN_SAFE_INTEGER: double = -9007199254740991--><!--Device-Double-public static readonly MIN_SAFE_INTEGER: double = -9007199254740991-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24
```

Minimal value that this type can have as a double the workarond for libc's double literal parsing bug.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24--><!--Device-Double-public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24-End-->

**系统能力：** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0
```

Represents the -Infinity value according to IEEE-754 specification.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0--><!--Device-Double-public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0-End-->

**系统能力：** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static readonly NaN: double = 0.0 / 0.0
```

Represents the NaN value according to IEEE-754 specification.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly NaN: double = 0.0 / 0.0--><!--Device-Double-public static readonly NaN: double = 0.0 / 0.0-End-->

**系统能力：** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0
```

Represents the +Infinity value according to IEEE-754 specification.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0--><!--Device-Double-public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static readonly PRECISION: byte = 53
```

Number of significant precision bits in this floating type.

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly PRECISION: byte = 53--><!--Device-Double-public static readonly PRECISION: byte = 53-End-->

**系统能力：** SystemCapability.Utils.Lang

