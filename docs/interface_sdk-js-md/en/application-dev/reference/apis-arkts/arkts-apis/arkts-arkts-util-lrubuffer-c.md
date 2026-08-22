# LruBuffer

The LruBuffer algorithm replaces the least used data with new data when the buffer space is insufficient.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [LRUCache](../../apis-default/arkts-apis/arkts-util-lrucache-c.md)

<!--Device-util-class LruBuffer--><!--Device-util-class LruBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArrayList } from '@kit.ArkTS';
import { ArrayListComparatorFn } from '@kit.ArkTS';
import { ArrayListForEachCb } from '@kit.ArkTS';
import { ArrayListReplaceCb } from '@kit.ArkTS';
import { util } from '@kit.ArkTS';
import { Deque } from '@kit.ArkTS';
import { DequeForEachCb } from '@kit.ArkTS';
import { HashMap } from '@kit.ArkTS';
import { HashMapCbFn } from '@kit.ArkTS';
import { HashSet } from '@kit.ArkTS';
import { HashSetCbFn } from '@kit.ArkTS';
import { LightWeightMap } from '@kit.ArkTS';
import { LightWeightMapCbFn } from '@kit.ArkTS';
import { LightWeightSet } from '@kit.ArkTS';
import { LightWeightSetForEachCb } from '@kit.ArkTS';
import { LinkedList } from '@kit.ArkTS';
import { LinkedListForEachCb } from '@kit.ArkTS';
import { List } from '@kit.ArkTS';
import { ListComparatorFn } from '@kit.ArkTS';
import { ListForEachCb } from '@kit.ArkTS';
import { ListReplaceCb } from '@kit.ArkTS';
import { PlainArray } from '@kit.ArkTS';
import { PlainArrayForEachCb } from '@kit.ArkTS';
import { Queue } from '@kit.ArkTS';
import { QueueForEachCb } from '@kit.ArkTS';
import { Stack } from '@kit.ArkTS';
import { StackForEachCb } from '@kit.ArkTS';
import { TreeMap } from '@kit.ArkTS';
import { TreeMapForEachCb } from '@kit.ArkTS';
import { TreeMapComparator } from '@kit.ArkTS';
import { TreeSet } from '@kit.ArkTS';
import { TreeSetForEachCb } from '@kit.ArkTS';
import { TreeSetComparator } from '@kit.ArkTS';
import { stream } from '@kit.ArkTS';
import { Vector } from '@kit.ArkTS';
import { JSON } from '@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

Specifies the default iterator for an object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** iterator]

<!--Device-LruBuffer-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-LruBuffer-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[K, V]&gt; | Returns a two - dimensional array in the form of key - value pairs. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(3, 15);

for (let value of pro) {
  console.info(value[0]+ ', '+ value[1]);
}
// Output:
// 2, 10
// 3, 15
```

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

**Substitutes:** [afterRemoval](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#afterremoval)

<!--Device-LruBuffer-afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void--><!--Device-LruBuffer-afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEvict | boolean | Yes | Whether the capacity is insufficient. If the value is **true**, this API is called due to insufficient capacity. |
| key | K | Yes | Key removed. |
| value | V | Yes | Value removed. |
| newValue | V | Yes | New value for the key if the **put()** method is called and the key to be added already exists. In other cases, this parameter is left blank. |

**Examples**

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

**Substitutes:** [clear](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#clear)

<!--Device-LruBuffer-clear(): void--><!--Device-LruBuffer-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.length;
pro.clear();
let res = pro.length;
console.info('result = ' + result);
console.info('res = ' + res);
// Output: result = 1
// Output: res = 0
```

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

**Substitutes:** constructor

