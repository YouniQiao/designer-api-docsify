# Uint8ClampedArray

A linear data structure that is implemented on [ArkTS ArrayBuffer](./arkts/@arkts.collections:collections).

> **NOTE：**
> 
> - This module can be imported only to ArkTS files (with the file name extension .ets).
> **Decorator**: \@Sendable

**Since:** 12

**Decorator:** @Sendable

<!--Device-collections-class Uint8ClampedArray--><!--Device-collections-class Uint8ClampedArray-End-->

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

<!--Device-Uint8ClampedArray-[Symbol.iterator](): IterableIterator<number>--><!--Device-Uint8ClampedArray-[Symbol.iterator](): IterableIterator<number>-End-->

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

<!--Device-Uint8ClampedArray-at(index: number): number | undefined--><!--Device-Uint8ClampedArray-at(index: number): number | undefined-End-->

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

A constructor used to create an empty ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-constructor()--><!--Device-Uint8ClampedArray-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(length: number)
```

A constructor used to create an ArkTS Uint8ClampedArray of a given length.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-constructor(length: number)--><!--Device-Uint8ClampedArray-constructor(length: number)-End-->

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

A constructor that creates an ArkTS Uint8ClampedArray from an iterable object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-constructor(elements: Iterable<number>)--><!--Device-Uint8ClampedArray-constructor(elements: Iterable<number>)-End-->

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

A constructor that creates an ArkTS Uint8ClampedArray from an array-like object or ArkTS ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-constructor(array: ArrayLike<number> | ArrayBuffer)--><!--Device-Uint8ClampedArray-constructor(array: ArrayLike<number> | ArrayBuffer)-End-->

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

A constructor that creates an ArkTS Uint8ClampedArray from an ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)--><!--Device-Uint8ClampedArray-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)-End-->

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
copyWithin(target: number, start: number, end?: number): Uint8ClampedArray
```

