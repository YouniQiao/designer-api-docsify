# Uint8ClampedArray

A typed array of 8-bit unsigned integer (clamped) values. The contents are initialized to 0.If the requested number of bytes could not be allocated an exception is raised.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface Uint8ClampedArray--><!--Device-unnamed-interface Uint8ClampedArray-End-->

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): this
```

Returns the this object after copying a section of the array identified by start and end to the same array starting at position target

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-copyWithin(target: number, start: number, end?: number): this--><!--Device-Uint8ClampedArray-copyWithin(target: number, start: number, end?: number): this-End-->

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

## every

```TypeScript
every(predicate: (value: number, index: number, array: Uint8ClampedArray) => unknown, thisArg?: any): boolean
```

Determines whether all the members of an array satisfy the specified test.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-every(predicate: (value: number, index: number, array: Uint8ClampedArray) => unknown, thisArg?: any): boolean--><!--Device-Uint8ClampedArray-every(predicate: (value: number, index: number, array: Uint8ClampedArray) => unknown, thisArg?: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, array: Uint8ClampedArray) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): this
```

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-fill(value: number, start?: number, end?: number): this--><!--Device-Uint8ClampedArray-fill(value: number, start?: number, end?: number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 |  |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## filter

```TypeScript
filter(predicate: (value: number, index: number, array: Uint8ClampedArray) => any, thisArg?: any): Uint8ClampedArray
```

Returns the elements of an array that meet the condition specified in a callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-filter(predicate: (value: number, index: number, array: Uint8ClampedArray) => any, thisArg?: any): Uint8ClampedArray--><!--Device-Uint8ClampedArray-filter(predicate: (value: number, index: number, array: Uint8ClampedArray) => any, thisArg?: any): Uint8ClampedArray-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, array: Uint8ClampedArray) =&gt; any | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## find

```TypeScript
find(predicate: (value: number, index: number, obj: Uint8ClampedArray) => boolean, thisArg?: any): number | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-find(predicate: (value: number, index: number, obj: Uint8ClampedArray) => boolean, thisArg?: any): number | undefined--><!--Device-Uint8ClampedArray-find(predicate: (value: number, index: number, obj: Uint8ClampedArray) => boolean, thisArg?: any): number | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, obj: Uint8ClampedArray) =&gt; boolean | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## findIndex

```TypeScript
findIndex(predicate: (value: number, index: number, obj: Uint8ClampedArray) => boolean, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-findIndex(predicate: (value: number, index: number, obj: Uint8ClampedArray) => boolean, thisArg?: any): number--><!--Device-Uint8ClampedArray-findIndex(predicate: (value: number, index: number, obj: Uint8ClampedArray) => boolean, thisArg?: any): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, obj: Uint8ClampedArray) =&gt; boolean | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## forEach

```TypeScript
forEach(callbackfn: (value: number, index: number, array: Uint8ClampedArray) => void, thisArg?: any): void
```

Performs the specified action for each element in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-forEach(callbackfn: (value: number, index: number, array: Uint8ClampedArray) => void, thisArg?: any): void--><!--Device-Uint8ClampedArray-forEach(callbackfn: (value: number, index: number, array: Uint8ClampedArray) => void, thisArg?: any): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: number, index: number, array: Uint8ClampedArray) =&gt; void | 是 |  |
| thisArg | any | 否 |  |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8ClampedArray-indexOf(searchElement: number, fromIndex?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | number | 是 |  |
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

<!--Device-Uint8ClampedArray-join(separator?: string): string--><!--Device-Uint8ClampedArray-join(separator?: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the last occurrence of a value in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8ClampedArray-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | number | 是 |  |
| fromIndex | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## map

```TypeScript
map(callbackfn: (value: number, index: number, array: Uint8ClampedArray) => number, thisArg?: any): Uint8ClampedArray
```

Calls a defined callback function on each element of an array, and returns an array that contains the results.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-map(callbackfn: (value: number, index: number, array: Uint8ClampedArray) => number, thisArg?: any): Uint8ClampedArray--><!--Device-Uint8ClampedArray-map(callbackfn: (value: number, index: number, array: Uint8ClampedArray) => number, thisArg?: any): Uint8ClampedArray-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: number, index: number, array: Uint8ClampedArray) =&gt; number | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number): number
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number): number--><!--Device-Uint8ClampedArray-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) =&gt; number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number, initialValue: number): number
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) =&gt; number | 是 |  |
| initialValue | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## reduce

