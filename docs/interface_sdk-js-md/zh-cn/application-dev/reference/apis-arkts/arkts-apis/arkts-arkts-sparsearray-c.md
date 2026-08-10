# SparseArray

SparseArray is a sparse array implementation that uses Map as the underlying storage.It only stores non-undefined values, making it memory-efficient for arrays with many empty slots.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class SparseArray<T>--><!--Device-unnamed-export class SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## at

```TypeScript
at(index: int): T | undefined
```

Returns the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-at(index: int): T | undefined--><!--Device-SparseArray-at(index: int): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The zero-based index of the desired element. A negative index counts back from the end of the sparse array. If index is negative, it is treated as length + index (e.g., -1 refers to the last element). If index is less than -length, returns undefined. If index is greater than or equal to length, returns undefined. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The element at the specified index, or undefined if the index is out of range. |

## concat

```TypeScript
concat(items: SparseArray<T>): SparseArray<T>
```

Returns a new sparse array consisting of this sparse array concatenated with other arrays or values.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-concat(items: SparseArray<T>): SparseArray<T>--><!--Device-SparseArray-concat(items: SparseArray<T>): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 是 | Additional arrays and/or values to concatenate to the result. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | Returns a new SparseArray containing the elements of this sparse array followed by the elements from the input sparse array. |

## constructor

```TypeScript
constructor()
```

Creates a new empty instance of SparseArray.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-constructor()--><!--Device-SparseArray-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(arrayLen: int)
```

Creates a new instance of SparseArray with the specified initial length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-constructor(arrayLen: int)--><!--Device-SparseArray-constructor(arrayLen: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLen | int | 是 | The initial length of the sparse array. If arrayLen is negative, it is clamped to 0. The maximum value of a positive number is int_max. &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
constructor(first: T, ...d: T[])
```

