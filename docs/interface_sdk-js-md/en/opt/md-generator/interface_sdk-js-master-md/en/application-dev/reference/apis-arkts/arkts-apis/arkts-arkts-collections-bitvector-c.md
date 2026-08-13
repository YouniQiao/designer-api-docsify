# BitVector

A linear data structure that is implemented on arrays. A bit vector stores bit values and provides bit-level storage and processing. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable

**Since:** 12

**Deprecated since:** -1

<!--Device-collections-class BitVector--><!--Device-collections-class BitVector-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

Returns an iterator that iterates over bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-[Symbol.iterator](): IterableIterator<number>--><!--Device-BitVector-[Symbol.iterator](): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## constructor

```TypeScript
constructor(length: number)
```

Constructor used to create a bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-constructor(length: number)--><!--Device-BitVector-constructor(length: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [length](#length) | number | Yes |

## flipBitByIndex

```TypeScript
flipBitByIndex(index: number): void
```

Flips the bit value (from 0 to 1 or from 1 to 0) at a given index in this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-flipBitByIndex(index: number): void--><!--Device-BitVector-flipBitByIndex(index: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## flipBitsByRange

```TypeScript
flipBitsByRange(fromIndex: number, toIndex: number): void
```

Flips the bit values (from 0 to 1 or from 1 to 0) in a given range in this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-flipBitsByRange(fromIndex: number, toIndex: number): void--><!--Device-BitVector-flipBitsByRange(fromIndex: number, toIndex: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## getBitCountByRange

```TypeScript
getBitCountByRange(element: number, fromIndex: number, toIndex: number): number
```

Counts the number of bit values in a given range of this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-getBitCountByRange(element: number, fromIndex: number, toIndex: number): number--><!--Device-BitVector-getBitCountByRange(element: number, fromIndex: number, toIndex: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## getBitsByRange

```TypeScript
getBitsByRange(fromIndex: number, toIndex: number): BitVector
```

Obtains bit values within a given range of this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-getBitsByRange(fromIndex: number, toIndex: number): BitVector--><!--Device-BitVector-getBitsByRange(fromIndex: number, toIndex: number): BitVector-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [BitVector](arkts-arkts-collections-bitvector-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## getIndexOf

```TypeScript
getIndexOf(element: number, fromIndex: number, toIndex: number): number
```

Returns the index of the first occurrence of a bit value in this bit vector. If the bit value is not found, **-1** is returned.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-getIndexOf(element: number, fromIndex: number, toIndex: number): number--><!--Device-BitVector-getIndexOf(element: number, fromIndex: number, toIndex: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## getLastIndexOf

```TypeScript
getLastIndexOf(element: number, fromIndex: number, toIndex: number): number
```

Returns the index of the last occurrence of a bit value in this bit vector. If the bit value is not found, **-1** is returned.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-getLastIndexOf(element: number, fromIndex: number, toIndex: number): number--><!--Device-BitVector-getLastIndexOf(element: number, fromIndex: number, toIndex: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## has

```TypeScript
has(element: number, fromIndex: number, toIndex: number): boolean
```

Checks whether a bit value is included in a given range of this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-has(element: number, fromIndex: number, toIndex: number): boolean--><!--Device-BitVector-has(element: number, fromIndex: number, toIndex: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## pop

```TypeScript
pop(): number
```

Removes the last element from this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-pop(): number--><!--Device-BitVector-pop(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## push

```TypeScript
push(element: number): boolean
```

Adds an element at the end of this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-push(element: number): boolean--><!--Device-BitVector-push(element: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## resize

```TypeScript
resize(size: number): void
```

Resizes this bit vector. If **size** is greater than the length of the existing bit vector, the bit vector is extended, and elements of the extra part are set to 0. If **size** is less than or equal to the length of the existing bit vector, the bit vector is shrunk according to the size.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-resize(size: number): void--><!--Device-BitVector-resize(size: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## setAllBits

```TypeScript
setAllBits(element: number): void
```

Sets all elements in this bit vector to a bit value.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-setAllBits(element: number): void--><!--Device-BitVector-setAllBits(element: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## setBitsByRange

```TypeScript
setBitsByRange(element: number, fromIndex: number, toIndex: number): void
```

Sets elements in a given range in this bit vector to a bit value.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-setBitsByRange(element: number, fromIndex: number, toIndex: number): void--><!--Device-BitVector-setBitsByRange(element: number, fromIndex: number, toIndex: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | number | Yes |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## values

```TypeScript
values(): IterableIterator<number>
```

Returns an iterator object that contains the value of each element in this bit vector.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-values(): IterableIterator<number>--><!--Device-BitVector-values(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## length

```TypeScript
readonly length: number
```

Number of elements in a bit vector.

**Type:** number

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BitVector-readonly length: number--><!--Device-BitVector-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
