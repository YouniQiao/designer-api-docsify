# Uint8Array

class Uint8Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Uint8Array--><!--Device-unnamed-export class Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
public $_get(i: int): double
```

Returns an instance of number at passed index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_get(i: int): double--><!--Device-Uint8Array-public $_get(i: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | index to look at &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the raw numeric value at index. |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<double>
```

Iteratorable interface implementation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_iterator(): IterableIterator<double>--><!--Device-Uint8Array-public $_iterator(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | iterator that yields each element in order. |

## $_set

```TypeScript
public $_set(index: int, val: int): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_set(index: int, val: int): void--><!--Device-Uint8Array-public $_set(index: int, val: int): void-End-->

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

<!--Device-Uint8Array-public $_set(index: int, val: double): void--><!--Device-Uint8Array-public $_set(index: int, val: double): void-End-->

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

Returns an instance of primitive type at passed index if index is correct.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public at(index: int): double | undefined--><!--Device-Uint8Array-public at(index: int): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to look at &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the element at the index, or undefined if out of bounds. |

## constructor

```TypeScript
public constructor()
```

Creates an empty Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor()--><!--Device-Uint8Array-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

Creates an Uint8Array with respect to length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(length: int)--><!--Device-Uint8Array-public constructor(length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | Number of elements &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(length: double)
```

Creates an Uint8Array with respect to length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(length: double)--><!--Device-Uint8Array-public constructor(length: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | Number of elements |

## constructor

```TypeScript
public constructor(numbers: FixedArray<int>)
```

Creates an Uint8Array from FixedArray&lt;int&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(numbers: FixedArray<int>)--><!--Device-Uint8Array-public constructor(numbers: FixedArray<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;int&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(numbers: FixedArray<double>)
```

Creates an Uint8Array from FixedArray&lt;double&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(numbers: FixedArray<double>)--><!--Device-Uint8Array-public constructor(numbers: FixedArray<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;double&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(numbers: Array<int>)
```

Creates an Uint8Array from Array&lt;int&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(numbers: Array<int>)--><!--Device-Uint8Array-public constructor(numbers: Array<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | Array&lt;int&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(other: Uint8Array)
```

Creates a copy of Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(other: Uint8Array)--><!--Device-Uint8Array-public constructor(other: Uint8Array)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Uint8Array | 是 | data initializer |

## constructor

```TypeScript
public constructor(elements: Iterable<double>)
```

Creates an Uint8Array with respect to data accessed via Iterable&lt;double&gt; interface

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(elements: Iterable<double>)--><!--Device-Uint8Array-public constructor(elements: Iterable<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;double&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)
```

Creates an Uint8Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)--><!--Device-Uint8Array-public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayBufferLike](arkts-arkts-arraybufferlike-t.md) | 是 | data initializer |
| byteOffset | int | 是 | byte offset from begin of the buf &lt;br&gt;The value should be an integer. |
| length | int | 是 | size of elements of type int in newly created Uint8Array &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

Creates an Uint8Array with respect to buf and byteOffset.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | int | 是 | byte offset from begin of the buf &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

Creates an Uint8Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | double \| undefined | 是 | byte offset from begin of the buf |
| length | double \| undefined | 是 | size of elements of type int in newly created Uint8Array |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

Creates an Uint8Array with respect to buf and byteOffset.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | double | 是 | byte offset from begin of the buf |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

Creates an Uint8Array with respect to buf.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-Uint8Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; \| ArrayBuffer | 是 | data initializer |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): Uint8Array
```

Makes a copy of internal elements to targetPos from startPos to endPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public copyWithin(target: int, start: int, end?: int): Uint8Array--><!--Device-Uint8Array-public copyWithin(target: int, start: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | insert index to place copied elements |
| start | int | 是 | start index to begin copy from |
| end | int | 否 | last index to end copy from, excluded, defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | the modified Uint8Array. |

## copyWithin

```TypeScript
public copyWithin(target: int): Uint8Array
```

Makes a copy of internal elements to targetPos from begin to end of Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public copyWithin(target: int): Uint8Array--><!--Device-Uint8Array-public copyWithin(target: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | insert index to place copied elements &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | the modified Uint8Array. |

## entries

```TypeScript
public entries(): IterableIterator<[int, double]>
```

Returns an array of key, value pairs for every entry in the Uint8Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public entries(): IterableIterator<[int, double]>--><!--Device-Uint8Array-public entries(): IterableIterator<[int, double]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, double]&gt; | iterator over [index, value] pairs for each element. |

## every

```TypeScript
public every(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean
```

Determines whether the specified callback function returns true for all elements of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public every(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean--><!--Device-Uint8Array-public every(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Uint8Array) =&gt; boolean | 是 | A function that accepts three arguments. The every method calls the predicate function for each element in the array until the predicate returns a false, or until the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true unless predicate function returns a false for an array element, in which case false is immediately returned. |

## fill

```TypeScript
public fill(value: int, start?: int, end?: int): Uint8Array
```

Fills the Uint8Array with specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public fill(value: int, start?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public fill(value: int, start?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | new value. &lt;br&gt;The value should be an integer. |
| start | int | 否 | start index to begin fill from &lt;br&gt;The value should be an integer. |
| end | int | 否 | last index to end fill from, excluded &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | modified Uint8Array |

## fill

```TypeScript
public fill(value: double, start?: int, end?: int): Uint8Array
```

Fills the Uint8Array with specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public fill(value: double, start?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public fill(value: double, start?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | new value. |
| start | int | 否 | start index to begin fill from &lt;br&gt;The value should be an integer. |
| end | int | 否 | last index to end fill from, excluded &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | modified Uint8Array |

## filter

```TypeScript
public filter(fn: (val: double, index: int, array: Uint8Array) => boolean): Uint8Array
```

Creates a new Uint8Array from current Uint8Array based on a condition fn.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public filter(fn: (val: double, index: int, array: Uint8Array) => boolean): Uint8Array--><!--Device-Uint8Array-public filter(fn: (val: double, index: int, array: Uint8Array) => boolean): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; boolean | 是 | the condition to apply for each element |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with the elements that pass the test. |

## find

```TypeScript
public find(predicate: (value: double, index: int, array: Uint8Array) => boolean): double | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public find(predicate: (value: double, index: int, array: Uint8Array) => boolean): double | undefined--><!--Device-Uint8Array-public find(predicate: (value: double, index: int, array: Uint8Array) => boolean): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, array: Uint8Array) =&gt; boolean | 是 | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, find immediately returns that element value. Otherwise, find returns undefined |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the found element, or undefined if no element matches. |

## findIndex

```TypeScript
public findIndex(predicate: (value: double, index: int, obj: Uint8Array) => boolean): int
```

Returns the index of the first element in the array where predicate is true, and -1otherwise

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public findIndex(predicate: (value: double, index: int, obj: Uint8Array) => boolean): int--><!--Device-Uint8Array-public findIndex(predicate: (value: double, index: int, obj: Uint8Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Uint8Array) =&gt; boolean | 是 | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, findIndex immediately returns that element index. Otherwise, findIndex returns -1 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Index of the first matched element |

## findLast

```TypeScript
public findLast(fn: (val: double, index: int, array: Uint8Array) => boolean): double
```

Finds the last element in the Uint8Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public findLast(fn: (val: double, index: int, array: Uint8Array) => boolean): double--><!--Device-Uint8Array-public findLast(fn: (val: double, index: int, array: Uint8Array) => boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; boolean | 是 | condition |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the last element that satisfies fn |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: double, index: int, array: Uint8Array) => boolean): int
```

Finds an index of the last element in the Uint8Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public findLastIndex(fn: (val: double, index: int, array: Uint8Array) => boolean): int--><!--Device-Uint8Array-public findLastIndex(fn: (val: double, index: int, array: Uint8Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; boolean | 是 | condition |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the index of the last element that satisfies fn, -1 otherwise |

## forEach

```TypeScript
public forEach(callbackfn: (value: double, index: int, array: Uint8Array) => void): void
```

Performs the specified action for each element in Uint8Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public forEach(callbackfn: (value: double, index: int, array: Uint8Array) => void): void--><!--Device-Uint8Array-public forEach(callbackfn: (value: double, index: int, array: Uint8Array) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: double, index: int, array: Uint8Array) =&gt; void | 是 | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array. |

## from

```TypeScript
public static from(arr: FixedArray<int>): Uint8Array
```

Creates an array from an object of FixedArray&lt;int&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: FixedArray<int>): Uint8Array--><!--Device-Uint8Array-public static from(arr: FixedArray<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | An instance of the FixedArray type to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from(set: Set<int>): Uint8Array
```

Creates an array from a set of type std.core.Set&lt;int&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(set: Set<int>): Uint8Array--><!--Device-Uint8Array-public static from(set: Set<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;int&gt; | 是 | A set object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from(arr: Uint8Array): Uint8Array
```

Creates an array from an array of the same type.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: Uint8Array): Uint8Array--><!--Device-Uint8Array-public static from(arr: Uint8Array): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Uint8Array | 是 | An array to convert to a new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from(arr: Int8Array): Uint8Array
```

Creates an array from an array of the same up to the signess type.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: Int8Array): Uint8Array--><!--Device-Uint8Array-public static from(arr: Int8Array): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Int8Array | 是 | An array to convert to a new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from(arr: Array<int>): Uint8Array
```

Creates an array from an object of std.core.Array&lt;int&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: Array<int>): Uint8Array--><!--Device-Uint8Array-public static from(arr: Array<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array&lt;int&gt; | 是 | An instance of the std.core.Array type to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from(arr: ArrayLike<double>): Uint8Array
```

Creates an array from an array-like object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: ArrayLike<double>): Uint8Array--><!--Device-Uint8Array-public static from(arr: ArrayLike<double>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | An array-like object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8Array
```

Creates an array from an array-like object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8Array--><!--Device-Uint8Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 | An array-like object to convert to an array. |
| mapfn | (v: T, k: double) =&gt; double | 是 | A mapping function to call on every element of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## from

```TypeScript
public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8Array
```

Creates an array from an iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8Array--><!--Device-Uint8Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;double&gt; | 是 | An iterable object to convert to an array. |
| mapfn | (v: double, k: double) =&gt; double | 否 | A mapping function to call on every element of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | A new Uint8Array |

## includes

```TypeScript
public includes(searchElement: int, fromIndex: int): boolean
```

Determines whether Uint8Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public includes(searchElement: int, fromIndex: int): boolean--><!--Device-Uint8Array-public includes(searchElement: int, fromIndex: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The element to search for &lt;br&gt;The value should be an integer. |
| fromIndex | int | 是 | The position in this array at which to begin searching for searchElement &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in Uint8Array, false otherwise |

## includes

```TypeScript
public includes(searchElement: int): boolean
```

Determines whether Uint8Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public includes(searchElement: int): boolean--><!--Device-Uint8Array-public includes(searchElement: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The element to search for. The search starts at index 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in Uint8Array, false otherwise |

## includes

```TypeScript
public includes(searchElement: double, fromIndex?: int): boolean
```

Determines whether Uint8Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public includes(searchElement: double, fromIndex?: int): boolean--><!--Device-Uint8Array-public includes(searchElement: double, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The element to search for. |
| fromIndex | int | 否 | The position in this array at which to begin searching for searchElement If fromIndex is undefined, the search starts at index 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in Uint8Array, false otherwise |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

Returns the index of the first occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public indexOf(searchElement: int): int--><!--Device-Uint8Array-public indexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. The search starts at index 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | index of element if present, -1 otherwise |

## indexOf

```TypeScript
public indexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the first occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-Uint8Array-public indexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. |
| fromIndex | int | 是 | The array index at which to begin the search. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | index of element if present, -1 otherwise |

## indexOf

```TypeScript
public indexOf(searchElement: double, fromIndex?: int): int
```

Returns the index of the first occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public indexOf(searchElement: double, fromIndex?: int): int--><!--Device-Uint8Array-public indexOf(searchElement: double, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The value to locate in the array. |
| fromIndex | int | 否 | The array index at which to begin the search. If fromIndex is omitted, the search starts at index 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | index of element if present, -1 otherwise |

## join

```TypeScript
public join(separator?: string): string
```

Adds all the elements of an array separated by the specified separator string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public join(separator?: string): string--><!--Device-Uint8Array-public join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | A string used to separate one element of an array from the next in the resulting string. If omitted, the array elements are separated with a comma. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a string of all array elements joined by the separator. |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

Returns an list of keys in Uint8Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public keys(): IterableIterator<int>--><!--Device-Uint8Array-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | iterator over the array indices. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

Returns the index of the last occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: int): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. The search begins at index length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | right-most index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: double): int
```

Returns the index of the last occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: double): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The value to locate in the array. The search begins at index length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | right-most index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the last occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | The value to locate in the array. |
| fromIndex | int | 是 | The array index at which to begin the search. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | right-most index of searchElement. It must be less or equal than fromIndex. -1 if not found. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: double, fromIndex: int | undefined): int
```

