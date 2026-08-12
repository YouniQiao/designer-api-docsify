# Int32Array

A linear data structure that is implemented on [ArkTS ArrayBuffer](./arkts/@arkts.collections:collections).

> **NOTE：**
> 
> - This module can be imported only to ArkTS files (with the file name extension .ets).
> **Decorator**: \@Sendable

**Since:** 12

**Decorator:** @Sendable

<!--Device-collections-class Int32Array--><!--Device-collections-class Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

Returns an iterator that iterates over numbers.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-[Symbol.iterator](): IterableIterator<number>--><!--Device-Int32Array-[Symbol.iterator](): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## at

```TypeScript
at(index: number): number | undefined
```

Returns the element at the given index. If no element is found, **undefined** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-at(index: number): number | undefined--><!--Device-Int32Array-at(index: number): number | undefined-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## constructor

```TypeScript
constructor()
```

A constructor used to create an empty ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-constructor()--><!--Device-Int32Array-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(length: number)
```

A constructor used to create an ArkTS Int32Array of a given length.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-constructor(length: number)--><!--Device-Int32Array-constructor(length: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [length](#length) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(elements: Iterable<number>)
```

A constructor that creates an ArkTS Int32Array from an iterable object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-constructor(elements: Iterable<number>)--><!--Device-Int32Array-constructor(elements: Iterable<number>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Iterable & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(array: ArrayLike<number> | ArrayBuffer)
```

A constructor that creates an ArkTS Int32Array from an array-like object or ArkTS ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-constructor(array: ArrayLike<number> | ArrayBuffer)--><!--Device-Int32Array-constructor(array: ArrayLike<number> | ArrayBuffer)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;number&gt; \| ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)
```

A constructor that creates an ArkTS Int32Array from an ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)--><!--Device-Int32Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)-End-->

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
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Int32Array
```

Copies elements within a given range from this ArkTS Int32Array to another position in sequence.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-copyWithin(target: number, start: number, end?: number): Int32Array--><!--Device-Int32Array-copyWithin(target: number, start: number, end?: number): Int32Array-End-->

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
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

Returns an iterator object that contains the key-value pair of each element in this ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-entries(): IterableIterator<[number, number]>--><!--Device-Int32Array-entries(): IterableIterator<[number, number]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[number, number]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## every

```TypeScript
every(predicate: TypedArrayPredicateFn<number, Int32Array>): boolean
```

Checks whether all elements in this ArkTS Int32Array meet a given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-every(predicate: TypedArrayPredicateFn<number, Int32Array>): boolean--><!--Device-Int32Array-every(predicate: TypedArrayPredicateFn<number, Int32Array>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): Int32Array
```

Fills all elements in a given range in this ArkTS Int32Array with a value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-fill(value: number, start?: number, end?: number): Int32Array--><!--Device-Int32Array-fill(value: number, start?: number, end?: number): Int32Array-End-->

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
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## filter

```TypeScript
filter(predicate: TypedArrayPredicateFn<number, Int32Array>): Int32Array
```

Returns a new ArkTS Int32Array that contains all elements that meet the given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-filter(predicate: TypedArrayPredicateFn<number, Int32Array>): Int32Array--><!--Device-Int32Array-filter(predicate: TypedArrayPredicateFn<number, Int32Array>): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## find

```TypeScript
find(predicate: TypedArrayPredicateFn<number, Int32Array>): number | undefined
```

Returns the value of the first element that passes a test provided by a callback function. If none of the elements pass the test, **undefined** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-find(predicate: TypedArrayPredicateFn<number, Int32Array>): number | undefined--><!--Device-Int32Array-find(predicate: TypedArrayPredicateFn<number, Int32Array>): number | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## findIndex

```TypeScript
findIndex(predicate: TypedArrayPredicateFn<number, Int32Array>): number
```

Returns the index of the first element that passes a test provided by a callback function. If none of the elements pass the test, **-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-findIndex(predicate: TypedArrayPredicateFn<number, Int32Array>): number--><!--Device-Int32Array-findIndex(predicate: TypedArrayPredicateFn<number, Int32Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## forEach

```TypeScript
forEach(callbackFn: TypedArrayForEachCallback<number, Int32Array>): void
```

Calls a callback function for each element in this ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-forEach(callbackFn: TypedArrayForEachCallback<number, Int32Array>): void--><!--Device-Int32Array-forEach(callbackFn: TypedArrayForEachCallback<number, Int32Array>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md)&lt;number, Int32Array&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## from

```TypeScript
static from(arrayLike: ArrayLike<number>): Int32Array
```

Creates an ArkTS Int32Array from an array-like or iterator object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-static from(arrayLike: ArrayLike<number>): Int32Array--><!--Device-Int32Array-static from(arrayLike: ArrayLike<number>): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Int32Array
```

Creates an ArkTS Int32Array from an array-like object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Int32Array--><!--Device-Int32Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;T, number&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

## from

```TypeScript
static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Int32Array
```

Creates an ArkTS Int32Array from an iterator object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Int32Array--><!--Device-Int32Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | Iterable & lt;number & gt; | Yes |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;number, number&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

## includes

```TypeScript
includes(searchElement: number, fromIndex?: number): boolean
```

Checks whether elements are contained in this ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-includes(searchElement: number, fromIndex?: number): boolean--><!--Device-Int32Array-includes(searchElement: number, fromIndex?: number): boolean-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in this ArkTS Int32Array. If the value is not found,  
**-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Int32Array-indexOf(searchElement: number, fromIndex?: number): number-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## join

```TypeScript
join(separator?: string): string
```

Concatenates all elements in this ArkTS Int32Array into a string, with a given separator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-join(separator?: string): string--><!--Device-Int32Array-join(separator?: string): string-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## keys

```TypeScript
keys(): IterableIterator<number>
```

Returns an iterator object that contains the key (index) of each element in this ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-keys(): IterableIterator<number>--><!--Device-Int32Array-keys(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

Obtains the index of the last occurrence of the specified value in this ArkTS Int32Array.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Int32Array-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Int32Array-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## map

```TypeScript
map(callbackFn: TypedArrayMapCallback<number, Int32Array>): Int32Array
```

Applies a callback function to each element in this ArkTS Int32Array and uses the result to create an ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-map(callbackFn: TypedArrayMapCallback<number, Int32Array>): Int32Array--><!--Device-Int32Array-map(callbackFn: TypedArrayMapCallback<number, Int32Array>): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md)&lt;number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## of

```TypeScript
static of(...items: number[]): Int32Array
```

Creates an ArkTS Int32Array with a variable number of parameters.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Int32Array-static of(...items: number[]): Int32Array--><!--Device-Int32Array-static of(...items: number[]): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | number[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number
```

Applies a reduce function on each element in this ArkTS Int32Array and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number--><!--Device-Int32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>, initialValue: number): number
```

Applies a reduce function for each element in this ArkTS Int32Array, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>, initialValue: number): number--><!--Device-Int32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>, initialValue: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Int32Array&gt; | Yes |
| initialValue | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reduce

```TypeScript
reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U
```

Applies a reduce function for each element in this ArkTS Int32Array, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U--><!--Device-Int32Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Int32Array&gt; | Yes |
| initialValue | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| U |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reduceRight

```TypeScript
reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U
```

Reversely traverses this ArkTS Int32Array, applies a reduce function for each element in the array, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Int32Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U--><!--Device-Int32Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Int32Array&gt; | Yes |
| initialValue | U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| U |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reduceRight

```TypeScript
reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number
```

Reversely traverses this ArkTS Int32Array, applies a reduce function on each element in the array, and returns the final reduction result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Int32Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number--><!--Device-Int32Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reverse

```TypeScript
reverse(): Int32Array
```

Reverses this ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-reverse(): Int32Array--><!--Device-Int32Array-reverse(): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

Writes the elements in an array-like object to the given start position in sequence.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Int32Array-set(array: ArrayLike<number>, offset?: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |
| offset | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## slice

```TypeScript
slice(start?: number, end?: number): Int32Array
```

Selects a range of elements in this ArkTS Int32Array to create an ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-slice(start?: number, end?: number): Int32Array--><!--Device-Int32Array-slice(start?: number, end?: number): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## some

```TypeScript
some(predicate: TypedArrayPredicateFn<number, Int32Array>): boolean
```

Checks whether any element in this ArkTS Int32Array meets a given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-some(predicate: TypedArrayPredicateFn<number, Int32Array>): boolean--><!--Device-Int32Array-some(predicate: TypedArrayPredicateFn<number, Int32Array>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Int32Array&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## sort

```TypeScript
sort(compareFn?: TypedArrayCompareFn<number>): Int32Array
```

Sorts elements in this ArkTS Int32Array and returns the sorted ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-sort(compareFn?: TypedArrayCompareFn<number>): Int32Array--><!--Device-Int32Array-sort(compareFn?: TypedArrayCompareFn<number>): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md)&lt;number&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Int32Array
```

Truncates an array from a specified position and returns a new ArkTS Int32Array based on the same ArkTS ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-subarray(begin?: number, end?: number): Int32Array--><!--Device-Int32Array-subarray(begin?: number, end?: number): Int32Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Int32Array |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Generates a string of digits that matches the cultural conventions of the current system locale. Each element converts its digits to a string via its **toLocaleString** API, and these strings are then joined in sequence with commas (,).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Int32Array-toLocaleString(): string--><!--Device-Int32Array-toLocaleString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## toString

```TypeScript
toString(): string
```

Converts an ArkTS Int32Array into a string.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Int32Array-toString(): string--><!--Device-Int32Array-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## values

```TypeScript
values(): IterableIterator<number>
```

Returns an iterator object that contains the value of each element in this ArkTS Int32Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-values(): IterableIterator<number>--><!--Device-Int32Array-values(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## BYTES_PER_ELEMENT

```TypeScript
static readonly BYTES_PER_ELEMENT: number
```

Number of bytes occupied by each element in the ArkTS Int32Array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-static readonly BYTES_PER_ELEMENT: number--><!--Device-Int32Array-static readonly BYTES_PER_ELEMENT: number-End-->

**System capability:** SystemCapability.Utils.Lang

## [index: number]

```TypeScript
[index: number]: number
```

Returns the item at that index.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-[index: number]: number--><!--Device-Int32Array-[index: number]: number-End-->

**System capability:** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

Bottom-layer buffer used by an ArkTS Int32Array.

**Type:** ArrayBuffer

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-readonly buffer: ArrayBuffer--><!--Device-Int32Array-readonly buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: number
```

Number of bytes occupied by an ArkTS Int32Array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-readonly byteLength: number--><!--Device-Int32Array-readonly byteLength: number-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: number
```

Offset between the ArkTS Int32Array and the start position of the ArrayBuffer.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-readonly byteOffset: number--><!--Device-Int32Array-readonly byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

Number of elements in an ArkTS Int32Array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Int32Array-readonly length: number--><!--Device-Int32Array-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
