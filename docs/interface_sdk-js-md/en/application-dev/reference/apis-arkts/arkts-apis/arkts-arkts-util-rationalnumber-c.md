# RationalNumber

The rational number is mainly to compare rational numbers and obtain the numerator and denominator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-class RationalNumber--><!--Device-util-class RationalNumber-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
compare(another: RationalNumber): int
```

Compares the current RationalNumber object to the given object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-compare(another: RationalNumber): int--><!--Device-RationalNumber-compare(another: RationalNumber): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| another | [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | Yes | An object of other rational numbers |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns 0 or 1, or -1, depending on the comparison. |

## constructor

```TypeScript
constructor()
```

A constructor used to create a RationalNumber instance with a given numerator and denominator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-constructor()--><!--Device-RationalNumber-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## createRationalFromString

```TypeScript
static createRationalFromString(rationalString: string): RationalNumber
```

Creates a RationalNumber object based on a given string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-static createRationalFromString(rationalString: string): RationalNumber--><!--Device-RationalNumber-static createRationalFromString(rationalString: string): RationalNumber-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rationalString | string | Yes | String Expression of Rational Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | Returns a RationalNumber object generated based on the given string. |

## equals

```TypeScript
equals(obj: Object): boolean
```

Compares two objects for equality.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-equals(obj: Object): boolean--><!--Device-RationalNumber-equals(obj: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Object | Yes | An object |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the given object is the same as the current object; Otherwise, false is returned. |

## getCommonFactor

```TypeScript
static getCommonFactor(number1: long, number2: long): long
```

Get the greatest common factor of two integers.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-static getCommonFactor(number1: long, number2: long): long--><!--Device-RationalNumber-static getCommonFactor(number1: long, number2: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| number1 | long | Yes | Is an integer. |
| number2 | long | Yes | Is an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the greatest common factor of two integers, integer type. |

## getDenominator

```TypeScript
getDenominator(): long
```

Gets the denominator of the current object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-getDenominator(): long--><!--Device-RationalNumber-getDenominator(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the denominator of the current object. |

## getNumerator

```TypeScript
getNumerator(): long
```

Gets the numerator of the current object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-getNumerator(): long--><!--Device-RationalNumber-getNumerator(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the numerator of the current object. |

## isFinite

```TypeScript
isFinite(): boolean
```

Checks whether the current RationalNumber object represents an infinite value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-isFinite(): boolean--><!--Device-RationalNumber-isFinite(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the denominator is not 0, true is returned. Otherwise, false is returned. |

## isNaN

```TypeScript
isNaN(): boolean
```

Checks whether the current RationalNumber object represents a Not-a-Number (NaN) value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-isNaN(): boolean--><!--Device-RationalNumber-isNaN(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If both the denominator and numerator are 0, true is returned. Otherwise, false is returned. |

## isZero

```TypeScript
isZero(): boolean
```

Checks whether the current RationalNumber object represents the value 0.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-isZero(): boolean--><!--Device-RationalNumber-isZero(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the value represented by the current object is 0, true is returned. Otherwise, false is returned. |

## parseRationalNumber

```TypeScript
static parseRationalNumber(numerator: long, denominator: long): RationalNumber
```

Used to create a RationalNumber instance with a given numerator and denominator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-static parseRationalNumber(numerator: long, denominator: long): RationalNumber--><!--Device-RationalNumber-static parseRationalNumber(numerator: long, denominator: long): RationalNumber-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numerator | long | Yes | An integer number |
| denominator | long | Yes | An integer number |

**Return value:**

| Type | Description |
| --- | --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |  |

## toString

```TypeScript
toString(): string
```

Obtains a string representation of the current RationalNumber object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-toString(): string--><!--Device-RationalNumber-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns a string representation of the current RationalNumber object. |

## valueOf

```TypeScript
valueOf(): double
```

Gets integer and floating-point values of a rational number object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RationalNumber-valueOf(): double--><!--Device-RationalNumber-valueOf(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | Returns the integer and floating-point values of a rational number object. |

