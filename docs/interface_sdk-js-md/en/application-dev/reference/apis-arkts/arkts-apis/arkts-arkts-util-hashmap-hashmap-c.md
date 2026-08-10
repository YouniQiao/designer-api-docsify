# HashMap

HashMap底层采用数组、链表和红黑树实现，支持高效查询、插入和删除。HashMap存储内容基于键值对映射，不允许重复的key，且一个key只能对应一个value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class HashMap<K, V>--><!--Device-unnamed-declare class HashMap<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { HashMap } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

返回一个迭代器，迭代器的每一项都是一个包含键和值的数组[K, V]。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashMap-$_iterator(): IterableIterator<[K, V]>--><!--Device-HashMap-$_iterator(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | HashMap的迭代器。 |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

返回一个迭代器，迭代器的每一项都是一个包含键和值的数组[K, V]。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-HashMap-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 返回包含此HashMap中所有键值对的迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);

// Method 1:
for (let item of hashMap) {
  console.info("key:", item[0]);
  console.info("value:", item[1]);
}
// key: squirrel
// value: 123
// key: sparrow
// value: 356

// Method 2:
let iter = hashMap[Symbol.iterator]();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:", temp.value[0]);
  console.info("value:", temp.value[1]);
  temp = iter.next();
}
// key: squirrel
// value: 123
// key: sparrow
// value: 356
```

```TypeScript
// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
```

## clear

```TypeScript
clear(): void
```

清除HashMap中的所有元素，并将length置为0。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-clear(): void--><!--Device-HashMap-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
hashMap.clear();
let result = hashMap.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

创建HashMap实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-constructor()--><!--Device-HashMap-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The HashMap's constructor cannot be directly invoked. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
```

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

返回此HashMap中包含的键值对的新迭代器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-entries(): IterableIterator<[K, V]>--><!--Device-HashMap-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 返回包含此HashMap中所有键值对的迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let iter = hashMap.entries();
let temp: IteratorResult<Object[]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value[0]);
  console.info("value:" + temp.value[1]);
  temp = iter.next();
}
```

```TypeScript
// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void
```

在遍历过程中对每个元素调用一次回调函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void--><!--Device-HashMap-forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value?: V, key?: K, map?: HashMap&lt;K, V&gt;) =&gt; void | Yes | 回调函数。 |
| thisArg | Object | No | callbackFn被调用时用作this值，默认值为当前实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("sparrow", 123);
hashMap.set("gull", 357);
hashMap.forEach((value: number, key: string) => {
  console.info("value: " + value, "key: " + key);
});
// value: 123 key: sparrow
// value: 357 key: gull
```

```TypeScript
// You are not advised to use the set or remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: HashMapCbFn<K, V>): void
```