<!--Device-LruBuffer-constructor(capacity?: number)--><!--Device-LruBuffer-constructor(capacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capacity | number | No | Capacity of the cache to create. The default value is **64**. |

**Examples**

```TypeScript
let textDecoder = new util.TextDecoder();
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// Output: retStr = utf-8
```

```TypeScript
let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
```

```TypeScript
let textEncoder = new util.TextEncoder();
```

```TypeScript
let textEncoder = new util.TextEncoder("utf-8");
```

```TypeScript
let rationalNumber = new util.RationalNumber();
```

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
```

```TypeScript
let pro = new util.LRUCache<number, number>();
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}
let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = [30, 40]
```

```TypeScript
let base64 = new util.Base64Helper();
```

```TypeScript
let decoder = new util.StringDecoder();
```

```TypeScript
let type = new util.types();
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = [30, 40]
```

```TypeScript
let base64 = new  util.Base64();
```

## contains

```TypeScript
contains(key: K): boolean
```

Checks whether this cache contains the specified key.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [contains](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#contains)

<!--Device-LruBuffer-contains(key: K): boolean--><!--Device-LruBuffer-contains(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | Key to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** is returned if the cache contains the specified key; otherwise, **false** is returned. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.contains(2);
console.info('result = ' + result);
// Output: result = true
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// Output: result = true
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.ScopeHelper(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// Output: result = false
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.contains(20);
console.info('result = ' + result);
// Output: result = false
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// Output: result = true
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.Scope(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// Output: result = false
```

## createDefault

```TypeScript
createDefault(key: K): V
```

