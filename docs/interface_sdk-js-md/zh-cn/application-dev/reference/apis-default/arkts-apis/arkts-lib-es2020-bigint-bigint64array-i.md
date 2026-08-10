# BigInt64Array

A typed array of 64-bit signed integer values. The contents are initialized to 0. If the requested number of bytes could not be allocated, an exception is raised.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface BigInt64Array--><!--Device-unnamed-interface BigInt64Array-End-->

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<bigint>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;bigint&gt; |  |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): this
```

Returns the this object after copying a section of the array identified by start and end to the same array starting at position target

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-copyWithin(target: number, start: number, end?: number): this--><!--Device-BigInt64Array-copyWithin(target: number, start: number, end?: number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | number | 是 |  |
| start | number | 是 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## entries

```TypeScript
entries(): IterableIterator<[number, bigint]>
```

Yields index, value pairs for every entry in the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-entries(): IterableIterator<[number, bigint]>--><!--Device-BigInt64Array-entries(): IterableIterator<[number, bigint]>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, bigint]&gt; |  |

## every

```TypeScript
every(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean
```

Determines whether all the members of an array satisfy the specified test.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-every(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean--><!--Device-BigInt64Array-every(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) =&gt; boolean | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## fill

```TypeScript
fill(value: bigint, start?: number, end?: number): this
```

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-fill(value: bigint, start?: number, end?: number): this--><!--Device-BigInt64Array-fill(value: bigint, start?: number, end?: number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 |  |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## filter

```TypeScript
filter(predicate: (value: bigint, index: number, array: BigInt64Array) => any, thisArg?: any): BigInt64Array
```

Returns the elements of an array that meet the condition specified in a callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-filter(predicate: (value: bigint, index: number, array: BigInt64Array) => any, thisArg?: any): BigInt64Array--><!--Device-BigInt64Array-filter(predicate: (value: bigint, index: number, array: BigInt64Array) => any, thisArg?: any): BigInt64Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) =&gt; any | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## find

```TypeScript
find(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): bigint | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-find(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): bigint | undefined--><!--Device-BigInt64Array-find(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): bigint | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) =&gt; boolean | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## findIndex

