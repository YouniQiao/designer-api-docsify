# ScopeHelper

提供定义字段有效范围的 API。此类的构造函数创建具有上下限的可比较对象。

**起始版本：** 9

<!--Device-util-class ScopeHelper--><!--Device-util-class ScopeHelper-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from '@kit.ArkTS';
```

## clamp

```TypeScript
clamp(value: ScopeType): ScopeType
```

将一个值限制在此 **Scope** 范围内。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-clamp(value: ScopeType): ScopeType--><!--Device-ScopeHelper-clamp(value: ScopeType): ScopeType-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | 如果指定值小于下限，则返回 **lowerObj**；如果指定值大于上限，则返回 **upperObj**；如果 在此 **Scope** 范围内，则返回指定值。 |

**示例**

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
// 输出结果：result = 35
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// 输出结果：result = 35
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
// 输出结果：result = 35
```

## constructor

```TypeScript
constructor(lowerObj: ScopeType, upperObj: ScopeType)
```

用于创建具有指定上下限的 **ScopeHelper** 对象的构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-constructor(lowerObj: ScopeType, upperObj: ScopeType)--><!--Device-ScopeHelper-constructor(lowerObj: ScopeType, upperObj: ScopeType)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | Scope** 对象的下限。 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | Scope** 对象的上限。 |

**示例**

```TypeScript
let textDecoder = new util.TextDecoder();
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// 输出结果：retStr = utf-8
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

ArkTS-Dyn示例：

```TypeScript
let lruCache = new util.LRUCache<number, number>();
```

ArkTS-Sta示例：

```TypeScript
let lruCache = new util.LRUCache<int, int>();
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
// 输出结果：range = [30, 40]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}
let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
console.info("range = " + range);
// 输出结果：range = [30, 40]
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
// 输出结果：range = [30, 40]
```

```TypeScript
let base64 = new  util.Base64();
```

## contains

```TypeScript
contains(value: ScopeType): boolean
```

判断一个范围是否在此 **Scope** 范围内。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-contains(value: ScopeType): boolean--><!--Device-ScopeHelper-contains(value: ScopeType): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检查结果。如果值在此 **Scope** 范围内，则返回 **true**；否则返回 **false**。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.contains(2);
console.info('result = ' + result);
// 输出结果：result = true
```

ArkTS-Sta示例：

```TypeScript
let pro = new util.LRUCache<int, int>();
pro.put(2, 10);
let result = pro.contains(2);
console.info('result = ' + result);
// 输出结果：result = true
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
// 输出结果：result = true
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
// 输出结果：result = false
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// 输出结果：result = true
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.ScopeHelper<Temperature>(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// 输出结果：result = false
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.contains(20);
console.info('result = ' + result);
// 输出结果：result = false
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
// 输出结果：result = true
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
// 输出结果：result = false
```

## contains

```TypeScript
contains(range: ScopeHelper): boolean
```

判断一个范围是否在此 **Scope** 范围内。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-contains(range: ScopeHelper): boolean--><!--Device-ScopeHelper-contains(range: ScopeHelper): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 是 | 指定的 **Scope**。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检查结果。如果范围在此 **Scope** 范围内，则返回 **true**；否则返回 **false**。 |

**示例**

