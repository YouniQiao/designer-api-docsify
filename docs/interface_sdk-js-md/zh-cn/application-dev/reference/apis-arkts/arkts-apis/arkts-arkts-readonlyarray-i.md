# ReadonlyArray

A read-only array that provides methods for reading elements.

**继承/实现关系：** ReadonlyArray extends [ConcatArray<T>](ConcatArray<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ReadonlyArray<out T> extends ConcatArray<T>--><!--Device-unnamed-export interface ReadonlyArray<out T> extends ConcatArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## concat

```TypeScript
concat(...items: FixedArray<ConcatArray<T>>): Array<T>
```

Combines two or more arrays.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-concat(...items: FixedArray<ConcatArray<T>>): Array<T>--><!--Device-ReadonlyArray-concat(...items: FixedArray<ConcatArray<T>>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;ConcatArray&lt;T&gt;&gt; | 是 | Arrays to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | New combined array. |

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

Returns a new iterator object that contains key-value pairs for each index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-entries(): IterableIterator<[int, T]>--><!--Device-ReadonlyArray-entries(): IterableIterator<[int, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; | New iterator object. |

## every

```TypeScript
every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

Tests whether all elements in the array pass the test implemented by the provided function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean--><!--Device-ReadonlyArray-every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if all elements pass the test, false otherwise. |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>
```

Creates a new array with all elements that pass the test implemented by the provided function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>--><!--Device-ReadonlyArray-filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | New array with elements that pass the test. |

## find

```TypeScript
find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

Returns the first element in the array that satisfies the provided testing function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined--><!--Device-ReadonlyArray-find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | First element satisfying the test, or undefined if none found. |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

Returns the index of the first element in the array that satisfies the provided testing function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int--><!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Index of first element satisfying the test, or -1 if none found. |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

Returns the last element in the array that satisfies the provided testing function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined--><!--Device-ReadonlyArray-findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Last element satisfying the test, or undefined if none found. |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

Returns the index of the last element in the array that satisfies the provided testing function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int--><!--Device-ReadonlyArray-findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Index of last element satisfying the test, or -1 if none found. |

## forEach

```TypeScript
forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void
```

Executes a provided function once for each array element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void--><!--Device-ReadonlyArray-forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; void | 是 | Function to execute for each element. |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

Determines whether an array includes a certain value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-includes(searchElement: T, fromIndex?: int): boolean--><!--Device-ReadonlyArray-includes(searchElement: T, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The value to search for. |
| fromIndex | int | 否 | The position in this array at which to begin searching. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the value is found, false otherwise. |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

Returns the first index at which a given element can be found in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-indexOf(searchElement: T, fromIndex?: int): int--><!--Device-ReadonlyArray-indexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The element to search for. |
| fromIndex | int | 否 | The position in this array at which to begin searching. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | First index of the element, or -1 if not found. |

## join

```TypeScript
join(separator?: string): string
```

Joins all elements of an array into a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-join(separator?: string): string--><!--Device-ReadonlyArray-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | Specifies a string to separate adjacent elements. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string with all array elements joined. |

## keys

```TypeScript
keys(): IterableIterator<int>
```

Returns a new iterator object that contains the keys for each index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-keys(): IterableIterator<int>--><!--Device-ReadonlyArray-keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | New iterator object containing keys. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T): int
```

Returns the last index at which a given element can be found in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-lastIndexOf(searchElement: T): int--><!--Device-ReadonlyArray-lastIndexOf(searchElement: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The element to search for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Last index of the element, or -1 if not found. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T, fromIndex?: int): int
```

Returns the last index at which a given element can be found in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-ReadonlyArray-lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The element to search for. |
| fromIndex | int | 否 | The position in this array at which to begin searching backward. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Last index of the element, or -1 if not found. |

## map

```TypeScript
map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>
```

Transforms each element of the array using a mapper function and returns a new array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>--><!--Device-ReadonlyArray-map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mapper | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | 是 | Function to transform each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | New array with transformed elements. |

## reduce

```TypeScript
reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

Applies a function against an accumulator to reduce the array to a single value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T--><!--Device-ReadonlyArray-reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; T | 是 | Function to execute on each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The value resulting from the reduction. |

## reduce

```TypeScript
reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

Applies a function against an accumulator to reduce the array to a single value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U--><!--Device-ReadonlyArray-reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | 是 | Function to execute on each element. |
| initialValue | U | 是 | Initial value for the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The value resulting from the reduction. |

## reduceRight

```TypeScript
reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

Applies a function against an accumulator to reduce the array from right to left to a single value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T--><!--Device-ReadonlyArray-reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; T | 是 | Function to execute on each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The value resulting from the reduction. |

## reduceRight

```TypeScript
reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

Applies a function against an accumulator to reduce the array from right to left to a single value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U--><!--Device-ReadonlyArray-reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | 是 | Function to execute on each element. |
| initialValue | U | 是 | Initial value for the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The value resulting from the reduction. |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

Returns a shallow copy of a portion of an array into a new array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-slice(start?: int, end?: int): Array<T>--><!--Device-ReadonlyArray-slice(start?: int, end?: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | Start index (inclusive). Defaults to 0. &lt;br&gt;The value should be an integer. |
| end | int | 否 | End index (exclusive). Defaults to array length. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | New array containing the extracted elements. |

## some

```TypeScript
some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

Tests whether at least one element in the array passes the test implemented by the provided function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean--><!--Device-ReadonlyArray-some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | Function to test each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if at least one element passes the test, false otherwise. |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns a new iterator object that contains the values for each index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-values(): IterableIterator<T>--><!--Device-ReadonlyArray-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | New iterator object containing values. |

