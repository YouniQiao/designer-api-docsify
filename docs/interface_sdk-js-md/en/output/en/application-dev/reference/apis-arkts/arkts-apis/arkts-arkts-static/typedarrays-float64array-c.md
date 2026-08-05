# Float64Array

class Float64Array

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class Float64Array--><!--Device-unnamed-export class Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

## $_get

```TypeScript
public $_get(index: int): double
```

Returns an instance of number at passed index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public $_get(index: int): double--><!--Device-Float64Array-public $_get(index: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | index to look at\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| double | - the raw numeric value at index. |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<Double>
```

Iterable interface implementation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public $_iterator(): IterableIterator<Double>--><!--Device-Float64Array-public $_iterator(): IterableIterator<Double>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | - iterator over all elements |

## $_set

```TypeScript
public $_set(index: int, val: double): void
```

Assigns val as element on index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public $_set(index: int, val: double): void--><!--Device-Float64Array-public $_set(index: int, val: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | index to change\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| val | double | Yes | value to set |

## at

```TypeScript
public at(index: int): double | undefined
```

Returns an instance of primitive type at passed index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public at(index: int): double | undefined--><!--Device-Float64Array-public at(index: int): double | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | index to look at |

**Return value:**

| Type | Description |
| --- | --- |
| double | - the raw numeric value at index, or undefined if the index is out of bounds. |

## constructor

```TypeScript
public constructor()
```

Creates an empty Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor()--><!--Device-Float64Array-public constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

Creates a Float64Array with respect to length.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(length: int)--><!--Device-Float64Array-public constructor(length: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | Number of elements\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## constructor

```TypeScript
public constructor(length: double)
```

Creates a Float64Array with respect to length.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(length: double)--><!--Device-Float64Array-public constructor(length: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | double | Yes | Number of elements |

## constructor

```TypeScript
public constructor(other: Float64Array)
```

Creates a copy of Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(other: Float64Array)--><!--Device-Float64Array-public constructor(other: Float64Array)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Float64Array | Yes | data initializer |

## constructor

```TypeScript
public constructor(numbers: FixedArray<int>)
```

Creates a Float64Array from FixedArray\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(numbers: FixedArray<int>)--><!--Device-Float64Array-public constructor(numbers: FixedArray<int>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;int&gt; | Yes | data initializer |

## constructor

```TypeScript
public constructor(numbers: FixedArray<double>)
```

Creates a Float64Array from FixedArray\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(numbers: FixedArray<double>)--><!--Device-Float64Array-public constructor(numbers: FixedArray<double>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;double&gt; | Yes | data initializer |

## constructor

```TypeScript
public constructor(elements: Iterable<double>)
```

Creates a Float64Array with respect to data accessed via Iterable\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ interface

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(elements: Iterable<double>)--><!--Device-Float64Array-public constructor(elements: Iterable<double>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | Iterable&lt;double&gt; | Yes | an iterable object |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

Creates a Float64Array with respect to buf and byteOffset.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | data initializer |
| byteOffset | int | Yes | byte offset from begin of the buf\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

Creates a Float64Array with respect to data, byteOffset and length.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | data initializer |
| byteOffset | double | Yes | byte offset from begin of the buf |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int, length: int)
```

Creates a Float64Array with respect to data, byteOffset and length.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)--><!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | data initializer |
| byteOffset | int | Yes | byte offset from begin of the buf\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| length | int | Yes | size of elements of type double in newly created Float64Array\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

Creates a Float64Array with respect to data, byteOffset and length.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-Float64Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | data initializer |
| byteOffset | double \| undefined | Yes | byte offset from begin of the buf |
| length | double \| undefined | Yes | size of elements of type double in newly created Float64Array |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

