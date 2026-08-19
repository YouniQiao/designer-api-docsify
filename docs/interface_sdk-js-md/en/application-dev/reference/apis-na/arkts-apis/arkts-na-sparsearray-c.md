# SparseArray

SparseArray is a sparse array implementation that uses Map as the underlying storage. It only stores non-undefined values, making it memory-efficient for arrays with many empty slots.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class SparseArray--><!--Device-unnamed-export class SparseArray-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## at

```TypeScript
at(index: int): T | undefined
```

Returns the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-at(index: int): T | undefined--><!--Device-SparseArray-at(index: int): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The zero-based index of the desired element. A negative index counts back from the end of the sparse array. If index is negative, it is treated as length + index (e.g., -1 refers to the last element). If index is less than -length, returns undefined. If index is greater than or equal to length, returns undefined. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| T \| undefined | The element at the specified index, or undefined if the index is out of range. |

## concat

```TypeScript
concat(items: SparseArray<T>): SparseArray<T>
```

Returns a new sparse array consisting of this sparse array concatenated with other arrays or values.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-concat(items: SparseArray<T>): SparseArray<T>--><!--Device-SparseArray-concat(items: SparseArray<T>): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | Yes | Additional arrays and/or values to concatenate to the result. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | Returns a new SparseArray containing the elements of this sparse array followed by the elements from the input sparse array. |

## constructor

```TypeScript
constructor()
```

Creates a new empty instance of SparseArray.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-constructor()--><!--Device-SparseArray-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(arrayLen: int)
```

Creates a new instance of SparseArray with the specified initial length.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-constructor(arrayLen: int)--><!--Device-SparseArray-constructor(arrayLen: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLen | int | Yes | The initial length of the sparse array. If arrayLen is negative, it is clamped to 0. The maximum value of a positive number is int_max. <br>The value should be an integer. |

## constructor

```TypeScript
constructor(first: T, ...d: T[])
```

Creates a new instance of SparseArray with the given elements.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-constructor(first: T, ...d: T[])--><!--Device-SparseArray-constructor(first: T, ...d: T[])-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | T | Yes | The first element of the sparse array. |
| d | T[] | Yes | The rest of the elements to initialize the sparse array with. |

## copyWithin

```TypeScript
copyWithin(target: int, start: int, end?: int): this
```

Copies a sequence of sparse array elements within the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-copyWithin(target: int, start: int, end?: int): this--><!--Device-SparseArray-copyWithin(target: int, start: int, end?: int): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | int | Yes | The zero-based index at which to copy the sequence to. <br>The value should be an integer. |
| start | int | Yes | The zero-based index at which to begin copying elements from. <br>The value should be an integer. |
| end | int | No | The zero-based index at which to stop copying elements from. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the modified sparse array. |

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

Returns an iterable of key, value pairs for every entry in the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-entries(): IterableIterator<[int, T]>--><!--Device-SparseArray-entries(): IterableIterator<[int, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[int, T]&gt; | An iterable of key, value pairs for every entry in the sparse array. |

## every

```TypeScript
every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

Determines whether all the members of a sparse array satisfy the specified test.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean--><!--Device-SparseArray-every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The every method calls the predicate function for each element in the sparse array until the predicate returns a value which is coercible to the Boolean value false,or until the end of the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the callback function returns true for all elements, otherwise returns false. |

## fill

```TypeScript
fill(value: T, start?: int, end?: int): this
```

Changes all sparse array elements from start to end index to a static value and returns the modified sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-fill(value: T, start?: int, end?: int): this--><!--Device-SparseArray-fill(value: T, start?: int, end?: int): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value to fill the sparse array section with. |
| start | int | No | The index to start filling the sparse array at. Defaults to 0. If start is negative, it is treated as length + start. <br>The value should be an integer. |
| end | int | No | The index to stop filling the sparse array at. Defaults to 0. If end is negative, it is treated as length + end. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The modified sparse array. |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>
```

Returns the elements of a sparse array that meet the condition specified in a callback function.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>--><!--Device-SparseArray-filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | A sparse array containing the elements that meet the condition. |

## find

```TypeScript
find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

