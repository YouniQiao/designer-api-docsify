# LruBuffer

The LruBuffer algorithm replaces the least used data with new data when the buffer space is insufficient.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [LRUCache](arkts-arkts-util-lrucache-c.md)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** iterator]

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

## afterRemoval

```TypeScript
afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void
```

Performs subsequent operations after a value is removed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [afterRemoval](arkts-arkts-util-lrucache-c.md#afterremoval)

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

Clears key-value pairs from this cache. The **afterRemoval()** API will be called to perform subsequent operations.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [clear](arkts-arkts-util-lrucache-c.md#clear)

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(capacity?: number)
```

A constructor used to create a **LruBuffer** instance. The default capacity of the cache is 64.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** constructor

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [contains](arkts-arkts-util-lrucache-c.md#contains)

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

Creates a value if the value of the specified key is not available.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createDefault](arkts-arkts-util-lrucache-c.md#createdefault)

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

Obtains a new iterator object that contains all key-value pairs in this object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [entries](arkts-arkts-util-lrucache-c.md#entries)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[K, V]&gt; |

## get

```TypeScript
get(key: K): V | undefined
```

Obtains the value of the specified key.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [get](arkts-arkts-util-lrucache-c.md#get)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getCapacity](arkts-arkts-util-lrucache-c.md#getcapacity)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCreateCount

```TypeScript
getCreateCount(): number
```

Obtains the number of return values for **createDefault()**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getCreateCount](arkts-arkts-util-lrucache-c.md#getcreatecount)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getMatchCount](arkts-arkts-util-lrucache-c.md#getmatchcount)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getMissCount](arkts-arkts-util-lrucache-c.md#getmisscount)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getPutCount](arkts-arkts-util-lrucache-c.md#getputcount)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getRemovalCount

```TypeScript
getRemovalCount(): number
```

Obtains the number of removals from this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRemovalCount](arkts-arkts-util-lrucache-c.md#getremovalcount)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isEmpty](arkts-arkts-util-lrucache-c.md#isempty)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(): K[]
```

Obtains all keys in this cache, listed from the most to the least recently accessed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [keys](arkts-arkts-util-lrucache-c.md#keys)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| K[] |

## put

```TypeScript
put(key: K, value: V): V
```

Adds a key-value pair to this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [put](arkts-arkts-util-lrucache-c.md#put)

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

Removes the specified key and its value from this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [remove](arkts-arkts-util-lrucache-c.md#remove)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [toString](arkts-arkts-util-lrucache-c.md#tostring)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## updateCapacity

```TypeScript
updateCapacity(newCapacity: number): void
```

Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [updateCapacity](arkts-arkts-util-lrucache-c.md#updatecapacity)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newCapacity | number | Yes |

## values

```TypeScript
values(): V[]
```

Obtains all values in this cache, listed from the most to the least recently accessed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [values](arkts-arkts-util-lrucache-c.md#values)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** length

**System capability:** SystemCapability.Utils.Lang