Creates a value if the value of the specified key is not available.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createDefault](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#createdefault)

<!--Device-LruBuffer-createDefault(key: K): V--><!--Device-LruBuffer-createDefault(key: K): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | Key of which the value is missing. |

**Return value:**

| Type | Description |
| --- | --- |
| V | Value of the key. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
let result = pro.createDefault(50);
console.info('result = ' + result);
// Output: result = undefined
```

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

**Substitutes:** [entries](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#entries)

<!--Device-LruBuffer-entries(): IterableIterator<[K, V]>--><!--Device-LruBuffer-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[K, V]&gt; | Iterable array. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(3, 15);
let pair = pro.entries();
for (let value of pair) {
  console.info(value[0]+ ', '+ value[1]);
}
// Output:
// 2, 10
// 3, 15
```

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

**Substitutes:** [get](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#get)

<!--Device-LruBuffer-get(key: K): V | undefined--><!--Device-LruBuffer-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | Key based on which the value is queried. |

**Return value:**

| Type | Description |
| --- | --- |
| V \| undefined | Value of the key. If no match is found, **undefined** is returned. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result  = pro.get(2);
console.info('result = ' + result);
// Output: result = 10
```

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

**Substitutes:** [getCapacity](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#getcapacity)

<!--Device-LruBuffer-getCapacity(): number--><!--Device-LruBuffer-getCapacity(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Capacity of the cache. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
let result = pro.getCapacity();
console.info('result = ' + result);
// Output: result = 64
```

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

**Substitutes:** [getCreateCount](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#getcreatecount)

<!--Device-LruBuffer-getCreateCount(): number--><!--Device-LruBuffer-getCreateCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of return values for **createDefault()**. |

**Examples**

```TypeScript
// Create the ChildLRUCache class that inherits LRUCache, and override createDefault() to return a non-undefined value.
class ChildLRUCache extends util.LRUCache<number, number> {
  constructor() {
    super();
  }

  createDefault(key: number): number {
    return key;
  }
}
let lru = new ChildLRUCache();
lru.put(2, 10);
lru.get(3);
lru.get(5);
let res = lru.getCreateCount();
console.info('res = ' + res);
// Output: res = 2
```

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

**Substitutes:** [getMatchCount](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#getmatchcount)

<!--Device-LruBuffer-getMatchCount(): number--><!--Device-LruBuffer-getMatchCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of times that the queried values are matched. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
let result = pro.getMatchCount();
console.info('result = ' + result);
// Output: result = 1
```

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

**Substitutes:** [getMissCount](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#getmisscount)

<!--Device-LruBuffer-getMissCount(): number--><!--Device-LruBuffer-getMissCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of times that the queried values are mismatched. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
let result = pro.getMissCount();
console.info('result = ' + result);
// Output: result = 0
```

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

**Substitutes:** [getPutCount](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#getputcount)

<!--Device-LruBuffer-getPutCount(): number--><!--Device-LruBuffer-getPutCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of additions to the cache. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.getPutCount();
console.info('result = ' + result);
// Output: result = 1
```

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

**Substitutes:** [getRemovalCount](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#getremovalcount)

<!--Device-LruBuffer-getRemovalCount(): number--><!--Device-LruBuffer-getRemovalCount(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of removals from the cache. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.updateCapacity(2);
pro.put(50, 22);
let result = pro.getRemovalCount();
console.info('result = ' + result);
// Output: result = 0
```

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

**Substitutes:** [isEmpty](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#isempty)

<!--Device-LruBuffer-isEmpty(): boolean--><!--Device-LruBuffer-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the cache does not contain any value. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.isEmpty();
console.info('result = ' + result);
// Output: result = false
```

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

**Substitutes:** [keys](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#keys)

<!--Device-LruBuffer-keys(): K[]--><!--Device-LruBuffer-keys(): K[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| K[] | All keys in the cache, listed from the most to the least recently accessed. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, string>();
pro.put(1, 'A');
pro.put(2, "B");
pro.put(3, 'C');
pro.put(4, 'D')
pro.put(5, 'E')
pro.put(6, 'F')
let result = pro.keys();
console.info('result = ' + result);
// Output: result = 1,2,3,4,5,6
pro.get(5);
pro.get(3);
result = pro.keys();
console.info('result = ' + result);
// Output: result = 1,2,4,6,5,3
```

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

**Substitutes:** [put](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#put)

<!--Device-LruBuffer-put(key: K, value: V): V--><!--Device-LruBuffer-put(key: K, value: V): V-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | Key of the key-value pair to add. |
| value | V | Yes | Value of the key-value pair to add. |

**Return value:**

| Type | Description |
| --- | --- |
| V | Value added. If the key already exists, the existing value is returned; if **null** is passed in for **key** or **value**, an error is thrown. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
let result = pro.put(2, 10);
console.info('result = ' + result);
// Output: result = 10
```

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

**Substitutes:** [remove](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#remove)

<!--Device-LruBuffer-remove(key: K): V | undefined--><!--Device-LruBuffer-remove(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | Key to remove. |

**Return value:**

| Type | Description |
| --- | --- |
| V \| undefined | Optional** object containing the removed key-value pair. If the key does not exist, an empty **Optional** object is returned; if **null** is passed in for **key**, an error is thrown. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.remove(20);
console.info('result = ' + result);
// Output: result = undefined
```

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

**Substitutes:** [toString](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#tostring)

<!--Device-LruBuffer-toString(): string--><!--Device-LruBuffer-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | String representation of this cache. |

**Examples**

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// Output: result = 1/2
```

You are advised to use the following code snippet for API version 9 and later versions:

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// Output: result = 1/2
```

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
pro.get(3);
console.info(pro.toString());
// Output: LRUCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
// maxSize: maximum size of the cache. hits: number of matched queries. misses: number of mismatched queries. hitRate: matching rate.
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// Output: result = [30, 40]
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
pro.remove(20);
let result = pro.toString();
console.info("result = " + result);
// Output: result = Lrubuffer[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% ]
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// Output: result = [30, 40]
```

## updateCapacity

```TypeScript
updateCapacity(newCapacity: number): void
```

Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [updateCapacity](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#updatecapacity)

<!--Device-LruBuffer-updateCapacity(newCapacity: number): void--><!--Device-LruBuffer-updateCapacity(newCapacity: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newCapacity | number | Yes | New capacity of the cache. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, number>();
pro.updateCapacity(100);
```

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

**Substitutes:** [values](../../apis-default/arkts-apis/arkts-util-lrucache-c.md#values)

<!--Device-LruBuffer-values(): V[]--><!--Device-LruBuffer-values(): V[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| V[] | All values in the cache, listed from the most to the least recently accessed. |

**Examples**

```TypeScript
let pro = new util.LRUCache<number, string>();
pro.put(1, 'A');
pro.put(2, "B");
pro.put(3, 'C');
pro.put(4, 'D')
pro.put(5, 'E')
pro.put(6, 'F')
let result = pro.values();
console.info('result = ' + result);
// Output: result = A,B,C,D,E,F
pro.get(1);
pro.get(2);
result = pro.values();
console.info('result = ' + result);
// Output: result = C,D,E,F,A,B
```

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

**Substitutes:** length

<!--Device-LruBuffer-length: number--><!--Device-LruBuffer-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