通过回调函数遍历此容器中的元素，并获取其位置索引。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashMap-forEach(callbackFn: HashMapCbFn<K, V>): void--><!--Device-HashMap-forEach(callbackFn: HashMapCbFn<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [HashMapCbFn](arkts-arkts-hashmapcbfn-t.md)&lt;K, V&gt; | Yes | 用于遍历容器中元素的回调函数。 |

## get

```TypeScript
get(key: K): V
```

获取指定key对应的value，不存在返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-get(key: K): V--><!--Device-HashMap-get(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定要获取其对应value的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回key映射的value值；key不存在时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The get method cannot be bound. |

## Examples

```TypeScript
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let result = hashMap.get("sparrow");
console.info("result:", result);  // result: 356
```

## get

```TypeScript
get(key: K): V | undefined
```

获取此容器中指定key对应的值。如果未获取到，则返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashMap-get(key: K): V | undefined--><!--Device-HashMap-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 查找的指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 值或undefined。 |

## hasKey

```TypeScript
hasKey(key: K): boolean
```

判断此HashMap中是否包含指定key。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-hasKey(key: K): boolean--><!--Device-HashMap-hasKey(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定要查询的键，用于判断HashMap中是否包含该键。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定key返回true，不包含指定key返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The hasKey method cannot be bound. |

## Examples

```TypeScript
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
let result = hashMap.hasKey("squirrel");
console.info("result:", result);  // result: true
```

## hasValue

```TypeScript
hasValue(value: V): boolean
```

判断此HashMap中是否包含指定value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-hasValue(value: V): boolean--><!--Device-HashMap-hasValue(value: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | 指定要查询的值，用于判断HashMap中是否包含该值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 包含指定的value返回true，不包含指定的value返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The hasValue method cannot be bound. |

## Examples

```TypeScript
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
let result = hashMap.hasValue(123);
console.info("result:", result);  // result: true
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断该HashMap是否为空。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-isEmpty(): boolean--><!--Device-HashMap-isEmpty(): boolean-End-->

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
const hashMap = new HashMap<string, number>();
let result = hashMap.isEmpty();
console.info("result = ", result) // result = true
```

## keys

```TypeScript
keys(): IterableIterator<K>
```

返回新迭代器对象，包含此HashMap中所有的键。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-keys(): IterableIterator<K>--><!--Device-HashMap-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | 返回包含此HashMap中所有key的迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The keys method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let keys = hashMap.keys();
for (let key of keys) {
  console.info("key:" + key);
}
// key:squirrel
// key:sparrow
```

## remove

```TypeScript
remove(key: K): V
```

删除指定key对应的元素，并返回该元素的value。若key不存在，则返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-remove(key: K): V--><!--Device-HashMap-remove(key: K): V-End-->

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
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let result = hashMap.remove("sparrow");
console.info("result:", result);  // result: 356
```

## remove

```TypeScript
remove(key: K): V | undefined
```

删除此容器中指定key所对应的元素。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashMap-remove(key: K): V | undefined--><!--Device-HashMap-remove(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 如果删除了指定key则返回其关联的值，否则返回undefined。 |

## replace

```TypeScript
replace(key: K, newValue: V): boolean
```

替换指定键对应的值。仅当指定key已存在时才执行替换并返回true，若key不存在则不修改HashMap并返回false。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-replace(key: K, newValue: V): boolean--><!--Device-HashMap-replace(key: K, newValue: V): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 依据key指定替换的元素，仅当key已存在时替换生效。 |
| newValue | V | Yes | 替换指定key对应value的新值。仅当指定key已存在时，newValue才会替换原有value；若key不存在，该值不会被设置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否成功对已有数据进行替换，成功返回true，失败返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The replace method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("sparrow", 123);
let result = hashMap.replace("sparrow", 357);
console.info("result:", result);  // result: true
```

## set

```TypeScript
set(key: K, value: V): Object
```

向HashMap中添加或更新一个键值对。若key不存在，则添加新的键值对；若key已存在，则更新其对应的value。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-set(key: K, value: V): Object--><!--Device-HashMap-set(key: K, value: V): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 添加或更新的键名。若key已存在，将替换对应的value。 |
| value | V | Yes | 添加或更新的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 返回包含添加或更新后元素的当前HashMap实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The set method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123)
console.info("result:", hashMap.get("squirrel"));  // result: 123
```

## setAll

```TypeScript
setAll(map: HashMap<K, V>): void
```

将指定HashMap中的所有元素设置到当前HashMap中，若当前HashMap中已存在相同key，则对应value会被覆盖。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-setAll(map: HashMap<K, V>): void--><!--Device-HashMap-setAll(map: HashMap<K, V>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | [HashMap](arkts-arkts-util-hashmap-hashmap-c.md)&lt;K, V&gt; | Yes | 需要将其全部元素添加到当前HashMap的源HashMap对象。若map与当前HashMap存在重复key，map中的value将替换当前HashMap中对应key的value。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The setAll method cannot be bound. |

## Examples

```TypeScript
const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let newHashMap = new HashMap<string, number>();
newHashMap.set("newMap", 99);
hashMap.setAll(newHashMap);
let result = hashMap.hasKey("newMap");
console.info("result:", result);  // result: true
```

## values

```TypeScript
values(): IterableIterator<V>
```

返回新迭代器对象，包含此HashMap中所有键对应的值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-values(): IterableIterator<V>--><!--Device-HashMap-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; | 返回包含此HashMap中所有value的迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound. |

## Examples

```TypeScript
let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let values = hashMap.values();
for (let value of values) {
  console.info("value:", value)
}
// value: 123
// value: 356
```

## length

```TypeScript
length: number
```

HashMap的元素个数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashMap-length: number--><!--Device-HashMap-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