Creates a Float64Array with respect to buf.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-Float64Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; \| ArrayBuffer | Yes | data initializer |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): Float64Array
```

Makes a copy of internal elements to targetPos from startPos to endPos. See rules of parameters normalization on

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public copyWithin(target: int, start: int, end?: int): Float64Array--><!--Device-Float64Array-public copyWithin(target: int, start: int, end?: int): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | int | Yes | insert index to place copied elements |
| start | int | Yes | start index to begin copy from |
| end | int | No | last index to end copy from, excluded. Defaults to the array length. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | The modified Float64Array instance. |

## copyWithin

```TypeScript
public copyWithin(target: int): Float64Array
```

Makes a copy of internal elements to targetPos from begin to end of Float64Array. See rules of parameters normalization on

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public copyWithin(target: int): Float64Array--><!--Device-Float64Array-public copyWithin(target: int): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | int | Yes | insert index to place copied elements\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | The modified Float64Array instance. |

## entries

```TypeScript
public entries(): IterableIterator<[int, double]>
```

Returns an array of key, value pairs for every entry in the Float64Array

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public entries(): IterableIterator<[int, double]>--><!--Device-Float64Array-public entries(): IterableIterator<[int, double]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;[int, double]&gt; | - key, value pairs for every entry in the array |

## every

```TypeScript
public every(predicate: (element: double, index: int, array: Float64Array) => boolean): boolean
```

Determines whether the specified callback function returns true for all elements of an array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public every(predicate: (element: double, index: int, array: Float64Array) => boolean): boolean--><!--Device-Float64Array-public every(predicate: (element: double, index: int, array: Float64Array) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Float64Array) =&gt; boolean | Yes | A function that accepts three arguments.The every method calls the predicate function for each element in the array until the predicate returns a false, or until the end of the array. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - true unless predicate function returns a false for an array element, |

## fill

```TypeScript
public fill(value: double, start?: int, end?: int): this
```

Fills the Float64Array with specified value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public fill(value: double, start?: int, end?: int): this--><!--Device-Float64Array-public fill(value: double, start?: int, end?: int): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | new value |
| start | int | No | start index to begin fill from. Defaults to 0. |
| end | int | No | last index to end fill from, excluded. Defaults to the array length. |

**Return value:**

| Type | Description |
| --- | --- |
| this | - modified Float64Array |

## filter

```TypeScript
public filter(fn: (val: double, index: int, array: Float64Array) => boolean): Float64Array
```

Creates a new Float64Array from current Float64Array based on a condition fn.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public filter(fn: (val: double, index: int, array: Float64Array) => boolean): Float64Array--><!--Device-Float64Array-public filter(fn: (val: double, index: int, array: Float64Array) => boolean): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Float64Array) =&gt; boolean | Yes | the condition to apply for each element |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array |

## find

```TypeScript
public find(predicate: (value: double, index: int, obj: Float64Array) => boolean): double | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public find(predicate: (value: double, index: int, obj: Float64Array) => boolean): double | undefined--><!--Device-Float64Array-public find(predicate: (value: double, index: int, obj: Float64Array) => boolean): double | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Float64Array) =&gt; boolean | Yes | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, find immediately returns that element value. Otherwise, find returns undefined |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## findIndex

```TypeScript
public findIndex(predicate: (value: double, index: int, obj: Float64Array) => boolean): int
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public findIndex(predicate: (value: double, index: int, obj: Float64Array) => boolean): int--><!--Device-Float64Array-public findIndex(predicate: (value: double, index: int, obj: Float64Array) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Float64Array) =&gt; boolean | Yes | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found,findIndex immediately returns that element index. Otherwise, findIndex returns -1 |

**Return value:**

| Type | Description |
| --- | --- |
| int | - Index of the first matched element |

## findLast

```TypeScript
public findLast(fn: (val: double) => boolean): double
```

Finds the last element in the Float64Array that satisfies the condition

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public findLast(fn: (val: double) => boolean): double--><!--Device-Float64Array-public findLast(fn: (val: double) => boolean): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fn | (val: double) =&gt; boolean | Yes | A function to test each element. Should return true for the element to be found. |

**Return value:**

| Type | Description |
| --- | --- |
| double | - the last element that satisfies fn |

## findLast

```TypeScript
public findLast(fn: (val: double, index: int, array: Float64Array) => boolean): double
```

Finds the last element in the Float64Array that satisfies the condition

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public findLast(fn: (val: double, index: int, array: Float64Array) => boolean): double--><!--Device-Float64Array-public findLast(fn: (val: double, index: int, array: Float64Array) => boolean): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Float64Array) =&gt; boolean | Yes | A function to test each element. Called with (value, index, array).Should return true for the element to be found. |

**Return value:**

| Type | Description |
| --- | --- |
| double | - the last element that satisfies fn |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: double, index: int, array: Float64Array) => boolean): int
```