Returns the value of the first element in the sparse array where predicate is true, and undefined otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined--><!--Device-SparseArray-find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The find method calls the predicate function one time for each element in the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| T \| undefined | The value of the first element in the sparse array where predicate is true, and undefined otherwise. |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

Returns the index of the first element in the sparse array where predicate is true, and -1 otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int--><!--Device-SparseArray-findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The findIndex method calls the predicate function one time for each element in the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element in the sparse array where predicate is true, and -1 otherwise. |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

Returns the value of the last element in the sparse array where predicate is true, and undefined otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined--><!--Device-SparseArray-findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The findLast method calls the predicate function one time for each element in the sparse array, in descending order. |

**Return value:**

| Type | Description |
| --- | --- |
| T \| undefined | The value of the last element in the sparse array where predicate is true, and undefined otherwise. |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

Returns the index of the last element in the sparse array where predicate is true, and -1 otherwise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int--><!--Device-SparseArray-findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The findLastIndex method calls the predicate function one time for each element in the sparse array, in descending order. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the last element in the sparse array where predicate is true, and -1 otherwise. |

## flat

```TypeScript
flat<U = T>(depth?: int): SparseArray<U>
```

Returns a new sparse array with all sub-array elements concatenated into it recursively up to the specified depth.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-flat<U = T>(depth?: int): SparseArray<U>--><!--Device-SparseArray-flat<U = T>(depth?: int): SparseArray<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| depth | int | No | The depth level specifying how deep the nested array structure should be flattened. Defaults to 1. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;U&gt; | SparseArray |

## flatMap

```TypeScript
flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>
```

Calls a defined callback function on each element of a sparse array. Then, flattens the result into a new sparse array. This is identical to a map() followed by a flat() with depth 1.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>--><!--Device-SparseArray-flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fn | (v: T, k: int, arr: SparseArray&lt;T&gt;) =&gt; U | Yes | A function that produces an element of the new SparseArray. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;U&gt; | A new sparse array with each element being the result of the callback function and flattened. |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void
```

Performs the specified action for each element in the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void--><!--Device-SparseArray-forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; void | Yes | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the sparse array. |

## from

```TypeScript
static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>
```

Creates a new SparseArray instance from an array-like or iterable object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>--><!--Device-SparseArray-static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | ArrayLike&lt;U&gt; \| Iterable&lt;U&gt; | Yes | An array-like or iterable object to convert to a sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;U&gt; | A new SparseArray instance. |

## from

```TypeScript
static from<U>(arr: ArrayLike<U>): SparseArray<U>
```

Creates a new SparseArray instance from an array-like.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-static from<U>(arr: ArrayLike<U>): SparseArray<U>--><!--Device-SparseArray-static from<U>(arr: ArrayLike<U>): SparseArray<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | ArrayLike&lt;U&gt; | Yes | An array-like or iterable object to convert to a sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;U&gt; | A new SparseArray instance. |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

Determines whether the sparse array includes a certain element, returning true or false as appropriate.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-includes(searchElement: T, fromIndex?: int): boolean--><!--Device-SparseArray-includes(searchElement: T, fromIndex?: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The element to search for. |
| fromIndex | int | No | The position in this sparse array at which to begin searching for searchElement. Defaults to 0 (the entire array is searched). If fromIndex is negative, it is used as the offset from the end of the array. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if searchElement is found, false otherwise. |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

Returns the index of the first occurrence of a value in a sparse array, or -1 if it is not present.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-indexOf(searchElement: T, fromIndex?: int): int--><!--Device-SparseArray-indexOf(searchElement: T, fromIndex?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The value to locate in the sparse array. |
| fromIndex | int | No | The sparse array index at which to begin the search. If fromIndex is omitted, the search starts at index 0. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first occurrence of the value in the sparse array, or -1 if not found. |

## isSparseArray

```TypeScript
static isSparseArray(value: Any): boolean
```

Determines whether the specified value is a sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-static isSparseArray(value: Any): boolean--><!--Device-SparseArray-static isSparseArray(value: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Any | Yes | The value to test. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is a sparse array, false otherwise. |

## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of a sparse array separated by the specified separator string.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-join(separator?: string): string--><!--Device-SparseArray-join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No | A string used to separate one element of the sparse array from the next in the resulting string. Defaults to "," (comma). |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string with all sparse array elements joined. |

## keys

```TypeScript
keys(): IterableIterator<int>
```

Returns an iterable of keys in the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-keys(): IterableIterator<int>--><!--Device-SparseArray-keys(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;int&gt; | An iterable of keys in the sparse array. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T, fromIndex?: int): int
```

