# ScopeHelper

Provides APIs to define the valid range of a field. The constructor of this class creates comparable objects with lower and upper limits.

**Since:** 9

<!--Device-util-class ScopeHelper--><!--Device-util-class ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## clamp

```TypeScript
clamp(value: ScopeType): ScopeType
```

Limits a value to this **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-clamp(value: ScopeType): ScopeType--><!--Device-ScopeHelper-clamp(value: ScopeType): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// Output: result = 35
```

## constructor

```TypeScript
constructor(lowerObj: ScopeType, upperObj: ScopeType)
```

A constructor used to create a **ScopeHelper** object with the specified upper and lower limits.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-constructor(lowerObj: ScopeType, upperObj: ScopeType)--><!--Device-ScopeHelper-constructor(lowerObj: ScopeType, upperObj: ScopeType)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}
let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = [30, 40]
```

## contains

```TypeScript
contains(value: ScopeType): boolean
```

Checks whether a range is within this **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-contains(value: ScopeType): boolean--><!--Device-ScopeHelper-contains(value: ScopeType): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// Output: result = true
```

## contains

```TypeScript
contains(range: ScopeHelper): boolean
```

Checks whether a range is within this **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-contains(range: ScopeHelper): boolean--><!--Device-ScopeHelper-contains(range: ScopeHelper): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.ScopeHelper(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// Output: result = false
```

## expand

```TypeScript
expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper
```

Obtains the union set of this **Scope** and the given lower and upper limits.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper--><!--Device-ScopeHelper-expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = [30, 40]
```

## expand

```TypeScript
expand(range: ScopeHelper): ScopeHelper
```

Obtains the union set of this **Scope** and the given **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-expand(range: ScopeHelper): ScopeHelper--><!--Device-ScopeHelper-expand(range: ScopeHelper): ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// Output: result = [30, 40]
```

## expand

```TypeScript
expand(value: ScopeType): ScopeHelper
```

Obtains the union set of this **Scope** and the given value.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-expand(value: ScopeType): ScopeHelper--><!--Device-ScopeHelper-expand(value: ScopeType): ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// Output: result = [30, 40]
```

## getLower

```TypeScript
getLower(): ScopeType
```

Obtains the lower limit of this **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-getLower(): ScopeType--><!--Device-ScopeHelper-getLower(): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// Output: result = 30
```

## getUpper

```TypeScript
getUpper(): ScopeType
```

Obtains the upper limit of this **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-getUpper(): ScopeType--><!--Device-ScopeHelper-getUpper(): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// Output: result = 40
```

## intersect

```TypeScript
intersect(range: ScopeHelper): ScopeHelper
```

Obtains the intersection of this **Scope** and the given **Scope**. If the intersection is empty, an exception is thrown.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-intersect(range: ScopeHelper): ScopeHelper--><!--Device-ScopeHelper-intersect(range: ScopeHelper): ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
let result = range.intersect(rangeFir);
console.info("result = " + result);
// Output: result = [35, 39]
```

## intersect

```TypeScript
intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper
```

Obtains the intersection of this **Scope** and the given lower and upper limits. If the intersection is empty, an exception is thrown.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper--><!--Device-ScopeHelper-intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = [35, 39]
```

## toString

```TypeScript
toString(): string
```

Obtains a string representation that contains this **Scope**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-toString(): string--><!--Device-ScopeHelper-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// Output: result = [30, 40]
```
