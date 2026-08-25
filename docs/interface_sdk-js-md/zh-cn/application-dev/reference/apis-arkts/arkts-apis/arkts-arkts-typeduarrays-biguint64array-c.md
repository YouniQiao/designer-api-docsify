# BigUint64Array

BigUint64Array类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
public $_get(i: int): BigInt
```

返回指定索引处的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| i | int | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<BigInt>
```

Iterable接口实现。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; |

## $_set

```TypeScript
public $_set(index: int, val: int): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| val | int | 是 |

## $_set

```TypeScript
public $_set(index: int, val: long): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| val | long | 是 |

## $_set

```TypeScript
public $_set(index: int, val: BigInt): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| val | [BigInt](arkts-arkts-bigint-c.md) | 是 |

## at

```TypeScript
public at(index: int): BigInt | undefined
```

当索引合法时，返回指定索引处的基本类型实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) \| undefined |

## constructor

```TypeScript
public constructor()
```

创建空的BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

根据length创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [length](#length) | int | 是 |

## constructor

```TypeScript
public constructor(length: double)
```

根据length创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [length](#length) | double | 是 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<int>)
```

根据FixedArray&lt;int&gt;创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numbers | FixedArray & lt;int & gt; | 是 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<double>)
```

根据FixedArray&lt;double&gt;创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numbers | FixedArray & lt;double & gt; | 是 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<bigint>)
```

根据FixedArray&lt;bigint&gt;创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numbers | FixedArray & lt;bigint & gt; | 是 |

## constructor

```TypeScript
public constructor(other: BigUint64Array)
```

根据另一个BigUint64Array初始化并创建新的BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) | 是 |

## constructor

```TypeScript
public constructor(elements: Iterable<BigInt>)
```

根据通过Iterable&lt;Number&gt;接口访问的数据创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Iterable&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |

## constructor

```TypeScript
public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)
```

