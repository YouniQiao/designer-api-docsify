# BigInt64Array

BigInt64Array类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class BigInt64Array--><!--Device-unnamed-export class BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
public $_get(index: int): BigInt
```

返回指定索引处的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_get(index: int): BigInt--><!--Device-BigInt64Array-public $_get(index: int): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待查看的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | index处的原始数值。 |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<BigInt>
```

Iterable接口实现。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_iterator(): IterableIterator<BigInt>--><!--Device-BigInt64Array-public $_iterator(): IterableIterator<BigInt>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 遍历所有元素的迭代器。 |

## $_set

```TypeScript
public $_set(index: int, val: long): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_set(index: int, val: long): void--><!--Device-BigInt64Array-public $_set(index: int, val: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：可以为任意整数。 |
| val | long | 是 | 待设置的值。 |

## $_set

```TypeScript
public $_set(index: int, val: BigInt): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public $_set(index: int, val: BigInt): void--><!--Device-BigInt64Array-public $_set(index: int, val: BigInt): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 |
| val | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待设置的值。 |

## at

```TypeScript
public at(index: int): BigInt | undefined
```

返回指定索引处的基本类型实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public at(index: int): BigInt | undefined--><!--Device-BigInt64Array-public at(index: int): BigInt | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待查看的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) \| undefined | index处的原始数值；如果索引越界，则返回undefined。 |

## constructor

```TypeScript
public constructor()
```

创建空的BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor()--><!--Device-BigInt64Array-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

