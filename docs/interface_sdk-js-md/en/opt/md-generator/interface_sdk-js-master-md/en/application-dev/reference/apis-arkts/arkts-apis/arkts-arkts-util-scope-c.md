# Scope

The Scope interface is used to describe the valid range of a field.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper](arkts-arkts-util-scopehelper-c.md)

<!--Device-util-class Scope--><!--Device-util-class Scope-End-->

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper.clamp](arkts-arkts-util-scopehelper-c.md#clamp)

<!--Device-Scope-clamp(value: ScopeType): ScopeType--><!--Device-Scope-clamp(value: ScopeType): ScopeType-End-->

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// Output: result = 35
```

## constructor

```TypeScript
constructor(lowerObj: ScopeType, upperObj: ScopeType)
```

A constructor used to create a **Scope** object with the specified upper and lower limits.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.constructor

<!--Device-Scope-constructor(lowerObj: ScopeType, upperObj: ScopeType)--><!--Device-Scope-constructor(lowerObj: ScopeType, upperObj: ScopeType)-End-->

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
let range = new util.Scope(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = [30, 40]
```

## contains

```TypeScript
contains(value: ScopeType): boolean
```

Checks whether a value is within this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.contains](arkts-arkts-util-lrucache-c.md#contains)

<!--Device-Scope-contains(value: ScopeType): boolean--><!--Device-Scope-contains(value: ScopeType): boolean-End-->

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// Output: result = true
```

## contains

```TypeScript
contains(range: Scope): boolean
```

Checks whether a range is within this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.contains](arkts-arkts-util-lrucache-c.md#contains)

<!--Device-Scope-contains(range: Scope): boolean--><!--Device-Scope-contains(range: Scope): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes |

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
let range = new util.Scope(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.Scope(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// Output: result = false
```

## expand

```TypeScript
expand(lowerObj: ScopeType, upperObj: ScopeType): Scope
```

Obtains the union set of this **Scope** and the given lower and upper limits.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.expand

<!--Device-Scope-expand(lowerObj: ScopeType, upperObj: ScopeType): Scope--><!--Device-Scope-expand(lowerObj: ScopeType, upperObj: ScopeType): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = [30, 40]
```

## expand

```TypeScript
expand(range: Scope): Scope
```

Obtains the union set of this **Scope** and the given **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.expand

<!--Device-Scope-expand(range: Scope): Scope--><!--Device-Scope-expand(range: Scope): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

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
let range = new util.Scope(tempLower, tempUpper);
let rangeFir = new util.Scope(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// Output: result = [30, 40]
```

## expand

```TypeScript
expand(value: ScopeType): Scope
```

Obtains the union set of this **Scope** and the given value.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.expand

<!--Device-Scope-expand(value: ScopeType): Scope--><!--Device-Scope-expand(value: ScopeType): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// Output: result = [30, 40]
```

## getLower

```TypeScript
getLower(): ScopeType
```

Obtains the lower limit of this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper.getLower](arkts-arkts-util-scopehelper-c.md#getlower)

<!--Device-Scope-getLower(): ScopeType--><!--Device-Scope-getLower(): ScopeType-End-->

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// Output: result = 30
```

## getUpper

```TypeScript
getUpper(): ScopeType
```

Obtains the upper limit of this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper.getUpper](arkts-arkts-util-scopehelper-c.md#getupper)

<!--Device-Scope-getUpper(): ScopeType--><!--Device-Scope-getUpper(): ScopeType-End-->

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// Output: result = 40
```

## intersect

```TypeScript
intersect(range: Scope): Scope
```

Obtains the intersection of this **Scope** and the given **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.intersect

<!--Device-Scope-intersect(range: Scope): Scope--><!--Device-Scope-intersect(range: Scope): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

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
let range = new util.Scope(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.Scope(tempMiDF, tempMidS);
let result = range.intersect(rangeFir );
console.info("result = " + result);
  // Output: result = [35, 39]
```

## intersect

```TypeScript
intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope
```

Obtains the intersection of this **Scope** and the given lower and upper limits.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.intersect

<!--Device-Scope-intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope--><!--Device-Scope-intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = [35, 39]
```

## toString

```TypeScript
toString(): string
```

Obtains a string representation that contains this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.toString](arkts-arkts-util-lrucache-c.md#tostring)

<!--Device-Scope-toString(): string--><!--Device-Scope-toString(): string-End-->

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
let range = new util.Scope(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// Output: result = [30, 40]
```
