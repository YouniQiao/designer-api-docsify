# LruBuffer

The LruBuffer algorithm replaces the least used data with new data when the buffer space is insufficient.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache](arkts-arkts-util-lrucache-c.md)

<!--Device-util-class LruBuffer<K, V>--><!--Device-util-class LruBuffer<K, V>-End-->

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

**Substitutes:** ohos.util.LRUCache.[Symbol.iterator]

<!--Device-LruBuffer-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-LruBuffer-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;[K, V]&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro[Symbol.iterator]();
```

## afterRemoval

```TypeScript
afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void
```

Performs subsequent operations after a value is removed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.afterRemoval](arkts-arkts-util-lrucache-c.md#afterremoval)

<!--Device-LruBuffer-afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void--><!--Device-LruBuffer-afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEvict | boolean | Yes |
| key | K | Yes |
| value | V | Yes |
| newValue | V | Yes |

## Examples

```TypeScript
class ChildLruBuffer<K, V> extends util.LruBuffer<K, V> {
  constructor(capacity?: number) {
    super(capacity);
  }

  afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
    if (isEvict === true) {
      console.info('key: ' + key);
      // Output: key: 11
      console.info('value: ' + value);
      // Output: value: 1
      console.info('newValue: ' + newValue);
      // Output: newValue: null
    }
  }
}
let lru: ChildLruBuffer<number, number> = new ChildLruBuffer(2);
lru.put(11, 1);
lru.put(22, 2);
lru.put(33, 3);
```

## clear

```TypeScript
clear(): void
```

Clears key-value pairs from this cache. The **afterRemoval()** API will be called to perform subsequent operations.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.clear](arkts-arkts-util-lrucache-c.md#clear)

<!--Device-LruBuffer-clear(): void--><!--Device-LruBuffer-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.length;
pro.clear();
```

## constructor

```TypeScript
constructor(capacity?: number)
```

A constructor used to create a **LruBuffer** instance. The default capacity of the cache is 64.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.LRUCache.constructor

