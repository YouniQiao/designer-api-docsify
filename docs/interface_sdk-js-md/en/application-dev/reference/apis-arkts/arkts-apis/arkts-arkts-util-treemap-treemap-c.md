# TreeMap

TreeMap可用于存储具有关联关系的key-value键值对集合，存储元素中key值唯一，每个key对应一个value。TreeMap底层使用红黑树实现，可以利用二叉树特性查找键值对，查找、插入和删除操作的时间复杂度为O(log n)。key值有序存储，可以实现高效的有序遍历。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class TreeMap<K, V>--><!--Device-unnamed-declare class TreeMap<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { TreeMap } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

返回一个迭代器，每一项都是一个JavaScript对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-$_iterator(): IterableIterator<[K, V]>--><!--Device-TreeMap-$_iterator(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | TreeMap的迭代器。 |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

返回一个迭代器，迭代器的每一项是一个包含键和值的[K, V]数组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-TreeMap-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 返回一个迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);

// Method 1:
for (let item of treeMap) {
  console.info("TreeMap:", item[0], item[1]);
}
// Output:
// TreeMap: sparrow,356
// TreeMap: squirrel,123

// Method 2:
let iter = treeMap[Symbol.iterator]();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:", temp.value[0]);
  console.info("value:", temp.value[1]);
  temp = iter.next();
}
// Output:
// key: sparrow
// value: 356
// key: squirrel
// value: 123
```

```TypeScript
// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
 let treeMap = new TreeMap<string, number>();
 for(let i = 0; i < 10; i++) {
   treeMap.set("sparrow" + i, 123);
 }
 for(let i = 0;i < 10; i++) {
   treeMap.remove("sparrow" + i);
 }
```

## clear

```TypeScript
clear(): void
```

清除容器中的所有元素，并将length置为0。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-clear(): void--><!--Device-TreeMap-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
treeMap.clear();
let result = treeMap.isEmpty();
console.info("result:", result); // result: true
```

## constructor

```TypeScript
constructor(comparator?: (firstValue: K, secondValue: K) => boolean)
```

TreeMap的构造函数，支持通过比较函数使元素按照自定义规则排序。当key为自定义类型时，必须提供比较函数，否则自定义类型的key无法正常排序和比较。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-constructor(comparator?: (firstValue: K, secondValue: K) => boolean)--><!--Device-TreeMap-constructor(comparator?: (firstValue: K, secondValue: K) => boolean)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| comparator | (firstValue: K, secondValue: K) =&gt; boolean | No | 比较函数。 comparator（可选）用户自定义的比较函数。 firstValue（必填）前一项元素。 secondValue（必填）后一项元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The TreeMap's constructor cannot be directly invoked. |

## Examples

```TypeScript
// Default constructor.
let treeMap = new TreeMap<number, number>();
```

```TypeScript
// Use the comparator firstValue < secondValue if the elements are expected to be sorted in ascending order. Use firstValue > secondValue if the elements are expected to be sorted in descending order.
let treeMap: TreeMap<string,string> = new TreeMap<string,string>((firstValue: string, secondValue: string): boolean => {
  return firstValue > secondValue;
});
treeMap.set("aa","3");
treeMap.set("dd","1");
treeMap.set("cc","2");
treeMap.set("bb","4");
for (let item of treeMap) {
  console.info("key: " + item[0], "value: " + item[1]);
}
// Output:
// key: dd value: 1
// key: cc value: 2
// key: bb value: 4
// key: aa value: 3
```

```TypeScript
// When a custom type is inserted, a comparator must be provided.
class TestEntry{
  public id: number = 0;
}

let ts1: TreeMap<TestEntry, string> = new TreeMap<TestEntry, string>((t1: TestEntry, t2: TestEntry): boolean => {
  return t1.id < t2.id;
});
let entry1: TestEntry = {
  id: 0
};
let entry2: TestEntry = {
  id: 1
}
ts1.set(entry1, "0");
ts1.set(entry2, "1");
console.info("length:", ts1.length); // length: 2
```

## constructor

```TypeScript
constructor(comparator?: TreeMapComparator<K>)
```

