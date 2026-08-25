# Decimal

An arbitrary-precision Decimal type

**Since:** 12

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Decimal } from 'kits/@kit.ArkTS';
```

## abs

```TypeScript
abs(): Decimal
```

Return a new Decimal whose value is the absolute value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## abs

```TypeScript
static abs(n: Value): Decimal
```

Return a new Decimal whose value is the absolute value of `n`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## acos

```TypeScript
acos(): Decimal
```

Return a new Decimal whose value is the arccosine (inverse cosine) in radians of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## acos

```TypeScript
static acos(n: Value): Decimal
```

Return a new Decimal whose value is the arccosine in radians of `n`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## acosh

```TypeScript
acosh(): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic cosine in radians of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## acosh

```TypeScript
static acosh(n: Value): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic cosine of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## add

```TypeScript
add(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal plus `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## add

```TypeScript
static add(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is the sum of `x` and `y`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| y | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## asin

```TypeScript
asin(): Decimal
```

Return a new Decimal whose value is the arcsine (inverse sine) in radians of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## asin

```TypeScript
static asin(n: Value): Decimal
```

Return a new Decimal whose value is the arcsine in radians of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## asinh

```TypeScript
asinh(): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic sine in radians of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## asinh

```TypeScript
static asinh(n: Value): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic sine of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## atan

```TypeScript
atan(): Decimal
```

Return a new Decimal whose value is the arctangent (inverse tangent) in radians of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## atan

```TypeScript
static atan(n: Value): Decimal
```

Return a new Decimal whose value is the arctangent in radians of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## atan2

```TypeScript
static atan2(y: Value, x: Value): Decimal
```

Return a new Decimal whose value is the arctangent in radians of `y/x` in the range -pi to pi (inclusive), rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| y | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| x | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## atanh

```TypeScript
atanh(): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic tangent in radians of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## atanh

```TypeScript
static atanh(n: Value): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic tangent of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## cbrt

```TypeScript
cbrt(): Decimal
```

Return a new Decimal whose value is the cube root of the value of this Decimal, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## cbrt

```TypeScript
static cbrt(n: Value): Decimal
```

Return a new Decimal whose value is the cube root of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## ceil

```TypeScript
ceil(): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a whole number in the direction of positive Infinity.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## ceil

```TypeScript
static ceil(n: Value): Decimal
```

Return a new Decimal whose value is `n` rounded to an integer using `ROUND_CEIL`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clamp

```TypeScript
clamp(min: Value, max: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal clamped to the range delineated by `min` and `max`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [min](#min) | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| [max](#max) | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## clamp

```TypeScript
static clamp(n: Value, min: Value, max: Value): Decimal
```

Return a new Decimal whose value is `n` clamped to the range delineated by `min` and `max`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| [min](#min) | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| [max](#max) | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## comparedTo

```TypeScript
comparedTo(n: Value): number
```

Return 1 if the value of this Decimal is greater than the value of `n`, -1 if the value of this Decimal is less than the value of `n`, 0 if they have the same value, NaN if the value of either Decimal is NaN.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## constructor

```TypeScript
constructor(n: Value)
```

Return a new Decimal whose value is the absolute value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## cos

```TypeScript
cos(): Decimal
```

Return a new Decimal whose value is the cosine of the value in radians of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## cos

```TypeScript
static cos(n: Value): Decimal
```

Return a new Decimal whose value is the cosine of `n`, rounded to `precision` significant digits using rounding mode `rounding`

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## cosh

```TypeScript
cosh(): Decimal
```

Return a new Decimal whose value is the hyperbolic cosine of the value in radians of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## cosh

```TypeScript
static cosh(n: Value): Decimal
```

Return a new Decimal whose value is the hyperbolic cosine of `n`, rounded to precision significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## decimalPlaces

```TypeScript
decimalPlaces(): number
```

Return the number of decimal places of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## div

```TypeScript
div(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal divided by `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## div

```TypeScript
static div(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is `x` divided by `y`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| y | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## dividedToIntegerBy

```TypeScript
dividedToIntegerBy(n: Value): Decimal
```

Return a new Decimal whose value is the integer part of dividing the value of this Decimal by the value of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## equals

```TypeScript
equals(n: Value): boolean
```

Return true if the value of this Decimal is equal to the value of `n`, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## exp

```TypeScript
exp(): Decimal
```

Return a new Decimal whose value is the natural exponential of the value of this Decimal, i.e. the base e raised to the power the value of this Decimal, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## exp

```TypeScript
static exp(n: Value): Decimal
```

Return a new Decimal whose value is the natural exponential of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## floor

```TypeScript
floor(): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a whole number in the direction of negative Infinity.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## floor

```TypeScript
static floor(n: Value): Decimal
```

Return a new Decimal whose value is `n` round to an integer using `ROUND_FLOOR`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## greaterThan

```TypeScript
greaterThan(n: Value): boolean
```

Return true if the value of this Decimal is greater than the value of `n`, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(n: Value): boolean
```

Return true if the value of this Decimal is greater than or equal to the value of `n`, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## hypot

```TypeScript
static hypot(...n: Value[]): Decimal
```

Return a new Decimal whose value is the square root of the sum of the squares of the arguments, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md)[] | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isFinite

```TypeScript
isFinite(): boolean
```

Return true if the value of this Decimal is a finite number, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInteger

```TypeScript
isInteger(): boolean
```

Return true if the value of this Decimal is an integer, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isNaN

```TypeScript
isNaN(): boolean
```

Return true if the value of this Decimal is NaN, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isNegative

```TypeScript
isNegative(): boolean
```

Return true if the value of this Decimal is negative, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isPositive

```TypeScript
isPositive(): boolean
```

Return true if the value of this Decimal is positive, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isZero

```TypeScript
isZero(): boolean
```

Return true if the value of this Decimal is 0 or -0, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## lessThan

```TypeScript
lessThan(n: Value): boolean
```

Return true if the value of this Decimal is less than `n`, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(n: Value): boolean
```

Return true if the value of this Decimal is less than or equal to `n`, otherwise return false.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## ln

```TypeScript
ln(): Decimal
```

Return a new Decimal whose value is the natural logarithm of the value of this Decimal, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## ln

```TypeScript
static ln(n: Value): Decimal
```

Return a new Decimal whose value is the natural logarithm of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## log

```TypeScript
log(n: Value): Decimal
```

Return the logarithm of the value of this Decimal to the specified base, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## log

```TypeScript
static log(n: Value, base: Value): Decimal
```

Return a new Decimal whose value is the log of `n` to the base `base`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| base | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## log10

```TypeScript
static log10(n: Value): Decimal
```

Return a new Decimal whose value is the base 10 logarithm of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## log2

```TypeScript
static log2(n: Value): Decimal
```

Return a new Decimal whose value is the base 2 logarithm of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## max

```TypeScript
static max(...n: Value[]): Decimal
```

Return a new Decimal whose value is the maximum of the arguments.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md)[] | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## min

```TypeScript
static min(...n: Value[]): Decimal
```

Return a new Decimal whose value is the minimum of the arguments.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md)[] | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## mod

```TypeScript
mod(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal modulo `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## mod

```TypeScript
static mod(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is `x` modulo `y`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| y | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## mul

```TypeScript
mul(n: Value): Decimal
```

Return a new Decimal whose value is this Decimal times `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## mul

```TypeScript
static mul(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is `x` multiplied by `y`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| y | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## negate

```TypeScript
negate(): Decimal
```

Return a new Decimal whose value is the value of this Decimal negated, i.e. as if multiplied by -1.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## pow

```TypeScript
pow(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal raised to the power `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## pow

```TypeScript
static pow(base: Value, exponent: Value): Decimal
```

Return a new Decimal whose value is `base` raised to the power `exponent`, rounded to precision significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| base | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| exponent | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200060](../errorcode-utils.md#10200060-precision-limit-is-exceeded) |

## precision

```TypeScript
precision(): number
```

Return the number of significant digits of the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## precision

```TypeScript
precision(includeZeros: boolean | number): number
```

Return the number of significant digits of the value of this Decimal, whether to count integer-part trailing zeros.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| includeZeros | boolean \| number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## random

```TypeScript
static random(): Decimal
```

Returns a new Decimal with a random value equal to or greater than 0 and less than 1.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200061](../errorcode-utils.md#10200061-encryption-method-is-unavailable) |

## random

```TypeScript
static random(significantDigits: number): Decimal
```

Returns a new Decimal with a random value equal to or greater than 0 and less than 1, and with `significantDigits` significant digits (or less if trailing zeros are produced).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200061](../errorcode-utils.md#10200061-encryption-method-is-unavailable) |

## round

```TypeScript
static round(n: Value): Decimal
```

Return a new Decimal whose value is `n` rounded to an integer using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## set

```TypeScript
static set(config: DecimalConfig): void
```

Configures the 'global' settings for this particular Decimal constructor.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [DecimalConfig](arkts-arkts-math-decimal-decimalconfig-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
| [10200061](../errorcode-utils.md#10200061-encryption-method-is-unavailable) |

## sign

```TypeScript
static sign(n: Value): number
```

Return the sign of the passed value to the method. 1 if x &gt; 0, -1 if x &lt; 0, 0 if x is 0, -0 if x is -0, NaN otherwise

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sin

```TypeScript
sin(): Decimal
```

Return a new Decimal whose value is the sine of the value in radians of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## sin

```TypeScript
static sin(n: Value): Decimal
```

Return a new Decimal whose value is the sine of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sinh

```TypeScript
sinh(): Decimal
```

Return a new Decimal whose value is the hyperbolic sine of the value in radians of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## sinh

```TypeScript
static sinh(n: Value): Decimal
```

Return a new Decimal whose value is the hyperbolic sine of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sqrt

```TypeScript
sqrt(): Decimal
```

Return a new Decimal whose value is the square root of this Decimal, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## sqrt

```TypeScript
static sqrt(n: Value): Decimal
```

Return a new Decimal whose value is the square root of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sub

```TypeScript
sub(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal minus `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sub

```TypeScript
static sub(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is `x` minus `y`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| y | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sum

```TypeScript
static sum(...n: Value[]): Decimal
```

Return a new Decimal whose value is the sum of the arguments, rounded to `precision` significant digits using rounding mode `rounding`.Only the result is rounded, not the intermediate calculations.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md)[] | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## tan

```TypeScript
tan(): Decimal
```

Return a new Decimal whose value is the tangent of the value in radians of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## tan

```TypeScript
static tan(n: Value): Decimal
```

Return a new Decimal whose value is the tangent of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## tanh

```TypeScript
tanh(): Decimal
```

Return a new Decimal whose value is the hyperbolic tangent of the value in radians of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## tanh

```TypeScript
static tanh(n: Value): Decimal
```

Return a new Decimal whose value is the hyperbolic tangent of `n`, rounded to `precision` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## toBinary

```TypeScript
toBinary(): string
```

Return a string representing the value of this Decimal in base 2.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toBinary

```TypeScript
toBinary(significantDigits: number): string
```

Return a string representing the value of this Decimal in base 2, round to `significantDigits` significant digits.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toBinary

```TypeScript
toBinary(significantDigits: number, rounding: Rounding): string
```

Return a string representing the value of this Decimal in base 2, round to `significantDigits` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `significantDigits \|

## toDecimalPlaces

```TypeScript
toDecimalPlaces(): Decimal
```

Return a new Decimal whose value is the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## toDecimalPlaces

```TypeScript
toDecimalPlaces(decimalPlaces: number): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of `decimalPlaces` decimal places.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [decimalPlaces](arkts-arkts-math-decimal-decimal-c.md) | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toDecimalPlaces

```TypeScript
toDecimalPlaces(decimalPlaces: number, rounding: Rounding): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of `decimalPlaces` decimal places using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [decimalPlaces](arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `decimalPlaces \|

## toExponential

```TypeScript
toExponential(): string
```

Return a string representing the value of this Decimal in exponential notation.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toExponential

```TypeScript
toExponential(decimalPlaces: number): string
```

Return a string representing the value of this Decimal in exponential notation rounded to `decimalPlaces` fixed decimal places.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [decimalPlaces](arkts-arkts-math-decimal-decimal-c.md) | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toExponential

```TypeScript
toExponential(decimalPlaces: number, rounding: Rounding): string
```

Return a string representing the value of this Decimal in exponential notation rounded to `decimalPlaces` fixed decimal places using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [decimalPlaces](arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `decimalPlaces \|

## toFixed

```TypeScript
toFixed(): string
```

Return a string representing the value of this Decimal in normal (fixed-point).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toFixed

```TypeScript
toFixed(decimalPlaces: number): string
```

Return a string representing the value of this Decimal in normal (fixed-point) notation to `decimalPlaces` fixed decimal places.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 18 and later: SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [decimalPlaces](arkts-arkts-math-decimal-decimal-c.md) | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toFixed

```TypeScript
toFixed(decimalPlaces: number, rounding: Rounding): string
```

Return a string representing the value of this Decimal in normal (fixed-point) notation to `decimalPlaces` fixed decimal places and rounded using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [decimalPlaces](arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `decimalPlaces \|

## toFraction

```TypeScript
toFraction(): Decimal[]
```

Return an array representing the value of this Decimal as a simple fraction with an integer numerator and an integer denominator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md)[] |

## toFraction

```TypeScript
toFraction(maxDenominator: Value): Decimal[]
```

Return an array representing the value of this Decimal as a simple fraction with an integer numerator and an integer denominator. The denominator will be a positive non-zero value less than or equal to `max_denominator`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxDenominator | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## toHexadecimal

```TypeScript
toHexadecimal(): string
```

Return a string representing the value of this Decimal in base 16

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toHexadecimal

```TypeScript
toHexadecimal(significantDigits: number): string
```

Return a string representing the value of this Decimal in base 16, round to `significantDigits` significant.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toHexadecimal

```TypeScript
toHexadecimal(significantDigits: number, rounding: Rounding): string
```

Return a string representing the value of this Decimal in base 16, round to `significantDigits` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `significantDigits \|

## toNearest

```TypeScript
toNearest(n: Value): Decimal
```

Returns a new Decimal whose value is the nearest multiple of `n`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## toNearest

```TypeScript
toNearest(n: Value, rounding: Rounding): Decimal
```

Returns a new Decimal whose value is the nearest multiple of `n` in the direction of rounding mode `rounding`, to the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toNumber

```TypeScript
toNumber(): number
```

Return the value of this Decimal converted to a number primitive. Zero keeps its sign.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## toOctal

```TypeScript
toOctal(): string
```

Return a string representing the value of this Decimal in base 8.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toOctal

```TypeScript
toOctal(significantDigits: number): string
```

Return a string representing the value of this Decimal in base 8, round to `significantDigits` significant.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toOctal

```TypeScript
toOctal(significantDigits: number, rounding: Rounding): string
```

Return a string representing the value of this Decimal in base 8, round to `significantDigits` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes | {number \| string \|
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `significantDigits \|

## toPrecision

```TypeScript
toPrecision(): string
```

Return a string representing the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toPrecision

```TypeScript
toPrecision(significantDigits: number): string
```

Return a string representing the value of this Decimal rounded to `significantDigits` significant digits.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toPrecision

```TypeScript
toPrecision(significantDigits: number, rounding: Rounding): string
```

Return a string representing the value of this Decimal rounded to `significantDigits` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `significantDigits \|

## toSignificantDigits

```TypeScript
toSignificantDigits(): Decimal
```

Return a new Decimal whose value is the value of this Decimal.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## toSignificantDigits

```TypeScript
toSignificantDigits(significantDigits: number): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of `significantDigits` significant digits.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## toSignificantDigits

```TypeScript
toSignificantDigits(significantDigits: number, rounding: Rounding): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of `significantDigits` significant digits using rounding mode `rounding`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| significantDigits | number | Yes |
| [rounding](arkts-arkts-math-decimal-decimalconfig-i.md) | [Rounding](arkts-arkts-rounding-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of `significantDigits \|

## toString

```TypeScript
toString(): string
```

Return a string representing the value of this Decimal. Return exponential notation if this Decimal has a positive exponent equal to or greater than `toExpPos`, or a negative exponent equal to or less than `toExpNeg`.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## trunc

```TypeScript
trunc(): Decimal
```

Return a new Decimal whose value is the value of this Decimal truncated to a whole number.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

## trunc

```TypeScript
static trunc(n: Value): Decimal
```

Return a new Decimal whose value is `n` truncated to an integer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | [Value](arkts-arkts-value-t.md) | Yes | {number \| string \|

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Decimal](arkts-arkts-math-decimal-decimal-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## valueOf

```TypeScript
valueOf(): string
```

Return a string representing the value of this Decimal. Unlike `toString`, negative zero will include the minus sign.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## d

```TypeScript
readonly d: number[]
```

The numbers of decimal digits.

**Type:** number[]

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## e

```TypeScript
get e(): number
```

The number of decimal exponent.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## EUCLIDEAN

```TypeScript
static readonly EUCLIDEAN : 9
```

Not a rounding mode, see modulo

**Type:** 9

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_CEILING

```TypeScript
static readonly ROUND_CEILING : 2
```

Rounds towards Infinity

**Type:** 2

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_DOWN

```TypeScript
static readonly ROUND_DOWN : 1
```

Rounds towards zero

**Type:** 1

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_FLOOR

```TypeScript
static readonly ROUND_FLOOR : 3
```

Rounds towards -Infinity

**Type:** 3

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_CEILING

```TypeScript
static readonly ROUND_HALF_CEILING : 7
```

Rounds towards nearest neighbour. If equidistant, rounds towards Infinity

**Type:** 7

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_DOWN

```TypeScript
static readonly ROUND_HALF_DOWN : 5
```

Rounds towards nearest neighbour. If equidistant, rounds towards zero

**Type:** 5

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_EVEN

```TypeScript
static readonly ROUND_HALF_EVEN : 6
```

Rounds towards nearest neighbour. If equidistant, rounds towards even neighbour

**Type:** 6

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_FLOOR

```TypeScript
static readonly ROUND_HALF_FLOOR : 8
```

Rounds towards nearest neighbour. If equidistant, rounds towards -Infinity

**Type:** 8

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_UP

```TypeScript
static readonly ROUND_HALF_UP : 4
```

Rounds towards nearest neighbour. If equidistant, rounds away from zero

**Type:** 4

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ROUND_UP

```TypeScript
static readonly ROUND_UP : 0
```

Rounds away from zero

**Type:** 0

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## s

```TypeScript
get s(): number
```

The number of decimal sign.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang
