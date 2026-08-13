# HashSet

HashSet is implemented based on HashMap. In HashSet, only the value object is processed.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class HashSet--><!--Device-unnamed-declare class HashSet-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { HashSet } from '@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

returns an iterator.Each item of the iterator is a Javascript Object

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashSet-$_iterator(): IterableIterator<T>--><!--Device-HashSet-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

returns an iterator.Each item of the iterator is a Javascript Object

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-[Symbol.iterator](): IterableIterator<T>--><!--Device-HashSet-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");

// Method 1:
for (let item of hashSet) {
  console.info("value: " + item);
}
// value: squirrel
// value: sparrow

// Method 2:
let iter = hashSet[Symbol.iterator]();
let temp: IteratorResult<string> = iter.next();
while(!temp.done) {
  console.info("value: " + temp.value);
  temp = iter.next();
}
// value: squirrel
// value: sparrow
```

```TypeScript
// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashSet = new HashSet<string>();
for(let i = 0;i < 10;i++) {
  hashSet.add("sparrow" + i);
}
for(let i = 0;i < 10;i++) {
  hashSet.remove("sparrow" + i);
}
```

## add

```TypeScript
add(value: T): boolean
```

Adds elements to this HashSet.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-add(value: T): boolean--><!--Device-HashSet-add(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
let result = hashSet.add("squirrel");
console.info("result:", result);  // result: true
```

## clear

```TypeScript
clear(): void
```

Clears this HashSet and sets its length to **0**.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-clear(): void--><!--Device-HashSet-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
hashSet.clear();
let result = hashSet.isEmpty();
console.info("result:", result);  // result: true
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **HashSet** instance.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-constructor()--><!--Device-HashSet-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## Examples

```TypeScript
let hashSet = new HashSet<number>();
```

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

Returns an iterator that contains all the elements in this HashSet.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-entries(): IterableIterator<[T, T]>--><!--Device-HashSet-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;[T, T]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
let iter = hashSet.entries();
let temp: IteratorResult<[string, string]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value[0]);
  console.info("value:" + temp.value[1]);
  temp = iter.next();
}
// key:squirrel
// value:squirrel
// key:sparrow
// value:sparrow
```

```TypeScript
// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashSet = new HashSet<string>();
for(let i = 0; i < 10; i++) {
  hashSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  hashSet.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse each element.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void--><!--Device-HashSet-forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value?: T, key?: T, set?: HashSet & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("sparrow");
hashSet.add("squirrel");
hashSet.forEach((value: string, key: string): void => {
  console.info("value:" + value, "key:" + key);
});
// value:squirrel key:squirrel
// value:sparrow key:sparrow
```

```TypeScript
// You are not advised to use the add and remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashSet = new HashSet<string>();
for(let i = 0; i < 10; i++) {
  hashSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  hashSet.remove("sparrow" + i);
}
```

## forEach

```TypeScript
forEach(callbackFn: HashSetCbFn<T>): void
```

Iterates over all elements in the HashSet and executes a callback function for each element.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HashSet-forEach(callbackFn: HashSetCbFn<T>): void--><!--Device-HashSet-forEach(callbackFn: HashSetCbFn<T>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [HashSetCbFn](arkts-arkts-hashsetcbfn-t.md)&lt;T&gt; | Yes |

## has

```TypeScript
has(value: T): boolean
```

Checks whether this HashSet has the specified element.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-has(value: T): boolean--><!--Device-HashSet-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
let result = hashSet.has("squirrel");
console.info("result:", result);  // result: true
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this HashSet is empty (contains no element).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-isEmpty(): boolean--><!--Device-HashSet-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
const hashSet = new HashSet<number>();
let result = hashSet.isEmpty();
console.info("result:", result);  // result: true
```

## remove

```TypeScript
remove(value: T): boolean
```

Removes an element from this HashSet.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-remove(value: T): boolean--><!--Device-HashSet-remove(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
let result = hashSet.remove("sparrow");
console.info("result:", result);  // result: true
```

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterator that contains all the values in this HashSet.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-values(): IterableIterator<T>--><!--Device-HashSet-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## Examples

```TypeScript
let hashSet = new HashSet<string>();
hashSet.add("squirrel");
hashSet.add("sparrow");
let values = hashSet.values();
for (let value of values) {
  console.info("value:", value);
}
// value: squirrel
// value: sparrow
```

## length

```TypeScript
length: number
```

Number of elements in a HashSet.

**Type:** number

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HashSet-length: number--><!--Device-HashSet-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
