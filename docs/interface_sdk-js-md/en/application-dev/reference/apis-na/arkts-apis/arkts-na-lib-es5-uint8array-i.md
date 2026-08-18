# Uint8Array

A typed array of 8-bit unsigned integer values. The contents are initialized to 0. If the requested number of bytes could not be allocated an exception is raised.

**Since:** -1

<!--Device-unnamed-interface Uint8Array--><!--Device-unnamed-interface Uint8Array-End-->

## Modules to Import

```TypeScript
```

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): this
```

Returns the this object after copying a section of the array identified by start and end to the same array starting at position target

**Since:** -1

<!--Device-Uint8Array-copyWithin(target: number, start: number, end?: number): this--><!--Device-Uint8Array-copyWithin(target: number, start: number, end?: number): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | number | Yes |  |
| start | number | Yes |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## every

```TypeScript
every(predicate: (value: number, index: number, array: Uint8Array) => unknown, thisArg?: any): boolean
```

Determines whether all the members of an array satisfy the specified test.

**Since:** -1

<!--Device-Uint8Array-every(predicate: (value: number, index: number, array: Uint8Array) => unknown, thisArg?: any): boolean--><!--Device-Uint8Array-every(predicate: (value: number, index: number, array: Uint8Array) => unknown, thisArg?: any): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, array: Uint8Array) =&gt; unknown | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): this
```

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

**Since:** -1

<!--Device-Uint8Array-fill(value: number, start?: number, end?: number): this--><!--Device-Uint8Array-fill(value: number, start?: number, end?: number): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes |  |
| start | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## filter

```TypeScript
filter(predicate: (value: number, index: number, array: Uint8Array) => any, thisArg?: any): Uint8Array
```

Returns the elements of an array that meet the condition specified in a callback function.

**Since:** -1

<!--Device-Uint8Array-filter(predicate: (value: number, index: number, array: Uint8Array) => any, thisArg?: any): Uint8Array--><!--Device-Uint8Array-filter(predicate: (value: number, index: number, array: Uint8Array) => any, thisArg?: any): Uint8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, array: Uint8Array) =&gt; any | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array |  |

## find

```TypeScript
find(predicate: (value: number, index: number, obj: Uint8Array) => boolean, thisArg?: any): number | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**Since:** -1

<!--Device-Uint8Array-find(predicate: (value: number, index: number, obj: Uint8Array) => boolean, thisArg?: any): number | undefined--><!--Device-Uint8Array-find(predicate: (value: number, index: number, obj: Uint8Array) => boolean, thisArg?: any): number | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, obj: Uint8Array) =&gt; boolean | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## findIndex

```TypeScript
findIndex(predicate: (value: number, index: number, obj: Uint8Array) => boolean, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise.

**Since:** -1

<!--Device-Uint8Array-findIndex(predicate: (value: number, index: number, obj: Uint8Array) => boolean, thisArg?: any): number--><!--Device-Uint8Array-findIndex(predicate: (value: number, index: number, obj: Uint8Array) => boolean, thisArg?: any): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, obj: Uint8Array) =&gt; boolean | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## forEach

```TypeScript
forEach(callbackfn: (value: number, index: number, array: Uint8Array) => void, thisArg?: any): void
```

Performs the specified action for each element in an array.

**Since:** -1

<!--Device-Uint8Array-forEach(callbackfn: (value: number, index: number, array: Uint8Array) => void, thisArg?: any): void--><!--Device-Uint8Array-forEach(callbackfn: (value: number, index: number, array: Uint8Array) => void, thisArg?: any): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: number, index: number, array: Uint8Array) =&gt; void | Yes |  |
| thisArg | any | No |  |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in an array.

**Since:** -1

<!--Device-Uint8Array-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8Array-indexOf(searchElement: number, fromIndex?: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | number | Yes |  |
| fromIndex | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string.

**Since:** -1

<!--Device-Uint8Array-join(separator?: string): string--><!--Device-Uint8Array-join(separator?: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the last occurrence of a value in an array.

**Since:** -1

<!--Device-Uint8Array-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8Array-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | number | Yes |  |
| fromIndex | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## map

```TypeScript
map(callbackfn: (value: number, index: number, array: Uint8Array) => number, thisArg?: any): Uint8Array
```

Calls a defined callback function on each element of an array, and returns an array that contains the results.

**Since:** -1

<!--Device-Uint8Array-map(callbackfn: (value: number, index: number, array: Uint8Array) => number, thisArg?: any): Uint8Array--><!--Device-Uint8Array-map(callbackfn: (value: number, index: number, array: Uint8Array) => number, thisArg?: any): Uint8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: number, index: number, array: Uint8Array) =&gt; number | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number): number
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

