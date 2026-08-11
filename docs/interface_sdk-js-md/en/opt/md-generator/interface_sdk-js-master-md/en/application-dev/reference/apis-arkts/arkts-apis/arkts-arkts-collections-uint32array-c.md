# Uint32Array

A linear data structure that is implemented on [ArkTS ArrayBuffer](arkts-collections.md).

> **NOTE：**
> 
> - This module can be imported only to ArkTS files (with the file name extension .ets).
> **Decorator**: \@Sendable

**Since:** 12

**Decorator:** @Sendable

<!--Device-collections-class Uint32Array--><!--Device-collections-class Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

Returns an iterator that iterates over numbers.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-[Symbol.iterator](): IterableIterator<number>--><!--Device-Uint32Array-[Symbol.iterator](): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;number&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## at

```TypeScript
at(index: number): number | undefined
```

Returns the element at the given index. If no element is found, **undefined** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-at(index: number): number | undefined--><!--Device-Uint32Array-at(index: number): number | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## constructor

```TypeScript
constructor()
```

A constructor used to create an empty ArkTS Uint32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-constructor()--><!--Device-Uint32Array-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(length: number)
```

A constructor used to create an ArkTS Uint32Array of a given length.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-constructor(length: number)--><!--Device-Uint32Array-constructor(length: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [length](#length) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(elements: Iterable<number>)
```