根据data、byteOffset和length创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | [ArrayBufferLike](arkts-arkts-arraybufferlike-t.md) | 是 |
| [byteOffset](#byteoffset) | int | 是 |
| [length](#length) | int | 是 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

根据buf和byteOffset创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| [byteOffset](#byteoffset) | int | 是 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

根据data、byteOffset和length创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| [byteOffset](#byteoffset) | double \| undefined | 是 |
| [length](#length) | double \| undefined | 是 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

根据buf和byteOffset创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| [byteOffset](#byteoffset) | double | 是 |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

根据buf创建BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayLike & lt;double & gt; \ | ArrayBuffer | 是 |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): BigUint64Array
```

将startPos到endPos之间的内部元素复制到targetPos。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | int | 是 |
| start | int | 是 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## copyWithin

```TypeScript
public copyWithin(target: int): BigUint64Array
```

将BigUint64Array从头到尾的内部元素复制到targetPos。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | int | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## entries

```TypeScript
public entries(): IterableIterator<[int, BigInt]>
```

返回由BigUint64Array中每个条目的键值对组成的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, BigInt]&gt; |

## every

```TypeScript
public every(predicate: (element: BigInt, index: int, array: BigUint64Array) => boolean): boolean
```

判断指定的回调函数是否对数组中的所有元素都返回true。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (element: BigInt, index: int, array: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## fill

```TypeScript
public fill(value: long, start?: int, end?: int): BigUint64Array
```

使用指定值填充BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | long | 是 |
| start | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## fill

```TypeScript
public fill(value: BigInt, start?: int, end?: int): BigUint64Array
```

使用指定值填充BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 |
| start | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## filter

```TypeScript
public filter(fn: (val: BigInt, index: int, array: BigUint64Array) => boolean): BigUint64Array
```

根据条件fn从当前BigUint64Array创建新的BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## find

```TypeScript
public find(predicate: (value: BigInt, index: int, array: BigUint64Array) => boolean): BigInt | undefined
```

返回数组中第一个使predicate返回true的元素的值， 否则。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: BigInt, index: int, array: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) \| undefined |

## findIndex

```TypeScript
public findIndex(predicate: (value: BigInt, index: int, obj: BigUint64Array) => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: BigInt, index: int, obj: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## findLast

```TypeScript
public findLast(fn: (val: BigInt, index: int, array: BigUint64Array) => boolean): BigInt
```

返回BigUint64Array中最后一个满足给定predicate的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: BigInt, index: int, array: BigUint64Array) => boolean): int
```

返回BigUint64Array中最后一个满足给定predicate的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## forEach

```TypeScript
public forEach(callbackfn: (value: BigInt, index: int, array: BigUint64Array) => void): void
```

对BigUint64Array中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (value: BigInt, index: int, array: BigUint64Array) = & gt; void | 是 |

## from

```TypeScript
public static from(arr: FixedArray<BigInt>): BigUint64Array
```

根据FixedArray&lt;BigInt&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## from

```TypeScript
public static from(set: Set<BigInt>): BigUint64Array
```

根据std.core.Set&lt;BigInt&gt;类型的集合创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [set](#set) | Set&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## from

```TypeScript
public static from(arr: BigUint64Array): BigUint64Array
```

根据同类型的数组创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## from

```TypeScript
public static from(arr: Array<BigInt>): BigUint64Array
```

根据std.core.Array&lt;BigInt&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | Array&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## from

```TypeScript
public static from(arr: ArrayLike<BigInt>): BigUint64Array
```

根据类数组对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | ArrayLike&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigUint64Array
```

根据类数组对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike & lt;T & gt; | 是 |
| mapfn | (v: T, k: double) = & gt; BigInt | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## from

```TypeScript
public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigUint64Array
```

根据可迭代对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | Iterable&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |
| mapfn | (v: BigInt, k: double) = & gt; BigInt | 否 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## includes

```TypeScript
public includes(searchElement: long, fromIndex: int): boolean
```

判断BigUint64Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | long | 是 |
| fromIndex | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## includes

```TypeScript
public includes(searchElement: long): boolean
```

判断BigUint64Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | long | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## includes

```TypeScript
public includes(searchElement: BigInt, fromIndex?: int): boolean
```

判断BigUint64Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 |
| fromIndex | int | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

返回指定值在BigUint64Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## indexOf

```TypeScript
public indexOf(searchElement: int, fromIndex: int): int
```

返回指定值在BigUint64Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | int | 是 |
| fromIndex | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## indexOf

```TypeScript
public indexOf(searchElement: BigInt, fromIndex?: int): int
```

返回指定值在BigUint64Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 |
| fromIndex | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## join

```TypeScript
public join(separator?: string): string
```

使用指定的分隔字符串连接数组中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| separator | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

返回BigUint64Array中索引的列表。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

返回指定值在BigUint64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: BigInt): int
```

返回指定值在BigUint64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

返回指定值在BigUint64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | int | 是 |
| fromIndex | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int
```

返回指定值在BigUint64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 |
| fromIndex | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## map

```TypeScript
public map(fn: (val: BigInt, index: int, array: BigUint64Array) => BigInt): BigUint64Array
```

对当前BigUint64Array的所有元素执行fn(arr[i])，创建新的BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigUint64Array) = & gt; BigInt | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## of

```TypeScript
public static of(...items: FixedArray<int>): BigUint64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | FixedArray & lt;int & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## of

```TypeScript
public static of(...items: FixedArray<long>): BigUint64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | FixedArray & lt;long & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## of

```TypeScript
public static of(...items: FixedArray<bigint>): BigUint64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | FixedArray & lt;bigint & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## of

```TypeScript
public static of(...items: FixedArray<double>): BigUint64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | FixedArray & lt;double & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## of

```TypeScript
public static of(): BigUint64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## reduce

```TypeScript
public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,
        array: BigUint64Array) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: BigInt, currentIndex: int,         array: BigUint64Array) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,
        array: BigUint64Array) => BigInt): BigInt
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: BigInt, currentValue: BigInt, currentIndex: int,         array: BigUint64Array) = & gt; BigInt | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## reduceRight

