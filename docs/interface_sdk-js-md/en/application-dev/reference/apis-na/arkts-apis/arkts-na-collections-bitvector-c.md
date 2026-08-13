# BitVector

An ordered collections of bit values, which are either 0 or 1. If multiple threads access a BitVector instance concurrently, and at least one of the threads modifies the array structurally, it must be synchronized externally.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-collections-class BitVector--><!--Device-collections-class BitVector-End-->

**System capability:** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<int>
```

Returns an iterator that iterates over bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-$_iterator(): IterableIterator<int>--><!--Device-BitVector-$_iterator(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;int&gt; | A new iterable iterator object. |

## constructor

```TypeScript
constructor(length: int)
```

A constructor used to create a BitVector object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-constructor(length: int)--><!--Device-BitVector-constructor(length: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | The length of BitVector object. |

## flipBitByIndex

```TypeScript
flipBitByIndex(index: int): void
```

Flips the bit value by index in a bit vector.(Flip 0 to 1, flip 1 to 0)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-flipBitByIndex(index: int): void--><!--Device-BitVector-flipBitByIndex(index: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index in the bit vector. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The flipBitByIndex method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of index is out of range. |

## flipBitsByRange

```TypeScript
flipBitsByRange(fromIndex: int, toIndex: int): void
```

Flips a range of bit values in a bit vector.(Flip 0 to 1, flip 1 to 0).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-flipBitsByRange(fromIndex: int, toIndex: int): void--><!--Device-BitVector-flipBitsByRange(fromIndex: int, toIndex: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, excluding the value at that index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The flipBitsByRange method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## getBitCountByRange

```TypeScript
getBitCountByRange(element: int, fromIndex: int, toIndex: int): int
```

Counts the number of times a certain bit element occurs within a range of bits in a bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-getBitCountByRange(element: int, fromIndex: int, toIndex: int): int--><!--Device-BitVector-getBitCountByRange(element: int, fromIndex: int, toIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be counted (0 means 0, else means 1). |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, excluding the value at that index. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The number type, return the number of times a certain bit element |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The getBitCountByRange method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## getBitsByRange

```TypeScript
getBitsByRange(fromIndex: int, toIndex: int): BitVector
```

Returns the bit values in a range of indices in a bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-getBitsByRange(fromIndex: int, toIndex: int): BitVector--><!--Device-BitVector-getBitsByRange(fromIndex: int, toIndex: int): BitVector-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, excluding the value at that index. |

**Return value:**

| Type | Description |
| --- | --- |
| [BitVector](../../apis-arkts/arkts-apis/arkts-arkts-collections-bitvector-c.md) | The BitVector type, returns the bit values in a range of indices in a bit vector. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The getBitsByRange method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## getIndexOf

```TypeScript
getIndexOf(element: int, fromIndex: int, toIndex: int): int
```

Locates the first occurrence of a certain bit value within a range of bits in a bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-getIndexOf(element: int, fromIndex: int, toIndex: int): int--><!--Device-BitVector-getIndexOf(element: int, fromIndex: int, toIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be Located (0 means 0, else means 1). |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, excluding the value at that index. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The number type, return the first index of specified bit within a range, or -1 if this range of the bitVector does not contain the element. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The getIndexOf method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## getLastIndexOf

```TypeScript
getLastIndexOf(element: int, fromIndex: int, toIndex: int): int
```

Locates the last occurrence of a certain bit value within a range of bits in a bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-getLastIndexOf(element: int, fromIndex: int, toIndex: int): int--><!--Device-BitVector-getLastIndexOf(element: int, fromIndex: int, toIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be Located (0 means 0, else means 1). |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, excluding the value at that index. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The number type, return the last index of specified bit within a range, or -1 if this range of the bitVector does not contain the element. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The getLastIndexOf method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## has

```TypeScript
has(element: int, fromIndex: int, toIndex: int): boolean
```

Check if bit vector contains a particular bit element.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-has(element: int, fromIndex: int, toIndex: int): boolean--><!--Device-BitVector-has(element: int, fromIndex: int, toIndex: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be contained (0 means 0, else means 1). |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, containing the value at that index. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The boolean type, if bit vector contains the specified element, return true, |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The has method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## pop

```TypeScript
pop(): int | undefined
```

Retrieves and removes the bit element to the end of this bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-pop(): int | undefined--><!--Device-BitVector-pop(): int | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The boolean type, if the bit push successfully, return true, else return false. |

## push

```TypeScript
push(element: int): boolean
```

Appends the bit element to the end of this bit vector.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-push(element: int): boolean--><!--Device-BitVector-push(element: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be appended to this bit vector (0 means 0, else means 1). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The boolean type, returns true if the addition is successful, and returns false if it fails. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The push method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |

## resize

```TypeScript
resize(size: int): void
```

Resize the bitVector's length.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-resize(size: int): void--><!--Device-BitVector-resize(size: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int | Yes | The new size for bitVector. If count is greater than the current size of bitVector, the additional bit elements are set to 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The resize method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |

## setAllBits

```TypeScript
setAllBits(element: int): void
```

Sets all of bits in a bit vector to a particular element.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-setAllBits(element: int): void--><!--Device-BitVector-setAllBits(element: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be set (0 means 0, else means 1). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The setAllBits method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |

## setBitsByRange

```TypeScript
setBitsByRange(element: int, fromIndex: int, toIndex: int): void
```

Sets a range of bits in a bit vector to a particular element.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-setBitsByRange(element: int, fromIndex: int, toIndex: int): void--><!--Device-BitVector-setBitsByRange(element: int, fromIndex: int, toIndex: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | int | Yes | Element to be set (0 means 0, else means 1). |
| fromIndex | int | Yes | The starting position of the index, containing the value at that index position. |
| toIndex | int | Yes | The end of the index, excluding the value at that index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The setBitsByRange method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |
| [10200001](../../apis-arkts/errorcode-utils.md#10200001-value-out-of-range) | The value of fromIndex or toIndex is out of range. |

## values

```TypeScript
values(): IterableIterator<int>
```

Returns an iterable of values in the bit vector

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BitVector-values(): IterableIterator<int>--><!--Device-BitVector-values(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;int&gt; | A new iterable iterator object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200011](../../apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) | The values method cannot be bound. |
| [10200201](../../apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) | Concurrent modification error. |