Copies elements within a given range from this ArkTS Uint8ClampedArray to another position in sequence.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-copyWithin(target: number, start: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-copyWithin(target: number, start: number, end?: number): Uint8ClampedArray-End-->

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
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

Returns an iterator object that contains the key-value pair of each element in this ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-entries(): IterableIterator<[number, number]>--><!--Device-Uint8ClampedArray-entries(): IterableIterator<[number, number]>-End-->

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
every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean
```

Checks whether all elements in this ArkTS Uint8ClampedArray meet a given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean--><!--Device-Uint8ClampedArray-every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

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
fill(value: number, start?: number, end?: number): Uint8ClampedArray
```

Fills all elements in a given range in this ArkTS Uint8ClampedArray with a value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-fill(value: number, start?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-fill(value: number, start?: number, end?: number): Uint8ClampedArray-End-->

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
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## filter

```TypeScript
filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray
```

Returns a new ArkTS Uint8ClampedArray that contains all elements that meet the given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## find

```TypeScript
find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined
```

Returns the value of the first element that passes a test provided by a callback function. If none of the elements pass the test, **undefined** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined--><!--Device-Uint8ClampedArray-find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

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
findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number
```

Returns the index of the first element that passes a test provided by a callback function. If none of the elements pass the test, **-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number--><!--Device-Uint8ClampedArray-findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

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
forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void
```

Calls a callback function for each element in this ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void--><!--Device-Uint8ClampedArray-forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## from

```TypeScript
static from(arrayLike: ArrayLike<number>): Uint8ClampedArray
```

Creates an ArkTS Uint8ClampedArray from an array-like or iterator object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-static from(arrayLike: ArrayLike<number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static from(arrayLike: ArrayLike<number>): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray
```

Creates an ArkTS Uint8ClampedArray from an array-like object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-default/arkts-apis/arkts-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;T, number&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

## from

```TypeScript
static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray
```

Creates an ArkTS Uint8ClampedArray from an iterator object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | Iterable & lt;number & gt; | Yes |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;number, number&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

## includes

```TypeScript
includes(searchElement: number, fromIndex?: number): boolean
```

Checks whether elements are contained in this ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-includes(searchElement: number, fromIndex?: number): boolean--><!--Device-Uint8ClampedArray-includes(searchElement: number, fromIndex?: number): boolean-End-->

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

Returns the index of the first occurrence of a value in this ArkTS Uint8ClampedArray. If the value is not found,  
**-1** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8ClampedArray-indexOf(searchElement: number, fromIndex?: number): number-End-->

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

Concatenates all elements in this ArkTS Uint8ClampedArray into a string, with a given separator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-join(separator?: string): string--><!--Device-Uint8ClampedArray-join(separator?: string): string-End-->

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

Returns an iterator object that contains the key (index) of each element in this ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-keys(): IterableIterator<number>--><!--Device-Uint8ClampedArray-keys(): IterableIterator<number>-End-->

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

Obtains the index of the last occurrence of the specified value in this ArkTS Uint8ClampedArray.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8ClampedArray-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8ClampedArray-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

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
map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray
```

Applies a callback function to each element in this ArkTS Uint8ClampedArray and uses the result to create an ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## of

```TypeScript
static of(...items: number[]): Uint8ClampedArray
```

Creates an ArkTS Uint8ClampedArray with a variable number of parameters.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8ClampedArray-static of(...items: number[]): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static of(...items: number[]): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | number[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number
```

Applies a reduce function on each element in this ArkTS Uint8ClampedArray and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number--><!--Device-Uint8ClampedArray-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint8ClampedArray&gt; | Yes |

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
reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U
```

Applies a reduce function for each element in this ArkTS Uint8ClampedArray, receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U--><!--Device-Uint8ClampedArray-reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint8ClampedArray&gt; | Yes |
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
reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U
```

Reversely traverses this ArkTS Uint8ClampedArray, applies a reduce function for each element in the array,receives an initial value as the parameter called by the reduce function for the first time, and returns the final reduction result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8ClampedArray-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U--><!--Device-Uint8ClampedArray-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint8ClampedArray&gt; | Yes |
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
reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number
```

Reversely traverses this ArkTS Uint8ClampedArray, applies a reduce function on each element in the array, and returns the final reduction result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8ClampedArray-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number--><!--Device-Uint8ClampedArray-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint8ClampedArray&gt; | Yes |

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
reverse(): Uint8ClampedArray
```

Reverses this ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-reverse(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-reverse(): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

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

<!--Device-Uint8ClampedArray-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint8ClampedArray-set(array: ArrayLike<number>, offset?: number): void-End-->

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
slice(start?: number, end?: number): Uint8ClampedArray
```

Selects a range of elements in this ArkTS Uint8ClampedArray to create an ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-slice(start?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-slice(start?: number, end?: number): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## some

```TypeScript
some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean
```

Checks whether any element in this ArkTS Uint8ClampedArray meets a given condition.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean--><!--Device-Uint8ClampedArray-some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8ClampedArray&gt; | Yes |

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
sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray
```

Sorts elements in this ArkTS Uint8ClampedArray and returns the sorted ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md)&lt;number&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint8ClampedArray
```

Truncates an array from a specified position and returns a new ArkTS Uint8ClampedArray based on the same ArkTS ArrayBuffer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-subarray(begin?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-subarray(begin?: number, end?: number): Uint8ClampedArray-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Generates digits that match the cultural conventions of the current system locale. Each element converts its digits to a string via its **toLocaleString** API, and these strings are then joined in sequence with commas (,).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8ClampedArray-toLocaleString(): string--><!--Device-Uint8ClampedArray-toLocaleString(): string-End-->

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

Converts an ArkTS Uint8ClampedArray into a string.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8ClampedArray-toString(): string--><!--Device-Uint8ClampedArray-toString(): string-End-->

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

Returns an iterator object that contains the value of each element in this ArkTS Uint8ClampedArray.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-values(): IterableIterator<number>--><!--Device-Uint8ClampedArray-values(): IterableIterator<number>-End-->

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

Number of bytes occupied by each element in the ArkTS Uint8ClampedArray.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-static readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8ClampedArray-static readonly BYTES_PER_ELEMENT: number-End-->

**System capability:** SystemCapability.Utils.Lang

## [index: number]

```TypeScript
[index: number]: number
```

Returns the item at that index.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-[index: number]: number--><!--Device-Uint8ClampedArray-[index: number]: number-End-->

**System capability:** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

Bottom-layer buffer used by an ArkTS Uint8ClampedArray.

**Type:** ArrayBuffer

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-readonly buffer: ArrayBuffer--><!--Device-Uint8ClampedArray-readonly buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: number
```

Number of bytes occupied by an ArkTS Uint8ClampedArray.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-readonly byteLength: number--><!--Device-Uint8ClampedArray-readonly byteLength: number-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: number
```

Offset between the ArkTS Uint8ClampedArray and the start position of the ArrayBuffer.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-readonly byteOffset: number--><!--Device-Uint8ClampedArray-readonly byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

Number of elements in an ArkTS Uint8ClampedArray.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8ClampedArray-readonly length: number--><!--Device-Uint8ClampedArray-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
