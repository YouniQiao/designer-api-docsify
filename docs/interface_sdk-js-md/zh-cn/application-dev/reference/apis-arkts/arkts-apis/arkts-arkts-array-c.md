# Array

Represents a JS API-compatible Array.

**继承/实现关系：** Array implements [ReadonlyArray<T>](ReadonlyArray<T>), [Iterable<T>](Iterable<T>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Array<T> implements ReadonlyArray<T>, Iterable<T>--><!--Device-unnamed-export class Array<T> implements ReadonlyArray<T>, Iterable<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(idx: int): T
```

Get the element at the specified index.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-$_get(idx: int): T--><!--Device-Array-$_get(idx: int): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| idx | int | 是 | The index of the element to get. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The element at the specified index. |

## $_invoke

```TypeScript
static $_invoke<T>(...items: T[]): Array<T>
```

Creates a new instance of Array with the given elements.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static $_invoke<T>(...items: T[]): Array<T>--><!--Device-Array-static $_invoke<T>(...items: T[]): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 | The elements to initialize the array with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array instance with the given elements. |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns an iterator over all values

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-$_iterator(): IterableIterator<T>--><!--Device-Array-$_iterator(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | An iterator over all values. |

## $_set

```TypeScript
$_set(idx: int, val: T): void
```

Set the element at the specified index.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-$_set(idx: int, val: T): void--><!--Device-Array-$_set(idx: int, val: T): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| idx | int | 是 | The index of the element to set. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| val | T | 是 | The value to set at the specified index. |

## at

```TypeScript
public at(index: int): T
```

Takes an integer value and returns the item at that index, allowing for positive and negative integers.Negative integers count back from the last item in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public at(index: int): T--><!--Device-Array-public at(index: int): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | Zero-based index of the array element to be returned. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The element at the given index. |

## concat

```TypeScript
public concat(...items: FixedArray<ConcatArray<T>>): Array<T>
```

Creates a new `Array` by merging this `Array` instance with given arrays and/or values.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public concat(...items: FixedArray<ConcatArray<T>>): Array<T>--><!--Device-Array-public concat(...items: FixedArray<ConcatArray<T>>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;ConcatArray&lt;T&gt;&gt; | 是 | Arrays and/or values to concatenate into a new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array instance. |

## constructor

```TypeScript
public constructor()
```

Creates a new empty instance of Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public constructor()--><!--Device-Array-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(first: T, ...d: T[])
```

Creates a new instance of Array with the given elements.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-constructor(first: T, ...d: T[])--><!--Device-Array-constructor(first: T, ...d: T[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | T | 是 | The first element of the array. |
| d | T[] | 是 | The rest of the elements to initialize the array with. |

## constructor

```TypeScript
constructor(arrayLen: int, initializer: (index: int) => T)
```

Creates a new instance of Array with a specific length and initializes each element using a function.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-constructor(arrayLen: int, initializer: (index: int) => T)--><!--Device-Array-constructor(arrayLen: int, initializer: (index: int) => T)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLen | int | 是 | The amount of elements in the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| initializer | (index: int) =&gt; T | 是 | A function that generates an element for a given index. |

## copyWithin

```TypeScript
public copyWithin(target: int): this
```

Makes a shallow copy of the Array part to another location in the same Array and returns it without modifying its length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public copyWithin(target: int): this--><!--Device-Array-public copyWithin(target: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | Zero-based index at which to copy the sequence to. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The modified array. |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int): this
```

Makes a shallow copy of the Array part to another location in the same Array and returns it without modifying its length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public copyWithin(target: int, start: int): this--><!--Device-Array-public copyWithin(target: int, start: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | Zero-based index at which to copy the sequence to. &lt;br&gt;The value should be an integer. |
| start | int | 是 | Zero-based index at which to start copying elements from. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The modified array. |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): this
```

Makes a shallow copy of the Array part to another location in the same Array and returns it without modifying its length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public copyWithin(target: int, start: int, end?: int): this--><!--Device-Array-public copyWithin(target: int, start: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | Zero-based index at which to copy the sequence to. &lt;br&gt;The value should be an integer. |
| start | int | 是 | Zero-based index at which to start copying elements from. &lt;br&gt;The value should be an integer. |
| end | int | 否 | Zero-based index at which to end copying elements from. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The modified array. |

## create

```TypeScript
public static create<T>(arrayLength: int, initialValue: T): Array<T>
```

Creates a new Array of the specified length, filled with the specified initial value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public static create<T>(arrayLength: int, initialValue: T): Array<T>--><!--Device-Array-public static create<T>(arrayLength: int, initialValue: T): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLength | int | 是 | The amount of elements in the new array. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| initialValue | T | 是 | The value to fill the array with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array instance filled with the initial value. |

## entries

```TypeScript
public entries(): IterableIterator<[int, T]>
```

Returns a new Array Iterator object that contains the key/value pairs for each index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public entries(): IterableIterator<[int, T]>--><!--Device-Array-public entries(): IterableIterator<[int, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; | A new Array Iterator object. |

## every

```TypeScript
public every(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean
```

Determines whether all the members of an array satisfy the specified test.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public every(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean--><!--Device-Array-public every(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The every method calls the predicate function for each element in the array until the predicate returns a value which is coercible to the Boolean value false, or until the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the predicate returns true for all elements in the array; otherwise, false. |

## extendTo

```TypeScript
public extendTo(arrayLength: int, initialValue: T): void
```

Extends the Array with new elements up to the specified length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public extendTo(arrayLength: int, initialValue: T): void--><!--Device-Array-public extendTo(arrayLength: int, initialValue: T): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLength | int | 是 | The new length of the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| initialValue | T | 是 | The initial value for the added elements. |

## fill

```TypeScript
public fill(value: T, start?: int, end?: int): this
```

Changes all elements in the Array to a static value, from a start index to an end index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public fill(value: T, start?: int, end?: int): this--><!--Device-Array-public fill(value: T, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | The value to fill the array with. |
| start | int | 否 | The index at which to start filling (optional).If start is greater than or equal to the array length, no elements are filled. If start is negative, it is treated as 0. &lt;br&gt;The value should be an integer. |
| end | int | 否 | The index at which to end filling (optional, not included). If end is greater than the array length, the array length is used as the end index. If end is negative, it is treated as 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The modified array. |

## filter

```TypeScript
public filter(predicate: (value: T, index: int, array: Array<T>) => boolean): Array<T>
```

Returns the elements of an array that meet the condition specified in a callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public filter(predicate: (value: T, index: int, array: Array<T>) => boolean): Array<T>--><!--Device-Array-public filter(predicate: (value: T, index: int, array: Array<T>) => boolean): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new array with the elements that pass the test. |

## find

```TypeScript
public find(predicate: (value: T, index: int, array: Array<T>) => boolean): T | undefined
```

Iterates the array and returns the value of the first element that satisfies the provided testing function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public find(predicate: (value: T, index: int, array: Array<T>) => boolean): T | undefined--><!--Device-Array-public find(predicate: (value: T, index: int, array: Array<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function to execute on each value in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The value of the first element that satisfies the provided testing function; otherwise, undefined. |

## findIndex

```TypeScript
public findIndex(predicate: (value: T, index: int, array: Array<T>) => boolean): int
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public findIndex(predicate: (value: T, index: int, array: Array<T>) => boolean): int--><!--Device-Array-public findIndex(predicate: (value: T, index: int, array: Array<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function to execute on each value in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |

## findLast

```TypeScript
public findLast(predicate: (elem: T, index: int, array: Array<T>) => boolean): T | undefined
```

Iterates the array in reverse order and returns the value of the first element that satisfies the provided testing function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public findLast(predicate: (elem: T, index: int, array: Array<T>) => boolean): T | undefined--><!--Device-Array-public findLast(predicate: (elem: T, index: int, array: Array<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (elem: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function to execute on each value in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The value of the element if found; otherwise, undefined. |

## findLastIndex

```TypeScript
public findLastIndex(predicate: (element: T, index: int, array: Array<T>) => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public findLastIndex(predicate: (element: T, index: int, array: Array<T>) => boolean): int--><!--Device-Array-public findLastIndex(predicate: (element: T, index: int, array: Array<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function to execute on each value in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |

## flat

```TypeScript
public flat<U = T>(depth: int): Array<U>
```

Creates a new Array with all sub-array elements concatenated into it recursively up to the specified depth.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public flat<U = T>(depth: int): Array<U>--><!--Device-Array-public flat<U = T>(depth: int): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| depth | int | 是 | The depth level specifying how deep a nested array structure should be flattened. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | A new array with the sub-array elements concatenated into it. |

## flat

```TypeScript
public flat<U = T>(): Array<U>
```

Creates a new Array with all sub-array elements concatenated into it recursively with a default depth of 1.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public flat<U = T>(): Array<U>--><!--Device-Array-public flat<U = T>(): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | A new array with the sub-array elements concatenated into it. |

## flatMap

```TypeScript
public flatMap<U=T>(fn: (v: T, k: int, arr: Array<T>) => U | ReadonlyArray<U>): Array<U>
```

Calls a defined callback function on each element of an array. Then, flattens the result into a new array.This is identical to a map() followed by a flat() with depth 1.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public flatMap<U=T>(fn: (v: T, k: int, arr: Array<T>) => U | ReadonlyArray<U>): Array<U>--><!--Device-Array-public flatMap<U=T>(fn: (v: T, k: int, arr: Array<T>) => U | ReadonlyArray<U>): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (v: T, k: int, arr: Array&lt;T&gt;) =&gt; U \| ReadonlyArray&lt;U&gt; | 是 | A function that produces an element of the new Array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | A new array with each element being the result of the callback function and flattened. |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: int, array: Array<T>) => void): void
```

Performs the specified action for each element in an array.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-forEach(callbackfn: (value: T, index: int, array: Array<T>) => void): void--><!--Device-Array-forEach(callbackfn: (value: T, index: int, array: Array<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: Array&lt;T&gt;) =&gt; void | 是 | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array. |

## from

```TypeScript
static from<T>(arr: FixedArray<T>): Array<T>
```

Creates a new `Array` instance from a `FixedArray`.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static from<T>(arr: FixedArray<T>): Array<T>--><!--Device-Array-static from<T>(arr: FixedArray<T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;T&gt; | 是 | The source primitive array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array instance containing the elements from the source array. |

## from

```TypeScript
static from<T>(arr: ArrayLike<T>): Array<T>
```

Creates a new `Array` instance from an `ArrayLike` object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static from<T>(arr: ArrayLike<T>): Array<T>--><!--Device-Array-static from<T>(arr: ArrayLike<T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 | An array-like object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array instance containing the elements from the array-like object. |

## from

```TypeScript
static from<T>(iterable: ArrayLike<T> | Iterable<T>): Array<T>
```

Creates a new `Array` instance from an iterable or array-like object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static from<T>(iterable: ArrayLike<T> | Iterable<T>): Array<T>--><!--Device-Array-static from<T>(iterable: ArrayLike<T> | Iterable<T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterable | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; \| Iterable&lt;T&gt; | 是 | An iterable or array-like object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array instance containing the elements from the iterable. |

## from

```TypeScript
static from<T, U>(values: FixedArray<T>, mapfn: (v: T, k: int) => U): Array<U>
```

Creates a new `Array` instance from a `FixedArray` and applies a mapping function to each element.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static from<T, U>(values: FixedArray<T>, mapfn: (v: T, k: int) => U): Array<U>--><!--Device-Array-static from<T, U>(values: FixedArray<T>, mapfn: (v: T, k: int) => U): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | FixedArray&lt;T&gt; | 是 | The source primitive array. |
| mapfn | (v: T, k: int) =&gt; U | 是 | A mapping function to call on every element of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | A new Array instance with the mapped values. |

## from

```TypeScript
static from<T, U>(iterable: ArrayLike<T> | Iterable<T>, mapfn: (v: T, k: int) => U): Array<U>
```

Creates a new `Array` instance from an iterable object, applying a mapping function to each element.Every value to be added to the array is first passed through this function, and `mapfn`'s return value is added to the array instead.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static from<T, U>(iterable: ArrayLike<T> | Iterable<T>, mapfn: (v: T, k: int) => U): Array<U>--><!--Device-Array-static from<T, U>(iterable: ArrayLike<T> | Iterable<T>, mapfn: (v: T, k: int) => U): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterable | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; \| Iterable&lt;T&gt; | 是 | An iterable or array-like object to convert to an array. |
| mapfn | (v: T, k: int) =&gt; U | 是 | A mapping function to call on every element of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | A new Array instance with the mapped values. |

## includes

```TypeScript
public includes(val: T, fromIndex?: int): boolean
```

Determines whether an array includes a certain value among its entries, returning true or false as appropriate.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public includes(val: T, fromIndex?: int): boolean--><!--Device-Array-public includes(val: T, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | T | 是 | The value to search for. |
| fromIndex | int | 否 | The position in this array at which to begin searching for value. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the value is found, false otherwise. |

## indexOf

```TypeScript
public indexOf(val: T): int
```

Returns the first index at which a given element can be found in the array, or -1 if it is not present.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public indexOf(val: T): int--><!--Device-Array-public indexOf(val: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | T | 是 | The element to locate in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The first index of the element in the array; -1 if not found. |

## indexOf

```TypeScript
public indexOf(val: T, fromIndex?: int): int
```

Returns the first index at which a given element can be found in the array, or -1 if it is not present.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public indexOf(val: T, fromIndex?: int): int--><!--Device-Array-public indexOf(val: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | T | 是 | The element to locate in the array. |
| fromIndex | int | 否 | The index to start the search at. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The first index of the element in the array; -1 if not found. |

## isArray

```TypeScript
static isArray(o: Any): boolean
```

Checks whether the passed value is an Array.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-static isArray(o: Any): boolean--><!--Device-Array-static isArray(o: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | Any | 是 | The value to be checked. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the value is an Array; otherwise, false. |

## join

```TypeScript
public join(sep?: string): string
```

Creates and returns a new string by concatenating all of the elements in an `Array`, separated by a specified separator string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public join(sep?: string): string--><!--Device-Array-public join(sep?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sep | string | 否 | A string to separate each pair of adjacent elements of the array. If omitted, the array elements are separated with a comma. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string with all array elements joined. |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

Returns a new Array Iterator object that contains the keys for each index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public keys(): IterableIterator<int>--><!--Device-Array-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | A new Array Iterator object. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: T): int
```

Returns the last index at which a given element can be found in the array, or -1 if it is not present. The array is searched backwards.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public lastIndexOf(searchElement: T): int--><!--Device-Array-public lastIndexOf(searchElement: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The element to locate in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The last index of the element in the array; -1 if not found. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: T, fromIndex?: int): int
```

Returns the last index at which a given element can be found in the array, or -1 if it is not present. The array is searched backwards, starting at fromIndex.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-Array-public lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | The element to locate in the array. |
| fromIndex | int | 否 | The index at which to start searching backwards. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The last index of the element in the array; -1 if not found. |

## map

```TypeScript
public map<U>(callbackfn: (value: T, index: int, array: Array<T>) => U): Array<U>
```

Creates a new array populated with the results of calling a provided function on every element in the calling array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public map<U>(callbackfn: (value: T, index: int, array: Array<T>) => U): Array<U>--><!--Device-Array-public map<U>(callbackfn: (value: T, index: int, array: Array<T>) => U): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: Array&lt;T&gt;) =&gt; U | 是 | Function that is called for every element of the array. Each time callbackfn executes, the returned value is added to the new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | A new array with each element being the result of the callback function. |

## pop

```TypeScript
public pop(): T | undefined
```

Removes the last element from an array and returns that element. This method changes the length of the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public pop(): T | undefined--><!--Device-Array-public pop(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The removed element from the array; undefined if the array is empty. |

## push

```TypeScript
public push(...val: T[]): int
```

Adds the specified elements to the end of an array and returns the new length of the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public push(...val: T[]): int--><!--Device-Array-public push(...val: T[]): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | T[] | 是 | The elements to add to the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The new length of the array upon which the method was called. |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T--><!--Device-Array-public reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: Array&lt;T&gt;) =&gt; T | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The accumulated result. |

## reduce

```TypeScript
public reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,
                         initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,                         initialValue: U): U--><!--Device-Array-public reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,                         initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: Array&lt;T&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |

## reduceRight

```TypeScript
public reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,
                          initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,                          initialValue: U): U--><!--Device-Array-public reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,                          initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: Array&lt;T&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T--><!--Device-Array-public reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: Array&lt;T&gt;) =&gt; T | 是 | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The accumulated result. |

## reverse

```TypeScript
public reverse(): this
```

Reverses an array in place. The first array element becomes the last, and the last array element becomes the first.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public reverse(): this--><!--Device-Array-public reverse(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The reversed array. |

## shift

```TypeScript
public shift(): T | undefined
```

Removes the first element from an array and returns that removed element.This method changes the length of the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public shift(): T | undefined--><!--Device-Array-public shift(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The removed element from the array; undefined if the array is empty. |

## shrinkTo

```TypeScript
public shrinkTo(arrayLength: int): void
```

Shrinks the Array to the specified length. Elements beyond the new length are removed.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public shrinkTo(arrayLength: int): void--><!--Device-Array-public shrinkTo(arrayLength: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLength | int | 是 | The length at which to shrink the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |

## slice

```TypeScript
public slice(start: int): Array<T>
```

Returns a copy of a section of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public slice(start: int): Array<T>--><!--Device-Array-public slice(start: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The beginning index of the specified portion of the array. If start is greater than or equal to the array length, an empty array is returned. If start is negative, it is treated as length + start. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array object containing the extracted elements. |

## slice

```TypeScript
public slice(start?: int, end?: int): Array<T>
```

Returns a copy of a section of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public slice(start?: int, end?: int): Array<T>--><!--Device-Array-public slice(start?: int, end?: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | The beginning index of the specified portion of the array.If start is greater than or equal to the array length, an empty array is returned. If start is negative, it is treated as length + start. &lt;br&gt;The value should be an integer. |
| end | int | 否 | The end index of the specified portion of the array. If end is greater than the array length,the array length is used as the end index. If end is negative, it is treated as 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new Array object containing the extracted elements. |

## some

```TypeScript
public some(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public some(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean--><!--Device-Array-public some(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: Array&lt;T&gt;) =&gt; boolean | 是 | A function that accepts up to three arguments. The some method calls the predicate function for each element in the array until the predicate returns a value which is coercible to the Boolean value true, or until the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the predicate returns true for at least one element in the array; otherwise, false. |

## sort

```TypeScript
public sort(comparator?: (a: T, b: T) => int): this
```

Sorts the elements of an array in place and returns the reference to the same array, now sorted.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public sort(comparator?: (a: T, b: T) => int): this--><!--Device-Array-public sort(comparator?: (a: T, b: T) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| comparator | (a: T, b: T) =&gt; int | 否 | Optional. A function that defines the sort order. If omitted, the array is sorted according to each character's Unicode code point value, according to the string conversion of each element. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The sorted array. |

## splice

```TypeScript
public splice(start: int, del: int | undefined, ...items: T[]): Array<T>
```

Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public splice(start: int, del: int | undefined, ...items: T[]): Array<T>--><!--Device-Array-public splice(start: int, del: int | undefined, ...items: T[]): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The index at which to start changing the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| del | int \| undefined | 是 | The number of items to remove after the start index, If the input is undefined, it means 0, and no elements are deleted. |
| items | T[] | 是 | The elements to add to the array, beginning from start. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements. |

## splice

```TypeScript
public splice(start: int): Array<T>
```

Changes the contents of an array by removing existing elements in place from the start index to the end.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public splice(start: int): Array<T>--><!--Device-Array-public splice(start: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | An array containing the deleted elements. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | 否 | An object with configuration properties. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the elements of the array. |

## toReversed

```TypeScript
public toReversed(): Array<T>
```

Returns a new array with the elements in reversed order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toReversed(): Array<T>--><!--Device-Array-public toReversed(): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new reversed array. |

## toSorted

```TypeScript
public toSorted(): Array<T>
```

Sort in ascending order， Returns a new array with the elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toSorted(): Array<T>--><!--Device-Array-public toSorted(): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new sorted array. |

## toSorted

```TypeScript
public toSorted(comparator: (a: T, b: T) => int): Array<T>
```

Returns a new array with the elements sorted using the provided comparator function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toSorted(comparator: (a: T, b: T) => int): Array<T>--><!--Device-Array-public toSorted(comparator: (a: T, b: T) => int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| comparator | (a: T, b: T) =&gt; int | 是 | A function that defines the sort order. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new sorted array. |

## toSpliced

```TypeScript
public toSpliced(start: int): Array<T>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toSpliced(start: int): Array<T>--><!--Device-Array-public toSpliced(start: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new array with the changes applied. |

## toSpliced

```TypeScript
public toSpliced(start: int, del: int, ...items: FixedArray<T>): Array<T>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toSpliced(start: int, del: int, ...items: FixedArray<T>): Array<T>--><!--Device-Array-public toSpliced(start: int, del: int, ...items: FixedArray<T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| items | FixedArray&lt;T&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new array with the changes applied. |

## toSpliced

```TypeScript
public toSpliced(start?: int, del?: int): Array<T>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toSpliced(start?: int, del?: int): Array<T>--><!--Device-Array-public toSpliced(start?: int, del?: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new array with the changes applied. |

## toString

```TypeScript
public toString(): string
```

Returns a string representing the specified array and its elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public toString(): string--><!--Device-Array-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the array. |

## unshift

```TypeScript
public unshift(...values: T[]): int
```

Adds the specified elements to the beginning of an Array and returns the new length of the Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public unshift(...values: T[]): int--><!--Device-Array-public unshift(...values: T[]): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | T[] | 是 | The elements to add to the front of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The new length of the array. |

## values

```TypeScript
public values(): IterableIterator<T>
```

Returns a new Array Iterator object that contains the values for each index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public values(): IterableIterator<T>--><!--Device-Array-public values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | A new Array Iterator object. |

## with

```TypeScript
public with(index: int, value: T): Array<T>
```

Returns a new Array with the element at the given index replaced with the given value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-public with(index: int, value: T): Array<T>--><!--Device-Array-public with(index: int, value: T): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The zero-based index at which to replace the value. &lt;br&gt;The value should be an integer. |
| value | T | 是 | The new value to insert at the given index. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new array with the element replaced. |

## length

```TypeScript
set length(newLen: int)
```

Set the length of the array.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Array-set length(newLen: int)--><!--Device-Array-set length(newLen: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

