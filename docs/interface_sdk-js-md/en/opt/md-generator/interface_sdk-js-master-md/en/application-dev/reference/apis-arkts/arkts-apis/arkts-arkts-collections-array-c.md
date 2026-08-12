# Array

A linear data structure that is implemented on arrays and can be passed between ArkTS concurrent instances.Pass-by-reference is recommended for better transfer performance.

> **NOTE：**
> 
> - This module can be imported only to ArkTS files (with the file name extension .ets).
> This section uses the following to identify the use of generics:

- T: type, which can be any of the  
[sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types).  
**Decorator**: \@Sendable

**Inheritance/Implementation:** Array implements [ConcatArray<T>](ConcatArray<T>)

**Since:** 12

**Decorator:** @Sendable

<!--Device-collections-class Array<T> implements ConcatArray<T>--><!--Device-collections-class Array<T> implements ConcatArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

Obtains an iterator, each item of which is a JavaScript object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-[Symbol.iterator](): IterableIterator<T>--><!--Device-Array-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## at

```TypeScript
at(index: number): T | undefined
```

Returns the element at a given index in this ArkTS array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-at(index: number): T | undefined--><!--Device-Array-at(index: number): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## concat

```TypeScript
concat(...items: ConcatArray<T>[]): Array<T>
```