根据length创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(length: int)--><!--Device-BigInt64Array-public constructor(length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | 元素数量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(length: double)
```

根据length创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(length: double)--><!--Device-BigInt64Array-public constructor(length: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | 元素数量。 |

## constructor

```TypeScript
public constructor(other: BigInt64Array)
```

创建BigInt64Array的副本。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(other: BigInt64Array)--><!--Device-BigInt64Array-public constructor(other: BigInt64Array)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(doubles: FixedArray<int>)
```

根据FixedArray&lt;int&gt;创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(doubles: FixedArray<int>)--><!--Device-BigInt64Array-public constructor(doubles: FixedArray<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubles | FixedArray&lt;int&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(doubles: FixedArray<double>)
```

根据FixedArray&lt;double&gt;创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(doubles: FixedArray<double>)--><!--Device-BigInt64Array-public constructor(doubles: FixedArray<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubles | FixedArray&lt;double&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(doubles: FixedArray<bigint>)
```

根据FixedArray&lt;bigint&gt;创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(doubles: FixedArray<bigint>)--><!--Device-BigInt64Array-public constructor(doubles: FixedArray<bigint>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubles | FixedArray&lt;bigint&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(elements: Iterable<BigInt>)
```

根据通过Iterable&lt;double&gt;接口访问的数据创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(elements: Iterable<BigInt>)--><!--Device-BigInt64Array-public constructor(elements: Iterable<BigInt>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 可迭代对象。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

根据buf和byteOffset创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | int | 是 | 相对于buf起始位置的字节偏移量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

根据data、byteOffset和length创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | double | 是 | 相对于buf起始位置的字节偏移量。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int, length: int)
```

根据data、byteOffset和length创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: int, length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | int | 是 | 相对于buf起始位置的字节偏移量。 <br>取值约束：应为整数。 |
| length | int | 是 | 新建BigInt64Array中long类型元素的数量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

根据data、byteOffset和length创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-BigInt64Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | double \| undefined | 是 | 相对于buf起始位置的字节偏移量。 |
| length | double \| undefined | 是 | 新建BigInt64Array中long类型元素的数量。 |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

根据buf创建BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-BigInt64Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; \| ArrayBuffer | 是 | 初始化数据。 |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): BigInt64Array
```

将startPos到endPos之间的内部元素复制到targetPos。 参数归一化规则参见

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public copyWithin(target: int, start: int, end?: int): BigInt64Array--><!--Device-BigInt64Array-public copyWithin(target: int, start: int, end?: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | 放置所复制元素的插入索引。 |
| start | int | 是 | 开始复制的索引。 |
| end | int | 否 | 结束复制的索引（不包含），默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 修改后的BigInt64Array实例。 |

## copyWithin

```TypeScript
public copyWithin(target: int): BigInt64Array
```

将BigInt64Array从头到尾的内部元素复制到targetPos。 参数归一化规则参见

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public copyWithin(target: int): BigInt64Array--><!--Device-BigInt64Array-public copyWithin(target: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | 放置所复制元素的插入索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 修改后的BigInt64Array实例。 |

## entries

```TypeScript
public entries(): IterableIterator<[int, BigInt]>
```

返回由BigInt64Array中每个条目的键值对组成的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public entries(): IterableIterator<[int, BigInt]>--><!--Device-BigInt64Array-public entries(): IterableIterator<[int, BigInt]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, BigInt]&gt; | 数组中每个条目的键值对。 |

## every

```TypeScript
public every(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean
```

判断指定的回调函数是否对数组中的所有元素都返回true。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public every(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean--><!--Device-BigInt64Array-public every(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | 最多接受三个参数的函数。 every方法会对数组中的每个元素调用predicate函数，直到predicate 返回false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 除非predicate对某个数组元素返回false，否则返回true； 此时立即返回false。 |

## fill

```TypeScript
public fill(value: long, start?: int, end?: int): this
```

使用指定值填充BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public fill(value: long, start?: int, end?: int): this--><!--Device-BigInt64Array-public fill(value: long, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 新的值。 |
| start | int | 否 | 开始填充的索引，默认值为0。 |
| end | int | 否 | 结束填充的索引（不包含），默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 修改后的BigInt64Array。 |

## fill

```TypeScript
public fill(value: BigInt, start?: int, end?: int): this
```

使用指定值填充BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public fill(value: BigInt, start?: int, end?: int): this--><!--Device-BigInt64Array-public fill(value: BigInt, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 | 新的值。 |
| start | int | 否 | 开始填充的索引，默认值为0。 |
| end | int | 否 | 结束填充的索引（不包含），默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 修改后的BigInt64Array。 |

## filter

```TypeScript
public filter(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt64Array
```

根据条件fn从当前BigInt64Array创建新的BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public filter(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt64Array--><!--Device-BigInt64Array-public filter(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | 对每个元素应用的判断条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## find

```TypeScript
public find(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): BigInt | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public find(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): BigInt | undefined--><!--Device-BigInt64Array-public find(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): BigInt | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: BigInt, index: int, obj: BigInt64Array) =&gt; boolean | 是 | find会按升序对数组中的每个元素调用一次predicate， 直到找到使predicate返回true的元素。如果找到这样的元素，find 会立即返回该元素的值；否则find返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) \| undefined |  |

## findIndex

```TypeScript
public findIndex(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findIndex(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): int--><!--Device-BigInt64Array-public findIndex(predicate: (value: BigInt, index: int, obj: BigInt64Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: BigInt, index: int, obj: BigInt64Array) =&gt; boolean | 是 | find会按升序对数组中的每个元素调用一次predicate， 直到找到使predicate返回true的元素。如果找到这样的元素， findIndex会立即返回该元素的索引；否则findIndex返回-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个匹配元素的索引。 |

## findLast

```TypeScript
public findLast(fn: (val: BigInt) => boolean): BigInt
```

查找BigInt64Array中最后一个满足该条件的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findLast(fn: (val: BigInt) => boolean): BigInt--><!--Device-BigInt64Array-public findLast(fn: (val: BigInt) => boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt) =&gt; boolean | 是 | 用于测试每个元素的函数，命中目标元素时应返回true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 最后一个满足fn的元素。 |

## findLast

```TypeScript
public findLast(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt
```

查找BigInt64Array中最后一个满足该条件的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findLast(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt--><!--Device-BigInt64Array-public findLast(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | 用于测试每个元素的函数，调用时传入(value, index, array)。 命中目标元素时应返回true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 最后一个满足fn的元素。 |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): int
```

查找BigInt64Array中最后一个满足该条件的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public findLastIndex(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): int--><!--Device-BigInt64Array-public findLastIndex(fn: (val: BigInt, index: int, array: BigInt64Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | 用于测试每个元素的函数，调用时传入(value, index, array)。 命中目标元素时应返回true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 最后一个满足fn的元素的索引，若不存在则返回-1。 |

## forEach

```TypeScript
public forEach(callbackfn: (value: BigInt, index: int, array: BigInt64Array) => void): void
```

按升序对BigInt64Array中的每个元素调用一次给定的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public forEach(callbackfn: (value: BigInt, index: int, array: BigInt64Array) => void): void--><!--Device-BigInt64Array-public forEach(callbackfn: (value: BigInt, index: int, array: BigInt64Array) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: BigInt, index: int, array: BigInt64Array) =&gt; void | 是 | 最多接受三个参数的函数。forEach会对数组中的每个元素 调用一次callbackfn函数。 |

## from

```TypeScript
public static from(arr: FixedArray<BigInt>): BigInt64Array
```

根据FixedArray&lt;BigInt&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arr: FixedArray<BigInt>): BigInt64Array--><!--Device-BigInt64Array-public static from(arr: FixedArray<BigInt>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 待转换为数组的FixedArray类型实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## from

```TypeScript
public static from(set: Set<BigInt>): BigInt64Array
```

根据std.core.Set&lt;BigInt&gt;类型的集合创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(set: Set<BigInt>): BigInt64Array--><!--Device-BigInt64Array-public static from(set: Set<BigInt>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 待转换为数组的Set对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## from

```TypeScript
public static from(arr: BigInt64Array): BigInt64Array
```

根据同类型的数组创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arr: BigInt64Array): BigInt64Array--><!--Device-BigInt64Array-public static from(arr: BigInt64Array): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 是 | 待转换为新数组的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## from

```TypeScript
public static from(arr: Array<BigInt>): BigInt64Array
```

根据std.core.Array&lt;BigInt&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arr: Array<BigInt>): BigInt64Array--><!--Device-BigInt64Array-public static from(arr: Array<BigInt>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 待转换为数组的std.core.Array类型实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## from

```TypeScript
public static from(arrayLike: ArrayLike<double>): BigInt64Array
```

根据类数组对象或可迭代对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arrayLike: ArrayLike<double>): BigInt64Array--><!--Device-BigInt64Array-public static from(arrayLike: ArrayLike<double>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | 待转换为数组的类数组对象或可迭代对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigInt64Array
```

根据类数组对象或可迭代对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigInt64Array--><!--Device-BigInt64Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 | 待转换为数组的类数组对象或可迭代对象。 |
| mapfn | (v: T, k: double) =&gt; BigInt | 是 | 对数组中每个元素调用的映射函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## from

```TypeScript
public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigInt64Array
```

根据类数组对象或可迭代对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigInt64Array--><!--Device-BigInt64Array-public static from(arrayLike: Iterable<BigInt>, mapfn?: (v: BigInt, k: double) => BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 待转换为数组的类数组对象或可迭代对象。 |
| mapfn | (v: BigInt, k: double) =&gt; BigInt | 否 | 对数组中每个元素调用的映射函数。 默认使用恒等函数，即原样返回该元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## includes

```TypeScript
public includes(searchElement: long, fromIndex: int): boolean
```

判断BigInt64Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public includes(searchElement: long, fromIndex: int): boolean--><!--Device-BigInt64Array-public includes(searchElement: long, fromIndex: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | long | 是 | 待查找的元素。 |
| fromIndex | int | 是 | 在该数组中开始查找searchElement的位置。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于BigInt64Array中则返回true，否则返回false。 |

## includes

```TypeScript
public includes(searchElement: long): boolean
```

判断BigInt64Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public includes(searchElement: long): boolean--><!--Device-BigInt64Array-public includes(searchElement: long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | long | 是 | 待查找的元素，查找从索引0处开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于BigInt64Array中则返回true，否则返回false。 |

## includes

```TypeScript
public includes(searchElement: BigInt, fromIndex?: int): boolean
```

判断BigInt64Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public includes(searchElement: BigInt, fromIndex?: int): boolean--><!--Device-BigInt64Array-public includes(searchElement: BigInt, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待查找的元素。 |
| fromIndex | int | 否 | 在该数组中开始查找searchElement的位置。 默认值为0。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于BigInt64Array中则返回true，否则返回false。 |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

返回指定值在BigInt64Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public indexOf(searchElement: int): int--><!--Device-BigInt64Array-public indexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待在数组中查找的值，查找从索引0处开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 找到时返回该元素的索引，否则返回-1。 |

## indexOf

```TypeScript
public indexOf(searchElement: int, fromIndex: int): int
```

返回指定值在BigInt64Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-BigInt64Array-public indexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待在数组中查找的值。 |
| fromIndex | int | 是 | 开始查找的数组索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 找到时返回该元素的索引，否则返回-1。 |

## indexOf

```TypeScript
public indexOf(searchElement: BigInt, fromIndex?: int): int
```

返回指定值在BigInt64Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public indexOf(searchElement: BigInt, fromIndex?: int): int--><!--Device-BigInt64Array-public indexOf(searchElement: BigInt, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待在数组中查找的值。 |
| fromIndex | int | 否 | 开始查找的数组索引。 默认值为0。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 找到时返回该元素的索引，否则返回-1。 |

## join

```TypeScript
public join(separator?: string): string
```

使用指定的分隔字符串连接数组中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public join(separator?: string): string--><!--Device-BigInt64Array-public join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | 用于在结果字符串中分隔数组相邻元素的 字符串。如果不传入该参数，则元素之间以逗号分隔。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 使用指定分隔符连接所有数组元素而成的字符串。 |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

返回BigInt64Array中索引的列表。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public keys(): IterableIterator<int>--><!--Device-BigInt64Array-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | 遍历索引的迭代器。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

返回指定值在BigInt64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: int): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待在数组中查找的值，查找从索引length - 1处开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | searchElement最靠右的索引，必须小于length；未找到时返回-1。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: BigInt): int
```

返回指定值在BigInt64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待在数组中查找的值，查找从索引length - 1处开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | searchElement最靠右的索引，必须小于length；未找到时返回-1。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

返回指定值在BigInt64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待在数组中查找的值。 |
| fromIndex | int | 是 | 开始查找的数组索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | searchElement最靠右的索引，必须小于或等于fromIndex；未找到时返回-1。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int
```

返回指定值在BigInt64Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int--><!--Device-BigInt64Array-public lastIndexOf(searchElement: BigInt, fromIndex: int | undefined): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待在数组中查找的值。 |
| fromIndex | int \| undefined | 是 | 开始查找的数组索引。 默认值为数组长度减1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | searchElement最靠右的索引，必须小于或等于fromIndex；未找到时返回-1。 |

## map

```TypeScript
public map(fn: (val: BigInt, index: int, array: BigInt64Array) => BigInt): BigInt64Array
```

对当前BigInt64Array的所有元素执行fn(arr[i])，创建新的BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public map(fn: (val: BigInt, index: int, array: BigInt64Array) => BigInt): BigInt64Array--><!--Device-BigInt64Array-public map(fn: (val: BigInt, index: int, array: BigInt64Array) => BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: BigInt, index: int, array: BigInt64Array) =&gt; BigInt | 是 | 对当前BigInt64Array中每个元素应用的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 对当前BigInt64Array中每个元素应用fn后得到的新BigInt64Array。 |

## of

```TypeScript
public static of(...items: FixedArray<int>): BigInt64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<int>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<int>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## of

```TypeScript
public static of(...items: FixedArray<long>): BigInt64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<long>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<long>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;long&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## of

```TypeScript
public static of(...items: FixedArray<bigint>): BigInt64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<bigint>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<bigint>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;bigint&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## of

```TypeScript
public static of(...items: FixedArray<double>): BigInt64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(...items: FixedArray<double>): BigInt64Array--><!--Device-BigInt64Array-public static of(...items: FixedArray<double>): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## of

```TypeScript
public static of(): BigInt64Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static of(): BigInt64Array--><!--Device-BigInt64Array-public static of(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 新的BigInt64Array。 |

## reduce

```TypeScript
public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,
        array: BigInt64Array) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => U, initialValue: U): U--><!--Device-BigInt64Array-public reduce<U = BigInt>( callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: BigInt, currentIndex: int,         array: BigInt64Array) =&gt; U | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 其值作为累加初始值的参数。 首次调用callbackfn时，将该值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 上一次调用回调函数得到的累加结果。 |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,
        array: BigInt64Array) => BigInt): BigInt
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt--><!--Device-BigInt64Array-public reduce(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: BigInt, currentValue: BigInt, currentIndex: int,         array: BigInt64Array) =&gt; BigInt | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 首次调用callbackfn时，将数组的第一个元素值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 上一次调用回调函数得到的累加结果。 |

## reduceRight

```TypeScript
public reduceRight<U = BigInt>(
        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) => U,
        initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduceRight<U = BigInt>(        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) => U,        initialValue: U): U--><!--Device-BigInt64Array-public reduceRight<U = BigInt>(        callbackfn: (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: BigInt, currentIndex: int, array: BigInt64Array) =&gt; U | 是 | 最多接受四个参数的函数。 reduceRight方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 其值作为累加初始值的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 上一次调用回调函数得到的累加结果。 |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,
        array: BigInt64Array) => BigInt): BigInt
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt--><!--Device-BigInt64Array-public reduceRight(callbackfn: (previousValue: BigInt, currentValue: BigInt, currentIndex: int,        array: BigInt64Array) => BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: BigInt, currentValue: BigInt, currentIndex: int,         array: BigInt64Array) =&gt; BigInt | 是 | 最多接受四个参数的函数。 reduceRight方法会对数组中的每个元素调用一次callbackfn函数。 首次调用callbackfn时，将数组的最后一个元素值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 上一次调用回调函数得到的累加结果。 |

## reverse

```TypeScript
public reverse(): BigInt64Array
```

基于当前BigInt64Array的反转数据创建新的BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public reverse(): BigInt64Array--><!--Device-BigInt64Array-public reverse(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 基于当前BigInt64Array的反转数据构造的新BigInt64Array。 |

## set

```TypeScript
public set(insertPos: int, val: long): void
```

将val赋值为insertPos处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(insertPos: int, val: long): void--><!--Device-BigInt64Array-public set(insertPos: int, val: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| val | long | 是 | 待设置的值。 |

## set

```TypeScript
public set(insertPos: int, val: BigInt): void
```

将val赋值为insertPos处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(insertPos: int, val: BigInt): void--><!--Device-BigInt64Array-public set(insertPos: int, val: BigInt): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| val | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待设置的值。 |

## set

```TypeScript
public set(arr: FixedArray<long>): void
```

将arr中的所有元素复制到当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<long>): void--><!--Device-BigInt64Array-public set(arr: FixedArray<long>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(arr: FixedArray<long>, insertPos: int): void
```

从insertPos开始，将arr中的所有元素复制到当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<long>, insertPos: int): void--><!--Device-BigInt64Array-public set(arr: FixedArray<long>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | 复制数据的源数组。 |
| insertPos | int | 是 | 写入arr数据的起始索引。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(arr: FixedArray<BigInt>): void
```

将arr中的所有元素复制到当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>): void--><!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(arr: FixedArray<BigInt>, insertPos: int): void
```

从insertPos开始，将arr中的所有元素复制到当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>, insertPos: int): void--><!--Device-BigInt64Array-public set(arr: FixedArray<BigInt>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 复制数据的源数组。 |
| insertPos | int | 是 | 写入arr数据的起始索引。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(array: BigInt64Array): void
```

将array中的所有元素复制到当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(array: BigInt64Array): void--><!--Device-BigInt64Array-public set(array: BigInt64Array): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(array: BigInt64Array, offset: int): void
```

从offset开始，将arr中的所有元素复制到当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(array: BigInt64Array, offset: int): void--><!--Device-BigInt64Array-public set(array: BigInt64Array, offset: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 是 | 复制数据的源数组。 |
| offset | int | 是 | 写入arr数据的起始索引。 <br>取值约束：可以为任意整数。 |

## set

```TypeScript
public set(array: ArrayLike<BigInt>, offset: int = 0): void
```

将ArrayLike对象中的元素复制到BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public set(array: ArrayLike<BigInt>, offset: int = 0): void--><!--Device-BigInt64Array-public set(array: ArrayLike<BigInt>, offset: int = 0): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 是 | 包含待复制元素的ArrayLike对象。 |
| offset | int | 是 | 可选参数，指定在目标数组中开始写入源数组值的 偏移量，默认值为0。 <br>取值约束：应为整数。 |

## slice

```TypeScript
public slice(begin: int): BigInt64Array
```

使用[begin, this.length)区间截取当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public slice(begin: int): BigInt64Array--><!--Device-BigInt64Array-public slice(begin: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | 截取的起始索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 包含当前BigInt64Array[begin, this.length)区间元素的新BigInt64Array。 |

## slice

```TypeScript
public slice(begin?: int, end?: int): BigInt64Array
```

使用[begin, end)区间截取当前BigInt64Array。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public slice(begin?: int, end?: int): BigInt64Array--><!--Device-BigInt64Array-public slice(begin?: int, end?: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | 截取的起始索引，默认值为0。 |
| end | int | 否 | 截取的结束索引，默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 包含当前BigInt64Array[begin;end)区间元素的新BigInt64Array， 其中不包含结束索引处的元素。 |

## some

```TypeScript
public some(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean
```

判断数组中是否存在使指定回调函数返回true的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public some(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean--><!--Device-BigInt64Array-public some(predicate: (element: BigInt, index: int, array: BigInt64Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: BigInt, index: int, array: BigInt64Array) =&gt; boolean | 是 | 最多接受三个参数的函数。 some方法会对数组中的每个元素调用predicate函数， 直到predicate返回true，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 除非predicate对某个数组元素返回true，否则返回false； 此时立即返回true。 |

## sort

```TypeScript
public sort(): this
```

按数值升序进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public sort(): this--><!--Device-BigInt64Array-public sort(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的BigInt64Array。 |

## sort

```TypeScript
public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this
```

原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this--><!--Device-BigInt64Array-public sort(compareFn?: (a: BigInt, b: BigInt) => int | BigInt): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: BigInt, b: BigInt) =&gt; int \| BigInt | 否 | 用于确定元素顺序的比较函数。 当第一个参数小于第二个参数时compareFn返回负值， 相等时返回0，否则返回正值。 默认按数值升序排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的BigInt64Array。 |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): BigInt64Array
```

创建与当前数组共享同一底层ArrayBuffer的新BigInt64Array， 可选择限定范围。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public subarray(begin?: int, end?: int): BigInt64Array--><!--Device-BigInt64Array-public subarray(begin?: int, end?: int): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | 起始索引（包含），默认值为0。 |
| end | int | 否 | 结束索引（不包含），默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 与当前数组共享同一底层ArrayBuffer的新BigInt64Array。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-BigInt64Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 包含BCP 47语言标签的字符串，或由此类 字符串组成的数组。 |
| options | object | 否 | 包含Intl.NumberFormat选项的部分或 全部属性的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 按区域设置转换后的结果。 |

## toReversed

```TypeScript
public toReversed(): BigInt64Array
```

返回元素顺序反转后的新BigInt64Array，原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toReversed(): BigInt64Array--><!--Device-BigInt64Array-public toReversed(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 元素顺序反转后的新BigInt64Array。 |

## toSorted

```TypeScript
public toSorted(): BigInt64Array
```

返回元素按升序排序后的新BigInt64Array，原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toSorted(): BigInt64Array--><!--Device-BigInt64Array-public toSorted(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 元素按升序排序后的新BigInt64Array。 |

## toString

```TypeScript
public toString(): string
```

返回以逗号分隔的BigInt64Array元素字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public toString(): string--><!--Device-BigInt64Array-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以逗号分隔数组元素所形成的字符串。 |

## valueOf

```TypeScript
public valueOf(): BigInt64Array
```

返回对象本身。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public valueOf(): BigInt64Array--><!--Device-BigInt64Array-public valueOf(): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) |  |

## values

```TypeScript
public values(): IterableIterator<BigInt>
```

按升序返回遍历BigInt64Array各元素值的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public values(): IterableIterator<BigInt>--><!--Device-BigInt64Array-public values(): IterableIterator<BigInt>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[BigInt](arkts-arkts-bigint-c.md)&gt; | 遍历所有元素的迭代器。 |

## with

```TypeScript
public with(index: int, value: long): BigInt64Array
```

返回将指定索引处的元素替换为给定值后的新BigInt64Array。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public with(index: int, value: long): BigInt64Array--><!--Device-BigInt64Array-public with(index: int, value: long): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：可以为任意整数。 |
| value | long | 是 | 待设置的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 将index处元素替换为value后的新BigInt64Array。 |

## with

```TypeScript
public with(index: int, value: BigInt): BigInt64Array
```

返回将指定索引处的元素替换为给定值后的新BigInt64Array。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public with(index: int, value: BigInt): BigInt64Array--><!--Device-BigInt64Array-public with(index: int, value: BigInt): BigInt64Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：可以为任意整数。 |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待设置的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt64Array](arkts-arkts-typedarrays-bigint64array-c.md) | 将index处元素替换为value后的新BigInt64Array。 |

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 8
```

每个元素占用的字节数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public static readonly BYTES_PER_ELEMENT: int = 8--><!--Device-BigInt64Array-public static readonly BYTES_PER_ELEMENT: int = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

底层ArrayBuffer。

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly buffer: ArrayBuffer--><!--Device-BigInt64Array-public readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public readonly byteLength: int
```

占用的字节数。 取值约束：可以为任意整数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly byteLength: int--><!--Device-BigInt64Array-public readonly byteLength: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public readonly byteOffset: int
```

底层ArrayBuffer中的字节偏移量。 取值约束：可以为任意整数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly byteOffset: int--><!--Device-BigInt64Array-public readonly byteOffset: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'BigInt64Array'
```

字符串\"BigInt64Array\"，表示该类型化数组的类型名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt64Array-public readonly name: string = 'BigInt64Array'--><!--Device-BigInt64Array-public readonly name: string = 'BigInt64Array'-End-->

**系统能力：** SystemCapability.Utils.Lang

