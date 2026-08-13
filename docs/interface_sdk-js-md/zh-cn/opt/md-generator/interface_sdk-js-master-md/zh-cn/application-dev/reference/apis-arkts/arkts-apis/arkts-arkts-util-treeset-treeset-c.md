# TreeSet

TreeSet基于[TreeMap](arkts-arkts-util-treemap-treemap-c.md#TreeMap)实现，在TreeSet中，仅处理元素的值（value），不单独处理键（key）。 TreeSet的每个元素在底层TreeMap中同时作为key和value存储，因此元素中value唯一且有序。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare class TreeSet--><!--Device-unnamed-declare class TreeSet-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，每一项都是一个JavaScript对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-$_iterator(): IterableIterator<T>--><!--Device-TreeSet-$_iterator(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器的每一项为容器中的元素值。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-[Symbol.iterator](): IterableIterator<T>--><!--Device-TreeSet-[Symbol.iterator](): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
// 使用方法一：使用for...of语法遍历TreeSet
for (let item of treeSet) {
  console.info('value:' + item);
}
// value:sparrow
// value:squirrel

// 使用方法二：通过Symbol.iterator获取迭代器手动遍历
let iterator = treeSet[Symbol.iterator]();
let currentValue: IteratorResult<string> = iterator.next().value;
while (currentValue != undefined) {
  console.info('value:' + currentValue);
  currentValue = iterator.next().value;
}
// value:sparrow
// value:squirrel
```

```TypeScript
// 不建议在Symbol.iterator中使用add、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let treeSet = new TreeSet<string>();
for (let i = 0; i < 10; i++) {
  treeSet.add('sparrow' + i);
}
for (let i = 0; i < 10; i++) {
  treeSet.remove('sparrow' + i);
}
```

## add

```TypeScript
add(value: T): boolean
```

向容器中添加指定元素。不建议插入null值，可能会影响排序结果；添加自定义类型元素时，需确保TreeSet在构造时已提供比较函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-add(value: T): boolean--><!--Device-TreeSet-add(value: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
let result = treeSet.add('squirrel');
console.info('result:', result); // result: true
```

## clear

```TypeScript
clear(): void
```

清除容器中的所有元素，并将length置为0。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-clear(): void--><!--Device-TreeSet-clear(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
treeSet.clear();
let result = treeSet.isEmpty();
console.info('result:', result); // result: true
```

## constructor

```TypeScript
constructor(comparator?: (firstValue: T, secondValue: T) => boolean)
```

TreeSet的构造函数，支持通过比较函数对元素进行升序或降序排序。当插入自定义类型时，必须提供比较函数。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-constructor(comparator?: (firstValue: T, secondValue: T) => boolean)--><!--Device-TreeSet-constructor(comparator?: (firstValue: T, secondValue: T) => boolean)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | (firstValue: T, secondValue: T) = & gt; boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## 示例

```TypeScript
// 默认构造
let treeSet = new TreeSet<string | number | boolean | Object>();
```

```TypeScript
// 使用comparator firstValue < secondValue，表示期望结果为升序排序。反之firstValue > secondValue，表示为降序排序。
let treeSet: TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string): boolean => {
  return firstValue < secondValue;
});
treeSet.add('a');
treeSet.add('c');
treeSet.add('d');
treeSet.add('b');
for (let value of treeSet) {
  console.info('value:', value);
};
// value: a
// value: b
// value: c
// value: d
```

```TypeScript
// 插入自定义类型时，必须提供比较函数。
class TestEntry {
  public id: number = 0;
}
let testEntrySet: TreeSet<TestEntry> = new TreeSet<TestEntry>((t1: TestEntry, t2: TestEntry): boolean => { return t1.id > t2.id; });
let firstEntry: TestEntry = {
  id: 0
};
let secondEntry: TestEntry = {
  id: 1
}
testEntrySet.add(firstEntry);
testEntrySet.add(secondEntry);
console.info('treeSet: ', testEntrySet.length);
```

## constructor

```TypeScript
constructor(comparator?: TreeSetComparator<T>)
```

TreeSet的构造函数，支持通过比较函数对元素进行升序或降序排序。当插入自定义类型时，必须提供比较函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-constructor(comparator?: TreeSetComparator<T>)--><!--Device-TreeSet-constructor(comparator?: TreeSetComparator<T>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | [TreeSetComparator](arkts-arkts-treesetcomparator-t.md)&lt;T&gt; | 否 |

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

返回包含此容器中元素的新迭代器对象，每个元素以[value, value]的形式返回。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-entries(): IterableIterator<[T, T]>--><!--Device-TreeSet-entries(): IterableIterator<[T, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[T, T] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
// 获取entries迭代器
let iterator = treeSet.entries();
// 遍历迭代器获取键值对
let iterResult: IteratorResult<Object[]> = iterator.next();
while (!iterResult.done) {
  console.info('TreeSet: ' + iterResult.value[1]);
  iterResult = iterator.next();
}
// TreeSet: sparrow
// TreeSet: squirrel
```

```TypeScript
// 不建议在entries中使用add、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add('sparrow' + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove('sparrow' + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void
```