TreeMap的构造函数，支持通过比较函数使元素按照自定义规则排序。当key为自定义类型时，必须提供比较函数，否则自定义类型的key无法正常排序和比较。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-constructor(comparator?: TreeMapComparator<K>)--><!--Device-TreeMap-constructor(comparator?: TreeMapComparator<K>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| comparator | [TreeMapComparator](arkts-arkts-treemapcomparator-t.md)&lt;K&gt; | No | 比较函数。 comparator（可选）用户自定义的比较函数。 |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

返回包含此映射中键值对的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-entries(): IterableIterator<[K, V]>--><!--Device-TreeMap-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let it = treeMap.entries();
let t: IteratorResult<Object[]> = it.next();
while(!t.done) {
  console.info("TreeMap:", t.value);
  t = it.next()
}
// Output:
// TreeMap: sparrow,356
// TreeMap: squirrel,123
```

```TypeScript
// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
 let treeMap = new TreeMap<string, number>();
 for(let i = 0; i < 10; i++) {
   treeMap.set("sparrow" + i, 123);
 }
 for(let i = 0;i < 10; i++) {
   treeMap.remove("sparrow" + i);
 }
```

## forEach

```TypeScript
forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object): void
```

通过回调函数来遍历实例对象上的元素及其下标。不会对已删除的key执行回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object): void--><!--Device-TreeMap-forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value?: V, key?: K, map?: TreeMap&lt;K, V&gt;) =&gt; void | Yes | 回调函数。 callbackFn（必填）接受最多三个参数的函数。 对每个元素调用的函数。 |
| thisArg | Object | No | this值。 thisArg（可选）当callbackFn被调用时作为this值使用的对象。 如果省略thisArg，则使用undefined作为this值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("sparrow", 123);
treeMap.set("gull", 357);
treeMap.forEach((value: number, key: string): void => {
  console.info("value: " + value, "key: " + key);
});
// Output:
// value: 357 key: gull
// value: 123 key: sparrow
```

```TypeScript
// You are not advised to use the set or remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
 let treeMap = new TreeMap<string, number>();
 for(let i = 0; i < 10; i++) {
   treeMap.set("sparrow" + i, 123);
 }
 for(let i = 0;i < 10; i++) {
   treeMap.remove("sparrow" + i);
 }
```

## forEach

```TypeScript
forEach(callbackFn: TreeMapForEachCb<K, V>): void
```

通过回调函数来遍历实例对象上的元素及其下标。不会对已删除的key执行回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-forEach(callbackFn: TreeMapForEachCb<K, V>): void--><!--Device-TreeMap-forEach(callbackFn: TreeMapForEachCb<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TreeMapForEachCb](arkts-arkts-treemapforeachcb-t.md)&lt;K, V&gt; | Yes | 回调函数。 |

## get

```TypeScript
get(key: K): V
```

