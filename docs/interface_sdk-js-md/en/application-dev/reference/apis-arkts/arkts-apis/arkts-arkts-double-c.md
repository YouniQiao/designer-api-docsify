# Double

Represents boxed double value and related operations

**Inheritance/Implementation:** Double extends [Floating](arkts-arkts-numeric-floating-c.md) and implements Comparable<Double>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(): Double
```

Creates a new instance of a Double

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Double |

## $_invoke

```TypeScript
static $_invoke(value: string | Double | BigInt | undefined | null): Double
```

Creates a new instance of a Double

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| Double \| BigInt \| undefined \| null | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Double |

## add

```TypeScript
public add(other: Double): Double
```

Performs floating point addition of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Double |

## bitCastFromLong

```TypeScript
public static bitCastFromLong(bits: long): double
```

Converts bit representation to corresponding IEEE-754 floating point representation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [bits](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## bitCastToLong

```TypeScript
public static bitCastToLong(val: double): long
```

Converts IEEE-754 floating point representation to corresponding bit representation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## compare

```TypeScript
public static compare(lhs: double, rhs: double): boolean
```

compare(double, double) checks if two doubles are differs no more than by Double.DELTA

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lhs | double | Yes |
| rhs | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## compareTo

```TypeScript
public compareTo(other: Double): int
```

Compares this instance to other Double object The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## constructor

```TypeScript
constructor()
```

Constructs a new Double instance with initial value zero

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: double)
```

Constructs a new Double instance with provided initial value

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

## constructor

```TypeScript
constructor(value: BigInt)
```

Constructs a new Double instance from BigInt

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | Yes |

## constructor

```TypeScript
constructor(value: string)
```

Constructs a new Double instance from string

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## div

```TypeScript
public div(other: Double): Double
```

Performs floating point division of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Double |

## equals

```TypeScript
equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Double Returns false if type of provided object is not the same as this type

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Any | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFinite

```TypeScript
static isFinite(v: double): boolean
```

isFinite(double) checks if double is a floating point value (not a NaN or infinity)

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFinite

```TypeScript
isFinite(): boolean
```

isFinite() checks if the underlying double is a floating point value (not a NaN or infinity)

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Double): boolean
```

Checks if this instance value is greater than or equal to value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Double): boolean
```

Checks if this instance value is greater than value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInteger

```TypeScript
public static isInteger(v: double): boolean
```

Checks if double is similar to an integer value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInteger

```TypeScript
public isInteger(): boolean
```

Checks if the underlying double is similar to an integer value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Double): boolean
```

Checks if this instance value is less than or equal to value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isLessThan

```TypeScript
public isLessThan(other: Double): boolean
```

Checks if this instance value is less than value of provided instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isNaN

```TypeScript
static isNaN(v: double): boolean
```

isNaN(double) checks if double is NaN (not a number)

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isNaN

```TypeScript
isNaN(): boolean
```

isNaN() checks if the underlying double is NaN (not a number)

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: double): boolean
```

Checks if double is a safe integer value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

Checks if double is a safe integer value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## mul

```TypeScript
public mul(other: Double): Double
```

Performs floating point multiplication of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Double |

## parseFloat

```TypeScript
static parseFloat(s: string): double
```

parseFloat(String) converts std.core.String to double If arg is '+Infinity', 'Infinity' or '-Infinity', return value is `inf` or `-inf` respectively. If arg is '+0' or '-0', return value is 0 or -0. If arg has leading zeroes, it's ignored: '0001.5' -&gt; 1.5, '-0001.5' -&gt; -1.5 If arg starts from '.', leading zero is implied: '.5' -&gt; 0.5, '-.5' -&gt; -0.5 If arg successfully parsed, trailing non-digits ignored: '-.6ffg' -&gt; -0.6 If arg can not be parsed into a number, NaN is returned

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| s | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## parseInt

```TypeScript
static parseInt(s: string): double
```

parseInt(String) parses from String an integer of radix 10

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| s | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## parseInt

```TypeScript
static parseInt(s: string, r: int): double
```

parseInt(String, int) parses from String an integer of specified radix If args ('10', 1) -&gt; thrown ArgumentOutOfRangeError, ('10', 37) -&gt; thrown ArgumentOutOfRangeError If args ('10', 2) -&gt; 2 If args ('10', 10) -&gt; 10, ('10', 0) -&gt; 10 If args ('ff', 16) -&gt; 255 etc.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| s | string | Yes |
| r | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## parseInt

```TypeScript
static parseInt(s: string, r: double): double
```

parseInt(String, double) parses from String an integer of specified radix If args ('10', 1) -&gt; thrown ArgumentOutOfRangeError, ('10', 37) -&gt; thrown ArgumentOutOfRangeError If args ('10', 2) -&gt; 2 If args ('10', 10) -&gt; 10, ('10', 0) -&gt; 10 If args ('ff', 16) -&gt; 255 etc.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| s | string | Yes |
| r | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## sub

```TypeScript
public sub(other: Double): Double
```

Performs floating point subtraction of this instance with provided one, returns the result as new instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Double |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| byte |

## toByte

```TypeScript
public static toByte(value: double): byte
```

Returns the primitive as byte value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| byte |

## toDouble

```TypeScript
toDouble(): double
```

Returns value of this instance

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## toDouble

```TypeScript
static toDouble(value: double): double
```

Returns the primitive as double value

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## toExponential

```TypeScript
public toExponential(): string
```

toExponential() returns std.core.string representing the underlying double in exponential notation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toExponential

```TypeScript
public toExponential(d?: double): string
```

toExponential() returns std.core.String representing the underlying double in exponential notation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toExponentialWithNoDigit

```TypeScript
public toExponentialWithNoDigit(): string
```

toExponential(double) returns std.core.string representing the underlying double in exponential notation If d = new Double(0.25); d.toExponential(2) -&gt; '2.50e-1'If d = new Double(0.25); d.toExponential(2.5) -&gt; '2.50e-1'If d = new Double(0.25); d.toExponential(1) -&gt; '2.5e-1'If d = new Double(12345.01); d.toExponential(10) -&gt; '1.2345010000e+4'If d = new Double(NaN); d.toExponential(10) -&gt; 'NaN'; If d = new Double(Double.POSITIVE_INFINITY); d.toExponential(10) -&gt; 'Infinity';'-Infinity' for negative

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toFixed

```TypeScript
public toFixed(): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toFixed