Concatenates this ArkTS array with one or more arrays.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-concat(...items: ConcatArray<T>[]): Array<T>--><!--Device-Array-concat(...items: ConcatArray<T>[]): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | ConcatArray & lt;T & gt;[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## constructor

```TypeScript
constructor()
```

A constructor used to create an empty ArkTS array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-constructor()--><!--Device-Array-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(first: T, ...left: T[])
```

A constructor used to create an ArkTS array with the given elements.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-constructor(first: T, ...left: T[])--><!--Device-Array-constructor(first: T, ...left: T[])-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| first | T | Yes |
| left | T[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(...items: T[])
```

A constructor used to create an ArkTS array with the given elements.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-constructor(...items: T[])--><!--Device-Array-constructor(...items: T[])-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | T[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Array<T>
```

Copies elements within a given range from this ArkTS array to another position in sequence.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-copyWithin(target: number, start: number, end?: number): Array<T>--><!--Device-Array-copyWithin(target: number, start: number, end?: number): Array<T>-End-->

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
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## create

```TypeScript
static create<T>(arrayLength: number, initialValue: T): Array<T>
```

Creates an ArkTS array of a fixed length, with each element set to a given initial value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-static create<T>(arrayLength: number, initialValue: T): Array<T>--><!--Device-Array-static create<T>(arrayLength: number, initialValue: T): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLength | number | Yes |
| initialValue | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## entries

```TypeScript
entries(): IterableIterator<[number, T]>
```

Returns an iterator object that contains the key-value pair of each element in this ArkTS array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-entries(): IterableIterator<[number, T]>--><!--Device-Array-entries(): IterableIterator<[number, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[number, T]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## every

```TypeScript
every(predicate: ArrayPredicateFn<T, Array<T>>): boolean
```

Checks whether all elements in this ArkTS array meet a given condition.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-every(predicate: ArrayPredicateFn<T, Array<T>>): boolean--><!--Device-Array-every(predicate: ArrayPredicateFn<T, Array<T>>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [ArrayPredicateFn](arkts-arkts-collections-arraypredicatefn-t.md)&lt;T, Array&lt;T&gt;&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## extendTo

```TypeScript
extendTo(arrayLength: number, initialValue: T): void
```

Extends this array to a given length by adding elements with the specified initial value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-extendTo(arrayLength: number, initialValue: T): void--><!--Device-Array-extendTo(arrayLength: number, initialValue: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLength | number | Yes |
| initialValue | T | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## fill

```TypeScript
fill(value: T, start?: number, end?: number): Array<T>
```

Fills elements in the specified range of this ArkTS array with a given value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-fill(value: T, start?: number, end?: number): Array<T>--><!--Device-Array-fill(value: T, start?: number, end?: number): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## filter

```TypeScript
filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T>
```

Returns a new array containing all elements that pass a test provided by a callback function.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T>--><!--Device-Array-filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: number, array: Array & lt;T & gt;) = & gt; boolean | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## find

```TypeScript
find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined
```

Returns the value of the first element that passes a test provided by a callback function. If none of the elements pass the test, **undefined** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined--><!--Device-Array-find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: number, obj: Array & lt;T & gt;) = & gt; boolean | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number
```

Returns the index of the first element that passes a test provided by a callback function. If none of the elements pass the test, **-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number--><!--Device-Array-findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: number, obj: Array & lt;T & gt;) = & gt; boolean | Yes |

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
forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void
```

Calls a callback function for each element in this ArkTS Array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void--><!--Device-Array-forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index: number, array: Array & lt;T & gt;) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>): Array<T>
```

Creates an ArkTS array from an array-like object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-static from<T>(arrayLike: ArrayLike<T>): Array<T>--><!--Device-Array-static from<T>(arrayLike: ArrayLike<T>): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## from

```TypeScript
static from<T>(iterable: Iterable<T>): Array<T>
```

Creates an ArkTS array from an iterable object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-static from<T>(iterable: Iterable<T>): Array<T>--><!--Device-Array-static from<T>(iterable: Iterable<T>): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iterable | Iterable & lt;T & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>
```

Creates an ArkTS array from an array-like object, and uses a custom function to process each array element.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>--><!--Device-Array-static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;T&gt; \| Iterable & lt;T & gt; | Yes |
| mapFn | [ArrayFromMapFn](arkts-arkts-collections-arrayfrommapfn-t.md)&lt;T, T&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

## from

```TypeScript
static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>
```

Creates an ArkTS array from an array-like object, and uses a custom function to process each array element. The type of the elements in the array-like object can be different from that of the array elements.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>--><!--Device-Array-static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;U&gt; \| Iterable & lt;U & gt; | Yes |
| mapFn | [ArrayFromMapFn](arkts-arkts-collections-arrayfrommapfn-t.md)&lt;U, T&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: number): boolean
```

Checks whether this ArkTS array contains an element and returns a Boolean value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-includes(searchElement: T, fromIndex?: number): boolean--><!--Device-Array-includes(searchElement: T, fromIndex?: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | T | Yes |
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
indexOf(searchElement: T, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in this ArkTS Array. If the value is not found, **-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-indexOf(searchElement: T, fromIndex?: number): number--><!--Device-Array-indexOf(searchElement: T, fromIndex?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | T | Yes |
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

## isArray

```TypeScript
static isArray(value: Object | undefined | null): boolean
```

Check whether the input parameter is an ArkTS array.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-static isArray(value: Object | undefined | null): boolean--><!--Device-Array-static isArray(value: Object | undefined | null): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Object \| undefined \| null | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## join

```TypeScript
join(separator?: string): string
```

Concatenates all elements in this ArkTS array into a string, with a given separator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-join(separator?: string): string--><!--Device-Array-join(separator?: string): string-End-->

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

Returns an iterator object that contains the index of each element in this ArkTS array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-keys(): IterableIterator<number>--><!--Device-Array-keys(): IterableIterator<number>-End-->

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
lastIndexOf(searchElement: T, fromIndex?: number): number
```

Obtains the index of the last occurrence of the specified value in this ArkTS array.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-lastIndexOf(searchElement: T, fromIndex?: number): number--><!--Device-Array-lastIndexOf(searchElement: T, fromIndex?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | T | Yes |
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
map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U>
```

Calls a callback function for each element in this ArkTS Array and returns a new array that contains the result of the callback function.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U>--><!--Device-Array-map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index: number, array: Array & lt;T & gt;) = & gt; U | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;U & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## of

```TypeScript
static of<T>(...items: T[]): Array<T>
```

Creates an ArkTS array with a variable number of parameters.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-static of<T>(...items: T[]): Array<T>--><!--Device-Array-static of<T>(...items: T[]): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | T[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

## pop

```TypeScript
pop(): T | undefined
```

Removes the last element from this ArkTS array and returns that element. If the array is empty, **undefined** is returned and the array does not change.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-pop(): T | undefined--><!--Device-Array-pop(): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## push

```TypeScript
push(...items: T[]): number
```

Adds elements to the end of this ArkTS array and returns the new length of the array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-push(...items: T[]): number--><!--Device-Array-push(...items: T[]): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | T[] | Yes |

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
reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T
```

Calls a callback function for each element in this ArkTS array, uses the previous return value of the function as an accumulated value, and returns the final result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T--><!--Device-Array-reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (previousValue: T, currentValue: T, currentIndex: number, array: Array & lt;T & gt;) = & gt; T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reduce

```TypeScript
reduce<U>(
      callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U,
      initialValue: U
    ): U
```

Similar to the previous API, this API takes an initial value as the second parameter to initialize the accumulator before the array traversal starts.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-reduce<U>(      callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U,      initialValue: U    ): U--><!--Device-Array-reduce<U>(      callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U,      initialValue: U    ): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (previousValue: U, currentValue: T, currentIndex: number, array: Array & lt;T & gt;) = & gt; U | Yes |
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
reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U
```

This API is similar to the  
[reduceRight](#reduceRight) API, but it takes an initial value as the second parameter to initialize the accumulator before the array traversal starts from right to left.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U--><!--Device-Array-reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [ArrayReduceCallback](arkts-arkts-collections-arrayreducecallback-t.md)&lt;U, T, Array&lt;T&gt;&gt; | Yes |
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
reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T
```

Goes through each element in this ArkTS array from right to left, uses a callback function to combine them into a single value, and returns that final value.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T--><!--Device-Array-reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [ArrayReduceCallback](arkts-arkts-collections-arrayreducecallback-t.md)&lt;T, T, Array&lt;T&gt;&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## reverse

```TypeScript
reverse(): Array<T>
```

Reverses elements in this ArkTS array and returns a reference to the same array.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-reverse(): Array<T>--><!--Device-Array-reverse(): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## shift

```TypeScript
shift(): T | undefined
```

Removes the first element from this ArkTS array and returns that element. If the array is empty, **undefined** is returned and the array does not change.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-shift(): T | undefined--><!--Device-Array-shift(): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## shrinkTo

```TypeScript
shrinkTo(arrayLength: number): void
```

Shrinks this ArkTS array to a given length.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-shrinkTo(arrayLength: number): void--><!--Device-Array-shrinkTo(arrayLength: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLength | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## slice

```TypeScript
slice(start?: number, end?: number): Array<T>
```

Selects a range of elements in this ArkTS array to create an array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-slice(start?: number, end?: number): Array<T>--><!--Device-Array-slice(start?: number, end?: number): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## some

```TypeScript
some(predicate: ArrayPredicateFn<T, Array<T>>): boolean
```

Checks whether this ArkTS array contains an element that meets certain conditions.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-some(predicate: ArrayPredicateFn<T, Array<T>>): boolean--><!--Device-Array-some(predicate: ArrayPredicateFn<T, Array<T>>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [ArrayPredicateFn](arkts-arkts-collections-arraypredicatefn-t.md)&lt;T, Array&lt;T&gt;&gt; | Yes |

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
sort(compareFn?: (a: T, b: T) => number): Array<T>
```

Sorts elements in this ArkTS array and returns a new array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-sort(compareFn?: (a: T, b: T) => number): Array<T>--><!--Device-Array-sort(compareFn?: (a: T, b: T) => number): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compareFn | (a: T, b: T) = & gt; number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## splice

```TypeScript
splice(start: number): Array<T>
```

Removes elements from a specified position (start) and all elements after the specified position in an array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-splice(start: number): Array<T>--><!--Device-Array-splice(start: number): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## splice

```TypeScript
splice(start: number, deleteCount: number, ...items: T[]): Array<T>
```

Removes elements from a specified position in an array, and inserts new elements from the same position.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-splice(start: number, deleteCount: number, ...items: T[]): Array<T>--><!--Device-Array-splice(start: number, deleteCount: number, ...items: T[]): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| deleteCount | number | Yes |
| items | T[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Generates a string that matches the cultural conversions of the current system locale. Each element converts itself to a string via its **toLocaleString** API, and these strings are then joined in sequence with commas (,).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-toLocaleString(): string--><!--Device-Array-toLocaleString(): string-End-->

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

Converts an ArkTS array into a string.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Array-toString(): string--><!--Device-Array-toString(): string-End-->

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

## unshift

```TypeScript
unshift(...items: T[]): number
```

Adds elements to the beginning of this ArkTS array and returns the new length of the array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-unshift(...items: T[]): number--><!--Device-Array-unshift(...items: T[]): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | T[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterator object that contains the value of each element in this ArkTS array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-values(): IterableIterator<T>--><!--Device-Array-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## [index: number]

```TypeScript
[index: number]: T
```

Returns the element at a given index in this array.

**Type:** T

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-[index: number]: T--><!--Device-Array-[index: number]: T-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

Number of elements in an ArkTS array.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Array-readonly length: number--><!--Device-Array-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