Finds an index of the last element in the Float64Array that satisfies the condition

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public findLastIndex(fn: (val: double, index: int, array: Float64Array) => boolean): int--><!--Device-Float64Array-public findLastIndex(fn: (val: double, index: int, array: Float64Array) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Float64Array) =&gt; boolean | Yes | A function to test each element. Called with (value, index, array).Should return true for the element to be found. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - the index of the last element that satisfies fn, -1 otherwise |

## forEach

```TypeScript
public forEach(callbackfn: (value: double, index: int, array: Float64Array) => void): void
```

Calls the given callback function once for each element in the Float64Array, in ascending order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public forEach(callbackfn: (value: double, index: int, array: Float64Array) => void): void--><!--Device-Float64Array-public forEach(callbackfn: (value: double, index: int, array: Float64Array) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: double, index: int, array: Float64Array) =&gt; void | Yes | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array. |

## from

```TypeScript
public static from(arr: FixedArray<double>): Float64Array
```

Creates an array from an object of FixedArray\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from(arr: FixedArray<double>): Float64Array--><!--Device-Float64Array-public static from(arr: FixedArray<double>): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | Yes | An instance of the FixedArray type to convert to an array. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## from

```TypeScript
public static from(set: Set<double>): Float64Array
```

Creates an array from a set of type std.core.Set\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from(set: Set<double>): Float64Array--><!--Device-Float64Array-public static from(set: Set<double>): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| set | Set&lt;double&gt; | Yes | A set object to convert to an array. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## from

```TypeScript
public static from(arr: Float64Array): Float64Array
```

Creates an array from an array of the same type.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from(arr: Float64Array): Float64Array--><!--Device-Float64Array-public static from(arr: Float64Array): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Float64Array | Yes | An array to convert to a new array. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## from

```TypeScript
public static from(arr: Array<double>): Float64Array
```

Creates an array from an object of std.core.Array\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from(arr: Array<double>): Float64Array--><!--Device-Float64Array-public static from(arr: Array<double>): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Array&lt;double&gt; | Yes | An instance of the std.core.Array type to convert to an array. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## from

```TypeScript
public static from(arrayLike: ArrayLike<double>): Float64Array
```