Returns the index of the last occurrence of a value in a sparse array, or -1 if it is not present.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-SparseArray-lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | T | Yes | The value to locate in the sparse array. |
| fromIndex | int | No | The sparse array index at which to begin the search backwards. If fromIndex is omitted, the search starts at the last index. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the last occurrence of the value in the sparse array, or -1 if not found. |

## map

```TypeScript
map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>
```

Calls a defined callback function on each element of a sparse array, and returns an array that contains the results.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>--><!--Device-SparseArray-map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | Yes | A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;U&gt; |  |

## of

```TypeScript
static of<U>(...items: U[]): SparseArray<U>
```

Creates a new SparseArray instance from a variable number of arguments.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-static of<U>(...items: U[]): SparseArray<U>--><!--Device-SparseArray-static of<U>(...items: U[]): SparseArray<U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | U[] | Yes | Elements to include in the new SparseArray instance. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;U&gt; | A new SparseArray instance containing the specified elements. |

## pop

```TypeScript
pop(): T | undefined
```

Removes the last element from a sparse array and returns it.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-pop(): T | undefined--><!--Device-SparseArray-pop(): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T \| undefined | The last element of the sparse array, or undefined if the sparse array is empty. |

## push

```TypeScript
push(...items: T[]): int
```

Appends new elements to the end of the sparse array and returns the new length.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-push(...items: T[]): int--><!--Device-SparseArray-push(...items: T[]): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | T[] | Yes | The elements to add to the end of the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The new length of the sparse array. |

## push

```TypeScript
push(val: T): int
```

Appends new elements to the end of the sparse array and returns the new length.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-push(val: T): int--><!--Device-SparseArray-push(val: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | T | Yes | The elements to add to the end of the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The new length of the sparse array. |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

Calls the specified callback function for all the elements in a sparse array. The return value of the callback function is the accumulated result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T--><!--Device-SparseArray-reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; T | Yes | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The accumulated result. |

## reduce

```TypeScript
reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in a sparse array. The return value of the callback function is the accumulated result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U--><!--Device-SparseArray-reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the sparse array. |
| initialValue | U | Yes | If initialValue is specified, it is used as the initial value to start the accumulation. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

Calls the specified callback function for all the elements in a sparse array, in descending order. The return value of the callback function is the accumulated result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T--><!--Device-SparseArray-reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; T | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the sparse array, in descending order. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The accumulated result. |

## reduceRight

```TypeScript
reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in a sparse array, in descending order. The return value of the callback function is the accumulated result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U--><!--Device-SparseArray-reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the sparse array, in descending order. |
| initialValue | U | Yes | If initialValue is specified, used as the initial value to start the accumulation. |

**Return value:**

| Type | Description |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): this
```

Reverses the elements in a sparse array in place and returns the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-reverse(): this--><!--Device-SparseArray-reverse(): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| this | The reversed sparse array. |

## shift

```TypeScript
shift(): T | undefined
```

Removes the first element from a sparse array and returns it.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-shift(): T | undefined--><!--Device-SparseArray-shift(): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T \| undefined | The first element of the sparse array, or undefined if the sparse array is empty. |

## slice

```TypeScript
slice(start?: int, end?: int): SparseArray<T>
```

Returns a copy of a section of a sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-slice(start?: int, end?: int): SparseArray<T>--><!--Device-SparseArray-slice(start?: int, end?: int): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | No | The beginning index of the specified portion of the sparse array. Defaults to 0 (the entire array is searched). If fromIndex is negative, it is used as the offset from the end of the array. <br>The value should be an integer. |
| end | int | No | The end index of the specified portion of the sparse array. Defaults to 0 (the entire array is searched). If fromIndex is negative, it is used as the offset from the end of the array. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | A new SparseArray object containing the extracted elements. |

## some

```TypeScript
some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of a sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean--><!--Device-SparseArray-some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | Yes | A function that accepts up to three arguments. The some method calls the predicate function for each element in the sparse array until the predicate returns a value is coercible to the Boolean value true,until the end of the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the callback function returns true for any element, otherwise returns false. |

