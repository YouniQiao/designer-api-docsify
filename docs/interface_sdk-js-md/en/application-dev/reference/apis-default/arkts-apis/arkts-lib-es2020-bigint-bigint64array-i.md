# BigInt64Array

A typed array of 64-bit signed integer values. The contents are initialized to 0. If the requested number of bytes could not be allocated, an exception is raised.

## Modules to Import

```TypeScript
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<bigint>
```

**Return value:**

| Type | Description |
| --- | --- |
## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): this
```

Returns the this object after copying a section of the array identified by start and end to the same array starting at position target

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | number | Yes |  |
| start | number | Yes |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## entries

```TypeScript
entries(): IterableIterator<[number, bigint]>
```

Yields index, value pairs for every entry in the array.

**Return value:**

| Type | Description |
| --- | --- |
## every

```TypeScript
every(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean
```

Determines whether all the members of an array satisfy the specified test.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) = & gt; boolean | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## fill

```TypeScript
fill(value: bigint, start?: number, end?: number): this
```

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes |  |
| start | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## filter

```TypeScript
filter(predicate: (value: bigint, index: number, array: BigInt64Array) => any, thisArg?: any): BigInt64Array
```

Returns the elements of an array that meet the condition specified in a callback function.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) = & gt; any | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## find

```TypeScript
find(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): bigint | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) = & gt; boolean | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## findIndex

```TypeScript
findIndex(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) = & gt; boolean | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## forEach

```TypeScript
forEach(callbackfn: (value: bigint, index: number, array: BigInt64Array) => void, thisArg?: any): void
```

Performs the specified action for each element in an array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: bigint, index: number, array: BigInt64Array) = & gt; void | Yes |  |
| thisArg | any | No |  |

## includes

```TypeScript
includes(searchElement: bigint, fromIndex?: number): boolean
```

Determines whether an array includes a certain element, returning true or false as appropriate.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | bigint | Yes |  |
| fromIndex | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## indexOf

```TypeScript
indexOf(searchElement: bigint, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in an array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | bigint | Yes |  |
| fromIndex | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## keys

```TypeScript
keys(): IterableIterator<number>
```

Yields each index in the array.

**Return value:**

| Type | Description |
| --- | --- |
## lastIndexOf

```TypeScript
lastIndexOf(searchElement: bigint, fromIndex?: number): number
```

Returns the index of the last occurrence of a value in an array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | bigint | Yes |  |
| fromIndex | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## map

```TypeScript
map(callbackfn: (value: bigint, index: number, array: BigInt64Array) => bigint, thisArg?: any): BigInt64Array
```

Calls a defined callback function on each element of an array, and returns an array that contains the results.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: bigint, index: number, array: BigInt64Array) = & gt; bigint | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## reduce

```TypeScript
reduce(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) = & gt; bigint | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## reduce

```TypeScript
reduce<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) = & gt; U | Yes |  |
| initialValue | U | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) => bigint): bigint
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: bigint, currentValue: bigint, currentIndex: number, array: BigInt64Array) = & gt; bigint | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## reduceRight

```TypeScript
reduceRight<U>(callbackfn: (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: bigint, currentIndex: number, array: BigInt64Array) = & gt; U | Yes |  |
| initialValue | U | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## reverse

```TypeScript
reverse(): this
```

Reverses the elements in the array.

**Return value:**

| Type | Description |
| --- | --- |
## set

```TypeScript
set(array: ArrayLike<bigint>, offset?: number): void
```

Sets a value or an array of values.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | ArrayLike & lt;bigint & gt; | Yes |  |
| offset | number | No |  |

## slice

```TypeScript
slice(start?: number, end?: number): BigInt64Array
```

Returns a section of an array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## some

```TypeScript
some(predicate: (value: bigint, index: number, array: BigInt64Array) => boolean, thisArg?: any): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: bigint, index: number, array: BigInt64Array) = & gt; boolean | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## sort

```TypeScript
sort(compareFn?: (a: bigint, b: bigint) => number | bigint): this
```

Sorts the array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compareFn | (a: bigint, b: bigint) = & gt; number \ | bigint | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## subarray

```TypeScript
subarray(begin?: number, end?: number): BigInt64Array
```

Gets a new BigInt64Array view of the ArrayBuffer store for this array, referencing the elements at begin, inclusive, up to end, exclusive.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## toLocaleString

```TypeScript
toLocaleString(): string
```

Converts the array to a string by using the current locale.

**Return value:**

| Type | Description |
| --- | --- |
## toString

```TypeScript
toString(): string
```

Returns a string representation of the array.

**Return value:**

| Type | Description |
| --- | --- |
## valueOf

```TypeScript
valueOf(): BigInt64Array
```

Returns the primitive value of the specified object.

**Return value:**

| Type | Description |
| --- | --- |
## values

```TypeScript
values(): IterableIterator<bigint>
```

Yields each value in the array.

**Return value:**

| Type | Description |
| --- | --- |
## [index: number]

```TypeScript
[index: number]: bigint
```

**Type:** bigint

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "BigInt64Array"
```

**Type:** "BigInt64Array"

## buffer

```TypeScript
readonly buffer: ArrayBufferLike
```

The ArrayBuffer instance referenced by the array.

**Type:** [ArrayBufferLike](arkts-arraybufferlike-t.md)

## byteLength

```TypeScript
readonly byteLength: number
```

The length in bytes of the array.

**Type:** number

## byteOffset

```TypeScript
readonly byteOffset: number
```

The offset in bytes of the array.

**Type:** number

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

## length

```TypeScript
readonly length: number
```

The length of the array.

**Type:** number
