# Map

A collection that stores key-value pairs where each key is unique

**Inheritance/Implementation:** Map implements ReadonlyMap<K, V>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

Returns an iterator over the entries of the Map.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IterableIterator & lt;[K, V] & gt; |

## clear

```TypeScript
clear(): void
```

Deletes all elements from the Map.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(initialCapacity: int)
```

Creates an empty Map with the specified initial capacity

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| initialCapacity | int | Yes |

## constructor

```TypeScript
constructor(values: FixedArray<[K, V]>)
```

Creates a Map from a FixedArray containing key-value pairs

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [values](#values) | FixedArray & lt;[K, V] & gt; | Yes |

## constructor

```TypeScript
constructor(entries: Array<[K, V]>)
```

Creates a Map from an array containing key-value pairs

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [entries](#entries) | Array & lt;[K, V] & gt; | Yes |

## constructor

```TypeScript
constructor(map: Map<K, V>)
```

Creates a new Map from another Map

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| map | Map & lt;K, V & gt; | Yes |

## constructor

```TypeScript
constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)
```

Creates a Map from an iterable object or array-like object

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [entries](#entries) | Iterable & lt;[K, V] & gt; \ | readonly ((readonly [K, V]) \| null \| undefined)[] \| null | No |

## delete

```TypeScript
delete(key: K): boolean
```

Removes an Entry with specified key from the Map.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns elements from the Map as an array of Entries.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IterableIterator & lt;[K, V] & gt; |

## forEach

```TypeScript
forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (v: V, k: K, map: Map & lt;K, V & gt;) = & gt; void | Yes |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a value associated with key if present.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V \| undefined |

## get

```TypeScript
get(key: K, def: V): V
```

Returns a value associated with key if present, or a default value otherwise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |
| def | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## has

```TypeScript
has(key: K): boolean
```

Checks if a key is in the Map.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Returns elements from the Map as an keys Iterator.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IterableIterator & lt;K & gt; |

## keySet

```TypeScript
public keySet(): Set<K>
```

Returns map keys as Set.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Set & lt;K & gt; |

## set

```TypeScript
set(key: K, val: V): this
```

Puts a pair of key and value into the Map.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |
| val | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| this |

## toString

```TypeScript
toString(): string
```

Converts this Map to a String.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## values

```TypeScript
values(): IterableIterator<V>
```

Returns elements from the Map as an values Iterator.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IterableIterator & lt;V & gt; |

## size

```TypeScript
get size(): int
```

Returns the number of key-value pairs in the Map

**Type:** int

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