```TypeScript
public toFixed(d?: double): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toFixedImpl

```TypeScript
public toFixedImpl(d: double): string
```

toFixed(double) returns std.core.string representing the underlying double using fixed-point notation If d = new Double(0.1); d.toFixed(0) -&gt; '0'If d = new Double(0.7); d.toFixed(0) -&gt; '1'If d = new Double(0.12345); d.toFixed(1) -&gt; '0.1'If d = new Double(0.12345); d.toFixed(3) -&gt; '0.123'If d = new Double(Double.POSITIVE_INFINITY); d.toFixed(3) -&gt; 'Infinity'If d = new Double(Double.NaN); d.toFixed(3) -&gt; 'NaN'If d = new Double(0.25); d.toFixed(200) -&gt; thrown ArgumentOutOfRangeError

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| float |

## toFloat

```TypeScript
public static toFloat(value: double): float
```

Returns the primitive as float value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| float |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## toInt

```TypeScript
public static toInt(value: double): int
```

Returns the primitive as int value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | Intl.LocalesArgument | No |
| options | Intl.NumberFormatOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | Intl.LocalesArgument | No |
| options | object | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## toLong

```TypeScript
public static toLong(value: double): long
```

Returns the primitive as long value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## toPrecision

```TypeScript
public toPrecision(d: double): string
```

toPrecision(double) returns std.core.string representing the underlying double on the specified precision If d = new Double(0.25); d.toPrecision(4) -&gt; '0.2500'If d = new Double(1.01); d.toPrecision(4.7) -&gt; '1.010'If d = new Double(0.25); d.toPrecision(0) -&gt; thrown ArgumentOutOfRangeError If d = new Double(12345.123455); d.toPrecision(10) -&gt; '12345.12346'

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toPrecision

```TypeScript
public toPrecision(): string
```

toPrecision() returns std.core.string representing the underlying double in exponential notation basically, if toPrecision called with no argument it's just toString according to spec

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| short |

## toShort

```TypeScript
public static toShort(value: double): short
```

Returns the primitive as short value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| short |

## toString

```TypeScript
public static toString(d: double, r: int): string
```

toString(d: double, r: int): string -- returns a string representation of d by radix r

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | Yes |
| r | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
public static toString(d: double): string
```

Converts the specified double-precision floating-point value to its string representation.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
public toString(r: int): string
```

Converts the specified double-precision floating-point value to its string representation.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| r | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 64
```

Size of this type in bits.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 8
```

Size of this type in bytes.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)
```

Minimal possible difference between two double values. For double (IEEE-754 binary64) it is 2^(-52) and its bit representation is 0x3cb0000000000000.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static readonly EPSILON: double = Double.DELTA
```

Minimal possible difference between two double values.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## MAX_SAFE_INTEGER

```TypeScript
public static readonly MAX_SAFE_INTEGER: double = 9007199254740991
```

Maximal integer value that can be used as a double without loss of precision.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: double = 1.7976931348623157e+308
```

Maximal value that this type can have as a double.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## MIN_SAFE_INTEGER

```TypeScript
public static readonly MIN_SAFE_INTEGER: double = -9007199254740991
```

Minimal integer value that can be used as a double without loss of precision.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24
```

Minimal value that this type can have as a double the workarond for libc's double literal parsing bug.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static readonly NaN: double = 0.0 / 0.0
```

Represents the NaN value according to IEEE-754 specification.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0
```

Represents the -Infinity value according to IEEE-754 specification.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0
```

Represents the +Infinity value according to IEEE-754 specification.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static readonly PRECISION: byte = 53
```

Number of significant precision bits in this floating type.

**Type:** byte

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
