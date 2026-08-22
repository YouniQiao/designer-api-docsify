# Uint8ClampedArray

Uint8ClampedArray类。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class Uint8ClampedArray--><!--Device-unnamed-export class Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
public $_get(i: int): double
```

返回指定索引处的内部数值，不进行装箱。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public $_get(i: int): double--><!--Device-Uint8ClampedArray-public $_get(i: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | 待查看的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | index处的原始数值。 |

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<double>
```

Iterable接口实现。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public $_iterator(): IterableIterator<double>--><!--Device-Uint8ClampedArray-public $_iterator(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | 遍历所有元素的迭代器。 |

## $_set

```TypeScript
public $_set(index: int, val: double): void
```

设置指定索引处的值，不进行装箱。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public $_set(index: int, val: double): void--><!--Device-Uint8ClampedArray-public $_set(index: int, val: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| val | double | 是 | 待设置的值。 |

## at

```TypeScript
public at(index: int): double | undefined
```

返回指定索引处的元素，支持负数索引， 负数索引表示从数组末尾开始倒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public at(index: int): double | undefined--><!--Device-Uint8ClampedArray-public at(index: int): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待查看的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double \| undefined | 该索引处的元素；如果越界，则返回undefined。 |

## constructor

```TypeScript
public constructor()
```

创建空的Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor()--><!--Device-Uint8ClampedArray-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

根据length创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(length: int)--><!--Device-Uint8ClampedArray-public constructor(length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | 元素数量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(length: double)
```

根据length创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(length: double)--><!--Device-Uint8ClampedArray-public constructor(length: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | 元素数量。 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<int>)
```

根据FixedArray&lt;int&gt;创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(numbers: FixedArray<int>)--><!--Device-Uint8ClampedArray-public constructor(numbers: FixedArray<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;int&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<double>)
```

根据FixedArray&lt;double&gt;创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(numbers: FixedArray<double>)--><!--Device-Uint8ClampedArray-public constructor(numbers: FixedArray<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;double&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(numbers: Array<int>)
```

根据Array&lt;int&gt;创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(numbers: Array<int>)--><!--Device-Uint8ClampedArray-public constructor(numbers: Array<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | Array&lt;int&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(other: Uint8ClampedArray)
```

创建Uint8ClampedArray的副本。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(other: Uint8ClampedArray)--><!--Device-Uint8ClampedArray-public constructor(other: Uint8ClampedArray)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(elements: Iterable<double>)
```

根据通过Iterable&lt;double&gt;接口访问的数据创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(elements: Iterable<double>)--><!--Device-Uint8ClampedArray-public constructor(elements: Iterable<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;double&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)
```

根据data、byteOffset和length创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)--><!--Device-Uint8ClampedArray-public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayBufferLike](arkts-arkts-arraybufferlike-t.md) | 是 | 初始化数据。 |
| byteOffset | int | 是 | 相对于buf起始位置的字节偏移量。 <br>取值约束：应为整数。 |
| length | int | 是 | 新建Uint8ClampedArray中int类型元素的数量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

根据buf和byteOffset创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-Uint8ClampedArray-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | int | 是 | 相对于buf起始位置的字节偏移量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)
```

根据data、byteOffset和length创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-Uint8ClampedArray-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | double \| undefined | 是 | 相对于buf起始位置的字节偏移量。 |
| length | double \| undefined | 是 | 新建Uint8ClampedArray中int类型元素的数量。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

根据buf和byteOffset创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-Uint8ClampedArray-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | double | 是 | 相对于buf起始位置的字节偏移量。 |

## constructor

```TypeScript
public constructor(buf: ArrayLike<double> | ArrayBuffer)
```

根据buf创建Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-Uint8ClampedArray-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; \| ArrayBuffer | 是 | 初始化数据。 |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): Uint8ClampedArray
```

将startPos到endPos之间的内部元素复制到targetPos。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public copyWithin(target: int, start: int, end?: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public copyWithin(target: int, start: int, end?: int): Uint8ClampedArray-End-->

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
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 修改后的Uint8ClampedArray。 |

## copyWithin

```TypeScript
public copyWithin(target: int): Uint8ClampedArray
```

将Uint8ClampedArray从头到尾的内部元素复制到targetPos。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public copyWithin(target: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public copyWithin(target: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | 放置所复制元素的插入索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 修改后的Uint8ClampedArray。 |

## entries

```TypeScript
public entries(): IterableIterator<[int, double]>
```

返回由Uint8ClampedArray中每个条目的键值对组成的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public entries(): IterableIterator<[int, double]>--><!--Device-Uint8ClampedArray-public entries(): IterableIterator<[int, double]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, double]&gt; | 数组中每个条目的键值对。 |

## every

```TypeScript
public every(predicate: (element: double, index: int, array: Uint8ClampedArray) => boolean): boolean
```

判断指定的回调函数是否对数组中的所有元素都返回true。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public every(predicate: (element: double, index: int, array: Uint8ClampedArray) => boolean): boolean--><!--Device-Uint8ClampedArray-public every(predicate: (element: double, index: int, array: Uint8ClampedArray) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Uint8ClampedArray) =&gt; boolean | 是 | 最多接受三个参数的函数。 every方法会对数组中的每个元素调用predicate函数，直到predicate 返回false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 除非predicate对某个数组元素返回false，否则返回true； 此时立即返回false。 |

## fill

```TypeScript
public fill(value: int, start?: int, end?: int): Uint8ClampedArray
```

使用指定值填充Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public fill(value: int, start?: int, end?: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public fill(value: int, start?: int, end?: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的值。 <br>取值约束：应为整数。 |
| start | int | 否 | 开始填充的索引，默认值为0。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束填充的索引（不包含），默认值为数组长度。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 修改后的Uint8ClampedArray。 |

## fill

```TypeScript
public fill(value: double, start?: int, end?: int): Uint8ClampedArray
```

使用指定值填充Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public fill(value: double, start?: int, end?: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public fill(value: double, start?: int, end?: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 新的值。 |
| start | int | 否 | 开始填充的索引，默认值为0。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束填充的索引（不包含），默认值为数组长度。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 修改后的Uint8ClampedArray。 |

## filter

```TypeScript
public filter(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): Uint8ClampedArray
```

创建仅包含通过给定测试的元素的新Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public filter(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public filter(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8ClampedArray) =&gt; boolean | 是 | 用于测试每个元素的函数，调用时传入(value, index, array)。 保留该元素时应返回true，丢弃时返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 由通过测试的元素组成的新Uint8ClampedArray。 |

## find

```TypeScript
public find(predicate: (value: double, index: int, array: Uint8ClampedArray) => boolean): double | undefined
```

返回数组中第一个使predicate返回true的元素的值， 否则。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public find(predicate: (value: double, index: int, array: Uint8ClampedArray) => boolean): double | undefined--><!--Device-Uint8ClampedArray-public find(predicate: (value: double, index: int, array: Uint8ClampedArray) => boolean): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, array: Uint8ClampedArray) =&gt; boolean | 是 | find会按升序对数组中的每个元素调用一次predicate， 直到找到使predicate返回true的元素。如果找到这样的元素，find 会立即返回该元素的值；否则find返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double \| undefined | 查找到的元素；如果没有元素匹配，则返回undefined。 |

## findIndex

```TypeScript
public findIndex(predicate: (value: double, index: int, obj: Uint8ClampedArray) => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引， 否则。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public findIndex(predicate: (value: double, index: int, obj: Uint8ClampedArray) => boolean): int--><!--Device-Uint8ClampedArray-public findIndex(predicate: (value: double, index: int, obj: Uint8ClampedArray) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Uint8ClampedArray) =&gt; boolean | 是 | find会按升序对数组中的每个元素调用一次predicate， 直到找到使predicate返回true的元素。如果找到这样的元素， findIndex会立即返回该元素的索引；否则findIndex返回-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个匹配元素的索引。 |

## findLast

```TypeScript
public findLast(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): double
```

返回Uint8ClampedArray中最后一个满足给定predicate的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public findLast(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): double--><!--Device-Uint8ClampedArray-public findLast(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8ClampedArray) =&gt; boolean | 是 | 用于测试每个元素的函数，调用时传入(value, index, array)。 命中目标元素时应返回true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 最后一个满足predicate的元素。 |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): int
```

返回Uint8ClampedArray中最后一个满足给定predicate的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public findLastIndex(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): int--><!--Device-Uint8ClampedArray-public findLastIndex(fn: (val: double, index: int, array: Uint8ClampedArray) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8ClampedArray) =&gt; boolean | 是 | 用于测试每个元素的函数，调用时传入(value, index, array)。 命中目标元素时应返回true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 最后一个满足predicate的元素的索引，若不存在则返回-1。 |

## forEach

```TypeScript
public forEach(callbackfn: (value: double, index: int, array: Uint8ClampedArray) => void): void
```

按升序对Uint8ClampedArray中的每个元素调用一次给定的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public forEach(callbackfn: (value: double, index: int, array: Uint8ClampedArray) => void): void--><!--Device-Uint8ClampedArray-public forEach(callbackfn: (value: double, index: int, array: Uint8ClampedArray) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: double, index: int, array: Uint8ClampedArray) =&gt; void | 是 | 最多接受三个参数的函数。forEach会对数组中的每个元素 调用一次callbackfn函数。 |

## from

```TypeScript
public static from(arr: FixedArray<int>): Uint8ClampedArray
```

根据FixedArray&lt;int&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from(arr: FixedArray<int>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from(arr: FixedArray<int>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 待转换为数组的FixedArray类型实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## from

```TypeScript
public static from(set: Set<int>): Uint8ClampedArray
```

根据std.core.Set&lt;int&gt;类型的集合创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from(set: Set<int>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from(set: Set<int>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;int&gt; | 是 | 待转换为数组的Set对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## from

```TypeScript
public static from(arr: Uint8ClampedArray): Uint8ClampedArray
```

根据同类型的数组创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from(arr: Uint8ClampedArray): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from(arr: Uint8ClampedArray): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 是 | 待转换为新数组的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## from

```TypeScript
public static from(arr: Array<int>): Uint8ClampedArray
```

根据std.core.Array&lt;int&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from(arr: Array<int>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from(arr: Array<int>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array&lt;int&gt; | 是 | 待转换为数组的std.core.Array类型实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## from

```TypeScript
public static from(arr: ArrayLike<double>): Uint8ClampedArray
```

根据类数组对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from(arr: ArrayLike<double>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from(arr: ArrayLike<double>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | 待转换为数组的类数组对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8ClampedArray
```

根据类数组对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 | 待转换为数组的类数组对象。 |
| mapfn | (v: T, k: double) =&gt; double | 是 | 对数组中每个元素调用的映射函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## from

```TypeScript
public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8ClampedArray
```

根据可迭代对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;double&gt; | 是 | 待转换为数组的可迭代对象。 |
| mapfn | (v: double, k: double) =&gt; double | 否 | 对数组中每个元素调用的函数。 默认使用恒等函数，即原样返回该元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## includes

```TypeScript
public includes(searchElement: int, fromIndex: int): boolean
```

判断Uint8ClampedArray中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public includes(searchElement: int, fromIndex: int): boolean--><!--Device-Uint8ClampedArray-public includes(searchElement: int, fromIndex: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待查找的元素。 <br>取值约束：应为整数。 |
| fromIndex | int | 是 | 在该数组中开始查找searchElement的位置。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于Uint8ClampedArray中则返回true，否则返回false。 |

## includes

```TypeScript
public includes(searchElement: int): boolean
```

判断Uint8ClampedArray中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public includes(searchElement: int): boolean--><!--Device-Uint8ClampedArray-public includes(searchElement: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待查找的元素，查找从索引0处开始。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于Uint8ClampedArray中则返回true，否则返回false。 |

## includes

```TypeScript
public includes(searchElement: double, fromIndex?: int): boolean
```

判断Uint8ClampedArray中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public includes(searchElement: double, fromIndex?: int): boolean--><!--Device-Uint8ClampedArray-public includes(searchElement: double, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | 待查找的元素。 |
| fromIndex | int | 否 | 在该数组中开始查找的位置，默认值为0。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于Uint8ClampedArray中则返回true，否则返回false。 |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

返回指定值在Uint8ClampedArray中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public indexOf(searchElement: int): int--><!--Device-Uint8ClampedArray-public indexOf(searchElement: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待在数组中查找的值，查找从索引0处开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 存在时返回该元素的索引，否则返回-1。 |

## indexOf

```TypeScript
public indexOf(searchElement: int, fromIndex: int): int
```

返回指定值在Uint8ClampedArray中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-Uint8ClampedArray-public indexOf(searchElement: int, fromIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待在数组中查找的值。 |
| fromIndex | int | 是 | 开始查找的数组索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 存在时返回该元素的索引，否则返回-1。 |

## indexOf

```TypeScript
public indexOf(searchElement: double, fromIndex?: int): int
```

返回指定值在Uint8ClampedArray中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public indexOf(searchElement: double, fromIndex?: int): int--><!--Device-Uint8ClampedArray-public indexOf(searchElement: double, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | 待在数组中查找的值。 |
| fromIndex | int | 否 | 开始查找的数组索引，默认值为0。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 存在时返回该元素的索引，否则返回-1。 |

## join

```TypeScript
public join(separator?: string): string
```

使用指定的分隔字符串连接数组中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public join(separator?: string): string--><!--Device-Uint8ClampedArray-public join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | 用于在结果字符串中分隔数组相邻元素的 字符串。如果不传入该参数，则元素之间以逗号分隔。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 使用分隔符连接所有数组元素而成的字符串。 |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

返回Uint8ClampedArray中索引的列表。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public keys(): IterableIterator<int>--><!--Device-Uint8ClampedArray-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | 遍历数组索引的迭代器。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

返回指定值在Uint8ClampedArray中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: int): int--><!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: int): int-End-->

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
public lastIndexOf(searchElement: double): int
```

返回指定值在Uint8ClampedArray中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: double): int--><!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | 待在数组中查找的值，查找从索引length - 1处开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | searchElement最靠右的索引，必须小于length；未找到时返回-1。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int, fromIndex: int): int
```

返回指定值在Uint8ClampedArray中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

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
public lastIndexOf(searchElement: double, fromIndex: int | undefined): int
```

返回指定值在Uint8ClampedArray中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int--><!--Device-Uint8ClampedArray-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | 待在数组中查找的值。 |
| fromIndex | int \| undefined | 是 | 开始查找的数组索引。 如果fromIndex为undefined，则从索引0处开始查找。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | searchElement最靠右的索引，必须小于或等于fromIndex；未找到时返回-1。 |

## map

```TypeScript
public map(fn: (val: double, index: int, array: Uint8ClampedArray) => double): Uint8ClampedArray
```

对当前Uint8ClampedArray的所有元素执行fn(arr[i])，创建新的Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public map(fn: (val: double, index: int, array: Uint8ClampedArray) => double): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public map(fn: (val: double, index: int, array: Uint8ClampedArray) => double): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8ClampedArray) =&gt; double | 是 | 对当前Uint8ClampedArray中每个元素应用的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray， 其中每个元素均由当前Uint8ClampedArray的元素应用fn后得到。 |

## of

```TypeScript
public static of(...items: FixedArray<short>): Uint8ClampedArray
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static of(...items: FixedArray<short>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static of(...items: FixedArray<short>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;short&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## of

```TypeScript
public static of(...items: FixedArray<int>): Uint8ClampedArray
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static of(...items: FixedArray<int>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static of(...items: FixedArray<int>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## of

```TypeScript
public static of(...items: FixedArray<double>): Uint8ClampedArray
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static of(...items: FixedArray<double>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static of(...items: FixedArray<double>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## of

```TypeScript
public static of(): Uint8ClampedArray
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static of(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public static of(): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 新的Uint8ClampedArray。 |

## reduce

```TypeScript
public reduce<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) => U,
        initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) => U,        initialValue: U): U--><!--Device-Uint8ClampedArray-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) =&gt; U | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 其值作为累加初始值的参数。 首次调用callbackfn时，将该值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 上一次调用回调函数得到的累加结果。 |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Uint8ClampedArray) => double): double
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8ClampedArray) => double): double--><!--Device-Uint8ClampedArray-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8ClampedArray) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Uint8ClampedArray) =&gt; double | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 首次调用callbackfn时，将数组的第一个元素值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 上一次调用回调函数得到的累加结果。 |

## reduceRight

```TypeScript
public reduceRight<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) => U,
        initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public reduceRight<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) => U,        initialValue: U): U--><!--Device-Uint8ClampedArray-public reduceRight<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Uint8ClampedArray) =&gt; U | 是 | 最多接受四个参数的函数。 reduceRight方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 其值作为累加初始值的参数。 首次调用callbackfn时，将该值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 上一次调用回调函数得到的累加结果。 |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Uint8ClampedArray) => double): double
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8ClampedArray) => double): double--><!--Device-Uint8ClampedArray-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8ClampedArray) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Uint8ClampedArray) =&gt; double | 是 | 最多接受四个参数的函数。 reduceRight方法会对数组中的每个元素调用一次callbackfn函数。 首次调用callbackfn时，将数组的最后一个元素值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 上一次调用回调函数得到的累加结果。 |

## reverse

```TypeScript
public reverse(): Uint8ClampedArray
```

原地反转Uint8ClampedArray中的元素，并返回修改后的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public reverse(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public reverse(): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 反转后的Uint8ClampedArray。 |

## set

```TypeScript
public set(insertPos: int, val: int): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(insertPos: int, val: int): void--><!--Device-Uint8ClampedArray-public set(insertPos: int, val: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| val | int | 是 | 待设置的值。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(insertPos: int, val: double): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(insertPos: int, val: double): void--><!--Device-Uint8ClampedArray-public set(insertPos: int, val: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertPos | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| val | double | 是 | 待设置的值。 |

## set

```TypeScript
public set(arr: FixedArray<int>, insertPos: int): void
```

从insertPos开始，将arr中的所有元素复制到当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(arr: FixedArray<int>, insertPos: int): void--><!--Device-Uint8ClampedArray-public set(arr: FixedArray<int>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 复制数据的源数组。 |
| insertPos | int | 是 | 写入arr数据的起始索引。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(arr: FixedArray<double>, insertPos: int): void
```

从insertPos开始，将arr中的所有元素复制到当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(arr: FixedArray<double>, insertPos: int): void--><!--Device-Uint8ClampedArray-public set(arr: FixedArray<double>, insertPos: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | 复制数据的源数组。 |
| insertPos | int | 是 | 写入arr数据的起始索引。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(arr: FixedArray<int>): void
```

将arr中的所有元素复制到当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(arr: FixedArray<int>): void--><!--Device-Uint8ClampedArray-public set(arr: FixedArray<int>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(arr: FixedArray<double>): void
```

将arr中的所有元素复制到当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(arr: FixedArray<double>): void--><!--Device-Uint8ClampedArray-public set(arr: FixedArray<double>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(array: Uint8ClampedArray): void
```

将arr中的所有元素复制到当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(array: Uint8ClampedArray): void--><!--Device-Uint8ClampedArray-public set(array: Uint8ClampedArray): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(array: Uint8ClampedArray, offset: int): void
```

将arr中的所有元素复制到当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(array: Uint8ClampedArray, offset: int): void--><!--Device-Uint8ClampedArray-public set(array: Uint8ClampedArray, offset: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 是 | 复制数据的源数组。 |
| offset | int | 是 | 写入arr数据的起始索引。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(array: ArrayLike<double>, offset: int = 0): void
```

将ArrayLike对象中的元素复制到Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public set(array: ArrayLike<double>, offset: int = 0): void--><!--Device-Uint8ClampedArray-public set(array: ArrayLike<double>, offset: int = 0): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;double&gt; | 是 | 包含待复制元素的ArrayLike对象。 |
| offset | int | 是 | 可选参数，指定在目标数组中开始写入源数组值的 偏移量，默认值为0。 <br>取值约束：应为整数。 |

## slice

```TypeScript
public slice(begin?: int, end?: int): Uint8ClampedArray
```

使用[begin, end]区间截取当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public slice(begin?: int, end?: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public slice(begin?: int, end?: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start - 截取的起始索引，默认值为0。 |
| end | int | 否 | 截取的结束索引，默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 包含当前Uint8ClampedArray[begin;end)区间元素的新Uint8ClampedArray， 其中不包含结束索引处的元素。 |

## slice

```TypeScript
public slice(begin: int): Uint8ClampedArray
```

使用[begin, this.lengthInt]区间截取当前Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public slice(begin: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public slice(begin: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | 截取的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 包含当前 Uint8ClampedArray[begin, this.lengthInt]区间元素的新Uint8ClampedArray。 |

## some

```TypeScript
public some(predicate: (element: double, index: int, array: Uint8ClampedArray) => boolean): boolean
```

判断数组中是否存在使指定回调函数返回true的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public some(predicate: (element: double, index: int, array: Uint8ClampedArray) => boolean): boolean--><!--Device-Uint8ClampedArray-public some(predicate: (element: double, index: int, array: Uint8ClampedArray) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Uint8ClampedArray) =&gt; boolean | 是 | 最多接受三个参数的函数。 some方法会对数组中的每个元素调用predicate函数， 直到predicate返回true，或遍历完整个数组。 |

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

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public sort(): this--><!--Device-Uint8ClampedArray-public sort(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的Uint8ClampedArray。 |

## sort

```TypeScript
public sort(compareFn?: (a: double, b: double) => int): this
```

原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public sort(compareFn?: (a: double, b: double) => int): this--><!--Device-Uint8ClampedArray-public sort(compareFn?: (a: double, b: double) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: double, b: double) =&gt; int | 否 | 用于确定元素顺序的比较函数。 当第一个参数小于第二个参数时compareFn返回负值， 相等时返回0，否则返回正值。 默认按数值升序排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的Uint8ClampedArray。 |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): Uint8ClampedArray
```

创建与当前数组共享同一底层Buffer的Uint8ClampedArray。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public subarray(begin?: int, end?: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public subarray(begin?: int, end?: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | 起始索引（包含），默认值为0。 |
| end | int | 否 | 结束索引（不包含），默认值为数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 与当前数组共享同一底层Buffer的新Uint8ClampedArray。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Uint8ClampedArray-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
public toReversed(): Uint8ClampedArray
```

返回元素顺序反转后的新Uint8ClampedArray。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public toReversed(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public toReversed(): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 元素反转后的新Uint8ClampedArray。 |

## toSorted

```TypeScript
public toSorted(): Uint8ClampedArray
```

返回元素按升序排序后的新Uint8ClampedArray。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public toSorted(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public toSorted(): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 排序后的新Uint8ClampedArray。 |

## toString

```TypeScript
public toString(): string
```

返回以逗号分隔的Uint8ClampedArray元素字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public toString(): string--><!--Device-Uint8ClampedArray-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以逗号分隔数组元素所形成的字符串。 |

## toUint8Clamped

```TypeScript
public static toUint8Clamped(val: double): int
```

将double值截断为[0, 255]范围内的8位无符号整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static toUint8Clamped(val: double): int--><!--Device-Uint8ClampedArray-public static toUint8Clamped(val: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | double | 是 | 待转换并截断的浮点值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 截断后的8位无符号整数值。 |

## valueOf

```TypeScript
public valueOf(): Uint8ClampedArray
```

返回Uint8ClampedArray的原始值，即该数组对象本身。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public valueOf(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public valueOf(): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 该Uint8ClampedArray对象本身。 |

## values

```TypeScript
public values(): IterableIterator<double>
```

返回遍历Uint8ClampedArray各元素值的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public values(): IterableIterator<double>--><!--Device-Uint8ClampedArray-public values(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | 按顺序产出每个元素的迭代器。 |

## with

```TypeScript
public with(index: int, value: int): Uint8ClampedArray
```

返回将指定索引处的元素替换为给定值后的新Uint8ClampedArray， 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public with(index: int, value: int): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public with(index: int, value: int): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| value | int | 是 | 待设置的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 将index处元素替换后的新Uint8ClampedArray。 |

## with

```TypeScript
public with(index: int, value: double): Uint8ClampedArray
```

返回将指定索引处的元素替换为给定值后的新Uint8ClampedArray， 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public with(index: int, value: double): Uint8ClampedArray--><!--Device-Uint8ClampedArray-public with(index: int, value: double): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| value | double | 是 | 待设置的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Uint8ClampedArray](arkts-arkts-typeduarrays-uint8clampedarray-c.md) | 将index处元素替换后的新Uint8ClampedArray。 |

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 1
```

每个元素占用的字节数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public static readonly BYTES_PER_ELEMENT: int = 1--><!--Device-Uint8ClampedArray-public static readonly BYTES_PER_ELEMENT: int = 1-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

底层Buffer。

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public readonly buffer: ArrayBuffer--><!--Device-Uint8ClampedArray-public readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'Uint8ClampedArray'
```

字符串\"Uint8ClampedArray\"，表示该类型化数组的类型名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8ClampedArray-public readonly name: string = 'Uint8ClampedArray'--><!--Device-Uint8ClampedArray-public readonly name: string = 'Uint8ClampedArray'-End-->

**系统能力：** SystemCapability.Utils.Lang