Returns the index of the last occurrence of a value in Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | The value to locate in the array. |
| fromIndex | int \| undefined | 是 | The array index at which to begin the search. If fromIndex is undefined, the search starts at index 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | right-most index of searchElement. It must be less or equal than fromIndex. -1 if not found. |

## map

```TypeScript
public map(fn: (val: double, index: int, array: Uint8Array) => number): Uint8Array
```

Creates a new Uint8Array using fn(arr[i]) over all elements of current Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public map(fn: (val: double, index: int, array: Uint8Array) => number): Uint8Array--><!--Device-Uint8Array-public map(fn: (val: double, index: int, array: Uint8Array) => number): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; number | 是 | a function to apply for each element of current Uint8Array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with each element being the result of the callback function. |

## of

```TypeScript
public static of(...items: FixedArray<short>): Uint8Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(...items: FixedArray<short>): Uint8Array--><!--Device-Uint8Array-public static of(...items: FixedArray<short>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;short&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array |

## of

```TypeScript
public static of(...items: FixedArray<int>): Uint8Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(...items: FixedArray<int>): Uint8Array--><!--Device-Uint8Array-public static of(...items: FixedArray<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array |

## of

```TypeScript
public static of(...items: FixedArray<double>): Uint8Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(...items: FixedArray<double>): Uint8Array--><!--Device-Uint8Array-public static of(...items: FixedArray<double>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array |

## of

```TypeScript
public static of(): Uint8Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(): Uint8Array--><!--Device-Uint8Array-public static of(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array |

## reduce

```TypeScript
public reduce<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in an array.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) => U,        initialValue: U): U--><!--Device-Uint8Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) =&gt; U | 是 | A function that accepts four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The parameter which value is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | the accumulated result from the last call to the callback function. |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Uint8Array) => double): double
```

Calls the specified callback function for all the elements in an array.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double--><!--Device-Uint8Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Uint8Array) =&gt; double | 是 | A function that accepts four arguments. The reduce method calls the callbackfn function one time for each element in the array. The first call to the callbackfn function provides array first element value as an argument |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight<U = double>(callbackfn: (previousValue: U, currentValue: double,
        currentIndex: int, array: Uint8Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduceRight<U = double>(callbackfn: (previousValue: U, currentValue: double,        currentIndex: int, array: Uint8Array) => U, initialValue: U): U--><!--Device-Uint8Array-public reduceRight<U = double>(callbackfn: (previousValue: U, currentValue: double,        currentIndex: int, array: Uint8Array) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double,         currentIndex: int, array: Uint8Array) =&gt; U | 是 | A function that accepts four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The parameter which value is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Uint8Array) => double): double
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double--><!--Device-Uint8Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Uint8Array) =&gt; double | 是 | A function that accepts four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. The first call to the callbackfn function provides array last element value as an argument |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the accumulated result from the last call to the callback function. |