Creates a new instance of SparseArray with the given elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-constructor(first: T, ...d: T[])--><!--Device-SparseArray-constructor(first: T, ...d: T[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | T | 是 | The first element of the sparse array. |
| d | T[] | 是 | The rest of the elements to initialize the sparse array with. |

## copyWithin

```TypeScript
copyWithin(target: int, start: int, end?: int): this
```

Copies a sequence of sparse array elements within the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-copyWithin(target: int, start: int, end?: int): this--><!--Device-SparseArray-copyWithin(target: int, start: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | The zero-based index at which to copy the sequence to. &lt;br&gt;The value should be an integer. |
| start | int | 是 | The zero-based index at which to begin copying elements from. &lt;br&gt;The value should be an integer. |
| end | int | 否 | The zero-based index at which to stop copying elements from. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the modified sparse array. |

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

Returns an iterable of key, value pairs for every entry in the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-entries(): IterableIterator<[int, T]>--><!--Device-SparseArray-entries(): IterableIterator<[int, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; | An iterable of key, value pairs for every entry in the sparse array. |

## every

```TypeScript
every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

Determines whether all the members of a sparse array satisfy the specified test.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean--><!--Device-SparseArray-every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The every method calls the predicate function for each element in the sparse array until the predicate returns a value which is coercible to the Boolean value false,or until the end of the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the callback function returns true for all elements, otherwise returns false. |

## fill

```TypeScript
fill(value: T, start?: int, end?: int): this
```

Changes all sparse array elements from start to end index to a static value and returns the modified sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-fill(value: T, start?: int, end?: int): this--><!--Device-SparseArray-fill(value: T, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | The value to fill the sparse array section with. |
| start | int | 否 | The index to start filling the sparse array at. Defaults to 0. If start is negative, it is treated as length + start. &lt;br&gt;The value should be an integer. |
| end | int | 否 | The index to stop filling the sparse array at. Defaults to 0. If end is negative, it is treated as length + end. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The modified sparse array. |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>
```

Returns the elements of a sparse array that meet the condition specified in a callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>--><!--Device-SparseArray-filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | A sparse array containing the elements that meet the condition. |

## find

```TypeScript
find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

Returns the value of the first element in the sparse array where predicate is true, and undefined otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined--><!--Device-SparseArray-find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The find method calls the predicate function one time for each element in the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The value of the first element in the sparse array where predicate is true, and undefined otherwise. |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

Returns the index of the first element in the sparse array where predicate is true, and -1 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int--><!--Device-SparseArray-findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The findIndex method calls the predicate function one time for each element in the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index of the first element in the sparse array where predicate is true, and -1 otherwise. |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

Returns the value of the last element in the sparse array where predicate is true, and undefined otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined--><!--Device-SparseArray-findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The findLast method calls the predicate function one time for each element in the sparse array, in descending order. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The value of the last element in the sparse array where predicate is true, and undefined otherwise. |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

Returns the index of the last element in the sparse array where predicate is true, and -1 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int--><!--Device-SparseArray-findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The findLastIndex method calls the predicate function one time for each element in the sparse array, in descending order. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index of the last element in the sparse array where predicate is true, and -1 otherwise. |

## flat

```TypeScript
flat<U = T>(depth?: int): SparseArray<U>
```

Returns a new sparse array with all sub-array elements concatenated into it recursively up to the specified depth.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-flat<U = T>(depth?: int): SparseArray<U>--><!--Device-SparseArray-flat<U = T>(depth?: int): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| depth | int | 否 | The depth level specifying how deep the nested array structure should be flattened. Defaults to 1. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | SparseArray |

## flatMap

```TypeScript
flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>
```

Calls a defined callback function on each element of a sparse array. Then, flattens the result into a new sparse array.This is identical to a map() followed by a flat() with depth 1.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>--><!--Device-SparseArray-flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (v: T, k: int, arr: SparseArray&lt;T&gt;) =&gt; U | 是 | A function that produces an element of the new SparseArray. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | A new sparse array with each element being the result of the callback function and flattened. |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void
```

Performs the specified action for each element in the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void--><!--Device-SparseArray-forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; void | 是 | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the sparse array. |

## from

```TypeScript
static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>
```

Creates a new SparseArray instance from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>--><!--Device-SparseArray-static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;U&gt; \| Iterable&lt;U&gt; | 是 | An array-like or iterable object to convert to a sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | A new SparseArray instance. |

## from

```TypeScript
static from<U>(arr: ArrayLike<U>): SparseArray<U>
```

Creates a new SparseArray instance from an array-like.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static from<U>(arr: ArrayLike<U>): SparseArray<U>--><!--Device-SparseArray-static from<U>(arr: ArrayLike<U>): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;U&gt; | 是 | An array-like or iterable object to convert to a sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | A new SparseArray instance. |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

Determines whether the sparse array includes a certain element, returning true or false as appropriate.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-includes(searchElement: T, fromIndex?: int): boolean--><!--Device-SparseArray-includes(searchElement: T, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The element to search for. |
| fromIndex | int | 否 | The position in this sparse array at which to begin searching for searchElement. Defaults to 0 (the entire array is searched). If fromIndex is negative, it is used as the offset from the end of the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is found, false otherwise. |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

Returns the index of the first occurrence of a value in a sparse array, or -1 if it is not present.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-indexOf(searchElement: T, fromIndex?: int): int--><!--Device-SparseArray-indexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The value to locate in the sparse array. |
| fromIndex | int | 否 | The sparse array index at which to begin the search. If fromIndex is omitted, the search starts at index 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index of the first occurrence of the value in the sparse array, or -1 if not found. |

## isSparseArray

```TypeScript
static isSparseArray(value: Any): boolean
```

Determines whether the specified value is a sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static isSparseArray(value: Any): boolean--><!--Device-SparseArray-static isSparseArray(value: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Any | 是 | The value to test. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value is a sparse array, false otherwise. |

## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of a sparse array separated by the specified separator string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-join(separator?: string): string--><!--Device-SparseArray-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | A string used to separate one element of the sparse array from the next in the resulting string. Defaults to "," (comma). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string with all sparse array elements joined. |

## keys

```TypeScript
keys(): IterableIterator<int>
```

Returns an iterable of keys in the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-keys(): IterableIterator<int>--><!--Device-SparseArray-keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | An iterable of keys in the sparse array. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T, fromIndex?: int): int
```

Returns the index of the last occurrence of a value in a sparse array, or -1 if it is not present.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-SparseArray-lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The value to locate in the sparse array. |
| fromIndex | int | 否 | The sparse array index at which to begin the search backwards. If fromIndex is omitted, the search starts at the last index. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index of the last occurrence of the value in the sparse array, or -1 if not found. |

## map

```TypeScript
map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>
```

Calls a defined callback function on each element of a sparse array,and returns an array that contains the results.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>--><!--Device-SparseArray-map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | 是 | A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |  |

## of

```TypeScript
static of<U>(...items: U[]): SparseArray<U>
```

Creates a new SparseArray instance from a variable number of arguments.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static of<U>(...items: U[]): SparseArray<U>--><!--Device-SparseArray-static of<U>(...items: U[]): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | U[] | 是 | Elements to include in the new SparseArray instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | A new SparseArray instance containing the specified elements. |

## pop

```TypeScript
pop(): T | undefined
```

Removes the last element from a sparse array and returns it.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-pop(): T | undefined--><!--Device-SparseArray-pop(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The last element of the sparse array, or undefined if the sparse array is empty. |

## push

```TypeScript
push(...items: T[]): int
```

Appends new elements to the end of the sparse array and returns the new length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-push(...items: T[]): int--><!--Device-SparseArray-push(...items: T[]): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 | The elements to add to the end of the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The new length of the sparse array. |

## push

```TypeScript
push(val: T): int
```

Appends new elements to the end of the sparse array and returns the new length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-push(val: T): int--><!--Device-SparseArray-push(val: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | T | 是 | The elements to add to the end of the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The new length of the sparse array. |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

Calls the specified callback function for all the elements in a sparse array. The return value of the callback function is the accumulated result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T--><!--Device-SparseArray-reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; T | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The accumulated result. |

## reduce

```TypeScript
reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in a sparse array.The return value of the callback function is the accumulated result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U--><!--Device-SparseArray-reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the sparse array. |
| initialValue | U | 是 | If initialValue is specified, it is used as the initial value to start the accumulation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

Calls the specified callback function for all the elements in a sparse array, in descending order.The return value of the callback function is the accumulated result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T--><!--Device-SparseArray-reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; T | 是 | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the sparse array, in descending order. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The accumulated result. |

## reduceRight

```TypeScript
reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in a sparse array, in descending order.The return value of the callback function is the accumulated result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U--><!--Device-SparseArray-reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the sparse array, in descending order. |
| initialValue | U | 是 | If initialValue is specified, used as the initial value to start the accumulation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): this
```

Reverses the elements in a sparse array in place and returns the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reverse(): this--><!--Device-SparseArray-reverse(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The reversed sparse array. |

## shift

```TypeScript
shift(): T | undefined
```

Removes the first element from a sparse array and returns it.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-shift(): T | undefined--><!--Device-SparseArray-shift(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The first element of the sparse array, or undefined if the sparse array is empty. |

## slice

```TypeScript
slice(start?: int, end?: int): SparseArray<T>
```

Returns a copy of a section of a sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-slice(start?: int, end?: int): SparseArray<T>--><!--Device-SparseArray-slice(start?: int, end?: int): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | The beginning index of the specified portion of the sparse array. Defaults to 0 (the entire array is searched). If fromIndex is negative, it is used as the offset from the end of the array. &lt;br&gt;The value should be an integer. |
| end | int | 否 | The end index of the specified portion of the sparse array. Defaults to 0 (the entire array is searched). If fromIndex is negative, it is used as the offset from the end of the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | A new SparseArray object containing the extracted elements. |

## some

```TypeScript
some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of a sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean--><!--Device-SparseArray-some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The some method calls the predicate function for each element in the sparse array until the predicate returns a value is coercible to the Boolean value true,until the end of the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the callback function returns true for any element, otherwise returns false. |

## sort

```TypeScript
sort(compareFn?: (a: T, b: T) => int): this
```

Sorts the elements of a sparse array in place and returns the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-sort(compareFn?: (a: T, b: T) => int): this--><!--Device-SparseArray-sort(compareFn?: (a: T, b: T) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; int | 否 | A function used to determine the order of the elements. If not provided, elements are sorted by converting them to strings and comparing their UTF-16 code units in ascending order (default sort behavior). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The sorted sparse array. |

## splice

```TypeScript
splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

Changes the contents of the sparse array by removing or replacing existing elements and/or adding new elements in place.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>--><!--Device-SparseArray-splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The zero-based location in the sparse array from which to start removing elements. If start is negative, it is treated as length + start (e.g., -1 refers to the last element). If start is less than -length, it is clamped to 0. If start is greater than or equal to length, no elements are removed and new elements are added at the end. &lt;br&gt;The value should be an integer. |
| deleteCount | int | 是 | The number of elements to remove. If deleteCount is negative, it is clamped to 0 (no elements are removed). If deleteCount is greater than the number of elements from start to the end of the array, only the available elements are removed. &lt;br&gt;The value should be an integer. |
| items | T[] | 是 | Elements to insert into the sparse array in place of the deleted elements. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | A sparse array containing the elements that were deleted. |

## toReversed

```TypeScript
toReversed(): SparseArray<T>
```

Returns a new sparse array with the elements in reversed order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toReversed(): SparseArray<T>--><!--Device-SparseArray-toReversed(): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | A new sparse array with the elements in reversed order. |

## toSorted

```TypeScript
toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>
```

Returns a new sparse array with the elements sorted in ascending order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>--><!--Device-SparseArray-toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; int | 否 | A function used to determine the order of the elements. If not provided, elements are sorted by converting them to strings and comparing their UTF-16 code units in ascending order (default sort behavior). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |  |

## toSpliced

```TypeScript
toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

Returns a new sparse array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>--><!--Device-SparseArray-toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The zero-based location in the sparse array from which to start removing elements. If start is negative, it is treated as length + start (e.g., -1 refers to the last element). If start is less than -length, it is clamped to 0. If start is greater than or equal to length, no elements are removed and new elements are added at the end. If start is not an integer, it is truncated towards zero. &lt;br&gt;The value should be an integer. |
| deleteCount | int | 是 | The number of elements to remove. If deleteCount is negative, it is clamped to 0 (no elements are removed). If deleteCount is greater than the number of elements from start to the end of the array, only the available elements are removed. If deleteCount is not an integer, it is truncated towards zero. &lt;br&gt;The value should be an integer. |
| items | T[] | 是 | Elements to insert into the sparse array in place of the deleted elements. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | A new sparse array with the specified elements removed and/or replaced. |

## toString

```TypeScript
toString(): string
```

Returns a string representing the sparse array and its elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toString(): string--><!--Device-SparseArray-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Returns a string representing the elements of the sparse array separated by commas. |

## unshift

```TypeScript
unshift(...items: T[]): int
```

Inserts new elements at the start of a sparse array and returns the new length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-unshift(...items: T[]): int--><!--Device-SparseArray-unshift(...items: T[]): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 | Elements to insert at the start of the sparse array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The new length of the sparse array. |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterable of values in the sparse array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-values(): IterableIterator<T>--><!--Device-SparseArray-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | An iterable of values in the sparse array. |

## length

```TypeScript
get length(): int
```

Get the length of the sparse array.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-get length(): int--><!--Device-SparseArray-get length(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