Creates an array from an array-like or iterable object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from(arrayLike: ArrayLike<double>): Float64Array--><!--Device-Float64Array-public static from(arrayLike: ArrayLike<double>): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | Yes | An array-like or iterable object to convert to an array. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Float64Array
```

Creates an array from an array-like or iterable object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Float64Array--><!--Device-Float64Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | An array-like or iterable object to convert to an array. |
| mapfn | (v: T, k: double) =&gt; double | Yes | A mapping function to call on every element of the array. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## from

```TypeScript
public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Float64Array
```

Creates an array from an array-like or iterable object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Float64Array--><!--Device-Float64Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;double&gt; | Yes | An array-like or iterable object to convert to an array. |
| mapfn | (v: double, k: double) =&gt; double | No | A mapping function to call on every element of the array.Defaults to the identity function (returns the element unchanged). |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - A new Float64Array |

## includes

```TypeScript
public includes(searchElement: double, fromIndex?: int): boolean
```

Determines whether Float64Array includes a certain element, returning true or false as appropriate

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public includes(searchElement: double, fromIndex?: int): boolean--><!--Device-Float64Array-public includes(searchElement: double, fromIndex?: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | double | Yes | The element to search for |
| fromIndex | int | No | The position in this array at which to begin searching for searchElement.Defaults to 0.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - true if searchElement is in Float64Array, false otherwise |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

Returns the index of the first occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public indexOf(searchElement: int): int--><!--Device-Float64Array-public indexOf(searchElement: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | int | Yes | The value to locate in the array. The search starts at index 0. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - index of element if found, -1 otherwise. |

## indexOf

```TypeScript
public indexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the first occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-Float64Array-public indexOf(searchElement: int, fromIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | int | Yes | The value to locate in the array. |
| fromIndex | int | Yes | The array index at which to begin the search. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - index of element if found, -1 otherwise. |

## indexOf

```TypeScript
public indexOf(searchElement: double, fromIndex?: int): int
```

Returns the index of the first occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public indexOf(searchElement: double, fromIndex?: int): int--><!--Device-Float64Array-public indexOf(searchElement: double, fromIndex?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | double | Yes | The value to locate in the array. |
| fromIndex | int | No | The array index at which to begin the search.If fromIndex is undefined, the search starts at index 0.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - index of element if found, -1 otherwise. |

## join

```TypeScript
public join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public join(separator?: string): string--><!--Device-Float64Array-public join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No | A string used to separate one element of an array from the next in the resulting String. If omitted, the array elements are separated with a comma. |

**Return value:**

| Type | Description |
| --- | --- |
| string | - a string with all array elements joined by the specified separator. |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

Returns a list of indices in the Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public keys(): IterableIterator<int>--><!--Device-Float64Array-public keys(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | - iterator over indices. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

Returns the index of the last occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public lastIndexOf(searchElement: int): int--><!--Device-Float64Array-public lastIndexOf(searchElement: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | int | Yes | The value to locate in the array. The search begins at index length - 1. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - rightmost index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: double): int
```

Returns the index of the last occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public lastIndexOf(searchElement: double): int--><!--Device-Float64Array-public lastIndexOf(searchElement: double): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | double | Yes | The value to locate in the array. The search begins at index length - 1. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - rightmost index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the last occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-Float64Array-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | int | Yes | The value to locate in the array. |
| fromIndex | int | Yes | The array index at which to begin the search. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - rightmost index of searchElement. It must be less or equal than fromIndex. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: double, fromIndex: int | undefined): int
```

Returns the index of the last occurrence of a value in Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int--><!--Device-Float64Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | double | Yes | The value to locate in the array. |
| fromIndex | int \| undefined | Yes | The array index at which to begin the search.Defaults to the array length - 1. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - rightmost index of searchElement. It must be less or equal than fromIndex. -1 if not found |

## length

```TypeScript
public get length(): int
```

Number of double stored in Float64Array

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public get length(): int--><!--Device-Float64Array-public get length(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | - the number of elements |

## map

```TypeScript
public map(fn: (val: double, index: int, array: Float64Array) => double): Float64Array
```

Creates a new Float64Array using fn(arr[i]) over all elements of current Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public map(fn: (val: double, index: int, array: Float64Array) => double): Float64Array--><!--Device-Float64Array-public map(fn: (val: double, index: int, array: Float64Array) => double): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Float64Array) =&gt; double | Yes | a function to apply for each element of current Float64Array |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array where for each element from current Float64Array fn was applied |

## of

```TypeScript
public static of(...items: FixedArray<int>): Float64Array
```

Returns a new array from a set of elements.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static of(...items: FixedArray<int>): Float64Array--><!--Device-Float64Array-public static of(...items: FixedArray<int>): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | Yes | a set of elements to include in the new array object. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array |

## of

```TypeScript
public static of(...items: FixedArray<double>): Float64Array
```

Returns a new array from a set of elements.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static of(...items: FixedArray<double>): Float64Array--><!--Device-Float64Array-public static of(...items: FixedArray<double>): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | Yes | a set of elements to include in the new array object. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array |

## of

```TypeScript
public static of(): Float64Array
```

Returns a new array from a set of elements.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static of(): Float64Array--><!--Device-Float64Array-public static of(): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array |

## reduce

```TypeScript
public reduce<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) => U,        initialValue: U): U--><!--Device-Float64Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) => U,        initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) =&gt; U | Yes | A function that accepts four arguments.The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The parameter which value is used as the initial value to start the accumulation.The first call to the callbackfn function provides this value as an argument. |

**Return value:**

| Type | Description |
| --- | --- |
| U | - the accumulated result from the last call to the callback function. |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Float64Array) => double): double
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Float64Array) => double): double--><!--Device-Float64Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Float64Array) => double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Float64Array) =&gt; double | Yes | A function that accepts four arguments.The reduce method calls the callbackfn function one time for each element in the array.The first call to the callbackfn function provides array first element value as an argument |

