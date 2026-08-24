# Uint8Array

Uint8Array类。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class Uint8Array--><!--Device-unnamed-export class Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
public $_get(i: int): double
```

返回指定索引处的number实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_get(i: int): double--><!--Device-Uint8Array-public $_get(i: int): double-End-->

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

Iterator接口实现。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_iterator(): IterableIterator<double>--><!--Device-Uint8Array-public $_iterator(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | 按顺序产出每个元素的迭代器。 |

## $_set

```TypeScript
public $_set(index: int, val: int): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_set(index: int, val: int): void--><!--Device-Uint8Array-public $_set(index: int, val: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| val | int | 是 | 待设置的值。 <br>取值约束：应为整数。 |

## $_set

```TypeScript
public $_set(index: int, val: double): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public $_set(index: int, val: double): void--><!--Device-Uint8Array-public $_set(index: int, val: double): void-End-->

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

当索引合法时，返回指定索引处的基本类型实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public at(index: int): double | undefined--><!--Device-Uint8Array-public at(index: int): double | undefined-End-->

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

创建空的Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor()--><!--Device-Uint8Array-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(length: int)
```

根据length创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(length: int)--><!--Device-Uint8Array-public constructor(length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | 元素数量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(length: double)
```

根据length创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(length: double)--><!--Device-Uint8Array-public constructor(length: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | 元素数量。 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<int>)
```

根据FixedArray&lt;int&gt;创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(numbers: FixedArray<int>)--><!--Device-Uint8Array-public constructor(numbers: FixedArray<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;int&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(numbers: FixedArray<double>)
```

根据FixedArray&lt;double&gt;创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(numbers: FixedArray<double>)--><!--Device-Uint8Array-public constructor(numbers: FixedArray<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | FixedArray&lt;double&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(numbers: Array<int>)
```

根据Array&lt;int&gt;创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(numbers: Array<int>)--><!--Device-Uint8Array-public constructor(numbers: Array<int>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numbers | Array&lt;int&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(other: Uint8Array)
```

创建Uint8Array的副本。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(other: Uint8Array)--><!--Device-Uint8Array-public constructor(other: Uint8Array)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Uint8Array | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(elements: Iterable<double>)
```

根据通过Iterable&lt;double&gt;接口访问的数据创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(elements: Iterable<double>)--><!--Device-Uint8Array-public constructor(elements: Iterable<double>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;double&gt; | 是 | 初始化数据。 |

## constructor

```TypeScript
public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)
```

根据data、byteOffset和length创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)--><!--Device-Uint8Array-public constructor(buf: ArrayBufferLike, byteOffset: int, length: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | [ArrayBufferLike](arkts-arkts-arraybufferlike-t.md) | 是 | 初始化数据。 |
| byteOffset | int | 是 | 相对于buf起始位置的字节偏移量。 <br>取值约束：应为整数。 |
| length | int | 是 | 新建Uint8Array中int类型元素的数量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: int)
```

根据buf和byteOffset创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: int)--><!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: int)-End-->

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

根据data、byteOffset和length创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)--><!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double | undefined, length: double | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 初始化数据。 |
| byteOffset | double \| undefined | 是 | 相对于buf起始位置的字节偏移量。 |
| length | double \| undefined | 是 | 新建Uint8Array中int类型元素的数量。 |

## constructor

```TypeScript
public constructor(buf: ArrayBuffer, byteOffset: double)
```

根据buf和byteOffset创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double)--><!--Device-Uint8Array-public constructor(buf: ArrayBuffer, byteOffset: double)-End-->

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

根据buf创建Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)--><!--Device-Uint8Array-public constructor(buf: ArrayLike<double> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayLike&lt;double&gt; \| ArrayBuffer | 是 | 初始化数据。 |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): Uint8Array
```

将startPos到endPos之间的内部元素复制到targetPos。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public copyWithin(target: int, start: int, end?: int): Uint8Array--><!--Device-Uint8Array-public copyWithin(target: int, start: int, end?: int): Uint8Array-End-->

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
| Uint8Array | 修改后的Uint8Array。 |

## copyWithin

```TypeScript
public copyWithin(target: int): Uint8Array
```

将Uint8Array从头到尾的内部元素复制到targetPos。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public copyWithin(target: int): Uint8Array--><!--Device-Uint8Array-public copyWithin(target: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | 放置所复制元素的插入索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 修改后的Uint8Array。 |

## entries

```TypeScript
public entries(): IterableIterator<[int, double]>
```

返回由Uint8Array中每个条目的键值对组成的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public entries(): IterableIterator<[int, double]>--><!--Device-Uint8Array-public entries(): IterableIterator<[int, double]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, double]&gt; | 遍历每个元素[index, value]对的迭代器。 |

## every

```TypeScript
public every(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean
```

判断指定的回调函数是否对数组中的所有元素都返回true。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public every(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean--><!--Device-Uint8Array-public every(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Uint8Array) =&gt; boolean | 是 | 最多接受三个参数的函数。 every方法会对数组中的每个元素调用predicate函数，直到predicate 返回false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 除非predicate对某个数组元素返回false，否则返回true； 此时立即返回false。 |

## fill

```TypeScript
public fill(value: int, start?: int, end?: int): Uint8Array
```

使用指定值填充Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public fill(value: int, start?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public fill(value: int, start?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的值。 <br>取值约束：应为整数。 |
| start | int | 否 | 开始填充的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束填充的索引（不包含）。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 修改后的Uint8Array。 |

## fill

```TypeScript
public fill(value: double, start?: int, end?: int): Uint8Array
```

使用指定值填充Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public fill(value: double, start?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public fill(value: double, start?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 新的值。 |
| start | int | 否 | 开始填充的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束填充的索引（不包含）。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 修改后的Uint8Array。 |

## filter

```TypeScript
public filter(fn: (val: double, index: int, array: Uint8Array) => boolean): Uint8Array
```

根据条件fn从当前Uint8Array创建新的Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public filter(fn: (val: double, index: int, array: Uint8Array) => boolean): Uint8Array--><!--Device-Uint8Array-public filter(fn: (val: double, index: int, array: Uint8Array) => boolean): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; boolean | 是 | 对每个元素应用的判断条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 由通过测试的元素组成的新Uint8Array。 |

## find

```TypeScript
public find(predicate: (value: double, index: int, array: Uint8Array) => boolean): double | undefined
```

返回数组中第一个使predicate返回true的元素的值， 否则。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public find(predicate: (value: double, index: int, array: Uint8Array) => boolean): double | undefined--><!--Device-Uint8Array-public find(predicate: (value: double, index: int, array: Uint8Array) => boolean): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, array: Uint8Array) =&gt; boolean | 是 | find会按升序对数组中的每个元素调用一次predicate， 直到找到使predicate返回true的元素。如果找到这样的元素，find 会立即返回该元素的值；否则find返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double \| undefined | 查找到的元素；如果没有元素匹配，则返回undefined。 |

## findIndex

```TypeScript
public findIndex(predicate: (value: double, index: int, obj: Uint8Array) => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引， 否则。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public findIndex(predicate: (value: double, index: int, obj: Uint8Array) => boolean): int--><!--Device-Uint8Array-public findIndex(predicate: (value: double, index: int, obj: Uint8Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: double, index: int, obj: Uint8Array) =&gt; boolean | 是 | find会按升序对数组中的每个元素调用一次predicate， 直到找到使predicate返回true的元素。如果找到这样的元素， findIndex会立即返回该元素的索引；否则findIndex返回-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个匹配元素的索引。 |

## findLast

```TypeScript
public findLast(fn: (val: double, index: int, array: Uint8Array) => boolean): double
```

查找Uint8Array中最后一个满足该条件的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public findLast(fn: (val: double, index: int, array: Uint8Array) => boolean): double--><!--Device-Uint8Array-public findLast(fn: (val: double, index: int, array: Uint8Array) => boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; boolean | 是 | 判断条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 最后一个满足fn的元素。 |

## findLastIndex

```TypeScript
public findLastIndex(fn: (val: double, index: int, array: Uint8Array) => boolean): int
```

查找Uint8Array中最后一个满足该条件的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public findLastIndex(fn: (val: double, index: int, array: Uint8Array) => boolean): int--><!--Device-Uint8Array-public findLastIndex(fn: (val: double, index: int, array: Uint8Array) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; boolean | 是 | 判断条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 最后一个满足fn的元素的索引，若不存在则返回-1。 |

## forEach

```TypeScript
public forEach(callbackfn: (value: double, index: int, array: Uint8Array) => void): void
```

对Uint8Array中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public forEach(callbackfn: (value: double, index: int, array: Uint8Array) => void): void--><!--Device-Uint8Array-public forEach(callbackfn: (value: double, index: int, array: Uint8Array) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: double, index: int, array: Uint8Array) =&gt; void | 是 | 最多接受三个参数的函数。forEach会对数组中的每个元素 调用一次callbackfn函数。 |

## from

```TypeScript
public static from(arr: FixedArray<int>): Uint8Array
```

根据FixedArray&lt;int&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: FixedArray<int>): Uint8Array--><!--Device-Uint8Array-public static from(arr: FixedArray<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 待转换为数组的FixedArray类型实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from(set: Set<int>): Uint8Array
```

根据std.core.Set&lt;int&gt;类型的集合创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(set: Set<int>): Uint8Array--><!--Device-Uint8Array-public static from(set: Set<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;int&gt; | 是 | 待转换为数组的Set对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from(arr: Uint8Array): Uint8Array
```

根据同类型的数组创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: Uint8Array): Uint8Array--><!--Device-Uint8Array-public static from(arr: Uint8Array): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Uint8Array | 是 | 待转换为新数组的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from(arr: Int8Array): Uint8Array
```

根据除符号性外类型相同的数组创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: Int8Array): Uint8Array--><!--Device-Uint8Array-public static from(arr: Int8Array): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Int8Array | 是 | 待转换为新数组的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from(arr: Array<int>): Uint8Array
```

根据std.core.Array&lt;int&gt;对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: Array<int>): Uint8Array--><!--Device-Uint8Array-public static from(arr: Array<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | Array&lt;int&gt; | 是 | 待转换为数组的std.core.Array类型实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from(arr: ArrayLike<double>): Uint8Array
```

根据类数组对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arr: ArrayLike<double>): Uint8Array--><!--Device-Uint8Array-public static from(arr: ArrayLike<double>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | ArrayLike&lt;double&gt; | 是 | 待转换为数组的类数组对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8Array
```

根据类数组对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8Array--><!--Device-Uint8Array-public static from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: double) => double): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | ArrayLike&lt;T&gt; | 是 | 待转换为数组的类数组对象。 |
| mapfn | (v: T, k: double) =&gt; double | 是 | 对数组中每个元素调用的映射函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## from

```TypeScript
public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8Array
```

根据可迭代对象创建数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8Array--><!--Device-Uint8Array-public static from(arrayLike: Iterable<double>, mapfn?: (v: double, k: double) => double): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;double&gt; | 是 | 待转换为数组的可迭代对象。 |
| mapfn | (v: double, k: double) =&gt; double | 否 | 对数组中每个元素调用的映射函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## includes

```TypeScript
public includes(searchElement: int, fromIndex: int): boolean
```

判断Uint8Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public includes(searchElement: int, fromIndex: int): boolean--><!--Device-Uint8Array-public includes(searchElement: int, fromIndex: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待查找的元素。 <br>取值约束：应为整数。 |
| fromIndex | int | 是 | 在该数组中开始查找searchElement的位置。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于Uint8Array中则返回true，否则返回false。 |

## includes

```TypeScript
public includes(searchElement: int): boolean
```

判断Uint8Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public includes(searchElement: int): boolean--><!--Device-Uint8Array-public includes(searchElement: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | int | 是 | 待查找的元素，查找从索引0处开始。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于Uint8Array中则返回true，否则返回false。 |

## includes

```TypeScript
public includes(searchElement: double, fromIndex?: int): boolean
```

判断Uint8Array中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public includes(searchElement: double, fromIndex?: int): boolean--><!--Device-Uint8Array-public includes(searchElement: double, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | 待查找的元素。 |
| fromIndex | int | 否 | 在该数组中开始查找searchElement的位置。 如果fromIndex为undefined，则从索引0处开始查找。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果searchElement存在于Uint8Array中则返回true，否则返回false。 |

## indexOf

```TypeScript
public indexOf(searchElement: int): int
```

返回指定值在Uint8Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public indexOf(searchElement: int): int--><!--Device-Uint8Array-public indexOf(searchElement: int): int-End-->

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

返回指定值在Uint8Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public indexOf(searchElement: int, fromIndex: int): int--><!--Device-Uint8Array-public indexOf(searchElement: int, fromIndex: int): int-End-->

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

返回指定值在Uint8Array中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public indexOf(searchElement: double, fromIndex?: int): int--><!--Device-Uint8Array-public indexOf(searchElement: double, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | double | 是 | 待在数组中查找的值。 |
| fromIndex | int | 否 | 开始查找的数组索引。 如果不传入fromIndex，则从索引0开始查找。 <br>取值约束：应为整数。 |

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

<!--Device-Uint8Array-public join(separator?: string): string--><!--Device-Uint8Array-public join(separator?: string): string-End-->

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

返回Uint8Array中键的列表。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public keys(): IterableIterator<int>--><!--Device-Uint8Array-public keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | 遍历数组索引的迭代器。 |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: int): int
```

返回指定值在Uint8Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: int): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: int): int-End-->

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

返回指定值在Uint8Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: double): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: double): int-End-->

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

返回指定值在Uint8Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: int, fromIndex: int): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: int, fromIndex: int): int-End-->

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

返回指定值在Uint8Array中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int--><!--Device-Uint8Array-public lastIndexOf(searchElement: double, fromIndex: int | undefined): int-End-->

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
public map(fn: (val: double, index: int, array: Uint8Array) => number): Uint8Array
```

对当前Uint8Array的所有元素执行fn(arr[i])，创建新的Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public map(fn: (val: double, index: int, array: Uint8Array) => number): Uint8Array--><!--Device-Uint8Array-public map(fn: (val: double, index: int, array: Uint8Array) => number): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (val: double, index: int, array: Uint8Array) =&gt; number | 是 | 对当前Uint8Array中每个元素应用的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array，其中每个元素都是回调函数的返回结果。 |

## of

```TypeScript
public static of(...items: FixedArray<short>): Uint8Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(...items: FixedArray<short>): Uint8Array--><!--Device-Uint8Array-public static of(...items: FixedArray<short>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;short&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## of

```TypeScript
public static of(...items: FixedArray<int>): Uint8Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(...items: FixedArray<int>): Uint8Array--><!--Device-Uint8Array-public static of(...items: FixedArray<int>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;int&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## of

```TypeScript
public static of(...items: FixedArray<double>): Uint8Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(...items: FixedArray<double>): Uint8Array--><!--Device-Uint8Array-public static of(...items: FixedArray<double>): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;double&gt; | 是 | 待包含在新数组对象中的一组元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## of

```TypeScript
public static of(): Uint8Array
```

根据一组元素返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static of(): Uint8Array--><!--Device-Uint8Array-public static of(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 新的Uint8Array。 |

## reduce

```TypeScript
public reduce<U = double>(
        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) => U,
        initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) => U,        initialValue: U): U--><!--Device-Uint8Array-public reduce<U = double>(        callbackfn: (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double, currentIndex: int, array: Uint8Array) =&gt; U | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 其值作为累加初始值的参数。 首次调用callbackfn时，将该值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 上一次调用回调函数得到的累加结果。 |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Uint8Array) => double): double
```

对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double--><!--Device-Uint8Array-public reduce(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Uint8Array) =&gt; double | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 首次调用callbackfn时，将数组的第一个元素值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 上一次调用回调函数得到的累加结果。 |

## reduceRight

```TypeScript
public reduceRight<U = double>(callbackfn: (previousValue: U, currentValue: double,
        currentIndex: int, array: Uint8Array) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduceRight<U = double>(callbackfn: (previousValue: U, currentValue: double,        currentIndex: int, array: Uint8Array) => U, initialValue: U): U--><!--Device-Uint8Array-public reduceRight<U = double>(callbackfn: (previousValue: U, currentValue: double,        currentIndex: int, array: Uint8Array) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: double,         currentIndex: int, array: Uint8Array) =&gt; U | 是 | 最多接受四个参数的函数。 reduceRight方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 其值作为累加初始值的参数。 首次调用callbackfn时，将该值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 上一次调用回调函数得到的累加结果。 |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,
        array: Uint8Array) => double): double
```

按降序对数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果， 并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double--><!--Device-Uint8Array-public reduceRight(callbackfn: (previousValue: double, currentValue: double, currentIndex: int,        array: Uint8Array) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: double, currentValue: double, currentIndex: int,         array: Uint8Array) =&gt; double | 是 | 最多接受四个参数的函数。 reduceRight方法会对数组中的每个元素调用一次callbackfn函数。 首次调用callbackfn时，将数组的最后一个元素值作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 上一次调用回调函数得到的累加结果。 |

## reverse

```TypeScript
public reverse(): Uint8Array
```

基于当前Uint8Array的反转数据创建新的Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public reverse(): Uint8Array--><!--Device-Uint8Array-public reverse(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 元素顺序反转后的新Uint8Array。 |

## set

```TypeScript
public set(insertPos: int, val: int): void
```

将val赋值为index处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(insertPos: int, val: int): void--><!--Device-Uint8Array-public set(insertPos: int, val: int): void-End-->

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

<!--Device-Uint8Array-public set(insertPos: int, val: double): void--><!--Device-Uint8Array-public set(insertPos: int, val: double): void-End-->

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

从insertPos开始，将arr中的所有元素复制到当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<int>, insertPos: int): void--><!--Device-Uint8Array-public set(arr: FixedArray<int>, insertPos: int): void-End-->

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

从insertPos开始，将arr中的所有元素复制到当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<double>, insertPos: int): void--><!--Device-Uint8Array-public set(arr: FixedArray<double>, insertPos: int): void-End-->

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

将arr中的所有元素复制到当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<int>): void--><!--Device-Uint8Array-public set(arr: FixedArray<int>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(arr: FixedArray<double>): void
```

将arr中的所有元素复制到当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(arr: FixedArray<double>): void--><!--Device-Uint8Array-public set(arr: FixedArray<double>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(array: Uint8Array): void
```

将arr中的所有元素复制到当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(array: Uint8Array): void--><!--Device-Uint8Array-public set(array: Uint8Array): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | Uint8Array | 是 | 复制数据的源数组。 |

## set

```TypeScript
public set(array: Uint8Array, offset: int): void
```

将arr中的所有元素复制到当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(array: Uint8Array, offset: int): void--><!--Device-Uint8Array-public set(array: Uint8Array, offset: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | Uint8Array | 是 | 复制数据的源数组。 |
| offset | int | 是 | 写入arr数据的起始索引。 <br>取值约束：应为整数。 |

## set

```TypeScript
public set(array: ArrayLike<double>, offset: int = 0): void
```

将ArrayLike对象中的元素复制到Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public set(array: ArrayLike<double>, offset: int = 0): void--><!--Device-Uint8Array-public set(array: ArrayLike<double>, offset: int = 0): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | ArrayLike&lt;double&gt; | 是 | 包含待复制元素的ArrayLike对象。 |
| offset | int | 是 | 可选参数，指定在目标数组中开始写入源数组值的 偏移量，默认值为0。 <br>取值约束：应为整数。 |

## slice

```TypeScript
public slice(begin?: int, end?: int): Uint8Array
```

使用[begin, end]区间截取当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public slice(begin?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public slice(begin?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | start - 截取的起始索引。 |
| end | int | 否 | 截取的结束索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 包含当前Uint8Array[begin;end)区间元素的新Uint8Array， 其中不包含结束索引处的元素。 |

## slice

```TypeScript
public slice(begin: int): Uint8Array
```

使用[begin, this.lengthInt]区间截取当前Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public slice(begin: int): Uint8Array--><!--Device-Uint8Array-public slice(begin: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | 截取的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 包含当前 Uint8Array[begin, this.lengthInt]区间元素的新Uint8Array。 |

## some

```TypeScript
public some(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean
```

判断数组中是否存在使指定回调函数返回true的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public some(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean--><!--Device-Uint8Array-public some(predicate: (element: double, index: int, array: Uint8Array) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (element: double, index: int, array: Uint8Array) =&gt; boolean | 是 | 最多接受三个参数的函数。 some方法会对数组中的每个元素调用predicate函数， 直到predicate返回true，或遍历完整个数组。 |

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

<!--Device-Uint8Array-public sort(): this--><!--Device-Uint8Array-public sort(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的Uint8Array。 |

## sort

```TypeScript
public sort(compareFn?: (a: double, b: double) => int): this
```

原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public sort(compareFn?: (a: double, b: double) => int): this--><!--Device-Uint8Array-public sort(compareFn?: (a: double, b: double) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: double, b: double) =&gt; int | 否 | 用于确定元素顺序的比较函数。 当第一个参数小于第二个参数时compareFn返回负值， 相等时返回0，否则返回正值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的Uint8Array。 |

## subarray

```TypeScript
public subarray(begin?: int, end?: int): Uint8Array
```

创建与当前数组共享同一底层Buffer的Uint8Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public subarray(begin?: int, end?: int): Uint8Array--><!--Device-Uint8Array-public subarray(begin?: int, end?: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 否 | 起始索引（包含）。 |
| end | int | 否 | 结束索引（不包含）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 与当前数组共享同一底层Buffer的新Uint8Array。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Uint8Array-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
public toReversed(): Uint8Array
```

创建反转后的副本。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toReversed(): Uint8Array--><!--Device-Uint8Array-public toReversed(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 反转后的副本。 |

## toSorted

```TypeScript
public toSorted(): Uint8Array
```

返回元素按升序排序后的新Uint8Array。 原数组不会被修改。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toSorted(): Uint8Array--><!--Device-Uint8Array-public toSorted(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 排序后的新Uint8Array。 |

## toString

```TypeScript
public toString(): string
```

返回该Uint8Array的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public toString(): string--><!--Device-Uint8Array-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该Uint8Array的字符串表示。 |

## valueOf

```TypeScript
public valueOf(): Uint8Array
```

返回Uint8Array的原始值，即该数组对象本身。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public valueOf(): Uint8Array--><!--Device-Uint8Array-public valueOf(): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 该Uint8Array对象本身。 |

## values

```TypeScript
public values(): IterableIterator<double>
```

返回数组值的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public values(): IterableIterator<double>--><!--Device-Uint8Array-public values(): IterableIterator<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;double&gt; | 按顺序产出每个元素的迭代器。 |

## with

```TypeScript
public with(index: int, value: int): Uint8Array
```

创建将index处的值替换后的副本。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public with(index: int, value: int): Uint8Array--><!--Device-Uint8Array-public with(index: int, value: int): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| value | int | 是 | 待设置的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 将index处元素替换后的新Uint8Array。 |

## with

```TypeScript
public with(index: int, value: double): Uint8Array
```

创建将index处的值替换后的副本。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public with(index: int, value: double): Uint8Array--><!--Device-Uint8Array-public with(index: int, value: double): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待修改的索引。 <br>取值约束：应为整数。 |
| value | double | 是 | 待设置的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 将index处的值替换后的Uint8Array。 |

## buffer

```TypeScript
public readonly buffer: ArrayBuffer
```

底层Buffer。

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public readonly buffer: ArrayBuffer--><!--Device-Uint8Array-public readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTES_PER_ELEMENT

```TypeScript
public static readonly BYTES_PER_ELEMENT: int = 1
```

每个元素占用的字节数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public static readonly BYTES_PER_ELEMENT: int = 1--><!--Device-Uint8Array-public static readonly BYTES_PER_ELEMENT: int = 1-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
public readonly name: string = 'Uint8Array'
```

字符串\"Uint8Array\"。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Uint8Array-public readonly name: string = 'Uint8Array'--><!--Device-Uint8Array-public readonly name: string = 'Uint8Array'-End-->

**系统能力：** SystemCapability.Utils.Lang

