# ReadonlyMap

Represents a read-only Map

**Inheritance/Implementation:** ReadonlyMap extends [Iterable<[K, V]>][Iterable<[K, V]>](Iterable<[K, V]>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface ReadonlyMap<K, V> extends Iterable<[K, V]>--><!--Device-unnamed-export interface ReadonlyMap<K, V> extends Iterable<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns elements from the Map as an array of Entries.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-entries(): IterableIterator<[K, V]>--><!--Device-ReadonlyMap-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[K, V]&gt; | an array of Entries. |

## forEach

```TypeScript
forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void): void--><!--Device-ReadonlyMap-forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: V, key: K, map: ReadonlyMap&lt;K, V&gt;) =&gt; void | Yes | to apply. |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a value associated with key if present.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-get(key: K): V | undefined--><!--Device-ReadonlyMap-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to find in the Map/class. |

**Return value:**

| Type | Description |
| --- | --- |
| V | value if associated with key is present. |

## has

```TypeScript
has(key: K): boolean
```

Checks if a key is in the Map.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-has(key: K): boolean--><!--Device-ReadonlyMap-has(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to find in the Map. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is in the Map. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Returns elements from the Map as an keys Iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-keys(): IterableIterator<K>--><!--Device-ReadonlyMap-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;K&gt; | ValueIterator with map keys. |

## values

```TypeScript
values(): IterableIterator<V>
```

Returns elements from the Map as an values Iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-values(): IterableIterator<V>--><!--Device-ReadonlyMap-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;V&gt; | ValueIterator with map values. |

## size

```TypeScript
get size(): int
```

Returns number of Entries with unique keys in the Map.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyMap-get size(): int--><!--Device-ReadonlyMap-get size(): int-End-->

**System capability:** SystemCapability.Utils.Lang

