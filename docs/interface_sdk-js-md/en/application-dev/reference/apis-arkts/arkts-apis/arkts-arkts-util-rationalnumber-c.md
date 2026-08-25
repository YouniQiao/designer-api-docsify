# RationalNumber

Provides APIs to compare rational numbers and obtain numerators and denominators. For example, the **toString()** API can be used to convert a rational number into a string.

**Since:** 8

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
compare(another: RationalNumber): number
```

Compares the current RationalNumber object to the given object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| another | [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## compareTo

```TypeScript
compareTo(another: RationalNumber): number
```

Compares the current RationalNumber object to the given object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** compare

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| another | [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## constructor

```TypeScript
constructor(numerator: number, denominator: number)
```

A constructor used to create a **RationalNumber** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [parseRationalNumber](#parserationalnumber)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| numerator | number | Yes |
| denominator | number | Yes |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **RationalNumber** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## createRationalFromString

```TypeScript
static createRationalFromString(rationalString: string): RationalNumber
```

Creates a **RationalNumber** object based on the given string.

> **NOTE：**&gt;
> The **rationalString** parameter must be a string. If a decimal string is passed in, the function is not
> intercepted, but the error message "createRationalFromString: The type of Parameter must be integer string" is
> displayed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rationalString | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |

## equals

```TypeScript
equals(obj: Object): boolean
```

Checks whether this **RationalNumber** object equals the given object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Object | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getCommonDivisor

```TypeScript
static getCommonDivisor(number1: number, number2: number): number
```

Obtains the greatest common divisor of two specified integers.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getCommonFactor](#getcommonfactor)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| number1 | number | Yes |
| number2 | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCommonFactor

```TypeScript
static getCommonFactor(number1: number, number2: number): number
```

Obtains the greatest common divisor of two specified integers.

> **NOTE：**&gt;
> The **number1** and **number2** parameters must be integers. If a decimal number is passed in, the function is
> not intercepted, but the error message "getCommonFactor: The type of Parameter must be integer" is displayed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| number1 | number | Yes |
| number2 | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getDenominator

```TypeScript
getDenominator(): number
```

Obtains the denominator of this **RationalNumber** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getNumerator

```TypeScript
getNumerator(): number
```

Obtains the numerator of this **RationalNumber** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## isFinite

```TypeScript
isFinite(): boolean
```

Checks whether this **RationalNumber** object represents a finite value.

**Since:** 8

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

Checks whether this **RationalNumber** object is a Not a Number (NaN).

**Since:** 8

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

Checks whether this **RationalNumber** object is **0**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## parseRationalNumber

```TypeScript
static parseRationalNumber(numerator: number, denominator: number): RationalNumber
```

Creates a **RationalNumber** instance with a given numerator and denominator.

> **NOTE：**&gt;
> The **numerator** and **denominator** parameters must be integers. If a decimal number is passed in, the
> function is not intercepted, but the error message "parseRationalNumber: The type of Parameter must be integer"
> is displayed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| numerator | number | Yes |
| denominator | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |

## toString

```TypeScript
toString(): string
```

Obtains the string representation of this **RationalNumber** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## valueOf

```TypeScript
valueOf(): number
```

Obtains the integer or floating-point value of this **RationalNumber** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
