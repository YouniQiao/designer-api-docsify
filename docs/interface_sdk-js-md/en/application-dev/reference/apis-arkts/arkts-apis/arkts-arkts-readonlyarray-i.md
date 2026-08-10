# ReadonlyArray

A read-only array that provides methods for reading elements.

**Inheritance/Implementation:** ReadonlyArray extends [ConcatArray<T>](ConcatArray<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface ReadonlyArray<out T> extends ConcatArray<T>--><!--Device-unnamed-export interface ReadonlyArray<out T> extends ConcatArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## concat

```TypeScript
concat(...items: FixedArray<ConcatArray<T>>): Array<T>
```

Combines two or more arrays.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-concat(...items: FixedArray<ConcatArray<T>>): Array<T>--><!--Device-ReadonlyArray-concat(...items: FixedArray<ConcatArray<T>>): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | FixedArray&lt;ConcatArray&lt;T&gt;&gt; | Yes | Arrays to add. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | New combined array. |

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

Returns a new iterator object that contains key-value pairs for each index in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-entries(): IterableIterator<[int, T]>--><!--Device-ReadonlyArray-entries(): IterableIterator<[int, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; | New iterator object. |

## every

```TypeScript
every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

Tests whether all elements in the array pass the test implemented by the provided function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean--><!--Device-ReadonlyArray-every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if all elements pass the test, false otherwise. |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>
```

Creates a new array with all elements that pass the test implemented by the provided function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>--><!--Device-ReadonlyArray-filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | New array with elements that pass the test. |

## find

```TypeScript
find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

Returns the first element in the array that satisfies the provided testing function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined--><!--Device-ReadonlyArray-find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| T | First element satisfying the test, or undefined if none found. |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

Returns the index of the first element in the array that satisfies the provided testing function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int--><!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Index of first element satisfying the test, or -1 if none found. |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

Returns the last element in the array that satisfies the provided testing function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined--><!--Device-ReadonlyArray-findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Last element satisfying the test, or undefined if none found. |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

Returns the index of the last element in the array that satisfies the provided testing function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int--><!--Device-ReadonlyArray-findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Index of last element satisfying the test, or -1 if none found. |

## forEach

```TypeScript
forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void
```

Executes a provided function once for each array element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void--><!--Device-ReadonlyArray-forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; void | Yes | Function to execute for each element. |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

Determines whether an array includes a certain value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-includes(searchElement: T, fromIndex?: int): boolean--><!--Device-ReadonlyArray-includes(searchElement: T, fromIndex?: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The value to search for. |
| fromIndex | int | No | The position in this array at which to begin searching. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the value is found, false otherwise. |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

Returns the first index at which a given element can be found in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-indexOf(searchElement: T, fromIndex?: int): int--><!--Device-ReadonlyArray-indexOf(searchElement: T, fromIndex?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The element to search for. |
| fromIndex | int | No | The position in this array at which to begin searching. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | First index of the element, or -1 if not found. |

## join

```TypeScript
join(separator?: string): string
```

Joins all elements of an array into a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-join(separator?: string): string--><!--Device-ReadonlyArray-join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No | Specifies a string to separate adjacent elements. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string with all array elements joined. |

## keys

```TypeScript
keys(): IterableIterator<int>
```

Returns a new iterator object that contains the keys for each index in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-keys(): IterableIterator<int>--><!--Device-ReadonlyArray-keys(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | New iterator object containing keys. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T): int
```

Returns the last index at which a given element can be found in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-lastIndexOf(searchElement: T): int--><!--Device-ReadonlyArray-lastIndexOf(searchElement: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The element to search for. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Last index of the element, or -1 if not found. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T, fromIndex?: int): int
```

Returns the last index at which a given element can be found in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-ReadonlyArray-lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The element to search for. |
| fromIndex | int | No | The position in this array at which to begin searching backward. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Last index of the element, or -1 if not found. |

## map

```TypeScript
map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>
```

Transforms each element of the array using a mapper function and returns a new array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>--><!--Device-ReadonlyArray-map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mapper | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | Yes | Function to transform each element. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;U&gt; | New array with transformed elements. |

## reduce

```TypeScript
reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

Applies a function against an accumulator to reduce the array to a single value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T--><!--Device-ReadonlyArray-reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; T | Yes | Function to execute on each element. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The value resulting from the reduction. |

## reduce

```TypeScript
reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

Applies a function against an accumulator to reduce the array to a single value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U--><!--Device-ReadonlyArray-reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | Yes | Function to execute on each element. |
| initialValue | U | Yes | Initial value for the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The value resulting from the reduction. |

## reduceRight

```TypeScript
reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

Applies a function against an accumulator to reduce the array from right to left to a single value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T--><!--Device-ReadonlyArray-reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; T | Yes | Function to execute on each element. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The value resulting from the reduction. |

## reduceRight

```TypeScript
reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

Applies a function against an accumulator to reduce the array from right to left to a single value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U--><!--Device-ReadonlyArray-reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | Yes | Function to execute on each element. |
| initialValue | U | Yes | Initial value for the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The value resulting from the reduction. |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

Returns a shallow copy of a portion of an array into a new array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-slice(start?: int, end?: int): Array<T>--><!--Device-ReadonlyArray-slice(start?: int, end?: int): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | No | Start index (inclusive). Defaults to 0. &lt;br&gt;The value should be an integer. |
| end | int | No | End index (exclusive). Defaults to array length. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | New array containing the extracted elements. |

## some

```TypeScript
some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

Tests whether at least one element in the array passes the test implemented by the provided function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean--><!--Device-ReadonlyArray-some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | Yes | Function to test each element. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if at least one element passes the test, false otherwise. |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns a new iterator object that contains the values for each index in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlyArray-values(): IterableIterator<T>--><!--Device-ReadonlyArray-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | New iterator object containing values. |

