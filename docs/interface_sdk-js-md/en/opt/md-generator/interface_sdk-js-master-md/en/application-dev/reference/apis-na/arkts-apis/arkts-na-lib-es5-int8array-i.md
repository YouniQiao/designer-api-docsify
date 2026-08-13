# Int8Array

A typed array of 8-bit integer values. The contents are initialized to 0. If the requested number of bytes could not be allocated an exception is raised.

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface Int8Array--><!--Device-unnamed-interface Int8Array-End-->

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): this
```

Returns the this object after copying a section of the array identified by start and end to the same array starting at position target

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-copyWithin(target: number, start: number, end?: number): this--><!--Device-Int8Array-copyWithin(target: number, start: number, end?: number): this-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | number | Yes |
| start | number | Yes |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## every

```TypeScript
every(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean
```

Determines whether all the members of an array satisfy the specified test.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-every(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean--><!--Device-Int8Array-every(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: number, index: number, array: Int8Array) = & gt; unknown | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): this
```

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-fill(value: number, start?: number, end?: number): this--><!--Device-Int8Array-fill(value: number, start?: number, end?: number): this-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## filter

```TypeScript
filter(predicate: (value: number, index: number, array: Int8Array) => any, thisArg?: any): Int8Array
```

Returns the elements of an array that meet the condition specified in a callback function.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-filter(predicate: (value: number, index: number, array: Int8Array) => any, thisArg?: any): Int8Array--><!--Device-Int8Array-filter(predicate: (value: number, index: number, array: Int8Array) => any, thisArg?: any): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: number, index: number, array: Int8Array) = & gt; any | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## find

```TypeScript
find(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-find(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | undefined--><!--Device-Int8Array-find(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | undefined-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: number, index: number, obj: Int8Array) = & gt; boolean | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## findIndex

```TypeScript
findIndex(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-findIndex(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number--><!--Device-Int8Array-findIndex(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: number, index: number, obj: Int8Array) = & gt; boolean | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## forEach

```TypeScript
forEach(callbackfn: (value: number, index: number, array: Int8Array) => void, thisArg?: any): void
```

Performs the specified action for each element in an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-forEach(callbackfn: (value: number, index: number, array: Int8Array) => void, thisArg?: any): void--><!--Device-Int8Array-forEach(callbackfn: (value: number, index: number, array: Int8Array) => void, thisArg?: any): void-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (value: number, index: number, array: Int8Array) = & gt; void | Yes |
| thisArg | any | No |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Int8Array-indexOf(searchElement: number, fromIndex?: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | number | Yes |
| fromIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-join(separator?: string): string--><!--Device-Int8Array-join(separator?: string): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| separator | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

Returns the index of the last occurrence of a value in an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Int8Array-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchElement | number | Yes |
| fromIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## map

```TypeScript
map(callbackfn: (value: number, index: number, array: Int8Array) => number, thisArg?: any): Int8Array
```

Calls a defined callback function on each element of an array, and returns an array that contains the results.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-map(callbackfn: (value: number, index: number, array: Int8Array) => number, thisArg?: any): Int8Array--><!--Device-Int8Array-map(callbackfn: (value: number, index: number, array: Int8Array) => number, thisArg?: any): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (value: number, index: number, array: Int8Array) = & gt; number | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number--><!--Device-Int8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) = & gt; number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number--><!--Device-Int8Array-reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) = & gt; number | Yes |
| initialValue | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## reduce

```TypeScript
reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U--><!--Device-Int8Array-reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) = & gt; U | Yes |
| initialValue | U | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| U |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number--><!--Device-Int8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) = & gt; number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number--><!--Device-Int8Array-reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) = & gt; number | Yes |
| initialValue | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## reduceRight

```TypeScript
reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U--><!--Device-Int8Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) = & gt; U | Yes |
| initialValue | U | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| U |

## reverse

```TypeScript
reverse(): Int8Array
```

Reverses the elements in an Array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-reverse(): Int8Array--><!--Device-Int8Array-reverse(): Int8Array-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

Sets a value or an array of values.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Int8Array-set(array: ArrayLike<number>, offset?: number): void-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |
| offset | number | No |

## slice

```TypeScript
slice(start?: number, end?: number): Int8Array
```

Returns a section of an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-slice(start?: number, end?: number): Int8Array--><!--Device-Int8Array-slice(start?: number, end?: number): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## some

```TypeScript
some(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-some(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean--><!--Device-Int8Array-some(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: number, index: number, array: Int8Array) = & gt; unknown | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## sort

```TypeScript
sort(compareFn?: (a: number, b: number) => number): this
```

Sorts an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-sort(compareFn?: (a: number, b: number) => number): this--><!--Device-Int8Array-sort(compareFn?: (a: number, b: number) => number): this-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compareFn | (a: number, b: number) = & gt; number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Int8Array
```

Gets a new Int8Array view of the ArrayBuffer store for this array, referencing the elements at begin, inclusive, up to end, exclusive.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-subarray(begin?: number, end?: number): Int8Array--><!--Device-Int8Array-subarray(begin?: number, end?: number): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | No |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Converts a number to a string by using the current locale.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-toLocaleString(): string--><!--Device-Int8Array-toLocaleString(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
toString(): string
```

Returns a string representation of an array.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-toString(): string--><!--Device-Int8Array-toString(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## valueOf

```TypeScript
valueOf(): Int8Array
```

Returns the primitive value of the specified object.

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-valueOf(): Int8Array--><!--Device-Int8Array-valueOf(): Int8Array-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-readonly BYTES_PER_ELEMENT: number--><!--Device-Int8Array-readonly BYTES_PER_ELEMENT: number-End-->

## buffer

```TypeScript
readonly buffer: ArrayBufferLike
```

The ArrayBuffer instance referenced by the array.

**Type:** [ArrayBufferLike](arkts-na-arraybufferlike-t.md)

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-readonly buffer: ArrayBufferLike--><!--Device-Int8Array-readonly buffer: ArrayBufferLike-End-->

## byteLength

```TypeScript
readonly byteLength: number
```

The length in bytes of the array.

**Type:** number

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-readonly byteLength: number--><!--Device-Int8Array-readonly byteLength: number-End-->

## byteOffset

```TypeScript
readonly byteOffset: number
```

The offset in bytes of the array.

**Type:** number

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-readonly byteOffset: number--><!--Device-Int8Array-readonly byteOffset: number-End-->

## length

```TypeScript
readonly length: number
```

The length of the array.

**Type:** number

**Since:** -1

**Deprecated since:** -1

<!--Device-Int8Array-readonly length: number--><!--Device-Int8Array-readonly length: number-End-->