获取指定key所对应的value，若指定key不存在则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-get(key: K): V--><!--Device-TreeMap-get(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定需要获取对应value的key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回key映射的value值，指定key不存在时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The get method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let result = treeMap.get("sparrow");
console.info("result:", result); // result: 356
```

## get

```TypeScript
get(key: K): V | undefined
```

获取指定key所对应的value，若为空则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-get(key: K): V | undefined--><!--Device-TreeMap-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 如果存在与key关联的值则返回该值，否则返回undefined。 |

## getFirstKey

```TypeScript
getFirstKey(): K
```

获取容器中排序第一的key，若容器为空则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-getFirstKey(): K--><!--Device-TreeMap-getFirstKey(): K-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回排序第一的key，容器为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getFirstKey method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let result = treeMap.getFirstKey();
console.info("result:", result); // result: sparrow
```

## getHigherKey

```TypeScript
getHigherKey(key: K): K
```

获取容器中大于对比key值的最小键，如果不存在大于对比key值的键，则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-getHigherKey(key: K): K--><!--Device-TreeMap-getHigherKey(key: K): K-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 对比的key值。 |

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回排序中大于对比key值的最小键，若不存在则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getHigherKey method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<number, string>();
treeMap.set(1, 'one');
treeMap.set(2, 'two');
treeMap.set(3, 'three');
treeMap.set(4, 'four');
let result = treeMap.getHigherKey(3);
console.info("result:", result); // result: 4
```

## getHigherKey

```TypeScript
getHigherKey(key: K): K | undefined
```

获取容器中大于对比key值的最小键，如果key不存在，则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-getHigherKey(key: K): K | undefined--><!--Device-TreeMap-getHigherKey(key: K): K | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 对比的key值。 |

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回值或undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getHigherKey method cannot be bound. |
| 10200010 | Container is empty. |

## getLastKey

```TypeScript
getLastKey(): K
```

获取容器中排序最后的key，若容器为空则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-getLastKey(): K--><!--Device-TreeMap-getLastKey(): K-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回排序最后的key，容器为空时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLastKey method cannot be bound. |
| 10200010 | Container is empty.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let result = treeMap.getLastKey();
console.info("result:", result); // result: squirrel
```

## getLowerKey

```TypeScript
getLowerKey(key: K): K
```

获取容器中小于对比key值的最大键，如果不存在小于对比key值的键，则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-getLowerKey(key: K): K--><!--Device-TreeMap-getLowerKey(key: K): K-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 对比的key值。 |

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回排序中小于对比key值的最大键，若不存在则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLowerKey method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<number, string>();
treeMap.set(1, 'one');
treeMap.set(2, 'two');
treeMap.set(3, 'three');
treeMap.set(4, 'four');
let result = treeMap.getLowerKey(3);
console.info("result:", result); // result: 2
```

## getLowerKey

```TypeScript
getLowerKey(key: K): K | undefined
```

获取容器中小于对比key值的最大键，如果key不存在，则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-getLowerKey(key: K): K | undefined--><!--Device-TreeMap-getLowerKey(key: K): K | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 对比的key值。 |

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回值或undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getLowerKey method cannot be bound. |
| 10200010 | Container is empty. |

## hasKey

```TypeScript
hasKey(key: K): boolean
```

判断容器中是否包含指定key。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-hasKey(key: K): boolean--><!--Device-TreeMap-hasKey(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 需要判断是否存在于容器中的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定key返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The hasKey method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
let result = treeMap.hasKey("squirrel");
console.info("result:", result);  // result: true
```

## hasValue

```TypeScript
hasValue(value: V): boolean
```

判断容器中是否包含指定value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-hasValue(value: V): boolean--><!--Device-TreeMap-hasValue(value: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | 需要判断是否存在于容器中的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定value返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The hasValue method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
let result = treeMap.hasValue(123);
console.info("result:", result);  // result: true
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断容器是否为空。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-isEmpty(): boolean--><!--Device-TreeMap-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 为空返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The isEmpty method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<number, number>();
let result = treeMap.isEmpty();
console.info("result:", result);  // result: true
```

## keys

```TypeScript
keys(): IterableIterator<K>
```

返回包含此映射中所有键的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-keys(): IterableIterator<K>--><!--Device-TreeMap-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The keys method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let keys = treeMap.keys();
for (let key of keys) {
  console.info("key:", key);
}
// Output:
// key: sparrow
// key: squirrel
```

## remove

```TypeScript
remove(key: K): V
```

删除指定key对应的元素并返回其value值，若指定key不存在则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-remove(key: K): V--><!--Device-TreeMap-remove(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定需要删除元素对应的key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回删除元素的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let result = treeMap.remove("sparrow"); // Delete data.
console.info("result = " + result); // result = 356
```

## remove

```TypeScript
remove(key: K): V | undefined
```

删除指定key对应的元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TreeMap-remove(key: K): V | undefined--><!--Device-TreeMap-remove(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 如果删除了元素则返回该元素的值，否则返回undefined。 |

## replace

```TypeScript
replace(key: K, newValue: V): boolean
```

对容器中指定key对应的键值对进行更新（替换）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-replace(key: K, newValue: V): boolean--><!--Device-TreeMap-replace(key: K, newValue: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定需要替换的key。 |
| newValue | V | Yes | 替换的新值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 替换成功返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The replace method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("sparrow", 123);
let result = treeMap.replace("sparrow", 357);
console.info("sparrow:", treeMap.get("sparrow")); // sparrow: 357
```

## set

```TypeScript
set(key: K, value: V): Object
```

向容器中添加一组键值对数据，若key已存在则更新对应value值，若key不存在则新增键值对。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-set(key: K, value: V): Object--><!--Device-TreeMap-set(key: K, value: V): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 添加成员数据的键名。 |
| value | V | Yes | 添加成员数据的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 返回添加后的TreeMap。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The set method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
console.info("squirrel:", treeMap.get("squirrel")); // squirrel: 123
```

## setAll

```TypeScript
setAll(map: TreeMap<K, V>): void
```

将一个TreeMap中的所有元素添加到另一个TreeMap中。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-setAll(map: TreeMap<K, V>): void--><!--Device-TreeMap-setAll(map: TreeMap<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | [TreeMap](arkts-arkts-util-treemap-treemap-c.md)&lt;K, V&gt; | Yes | 将参数map中的所有元素添加到调用setAll方法的TreeMap对象中。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The setAll method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let map : TreeMap<string, number> = new TreeMap();
map.set("demo", 12);
map.setAll(treeMap); // Add all elements in the treeMap to the map.
map.forEach((value ?: number, key ?: string) : void => {
  console.info("value: " + value, "key: " + key); 
})
// Output:
// value: 12 key: demo
// value: 356 key: sparrow
// value: 123 key: squirrel
```

## values

```TypeScript
values(): IterableIterator<V>
```

返回包含此映射中键值的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-values(): IterableIterator<V>--><!--Device-TreeMap-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound. |

## Examples

```TypeScript
let treeMap = new TreeMap<string, number>();
treeMap.set("squirrel", 123);
treeMap.set("sparrow", 356);
let values = treeMap.values();
for (let value of values) {
  console.info("value:", value);
}
// value: 356
// value: 123
```

## length

```TypeScript
length: number
```

TreeMap的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TreeMap-length: number--><!--Device-TreeMap-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

