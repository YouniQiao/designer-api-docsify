# LightWeightMap

LightWeightMap stores key-value (KV) pairs. Each key must be unique and have only one value.

**Since:** 8

<!--Device-unnamed-declare class LightWeightMap<K, V>--><!--Device-unnamed-declare class LightWeightMap<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { LightWeightMap } from '@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

returns an ES6 iterator.Each item of the iterator is a Javascript Object

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-LightWeightMap-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Clears this LightWeightMap and sets its length to **0**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-clear(): void--><!--Device-LightWeightMap-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

A constructor used to create a **LightWeightMap** instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-constructor()--><!--Device-LightWeightMap-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
```

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns an iterator that contains all the elements in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-entries(): IterableIterator<[K, V]>--><!--Device-LightWeightMap-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Uses a callback to traverse the elements in this LightWeightMap and obtain their indexes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void--><!--Device-LightWeightMap-forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value?: V, key?: K, map?: LightWeightMap & lt;K, V & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

## get

```TypeScript
get(key: K): V
```

Obtains the value of the specified key in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-get(key: K): V--><!--Device-LightWeightMap-get(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.get("sparrow");
console.info("result:", result);  // result: 356
```

## getIndexOfKey

```TypeScript
getIndexOfKey(key: K): number
```

Obtains the index of the first occurrence of an element with the specified key in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getIndexOfKey(key: K): int--><!--Device-LightWeightMap-getIndexOfKey(key: K): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getIndexOfKey("sparrow");
console.info("result:", result);  // result: 0
```

## getIndexOfValue

```TypeScript
getIndexOfValue(value: V): number
```

Obtains the index of the first occurrence of an element with the specified value in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getIndexOfValue(value: V): int--><!--Device-LightWeightMap-getIndexOfValue(value: V): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Obtains the key of an element at the specified position in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getKeyAt(index: number): K--><!--Device-LightWeightMap-getKeyAt(index: number): K-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| K |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getKeyAt(1);
console.info("result:", result);  // result: squirrel
```

## getValueAt

```TypeScript
getValueAt(index: number): V
```

Obtains the value of an element at the specified position in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-getValueAt(index: number): V--><!--Device-LightWeightMap-getValueAt(index: number): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.getValueAt(1);
console.info("result:", result);  // result: 123
```

## hasAll

```TypeScript
hasAll(map: LightWeightMap<K, V>): boolean
```

Checks whether this LightWeightMap contains all elements of the specified **LightWeightMap** instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-hasAll(map: LightWeightMap<K, V>): boolean--><!--Device-LightWeightMap-hasAll(map: LightWeightMap<K, V>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| map | [LightWeightMap](arkts-arkts-util-lightweightmap-lightweightmap-c.md)&lt;K, V&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Checks whether this LightWeightMap has the specified key.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-hasKey(key: K): boolean--><!--Device-LightWeightMap-hasKey(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Checks whether this LightWeightMap has the specified value.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-hasValue(value: V): boolean--><!--Device-LightWeightMap-hasValue(value: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("squirrel", 123);
let result = lightWeightMap.hasValue(123);
console.info("result:", result);  // result: true
```

## increaseCapacityTo

```TypeScript
increaseCapacityTo(minimumCapacity: number): void
```

Increases the capacity of this LightWeightMap. If the passed-in capacity is greater than or equal to the number of elements in this LightWeightMap, the capacity is changed to the new capacity. If the passed-in capacity is less than the number of elements in this LightWeightMap, the capacity is not changed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-increaseCapacityTo(minimumCapacity: int): void--><!--Device-LightWeightMap-increaseCapacityTo(minimumCapacity: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| minimumCapacity | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.increaseCapacityTo(10);
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this LightWeightMap is empty (contains no element).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-isEmpty(): boolean--><!--Device-LightWeightMap-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Returns an iterator that contains all the keys in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-keys(): IterableIterator<K>--><!--Device-LightWeightMap-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;K&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Removes an element with the specified key from this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-remove(key: K): V--><!--Device-LightWeightMap-remove(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let lightWeightMap = new LightWeightMap<string, number>();
lightWeightMap.set("sparrow", 356);
let result = lightWeightMap.remove("sparrow");
console.info("result:", result);  // result: 356
```

## removeAt

```TypeScript
removeAt(index: number): boolean
```

Removes an element at the specified position from this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-removeAt(index: int): boolean--><!--Device-LightWeightMap-removeAt(index: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Adds or updates an element in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-set(key: K, value: V): Object--><!--Device-LightWeightMap-set(key: K, value: V): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |
| value | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Adds all elements in a LightWeightMap to this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-setAll(map: LightWeightMap<K, V>): void--><!--Device-LightWeightMap-setAll(map: LightWeightMap<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| map | [LightWeightMap](arkts-arkts-util-lightweightmap-lightweightmap-c.md)&lt;K, V&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

```TypeScript
setValueAt(index: number, newValue: V): boolean
```

Sets a value for an element at the specified position in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-setValueAt(index: int, newValue: V): boolean--><!--Device-LightWeightMap-setValueAt(index: int, newValue: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| newValue | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200001-value-out-of-range) |

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

Concatenates the elements in this LightWeightMap into a string and returns the string.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-toString(): String--><!--Device-LightWeightMap-toString(): String-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| String |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Returns an iterator that contains all the values in this LightWeightMap.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-values(): IterableIterator<V>--><!--Device-LightWeightMap-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;V&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

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

Number of elements in a LightWeightMap.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LightWeightMap-length: number--><!--Device-LightWeightMap-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
