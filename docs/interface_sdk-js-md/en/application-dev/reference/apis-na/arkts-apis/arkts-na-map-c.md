# Map

A collection that stores key-value pairs where each key is unique

**Inheritance/Implementation:** Map implements ReadonlyMap<K, V>

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-export class Map--><!--Device-unnamed-export class Map-End-->

**System capability:** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

Returns an iterator over the entries of the Map.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-$_iterator(): IterableIterator<[K, V]>--><!--Device-Map-$_iterator(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[K, V]&gt; | iterator over entries. |

## clear

```TypeScript
clear(): void
```

Deletes all elements from the Map.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-clear(): void--><!--Device-Map-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(initialCapacity: int)
```

Creates an empty Map with the specified initial capacity

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-constructor(initialCapacity: int)--><!--Device-Map-constructor(initialCapacity: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| initialCapacity | int | Yes | Map's initial capacity &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
constructor(values: FixedArray<[K, V]>)
```

Creates a Map from a FixedArray containing key-value pairs

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-constructor(values: FixedArray<[K, V]>)--><!--Device-Map-constructor(values: FixedArray<[K, V]>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | FixedArray&lt;[K, V]&gt; | Yes | FixedArray containing key-value pairs |

## constructor

```TypeScript
constructor(entries: Array<[K, V]>)
```

Creates a Map from an array containing key-value pairs

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-constructor(entries: Array<[K, V]>)--><!--Device-Map-constructor(entries: Array<[K, V]>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entries | Array&lt;[K, V]&gt; | Yes | array containing key-value pairs |

## constructor

```TypeScript
constructor(map: Map<K, V>)
```

Creates a new Map from another Map

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-constructor(map: Map<K, V>)--><!--Device-Map-constructor(map: Map<K, V>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | Map&lt;K, V&gt; | Yes | source Map used to create the new Map |

## constructor

```TypeScript
constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)
```

Creates a Map from an iterable object or array-like object

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)--><!--Device-Map-constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entries | Iterable&lt;[K, V]&gt; \| readonly ((readonly [K, V]) \| null \| undefined)[] \| null | No | iterable object or array-like object containing key-value pairs |

## delete

```TypeScript
delete(key: K): boolean
```

Removes an Entry with specified key from the Map.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-delete(key: K): boolean--><!--Device-Map-delete(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to remove. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the entry was removed. |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns elements from the Map as an array of Entries.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-entries(): IterableIterator<[K, V]>--><!--Device-Map-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[K, V]&gt; | an array of Entries. |

## forEach

```TypeScript
forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void--><!--Device-Map-forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (v: V, k: K, map: Map&lt;K, V&gt;) =&gt; void | Yes | to apply. |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a value associated with key if present.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-get(key: K): V | undefined--><!--Device-Map-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to find in the Map. |

**Return value:**

| Type | Description |
| --- | --- |
| V | value if associated with key is present. |

## get

```TypeScript
get(key: K, def: V): V
```

Returns a value associated with key if present, or a default value otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-get(key: K, def: V): V--><!--Device-Map-get(key: K, def: V): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to find in the Map. |
| def | V | Yes | a value to return if key is not in the Map. |

**Return value:**

| Type | Description |
| --- | --- |
| V | value if key presents, def otherwise. |

## has

```TypeScript
has(key: K): boolean
```

Checks if a key is in the Map.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-has(key: K): boolean--><!--Device-Map-has(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to find in the Map. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is in the Map. |

## keySet

```TypeScript
public keySet(): Set<K>
```

Returns map keys as Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-public keySet(): Set<K>--><!--Device-Map-public keySet(): Set<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Set&lt;K&gt; | A new Set instance containing all of the keys. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Returns elements from the Map as an keys Iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-keys(): IterableIterator<K>--><!--Device-Map-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;K&gt; | iterator with map keys. |

## set

```TypeScript
set(key: K, val: V): this
```

Puts a pair of key and value into the Map.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-set(key: K, val: V): this--><!--Device-Map-set(key: K, val: V): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | the key to put into the Map. |
| val | V | Yes | the value to put into the Map. |

**Return value:**

| Type | Description |
| --- | --- |
| this | this Map. |

## toString

```TypeScript
toString(): string
```

Converts this Map to a String.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-toString(): string--><!--Device-Map-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the Map. |

## values

```TypeScript
values(): IterableIterator<V>
```

Returns elements from the Map as an values Iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Map-values(): IterableIterator<V>--><!--Device-Map-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;V&gt; | iterator with map values. |