```TypeScript
public reduceRight<U = BigInt>(
        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigUint64Array) => U,
        initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigUint64Array) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,
        array: BigUint64Array) => BigInt): BigInt
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: BigInt, currentValue: BigInt, currentIndex: int,         array: BigUint64Array) = & gt; BigInt | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## reverse

```TypeScript
public reverse(): BigUint64Array
```

基于当前BigUint64Array的反转数据创建新的BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## set

```TypeScript
public set(insertPos: int, val: long): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| insertPos | int | 是 |
| val | long | 是 |

## set

```TypeScript
public set(insertPos: int, val: BigInt): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| insertPos | int | 是 |
| val | [BigInt](arkts-arkts-bigint-c.md) | 是 |

## set

```TypeScript
public set(arr: FixedArray<long>, insertPos: int): void
```

从insertPos开始，将arr中的所有元素复制到当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray & lt;long & gt; | 是 |
| insertPos | int | 是 |

## set

```TypeScript
public set(arr: FixedArray<BigInt>, insertPos: int): void
```

从insertPos开始，将arr中的所有元素复制到当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |
| insertPos | int | 是 |

## set

```TypeScript
public set(arr: FixedArray<long>): void
```

将arr中的所有元素复制到当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray & lt;long & gt; | 是 |

## set

```TypeScript
public set(arr: FixedArray<BigInt>): void
```

将arr中的所有元素复制到当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |

## set

```TypeScript
public set(array: BigUint64Array): void
```

将arr中的所有元素复制到当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) | 是 |

## set

```TypeScript
public set(array: BigUint64Array, offset: int): void
```

将arr中的所有元素复制到当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) | 是 |
| offset | int | 是 |

## set

```TypeScript
public set(array: ArrayLike<BigInt>, offset: int = 0): void
```

将ArrayLike对象中的元素复制到BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | ArrayLike&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 |
| offset | int | 是 |

## slice

```TypeScript
public slice(begin?: int, end?: int): BigUint64Array
```

使用[begin, end]区间截取当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## slice

```TypeScript
public slice(begin: int): BigUint64Array
```

使用[begin, this.lengthInt]区间截取当前BigUint64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | int | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## some

```TypeScript
public some(predicate: (element: BigInt, index: int, array: BigUint64Array) => boolean): boolean
```

判断数组中是否存在使指定回调函数返回true的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (element: BigInt, index: int, array: BigUint64Array) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## sort

```TypeScript
public sort(): this
```

按数值升序进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| this |

## sort

```TypeScript
public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this
```

原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compareFn | (a: BigInt, b: BigInt) = & gt; int \ | [BigInt](arkts-arkts-bigint-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): BigUint64Array
```

创建与当前数组共享同一底层ArrayBuffer的新BigUint64Array， 可选择限定范围。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |
| options | object | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## toReversed

```TypeScript
public toReversed(): BigUint64Array
```

返回元素顺序反转后的新BigUint64Array。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## toSorted

```TypeScript
public toSorted(): BigUint64Array
```

返回元素按升序排序后的新BigUint64Array。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## toString

```TypeScript
public toString(): string
```

返回以逗号分隔的BigUint64Array元素字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## valueOf

```TypeScript
public valueOf(): BigUint64Array
```

按升序对BigUint64Array中的每个元素调用一次给定的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## values

```TypeScript
public values(): IterableIterator<BigInt>
```

返回数组值的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; |

## with

```TypeScript
public with(index: int, value: long): BigUint64Array
```

返回将指定索引处的元素替换为给定值后的新BigUint64Array， 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## with

```TypeScript
public with(index: int, value: BigInt): BigUint64Array
```

返回将指定索引处的元素替换为给定值后的新BigUint64Array， 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigUint64Array](arkts-arkts-typeduarrays-biguint64array-c.md) |

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

底层Buffer。

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public get byteLength(): int
```

占用的字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public get byteOffset(): int
```

底层Buffer中的字节偏移量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 8
```

每个元素占用的字节数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
public get length(): int
```

BigUint64Array中存储的元素数量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'BigUint64Array'
```

字符串\"BigUint64Array\"。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