```TypeScript
findIndex(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-findIndex(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): number--><!--Device-BigInt64Array-findIndex(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) =&gt; boolean | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## forEach

```TypeScript
forEach(callbackfn: (value: bigint, index: number, array: BigInt64Array) => void, thisArg?: any): void
```

Performs the specified action for each element in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-forEach(callbackfn: (value: bigint, index: number, array: BigInt64Array) => void, thisArg?: any): void--><!--Device-BigInt64Array-forEach(callbackfn: (value: bigint, index: number, array: BigInt64Array) => void, thisArg?: any): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: bigint, index: number, array: BigInt64Array) =&gt; void | 是 |  |
| thisArg | any | 否 |  |

## includes

```TypeScript
includes(searchElement: bigint, fromIndex?: number): boolean
```

Determines whether an array includes a certain element, returning true or false as appropriate.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-includes(searchElement: bigint, fromIndex?: number): boolean--><!--Device-BigInt64Array-includes(searchElement: bigint, fromIndex?: number): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | bigint | 是 |  |
| fromIndex | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## indexOf

```TypeScript
indexOf(searchElement: bigint, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-indexOf(searchElement: bigint, fromIndex?: number): number--><!--Device-BigInt64Array-indexOf(searchElement: bigint, fromIndex?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | bigint | 是 |  |
| fromIndex | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-join(separator?: string): string--><!--Device-BigInt64Array-join(separator?: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## keys

```TypeScript
keys(): IterableIterator<number>
```

Yields each index in the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-keys(): IterableIterator<number>--><!--Device-BigInt64Array-keys(): IterableIterator<number>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt; |  |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: bigint, fromIndex?: number): number
```

Returns the index of the last occurrence of a value in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-lastIndexOf(searchElement: bigint, fromIndex?: number): number--><!--Device-BigInt64Array-lastIndexOf(searchElement: bigint, fromIndex?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | bigint | 是 |  |
| fromIndex | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## map

```TypeScript
map(callbackfn: (value: bigint, index: number, array: BigInt64Array) => bigint, thisArg?: any): BigInt64Array
```

Calls a defined callback function on each element of an array, and returns an array that contains the results.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-map(callbackfn: (value: bigint, index: number, array: BigInt64Array) => bigint, thisArg?: any): BigInt64Array--><!--Device-BigInt64Array-map(callbackfn: (value: bigint, index: number, array: BigInt64Array) => bigint, thisArg?: any): BigInt64Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: bigint, index: number, array: BigInt64Array) =&gt; bigint | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-reduce(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint--><!--Device-BigInt64Array-reduce(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) =&gt; bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## reduce

```TypeScript
reduce<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-reduce<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U--><!--Device-BigInt64Array-reduce<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) =&gt; U | 是 |  |
| initialValue | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-reduceRight(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint--><!--Device-BigInt64Array-reduceRight(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) =&gt; bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## reduceRight

```TypeScript
reduceRight<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U--><!--Device-BigInt64Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) =&gt; U | 是 |  |
| initialValue | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): this
```

Reverses the elements in the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-reverse(): this--><!--Device-BigInt64Array-reverse(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## set

```TypeScript
set(array: ArrayLike<bigint>, offset?: number): void
```

Sets a value or an array of values.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-set(array: ArrayLike<bigint>, offset?: number): void--><!--Device-BigInt64Array-set(array: ArrayLike<bigint>, offset?: number): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;bigint&gt; | 是 |  |
| offset | number | 否 |  |

## slice

```TypeScript
slice(start?: number, end?: number): BigInt64Array
```

Returns a section of an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-slice(start?: number, end?: number): BigInt64Array--><!--Device-BigInt64Array-slice(start?: number, end?: number): BigInt64Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## some

```TypeScript
some(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-some(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean--><!--Device-BigInt64Array-some(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) =&gt; boolean | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## sort

```TypeScript
sort(compareFn?: (a: bigint, b: bigint) => number | bigint): this
```

Sorts the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-sort(compareFn?: (a: bigint, b: bigint) => number | bigint): this--><!--Device-BigInt64Array-sort(compareFn?: (a: bigint, b: bigint) => number | bigint): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: bigint, b: bigint) =&gt; number \| bigint | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## subarray

```TypeScript
subarray(begin?: number, end?: number): BigInt64Array
```

Gets a new BigInt64Array view of the ArrayBuffer store for this array, referencing the elements at begin, inclusive, up to end, exclusive.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-subarray(begin?: number, end?: number): BigInt64Array--><!--Device-BigInt64Array-subarray(begin?: number, end?: number): BigInt64Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Converts the array to a string by using the current locale.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-toLocaleString(): string--><!--Device-BigInt64Array-toLocaleString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toString

```TypeScript
toString(): string
```

Returns a string representation of the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-toString(): string--><!--Device-BigInt64Array-toString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## valueOf

```TypeScript
valueOf(): BigInt64Array
```

Returns the primitive value of the specified object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-valueOf(): BigInt64Array--><!--Device-BigInt64Array-valueOf(): BigInt64Array-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## values

```TypeScript
values(): IterableIterator<bigint>
```

Yields each value in the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-values(): IterableIterator<bigint>--><!--Device-BigInt64Array-values(): IterableIterator<bigint>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;bigint&gt; |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-readonly BYTES_PER_ELEMENT: number--><!--Device-BigInt64Array-readonly BYTES_PER_ELEMENT: number-End-->

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "BigInt64Array"
```

**类型：** "BigInt64Array"

**ArkTS模式：** 仅支持ArkTS-Dyn

## [index: number]

```TypeScript
[index: number]: bigint
```

**类型：** bigint

**ArkTS模式：** 仅支持ArkTS-Dyn

## buffer

```TypeScript
readonly buffer: ArrayBufferLike
```

The ArrayBuffer instance referenced by the array.

**类型：** [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md)

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-readonly buffer: ArrayBufferLike--><!--Device-BigInt64Array-readonly buffer: ArrayBufferLike-End-->

## byteLength

```TypeScript
readonly byteLength: number
```

The length in bytes of the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-readonly byteLength: number--><!--Device-BigInt64Array-readonly byteLength: number-End-->

## byteOffset

```TypeScript
readonly byteOffset: number
```

The offset in bytes of the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-readonly byteOffset: number--><!--Device-BigInt64Array-readonly byteOffset: number-End-->

## length

```TypeScript
readonly length: number
```

The length of the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt64Array-readonly length: number--><!--Device-BigInt64Array-readonly length: number-End-->

