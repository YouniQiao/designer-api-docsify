# ScopeHelper

Provides APIs to define the valid range of a field. The constructor of this class creates comparable objects with lower and upper limits.

**Since:** 9

<!--Device-util-class ScopeHelper--><!--Device-util-class ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Value specified. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Returns **lowerObj** if the specified value is less than the lower limit; returns **upperObj** if the specified value is greater than the upper limit; returns the specified value if it is within this **Scope**. |

**Examples**

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

A constructor used to create a **ScopeHelper** object with the specified upper and lower limits.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-constructor(lowerObj: ScopeType, upperObj: ScopeType)--><!--Device-ScopeHelper-constructor(lowerObj: ScopeType, upperObj: ScopeType)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Lower limit of the **Scope** object. |
| upperObj | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Upper limit of the **Scope** object. |

**Examples**

```TypeScript
let textDecoder = new util.TextDecoder();
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// Output: retStr = utf-8
```

```TypeScript
let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
```

```TypeScript
let textEncoder = new util.TextEncoder();
```

```TypeScript
let textEncoder = new util.TextEncoder("utf-8");
```

```TypeScript
let rationalNumber = new util.RationalNumber();
```

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
```

```TypeScript
let pro = new util.LRUCache<number, number>();
```

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

```TypeScript
let base64 = new util.Base64Helper();
```

```TypeScript
let decoder = new util.StringDecoder();
```

```TypeScript
let type = new util.types();
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
```

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

```TypeScript
let base64 = new  util.Base64();
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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Value specified. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** is returned if the value is within this **Scope**; otherwise, **false** is returned. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.contains(2);
console.info('result = ' + result);
// Output: result = true
```

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

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.contains(20);
console.info('result = ' + result);
// Output: result = false
```

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Yes | Scope** specified. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** is returned if the range is within this **Scope**; otherwise, **false** is returned. |

**Examples**

See [contains](#contains)

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Lower limit. |
| upperObj | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Upper limit. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Union set of this **Scope** and the given lower and upper limits. |

**Examples**

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Yes | Scope** specified. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Union set of this **Scope** and the given **Scope**. |

**Examples**

See [expand](#expand)

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Value specified. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Union set of this **Scope** and the given value. |

**Examples**

See [expand](#expand)

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

| Type | Description |
| --- | --- |
| [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Lower limit of this **Scope**. |

**Examples**

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

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-getUpper(): ScopeType--><!--Device-ScopeHelper-getUpper(): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Upper limit of this **Scope**. |

**Examples**

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
intersect(range: ScopeHelper): ScopeHelper
```

Obtains the intersection of this **Scope** and the given **Scope**. If the intersection is empty, an exception is thrown.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScopeHelper-intersect(range: ScopeHelper): ScopeHelper--><!--Device-ScopeHelper-intersect(range: ScopeHelper): ScopeHelper-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Yes | Scope** specified. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Intersection of this **Scope** and the given **Scope**. |

**Examples**

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Lower limit. |
| upperObj | [ScopeType](../../apis-default/arkts-apis/arkts-util-scopetype-t.md) | Yes | Upper limit. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](../../apis-default/arkts-apis/arkts-util-scopehelper-c.md) | Intersection of this **Scope** and the given lower and upper limits. |

**Examples**

See [intersect](#intersect)

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

| Type | Description |
| --- | --- |
| string | String representation containing the **Scope**. |

**Examples**

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// Output: result = 1/2
```

You are advised to use the following code snippet for API version 9 and later versions:

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// Output: result = 1/2
```

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
pro.get(3);
console.info(pro.toString());
// Output: LRUCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
// maxSize: maximum size of the cache. hits: number of matched queries. misses: number of mismatched queries. hitRate: matching rate.
```

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

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
pro.remove(20);
let result = pro.toString();
console.info("result = " + result);
// Output: result = Lrubuffer[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% ]
```

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