通过回调函数来遍历实例对象上的元素。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void--><!--Device-TreeSet-forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value?: T, key?: T, set?: TreeSet & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('sparrow');
treeSet.add('gull');
// 通过forEach遍历TreeSet中的元素
treeSet.forEach((value: string, key: string): void => {
  console.info('value:' + value);
});
// value:gull
// value:sparrow
```

```TypeScript
// 不建议在forEach中使用add、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let treeSet = new TreeSet<string>();
for (let i = 0; i < 10; i++) {
  treeSet.add('sparrow' + i);
}
for (let i = 0; i < 10; i++) {
  treeSet.remove('sparrow' + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: TreeSetForEachCb<T>): void
```

通过回调函数来遍历实例对象上的元素。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-forEach(callbackFn: TreeSetForEachCb<T>): void--><!--Device-TreeSet-forEach(callbackFn: TreeSetForEachCb<T>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TreeSetForEachCb](arkts-arkts-treesetforeachcb-t.md)&lt;T&gt; | 是 |

## getFirstValue

```TypeScript
getFirstValue(): T
```

获取容器中排序第一的元素，为空时返回undefined。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-getFirstValue(): T--><!--Device-TreeSet-getFirstValue(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200010](../errorcode-utils.md#10200010-容器为空) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
let result = treeSet.getFirstValue();
console.info('result:', result); // result: sparrow
```

## getHigherValue

```TypeScript
getHigherValue(key: T): T
```

获取容器中比传入元素排序靠后一位的元素，为空时返回undefined。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-getHigherValue(key: T): T--><!--Device-TreeSet-getHigherValue(key: T): T-End-->

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
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
treeSet.add('gander');
let result = treeSet.getHigherValue('sparrow');
console.info('result:', result); // result: squirrel
```

## getHigherValue

```TypeScript
getHigherValue(key: T): T | undefined
```

获取容器中比传入元素排序靠后一位的元素，如果key不存在，则返回undefined。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-getHigherValue(key: T): T | undefined--><!--Device-TreeSet-getHigherValue(key: T): T | undefined-End-->

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
| [10200010](../errorcode-utils.md#10200010-容器为空) |

## getLastValue

```TypeScript
getLastValue(): T
```

获取容器中排序最后的数据，为空时返回undefined。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-getLastValue(): T--><!--Device-TreeSet-getLastValue(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200010](../errorcode-utils.md#10200010-容器为空) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
let result = treeSet.getLastValue();
console.info('result:', result); // result: squirrel
```

## getLowerValue

```TypeScript
getLowerValue(key: T): T
```

获取容器中比传入元素排序靠前一位的元素，为空时返回undefined。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-getLowerValue(key: T): T--><!--Device-TreeSet-getLowerValue(key: T): T-End-->

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
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
treeSet.add('gander');
let result = treeSet.getLowerValue('sparrow');
console.info('result:', result); // result: gander
```

## getLowerValue

```TypeScript
getLowerValue(key: T): T | undefined
```

获取容器中比传入元素排序靠前一位的元素，如果key不存在，则返回undefined。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-getLowerValue(key: T): T | undefined--><!--Device-TreeSet-getLowerValue(key: T): T | undefined-End-->

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
| [10200010](../errorcode-utils.md#10200010-容器为空) |

## has

```TypeScript
has(value: T): boolean
```

判断容器中是否包含指定元素。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-has(value: T): boolean--><!--Device-TreeSet-has(value: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<number>();
treeSet.add(123);
// 判断容器中是否包含指定元素
let result = treeSet.has(123);
console.info('result:', result); // result: true
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断容器是否为空。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-isEmpty(): boolean--><!--Device-TreeSet-isEmpty(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
// 判断容器是否为空
let result = treeSet.isEmpty();
console.info('result:', result);  // result: true
```

## popFirst

```TypeScript
popFirst(): T
```

删除容器中排序最前的数据，为空时返回undefined。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-popFirst(): T--><!--Device-TreeSet-popFirst(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200010](../errorcode-utils.md#10200010-容器为空) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
let result = treeSet.popFirst();
console.info('result:', result); // result: sparrow
```

## popLast

```TypeScript
popLast(): T
```

删除容器中排序最后的数据，为空时返回undefined。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-popLast(): T--><!--Device-TreeSet-popLast(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200010](../errorcode-utils.md#10200010-容器为空) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
let result = treeSet.popLast();
console.info('result:', result); // result: squirrel
```

## remove

```TypeScript
remove(value: T): boolean
```

删除指定的元素。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-remove(value: T): boolean--><!--Device-TreeSet-remove(value: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
let result = treeSet.remove('sparrow');
console.info('result:', result); // result: true
```

## values

```TypeScript
values(): IterableIterator<T>
```

返回包含此容器中元素值的新迭代器对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-values(): IterableIterator<T>--><!--Device-TreeSet-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## 示例

```TypeScript
// 不建议在values中使用add、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
let treeSet = new TreeSet<string>();
treeSet.add('squirrel');
treeSet.add('sparrow');
let values = treeSet.values();
for (let value of values) {
  console.info('value:', value);
}
// value: sparrow
// value: squirrel
```

## length

```TypeScript
length: number
```

TreeSet的元素个数。

**类型：** number

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TreeSet-length: number--><!--Device-TreeSet-length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