```TypeScript
reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => U, initialValue: U): U--><!--Device-Uint8ClampedArray-reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => U, initialValue: U): U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) =&gt; U | 是 |  |
| initialValue | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number): number
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number): number--><!--Device-Uint8ClampedArray-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) =&gt; number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => number, initialValue: number): number
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8ClampedArray) =&gt; number | 是 |  |
| initialValue | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## reduceRight

```TypeScript
reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => U, initialValue: U): U--><!--Device-Uint8ClampedArray-reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) => U, initialValue: U): U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: number, currentIndex: number, array: Uint8ClampedArray) =&gt; U | 是 |  |
| initialValue | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): Uint8ClampedArray
```

Reverses the elements in an Array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-reverse(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-reverse(): Uint8ClampedArray-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

Sets a value or an array of values.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint8ClampedArray-set(array: ArrayLike<number>, offset?: number): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;number&gt; | 是 |  |
| offset | number | 否 |  |

## slice

```TypeScript
slice(start?: number, end?: number): Uint8ClampedArray
```

Returns a section of an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-slice(start?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-slice(start?: number, end?: number): Uint8ClampedArray-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## some

```TypeScript
some(predicate: (value: number, index: number, array: Uint8ClampedArray) => unknown, thisArg?: any): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-some(predicate: (value: number, index: number, array: Uint8ClampedArray) => unknown, thisArg?: any): boolean--><!--Device-Uint8ClampedArray-some(predicate: (value: number, index: number, array: Uint8ClampedArray) => unknown, thisArg?: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, array: Uint8ClampedArray) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## sort

```TypeScript
sort(compareFn?: (a: number, b: number) => number): this
```

Sorts an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-sort(compareFn?: (a: number, b: number) => number): this--><!--Device-Uint8ClampedArray-sort(compareFn?: (a: number, b: number) => number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: number, b: number) =&gt; number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint8ClampedArray
```

Gets a new Uint8ClampedArray view of the ArrayBuffer store for this array, referencing the elements at begin, inclusive, up to end, exclusive.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-subarray(begin?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-subarray(begin?: number, end?: number): Uint8ClampedArray-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Converts a number to a string by using the current locale.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-toLocaleString(): string--><!--Device-Uint8ClampedArray-toLocaleString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toString

```TypeScript
toString(): string
```

Returns a string representation of an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-toString(): string--><!--Device-Uint8ClampedArray-toString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## valueOf

```TypeScript
valueOf(): Uint8ClampedArray
```

Returns the primitive value of the specified object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-valueOf(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-valueOf(): Uint8ClampedArray-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8ClampedArray-readonly BYTES_PER_ELEMENT: number-End-->

## [index: number]

```TypeScript
[index: number]: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

## buffer

```TypeScript
readonly buffer: ArrayBufferLike
```

The ArrayBuffer instance referenced by the array.

**类型：** [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md)

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-readonly buffer: ArrayBufferLike--><!--Device-Uint8ClampedArray-readonly buffer: ArrayBufferLike-End-->

## byteLength

```TypeScript
readonly byteLength: number
```

The length in bytes of the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-readonly byteLength: number--><!--Device-Uint8ClampedArray-readonly byteLength: number-End-->

## byteOffset

```TypeScript
readonly byteOffset: number
```

The offset in bytes of the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-readonly byteOffset: number--><!--Device-Uint8ClampedArray-readonly byteOffset: number-End-->

## length

```TypeScript
readonly length: number
```

The length of the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Uint8ClampedArray-readonly length: number--><!--Device-Uint8ClampedArray-readonly length: number-End-->

