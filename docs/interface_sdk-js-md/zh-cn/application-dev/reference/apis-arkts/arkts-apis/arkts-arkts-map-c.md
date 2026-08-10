# Map

A collection that stores key-value pairs where each key is unique

**继承/实现关系：** Map implements [ReadonlyMap<K, V>](ReadonlyMap<K, V>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Map<K, V> implements ReadonlyMap<K, V>--><!--Device-unnamed-export class Map<K, V> implements ReadonlyMap<K, V>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

Returns an iterator over the entries of the Map.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-$_iterator(): IterableIterator<[K, V]>--><!--Device-Map-$_iterator(): IterableIterator<[K, V]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | iterator over entries. |

## clear

```TypeScript
clear(): void
```

Deletes all elements from the Map.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-clear(): void--><!--Device-Map-clear(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(initialCapacity: int)
```

Creates an empty Map with the specified initial capacity

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(initialCapacity: int)--><!--Device-Map-constructor(initialCapacity: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initialCapacity | int | 是 | Map's initial capacity &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
constructor(values: FixedArray<[K, V]>)
```

Creates a Map from a FixedArray containing key-value pairs

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(values: FixedArray<[K, V]>)--><!--Device-Map-constructor(values: FixedArray<[K, V]>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | FixedArray&lt;[K, V]&gt; | 是 | FixedArray containing key-value pairs |

## constructor

```TypeScript
constructor(entries: Array<[K, V]>)
```

Creates a Map from an array containing key-value pairs

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(entries: Array<[K, V]>)--><!--Device-Map-constructor(entries: Array<[K, V]>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | Array&lt;[K, V]&gt; | 是 | array containing key-value pairs |

## constructor

```TypeScript
constructor(map: Map<K, V>)
```

Creates a new Map from another Map

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(map: Map<K, V>)--><!--Device-Map-constructor(map: Map<K, V>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | Map&lt;K, V&gt; | 是 | source Map used to create the new Map |

## constructor

```TypeScript
constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)
```

Creates a Map from an iterable object or array-like object

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)--><!--Device-Map-constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | Iterable&lt;[K, V]&gt; \| readonly ((readonly [K, V]) \| null \| undefined)[] \| null | 否 | iterable object or array-like object containing key-value pairs |

## delete

```TypeScript
delete(key: K): boolean
```

Removes an Entry with specified key from the Map.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-delete(key: K): boolean--><!--Device-Map-delete(key: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to remove. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the entry was removed. |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns elements from the Map as an array of Entries.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-entries(): IterableIterator<[K, V]>--><!--Device-Map-entries(): IterableIterator<[K, V]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | an array of Entries. |

## forEach

```TypeScript
forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void--><!--Device-Map-forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (v: V, k: K, map: Map&lt;K, V&gt;) =&gt; void | 是 | to apply. |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a value associated with key if present.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-get(key: K): V | undefined--><!--Device-Map-get(key: K): V | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to find in the Map. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | value if associated with key is present. |

## get

```TypeScript
get(key: K, def: V): V
```

Returns a value associated with key if present, or a default value otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-get(key: K, def: V): V--><!--Device-Map-get(key: K, def: V): V-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to find in the Map. |
| def | V | 是 | a value to return if key is not in the Map. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | value if key presents, def otherwise. |

## has

```TypeScript
has(key: K): boolean
```

Checks if a key is in the Map.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-has(key: K): boolean--><!--Device-Map-has(key: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to find in the Map. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value is in the Map. |

## keySet

```TypeScript
public keySet(): Set<K>
```

Returns map keys as Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-public keySet(): Set<K>--><!--Device-Map-public keySet(): Set<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Set&lt;K&gt; | A new Set instance containing all of the keys. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Returns elements from the Map as an keys Iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-keys(): IterableIterator<K>--><!--Device-Map-keys(): IterableIterator<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | iterator with map keys. |

## set

```TypeScript
set(key: K, val: V): this
```

Puts a pair of key and value into the Map.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-set(key: K, val: V): this--><!--Device-Map-set(key: K, val: V): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to put into the Map. |
| val | V | 是 | the value to put into the Map. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | this Map. |

## toString

```TypeScript
toString(): string
```

Converts this Map to a String.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-toString(): string--><!--Device-Map-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the Map. |

## values

```TypeScript
values(): IterableIterator<V>
```

Returns elements from the Map as an values Iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-values(): IterableIterator<V>--><!--Device-Map-values(): IterableIterator<V>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; | iterator with map values. |

## size

```TypeScript
get size(): int
```

Returns the number of key-value pairs in the Map

**类型：** int

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-get size(): int--><!--Device-Map-get size(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