## sort

```TypeScript
sort(compareFn?: (a: T, b: T) => int): this
```

Sorts the elements of a sparse array in place and returns the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-sort(compareFn?: (a: T, b: T) => int): this--><!--Device-SparseArray-sort(compareFn?: (a: T, b: T) => int): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; int | No | A function used to determine the order of the elements. If not provided, elements are sorted by converting them to strings and comparing their UTF-16 code units in ascending order (default sort behavior). |

**Return value:**

| Type | Description |
| --- | --- |
| this | The sorted sparse array. |

## splice

```TypeScript
splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

Changes the contents of the sparse array by removing or replacing existing elements and/or adding new elements in place.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>--><!--Device-SparseArray-splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | The zero-based location in the sparse array from which to start removing elements. If start is negative, it is treated as length + start (e.g., -1 refers to the last element). If start is less than -length, it is clamped to 0. If start is greater than or equal to length, no elements are removed and new elements are added at the end. <br>The value should be an integer. |
| deleteCount | int | Yes | The number of elements to remove. If deleteCount is negative, it is clamped to 0 (no elements are removed). If deleteCount is greater than the number of elements from start to the end of the array, only the available elements are removed. <br>The value should be an integer. |
| items | T[] | Yes | Elements to insert into the sparse array in place of the deleted elements. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | A sparse array containing the elements that were deleted. |

## toReversed

```TypeScript
toReversed(): SparseArray<T>
```

Returns a new sparse array with the elements in reversed order.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-toReversed(): SparseArray<T>--><!--Device-SparseArray-toReversed(): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | A new sparse array with the elements in reversed order. |

## toSorted

```TypeScript
toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>
```

Returns a new sparse array with the elements sorted in ascending order.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>--><!--Device-SparseArray-toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; int | No | A function used to determine the order of the elements. If not provided, elements are sorted by converting them to strings and comparing their UTF-16 code units in ascending order (default sort behavior). |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; |  |

## toSpliced

```TypeScript
toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

Returns a new sparse array with some elements removed and/or replaced at a given index.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>--><!--Device-SparseArray-toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | The zero-based location in the sparse array from which to start removing elements. If start is negative, it is treated as length + start (e.g., -1 refers to the last element). If start is less than -length, it is clamped to 0. If start is greater than or equal to length, no elements are removed and new elements are added at the end. If start is not an integer, it is truncated towards zero. <br>The value should be an integer. |
| deleteCount | int | Yes | The number of elements to remove. If deleteCount is negative, it is clamped to 0 (no elements are removed). If deleteCount is greater than the number of elements from start to the end of the array, only the available elements are removed. If deleteCount is not an integer, it is truncated towards zero. <br>The value should be an integer. |
| items | T[] | Yes | Elements to insert into the sparse array in place of the deleted elements. |

**Return value:**

| Type | Description |
| --- | --- |
| [SparseArray](arkts-na-sparsearray-c.md)&lt;T&gt; | A new sparse array with the specified elements removed and/or replaced. |

## toString

```TypeScript
toString(): string
```

Returns a string representing the sparse array and its elements.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-toString(): string--><!--Device-SparseArray-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns a string representing the elements of the sparse array separated by commas. |

## unshift

```TypeScript
unshift(...items: T[]): int
```

Inserts new elements at the start of a sparse array and returns the new length.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-unshift(...items: T[]): int--><!--Device-SparseArray-unshift(...items: T[]): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | T[] | Yes | Elements to insert at the start of the sparse array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The new length of the sparse array. |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterable of values in the sparse array.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SparseArray-values(): IterableIterator<T>--><!--Device-SparseArray-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;T&gt; | An iterable of values in the sparse array. |