A constructor that creates an ArkTS Uint32Array from an iterable object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-constructor(elements: Iterable<number>)--><!--Device-Uint32Array-constructor(elements: Iterable<number>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elements | Iterable&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(array: ArrayLike<number> | ArrayBuffer)
```

A constructor that creates an ArkTS Uint32Array from an array-like object or ArkTS ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-constructor(array: ArrayLike<number> | ArrayBuffer)--><!--Device-Uint32Array-constructor(array: ArrayLike<number> | ArrayBuffer)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike&lt;number&gt; \](arkts-arkts-arraylike-i.md) | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)
```

A constructor that creates an ArkTS Uint32Array from an ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)--><!--Device-Uint32Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [buffer](#buffer) | ArrayBuffer | Yes |
| [byteOffset](#byteoffset) | number | No |
| [length](#length) | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Uint32Array
```

Copies elements within a given range from this ArkTS Uint32Array to another position in sequence.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-copyWithin(target: number, start: number, end?: number): Uint32Array--><!--Device-Uint32Array-copyWithin(target: number, start: number, end?: number): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | number | Yes |
| start | number | Yes |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

Returns an iterator object that contains the key-value pair of each element in this ArkTS Float32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-entries(): IterableIterator<[number, number]>--><!--Device-Uint32Array-entries(): IterableIterator<[number, number]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;[number, number]&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## every

```TypeScript
every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean
```

Checks whether all elements in this ArkTS Uint32Array meet a given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean--><!--Device-Uint32Array-every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): Uint32Array
```

Fills all elements in a given range in this ArkTS Uint32Array with a value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-fill(value: number, start?: number, end?: number): Uint32Array--><!--Device-Uint32Array-fill(value: number, start?: number, end?: number): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## filter

```TypeScript
filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array
```

Returns a new ArkTS Uint32Array that contains all elements that meet the given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array--><!--Device-Uint32Array-filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## find

```TypeScript
find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined
```

Returns the value of the first element that passes a test provided by a callback function. If none of the elements pass the test, **undefined** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined--><!--Device-Uint32Array-find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## findIndex

```TypeScript
findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number
```

Returns the index of the first element that passes a test provided by a callback function. If none of the elements pass the test, **-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number--><!--Device-Uint32Array-findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## forEach

```TypeScript
forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void
```

Calls a callback function for each element in this ArkTS Uint32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void--><!--Device-Uint32Array-forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md)&lt;number, Uint32Array&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## from

```TypeScript
static from(arrayLike: ArrayLike<number>): Uint32Array
```

Creates an ArkTS Uint32Array from an array-like or iterator object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-static from(arrayLike: ArrayLike<number>): Uint32Array--><!--Device-Uint32Array-static from(arrayLike: ArrayLike<number>): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;number&gt;](arkts-arkts-arraylike-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array
```

Creates an ArkTS Uint32Array from an array-like object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array--><!--Device-Uint32Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;T&gt;](arkts-arkts-arraylike-i.md) | Yes |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;T, number&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

## from

```TypeScript
static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array
```

Creates an ArkTS Uint32Array from an iterator object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array--><!--Device-Uint32Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | Iterable&lt;number&gt; | Yes |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;number, number&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

## includes

```TypeScript
includes(searchElement: number, fromIndex?: number): boolean
```

Checks whether elements are contained in this ArkTS Float32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-includes(searchElement: number, fromIndex?: number): boolean--><!--Device-Uint32Array-includes(searchElement: number, fromIndex?: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | number | Yes |
| fromIndex | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in this ArkTS Float32Array. If the value is not found,  
**-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint32Array-indexOf(searchElement: number, fromIndex?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | number | Yes |
| fromIndex | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## join

```TypeScript
join(separator?: string): string
```

Concatenates all elements in this ArkTS Float32Array into a string, with a given separator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-join(separator?: string): string--><!--Device-Uint32Array-join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| separator | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## keys

```TypeScript
keys(): IterableIterator<number>
```

Returns an iterator object that contains the key (index) of each element in this ArkTS Float32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-keys(): IterableIterator<number>--><!--Device-Uint32Array-keys(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;number&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

Obtains the index of the last occurrence of the specified value in this ArkTS Uint32Array.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint32Array-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint32Array-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | number | Yes |
| fromIndex | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## map

```TypeScript
map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array
```

Applies a callback function to each element in this ArkTS Uint32Array and uses the result to create an ArkTS Uint32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array--><!--Device-Uint32Array-map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md)&lt;number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## of

```TypeScript
static of(...items: number[]): Uint32Array
```

Creates an ArkTS Uint32Array with a variable number of parameters.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint32Array-static of(...items: number[]): Uint32Array--><!--Device-Uint32Array-static of(...items: number[]): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | number[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number
```

Applies a reduce function on each element in this ArkTS Uint32Array and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number--><!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number
```

Applies a reduce function for each element in this ArkTS Uint32Array, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number--><!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint32Array&gt; | Yes |
| initialValue | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## reduce

```TypeScript
reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U
```

Applies a reduce function for each element in this ArkTS Uint32Array, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U--><!--Device-Uint32Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint32Array&gt; | Yes |
| initialValue | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| U |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## reduceRight

```TypeScript
reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U
```

Reversely traverses this ArkTS Uint32Array, applies a reduce function for each element in the array, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint32Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U--><!--Device-Uint32Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint32Array&gt; | Yes |
| initialValue | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| U |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## reduceRight

```TypeScript
reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number
```

Reversely traverses this ArkTS Uint32Array, applies a reduce function on each element in the array, and returns the final reduction result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint32Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number--><!--Device-Uint32Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## reverse

```TypeScript
reverse(): Uint32Array
```

Reverses this ArkTS Uint32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-reverse(): Uint32Array--><!--Device-Uint32Array-reverse(): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

Writes the elements in an array-like object to the given start position in sequence.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint32Array-set(array: ArrayLike<number>, offset?: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike&lt;number&gt;](arkts-arkts-arraylike-i.md) | Yes |
| offset | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## slice

```TypeScript
slice(start?: number, end?: number): Uint32Array
```

Selects a range of elements in this ArkTS Uint32Array to create an ArkTS Uint32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-slice(start?: number, end?: number): Uint32Array--><!--Device-Uint32Array-slice(start?: number, end?: number): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## some

```TypeScript
some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean
```

Checks whether any element in this ArkTS Uint32Array meets a given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean--><!--Device-Uint32Array-some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## sort

```TypeScript
sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array
```

Sorts elements in this ArkTS Uint32Array and returns the sorted ArkTS Uint32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array--><!--Device-Uint32Array-sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md)&lt;number&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint32Array
```

Truncates an array from a specified position and returns a new ArkTS Uint32Array based on the same ArkTS ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-subarray(begin?: number, end?: number): Uint32Array--><!--Device-Uint32Array-subarray(begin?: number, end?: number): Uint32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Generates a string of digits that matches the cultural conventions of the current system locale. Each element converts its digits to a string via its **toLocaleString** API, and these strings are then joined in sequence with commas (,).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint32Array-toLocaleString(): string--><!--Device-Uint32Array-toLocaleString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## toString

```TypeScript
toString(): string
```

Converts an ArkTS Uint32Array into a string.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint32Array-toString(): string--><!--Device-Uint32Array-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## values

```TypeScript
values(): IterableIterator<number>
```

Returns an iterator object that contains the value of each element in this ArkTS Float32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-values(): IterableIterator<number>--><!--Device-Uint32Array-values(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;number&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## BYTES_PER_ELEMENT

```TypeScript
static readonly BYTES_PER_ELEMENT: number
```

Number of bytes occupied by each element in the ArkTS Float32Array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-static readonly BYTES_PER_ELEMENT: number--><!--Device-Uint32Array-static readonly BYTES_PER_ELEMENT: number-End-->

**System capability:** SystemCapability.Utils.Lang

## [index: number]

```TypeScript
[index: number]: number
```

Returns the item at that index.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-[index: number]: number--><!--Device-Uint32Array-[index: number]: number-End-->

**System capability:** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

Bottom-layer buffer used by an ArkTS Float32Array.

**Type:** ArrayBuffer

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-readonly buffer: ArrayBuffer--><!--Device-Uint32Array-readonly buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: number
```

Number of bytes occupied by an ArkTS Float32Array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-readonly byteLength: number--><!--Device-Uint32Array-readonly byteLength: number-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: number
```

Offset between the ArkTS Float32Array and the start position of the ArrayBuffer.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-readonly byteOffset: number--><!--Device-Uint32Array-readonly byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

Number of elements in an ArkTS Float32Array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint32Array-readonly length: number--><!--Device-Uint32Array-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
