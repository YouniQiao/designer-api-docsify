# LightWeightMap

LightWeightMap可用于存储具有关联关系的key-value键值对，其中key值唯一，每个key对应一个value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class LightWeightMap<K, V>--><!--Device-unnamed-declare class LightWeightMap<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { LightWeightMap } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

返回一个迭代器，迭代器的每一项都是一个包含键和值的[K, V]数组。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightMap-$_iterator(): IterableIterator<[K, V]>--><!--Device-LightWeightMap-$_iterator(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | LightWeightMap的迭代器。 |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

返回一个迭代器，迭代器的每一项都是一个包含键和值的[K, V]数组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-LightWeightMap-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

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
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);

// Method 1:
for (let item of lightWeightMap) {
  console.info("key:", item[0]);
  console.info("value:", item[1]);
}
// key: sparrow
// value: 356
// key: squirrel
// value: 123

// Method 2:
let iter = lightWeightMap[Symbol.iterator]();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:", temp.value[0]);
  console.info("value:", temp.value[1]);
  temp = iter.next();
}
// key: sparrow
// value: 356
// key: squirrel
// value: 123
```

```TypeScript
// You are not advised to use the set, setValueAt, remove, or removeAt APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightMap = new LightWeightMap<string, number>();
for(let i = 0; i < 10; i++) {
  lightWeightMap.set("sparrow" + i, 123);
}
for(let i = 0; i < 10; i++) {
  lightWeightMap.remove("sparrow" + i);
}
```

## clear

```TypeScript
clear(): void
```

清除LightWeightMap中的所有元素，并将length置为0。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-clear(): void--><!--Device-LightWeightMap-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
lightWeightMap.clear();
let result = lightWeightMap.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

LightWeightMap的构造函数，创建一个空的LightWeightMap实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-constructor()--><!--Device-LightWeightMap-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The LightWeightMap's constructor cannot be directly invoked. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
```

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

