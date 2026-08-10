# TreeSet

TreeSet基于[TreeMap](arkts-util-treemap.md)实现，在TreeSet中，仅处理元素的值（value），不单独处理键（key）。TreeSet的每个元素在底层TreeMap中同时作为key和value存储，因此元素中value唯一且有序。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class TreeSet<T>--><!--Device-unnamed-declare class TreeSet<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { TreeSet } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回一个迭代器，每一项都是一个JavaScript对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeSet-$_iterator(): IterableIterator<T>--><!--Device-TreeSet-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | TreeSet的迭代器。 |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器的每一项为容器中的元素值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-[Symbol.iterator](): IterableIterator<T>--><!--Device-TreeSet-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回包含TreeSet中所有元素的迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
// Method 1:
for (let item of treeSet) {
  console.info("value:" + item);
}
// value:sparrow
// value:squirrel

// Method 2:
let iter = treeSet[Symbol.iterator]();
let temp: IteratorResult<string> = iter.next().value;
while(temp != undefined) {
  console.info("value:" + temp);
  temp = iter.next().value;
}
// value:sparrow
// value:squirrel
```

```TypeScript
// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove("sparrow" + i);
}
```

## add

```TypeScript
add(value: T): boolean
```

向容器中添加指定元素。不建议插入null值，可能会影响排序结果；添加自定义类型元素时，需确保TreeSet在构造时已提供比较函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-add(value: T): boolean--><!--Device-TreeSet-add(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 向TreeSet中添加的值元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 成功添加新元素至容器返回true，当元素已存在时返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The add method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
let result = treeSet.add("squirrel");
console.info("result:", result); // result: true
```

## clear

```TypeScript
clear(): void
```

清除容器中的所有元素，并将length置为0。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-clear(): void--><!--Device-TreeSet-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
treeSet.clear();
let result = treeSet.isEmpty();
console.info("result:", result); // result: true
```

## constructor

```TypeScript
constructor(comparator?: (firstValue: T, secondValue: T) => boolean)
```

TreeSet的构造函数，支持通过比较函数对元素进行升序或降序排序。当插入自定义类型时，必须提供比较函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-constructor(comparator?: (firstValue: T, secondValue: T) => boolean)--><!--Device-TreeSet-constructor(comparator?: (firstValue: T, secondValue: T) => boolean)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| comparator | (firstValue: T, secondValue: T) =&gt; boolean | No | 比较函数。 comparator（可选）用户自定义的比较函数。 firstValue（必填）前一项元素。 secondValue（必填）后一项元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The TreeSet's constructor cannot be directly invoked. |

## Examples

```TypeScript
// Default constructor.
let treeSet = new TreeSet<string | number | boolean | Object>();
```

```TypeScript
// Use the comparator firstValue < secondValue if the elements are expected to be sorted in ascending order. Use firstValue > secondValue if the elements are expected to be sorted in descending order.
let treeSet: TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string): boolean => {
  return firstValue < secondValue;
});
treeSet.add("a");
treeSet.add("c");
treeSet.add("d");
treeSet.add("b");
for (let value of treeSet) {
  console.info("value:", value);
}
// value: a
// value: b
// value: c
// value: d
```

```TypeScript
// When a custom type is inserted, a comparator must be provided.
class TestEntry{
  public id: number = 0;
}
let ts1: TreeSet<TestEntry> = new TreeSet<TestEntry>((t1: TestEntry, t2: TestEntry): boolean => {return t1.id > t2.id;});
let entry1: TestEntry = {
  id: 0
};
let entry2: TestEntry = {
  id: 1
}
ts1.add(entry1);
ts1.add(entry2);
console.info("treeSet: ", ts1.length);
```

## constructor

```TypeScript
constructor(comparator?: TreeSetComparator<T>)
```

TreeSet的构造函数，支持通过比较函数对元素进行升序或降序排序。当插入自定义类型时，必须提供比较函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeSet-constructor(comparator?: TreeSetComparator<T>)--><!--Device-TreeSet-constructor(comparator?: TreeSetComparator<T>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| comparator | [TreeSetComparator](arkts-arkts-treesetcomparator-t.md)&lt;T&gt; | No | 比较函数。 comparator（可选）用户自定义的比较函数。 |

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

返回包含此容器中元素的新迭代器对象，每个元素以[value, value]的形式返回。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-entries(): IterableIterator<[T, T]>--><!--Device-TreeSet-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[T, T]&gt; | 返回包含TreeSet中所有元素键值对的迭代器对象，每个键值对中键与值相同，均为元素本身。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let it = treeSet.entries();
let t: IteratorResult<Object[]> = it.next();
while(!t.done) {
  console.info("TreeSet: " + t.value[1]);
  t = it.next()
}
// TreeSet: sparrow
// TreeSet: squirrel
```

```TypeScript
// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void
```