<!--Device-LruBuffer-constructor(capacity?: number)--><!--Device-LruBuffer-constructor(capacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capacity | number | No |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
```

## contains

```TypeScript
contains(key: K): boolean
```

Checks whether this cache contains the specified key.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.contains](arkts-arkts-util-lrucache-c.md#contains)

<!--Device-LruBuffer-contains(key: K): boolean--><!--Device-LruBuffer-contains(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.contains(20);
console.info('result = ' + result);
// Output: result = false
```

## createDefault

```TypeScript
createDefault(key: K): V
```

Creates a value if the value of the specified key is not available.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.createDefault](arkts-arkts-util-lrucache-c.md#createdefault)

<!--Device-LruBuffer-createDefault(key: K): V--><!--Device-LruBuffer-createDefault(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.createDefault(50);
```

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

Obtains a new iterator object that contains all key-value pairs in this object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.entries](arkts-arkts-util-lrucache-c.md#entries)

<!--Device-LruBuffer-entries(): IterableIterator<[K, V]>--><!--Device-LruBuffer-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;[K, V]&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.entries();
```

## get

```TypeScript
get(key: K): V | undefined
```

Obtains the value of the specified key.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.get](arkts-arkts-util-lrucache-c.md#get)

<!--Device-LruBuffer-get(key: K): V | undefined--><!--Device-LruBuffer-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result  = pro.get(2);
console.info("result = " + result);
// Output: result = 10
```

## getCapacity

```TypeScript
getCapacity(): number
```

Obtains the capacity of this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.getCapacity](arkts-arkts-util-lrucache-c.md#getcapacity)

<!--Device-LruBuffer-getCapacity(): number--><!--Device-LruBuffer-getCapacity(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.getCapacity();
console.info("result = " + result);
// Output: result = 64
```

## getCreateCount

```TypeScript
getCreateCount(): number
```

Obtains the number of return values for **createDefault()**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.getCreateCount](arkts-arkts-util-lrucache-c.md#getcreatecount)

<!--Device-LruBuffer-getCreateCount(): number--><!--Device-LruBuffer-getCreateCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(1,8);
let result = pro.getCreateCount();
console.info("result = " + result);
// Output: result = 0
```

## getMatchCount

```TypeScript
getMatchCount(): number
```

Obtains the number of times that the queried values are matched.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.getMatchCount](arkts-arkts-util-lrucache-c.md#getmatchcount)

<!--Device-LruBuffer-getMatchCount(): number--><!--Device-LruBuffer-getMatchCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
let result = pro.getMatchCount();
console.info("result = " + result);
// Output: result = 1
```

## getMissCount

```TypeScript
getMissCount(): number
```

Obtains the number of times that the queried values are mismatched.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.getMissCount](arkts-arkts-util-lrucache-c.md#getmisscount)

<!--Device-LruBuffer-getMissCount(): number--><!--Device-LruBuffer-getMissCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
let result = pro.getMissCount();
console.info("result = " + result);
// Output: result = 0
```

## getPutCount

```TypeScript
getPutCount(): number
```

Obtains the number of additions to this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.getPutCount](arkts-arkts-util-lrucache-c.md#getputcount)

<!--Device-LruBuffer-getPutCount(): number--><!--Device-LruBuffer-getPutCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.getPutCount();
console.info("result = " + result);
// Output: result = 1
```

## getRemovalCount

```TypeScript
getRemovalCount(): number
```

Obtains the number of removals from this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.getRemovalCount](arkts-arkts-util-lrucache-c.md#getremovalcount)

<!--Device-LruBuffer-getRemovalCount(): number--><!--Device-LruBuffer-getRemovalCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.updateCapacity(2);
pro.put(50,22);
let result = pro.getRemovalCount();
console.info("result = " + result);
// Output: result = 0
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this cache is empty.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.isEmpty](arkts-arkts-util-lrucache-c.md#isempty)

<!--Device-LruBuffer-isEmpty(): boolean--><!--Device-LruBuffer-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.isEmpty();
console.info("result = " + result);
// Output: result = false
```

## keys

```TypeScript
keys(): K[]
```

Obtains all keys in this cache, listed from the most to the least recently accessed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.keys](arkts-arkts-util-lrucache-c.md#keys)

<!--Device-LruBuffer-keys(): K[]--><!--Device-LruBuffer-keys(): K[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| K[] |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.keys();
console.info("result = " + result);
// Output: result = 2
```

## put

```TypeScript
put(key: K, value: V): V
```

Adds a key-value pair to this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.put](arkts-arkts-util-lrucache-c.md#put)

<!--Device-LruBuffer-put(key: K, value: V): V--><!--Device-LruBuffer-put(key: K, value: V): V-End-->

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

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.put(2,10);
console.info("result = " + result);
// Output: result = 10
```

## remove

```TypeScript
remove(key: K): V | undefined
```

Removes the specified key and its value from this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.remove](arkts-arkts-util-lrucache-c.md#remove)

<!--Device-LruBuffer-remove(key: K): V | undefined--><!--Device-LruBuffer-remove(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.remove(20);
console.info("result = " + result);
// Output: result = undefined
```

## toString

```TypeScript
toString(): string
```

Obtains the string representation of this cache.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.toString](arkts-arkts-util-lrucache-c.md#tostring)

<!--Device-LruBuffer-toString(): string--><!--Device-LruBuffer-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
pro.remove(20);
let result = pro.toString();
console.info("result = " + result);
// Output: result = Lrubuffer[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% ]
```

## updateCapacity

```TypeScript
updateCapacity(newCapacity: number): void
```

Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.updateCapacity](arkts-arkts-util-lrucache-c.md#updatecapacity)

<!--Device-LruBuffer-updateCapacity(newCapacity: number): void--><!--Device-LruBuffer-updateCapacity(newCapacity: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newCapacity | number | Yes |

## Examples

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.updateCapacity(100);
```

## values

```TypeScript
values(): V[]
```

Obtains all values in this cache, listed from the most to the least recently accessed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [util.LRUCache.values](arkts-arkts-util-lrucache-c.md#values)

<!--Device-LruBuffer-values(): V[]--><!--Device-LruBuffer-values(): V[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| V[] |

## Examples

```TypeScript
let pro : util.LruBuffer<number|string,number|string> = new util.LruBuffer();
pro.put(2,10);
pro.put(2,"anhu");
pro.put("afaf","grfb");
let result = pro.values();
console.info("result = " + result);
// Output: result = anhu,grfb
```

## length

```TypeScript
length: number
```

Total number of values in this cache.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.util.LRUCache.length

<!--Device-LruBuffer-length: number--><!--Device-LruBuffer-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
