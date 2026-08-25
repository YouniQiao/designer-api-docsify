# LRUCache

Provides APIs to discard the least recently used data to make rooms for new elements when the cache is full. This class uses the Least Recently Used (LRU) algorithm, which believes that the recently used data may be accessed again in the near future and the least accessed data is the least valuable data and should be removed from the cache.

**Since:** 9

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

Specifies the default iterator for an object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

## afterRemoval

```TypeScript
afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void
```

Performs subsequent operations after a value is removed. The subsequent operations must be implemented by developers. This API is called during deletion operations, such as [get&lt;sup&gt;9+&lt;/sup&gt;](#get), [put&lt;sup&gt;9+&lt;/sup&gt;](#put), [remove&lt;sup&gt;9+&lt;/sup&gt;](#remove), [clear&lt;sup&gt;9+&lt;/sup&gt;](#clear), and [updateCapacity&lt;sup&gt;9+&lt;/sup&gt;](#updatecapacity).

> **NOTE：**&gt;
> If the callback method is executed after [clear&lt;sup&gt;9+&lt;/sup&gt;](#clear) and
> [updateCapacity&lt;sup&gt;9+&lt;/sup&gt;](#updatecapacity) are called and the input **key** and
> **value** parameters are of the MapIterator type, perform subsequent operations by referring to example 2.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEvict | boolean | Yes |
| key | K | Yes |
| value | V | Yes |
| newValue | V | Yes |

## clear

```TypeScript
clear(): void
```

Clears key-value pairs from this cache.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(capacity?: number)
```

A constructor used to create a **LRUCache** instance. The default capacity of the cache is 64.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capacity | number | No |

## contains

```TypeScript
contains(key: K): boolean
```

Checks whether this cache contains the specified key.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## createDefault

```TypeScript
createDefault(key: K): V
```

Performs subsequent operations if no key is matched in the cache and returns the value (**undefined** by default) associated with the key.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Returns an iterator object that traverses all key-value pairs ([key, value]) in this object in the insertion order.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

## get

```TypeScript
get(key: K): V | undefined
```

Obtains the value of a key. If the key is not in the cache, [createDefault&lt;sup&gt;9+&lt;/sup&gt;](#createdefault) is called to create the key. If the value specified in **createDefault** is not **undefined**, [afterRemoval&lt;sup&gt;9+&lt;/sup&gt;](#afterremoval) is called to return the value specified in **createDefault**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V \| undefined |

## getCapacity

```TypeScript
getCapacity(): number
```

Obtains the capacity of this cache.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCreateCount

```TypeScript
getCreateCount(): number
```

Obtains the number of times that an object is created.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMatchCount

```TypeScript
getMatchCount(): number
```

Obtains the number of times that the queried values are matched.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMissCount

```TypeScript
getMissCount(): number
```

Obtains the number of times that the queried values are mismatched.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getPutCount

```TypeScript
getPutCount(): number
```

Obtains the number of additions to this cache.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getRemovalCount

```TypeScript
getRemovalCount(): number
```

Obtains the number of times that key-value pairs in the cache are recycled.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this cache is empty.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(): K[]
```

Obtains all keys in this cache, listed from the least to the most recently accessed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| K[] |

## put

```TypeScript
put(key: K, value: V): V
```

Adds a key-value pair to this cache and returns the value associated with the key. If the total number of values in the cache is greater than the specified capacity, the deletion operation is performed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

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

Removes a key and its associated value from this cache and returns the value associated with the key. If the key does not exist, **undefined** is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V \| undefined |

## toString

```TypeScript
toString(): string
```

Obtains the string representation of this cache.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## updateCapacity

```TypeScript
updateCapacity(newCapacity: number): void
```

Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown. If the total number of values in the cache is greater than the specified capacity, the deletion operation is performed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newCapacity | number | Yes |

## values

```TypeScript
values(): V[]
```

Obtains all values in this cache, listed from the least to the most recently accessed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V[] |

## length

```TypeScript
length: number
```

Total number of values in this cache.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang
