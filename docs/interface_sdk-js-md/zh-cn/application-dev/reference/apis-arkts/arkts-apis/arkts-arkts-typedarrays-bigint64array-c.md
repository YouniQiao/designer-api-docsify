# BigInt64Array

class BigInt64Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class BigInt64Array--><!--Device-unnamed-export class BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
public $_get(index: int): BigInt
```

Returns an instance of BigInt at passed index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_get(index: int): BigInt--><!--Device-BigInt64Array-public $_get(index: int): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to look at. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | the raw numeric value at index. |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<BigInt>
```

Iterable interface implementation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_iterator(): IterableIterator<BigInt>--><!--Device-BigInt64Array-public $_iterator(): IterableIterator<BigInt>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;BigInt&gt; | iterator over all elements |

## $_set

```TypeScript
public $_set(index: int, val: long): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_set(index: int, val: long): void--><!--Device-BigInt64Array-public $_set(index: int, val: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value range is all integers. |
| val | long | 是 | value to set |

## $_set

```TypeScript
public $_set(index: int, val: BigInt): void
```

Assigns val as element on index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_set(index: int, val: BigInt): void--><!--Device-BigInt64Array-public $_set(index: int, val: BigInt): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change |
| val | [BigInt](arkts-arkts-bigint-c.md) | 是 | value to set |

## at

```TypeScript
public at(index: int): BigInt | undefined
```

Returns an instance of primitive type at passed index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public at(index: int): BigInt | undefined--><!--Device-BigInt64Array-public at(index: int): BigInt | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to look at &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | the raw numeric value at index, or undefined if the index is out of bounds. |

## constructor

```TypeScript
public constructor()
```

Creates an empty BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor()--><!--Device-BigInt64Array-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

Creates a BigInt64Array with respect to length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(length: int)--><!--Device-BigInt64Array-public constructor(length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | double of elements &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(length: double)
```

Creates a BigInt64Array with respect to length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(length: double)--><!--Device-BigInt64Array-public constructor(length: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | double of elements |

## constructor

```TypeScript
public constructor(other: BigInt64Array)
```

Creates a copy of BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(other: BigInt64Array)--><!--Device-BigInt64Array-public constructor(other: BigInt64Array)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | 是 | data initializer |

## constructor

```TypeScript
public constructor(doubles: FixedArray<int>)
```

Creates a BigInt64Array from FixedArray&lt;int&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(doubles: FixedArray<int>)--><!--Device-BigInt64Array-public constructor(doubles: FixedArray<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubles | FixedArray&lt;int&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(doubles: FixedArray<double>)
```

Creates a BigInt64Array from FixedArray&lt;double&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(doubles: FixedArray<double>)--><!--Device-BigInt64Array-public constructor(doubles: FixedArray<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubles | FixedArray&lt;double&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(doubles: FixedArray<bigint>)
```

Creates a BigInt64Array from FixedArray&lt;bigint&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(doubles: FixedArray<bigint>)--><!--Device-BigInt64Array-public constructor(doubles: FixedArray<bigint>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubles | FixedArray&lt;bigint&gt; | 是 | data initializer |

## constructor

```TypeScript
public constructor(elements: Iterable<BigInt>)
```

Creates a BigInt64Array with respect to data accessed via Iterable&lt;double&gt; interface

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(elements: Iterable<BigInt>)--><!--Device-BigInt64Array-public constructor(elements: Iterable<BigInt>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;BigInt&gt; | 是 | an iterable object |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

Creates a BigInt64Array with respect to buf and byteOffset.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

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

Creates a BigInt64Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

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

Creates a BigInt64Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | int | 是 | byte offset from begin of the buf &lt;br&gt;The value should be an integer. |
| length | int | 是 | size of elements of type long in newly created BigInt64Array &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

Creates a BigInt64Array with respect to data, byteOffset and length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | data initializer |
| byteOffset | double \| undefined | 是 | byte offset from begin of the buf |
| length | double \| undefined | 是 | size of elements of type long in newly created BigInt64Array |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

Creates a BigInt64Array with respect to buf.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-BigInt64Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; \| ArrayBuffer | 是 | data initializer |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): BigInt64Array
```

Makes a copy of internal elements to targetPos from startPos to endPos.See rules of parameters normalization on

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public copyWithin(target: int, start: int, end?: int): BigInt64Array--><!--Device-BigInt64Array-public copyWithin(target: int, start: int, end?: int): BigInt64Array-End-->

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
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | The modified BigInt64Array instance. |

## copyWithin

```TypeScript
public copyWithin(target: int): BigInt64Array
```

Makes a copy of internal elements to targetPos from begin to end of BigInt64Array.See rules of parameters normalization on

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public copyWithin(target: int): BigInt64Array--><!--Device-BigInt64Array-public copyWithin(target: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | insert index to place copied elements &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | The modified BigInt64Array instance. |

## entries

```TypeScript
public entries(): IterableIterator<[int, BigInt]>
```

Returns an array of key, value pairs for every entry in the BigInt64Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public entries(): IterableIterator<[int, BigInt]>--><!--Device-BigInt64Array-public entries(): IterableIterator<[int, BigInt]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, BigInt]&gt; | key, value pairs for every entry in the array |

## every

```TypeScript
public every(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean
```

Determines whether the specified callback function returns true for all elements of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public every(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean--><!--Device-BigInt64Array-public every(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | A function that accepts three arguments. The every method calls the predicate function for each element in the array until the predicate returns a false, or until the end of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true unless predicate function returns a false for an array element, in which case false is immediately returned. |

## fill

```TypeScript
public fill(value: long, start?: int, end?: int): this
```

Fills the BigInt64Array with specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public fill(value: long, start?: int, end?: int): this--><!--Device-BigInt64Array-public fill(value: long, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | new value |
| start | int | 否 | start index to begin fill from. Defaults to 0. |
| end | int | 否 | last index to end fill from, excluded. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | modified BigInt64Array |

## fill

```TypeScript
public fill(value: BigInt, start?: int, end?: int): this
```

Fills the BigInt64Array with specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public fill(value: BigInt, start?: int, end?: int): this--><!--Device-BigInt64Array-public fill(value: BigInt, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 | new value |
| start | int | 否 | start index to begin fill from. Defaults to 0. |
| end | int | 否 | last index to end fill from, excluded. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | modified BigInt64Array |

## filter

```TypeScript
public filter(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt64Array
```

Creates a new BigInt64Array from current BigInt64Array based on a condition fn.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public filter(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt64Array--><!--Device-BigInt64Array-public filter(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | the condition to apply for each element |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array |

## find

```TypeScript
public find(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): BigInt | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public find(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): BigInt | undefined--><!--Device-BigInt64Array-public find(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): BigInt | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: BigInt, index: int, obj: BigInt64Array) =&gt; boolean | 是 | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, find immediately returns that element value. Otherwise, find returns undefined |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) |  |

## findIndex

```TypeScript
public findIndex(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): int
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findIndex(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): int--><!--Device-BigInt64Array-public findIndex(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: BigInt, index: int, obj: BigInt64Array) =&gt; boolean | 是 | find calls predicate once for each element of the array, in ascending order, until it finds one where predicate returns true. If such an element is found, findIndex immediately returns that element index. Otherwise, findIndex returns -1 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Index of the first matched element |

## findLast

```TypeScript
public findLast(fn: (val: BigInt) => boolean): BigInt
```

Finds the last element in the BigInt64Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findLast(fn: (val: BigInt) => boolean): BigInt--><!--Device-BigInt64Array-public findLast(fn: (val: BigInt) => boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt) =&gt; boolean | 是 | A function to test each element. Should return true for the element to be found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | the last element that satisfies fn |

## findLast

```TypeScript
public findLast(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt
```

Finds the last element in the BigInt64Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findLast(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt--><!--Device-BigInt64Array-public findLast(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | A function to test each element. Called with (value, index, array). Should return true for the element to be found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | the last element that satisfies fn |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): int
```

Finds an index of the last element in the BigInt64Array that satisfies the condition

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findLastIndex(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): int--><!--Device-BigInt64Array-public findLastIndex(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | A function to test each element. Called with (value, index, array). Should return true for the element to be found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the index of the last element that satisfies fn, -1 otherwise |

## forEach

```TypeScript
public forEach(callbackfn: (value: BigInt, index: int, array: BigInt64Array) => void): void
```

Calls the given callback function once for each element in the BigInt64Array, in ascending order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public forEach(callbackfn: (value: BigInt, index: int, array: BigInt64Array) => void): void--><!--Device-BigInt64Array-public forEach(callbackfn: (value: BigInt, index: int, array: BigInt64Array) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: BigInt, index: int, array: BigInt64Array) =&gt; void | 是 | A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array. |

## from

```TypeScript
public static from(arr: FixedArray<BigInt>): BigInt64Array
```

Creates an array from an object of FixedArray&lt;BigInt&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arr: FixedArray<BigInt>): BigInt64Array--><!--Device-BigInt64Array-public static from(arr: FixedArray<BigInt>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;BigInt&gt; | 是 | An instance of the FixedArray type to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## from

```TypeScript
public static from(set: Set<BigInt>): BigInt64Array
```

Creates an array from a set of type std.core.Set&lt;BigInt&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(set: Set<BigInt>): BigInt64Array--><!--Device-BigInt64Array-public static from(set: Set<BigInt>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;BigInt&gt; | 是 | A set object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## from

```TypeScript
public static from(arr: BigInt64Array): BigInt64Array
```

Creates an array from an array of the same type.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arr: BigInt64Array): BigInt64Array--><!--Device-BigInt64Array-public static from(arr: BigInt64Array): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | 是 | An array to convert to a new array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## from

```TypeScript
public static from(arr: Array<BigInt>): BigInt64Array
```

Creates an array from an object of std.core.Array&lt;BigInt&gt;.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arr: Array<BigInt>): BigInt64Array--><!--Device-BigInt64Array-public static from(arr: Array<BigInt>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array&lt;BigInt&gt; | 是 | An instance of the std.core.Array type to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## from

```TypeScript
public static from(arrayLike: ArrayLike<double>): BigInt64Array
```

Creates an array from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arrayLike: ArrayLike<double>): BigInt64Array--><!--Device-BigInt64Array-public static from(arrayLike: ArrayLike<double>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | An array-like or iterable object to convert to an array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigInt64Array
```

Creates an array from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigInt64Array--><!--Device-BigInt64Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 | An array-like or iterable object to convert to an array. |
| mapfn | (v: T, k: double) =&gt; BigInt | 是 | A mapping function to call on every element of the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## from

```TypeScript
public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigInt64Array
```

Creates an array from an array-like or iterable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigInt64Array--><!--Device-BigInt64Array-public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;BigInt&gt; | 是 | An array-like or iterable object to convert to an array. |
| mapfn | (v: BigInt, k: double) =&gt; BigInt | 否 | A mapping function to call on every element of the array. Defaults to the identity function (returns the element unchanged). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | A new BigInt64Array |

## includes

```TypeScript
public includes(searchElement: long, fromIndex: int): boolean
```

Determines whether BigInt64Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public includes(searchElement: long, fromIndex: int): boolean--><!--Device-BigInt64Array-public includes(searchElement: long, fromIndex: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | long | 是 | The element to search for |
| fromIndex | int | 是 | The position in this array at which to begin searching for searchElement &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in BigInt64Array, false otherwise |

## includes

```TypeScript
public includes(searchElement: long): boolean
```

Determines whether BigInt64Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public includes(searchElement: long): boolean--><!--Device-BigInt64Array-public includes(searchElement: long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | long | 是 | The element to search for. The search starts at index 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in BigInt64Array, false otherwise |

## includes

```TypeScript
public includes(searchElement: BigInt, fromIndex?: int): boolean
```

Determines whether BigInt64Array includes a certain element, returning true or false as appropriate

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public includes(searchElement: BigInt, fromIndex?: int): boolean--><!--Device-BigInt64Array-public includes(searchElement: BigInt, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | The element to search for |
| fromIndex | int | 否 | The position in this array at which to begin searching for searchElement. Defaults to 0. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if searchElement is in BigInt64Array, false otherwise |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

Returns the index of the first occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public indexOf(searchElement: int): int--><!--Device-BigInt64Array-public indexOf(searchElement: int): int-End-->

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

Returns the index of the first occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-BigInt64Array-public indexOf(searchElement: int, fromIndex: int): int-End-->

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
public indexOf(searchElement: BigInt, fromIndex?: int): int
```

Returns the index of the first occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public indexOf(searchElement: BigInt, fromIndex?: int): int--><!--Device-BigInt64Array-public indexOf(searchElement: BigInt, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to locate in the array. |
| fromIndex | int | 否 | The array index at which to begin the search. Defaults to 0. &lt;br&gt;The value should be an integer. |

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

<!--Device-BigInt64Array-public join(separator?: string): string--><!--Device-BigInt64Array-public join(separator?: string): string-End-->

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

Returns a list of indices in the BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public keys(): IterableIterator<int>--><!--Device-BigInt64Array-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | iterator over indices. |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

Returns the index of the last occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: int): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: int): int-End-->

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
public lastIndexOf(searchElement: BigInt): int
```

Returns the index of the last occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to locate in the array. The search begins at index length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | rightmost index of searchElement. It must be less than length. -1 if not found |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

Returns the index of the last occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

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
public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int
```

Returns the index of the last occurrence of a value in BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | The value to locate in the array. |
| fromIndex | int \| undefined | 是 | The array index at which to begin the search. Defaults to the array length - 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | rightmost index of searchElement. It must be less or equal than fromIndex. -1 if not found |

## map

```TypeScript
public map(fn: (val: BigInt, index: int, array: BigInt64Array) => BigInt): BigInt64Array
```

Creates a new BigInt64Array using fn(arr[i]) over all elements of current BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public map(fn: (val: BigInt, index: int, array: BigInt64Array) => BigInt): BigInt64Array--><!--Device-BigInt64Array-public map(fn: (val: BigInt, index: int, array: BigInt64Array) => BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; BigInt | 是 | a function to apply for each element of current BigInt64Array |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array where for each element from current BigInt64Array fn was applied |

## of

```TypeScript
public static of(...items: FixedArray<int>): BigInt64Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<int>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<int>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array |

## of

```TypeScript
public static of(...items: FixedArray<long>): BigInt64Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<long>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<long>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;long&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array |

## of

```TypeScript
public static of(...items: FixedArray<bigint>): BigInt64Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<bigint>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<bigint>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;bigint&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array |

## of

```TypeScript
public static of(...items: FixedArray<double>): BigInt64Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<double>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<double>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | 是 | a set of elements to include in the new array object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array |

## of

```TypeScript
public static of(): BigInt64Array
```

Returns a new array from a set of elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(): BigInt64Array--><!--Device-BigInt64Array-public static of(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array |

## reduce

```TypeScript
public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,
        array: BigInt64Array) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => U, initialValue: U): U--><!--Device-BigInt64Array-public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: BigInt, currentIndex: int,         array: BigInt64Array) =&gt; U | 是 | A function that accepts four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The parameter which value is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | the accumulated result from the last call to the callback function. |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,
        array: BigInt64Array) => BigInt): BigInt
```

Calls the specified callback function for all the elements in an array.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt--><!--Device-BigInt64Array-public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: BigInt, currentValue: BigInt, currentIndex: int,         array: BigInt64Array) =&gt; BigInt | 是 | A function that accepts four arguments. The reduce method calls the callbackfn function one time for each element in the array. The first call to the callbackfn function provides array first element value as an argument |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight<U = BigInt>(
        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) => U,
        initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduceRight<U = BigInt>(        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) => U,        initialValue: U): U--><!--Device-BigInt64Array-public reduceRight<U = BigInt>(        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) =&gt; U | 是 | A function that accepts four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The parameter which value is used as the initial value to start the accumulation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | the accumulated result from the last call to the callback function. |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,
        array: BigInt64Array) => BigInt): BigInt
```

Calls the specified callback function for all the elements in an array, in descending order.The return value of the callback function is the accumulated result,and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt--><!--Device-BigInt64Array-public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: BigInt, currentValue: BigInt, currentIndex: int,         array: BigInt64Array) =&gt; BigInt | 是 | A function that accepts four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. The first call to the callbackfn function provides array last element value as an argument. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | the accumulated result from the last call to the callback function. |

## reverse

```TypeScript
public reverse(): BigInt64Array
```

Creates a new BigInt64Array using reversed data from the current one

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reverse(): BigInt64Array--><!--Device-BigInt64Array-public reverse(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array using reversed data from the current one |

## set

```TypeScript
public set(insertPos: int, val: long): void
```

Assigns val as element on insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(insertPos: int, val: long): void--><!--Device-BigInt64Array-public set(insertPos: int, val: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | long | 是 | value to set |

## set

```TypeScript
public set(insertPos: int, val: BigInt): void
```

Assigns val as element on insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(insertPos: int, val: BigInt): void--><!--Device-BigInt64Array-public set(insertPos: int, val: BigInt): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | index to change &lt;br&gt;The value should be an integer. |
| val | [BigInt](arkts-arkts-bigint-c.md) | 是 | value to set |

## set

```TypeScript
public set(arr: FixedArray<long>): void
```

Copies all elements of arr to the current BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<long>): void--><!--Device-BigInt64Array-public set(arr: FixedArray<long>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | array to copy data from |

## set

```TypeScript
public set(arr: FixedArray<long>, insertPos: int): void
```

Copies all elements of arr to the current BigInt64Array starting from insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<long>, insertPos: int): void--><!--Device-BigInt64Array-public set(arr: FixedArray<long>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | array to copy data from |
| insertPos | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(arr: FixedArray<BigInt>): void
```

Copies all elements of arr to the current BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>): void--><!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;BigInt&gt; | 是 | array to copy data from |

## set

```TypeScript
public set(arr: FixedArray<BigInt>, insertPos: int): void
```

Copies all elements of arr to the current BigInt64Array starting from insertPos.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>, insertPos: int): void--><!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;BigInt&gt; | 是 | array to copy data from |
| insertPos | int | 是 | start index where data from arr will be inserted &lt;br&gt;The value should be an integer. |

## set

```TypeScript
public set(array: BigInt64Array): void
```

Copies all elements of array to the current BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(array: BigInt64Array): void--><!--Device-BigInt64Array-public set(array: BigInt64Array): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | 是 | array to copy data from |

## set

```TypeScript
public set(array: BigInt64Array, offset: int): void
```

Copies all elements of arr to the current BigInt64Array starting from offset.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(array: BigInt64Array, offset: int): void--><!--Device-BigInt64Array-public set(array: BigInt64Array, offset: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | 是 | array to copy data from. |
| offset | int | 是 | start index where data from arr will be inserted. &lt;br&gt;The value range is all integers. |

## set

```TypeScript
public set(array: ArrayLike<BigInt>, offset: int = 0): void
```

Copies elements from an ArrayLike object to the BigInt64Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(array: ArrayLike<BigInt>, offset: int = 0): void--><!--Device-BigInt64Array-public set(array: ArrayLike<BigInt>, offset: int = 0): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;BigInt&gt; | 是 | An ArrayLike object containing the elements to copy. |
| offset | int | 是 | Optional. The offset into the target array at which to begin writing values from the source array. The default value is 0. &lt;br&gt;The value should be an integer. |

## slice

```TypeScript
public slice(begin: int): BigInt64Array
```

Creates a slice of current BigInt64Array using range [begin, this.length).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public slice(begin: int): BigInt64Array--><!--Device-BigInt64Array-public slice(begin: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | start index to be taken into slice |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with elements of current BigInt64Array[begin, this.length) |

## slice

```TypeScript
public slice(begin?: int, end?: int): BigInt64Array
```

Creates a slice of current BigInt64Array using range [begin, end)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public slice(begin?: int, end?: int): BigInt64Array--><!--Device-BigInt64Array-public slice(begin?: int, end?: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start index to be taken into slice. Defaults to 0. |
| end | int | 否 | last index to be taken into slice. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with elements of current BigInt64Array[begin;end), where end index is excluded |

## some

```TypeScript
public some(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean
```

Determines whether the specified callback function returns true for any element of an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public some(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean--><!--Device-BigInt64Array-public some(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | A function that accepts three arguments. The some method calls the predicate function for each element in the array until the predicate returns a true or until the end of the array. |

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

<!--Device-BigInt64Array-public sort(): this--><!--Device-BigInt64Array-public sort(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | sorted BigInt64Array |

## sort

```TypeScript
public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this
```

Sorts in-place

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this--><!--Device-BigInt64Array-public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: BigInt, b: BigInt) =&gt; int \| BigInt | 否 | comparator used to determine the order of the elements. compareFn returns a negative value if first argument is less than second argument, zero if they're equal and a positive value otherwise. Defaults to an ascending numeric sort. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | sorted BigInt64Array |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): BigInt64Array
```

Creates a new BigInt64Array that shares the same underlying ArrayBuffer as the current array,optionally with a restricted range.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public subarray(begin?: int, end?: int): BigInt64Array--><!--Device-BigInt64Array-public subarray(begin?: int, end?: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start index, inclusive. Defaults to 0. |
| end | int | 否 | last index, exclusive. Defaults to the array length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with the same underlying ArrayBuffer |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Converts this object to a locale-specific string representation

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-BigInt64Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
public toReversed(): BigInt64Array
```

Returns a new BigInt64Array with the elements in reverse order. The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toReversed(): BigInt64Array--><!--Device-BigInt64Array-public toReversed(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with the elements in reverse order. |

## toSorted

```TypeScript
public toSorted(): BigInt64Array
```

Returns a new BigInt64Array with the elements sorted in ascending order. The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toSorted(): BigInt64Array--><!--Device-BigInt64Array-public toSorted(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with the elements sorted in ascending order. |

## toString

```TypeScript
public toString(): string
```

Returns a comma-separated string representation of the BigInt64Array elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toString(): string--><!--Device-BigInt64Array-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a comma-separated string of the array elements. |

## valueOf

```TypeScript
public valueOf(): BigInt64Array
```

Returns the object itself

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public valueOf(): BigInt64Array--><!--Device-BigInt64Array-public valueOf(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## values

```TypeScript
public values(): IterableIterator<BigInt>
```

Returns an iterator over the values of the BigInt64Array, in ascending order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public values(): IterableIterator<BigInt>--><!--Device-BigInt64Array-public values(): IterableIterator<BigInt>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;BigInt&gt; | an iterator over all elements. |

## with

```TypeScript
public with(index: int, value: long): BigInt64Array
```

Returns a new BigInt64Array with the element at the given index replaced by the given value.The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public with(index: int, value: long): BigInt64Array--><!--Device-BigInt64Array-public with(index: int, value: long): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value range is all integers. |
| value | long | 是 | value to set |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with the element at index replaced by value. |

## with

```TypeScript
public with(index: int, value: BigInt): BigInt64Array
```

Returns a new BigInt64Array with the element at the given index replaced by the given value.The original array is not modified.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public with(index: int, value: BigInt): BigInt64Array--><!--Device-BigInt64Array-public with(index: int, value: BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | index to change &lt;br&gt;The value range is all integers. |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 | value to set |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](../../apis-default/arkts-apis/arkts-lib-es2020-bigint-bigint64array-i.md) | a new BigInt64Array with the element at index replaced by value. |

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 8
```

double of bytes occupied by each element

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static readonly BYTES_PER_ELEMENT: int = 8--><!--Device-BigInt64Array-public static readonly BYTES_PER_ELEMENT: int = 8-End-->

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

<!--Device-BigInt64Array-public readonly buffer: ArrayBuffer--><!--Device-BigInt64Array-public readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public readonly byteLength: int
```

Number of bytes used The value range is all integers.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly byteLength: int--><!--Device-BigInt64Array-public readonly byteLength: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public readonly byteOffset: int
```

Byte offset within the underlying ArrayBuffer The value range is all integers.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly byteOffset: int--><!--Device-BigInt64Array-public readonly byteOffset: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
public get length(): int
```

double of long stored in BigInt64Array

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public get length(): int--><!--Device-BigInt64Array-public get length(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'BigInt64Array'
```

String \"BigInt64Array\", representing the type name of this typed array.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly name: string = 'BigInt64Array'--><!--Device-BigInt64Array-public readonly name: string = 'BigInt64Array'-End-->

**系统能力：** SystemCapability.Utils.Lang