返回包含此映射中所有键值对的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-entries(): IterableIterator<[K, V]>--><!--Device-LightWeightMap-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 返回包含此映射中所有键值对的迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let iter = lightWeightMap.entries();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value[0]);
  console.info("value:" + temp.value[1]);
  temp = iter.next();
}
```

```TypeScript
// You are not advised to use the set, setValueAt, remove, or removeAt APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightMap = new LightWeightMap<string, number>();
for(let i = 0; i < 10; i++) {
  lightWeightMap.set("sparrow" + i, 123);
}
for(let i = 0; i < 10; i++) {
  lightWeightMap.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void
```

通过回调函数来遍历实例对象上的元素及其键值对信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void--><!--Device-LightWeightMap-forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value?: V, key?: K, map?: LightWeightMap&lt;K, V&gt;) =&gt; void | Yes | 回调函数，用于遍历LightWeightMap实例中的元素及下标。 |
| thisArg | Object | No | callbackFn被调用时用作this值。当需要回调函数中的this指向非当前实例对象时传入此参数，当不需要改变this指向时可不传入。不传入时，默认值为当前实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("sparrow", 123);
lightWeightMap.set("gull", 357);
lightWeightMap.forEach((value: number, key: string) => {
  console.info("value:" + value, "key:" + key);
});
// value:123 key:sparrow
// value:357 key:gull
```

```TypeScript
// You are not advised to use the set, setValueAt, remove, or removeAt APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightMap = new LightWeightMap<string, number>();
for(let i = 0; i < 10; i++) {
  lightWeightMap.set("sparrow" + i, 123);
}
for(let i = 0; i < 10; i++) {
  lightWeightMap.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: LightWeightMapCbFn<K, V>): void
```

通过回调函数来遍历实例对象上的元素及其下标。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightMap-forEach(callbackFn: LightWeightMapCbFn<K, V>): void--><!--Device-LightWeightMap-forEach(callbackFn: LightWeightMapCbFn<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [LightWeightMapCbFn](arkts-arkts-lightweightmapcbfn-t.md)&lt;K, V&gt; | Yes | 回调函数。 |

## get

```TypeScript
get(key: K): V
```

获取指定key所对应的value。当key为number类型且值大于INT32_MAX或小于INT32_MIN时，结果可能与预期不一致。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-get(key: K): V--><!--Device-LightWeightMap-get(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回key映射的value值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The get method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.get("sparrow");
console.info("result:", result);  // result: 356
```

## get

```TypeScript
get(key: K): V | undefined
```

获取指定key所对应的value。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightMap-get(key: K): V | undefined--><!--Device-LightWeightMap-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 如果存在与key关联的值则返回该值，否则返回undefined。 |

## getIndexOfKey

ArkTS-Dyn:
```TypeScript
getIndexOfKey(key: K): number
```

ArkTS-Sta:
```TypeScript
getIndexOfKey(key: K): int
```

查找key元素首次出现的下标值，如果未找到返回-1。当key为number类型且值大于INT32_MAX或小于INT32_MIN时，结果可能与预期不一致。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getIndexOfKey(key: K): int--><!--Device-LightWeightMap-getIndexOfKey(key: K): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 被查找的元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回key元素首次出现的下标值，查找失败返回-1。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getIndexOfKey method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getIndexOfKey("sparrow");
console.info("result:", result);  // result: 0
```

## getIndexOfValue

ArkTS-Dyn:
```TypeScript
getIndexOfValue(value: V): number
```

ArkTS-Sta:
```TypeScript
getIndexOfValue(value: V): int
```

查找指定value元素首次出现的下标值，如果未找到则返回-1。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getIndexOfValue(value: V): int--><!--Device-LightWeightMap-getIndexOfValue(value: V): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | 要查找首次出现下标位置的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回value元素首次出现的下标值，查找失败返回-1。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getIndexOfValue method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getIndexOfValue(123);
console.info("result:", result);  // result: 1
```

## getKeyAt

```TypeScript
getKeyAt(index: number): K
```

查找指定下标的元素键值对中key值，如果未找到则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getKeyAt(index: number): K--><!--Device-LightWeightMap-getKeyAt(index: number): K-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 所查找的下标。需要小于等于INT32_MAX即2147483647。 |

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回该下标对应的元素键值对中key值，如果未找到则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getKeyAt method cannot be bound. |
| 10200001 | The value of index is out of range. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getKeyAt(1);
console.info("result:", result);  // result: squirrel
```

## getKeyAt

```TypeScript
getKeyAt(index: int): K | undefined
```

查找指定下标的元素键值对中key值，如果未找到则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightMap-getKeyAt(index: int): K | undefined--><!--Device-LightWeightMap-getKeyAt(index: int): K | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 所查找的下标。需要小于等于int32_max即2147483647。 取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| K | 返回指定下标对应的key，如果下标超出范围则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of index is out of range. |

## getValueAt

```TypeScript
getValueAt(index: number): V
```

获取指定下标对应键值对中的值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getValueAt(index: number): V--><!--Device-LightWeightMap-getValueAt(index: number): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 指定下标。需要小于等于INT32_MAX即2147483647。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回指定下标对应键值对中的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The getValueAt method cannot be bound. |
| 10200001 | The value of index is out of range. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getValueAt(1);
console.info("result:", result);  // result: 123
```

## getValueAt

```TypeScript
getValueAt(index: int): V | undefined
```

获取指定下标对应键值对中的值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightMap-getValueAt(index: int): V | undefined--><!--Device-LightWeightMap-getValueAt(index: int): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 指定下标。需要小于等于int32_max即2147483647。 取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回指定下标对应的值，如果下标超出范围则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of index is out of range. |

## hasAll

```TypeScript
hasAll(map: LightWeightMap<K, V>): boolean
```

判断LightWeightMap中是否包含指定map中的所有元素。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-hasAll(map: LightWeightMap<K, V>): boolean--><!--Device-LightWeightMap-hasAll(map: LightWeightMap<K, V>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | [LightWeightMap](arkts-arkts-util-lightweightmap-lightweightmap-c.md)&lt;K, V&gt; | Yes | 用于比较的LightWeightMap对象，判断当前实例是否包含此map中的所有元素。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含所有元素返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The hasAll method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let map = new LightWeightMap<string, number>();
map.set("sparrow", 356);
let result = lightWeightMap.hasAll(map); 
console.info("result = ", result); // result = true
```

## hasKey

```TypeScript
hasKey(key: K): boolean
```

判断LightWeightMap中是否包含指定key。当key为number类型且值大于INT32_MAX或小于INT32_MIN时，结果可能与预期不一致，详见规格限制。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-hasKey(key: K): boolean--><!--Device-LightWeightMap-hasKey(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。当key为number类型且值大于INT32_MAX或小于INT32_MIN时，结果可能与预期不一致。 |

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
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
let result = lightWeightMap.hasKey("squirrel");
console.info("result:", result);  // result: true
```

## hasValue

```TypeScript
hasValue(value: V): boolean
```

判断LightWeightMap中是否包含指定value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-hasValue(value: V): boolean--><!--Device-LightWeightMap-hasValue(value: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | 要判断是否包含的value。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定元素返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The hasValue method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
let result = lightWeightMap.hasValue(123);
console.info("result:", result);  // result: true
```

## increaseCapacityTo

ArkTS-Dyn:
```TypeScript
increaseCapacityTo(minimumCapacity: number): void
```

ArkTS-Sta:
```TypeScript
increaseCapacityTo(minimumCapacity: int): void
```

将当前LightWeightMap扩容至指定容量。如果传入的容量值大于或等于当前LightWeightMap中的元素个数，将容量扩容至新容量，小于则不会变更。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-increaseCapacityTo(minimumCapacity: int): void--><!--Device-LightWeightMap-increaseCapacityTo(minimumCapacity: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minimumCapacity | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 需要容纳的元素数量。取值需大于等于0，大于等于当前元素个数时扩容生效，否则不变更容量。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The increaseCapacityTo method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.increaseCapacityTo(10);
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断LightWeightMap是否为空。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-isEmpty(): boolean--><!--Device-LightWeightMap-isEmpty(): boolean-End-->

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
const lightWeightMap = new LightWeightMap<string, number>();
let result = lightWeightMap.isEmpty();
console.info("result:", result);  // result: true
```

## keys

```TypeScript
keys(): IterableIterator<K>
```

返回包含此映射中所有的键的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-keys(): IterableIterator<K>--><!--Device-LightWeightMap-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | 返回一个迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The keys method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let keys = lightWeightMap.keys();
for (let key of keys) {
  console.info("key:", key);
}
// key: sparrow
// key: squirrel
```

## remove

```TypeScript
remove(key: K): V
```

删除指定key映射的元素。当key为number类型且值大于INT32_MAX或小于INT32_MIN时，结果可能与预期不一致。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-remove(key: K): V--><!--Device-LightWeightMap-remove(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

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
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.remove("sparrow");
console.info("result:", result);  // result: 356
```

## remove

```TypeScript
remove(key: K): V | undefined
```

删除指定key映射的元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LightWeightMap-remove(key: K): V | undefined--><!--Device-LightWeightMap-remove(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 如果删除了元素则返回该元素的值，否则返回undefined。 |

## removeAt

ArkTS-Dyn:
```TypeScript
removeAt(index: number): boolean
```

ArkTS-Sta:
```TypeScript
removeAt(index: int): boolean
```

删除指定下标对应的元素。调用成功后，若下标有效则该位置的键值对从LightWeightMap中移除且length减少。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-removeAt(index: int): boolean--><!--Device-LightWeightMap-removeAt(index: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要删除的元素的下标位置。取值范围：[0, length-1]，需小于等于INT32_MAX即2147483647。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 成功删除元素返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The removeAt method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.removeAt(1);
console.info("result:", result);  // result: true
```

## set

```TypeScript
set(key: K, value: V): Object
```

向LightWeightMap中添加或更新一组数据。调用成功后，若key不存在则新增键值对且length增加，若key已存在则更新对应value值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-set(key: K, value: V): Object--><!--Device-LightWeightMap-set(key: K, value: V): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 添加或更新成员数据的键名。当key为number类型且值大于INT32_MAX或小于INT32_MIN时，结果可能与预期不一致。 |
| value | V | Yes | 添加或更新成员数据的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 返回添加或更新后的LightWeightMap实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The set method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
let result = lightWeightMap.set("squirrel", 123);
console.info("result:", result);  // result: squirrel:123
```

## setAll

```TypeScript
setAll(map: LightWeightMap<K, V>): void
```

将一个LightWeightMap中的所有元素添加到另一个LightWeightMap中，如果目标LightWeightMap中已存在相同的key，则会更新其对应的value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-setAll(map: LightWeightMap<K, V>): void--><!--Device-LightWeightMap-setAll(map: LightWeightMap<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | [LightWeightMap](arkts-arkts-util-lightweightmap-lightweightmap-c.md)&lt;K, V&gt; | Yes | 提供添加元素的LightWeightMap。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The setAll method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let map = new LightWeightMap<string, number>();
map.setAll(lightWeightMap);   // Add all elements in lightWeightMap to the map.
let result = map.get("sparrow");
console.info("result:", result);  // result: 356
```

## setValueAt

ArkTS-Dyn:
```TypeScript
setValueAt(index: number, newValue: V): boolean
```

ArkTS-Sta:
```TypeScript
setValueAt(index: int, newValue: V): boolean
```

替换指定下标对应键值对中的值。调用成功后，指定下标处键值对的值将被替换为newValue。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-setValueAt(index: int, newValue: V): boolean--><!--Device-LightWeightMap-setValueAt(index: int, newValue: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定下标。需要小于等于INT32_MAX即2147483647。 |
| newValue | V | Yes | 替换键值对中的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 成功替换返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The setValueAt method cannot be bound. |
| 10200001 | The value of index is out of range. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
lightWeightMap.setValueAt(1, 3546);
console.info("result:", lightWeightMap.get("squirrel"));  // result: 3546
```

## toString

```TypeScript
toString(): String
```

将此映射中包含的键值对拼接成字符串并返回。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-toString(): String--><!--Device-LightWeightMap-toString(): String-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| String | 返回将此映射中键值对拼接而成的字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The toString method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.toString();
console.info("result:", result);  // result: sparrow:356,squirrel:123
```

## values

```TypeScript
values(): IterableIterator<V>
```

返回包含此映射中所有值的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-values(): IterableIterator<V>--><!--Device-LightWeightMap-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; | 返回一个迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound. |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let values = lightWeightMap.values();
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

LightWeightMap的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-length: number--><!--Device-LightWeightMap-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

