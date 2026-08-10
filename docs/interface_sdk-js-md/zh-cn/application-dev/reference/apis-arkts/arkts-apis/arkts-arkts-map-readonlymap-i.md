# ReadonlyMap

Represents a read-only Map

**继承/实现关系：** ReadonlyMap extends [Iterable<[K, V]>]{@link Iterable<[K, V]>}

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ReadonlyMap<K, V> extends Iterable<[K, V]>--><!--Device-unnamed-export interface ReadonlyMap<K, V> extends Iterable<[K, V]>-End-->

**系统能力：** SystemCapability.Utils.Lang

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns elements from the Map as an array of Entries.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-entries(): IterableIterator<[K, V]>--><!--Device-ReadonlyMap-entries(): IterableIterator<[K, V]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | an array of Entries. |

## forEach

```TypeScript
forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void): void--><!--Device-ReadonlyMap-forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: V, key: K, map: ReadonlyMap&lt;K, V&gt;) =&gt; void | 是 | to apply. |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a value associated with key if present.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-get(key: K): V | undefined--><!--Device-ReadonlyMap-get(key: K): V | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to find in the Map/class. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | value if associated with key is present. |

## has

```TypeScript
has(key: K): boolean
```

Checks if a key is in the Map.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-has(key: K): boolean--><!--Device-ReadonlyMap-has(key: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | the key to find in the Map. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value is in the Map. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Returns elements from the Map as an keys Iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-keys(): IterableIterator<K>--><!--Device-ReadonlyMap-keys(): IterableIterator<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | ValueIterator with map keys. |

## values

```TypeScript
values(): IterableIterator<V>
```

Returns elements from the Map as an values Iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-values(): IterableIterator<V>--><!--Device-ReadonlyMap-values(): IterableIterator<V>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; | ValueIterator with map values. |

## size

```TypeScript
get size(): int
```

Returns number of Entries with unique keys in the Map.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyMap-get size(): int--><!--Device-ReadonlyMap-get size(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

