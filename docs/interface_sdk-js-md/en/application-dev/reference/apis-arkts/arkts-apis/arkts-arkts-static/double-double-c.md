# Double

Represents boxed double value and related operations

**Inheritance/Implementation:** Double extends [Floating](numeric-floating-c.md) and implements [Comparable<Double>](Comparable<Double>)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export class Double extends Floating implements Comparable<Double>--><!--Device-unnamed-export class Double extends Floating implements Comparable<Double>-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(): Double
```

Creates a new instance of a Double

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static $_invoke(): Double--><!--Device-Double-static $_invoke(): Double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new Double instance |

## $_invoke

```TypeScript
static $_invoke(value: string | Double | BigInt | undefined | null): Double
```

Creates a new instance of a Double

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static $_invoke(value: string | Double | BigInt | undefined | null): Double--><!--Device-Double-static $_invoke(value: string | Double | BigInt | undefined | null): Double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| Double \| BigInt \| undefined \| null | Yes | The value to be converted to a number. Can be a string, number, or BigInt (optional). |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new Double instance |

## add

```TypeScript
public add(other: Double): Double
```

Performs floating point addition of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public add(other: Double): Double--><!--Device-Double-public add(other: Double): Double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the addition. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Result of the addition |

## bitCastFromLong

```TypeScript
public static bitCastFromLong(bits: long): double
```

Converts bit representation to corresponding IEEE-754 floating point representation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static bitCastFromLong(bits: long): double--><!--Device-Double-public static bitCastFromLong(bits: long): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | long | Yes | bits to convert. |

**Return value:**

| Type | Description |
| --- | --- |
| double | converted value |

## bitCastToLong

```TypeScript
public static bitCastToLong(val: double): long
```

Converts IEEE-754 floating point representation to corresponding bit representation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static bitCastToLong(val: double): long--><!--Device-Double-public static bitCastToLong(val: double): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | double | Yes | value to convert. |

**Return value:**

| Type | Description |
| --- | --- |
| long | bit representation |

## compare

```TypeScript
public static compare(lhs: double, rhs: double): boolean
```

compare(double, double) checks if two doubles are differs no more than by Double.DELTA

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static compare(lhs: double, rhs: double): boolean--><!--Device-Double-public static compare(lhs: double, rhs: double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lhs | double | Yes | left-hand side double for comparison. |
| rhs | double | Yes | right-hand side double for comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if lhs and rhs are equal with respect to Double.DELTA |

## compareTo

```TypeScript
public compareTo(other: Double): int
```

Compares this instance to other Double object The result is less than 0 if this instance lesser than provided object0 if they are equal and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public compareTo(other: Double): int--><!--Device-Double-public compareTo(other: Double): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Double object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | if the cur value        the other reutrn 0,otherwise return -1 |

## constructor

```TypeScript
constructor()
```

Constructs a new Double instance with initial value zero

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-constructor()--><!--Device-Double-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: double)
```

