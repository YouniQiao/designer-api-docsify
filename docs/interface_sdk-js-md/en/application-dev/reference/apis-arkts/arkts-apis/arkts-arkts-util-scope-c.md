# Scope

Scope 接口用于描述字段的有效范围。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

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

将一个值限制在此 **Scope** 范围内。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper.clamp](arkts-arkts-util-scopehelper-c.md#clamp)

<!--Device-Scope-clamp(value: ScopeType): ScopeType--><!--Device-Scope-clamp(value: ScopeType): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | 如果指定值小于下限，则返回 **lowerObj**；如果指定值大于上限，则返回 **upperObj**；如果 在此 **Scope** 范围内，则返回指定值。 |

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

用于创建具有指定上下限的 **Scope** 对象的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.constructor

<!--Device-Scope-constructor(lowerObj: ScopeType, upperObj: ScopeType)--><!--Device-Scope-constructor(lowerObj: ScopeType, upperObj: ScopeType)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | Scope** 对象的下限。 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | Scope** 对象的上限。 |

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

判断一个值是否在此 **Scope** 范围内。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.contains](arkts-arkts-util-lrucache-c.md#contains)

<!--Device-Scope-contains(value: ScopeType): boolean--><!--Device-Scope-contains(value: ScopeType): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查结果。如果值在此 **Scope** 范围内，则返回 **true**；否则返回 **false**。 |

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

判断一个范围是否在此 **Scope** 范围内。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.contains](arkts-arkts-util-lrucache-c.md#contains)

<!--Device-Scope-contains(range: Scope): boolean--><!--Device-Scope-contains(range: Scope): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes | 指定的 **Scope**。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查结果。如果范围在此 **Scope** 范围内，则返回 **true**；否则返回 **false**。 |

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

获取此 **Scope** 与给定上下限的并集。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.expand

<!--Device-Scope-expand(lowerObj: ScopeType, upperObj: ScopeType): Scope--><!--Device-Scope-expand(lowerObj: ScopeType, upperObj: ScopeType): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 下限。 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 上限。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Scope](arkts-arkts-util-scope-c.md) | 此 **Scope** 与给定上下限的并集。 |

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

获取此 **Scope** 与给定 **Scope** 的并集。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.expand

<!--Device-Scope-expand(range: Scope): Scope--><!--Device-Scope-expand(range: Scope): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes | 指定的 **Scope**。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Scope](arkts-arkts-util-scope-c.md) | 此 **Scope** 与给定 **Scope** 的并集。 |

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

获取此 **Scope** 与给定值的并集。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.expand

<!--Device-Scope-expand(value: ScopeType): Scope--><!--Device-Scope-expand(value: ScopeType): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Scope](arkts-arkts-util-scope-c.md) | 此 **Scope** 与给定值的并集。 |

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

获取此 **Scope** 的下限。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper.getLower](arkts-arkts-util-scopehelper-c.md#getlower)

<!--Device-Scope-getLower(): ScopeType--><!--Device-Scope-getLower(): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | 此 **Scope** 的下限。 |

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

获取此 **Scope** 的上限。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [util.ScopeHelper.getUpper](arkts-arkts-util-scopehelper-c.md#getupper)

<!--Device-Scope-getUpper(): ScopeType--><!--Device-Scope-getUpper(): ScopeType-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | 此 **Scope** 的上限。 |

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

获取此 **Scope** 与给定 **Scope** 的交集。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.intersect

<!--Device-Scope-intersect(range: Scope): Scope--><!--Device-Scope-intersect(range: Scope): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes | 指定的 **Scope**。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Scope](arkts-arkts-util-scope-c.md) | 此 **Scope** 与给定 **Scope** 的交集。 |

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

获取此 **Scope** 与给定上下限的交集。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.util.ScopeHelper.intersect

<!--Device-Scope-intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope--><!--Device-Scope-intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 下限。 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes | 上限。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Scope](arkts-arkts-util-scope-c.md) | 此 **Scope** 与给定上下限的交集。 |

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

获取包含此 **Scope** 的字符串表示形式。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.toString](arkts-arkts-util-lrucache-c.md#tostring)

<!--Device-Scope-toString(): string--><!--Device-Scope-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 包含此 **Scope** 的字符串表示形式。 |

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

