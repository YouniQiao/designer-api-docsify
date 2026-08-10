# Array

**ArkTS模式：** 仅支持ArkTS-Dyn

## concat

```TypeScript
concat(...items: ConcatArray<T>[]): T[]
```

Combines two or more arrays.This method returns a new array without modifying any existing arrays.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-concat(...items: ConcatArray<T>[]): T[]--><!--Device-Array-concat(...items: ConcatArray<T>[]): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [ConcatArray](../../apis-arkts/arkts-apis/arkts-arkts-concatarray-i.md)&lt;T&gt;[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## concat

```TypeScript
concat(...items: (T | ConcatArray<T>)[]): T[]
```

Combines two or more arrays.This method returns a new array without modifying any existing arrays.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-concat(...items: (T | ConcatArray<T>)[]): T[]--><!--Device-Array-concat(...items: (T | ConcatArray<T>)[]): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | (T \| ConcatArray&lt;T&gt;)[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## every

```TypeScript
every<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): this is S[]
```

Determines whether all the members of an array satisfy the specified test.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-every<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): this is S[]--><!--Device-Array-every<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): this is S[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, array: T[]) =&gt; value is S | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this is S[] |  |

## every

```TypeScript
every(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean
```

Determines whether all the members of an array satisfy the specified test.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-every(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean--><!--Device-Array-every(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, array: T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## filter

```TypeScript
filter<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): S[]
```

Returns the elements of an array that meet the condition specified in a callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-filter<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): S[]--><!--Device-Array-filter<S extends T>(predicate: (value: T, index: number, array: T[]) => value is S, thisArg?: any): S[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, array: T[]) =&gt; value is S | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| S[] |  |

## filter

```TypeScript
filter(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[]
```

Returns the elements of an array that meet the condition specified in a callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-filter(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[]--><!--Device-Array-filter(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, array: T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: number, array: T[]) => void, thisArg?: any): void
```

Performs the specified action for each element in an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-forEach(callbackfn: (value: T, index: number, array: T[]) => void, thisArg?: any): void--><!--Device-Array-forEach(callbackfn: (value: T, index: number, array: T[]) => void, thisArg?: any): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: number, array: T[]) =&gt; void | 是 |  |
| thisArg | any | 否 |  |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: number): number
```

Returns the index of the first occurrence of a value in an array, or -1 if it is not present.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-indexOf(searchElement: T, fromIndex?: number): number--><!--Device-Array-indexOf(searchElement: T, fromIndex?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 |  |
| fromIndex | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## join

```TypeScript
join(separator?: string): string
```

Adds all the elements of an array into a string, separated by the specified separator string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-join(separator?: string): string--><!--Device-Array-join(separator?: string): string-End-->

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
lastIndexOf(searchElement: T, fromIndex?: number): number
```

Returns the index of the last occurrence of a specified value in an array, or -1 if it is not present.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-lastIndexOf(searchElement: T, fromIndex?: number): number--><!--Device-Array-lastIndexOf(searchElement: T, fromIndex?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 |  |
| fromIndex | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## map

```TypeScript
map<U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[]
```

Calls a defined callback function on each element of an array, and returns an array that contains the results.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-map<U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[]--><!--Device-Array-map<U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: number, array: T[]) =&gt; U | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U[] |  |

## pop

```TypeScript
pop(): T | undefined
```

Removes the last element from an array and returns it.If the array is empty, undefined is returned and the array is not modified.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-pop(): T | undefined--><!--Device-Array-pop(): T | undefined-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## push

```TypeScript
push(...items: T[]): number
```

Appends new elements to the end of an array, and returns the new length of the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-push(...items: T[]): number--><!--Device-Array-push(...items: T[]): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T--><!--Device-Array-reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, currentIndex: number, array: T[]) =&gt; T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T, initialValue: T): T
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, currentIndex: number, array: T[]) =&gt; T | 是 |  |
| initialValue | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## reduce

```TypeScript
reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U--><!--Device-Array-reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, currentIndex: number, array: T[]) =&gt; U | 是 |  |
| initialValue | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-reduceRight(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T--><!--Device-Array-reduceRight(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, currentIndex: number, array: T[]) =&gt; T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T, initialValue: T): T
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, currentIndex: number, array: T[]) =&gt; T | 是 |  |
| initialValue | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## reduceRight

```TypeScript
reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U--><!--Device-Array-reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, currentIndex: number, array: T[]) =&gt; U | 是 |  |
| initialValue | U | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): T[]
```

Reverses the elements in an array in place.This method mutates the array and returns a reference to the same array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-reverse(): T[]--><!--Device-Array-reverse(): T[]-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## shift

```TypeScript
shift(): T | undefined
```

Removes the first element from an array and returns it.If the array is empty, undefined is returned and the array is not modified.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-shift(): T | undefined--><!--Device-Array-shift(): T | undefined-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## slice

```TypeScript
slice(start?: number, end?: number): T[]
```

Returns a copy of a section of an array.For both start and end, a negative index can be used to indicate an offset from the end of the array.For example, -2 refers to the second to last element of the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-slice(start?: number, end?: number): T[]--><!--Device-Array-slice(start?: number, end?: number): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## some

```TypeScript
some(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-some(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean--><!--Device-Array-some(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, array: T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## sort

```TypeScript
sort(compareFn?: (a: T, b: T) => number): this
```

Sorts an array in place.This method mutates the array and returns a reference to the same array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-sort(compareFn?: (a: T, b: T) => number): this--><!--Device-Array-sort(compareFn?: (a: T, b: T) => number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## splice

```TypeScript
splice(start: number, deleteCount?: number): T[]
```

Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-splice(start: number, deleteCount?: number): T[]--><!--Device-Array-splice(start: number, deleteCount?: number): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 |  |
| deleteCount | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## splice

```TypeScript
splice(start: number, deleteCount: number, ...items: T[]): T[]
```

Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-splice(start: number, deleteCount: number, ...items: T[]): T[]--><!--Device-Array-splice(start: number, deleteCount: number, ...items: T[]): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 |  |
| deleteCount | number | 是 |  |
| items | T[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## toLocaleString

```TypeScript
toLocaleString(): string
```

Returns a string representation of an array. The elements are converted to string using their toLocaleString methods.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-toLocaleString(): string--><!--Device-Array-toLocaleString(): string-End-->

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

<!--Device-Array-toString(): string--><!--Device-Array-toString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## unshift

```TypeScript
unshift(...items: T[]): number
```

Inserts new elements at the start of an array, and returns the new length of the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-unshift(...items: T[]): number--><!--Device-Array-unshift(...items: T[]): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## [n: number]

```TypeScript
[n: number]: T
```

**类型：** T

**ArkTS模式：** 仅支持ArkTS-Dyn

## length

```TypeScript
length: number
```

Gets or sets the length of the array. This is a number one higher than the highest index in the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-length: number--><!--Device-Array-length: number-End-->

