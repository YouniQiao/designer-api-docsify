# SendableLruCache

Object used for store least recently used sendable Object.

**Since:** 18

**Deprecated since:** -1

<!--Device-utils-class SendableLruCache--><!--Device-utils-class SendableLruCache-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArkTSUtils } from '@kit.ArkTS';
```

## clear

```TypeScript
clear(): void
```

Clear all key-value pairs from the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-clear(): void--><!--Device-SendableLruCache-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(capacity?: number)
```

Default constructor.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-constructor(capacity?: number)--><!--Device-SendableLruCache-constructor(capacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capacity | number | No |

## contains

```TypeScript
contains(key: K): boolean
```

Check whether the given key exists in the SendableLruCache. If exists, returns true; otherwise, returns false.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-contains(key: K): boolean--><!--Device-SendableLruCache-contains(key: K): boolean-End-->

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

Returns an iterable of key-value pairs for each element in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-entries(): IterableIterator<[K, V]>--><!--Device-SendableLruCache-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

## get

```TypeScript
get(key: K): V | undefined
```

Get the value associated with a specified key in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-get(key: K): V | undefined--><!--Device-SendableLruCache-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## getCapacity

```TypeScript
getCapacity(): number
```

Get the Capacity of the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-getCapacity(): number--><!--Device-SendableLruCache-getCapacity(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCreateCount

```TypeScript
getCreateCount(): number
```

Get the number of times createDefault in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-getCreateCount(): number--><!--Device-SendableLruCache-getCreateCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMatchCount

```TypeScript
getMatchCount(): number
```

Get the number of times that the queried values are matched in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-getMatchCount(): number--><!--Device-SendableLruCache-getMatchCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMissCount

```TypeScript
getMissCount(): number
```

Get the number of times that the queried values are not matched in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-getMissCount(): number--><!--Device-SendableLruCache-getMissCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getPutCount

```TypeScript
getPutCount(): number
```

Get the number of times that values are added to SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-getPutCount(): number--><!--Device-SendableLruCache-getPutCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getRemoveCount

```TypeScript
getRemoveCount(): number
```

Get the number of times that values are removed from the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-getRemoveCount(): number--><!--Device-SendableLruCache-getRemoveCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether the SendableLruCache is empty.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-isEmpty(): boolean--><!--Device-SendableLruCache-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(): K[]
```

Returns a list of all keys in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-keys(): K[]--><!--Device-SendableLruCache-keys(): K[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| K[] |

## put

```TypeScript
put(key: K, value: V): V
```

Adds a key-value pair to the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-put(key: K, value: V): V--><!--Device-SendableLruCache-put(key: K, value: V): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |
| value | V | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## remove

```TypeScript
remove(key: K): V | undefined
```

Remove a specified key and its associated value from the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-remove(key: K): V | undefined--><!--Device-SendableLruCache-remove(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## toString

```TypeScript
toString(): string
```

Return the string representation of the object. The returned string format is: SendableLruCache[ maxSize = (maxSize), hits = (hitCount), misses = (missCount), hitRate = (hitRate) ]. (maxSize) represents the maximum size of the cache, (hitCount) indicates the number of successful query matches, (missCount) denotes the number of failed query matches, (hitRate) signifies the query match rate.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-toString(): string--><!--Device-SendableLruCache-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## updateCapacity

```TypeScript
updateCapacity(newCapacity: number): void
```

Update the capacity of the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-updateCapacity(newCapacity: number): void--><!--Device-SendableLruCache-updateCapacity(newCapacity: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newCapacity | number | Yes |

## values

```TypeScript
values(): V[]
```

Returns a list of all values in the SendableLruCache.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-values(): V[]--><!--Device-SendableLruCache-values(): V[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V[] |

## length

```TypeScript
readonly length: number
```

The length of the SendableLruCache.

**Type:** number

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SendableLruCache-readonly length: number--><!--Device-SendableLruCache-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