<!--Device-Uint8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number): number--><!--Device-Uint8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) =&gt; number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number, initialValue: number): number
```

**Since:** -1

<!--Device-Uint8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number, initialValue: number): number--><!--Device-Uint8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number, initialValue: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) =&gt; number | Yes |  |
| initialValue | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## reduce

```TypeScript
reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

<!--Device-Uint8Array-reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) => U, initialValue: U): U--><!--Device-Uint8Array-reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) => U, initialValue: U): U-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) =&gt; U | Yes |  |
| initialValue | U | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| U |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number): number
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

<!--Device-Uint8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number): number--><!--Device-Uint8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) =&gt; number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number, initialValue: number): number
```

**Since:** -1

<!--Device-Uint8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number, initialValue: number): number--><!--Device-Uint8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) => number, initialValue: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Uint8Array) =&gt; number | Yes |  |
| initialValue | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## reduceRight

```TypeScript
reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

<!--Device-Uint8Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) => U, initialValue: U): U--><!--Device-Uint8Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) => U, initialValue: U): U-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: number, currentIndex: number, array: Uint8Array) =&gt; U | Yes |  |
| initialValue | U | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): Uint8Array
```

Reverses the elements in an Array.

**Since:** -1

<!--Device-Uint8Array-reverse(): Uint8Array--><!--Device-Uint8Array-reverse(): Uint8Array-End-->

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array |  |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

Sets a value or an array of values.

**Since:** -1

<!--Device-Uint8Array-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint8Array-set(array: ArrayLike<number>, offset?: number): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |  |
| offset | number | No |  |

## slice

```TypeScript
slice(start?: number, end?: number): Uint8Array
```

Returns a section of an array.

**Since:** -1

<!--Device-Uint8Array-slice(start?: number, end?: number): Uint8Array--><!--Device-Uint8Array-slice(start?: number, end?: number): Uint8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array |  |

## some

```TypeScript
some(predicate: (value: number, index: number, array: Uint8Array) => unknown, thisArg?: any): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**Since:** -1

<!--Device-Uint8Array-some(predicate: (value: number, index: number, array: Uint8Array) => unknown, thisArg?: any): boolean--><!--Device-Uint8Array-some(predicate: (value: number, index: number, array: Uint8Array) => unknown, thisArg?: any): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: number, index: number, array: Uint8Array) =&gt; unknown | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## sort

```TypeScript
sort(compareFn?: (a: number, b: number) => number): this
```

Sorts an array.

**Since:** -1

<!--Device-Uint8Array-sort(compareFn?: (a: number, b: number) => number): this--><!--Device-Uint8Array-sort(compareFn?: (a: number, b: number) => number): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compareFn | (a: number, b: number) =&gt; number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint8Array
```

Gets a new Uint8Array view of the ArrayBuffer store for this array, referencing the elements at begin, inclusive, up to end, exclusive.

**Since:** -1

<!--Device-Uint8Array-subarray(begin?: number, end?: number): Uint8Array--><!--Device-Uint8Array-subarray(begin?: number, end?: number): Uint8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array |  |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Converts a number to a string by using the current locale.

**Since:** -1

<!--Device-Uint8Array-toLocaleString(): string--><!--Device-Uint8Array-toLocaleString(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## toString

```TypeScript
toString(): string
```

Returns a string representation of an array.

**Since:** -1

<!--Device-Uint8Array-toString(): string--><!--Device-Uint8Array-toString(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## valueOf

```TypeScript
valueOf(): Uint8Array
```

Returns the primitive value of the specified object.

**Since:** -1

<!--Device-Uint8Array-valueOf(): Uint8Array--><!--Device-Uint8Array-valueOf(): Uint8Array-End-->

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

**Since:** -1

<!--Device-Uint8Array-readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8Array-readonly BYTES_PER_ELEMENT: number-End-->

## buffer

```TypeScript
readonly buffer: ArrayBufferLike
```

The ArrayBuffer instance referenced by the array.

**Type:** [ArrayBufferLike](arkts-na-arraybufferlike-t.md)

**Since:** -1

<!--Device-Uint8Array-readonly buffer: ArrayBufferLike--><!--Device-Uint8Array-readonly buffer: ArrayBufferLike-End-->

## byteLength

```TypeScript
readonly byteLength: number
```

The length in bytes of the array.

**Type:** number

**Since:** -1

<!--Device-Uint8Array-readonly byteLength: number--><!--Device-Uint8Array-readonly byteLength: number-End-->

## byteOffset

```TypeScript
readonly byteOffset: number
```

The offset in bytes of the array.

**Type:** number

**Since:** -1

<!--Device-Uint8Array-readonly byteOffset: number--><!--Device-Uint8Array-readonly byteOffset: number-End-->

## length

```TypeScript
readonly length: number
```

The length of the array.

**Type:** number

**Since:** -1

<!--Device-Uint8Array-readonly length: number--><!--Device-Uint8Array-readonly length: number-End-->