**Return value:**

| Type | Description |
| --- | --- |
| double | - the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public reduceRight<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) => U,        initialValue: U): U--><!--Device-Float64Array-public reduceRight<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) => U,        initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Float64Array) =&gt; U | Yes | A function that accepts four arguments.The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The parameter which value is used as the initial value to start the accumulation. |

**Return value:**

| Type | Description |
| --- | --- |
| U | - the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Float64Array) => double): double
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Float64Array) => double): double--><!--Device-Float64Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Float64Array) => double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Float64Array) =&gt; double | Yes | A function that accepts four arguments.The reduceRight method calls the callbackfn function one time for each element in the array.The first call to the callbackfn function provides array last element value as an argument. |

**Return value:**

| Type | Description |
| --- | --- |
| double | - the accumulated result from the last call to the callback function. |

## reverse

```TypeScript
public reverse(): Float64Array
```

Creates a new Float64Array using reversed data from the current one

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public reverse(): Float64Array--><!--Device-Float64Array-public reverse(): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array using reversed data from the current one |

## set

```TypeScript
public set(insertPos: int, val: double): void
```

Assigns val as element on insertPos.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public set(insertPos: int, val: double): void--><!--Device-Float64Array-public set(insertPos: int, val: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| insertPos | int | Yes | index to change\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| val | double | Yes | value to set |

## set

```TypeScript
public set(arr: FixedArray<double>): void
```

Copies all elements of arr to the current Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public set(arr: FixedArray<double>): void--><!--Device-Float64Array-public set(arr: FixedArray<double>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | Yes | array to copy data from |

## set

```TypeScript
public set(arr: FixedArray<double>, insertPos: int): void
```

Copies all elements of arr to the current Float64Array starting from insertPos.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public set(arr: FixedArray<double>, insertPos: int): void--><!--Device-Float64Array-public set(arr: FixedArray<double>, insertPos: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | Yes | array to copy data from |
| insertPos | int | Yes | start index where data from arr will be inserted\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## set

```TypeScript
public set(array: Float64Array): void
```

Copies all elements of array to the current Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public set(array: Float64Array): void--><!--Device-Float64Array-public set(array: Float64Array): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | Float64Array | Yes | array to copy data from |

## set

```TypeScript
public set(array: Float64Array, offset: int): void
```

Copies all elements of arr to the current Float64Array starting from offset.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public set(array: Float64Array, offset: int): void--><!--Device-Float64Array-public set(array: Float64Array, offset: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | Float64Array | Yes | array to copy data from |
| offset | int | Yes | start index where data from arr will be inserted\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## set

```TypeScript
public set(array: ArrayLike<double>, offset: int = 0): void
```

Copies elements from an ArrayLike object to the Float64Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public set(array: ArrayLike<double>, offset: int = 0): void--><!--Device-Float64Array-public set(array: ArrayLike<double>, offset: int = 0): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | Yes | An ArrayLike object containing the elements to copy. |
| offset | int | Yes | Optional. The offset into the target array at which to begin writing values from the source array. The default value is 0.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## slice

```TypeScript
public slice(begin: int): Float64Array
```

Creates a slice of current Float64Array using range [begin, this.length).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public slice(begin: int): Float64Array--><!--Device-Float64Array-public slice(begin: int): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | int | Yes | start index to be taken into slice\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array with elements of current Float64Array[begin, this.length) |

## slice

```TypeScript
public slice(begin?: int, end?: int): Float64Array
```

Creates a slice of current Float64Array using range [begin, end)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public slice(begin?: int, end?: int): Float64Array--><!--Device-Float64Array-public slice(begin?: int, end?: int): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | int | No | start index to be taken into slice. Defaults to 0. |
| end | int | No | last index to be taken into slice. Defaults to the array length. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array with elements of current Float64Array[begin;end), |

## some

```TypeScript
public some(predicate: (element: double, index: int, array: Float64Array) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public some(predicate: (element: double, index: int, array: Float64Array) => boolean): boolean--><!--Device-Float64Array-public some(predicate: (element: double, index: int, array: Float64Array) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Float64Array) =&gt; boolean | Yes | A function that accepts three arguments.The some method calls the predicate function for each element in the array until the predicate returns a true or until the end of the array. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - false unless predicate function returns true for an array element, |

## sort

```TypeScript
public sort(): this
```

Sorts in-place by numeric value in ascending order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public sort(): this--><!--Device-Float64Array-public sort(): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| this | - sorted Float64Array |

## sort

```TypeScript
public sort(compareFn?: (a: double, b: double) => int): this
```

Sorts in-place

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public sort(compareFn?: (a: double, b: double) => int): this--><!--Device-Float64Array-public sort(compareFn?: (a: double, b: double) => int): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compareFn | (a: double, b: double) =&gt; int | No | comparator used to determine the order of the elements.compareFn returns a negative value if first argument is less than second argument,zero if they're equal and a positive value otherwise.Defaults to an ascending numeric sort. |

**Return value:**

| Type | Description |
| --- | --- |
| this | - sorted Float64Array |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): Float64Array
```

Creates a new Float64Array that shares the same underlying ArrayBuffer as the current array, optionally with a restricted range.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public subarray(begin?: int, end?: int): Float64Array--><!--Device-Float64Array-public subarray(begin?: int, end?: int): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | int | No | start index, inclusive. Defaults to 0. |
| end | int | No | last index, exclusive. Defaults to the array length. |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array with the same underlying ArrayBuffer |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Float64Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | No | An object with some or all of the properties of the Intl.NumberFormat options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the locale-specific conversion |

## toReversed

```TypeScript
public toReversed(): Float64Array
```

Returns a new Float64Array with the elements in reverse order. The original array is not modified.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public toReversed(): Float64Array--><!--Device-Float64Array-public toReversed(): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array with the elements in reverse order. |

## toSorted

```TypeScript
public toSorted(): Float64Array
```

Returns a new Float64Array with the elements sorted in ascending order. The original array is not modified.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public toSorted(): Float64Array--><!--Device-Float64Array-public toSorted(): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array with the elements sorted in ascending order. |

## toString

```TypeScript
public toString(): string
```

Returns a comma-separated string representation of the Float64Array elements.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public toString(): string--><!--Device-Float64Array-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | - a comma-separated string of the array elements. |

## valueOf

```TypeScript
public valueOf(): Float64Array
```

Returns the object itself

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public valueOf(): Float64Array--><!--Device-Float64Array-public valueOf(): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array |  |

## values

```TypeScript
public values(): IterableIterator<Double>
```

Returns an iterator over the values of the Float64Array, in ascending order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public values(): IterableIterator<Double>--><!--Device-Float64Array-public values(): IterableIterator<Double>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | - an iterator over all elements. |

## with

```TypeScript
public with(index: int, value: double): Float64Array
```

Returns a new Float64Array with the element at the given index replaced by the given value. The original array is not modified.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public with(index: int, value: double): Float64Array--><!--Device-Float64Array-public with(index: int, value: double): Float64Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | index to change\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| value | double | Yes | value to set |

**Return value:**

| Type | Description |
| --- | --- |
| Float64Array | - a new Float64Array with the element at index replaced by value. |

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 8
```

Number of bytes occupied by each element

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public static readonly BYTES_PER_ELEMENT: int = 8--><!--Device-Float64Array-public static readonly BYTES_PER_ELEMENT: int = 8-End-->

**System capability:** SystemCapability.Utils.Lang

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

Underlying ArrayBuffer

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public readonly buffer: ArrayBuffer--><!--Device-Float64Array-public readonly buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public readonly byteLength: int
```

Number of bytes used The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public readonly byteLength: int--><!--Device-Float64Array-public readonly byteLength: int-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public readonly byteOffset: int
```

Byte offset within the underlying ArrayBuffer The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public readonly byteOffset: int--><!--Device-Float64Array-public readonly byteOffset: int-End-->

**System capability:** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'Float64Array'
```

String \"Float64Array\", representing the type name of this typed array.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Float64Array-public readonly name: string = 'Float64Array'--><!--Device-Float64Array-public readonly name: string = 'Float64Array'-End-->

**System capability:** SystemCapability.Utils.Lang