参见 [contains](#contains)

## expand

```TypeScript
expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper
```

获取此 **Scope** 与给定上下限的并集。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper--><!--Device-ScopeHelper-expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 下限。 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 上限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 此 **Scope** 与给定上下限的并集。 |

**示例**

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
// 输出结果：result = [30, 40]
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
// 输出结果：result = [30, 40]
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
// 输出结果：result = [30, 40]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
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
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
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
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let rangeFir = new util.ScopeHelper<Temperature>(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// 输出结果：result = [30, 40]
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
// 输出结果：result = [30, 40]
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
// 输出结果：result = [30, 40]
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
// 输出结果：result = [30, 40]
```

## expand

```TypeScript
expand(range: ScopeHelper): ScopeHelper
```

获取此 **Scope** 与给定 **Scope** 的并集。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-expand(range: ScopeHelper): ScopeHelper--><!--Device-ScopeHelper-expand(range: ScopeHelper): ScopeHelper-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 是 | 指定的 **Scope**。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 此 **Scope** 与给定 **Scope** 的并集。 |

**示例**

参见 [expand](#expand)

## expand

```TypeScript
expand(value: ScopeType): ScopeHelper
```

获取此 **Scope** 与给定值的并集。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-expand(value: ScopeType): ScopeHelper--><!--Device-ScopeHelper-expand(value: ScopeType): ScopeHelper-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 此 **Scope** 与给定值的并集。 |

**示例**

参见 [expand](#expand)

## getLower

```TypeScript
getLower(): ScopeType
```

获取此 **Scope** 的下限。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-getLower(): ScopeType--><!--Device-ScopeHelper-getLower(): ScopeType-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | 此 **Scope** 的下限。 |

**示例**

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
// 输出结果：result = 30
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// 输出结果：result = 30
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
// 输出结果：result = 30
```

## getUpper

```TypeScript
getUpper(): ScopeType
```

获取此 **Scope** 的上限。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-getUpper(): ScopeType--><!--Device-ScopeHelper-getUpper(): ScopeType-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | 此 **Scope** 的上限。 |

**示例**

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
// 输出结果：result = 40
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// 输出结果：result = 40
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
// 输出结果：result = 40
```

## intersect

```TypeScript
intersect(range: ScopeHelper): ScopeHelper
```

获取此 **Scope** 与给定 **Scope** 的交集。如果交集为空，则抛出异常。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-intersect(range: ScopeHelper): ScopeHelper--><!--Device-ScopeHelper-intersect(range: ScopeHelper): ScopeHelper-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 是 | 指定的 **Scope**。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 此 **Scope** 与给定 **Scope** 的交集。 |

**示例**

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
// 输出结果：result = [35, 39]
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
// 输出结果：result = [35, 39]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.ScopeHelper<Temperature>(tempMiDF, tempMidS);
let result = range.intersect(rangeFir);
console.info("result = " + result);
// 输出结果：result = [35, 39]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
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
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// 输出结果：result = [35, 39]
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
  // 输出结果：result = [35, 39]
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
// 输出结果：result = [35, 39]
```

## intersect

```TypeScript
intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper
```

获取此 **Scope** 与给定上下限的交集。如果交集为空，则抛出异常。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper--><!--Device-ScopeHelper-intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 下限。 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 | 上限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 此 **Scope** 与给定上下限的交集。 |

**示例**

参见 [intersect](#intersect)

## toString

```TypeScript
toString(): string
```

获取包含此 **Scope** 的字符串表示形式。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScopeHelper-toString(): string--><!--Device-ScopeHelper-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 包含此 **Scope** 的字符串表示形式。 |

**示例**

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// 输出结果：result = 1/2
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// 输出结果：result = 1/2
```

ArkTS-Dyn示例：

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
pro.get(3);
console.info(pro.toString());
// 输出结果：LRUCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
// maxSize: 缓存区最大值 hits: 查询值匹配成功的次数 misses: 查询值匹配失败的次数 hitRate: 查询值匹配率
```

ArkTS-Sta示例：

```TypeScript
let pro = new util.LRUCache<int, int>();
pro.put(2, 10);
pro.get(2);
pro.get(3);
console.info(pro.toString());
// 输出结果：LRUCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
// maxSize: 缓存区最大值 hits: 查询值匹配成功的次数 misses: 查询值匹配失败的次数 hitRate: 查询值匹配率
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
// 输出结果：result = [30, 40]
```

```TypeScript
class Temperature implements util.ScopeComparable<Temperature> {
  private readonly _temp: int;

  constructor(value: int) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp(): int {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper<Temperature>(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// 输出结果：result = [30, 40]
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
pro.remove(20);
let result = pro.toString();
console.info("result = " + result);
// 输出结果：result = Lrubuffer[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% ]
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
// 输出结果：result = [30, 40]
```

