# Int16Array

class Int16Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Int16Array--><!--Device-unnamed-export class Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
public $_get(index: int): double
```

Returns an instance of number at passed index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public $_get(index: int): double--><!--Device-Int16Array-public $_get(index: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to look at &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the raw numeric value at index. |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<double>
```

Iterable interface implementation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public $_iterator(): IterableIterator<double>--><!--Device-Int16Array-public $_iterator(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | iterator over all elements |

## $_set

```TypeScript
public $_set(index: int, val: short): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public $_set(index: int, val: short): void--><!--Device-Int16Array-public $_set(index: int, val: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | short | 是 | value to set |

## $_set

```TypeScript
public $_set(index: int, val: int): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public $_set(index: int, val: int): void--><!--Device-Int16Array-public $_set(index: int, val: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | int | 是 | value to set &lt;br&gt;The value should be an integer. |

## $_set

```TypeScript
public $_set(index: int, val: double): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public $_set(index: int, val: double): void--><!--Device-Int16Array-public $_set(index: int, val: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | double | 是 | value to set |

## at

```TypeScript
public at(index: int): double | undefined
```

Returns an instance of primitive type at passed index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public at(index: int): double | undefined--><!--Device-Int16Array-public at(index: int): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to look at &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the raw numeric value at index, or undefined if the index is out of bounds. |

## constructor

```TypeScript
public constructor()
```

Creates an empty Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor()--><!--Device-Int16Array-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

Creates an Int16Array with respect to length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(length: int)--><!--Device-Int16Array-public constructor(length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | Number of elements &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(length: double)
```

Creates an Int16Array with respect to length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(length: double)--><!--Device-Int16Array-public constructor(length: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | Number of elements |

## constructor

```TypeScript
public constructor(other: Int16Array)
```

Creates a copy of Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(other: Int16Array)--><!--Device-Int16Array-public constructor(other: Int16Array)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Int16Array | 是 | data initializer |

## constructor

```TypeScript
public constructor(numbers: FixedArray<int>)
```

Creates an Int16Array from FixedArray&lt;int&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(numbers: FixedArray<int>)--><!--Device-Int16Array-public constructor(numbers: FixedArray<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;int&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(numbers: FixedArray<double>)
```

Creates an Int16Array from FixedArray&lt;number&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(numbers: FixedArray<double>)--><!--Device-Int16Array-public constructor(numbers: FixedArray<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;double&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(numbers: Array<int>)
```

Creates an Int16Array from Array&lt;int&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(numbers: Array<int>)--><!--Device-Int16Array-public constructor(numbers: Array<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | Array&lt;int&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(elements: Iterable<double>)
```

Creates an Int16Array with respect to data accessed via Iterable&lt;Number&gt; interface

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(elements: Iterable<double>)--><!--Device-Int16Array-public constructor(elements: Iterable<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;double&gt; | 是 | an iterable object |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

Creates an Int16Array with respect to buf and byteOffset.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | int | 是 | byte offset from begin of the buf &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

Creates an Int16Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | double | 是 | byte offset from begin of the buf |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int, length: int)
```

Creates an Int16Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)--><!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | int | 是 | byte offset from begin of the buf &lt;br&gt;The value should be an integer. |
| length | int | 是 | size of elements of type short in newly created Int16Array &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

Creates an Int16Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-Int16Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | double \| undefined | 是 | byte offset from begin of the buf |
| length | double \| undefined | 是 | size of elements of type short in newly created Int16Array |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

Creates an Int16Array with respect to buf.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-Int16Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; \| ArrayBuffer | 是 | data initializer |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): Int16Array
```

Makes a copy of internal elements to targetPos from startPos to endPos.See rules of parameters normalization on

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public copyWithin(target: int, start: int, end?: int): Int16Array--><!--Device-Int16Array-public copyWithin(target: int, start: int, end?: int): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | insert index to place copied elements |
| start | int | 是 | start index to begin copy from |
| end | int | 否 | last index to end copy from, excluded. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | The modified Int16Array instance. |

## copyWithin

```TypeScript
public copyWithin(target: int): Int16Array
```

Makes a copy of internal elements to targetPos from begin to end of Int16Array.See rules of parameters normalization on

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public copyWithin(target: int): Int16Array--><!--Device-Int16Array-public copyWithin(target: int): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | insert index to place copied elements &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | The modified Int16Array instance. |

## entries

```TypeScript
public entries(): IterableIterator<[int, double]>
```

Returns an array of key, value pairs for every entry in the Int16Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public entries(): IterableIterator<[int, double]>--><!--Device-Int16Array-public entries(): IterableIterator<[int, double]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, double]&gt; | key, value pairs for every entry in the array |

## every

```TypeScript
public every(predicate: (element: double, index: int, array: Int16Array) => boolean): boolean
```

Determines whether the specified callback function returns true for all elements of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public every(predicate: (element: double, index: int, array: Int16Array) => boolean): boolean--><!--Device-Int16Array-public every(predicate: (element: double, index: int, array: Int16Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Int16Array) =&gt; boolean | 是 | A function that accepts three arguments. The every method calls the predicate function for each element in the array until the predicate returns a false, or until the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true unless predicate function returns a false for an array element, in which case false is immediately returned. |

## fill

```TypeScript
public fill(value: short, start?: int, end?: int): this
```

Fills the Int16Array with specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public fill(value: short, start?: int, end?: int): this--><!--Device-Int16Array-public fill(value: short, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | new value |
| start | int | 否 | start index to begin fill from. Defaults to 0. &lt;br&gt;The value should be an integer. |
| end | int | 否 | last index to end fill from, excluded. Defaults to the array length. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | modified Int16Array |

## fill

```TypeScript
public fill(value: double, start?: int, end?: int): this
```

Fills the Int16Array with specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public fill(value: double, start?: int, end?: int): this--><!--Device-Int16Array-public fill(value: double, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | new value |
| start | int | 否 | start index to begin fill from. Defaults to 0. &lt;br&gt;The value should be an integer. |
| end | int | 否 | last index to end fill from, excluded. Defaults to the array length. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | modified Int16Array |

## filter

```TypeScript
public filter(fn: (val: double, index: int, array: Int16Array) => boolean): Int16Array
```

Creates a new Int16Array from current Int16Array based on a condition fn.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public filter(fn: (val: double, index: int, array: Int16Array) => boolean): Int16Array--><!--Device-Int16Array-public filter(fn: (val: double, index: int, array: Int16Array) => boolean): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Int16Array) =&gt; boolean | 是 | the condition to apply for each element |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array |

## find

```TypeScript
public find(predicate: (value: double, index: int, obj: Int16Array) => boolean): double | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public find(predicate: (value: double, index: int, obj: Int16Array) => boolean): double | undefined--><!--Device-Int16Array-public find(predicate: (value: double, index: int, obj: Int16Array) => boolean): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Int16Array) =&gt; boolean | 是 | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, find immediately returns that element value. Otherwise, find returns undefined |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double |  |

## findIndex

```TypeScript
public findIndex(predicate: (value: double, index: int, obj: Int16Array) => boolean): int
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public findIndex(predicate: (value: double, index: int, obj: Int16Array) => boolean): int--><!--Device-Int16Array-public findIndex(predicate: (value: double, index: int, obj: Int16Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Int16Array) =&gt; boolean | 是 | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, findIndex immediately returns that element index. Otherwise, findIndex returns -1 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Index of the first matched element |

## findLast

```TypeScript
public findLast(fn: (val: double) => boolean): double
```

Finds the last element in the Int16Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public findLast(fn: (val: double) => boolean): double--><!--Device-Int16Array-public findLast(fn: (val: double) => boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double) =&gt; boolean | 是 | A function to test each element. Should return true for the element to be found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the last element that satisfies fn |

## findLast

```TypeScript
public findLast(fn: (val: double, index: int, array: Int16Array) => boolean): short
```

Finds the last element in the Int16Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public findLast(fn: (val: double, index: int, array: Int16Array) => boolean): short--><!--Device-Int16Array-public findLast(fn: (val: double, index: int, array: Int16Array) => boolean): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Int16Array) =&gt; boolean | 是 | A function to test each element. Called with (value, index, array). Should return true for the element to be found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the last element that satisfies fn |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: double, index: int, array: Int16Array) => boolean): int
```

Finds an index of the last element in the Int16Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public findLastIndex(fn: (val: double, index: int, array: Int16Array) => boolean): int--><!--Device-Int16Array-public findLastIndex(fn: (val: double, index: int, array: Int16Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Int16Array) =&gt; boolean | 是 | A function to test each element. Called with (value, index, array). Should return true for the element to be found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the index of the last element that satisfies fn, -1 otherwise |

## forEach

```TypeScript
public forEach(callbackfn: (value: double, index: int, array: Int16Array) => void): void
```

Calls the given callback function once for each element in the Int16Array, in ascending order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public forEach(callbackfn: (value: double, index: int, array: Int16Array) => void): void--><!--Device-Int16Array-public forEach(callbackfn: (value: double, index: int, array: Int16Array) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: double, index: int, array: Int16Array) =&gt; void | 是 | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array. |

## from

```TypeScript
public static from(arr: FixedArray<int>): Int16Array
```

Creates an array from an object of FixedArray&lt;int&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(arr: FixedArray<int>): Int16Array--><!--Device-Int16Array-public static from(arr: FixedArray<int>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | An instance of the FixedArray type to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from(set: Set<int>): Int16Array
```

Creates an array from a set of type std.core.Set&lt;int&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(set: Set<int>): Int16Array--><!--Device-Int16Array-public static from(set: Set<int>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;int&gt; | 是 | A set object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from(arr: Int16Array): Int16Array
```

Creates an array from an array of the same type.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(arr: Int16Array): Int16Array--><!--Device-Int16Array-public static from(arr: Int16Array): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Int16Array | 是 | An array to convert to a new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from(arr: Uint16Array): Int16Array
```

Creates an array from an array of the same up to the signedness type.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(arr: Uint16Array): Int16Array--><!--Device-Int16Array-public static from(arr: Uint16Array): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Uint16Array | 是 | An array to convert to a new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from(arr: Array<int>): Int16Array
```

Creates an array from an object of std.core.Array&lt;int&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(arr: Array<int>): Int16Array--><!--Device-Int16Array-public static from(arr: Array<int>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array&lt;int&gt; | 是 | An instance of the std.core.Array type to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from(arrayLike: ArrayLike<double>): Int16Array
```

Creates an array from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(arrayLike: ArrayLike<double>): Int16Array--><!--Device-Int16Array-public static from(arrayLike: ArrayLike<double>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | An array-like or iterable object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Int16Array
```

Creates an array from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Int16Array--><!--Device-Int16Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 | An array-like or iterable object to convert to an array. |
| mapfn | (v: T, k: double) =&gt; double | 是 | A mapping function to call on every element of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## from

```TypeScript
public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Int16Array
```

Creates an array from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Int16Array--><!--Device-Int16Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;double&gt; | 是 | An array-like or iterable object to convert to an array. |
| mapfn | (v: double, k: double) =&gt; double | 否 | A mapping function to call on every element of the array. Defaults to the identity function (returns the element unchanged). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | A new Int16Array |

## includes

```TypeScript
public includes(searchElement: short, fromIndex: int): boolean
```

Determines whether Int16Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public includes(searchElement: short, fromIndex: int): boolean--><!--Device-Int16Array-public includes(searchElement: short, fromIndex: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | short | 是 | The element to search for |
| fromIndex | int | 是 | The position in this array at which to begin searching for searchElement &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in Int16Array, false otherwise |

## includes

```TypeScript
public includes(searchElement: short): boolean
```

Determines whether Int16Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public includes(searchElement: short): boolean--><!--Device-Int16Array-public includes(searchElement: short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | short | 是 | The element to search for. The search starts at index 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in Int16Array, false otherwise |

## includes

```TypeScript
public includes(searchElement: double, fromIndex?: int): boolean
```

Determines whether Int16Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public includes(searchElement: double, fromIndex?: int): boolean--><!--Device-Int16Array-public includes(searchElement: double, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The element to search for |
| fromIndex | int | 否 | The position in this array at which to begin searching for searchElement. Defaults to 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in Int16Array, false otherwise |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

Returns the index of the first occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public indexOf(searchElement: int): int--><!--Device-Int16Array-public indexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. The search starts at index 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | index of element if found, -1 otherwise. |

## indexOf

```TypeScript
public indexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the first occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-Int16Array-public indexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. |
| fromIndex | int | 是 | The array index at which to begin the search. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | index of element if found, -1 otherwise. |

## indexOf

```TypeScript
public indexOf(searchElement: double, fromIndex?: int): int
```

Returns the index of the first occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public indexOf(searchElement: double, fromIndex?: int): int--><!--Device-Int16Array-public indexOf(searchElement: double, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The value to locate in the array. |
| fromIndex | int | 否 | The array index at which to begin the search. If fromIndex is undefined, the search starts at index 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | index of element if found, -1 otherwise. |

## join

```TypeScript
public join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public join(separator?: string): string--><!--Device-Int16Array-public join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | A string used to separate one element of an array from the next in the resulting string. If omitted, the array elements are separated with a comma. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a string with all array elements joined by the specified separator. |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

Returns a list of indices in the Int16Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public keys(): IterableIterator<int>--><!--Device-Int16Array-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | iterator over indices. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

Returns the index of the last occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public lastIndexOf(searchElement: int): int--><!--Device-Int16Array-public lastIndexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. The search begins at index length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | rightmost index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: double): int
```

Returns the index of the last occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public lastIndexOf(searchElement: double): int--><!--Device-Int16Array-public lastIndexOf(searchElement: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The value to locate in the array. The search begins at index length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | rightmost index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the last occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-Int16Array-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. |
| fromIndex | int | 是 | The array index at which to begin the search. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | rightmost index of searchElement. It must be less or equal than fromIndex. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: double, fromIndex: int | undefined): int
```

Returns the index of the last occurrence of a value in Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int--><!--Device-Int16Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The value to locate in the array. |
| fromIndex | int \| undefined | 是 | The array index at which to begin the search. Defaults to the array length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | rightmost index of searchElement. It must be less or equal than fromIndex. -1 if not found |

## map

```TypeScript
public map(fn: (val: double, index: int, array: Int16Array) => double): Int16Array
```

Creates a new Int16Array using fn(arr[i]) over all elements of current Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public map(fn: (val: double, index: int, array: Int16Array) => double): Int16Array--><!--Device-Int16Array-public map(fn: (val: double, index: int, array: Int16Array) => double): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Int16Array) =&gt; double | 是 | a function to apply for each element of current Int16Array |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array where for each element from current Int16Array fn was applied |

## of

```TypeScript
public static of(...items: FixedArray<short>): Int16Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static of(...items: FixedArray<short>): Int16Array--><!--Device-Int16Array-public static of(...items: FixedArray<short>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;short&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array |

## of

```TypeScript
public static of(...items: FixedArray<int>): Int16Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static of(...items: FixedArray<int>): Int16Array--><!--Device-Int16Array-public static of(...items: FixedArray<int>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array |

## of

```TypeScript
public static of(...items: FixedArray<double>): Int16Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static of(...items: FixedArray<double>): Int16Array--><!--Device-Int16Array-public static of(...items: FixedArray<double>): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array |

## of

```TypeScript
public static of(): Int16Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static of(): Int16Array--><!--Device-Int16Array-public static of(): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array |

## reduce

```TypeScript
public reduce<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in an array.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) => U,        initialValue: U): U--><!--Device-Int16Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) =&gt; U | 是 | A function that accepts four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The parameter which value is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | the accumulated result from the last call to the callback function. |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Int16Array) => double): double
```

Calls the specified callback function for all the elements in an array.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Int16Array) => double): double--><!--Device-Int16Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Int16Array) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Int16Array) =&gt; double | 是 | A function that accepts four arguments. The reduce method calls the callbackfn function one time for each element in the array. The first call to the callbackfn function provides array first element value as an argument |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public reduceRight<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) => U,        initialValue: U): U--><!--Device-Int16Array-public reduceRight<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Int16Array) =&gt; U | 是 | A function that accepts four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The parameter which value is used as the initial value to start the accumulation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Int16Array) => double): double
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Int16Array) => double): double--><!--Device-Int16Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Int16Array) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Int16Array) =&gt; double | 是 | A function that accepts four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. The first call to the callbackfn function provides array last element value as an argument. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the accumulated result from the last call to the callback function. |

