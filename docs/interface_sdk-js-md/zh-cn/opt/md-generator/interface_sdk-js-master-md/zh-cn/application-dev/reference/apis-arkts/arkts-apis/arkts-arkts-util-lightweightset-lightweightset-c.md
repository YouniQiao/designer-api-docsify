# LightWeightSet

LightWeightSet可用于存储一系列值，存储元素中value唯一。

**起始版本：** 8

<!--Device-unnamed-declare class LightWeightSet<T>--><!--Device-unnamed-declare class LightWeightSet<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。不建议在Symbol.iterator中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-[Symbol.iterator](): IterableIterator<T>--><!--Device-LightWeightSet-[Symbol.iterator](): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");

// 使用方法一：
for (let value of lightWeightSet) {
  console.info("value:", value);
}
// value: sparrow
// value: squirrel

// 使用方法二：
let symbolIterator = lightWeightSet[Symbol.iterator]();
let iteratorResult: IteratorResult<string> = symbolIterator.next();
while (!iteratorResult.done) {
  console.info("value:", iteratorResult.value);
  iteratorResult = symbolIterator.next();
}
// value: sparrow
// value: squirrel
```

```TypeScript
// 不建议在Symbol.iterator中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let lightWeightSet = new LightWeightSet<string>();
for (let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for (let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}
```

## add

```TypeScript
add(obj: T): boolean
```

向容器中添加数据。若添加的元素已存在于容器中，则不会重复添加，返回false。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-add(obj: T): boolean--><!--Device-LightWeightSet-add(obj: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
// 向容器中添加元素
let lightWeightSet = new LightWeightSet<string>();
let result = lightWeightSet.add("squirrel");
console.info("result:", result);  // result: true
```

## addAll

```TypeScript
addAll(set: LightWeightSet<T>): boolean
```

将另一个容器的所有元素添加到当前容器。若源容器中的元素已存在于当前容器中，则跳过该元素不重复添加。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-addAll(set: LightWeightSet<T>): boolean--><!--Device-LightWeightSet-addAll(set: LightWeightSet<T>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let set = new LightWeightSet<string>();
set.add("gull");
// 将另一个容器的所有元素添加到当前容器
lightWeightSet.addAll(set);
let result = lightWeightSet.has("gull");
console.info("result:", result);  // result: true
```

## clear

```TypeScript
clear(): void
```

清除容器中的所有元素，并将length置为0。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-clear(): void--><!--Device-LightWeightSet-clear(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 清除容器中的所有元素
lightWeightSet.clear();
let result = lightWeightSet.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

LightWeightSet的构造函数。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-constructor()--><!--Device-LightWeightSet-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-构造函数调用异常) |

## 示例

```TypeScript
// 创建LightWeightSet实例
let lightWeightSet = new LightWeightSet<number | string>();
```

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

返回包含此容器中所有元素对的新迭代器对象，每个元素对由相同值组成[value, value]。不建议在entries中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-entries(): IterableIterator<[T, T]>--><!--Device-LightWeightSet-entries(): IterableIterator<[T, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[T, T] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let entryIterator = lightWeightSet.entries();
for (let item of entryIterator) {
  console.info("value:", item[1])
}
// value: sparrow
// value: squirrel
```

```TypeScript
// 不建议在entries中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}
```

## equal

```TypeScript
equal(obj: Object): boolean
```

判断此容器与obj的构成元素是否相同。

> **说明：**
> 
> 此接口从API version 8开始支持，从API version 12开始废弃。无替代接口。

**起始版本：** 8

**废弃版本：** 12

<!--Device-LightWeightSet-equal(obj: Object): boolean--><!--Device-LightWeightSet-equal(obj: Object): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let comparisonArray = ["sparrow", "squirrel"];
// 判断此容器与obj的构成元素是否相同
let result = lightWeightSet.equal(comparisonArray);
console.info("result:", result);  // result: true
```

## forEach

```TypeScript
forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void
```

通过回调函数来遍历LightWeightSet实例对象上的元素。不建议在forEach函数中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void--><!--Device-LightWeightSet-forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value?: T, key?: T, set?: LightWeightSet & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("sparrow");
lightWeightSet.add("gull");
// 通过回调函数遍历LightWeightSet中的元素
lightWeightSet.forEach((value: string, key: string) => {
  console.info("value:" + value, "key:" + key);
});
// value:gull key:gull
// value:sparrow key:sparrow
```

```TypeScript
// 不建议在forEach函数中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let lightWeightSet = new LightWeightSet<string>();
for (let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for (let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}
```

## getIndexOf

```TypeScript
getIndexOf(key: T): number
```

获取指定元素所对应的下标。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-getIndexOf(key: T): int--><!--Device-LightWeightSet-getIndexOf(key: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 获取指定元素的下标
let result = lightWeightSet.getIndexOf("sparrow");
console.info("result:", result);  // result: 0
```

## getValueAt

```TypeScript
getValueAt(index: number): T
```

获取容器中指定下标对应的元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-getValueAt(index: number): T--><!--Device-LightWeightSet-getValueAt(index: number): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 获取指定下标对应的元素
let result = lightWeightSet.getValueAt(1);
console.info("result:", result);  // result: squirrel
```

## has

```TypeScript
has(key: T): boolean
```

判断容器中是否包含指定元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-has(key: T): boolean--><!--Device-LightWeightSet-has(key: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<number>();
lightWeightSet.add(123);
// 判断容器中是否包含指定元素
let result = lightWeightSet.has(123);
console.info("result:", result);  // result: true
```

## hasAll

```TypeScript
hasAll(set: LightWeightSet<T>): boolean
```

判断容器中是否包含指定set中的所有元素。当容器中存储的value为number类型且值大于INT32_MAX(2147483647)或小于INT32_MIN(-2147483648)时，判断结果可能与预期不一致，详见规格限制。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-hasAll(set: LightWeightSet<T>): boolean--><!--Device-LightWeightSet-hasAll(set: LightWeightSet<T>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let set = new LightWeightSet<string>();
set.add("sparrow");
// 判断容器中是否包含指定set中的所有元素
let result = lightWeightSet.hasAll(set);
console.info("result:", result);  // result: true
```

## increaseCapacityTo

```TypeScript
increaseCapacityTo(minimumCapacity: number): void
```

将当前LightWeightSet扩容至指定容量。如果传入的容量值大于或等于当前LightWeightSet中的元素个数，将容量变更为新容量，小于则不会变更。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-increaseCapacityTo(minimumCapacity: int): void--><!--Device-LightWeightSet-increaseCapacityTo(minimumCapacity: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| minimumCapacity | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200001-参数范围越界错误) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
// 将容器扩容至指定容量
lightWeightSet.increaseCapacityTo(10);
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断容器是否为空。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-isEmpty(): boolean--><!--Device-LightWeightSet-isEmpty(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
// 判断容器是否为空
const lightWeightSet = new LightWeightSet<number>();
let result = lightWeightSet.isEmpty();
console.info("result:", result);  // result: true
```

## remove

```TypeScript
remove(key: T): T
```

删除并返回指定元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-remove(key: T): T--><!--Device-LightWeightSet-remove(key: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 删除并返回指定元素
let result = lightWeightSet.remove("sparrow");
console.info("result:", result);  // result: sparrow
```

## removeAt

```TypeScript
removeAt(index: number): boolean
```

删除指定下标所对应的元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-removeAt(index: int): boolean--><!--Device-LightWeightSet-removeAt(index: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 删除指定下标的元素
let result = lightWeightSet.removeAt(1);
console.info("result:", result);  // result: true
```

## toArray

```TypeScript
toArray(): Array<T>
```

获取包含此容器中所有元素的数组。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-toArray(): Array<T>--><!--Device-LightWeightSet-toArray(): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 获取包含此容器中所有对象的数组
let result = lightWeightSet.toArray();
console.info(result.toString());
// sparrow,squirrel
```

## toString

```TypeScript
toString(): String
```

获取包含容器中所有元素的字符串。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-toString(): String--><!--Device-LightWeightSet-toString(): String-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| String |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 获取包含容器中所有元素的字符串
let result = lightWeightSet.toString();
console.info("result:", result);  // result: sparrow,squirrel
```

## values

```TypeScript
values(): IterableIterator<T>
```

返回包含此集合中所有值的新迭代器对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-values(): IterableIterator<T>--><!--Device-LightWeightSet-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
// 获取包含所有元素的迭代器
let values = lightWeightSet.values();
for (let value of values) {
  console.info("value:", value);
}
// value: sparrow
// value: squirrel
```

## length

```TypeScript
length: number
```

LightWeightSet的元素个数。

**类型：** number

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LightWeightSet-length: number--><!--Device-LightWeightSet-length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