通过回调函数来遍历实例对象上的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void--><!--Device-TreeSet-forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value?: T, key?: T, set?: TreeSet&lt;T&gt;) =&gt; void | Yes | 遍历实例对象中每个元素时调用的回调函数，开发者可在回调中对元素及其下标进行自定义处理。 |
| thisArg | Object | No | callbackFn被调用时用作this值。当需要在回调函数中使用特定的this上下文（如访问外部对象属性）时传入此参数。 不传入时默认值为当前实例对象，回调函数中的this指向TreeSet实例本身。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("sparrow");
treeSet.add("gull");
treeSet.forEach((value: string, key: string): void => {
  console.info("value:" + value);
});
// value:gull
// value:sparrow
```

```TypeScript
// You are not advised to use the set or remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: TreeSetForEachCb<T>): void
```

通过回调函数来遍历实例对象上的元素及其下标。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeSet-forEach(callbackFn: TreeSetForEachCb<T>): void--><!--Device-TreeSet-forEach(callbackFn: TreeSetForEachCb<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TreeSetForEachCb](arkts-arkts-treesetforeachcb-t.md)&lt;T&gt; | Yes | 回调函数。 |

## getFirstValue

```TypeScript
getFirstValue(): T
```

获取容器中排序第一的元素，为空时返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-getFirstValue(): T--><!--Device-TreeSet-getFirstValue(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回排序第一的数据，为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getFirstValue method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.getFirstValue();
console.info("result:", result); // result: sparrow
```

## getHigherValue

```TypeScript
getHigherValue(key: T): T
```

获取容器中比传入元素排序靠后一位的元素，为空时返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-getHigherValue(key: T): T--><!--Device-TreeSet-getHigherValue(key: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | T | Yes | 作为查找基准的元素，用于定位排序中比该元素靠后一位的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回排序中传入元素后一位的数据。为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getHigherValue method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
treeSet.add("gander");
let result = treeSet.getHigherValue("sparrow");
console.info("result:", result); // result: squirrel
```

## getHigherValue

```TypeScript
getHigherValue(key: T): T | undefined
```

获取容器中比传入元素排序靠后一位的元素，如果key不存在，则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeSet-getHigherValue(key: T): T | undefined--><!--Device-TreeSet-getHigherValue(key: T): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | T | Yes | 对比的元素值。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 如果存在则返回指定key元素的后一位值，否则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200010 | Container is empty. |

## getLastValue

```TypeScript
getLastValue(): T
```

获取容器中排序最后的数据，为空时返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-getLastValue(): T--><!--Device-TreeSet-getLastValue(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回排序最后的数据，为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLastValue method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.getLastValue();
console.info("result:", result); // result: squirrel
```

## getLowerValue

```TypeScript
getLowerValue(key: T): T
```

获取容器中比传入元素排序靠前一位的元素，为空时返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-getLowerValue(key: T): T--><!--Device-TreeSet-getLowerValue(key: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | T | Yes | 作为查找基准的元素值，用于定位排序中比该元素靠前一位的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回排序中传入元素前一位的数据，为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLowerValue method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
treeSet.add("gander");
let result = treeSet.getLowerValue("sparrow");
console.info("result:", result); // result: gander
```

## getLowerValue

```TypeScript
getLowerValue(key: T): T | undefined
```

获取容器中比传入元素排序靠前一位的元素，如果key不存在，则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeSet-getLowerValue(key: T): T | undefined--><!--Device-TreeSet-getLowerValue(key: T): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | T | Yes | 对比的元素值。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 如果存在则返回指定key元素的前一位值，否则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200010 | Container is empty. |

## has

```TypeScript
has(value: T): boolean
```

判断容器中是否包含指定元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-has(value: T): boolean--><!--Device-TreeSet-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 要判断是否存在于容器中的目标元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定元素返回true，不包含指定元素返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The has method cannot be bound. |

## Examples

```TypeScript
let treeSet  = new TreeSet<number>();
treeSet.add(123);
let result = treeSet.has(123);
console.info("result:", result); // result: true
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断容器是否为空。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-isEmpty(): boolean--><!--Device-TreeSet-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 为空返回true，不为空返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The isEmpty method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
let result = treeSet.isEmpty();
console.info("result:", result);  // result: true
```

## popFirst

```TypeScript
popFirst(): T
```

删除容器中排序最前的数据，为空时返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-popFirst(): T--><!--Device-TreeSet-popFirst(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回删除的数据，为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The popFirst method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.popFirst();
console.info("result:", result); // result: sparrow
```

## popLast

```TypeScript
popLast(): T
```

删除容器中排序最后的数据，为空时返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-popLast(): T--><!--Device-TreeSet-popLast(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回删除的数据，为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The popLast method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.popLast();
console.info("result:", result); // result: squirrel
```

## remove

```TypeScript
remove(value: T): boolean
```

删除指定的元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-remove(value: T): boolean--><!--Device-TreeSet-remove(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 要从容器中删除的目标元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 成功删除元素返回true，指定元素不存在返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.remove("sparrow");
console.info("result:", result); // result: true
```

## values

```TypeScript
values(): IterableIterator<T>
```

返回包含此容器中元素值的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-values(): IterableIterator<T>--><!--Device-TreeSet-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回包含TreeSet中所有元素的迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound. |

## Examples

```TypeScript
let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let values = treeSet.values();
for (let value of values) {
  console.info("value:", value)
}
// value: sparrow
// value: squirrel
```

## length

```TypeScript
length: number
```

TreeSet的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeSet-length: number--><!--Device-TreeSet-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

