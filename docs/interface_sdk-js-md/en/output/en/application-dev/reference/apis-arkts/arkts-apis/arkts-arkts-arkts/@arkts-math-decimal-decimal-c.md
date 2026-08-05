# Decimal

An arbitrary-precision Decimal type

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class Decimal--><!--Device-unnamed-declare class Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

## abs

```TypeScript
abs(): Decimal
```

Return a new Decimal whose value is the absolute value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-abs(): Decimal--><!--Device-Decimal-abs(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## abs

```TypeScript
static abs(n: Value): Decimal
```

Return a new Decimal whose value is the absolute value of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static abs(n: Value): Decimal--><!--Device-Decimal-static abs(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## acos

```TypeScript
acos(): Decimal
```

Return a new Decimal whose value is the arccosine (inverse cosine) in radians of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-acos(): Decimal--><!--Device-Decimal-acos(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## acos

```TypeScript
static acos(n: Value): Decimal
```

Return a new Decimal whose value is the arccosine in radians of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static acos(n: Value): Decimal--><!--Device-Decimal-static acos(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## acosh

```TypeScript
acosh(): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic cosine in radians of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-acosh(): Decimal--><!--Device-Decimal-acosh(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## acosh

```TypeScript
static acosh(n: Value): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic cosine of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static acosh(n: Value): Decimal--><!--Device-Decimal-static acosh(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## add

```TypeScript
add(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal plus \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-add(n: Value): Decimal--><!--Device-Decimal-add(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## add

```TypeScript
static add(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is the sum of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ and \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static add(x: Value, y: Value): Decimal--><!--Device-Decimal-static add(x: Value, y: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| y | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## asin

```TypeScript
asin(): Decimal
```

Return a new Decimal whose value is the arcsine (inverse sine) in radians of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-asin(): Decimal--><!--Device-Decimal-asin(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## asin

```TypeScript
static asin(n: Value): Decimal
```

Return a new Decimal whose value is the arcsine in radians of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static asin(n: Value): Decimal--><!--Device-Decimal-static asin(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## asinh

```TypeScript
asinh(): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic sine in radians of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-asinh(): Decimal--><!--Device-Decimal-asinh(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## asinh

```TypeScript
static asinh(n: Value): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic sine of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static asinh(n: Value): Decimal--><!--Device-Decimal-static asinh(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## atan

```TypeScript
atan(): Decimal
```

Return a new Decimal whose value is the arctangent (inverse tangent) in radians of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-atan(): Decimal--><!--Device-Decimal-atan(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## atan

```TypeScript
static atan(n: Value): Decimal
```

Return a new Decimal whose value is the arctangent in radians of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static atan(n: Value): Decimal--><!--Device-Decimal-static atan(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## atan2

```TypeScript
static atan2(y: Value, x: Value): Decimal
```

Return a new Decimal whose value is the arctangent in radians of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ in the range -pi to pi (inclusive), rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static atan2(y: Value, x: Value): Decimal--><!--Device-Decimal-static atan2(y: Value, x: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| y | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} The y-coordinate. |
| x | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} The x-coordinate. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## atanh

```TypeScript
atanh(): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic tangent in radians of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-atanh(): Decimal--><!--Device-Decimal-atanh(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## atanh

```TypeScript
static atanh(n: Value): Decimal
```

Return a new Decimal whose value is the inverse of the hyperbolic tangent of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static atanh(n: Value): Decimal--><!--Device-Decimal-static atanh(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## cbrt

```TypeScript
cbrt(): Decimal
```

Return a new Decimal whose value is the cube root of the value of this Decimal, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-cbrt(): Decimal--><!--Device-Decimal-cbrt(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## cbrt

```TypeScript
static cbrt(n: Value): Decimal
```

Return a new Decimal whose value is the cube root of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static cbrt(n: Value): Decimal--><!--Device-Decimal-static cbrt(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## ceil

```TypeScript
ceil(): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a whole number in the direction of positive Infinity.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-ceil(): Decimal--><!--Device-Decimal-ceil(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## ceil

```TypeScript
static ceil(n: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ rounded to an integer using \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static ceil(n: Value): Decimal--><!--Device-Decimal-static ceil(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## clamp

```TypeScript
clamp(min: Value, max: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal clamped to the range delineated by \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ and \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-clamp(min: Value, max: Value): Decimal--><!--Device-Decimal-clamp(min: Value, max: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| min | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| max | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## clamp

```TypeScript
static clamp(n: Value, min: Value, max: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ clamped to the range delineated by \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ and \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static clamp(n: Value, min: Value, max: Value): Decimal--><!--Device-Decimal-static clamp(n: Value, min: Value, max: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| min | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| max | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## comparedTo

ArkTS-Dyn:
```TypeScript
comparedTo(n: Value): number
```

ArkTS-Sta:
```TypeScript
comparedTo(n: Value): double
```

Return 1 if the value of this Decimal is greater than the value of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, -1 if the value of this Decimal is less than the value of \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, 0 if they have the same value, NaN if the value of either Decimal is NaN.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-comparedTo(n: Value): double--><!--Device-Decimal-comparedTo(n: Value): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | the number type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## constructor

```TypeScript
constructor(n: Value)
```

Return a new Decimal whose value is the absolute value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-constructor(n: Value)--><!--Device-Decimal-constructor(n: Value)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## cos

```TypeScript
cos(): Decimal
```

Return a new Decimal whose value is the cosine of the value in radians of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-cos(): Decimal--><!--Device-Decimal-cos(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## cos

```TypeScript
static cos(n: Value): Decimal
```

Return a new Decimal whose value is the cosine of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static cos(n: Value): Decimal--><!--Device-Decimal-static cos(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## cosh

```TypeScript
cosh(): Decimal
```

Return a new Decimal whose value is the hyperbolic cosine of the value in radians of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-cosh(): Decimal--><!--Device-Decimal-cosh(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## cosh

```TypeScript
static cosh(n: Value): Decimal
```

Return a new Decimal whose value is the hyperbolic cosine of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to precision significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static cosh(n: Value): Decimal--><!--Device-Decimal-static cosh(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## decimalPlaces

ArkTS-Dyn:
```TypeScript
decimalPlaces(): number
```

ArkTS-Sta:
```TypeScript
decimalPlaces(): double
```

Return the number of decimal places of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-decimalPlaces(): double--><!--Device-Decimal-decimalPlaces(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | the number type |

## div

```TypeScript
div(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal divided by \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-div(n: Value): Decimal--><!--Device-Decimal-div(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## div

```TypeScript
static div(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ divided by \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static div(x: Value, y: Value): Decimal--><!--Device-Decimal-static div(x: Value, y: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| y | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## dividedToIntegerBy

```TypeScript
dividedToIntegerBy(n: Value): Decimal
```

Return a new Decimal whose value is the integer part of dividing the value of this Decimal by the value of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-dividedToIntegerBy(n: Value): Decimal--><!--Device-Decimal-dividedToIntegerBy(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## equals

```TypeScript
equals(n: Value): boolean
```

Return true if the value of this Decimal is equal to the value of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-equals(n: Value): boolean--><!--Device-Decimal-equals(n: Value): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## exp

```TypeScript
exp(): Decimal
```

Return a new Decimal whose value is the natural exponential of the value of this Decimal, i.e. the base e raised to the power the value of this Decimal, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-exp(): Decimal--><!--Device-Decimal-exp(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## exp

```TypeScript
static exp(n: Value): Decimal
```

Return a new Decimal whose value is the natural exponential of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static exp(n: Value): Decimal--><!--Device-Decimal-static exp(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## floor

```TypeScript
floor(): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a whole number in the direction of negative Infinity.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-floor(): Decimal--><!--Device-Decimal-floor(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## floor

```TypeScript
static floor(n: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ round to an integer using \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static floor(n: Value): Decimal--><!--Device-Decimal-static floor(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## greaterThan

```TypeScript
greaterThan(n: Value): boolean
```

Return true if the value of this Decimal is greater than the value of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-greaterThan(n: Value): boolean--><!--Device-Decimal-greaterThan(n: Value): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(n: Value): boolean
```

Return true if the value of this Decimal is greater than or equal to the value of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-greaterThanOrEqualTo(n: Value): boolean--><!--Device-Decimal-greaterThanOrEqualTo(n: Value): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## hypot

```TypeScript
static hypot(...n: Value[]): Decimal
```

Return a new Decimal whose value is the square root of the sum of the squares of the arguments, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static hypot(...n: Value[]): Decimal--><!--Device-Decimal-static hypot(...n: Value[]): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | {double \| string \| Decimal} Decimal |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## isFinite

```TypeScript
isFinite(): boolean
```

Return true if the value of this Decimal is a finite number, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-isFinite(): boolean--><!--Device-Decimal-isFinite(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

## isInteger

```TypeScript
isInteger(): boolean
```

Return true if the value of this Decimal is an integer, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-isInteger(): boolean--><!--Device-Decimal-isInteger(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

## isNaN

```TypeScript
isNaN(): boolean
```

Return true if the value of this Decimal is NaN, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-isNaN(): boolean--><!--Device-Decimal-isNaN(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

## isNegative

```TypeScript
isNegative(): boolean
```

Return true if the value of this Decimal is negative, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-isNegative(): boolean--><!--Device-Decimal-isNegative(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

## isPositive

```TypeScript
isPositive(): boolean
```

Return true if the value of this Decimal is positive, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-isPositive(): boolean--><!--Device-Decimal-isPositive(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

## isZero

```TypeScript
isZero(): boolean
```

Return true if the value of this Decimal is 0 or -0, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-isZero(): boolean--><!--Device-Decimal-isZero(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

## lessThan

```TypeScript
lessThan(n: Value): boolean
```

Return true if the value of this Decimal is less than \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-lessThan(n: Value): boolean--><!--Device-Decimal-lessThan(n: Value): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(n: Value): boolean
```

Return true if the value of this Decimal is less than or equal to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, otherwise return false.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-lessThanOrEqualTo(n: Value): boolean--><!--Device-Decimal-lessThanOrEqualTo(n: Value): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## ln

```TypeScript
ln(): Decimal
```

Return a new Decimal whose value is the natural logarithm of the value of this Decimal, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-ln(): Decimal--><!--Device-Decimal-ln(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## ln

```TypeScript
static ln(n: Value): Decimal
```

Return a new Decimal whose value is the natural logarithm of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static ln(n: Value): Decimal--><!--Device-Decimal-static ln(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## log

```TypeScript
log(n: Value): Decimal
```

Return the logarithm of the value of this Decimal to the specified base, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-log(n: Value): Decimal--><!--Device-Decimal-log(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## log

```TypeScript
static log(n: Value, base: Value): Decimal
```

Return a new Decimal whose value is the log of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ to the base \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static log(n: Value, base: Value): Decimal--><!--Device-Decimal-static log(n: Value, base: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| base | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## log10

```TypeScript
static log10(n: Value): Decimal
```

Return a new Decimal whose value is the base 10 logarithm of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static log10(n: Value): Decimal--><!--Device-Decimal-static log10(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## log2

```TypeScript
static log2(n: Value): Decimal
```

Return a new Decimal whose value is the base 2 logarithm of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static log2(n: Value): Decimal--><!--Device-Decimal-static log2(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## max

```TypeScript
static max(...n: Value[]): Decimal
```

Return a new Decimal whose value is the maximum of the arguments.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static max(...n: Value[]): Decimal--><!--Device-Decimal-static max(...n: Value[]): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## min

```TypeScript
static min(...n: Value[]): Decimal
```

Return a new Decimal whose value is the minimum of the arguments.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static min(...n: Value[]): Decimal--><!--Device-Decimal-static min(...n: Value[]): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## mod

```TypeScript
mod(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal modulo \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-mod(n: Value): Decimal--><!--Device-Decimal-mod(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## mod

```TypeScript
static mod(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ modulo \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static mod(x: Value, y: Value): Decimal--><!--Device-Decimal-static mod(x: Value, y: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| y | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## mul

```TypeScript
mul(n: Value): Decimal
```

Return a new Decimal whose value is this Decimal times \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-mul(n: Value): Decimal--><!--Device-Decimal-mul(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## mul

```TypeScript
static mul(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ multiplied by \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static mul(x: Value, y: Value): Decimal--><!--Device-Decimal-static mul(x: Value, y: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| y | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## negate

```TypeScript
negate(): Decimal
```

Return a new Decimal whose value is the value of this Decimal negated, i.e. as if multiplied by -1.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-negate(): Decimal--><!--Device-Decimal-negate(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## pow

```TypeScript
pow(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal raised to the power \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-pow(n: Value): Decimal--><!--Device-Decimal-pow(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## pow

```TypeScript
static pow(base: Value, exponent: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ raised to the power \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to precision significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static pow(base: Value, exponent: Value): Decimal--><!--Device-Decimal-static pow(base: Value, exponent: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| base | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} The base. |
| exponent | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} The exponent. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200060](../../errorcode-utils.md#10200060-precision-limit-is-exceeded) | Precision limit exceeded. |

## precision

ArkTS-Dyn:
```TypeScript
precision(): number
```

ArkTS-Sta:
```TypeScript
precision(): double
```

Return the number of significant digits of the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-precision(): double--><!--Device-Decimal-precision(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | the number type |

## precision

ArkTS-Dyn:
```TypeScript
precision(includeZeros: boolean | number): number
```

ArkTS-Sta:
```TypeScript
precision(includeZeros: boolean | int): double
```

Return the number of significant digits of the value of this Decimal, whether to count integer-part trailing zeros.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-precision(includeZeros: boolean | int): double--><!--Device-Decimal-precision(includeZeros: boolean | int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| includeZeros | ArkTS-Dyn: boolean \| number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：boolean \| int | Yes | Whether to count integer-part trailing zeros: true, false, |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | the number type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## random

```TypeScript
static random(): Decimal
```

Returns a new Decimal with a random value equal to or greater than 0 and less than 1.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static random(): Decimal--><!--Device-Decimal-static random(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200061](../../errorcode-utils.md#10200061-encryption-method-is-unavailable) | Crypto unavailable |

## random

ArkTS-Dyn:
```TypeScript
static random(significantDigits: number): Decimal
```

ArkTS-Sta:
```TypeScript
static random(significantDigits: double): Decimal
```

Returns a new Decimal with a random value equal to or greater than 0 and less than 1, and with \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits (or less if trailing zeros are produced).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static random(significantDigits: double): Decimal--><!--Device-Decimal-static random(significantDigits: double): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | {number} Significant digits. Integer, 0 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. [since 12 - 17] |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200061](../../errorcode-utils.md#10200061-encryption-method-is-unavailable) | Crypto unavailable |

## round

```TypeScript
static round(n: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ rounded to an integer using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static round(n: Value): Decimal--><!--Device-Decimal-static round(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## set

```TypeScript
static set(config: DecimalConfig): void
```

Configures the 'global' settings for this particular Decimal constructor.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static set(config: DecimalConfig): void--><!--Device-Decimal-static set(config: DecimalConfig): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |
| [10200061](../../errorcode-utils.md#10200061-encryption-method-is-unavailable) | Crypto unavailable |

## sign

ArkTS-Dyn:
```TypeScript
static sign(n: Value): number
```

ArkTS-Sta:
```TypeScript
static sign(n: Value): double
```

Return the sign of the passed value to the method. 1 if x > 0, -1 if x < 0, 0 if x is 0, -0 if x is -0, NaN otherwise

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static sign(n: Value): double--><!--Device-Decimal-static sign(n: Value): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 - 17 |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | the Decimal type\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 18 and later |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## sin

```TypeScript
sin(): Decimal
```

Return a new Decimal whose value is the sine of the value in radians of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-sin(): Decimal--><!--Device-Decimal-sin(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## sin

```TypeScript
static sin(n: Value): Decimal
```

Return a new Decimal whose value is the sine of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static sin(n: Value): Decimal--><!--Device-Decimal-static sin(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## sinh

```TypeScript
sinh(): Decimal
```

Return a new Decimal whose value is the hyperbolic sine of the value in radians of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-sinh(): Decimal--><!--Device-Decimal-sinh(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## sinh

```TypeScript
static sinh(n: Value): Decimal
```

Return a new Decimal whose value is the hyperbolic sine of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static sinh(n: Value): Decimal--><!--Device-Decimal-static sinh(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## sqrt

```TypeScript
sqrt(): Decimal
```

Return a new Decimal whose value is the square root of this Decimal, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-sqrt(): Decimal--><!--Device-Decimal-sqrt(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## sqrt

```TypeScript
static sqrt(n: Value): Decimal
```

Return a new Decimal whose value is the square root of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static sqrt(n: Value): Decimal--><!--Device-Decimal-static sqrt(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## sub

```TypeScript
sub(n: Value): Decimal
```

Return a new Decimal whose value is the value of this Decimal minus \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-sub(n: Value): Decimal--><!--Device-Decimal-sub(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## sub

```TypeScript
static sub(x: Value, y: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ minus \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static sub(x: Value, y: Value): Decimal--><!--Device-Decimal-static sub(x: Value, y: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| y | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## sum

```TypeScript
static sum(...n: Value[]): Decimal
```

Return a new Decimal whose value is the sum of the arguments, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_. Only the result is rounded, not the intermediate calculations.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static sum(...n: Value[]): Decimal--><!--Device-Decimal-static sum(...n: Value[]): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## tan

```TypeScript
tan(): Decimal
```

Return a new Decimal whose value is the tangent of the value in radians of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-tan(): Decimal--><!--Device-Decimal-tan(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## tan

```TypeScript
static tan(n: Value): Decimal
```

Return a new Decimal whose value is the tangent of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static tan(n: Value): Decimal--><!--Device-Decimal-static tan(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## tanh

```TypeScript
tanh(): Decimal
```

Return a new Decimal whose value is the hyperbolic tangent of the value in radians of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-tanh(): Decimal--><!--Device-Decimal-tanh(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## tanh

```TypeScript
static tanh(n: Value): Decimal
```

Return a new Decimal whose value is the hyperbolic tangent of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static tanh(n: Value): Decimal--><!--Device-Decimal-static tanh(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} A value in radians. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## toBinary

```TypeScript
toBinary(): string
```

Return a string representing the value of this Decimal in base 2.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toBinary(): string--><!--Device-Decimal-toBinary(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## toBinary

ArkTS-Dyn:
```TypeScript
toBinary(significantDigits: number): string
```

ArkTS-Sta:
```TypeScript
toBinary(significantDigits: double): string
```

Return a string representing the value of this Decimal in base 2, round to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toBinary(significantDigits: double): string--><!--Device-Decimal-toBinary(significantDigits: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toBinary

ArkTS-Dyn:
```TypeScript
toBinary(significantDigits: number, rounding: Rounding): string
```

ArkTS-Sta:
```TypeScript
toBinary(significantDigits: double, rounding: Rounding): string
```

Return a string representing the value of this Decimal in base 2, round to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toBinary(significantDigits: double, rounding: Rounding): string--><!--Device-Decimal-toBinary(significantDigits: double, rounding: Rounding): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toDecimalPlaces

```TypeScript
toDecimalPlaces(): Decimal
```

Return a new Decimal whose value is the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toDecimalPlaces(): Decimal--><!--Device-Decimal-toDecimalPlaces(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## toDecimalPlaces

ArkTS-Dyn:
```TypeScript
toDecimalPlaces(decimalPlaces: number): Decimal
```

ArkTS-Sta:
```TypeScript
toDecimalPlaces(decimalPlaces: double): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ decimal places.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toDecimalPlaces(decimalPlaces: double): Decimal--><!--Device-Decimal-toDecimalPlaces(decimalPlaces: double): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decimalPlaces | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toDecimalPlaces

ArkTS-Dyn:
```TypeScript
toDecimalPlaces(decimalPlaces: number, rounding: Rounding): Decimal
```

ArkTS-Sta:
```TypeScript
toDecimalPlaces(decimalPlaces: double, rounding: Rounding): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ decimal places using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toDecimalPlaces(decimalPlaces: double, rounding: Rounding): Decimal--><!--Device-Decimal-toDecimalPlaces(decimalPlaces: double, rounding: Rounding): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decimalPlaces | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toExponential

```TypeScript
toExponential(): string
```

Return a string representing the value of this Decimal in exponential notation.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toExponential(): string--><!--Device-Decimal-toExponential(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## toExponential

ArkTS-Dyn:
```TypeScript
toExponential(decimalPlaces: number): string
```

ArkTS-Sta:
```TypeScript
toExponential(decimalPlaces: double): string
```

Return a string representing the value of this Decimal in exponential notation rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ fixed decimal places.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toExponential(decimalPlaces: double): string--><!--Device-Decimal-toExponential(decimalPlaces: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decimalPlaces | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Decimal places. Integer, 0 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toExponential

ArkTS-Dyn:
```TypeScript
toExponential(decimalPlaces: number, rounding: Rounding): string
```

ArkTS-Sta:
```TypeScript
toExponential(decimalPlaces: double, rounding: Rounding): string
```

Return a string representing the value of this Decimal in exponential notation rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ fixed decimal places using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toExponential(decimalPlaces: double, rounding: Rounding): string--><!--Device-Decimal-toExponential(decimalPlaces: double, rounding: Rounding): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decimalPlaces | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Decimal places. Integer, 0 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toFixed

```TypeScript
toFixed(): string
```

Return a string representing the value of this Decimal in normal (fixed-point).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toFixed(): string--><!--Device-Decimal-toFixed(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## toFixed

ArkTS-Dyn:
```TypeScript
toFixed(decimalPlaces: number): string
```

ArkTS-Sta:
```TypeScript
toFixed(decimalPlaces: double): string
```

Return a string representing the value of this Decimal in normal (fixed-point) notation to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ fixed decimal places.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toFixed(decimalPlaces: double): string--><!--Device-Decimal-toFixed(decimalPlaces: double): string-End-->

**System capability:** 
- API version 18 and later: SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decimalPlaces | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Decimal places. Integer, 0 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toFixed

ArkTS-Dyn:
```TypeScript
toFixed(decimalPlaces: number, rounding: Rounding): string
```

ArkTS-Sta:
```TypeScript
toFixed(decimalPlaces: double, rounding: Rounding): string
```

Return a string representing the value of this Decimal in normal (fixed-point) notation to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ fixed decimal places and rounded using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toFixed(decimalPlaces: double, rounding: Rounding): string--><!--Device-Decimal-toFixed(decimalPlaces: double, rounding: Rounding): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decimalPlaces | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Decimal places. Integer, 0 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toFraction

```TypeScript
toFraction(): Decimal[]
```

Return an array representing the value of this Decimal as a simple fraction with an integer numerator and an integer denominator.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toFraction(): Decimal[]--><!--Device-Decimal-toFraction(): Decimal[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_[] | the Decimal[] type |

## toFraction

```TypeScript
toFraction(maxDenominator: Value): Decimal[]
```

Return an array representing the value of this Decimal as a simple fraction with an integer numerator and an integer denominator. The denominator will be a positive non-zero value less than or equal to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toFraction(maxDenominator: Value): Decimal[]--><!--Device-Decimal-toFraction(maxDenominator: Value): Decimal[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxDenominator | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_[] | the Decimal[] type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## toHexadecimal

```TypeScript
toHexadecimal(): string
```

Return a string representing the value of this Decimal in base 16

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toHexadecimal(): string--><!--Device-Decimal-toHexadecimal(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## toHexadecimal

ArkTS-Dyn:
```TypeScript
toHexadecimal(significantDigits: number): string
```

ArkTS-Sta:
```TypeScript
toHexadecimal(significantDigits: double): string
```

Return a string representing the value of this Decimal in base 16, round to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toHexadecimal(significantDigits: double): string--><!--Device-Decimal-toHexadecimal(significantDigits: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toHexadecimal

ArkTS-Dyn:
```TypeScript
toHexadecimal(significantDigits: number, rounding: Rounding): string
```

ArkTS-Sta:
```TypeScript
toHexadecimal(significantDigits: double, rounding: Rounding): string
```

Return a string representing the value of this Decimal in base 16, round to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toHexadecimal(significantDigits: double, rounding: Rounding): string--><!--Device-Decimal-toHexadecimal(significantDigits: double, rounding: Rounding): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toNearest

```TypeScript
toNearest(n: Value): Decimal
```

Returns a new Decimal whose value is the nearest multiple of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toNearest(n: Value): Decimal--><!--Device-Decimal-toNearest(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## toNearest

```TypeScript
toNearest(n: Value, rounding: Rounding): Decimal
```

Returns a new Decimal whose value is the nearest multiple of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ in the direction of rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, to the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toNearest(n: Value, rounding: Rounding): Decimal--><!--Device-Decimal-toNearest(n: Value, rounding: Rounding): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toNumber

ArkTS-Dyn:
```TypeScript
toNumber(): number
```

ArkTS-Sta:
```TypeScript
toNumber(): double
```

Return the value of this Decimal converted to a number primitive. Zero keeps its sign.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toNumber(): double--><!--Device-Decimal-toNumber(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | the number type |

## toOctal

```TypeScript
toOctal(): string
```

Return a string representing the value of this Decimal in base 8.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toOctal(): string--><!--Device-Decimal-toOctal(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## toOctal

ArkTS-Dyn:
```TypeScript
toOctal(significantDigits: number): string
```

ArkTS-Sta:
```TypeScript
toOctal(significantDigits: double): string
```

Return a string representing the value of this Decimal in base 8, round to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toOctal(significantDigits: double): string--><!--Device-Decimal-toOctal(significantDigits: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toOctal

ArkTS-Dyn:
```TypeScript
toOctal(significantDigits: number, rounding: Rounding): string
```

ArkTS-Sta:
```TypeScript
toOctal(significantDigits: double, rounding: Rounding): string
```

Return a string representing the value of this Decimal in base 8, round to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toOctal(significantDigits: double, rounding: Rounding): string--><!--Device-Decimal-toOctal(significantDigits: double, rounding: Rounding): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | {double \| string \| Decimal} |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toPrecision

```TypeScript
toPrecision(): string
```

Return a string representing the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toPrecision(): string--><!--Device-Decimal-toPrecision(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## toPrecision

ArkTS-Dyn:
```TypeScript
toPrecision(significantDigits: number): string
```

ArkTS-Sta:
```TypeScript
toPrecision(significantDigits: double): string
```

Return a string representing the value of this Decimal rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toPrecision(significantDigits: double): string--><!--Device-Decimal-toPrecision(significantDigits: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toPrecision

ArkTS-Dyn:
```TypeScript
toPrecision(significantDigits: number, rounding: Rounding): string
```

ArkTS-Sta:
```TypeScript
toPrecision(significantDigits: double, rounding: Rounding): string
```

Return a string representing the value of this Decimal rounded to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toPrecision(significantDigits: double, rounding: Rounding): string--><!--Device-Decimal-toPrecision(significantDigits: double, rounding: Rounding): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toSignificantDigits

```TypeScript
toSignificantDigits(): Decimal
```

Return a new Decimal whose value is the value of this Decimal.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toSignificantDigits(): Decimal--><!--Device-Decimal-toSignificantDigits(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## toSignificantDigits

ArkTS-Dyn:
```TypeScript
toSignificantDigits(significantDigits: number): Decimal
```

ArkTS-Sta:
```TypeScript
toSignificantDigits(significantDigits: double): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toSignificantDigits(significantDigits: double): Decimal--><!--Device-Decimal-toSignificantDigits(significantDigits: double): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toSignificantDigits

ArkTS-Dyn:
```TypeScript
toSignificantDigits(significantDigits: number, rounding: Rounding): Decimal
```

ArkTS-Sta:
```TypeScript
toSignificantDigits(significantDigits: double, rounding: Rounding): Decimal
```

Return a new Decimal whose value is the value of this Decimal rounded to a maximum of \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ significant digits using rounding mode \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toSignificantDigits(significantDigits: double, rounding: Rounding): Decimal--><!--Device-Decimal-toSignificantDigits(significantDigits: double, rounding: Rounding): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| significantDigits | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Significant digits. Integer, 1 to MAX\_\_\_ESCAPED\_UNDERSCORE\_\_\_DIGITS inclusive. |
| rounding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Rounding mode. Integer, 0 to 8 inclusive. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../../errorcode-utils.md#10200001-value-out-of-range) | The value of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is out of range. |

## toString

```TypeScript
toString(): string
```

Return a string representing the value of this Decimal. Return exponential notation if this Decimal has a positive exponent equal to or greater than \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, or a negative exponent equal to or less than \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-toString(): string--><!--Device-Decimal-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## trunc

```TypeScript
trunc(): Decimal
```

Return a new Decimal whose value is the value of this Decimal truncated to a whole number.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-trunc(): Decimal--><!--Device-Decimal-trunc(): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

## trunc

```TypeScript
static trunc(n: Value): Decimal
```

Return a new Decimal whose value is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ truncated to an integer.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static trunc(n: Value): Decimal--><!--Device-Decimal-static trunc(n: Value): Decimal-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | {double \| string \| Decimal} |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the Decimal type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

## valueOf

```TypeScript
valueOf(): string
```

Return a string representing the value of this Decimal. Unlike \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, negative zero will include the minus sign.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-valueOf(): string--><!--Device-Decimal-valueOf(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string type |

## EUCLIDEAN

```TypeScript
static readonly EUCLIDEAN : 9
```

Not a rounding mode, see modulo

**Type:** 9

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly EUCLIDEAN : 9--><!--Device-Decimal-static readonly EUCLIDEAN : 9-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_CEILING

```TypeScript
static readonly ROUND_CEILING : 2
```

Rounds towards Infinity

**Type:** 2

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_CEILING : 2--><!--Device-Decimal-static readonly ROUND_CEILING : 2-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_DOWN

```TypeScript
static readonly ROUND_DOWN : 1
```

Rounds towards zero

**Type:** 1

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_DOWN : 1--><!--Device-Decimal-static readonly ROUND_DOWN : 1-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_FLOOR

```TypeScript
static readonly ROUND_FLOOR : 3
```

Rounds towards -Infinity

**Type:** 3

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_FLOOR : 3--><!--Device-Decimal-static readonly ROUND_FLOOR : 3-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_CEILING

```TypeScript
static readonly ROUND_HALF_CEILING : 7
```

Rounds towards nearest neighbour. If equidistant, rounds towards Infinity

**Type:** 7

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_HALF_CEILING : 7--><!--Device-Decimal-static readonly ROUND_HALF_CEILING : 7-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_DOWN

```TypeScript
static readonly ROUND_HALF_DOWN : 5
```

Rounds towards nearest neighbour. If equidistant, rounds towards zero

**Type:** 5

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_HALF_DOWN : 5--><!--Device-Decimal-static readonly ROUND_HALF_DOWN : 5-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_EVEN

```TypeScript
static readonly ROUND_HALF_EVEN : 6
```

Rounds towards nearest neighbour. If equidistant, rounds towards even neighbour

**Type:** 6

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_HALF_EVEN : 6--><!--Device-Decimal-static readonly ROUND_HALF_EVEN : 6-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_FLOOR

```TypeScript
static readonly ROUND_HALF_FLOOR : 8
```

Rounds towards nearest neighbour. If equidistant, rounds towards -Infinity

**Type:** 8

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_HALF_FLOOR : 8--><!--Device-Decimal-static readonly ROUND_HALF_FLOOR : 8-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_HALF_UP

```TypeScript
static readonly ROUND_HALF_UP : 4
```

Rounds towards nearest neighbour. If equidistant, rounds away from zero

**Type:** 4

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_HALF_UP : 4--><!--Device-Decimal-static readonly ROUND_HALF_UP : 4-End-->

**System capability:** SystemCapability.Utils.Lang

## ROUND_UP

```TypeScript
static readonly ROUND_UP : 0
```

Rounds away from zero

**Type:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-static readonly ROUND_UP : 0--><!--Device-Decimal-static readonly ROUND_UP : 0-End-->

**System capability:** SystemCapability.Utils.Lang

## d

```TypeScript
readonly d: number[]
```

The numbers of decimal digits.

**Type:** number[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-readonly d: number[]--><!--Device-Decimal-readonly d: number[]-End-->

**System capability:** SystemCapability.Utils.Lang

## e

```TypeScript
get e(): double
```

The number of decimal exponent.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-get e(): double--><!--Device-Decimal-get e(): double-End-->

**System capability:** SystemCapability.Utils.Lang

## s

```TypeScript
get s(): double
```

The number of decimal sign.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Decimal-get s(): double--><!--Device-Decimal-get s(): double-End-->

**System capability:** SystemCapability.Utils.Lang