## reverse

```TypeScript
public reverse(): Uint8Array
```

Creates a new Uint8Array using reversed data from the current one.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reverse(): Uint8Array--><!--Device-Uint8Array-public reverse(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with the elements in reverse order. |

## set

```TypeScript
public set(insertPos: int, val: int): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(insertPos: int, val: int): void--><!--Device-Uint8Array-public set(insertPos: int, val: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | int | 是 | value to set &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(insertPos: int, val: double): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(insertPos: int, val: double): void--><!--Device-Uint8Array-public set(insertPos: int, val: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | double | 是 | value to set |

## set

```TypeScript
public set(arr: FixedArray<int>, insertPos: int): void
```

Copies all elements of arr to the current Uint8Array starting from insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<int>, insertPos: int): void--><!--Device-Uint8Array-public set(arr: FixedArray<int>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | array to copy data from |
| insertPos | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(arr: FixedArray<double>, insertPos: int): void
```

Copies all elements of arr to the current Uint8Array starting from insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<double>, insertPos: int): void--><!--Device-Uint8Array-public set(arr: FixedArray<double>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | array to copy data from |
| insertPos | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(arr: FixedArray<int>): void
```

Copies all elements of arr to the current Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<int>): void--><!--Device-Uint8Array-public set(arr: FixedArray<int>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | array to copy data from |

## set

```TypeScript
public set(arr: FixedArray<double>): void
```

Copies all elements of arr to the current Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<double>): void--><!--Device-Uint8Array-public set(arr: FixedArray<double>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | array to copy data from |

## set

```TypeScript
public set(array: Uint8Array): void
```

Copies all elements of arr to the current Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(array: Uint8Array): void--><!--Device-Uint8Array-public set(array: Uint8Array): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | Uint8Array | 是 | array to copy data from |

## set

```TypeScript
public set(array: Uint8Array, offset: int): void
```

Copies all elements of arr to the current Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(array: Uint8Array, offset: int): void--><!--Device-Uint8Array-public set(array: Uint8Array, offset: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | Uint8Array | 是 | array to copy data from |
| offset | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(array: ArrayLike<double>, offset: int = 0): void
```

Copies elements from an ArrayLike object to the Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(array: ArrayLike<double>, offset: int = 0): void--><!--Device-Uint8Array-public set(array: ArrayLike<double>, offset: int = 0): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | An ArrayLike object containing the elements to copy. |
| offset | int | 是 | Optional. The offset into the target array at which to begin writing values from the source array. The default value is 0. &lt;br&gt;The value should be an integer. |

## slice

```TypeScript
public slice(begin?: int, end?: int): Uint8Array
```

Creates a slice of current Uint8Array using range [begin, end]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public slice(begin?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public slice(begin?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start - index to be taken into slice |
| end | int | 否 | last index to be taken into slice |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with elements of current Uint8Array[begin;end), where end index is excluded |

## slice

```TypeScript
public slice(begin: int): Uint8Array
```

Creates a slice of current Uint8Array using range [begin, this.lengthInt].

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public slice(begin: int): Uint8Array--><!--Device-Uint8Array-public slice(begin: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | start index to be taken into slice. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with elements of current Uint8Array[begin, this.lengthInt]. |

## some

```TypeScript
public some(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public some(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean--><!--Device-Uint8Array-public some(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Uint8Array) =&gt; boolean | 是 | A function that accepts three arguments. The some method calls the predicate function for each element in the array until the predicate returns a true or until the end of the array. |

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

<!--Device-Uint8Array-public sort(): this--><!--Device-Uint8Array-public sort(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | sorted Uint8Array |

## sort

```TypeScript
public sort(compareFn?: (a: double, b: double) => int): this
```

Sorts in-place

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public sort(compareFn?: (a: double, b: double) => int): this--><!--Device-Uint8Array-public sort(compareFn?: (a: double, b: double) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: double, b: double) =&gt; int | 否 | comparator _ used to determine the order of the elements. compareFn returns a negative value if first argument is less than second argument, zero if they're equal and a positive value otherwise. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | sorted Uint8Array |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): Uint8Array
```

Creates a Uint8Array with the same underlying Buffer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public subarray(begin?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public subarray(begin?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start index, inclusive |
| end | int | 否 | last index, exclusive |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with the same underlying Buffer |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Uint8Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
public toReversed(): Uint8Array
```

Creates a reversed copy

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toReversed(): Uint8Array--><!--Device-Uint8Array-public toReversed(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a reversed copy |

## toSorted

```TypeScript
public toSorted(): Uint8Array
```

Returns a new Uint8Array with the elements sorted in ascending order.The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toSorted(): Uint8Array--><!--Device-Uint8Array-public toSorted(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with the elements sorted. |

## toString

```TypeScript
public toString(): string
```

Returns a string representation of the Uint8Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toString(): string--><!--Device-Uint8Array-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a string representation of the Uint8Array |

## valueOf

```TypeScript
public valueOf(): Uint8Array
```

Returns the primitive value of the Uint8Array, which is the array object itself.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public valueOf(): Uint8Array--><!--Device-Uint8Array-public valueOf(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | the Uint8Array object itself. |

## values

```TypeScript
public values(): IterableIterator<double>
```

Returns array values iterator

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public values(): IterableIterator<double>--><!--Device-Uint8Array-public values(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | iterator that yields each element in order. |

## with

```TypeScript
public with(index: int, value: int): Uint8Array
```

Creates a copy with replaced value on index

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public with(index: int, value: int): Uint8Array--><!--Device-Uint8Array-public with(index: int, value: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| value | int | 是 | value to set &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | a new Uint8Array with the element at index replaced. |

## with

```TypeScript
public with(index: int, value: double): Uint8Array
```

Creates a copy with replaced value on index

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public with(index: int, value: double): Uint8Array--><!--Device-Uint8Array-public with(index: int, value: double): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| value | double | 是 | value to set |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | an Uint8Array with replaced value on index |

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 1
```

Number of bytes occupied by each element

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static readonly BYTES_PER_ELEMENT: int = 1--><!--Device-Uint8Array-public static readonly BYTES_PER_ELEMENT: int = 1-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

Underlying Buffer.

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public readonly buffer: ArrayBuffer--><!--Device-Uint8Array-public readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public get byteLength(): int
```

Number of bytes used

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public get byteLength(): int--><!--Device-Uint8Array-public get byteLength(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public get byteOffset(): int
```

Byte offset within the underlying Buffer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public get byteOffset(): int--><!--Device-Uint8Array-public get byteOffset(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
public get length(): int
```

The number of elements stored in the Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public get length(): int--><!--Device-Uint8Array-public get length(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'Uint8Array'
```

String \"Uint8Array\"

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public readonly name: string = 'Uint8Array'--><!--Device-Uint8Array-public readonly name: string = 'Uint8Array'-End-->

**系统能力：** SystemCapability.Utils.Lang