Constructs a new Double instance with provided initial value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-constructor(value: double)--><!--Device-Double-constructor(value: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | the initial value |

## constructor

```TypeScript
constructor(value: BigInt)
```

Constructs a new Double instance from BigInt

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-constructor(value: BigInt)--><!--Device-Double-constructor(value: BigInt)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## constructor

```TypeScript
constructor(value: string)
```

Constructs a new Double instance from string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-constructor(value: string)--><!--Device-Double-constructor(value: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | string that may contain a number |

## div

```TypeScript
public div(other: Double): Double
```

Performs floating point division of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public div(other: Double): Double--><!--Device-Double-public div(other: Double): Double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the division. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Result of the division |

## equals

```TypeScript
equals(other: Any): boolean
```

Checks for equality this instance with provided object,treated as a Double Returns false if type of provided object is not the same as this type

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-equals(other: Any): boolean--><!--Device-Double-equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | object to be checked against |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if provided object and this instance have same value, false otherwise Returns false if type of provided object is not the same as this type |

## isFinite

```TypeScript
static isFinite(v: double): boolean
```

isFinite(double) checks if double is a floating point value (not a NaN or infinity)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static isFinite(v: double): boolean--><!--Device-Double-static isFinite(v: double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | double | Yes | the double to test |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is a floating point value |

## isFinite

```TypeScript
isFinite(): boolean
```

isFinite() checks if the underlying double is a floating point value (not a NaN or infinity)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-isFinite(): boolean--><!--Device-Double-isFinite(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying double is a floating point value |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Double): boolean
```

Checks if this instance value is greater than or equal to value of provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public isGreaterEqualThan(other: Double): boolean--><!--Device-Double-public isGreaterEqualThan(other: Double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than or equal to provided, false otherwise |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Double): boolean
```

Checks if this instance value is greater than value of provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public isGreaterThan(other: Double): boolean--><!--Device-Double-public isGreaterThan(other: Double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is greater than provided, false otherwise |

## isInteger

```TypeScript
public static isInteger(v: double): boolean
```

Checks if double is similar to an integer value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static isInteger(v: double): boolean--><!--Device-Double-public static isInteger(v: double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | double | Yes | the double to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is similar to an integer value |

## isInteger

```TypeScript
public isInteger(): boolean
```

Checks if the underlying double is similar to an integer value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public isInteger(): boolean--><!--Device-Double-public isInteger(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying double is similar to an integer value |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Double): boolean
```

Checks if this instance value is less than or equal to value of provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public isLessEqualThan(other: Double): boolean--><!--Device-Double-public isLessEqualThan(other: Double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than or equal to provided, false otherwise |

## isLessThan

```TypeScript
public isLessThan(other: Double): boolean
```

Checks if this instance value is less than value of provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public isLessThan(other: Double): boolean--><!--Device-Double-public isLessThan(other: Double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this value is less than provided, false otherwise |

## isNaN

```TypeScript
static isNaN(v: double): boolean
```

isNaN(double) checks if double is NaN (not a number)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static isNaN(v: double): boolean--><!--Device-Double-static isNaN(v: double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | double | Yes | the double to test |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is NaN |

## isNaN

```TypeScript
isNaN(): boolean
```

isNaN() checks if the underlying double is NaN (not a number)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-isNaN(): boolean--><!--Device-Double-isNaN(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying double is NaN |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: double): boolean
```

Checks if double is a safe integer value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static isSafeInteger(v: double): boolean--><!--Device-Double-public static isSafeInteger(v: double): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | double | Yes | the double to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the argument is integer ans less than MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_SAFE\_\_\_ESCAPED\_UNDERSCORE\_\_\_INTEGER |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

Checks if double is a safe integer value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public isSafeInteger(): boolean--><!--Device-Double-public isSafeInteger(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying double is a safe integer |

## mul

```TypeScript
public mul(other: Double): Double
```

Performs floating point multiplication of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public mul(other: Double): Double--><!--Device-Double-public mul(other: Double): Double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the multiplication. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Result of the multiplication |

## parseFloat

```TypeScript
static parseFloat(s: string): double
```

parseFloat(String) converts std.core.String to double If arg is '+Infinity', 'Infinity' or '-Infinity', return value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ or \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ respectively.If arg is '+0' or '-0', return value is 0 or -0.If arg has leading zeroes, it's ignored: '0001.5' -  
    1.5, '-0001.5' -  
    -1.5  
If arg starts from '.', leading zero is implied: '.5' -  
    0.5, '-.5' -  
    -0.5  
If arg successfully parsed, trailing non-digits ignored: '-.6ffg' -  
    -0.6  
If arg can not be parsed into a number, NaN is returned

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static parseFloat(s: string): double--><!--Device-Double-static parseFloat(s: string): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert |

**Return value:**

| Type | Description |
| --- | --- |
| double | the result of conversion |

## parseInt

```TypeScript
static parseInt(s: string): double
```

parseInt(String) parses from String an integer of radix 10

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static parseInt(s: string): double--><!--Device-Double-static parseInt(s: string): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert |

**Return value:**

| Type | Description |
| --- | --- |
| double | the result of parsing |

## parseInt

```TypeScript
static parseInt(s: string, r: int): double
```

parseInt(String, int) parses from String an integer of specified radix If args ('10', 1) -  
    thrown ArgumentOutOfRangeError, ('10', 37) -  
    thrown ArgumentOutOfRangeError  
If args ('10', 2) -  
    2  
If args ('10', 10) -  
    10, ('10', 0) -  
    10  
If args ('ff', 16) -  
    255  
etc.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static parseInt(s: string, r: int): double--><!--Device-Double-static parseInt(s: string, r: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert |
| r | int | Yes | the radix of conversion; should be [2, 36]; 0 assumed to be 10 \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the result of parsing |

## parseInt

```TypeScript
static parseInt(s: string, r: double): double
```

parseInt(String, double) parses from String an integer of specified radix If args ('10', 1) -  
    thrown ArgumentOutOfRangeError, ('10', 37) -  
    thrown ArgumentOutOfRangeError  
If args ('10', 2) -  
    2  
If args ('10', 10) -  
    10, ('10', 0) -  
    10  
If args ('ff', 16) -  
    255  
etc.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static parseInt(s: string, r: double): double--><!--Device-Double-static parseInt(s: string, r: double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | the string to convert |
| r | double | Yes | the radix of conversion; should be [2, 36]; 0 assumed to be 10 |

**Return value:**

| Type | Description |
| --- | --- |
| double | the result of parsing |

## sub

```TypeScript
public sub(other: Double): Double
```

Performs floating point subtraction of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public sub(other: Double): Double--><!--Device-Double-public sub(other: Double): Double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Right hand side of the subtraction. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Result of the subtraction |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toByte(): byte--><!--Device-Double-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | return the current value convert byte value |

## toByte

```TypeScript
public static toByte(value: double): byte
```

Returns the primitive as byte value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toByte(value: double): byte--><!--Device-Double-public static toByte(value: double): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| byte |  |

## toDouble

```TypeScript
toDouble(): double
```

Returns value of this instance

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-toDouble(): double--><!--Device-Double-toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | return the current value convert double value |

## toDouble

```TypeScript
static toDouble(value: double): double
```

Returns the primitive as double value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-static toDouble(value: double): double--><!--Device-Double-static toDouble(value: double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to cast |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## toExponential

```TypeScript
public toExponential(): string
```

toExponential() returns std.core.string representing the underlying double in exponential notation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toExponential(): string--><!--Device-Double-public toExponential(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the result of conversion |

## toExponential

```TypeScript
public toExponential(d?: double): string
```

toExponential() returns std.core.String representing the underlying double in exponential notation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toExponential(d?: double): string--><!--Device-Double-public toExponential(d?: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string | the result of conversion |

## toExponentialWithNoDigit

```TypeScript
public toExponentialWithNoDigit(): string
```

toExponential(double) returns std.core.string representing the underlying double in exponential notation If d = new Double(0.25); d.toExponential(2) -  
    '2.50e-1'  
If d = new Double(0.25); d.toExponential(2.5) -  
    '2.50e-1'  
If d = new Double(0.25); d.toExponential(1) -  
    '2.5e-1'  
If d = new Double(12345.01); d.toExponential(10) -  
    '1.2345010000e+4'  
If d = new Double(NaN); d.toExponential(10) -  
    'NaN';  
If d = new Double(Double.POSITIVE\_INFINITY); d.toExponential(10) -  
    'Infinity';  
'-Infinity' for negative

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toExponentialWithNoDigit(): string--><!--Device-Double-public toExponentialWithNoDigit(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the result of conversion |

## toFixed

```TypeScript
public toFixed(): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toFixed(): string--><!--Device-Double-public toFixed(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## toFixed

```TypeScript
public toFixed(d?: double): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toFixed(d?: double): string--><!--Device-Double-public toFixed(d?: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## toFixedImpl

```TypeScript
public toFixedImpl(d: double): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation If d = new Double(0.1); d.toFixed(0) -  
    '0'  
If d = new Double(0.7); d.toFixed(0) -  
    '1'  
If d = new Double(0.12345); d.toFixed(1) -  
    '0.1'  
If d = new Double(0.12345); d.toFixed(3) -  
    '0.123'  
If d = new Double(Double.POSITIVE\_INFINITY); d.toFixed(3) -  
    'Infinity'  
If d = new Double(Double.NaN); d.toFixed(3) -  
    'NaN'  
If d = new Double(0.25); d.toFixed(200) -  
    thrown ArgumentOutOfRangeError

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toFixedImpl(d: double): string--><!--Device-Double-public toFixedImpl(d: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | Yes | fixed size (integer part); must be in [0, 100]. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the result of conversion |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toFloat(): float--><!--Device-Double-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | return the current value convert float value |

## toFloat

```TypeScript
public static toFloat(value: double): float
```

Returns the primitive as float value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toFloat(value: double): float--><!--Device-Double-public static toFloat(value: double): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| float |  |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toInt(): int--><!--Device-Double-public toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | return the current value convert int value |

## toInt

```TypeScript
public static toInt(value: double): int
```

Returns the primitive as int value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toInt(value: double): int--><!--Device-Double-public static toInt(value: double): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| int |  |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

<!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toLong(): long--><!--Device-Double-public toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | return the current value convert long value |

## toLong

```TypeScript
public static toLong(value: double): long
```

Returns the primitive as long value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toLong(value: double): long--><!--Device-Double-public static toLong(value: double): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| long |  |

## toPrecision

```TypeScript
public toPrecision(d: double): string
```

toPrecision(double) returns std.core.string representing the underlying double on the specified precision If d = new Double(0.25); d.toPrecision(4) -  
    '0.2500'  
If d = new Double(1.01); d.toPrecision(4.7) -  
    '1.010'  
If d = new Double(0.25); d.toPrecision(0) -  
    thrown ArgumentOutOfRangeError  
If d = new Double(12345.123455); d.toPrecision(10) -  
    '12345.12346'

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toPrecision(d: double): string--><!--Device-Double-public toPrecision(d: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | Yes | precision (rounded to nearest integer); must be in [1, 100]. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the result of conversion |

## toPrecision

```TypeScript
public toPrecision(): string
```

toPrecision() returns std.core.string representing the underlying double in exponential notation basically, if toPrecision called with no argument it's just toString according to spec

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toPrecision(): string--><!--Device-Double-public toPrecision(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the result of conversion |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toShort(): short--><!--Device-Double-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | return the current value convert short value |

## toShort

```TypeScript
public static toShort(value: double): short
```

Returns the primitive as short value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toShort(value: double): short--><!--Device-Double-public static toShort(value: double): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| short |  |

## toString

```TypeScript
public static toString(d: double, r: int): string
```

toString(d: double, r: int): string -- returns a string representation of d by radix r

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toString(d: double, r: int): string--><!--Device-Double-public static toString(d: double, r: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | Yes |  |
| r | int | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | return the string value |

## toString

```TypeScript
public static toString(d: double): string
```

Converts the specified double-precision floating-point value to its string representation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static toString(d: double): string--><!--Device-Double-public static toString(d: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | Yes | return the string value. |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## toString

```TypeScript
public toString(r: int): string
```

Converts the specified double-precision floating-point value to its string representation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toString(r: int): string--><!--Device-Double-public toString(r: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| r | int | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | return the string value |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public toString(): string--><!--Device-Double-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | return the string value |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 64
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly BIT_SIZE: byte = 64--><!--Device-Double-public static readonly BIT_SIZE: byte = 64-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 8
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly BYTE_SIZE: byte = 8--><!--Device-Double-public static readonly BYTE_SIZE: byte = 8-End-->

**System capability:** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)
```

Minimal possible difference between two double values.For double (IEEE-754 binary64) it is 2^(-52) and its bit representation is 0x3cb0000000000000.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)--><!--Device-Double-public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)-End-->

**System capability:** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static readonly EPSILON: double = Double.DELTA
```

Minimal possible difference between two double values.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly EPSILON: double = Double.DELTA--><!--Device-Double-public static readonly EPSILON: double = Double.DELTA-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_SAFE_INTEGER

```TypeScript
public static readonly MAX_SAFE_INTEGER: double = 9007199254740991
```

Maximal integer value that can be used as a double without loss of precision.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly MAX_SAFE_INTEGER: double = 9007199254740991--><!--Device-Double-public static readonly MAX_SAFE_INTEGER: double = 9007199254740991-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: double = 1.7976931348623157e+308
```

Maximal value that this type can have as a double.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly MAX_VALUE: double = 1.7976931348623157e+308--><!--Device-Double-public static readonly MAX_VALUE: double = 1.7976931348623157e+308-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_SAFE_INTEGER

```TypeScript
public static readonly MIN_SAFE_INTEGER: double = -9007199254740991
```

Minimal integer value that can be used as a double without loss of precision.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly MIN_SAFE_INTEGER: double = -9007199254740991--><!--Device-Double-public static readonly MIN_SAFE_INTEGER: double = -9007199254740991-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24
```

Minimal value that this type can have as a double the workarond for libc's double literal parsing bug.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24--><!--Device-Double-public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24-End-->

**System capability:** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0
```

Represents the -Infinity value according to IEEE-754 specification.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0--><!--Device-Double-public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0-End-->

**System capability:** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static readonly NaN: double = 0.0 / 0.0
```

Represents the NaN value according to IEEE-754 specification.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly NaN: double = 0.0 / 0.0--><!--Device-Double-public static readonly NaN: double = 0.0 / 0.0-End-->

**System capability:** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0
```

Represents the +Infinity value according to IEEE-754 specification.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0--><!--Device-Double-public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0-End-->

**System capability:** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static readonly PRECISION: byte = 53
```

Number of significant precision bits in this floating type.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Double-public static readonly PRECISION: byte = 53--><!--Device-Double-public static readonly PRECISION: byte = 53-End-->

**System capability:** SystemCapability.Utils.Lang