## reverse

```TypeScript
public reverse(): Int16Array
```

Creates a new Int16Array using reversed data from the current one

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public reverse(): Int16Array--><!--Device-Int16Array-public reverse(): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array using reversed data from the current one |

## set

```TypeScript
public set(insertPos: int, val: short): void
```

Assigns val as element on insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(insertPos: int, val: short): void--><!--Device-Int16Array-public set(insertPos: int, val: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | short | 是 | value to set |

## set

```TypeScript
public set(insertPos: int, val: double): void
```

Assigns val as element on insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(insertPos: int, val: double): void--><!--Device-Int16Array-public set(insertPos: int, val: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | double | 是 | value to set |

## set

```TypeScript
public set(arr: FixedArray<short>): void
```

Copies all elements of arr to the current Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(arr: FixedArray<short>): void--><!--Device-Int16Array-public set(arr: FixedArray<short>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | 是 | array to copy data from |

## set

```TypeScript
public set(arr: FixedArray<short>, insertPos: int): void
```

Copies all elements of arr to the current Int16Array starting from insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(arr: FixedArray<short>, insertPos: int): void--><!--Device-Int16Array-public set(arr: FixedArray<short>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | 是 | array to copy data from |
| insertPos | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(arr: FixedArray<double>): void
```

Copies all elements of arr to the current Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(arr: FixedArray<double>): void--><!--Device-Int16Array-public set(arr: FixedArray<double>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | array to copy data from |

## set

```TypeScript
public set(arr: FixedArray<double>, insertPos: int): void
```

Copies all elements of arr to the current Int16Array starting from insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(arr: FixedArray<double>, insertPos: int): void--><!--Device-Int16Array-public set(arr: FixedArray<double>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | array to copy data from |
| insertPos | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(array: Int16Array): void
```

Copies all elements of array to the current Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(array: Int16Array): void--><!--Device-Int16Array-public set(array: Int16Array): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | Int16Array | 是 | array to copy data from |

## set

```TypeScript
public set(array: Int16Array, offset: int): void
```

Copies all elements of arr to the current Int16Array starting from offset.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(array: Int16Array, offset: int): void--><!--Device-Int16Array-public set(array: Int16Array, offset: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | Int16Array | 是 | array to copy data from |
| offset | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(array: ArrayLike<double>, offset: int = 0): void
```

Copies elements from an ArrayLike object to the Int16Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public set(array: ArrayLike<double>, offset: int = 0): void--><!--Device-Int16Array-public set(array: ArrayLike<double>, offset: int = 0): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | An ArrayLike object containing the elements to copy. |
| offset | int | 是 | Optional. The offset into the target array at which to begin writing values from the source array. The default value is 0. |

## slice

```TypeScript
public slice(begin: int): Int16Array
```

Creates a slice of current Int16Array using range [begin, this.length).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public slice(begin: int): Int16Array--><!--Device-Int16Array-public slice(begin: int): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | start index to be taken into slice |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with elements of current Int16Array[begin, this.length) |

## slice

```TypeScript
public slice(begin?: int, end?: int): Int16Array
```

Creates a slice of current Int16Array using range [begin, end)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public slice(begin?: int, end?: int): Int16Array--><!--Device-Int16Array-public slice(begin?: int, end?: int): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start index to be taken into slice. Defaults to 0. |
| end | int | 否 | last index to be taken into slice. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with elements of current Int16Array[begin;end), where end index is excluded |

## some

```TypeScript
public some(predicate: (element: double, index: int, array: Int16Array) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public some(predicate: (element: double, index: int, array: Int16Array) => boolean): boolean--><!--Device-Int16Array-public some(predicate: (element: double, index: int, array: Int16Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Int16Array) =&gt; boolean | 是 | A function that accepts three arguments. The some method calls the predicate function for each element in the array until the predicate returns a true or until the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | false unless predicate function returns true for an array element, in which case true is immediately returned. |

## sort

```TypeScript
public sort(): this
```

Sorts in-place by numeric value in ascending order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public sort(): this--><!--Device-Int16Array-public sort(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | sorted Int16Array |

## sort

```TypeScript
public sort(compareFn?: (a: double, b: double) => int): this
```

Sorts in-place

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public sort(compareFn?: (a: double, b: double) => int): this--><!--Device-Int16Array-public sort(compareFn?: (a: double, b: double) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: double, b: double) =&gt; int | 否 | comparator used to determine the order of the elements. compareFn returns a negative value if first argument is less than second argument, zero if they're equal and a positive value otherwise. Defaults to an ascending numeric sort. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | sorted Int16Array |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): Int16Array
```

Creates a new Int16Array that shares the same underlying ArrayBuffer as the current array,optionally with a restricted range.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public subarray(begin?: int, end?: int): Int16Array--><!--Device-Int16Array-public subarray(begin?: int, end?: int): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start index, inclusive. Defaults to 0. |
| end | int | 否 | last index, exclusive. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with the same underlying ArrayBuffer |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Int16Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | 否 | An object with some or all of the properties of the Intl.NumberFormat options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the locale-specific conversion |

## toReversed

```TypeScript
public toReversed(): Int16Array
```

Returns a new Int16Array with the elements in reverse order. The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public toReversed(): Int16Array--><!--Device-Int16Array-public toReversed(): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with the elements in reverse order. |

## toSorted

```TypeScript
public toSorted(): Int16Array
```

Returns a new Int16Array with the elements sorted in ascending order. The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public toSorted(): Int16Array--><!--Device-Int16Array-public toSorted(): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with the elements sorted in ascending order. |

## toString

```TypeScript
public toString(): string
```

Returns a comma-separated string representation of the Int16Array elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public toString(): string--><!--Device-Int16Array-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a comma-separated string of the array elements. |

## valueOf

```TypeScript
public valueOf(): Int16Array
```

Returns the object itself

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public valueOf(): Int16Array--><!--Device-Int16Array-public valueOf(): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array |  |

## values

```TypeScript
public values(): IterableIterator<double>
```

Returns array values iterator

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public values(): IterableIterator<double>--><!--Device-Int16Array-public values(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | an iterator |

## with

```TypeScript
public with(index: int, value: short): Int16Array
```

Returns a new Int16Array with the element at the given index replaced by the given value.The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public with(index: int, value: short): Int16Array--><!--Device-Int16Array-public with(index: int, value: short): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| value | short | 是 | value to set |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with the element at index replaced by value. |

## with

```TypeScript
public with(index: int, value: double): Int16Array
```

Returns a new Int16Array with the element at the given index replaced by the given value.The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public with(index: int, value: double): Int16Array--><!--Device-Int16Array-public with(index: int, value: double): Int16Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change. &lt;br&gt;The value should be an integer. |
| value | double | 是 | value to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int16Array | a new Int16Array with the element at index replaced by value. |

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 2
```

Number of bytes occupied by each element

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public static readonly BYTES_PER_ELEMENT: int = 2--><!--Device-Int16Array-public static readonly BYTES_PER_ELEMENT: int = 2-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

Underlying ArrayBuffer

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public readonly buffer: ArrayBuffer--><!--Device-Int16Array-public readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public readonly byteLength: int
```

Number of bytes used The value should be an integer.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public readonly byteLength: int--><!--Device-Int16Array-public readonly byteLength: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public readonly byteOffset: int
```

Byte offset within the underlying ArrayBuffer The value should be an integer.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public readonly byteOffset: int--><!--Device-Int16Array-public readonly byteOffset: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
public get length(): int
```

Number of short stored in Int16Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public get length(): int--><!--Device-Int16Array-public get length(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'Int16Array'
```

String \"Int16Array\", representing the type name of this typed array.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int16Array-public readonly name: string = 'Int16Array'--><!--Device-Int16Array-public readonly name: string = 'Int16Array'-End-->

**系统能力：** SystemCapability.Utils.Lang

