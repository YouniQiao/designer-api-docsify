# BitVector

一种线性数据结构，底层基于数组实现。BitVector 中存储的元素为 bit 值，能够存储和处理 bit 级别的操作。 > **NOTE：**> > - 此模块仅支持在 ArkTS 文件（文件后缀为 .ets）中导入使用。 > **装饰器**：\@Sendable

**起始版本：** 12

**废弃版本：** -1

<!--Device-collections-class BitVector--><!--Device-collections-class BitVector-End-->

**系统能力：** SystemCapability.Utils.Lang

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

返回一个迭代器，用于迭代 BitVector 中的元素。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-[Symbol.iterator](): IterableIterator<number>--><!--Device-BitVector-[Symbol.iterator](): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## constructor

```TypeScript
constructor(length: number)
```

BitVector 的构造函数。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-constructor(length: number)--><!--Device-BitVector-constructor(length: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [length](#length) | number | 是 |

## flipBitByIndex

```TypeScript
flipBitByIndex(index: number): void
```

翻转 BitVector 指定索引处的 bit 值，0 翻转为 1，1 翻转为 0。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-flipBitByIndex(index: number): void--><!--Device-BitVector-flipBitByIndex(index: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## flipBitsByRange

```TypeScript
flipBitsByRange(fromIndex: number, toIndex: number): void
```

翻转 BitVector 指定范围内的 bit 值，0 翻转为 1，1 翻转为 0。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-flipBitsByRange(fromIndex: number, toIndex: number): void--><!--Device-BitVector-flipBitsByRange(fromIndex: number, toIndex: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## getBitCountByRange

```TypeScript
getBitCountByRange(element: number, fromIndex: number, toIndex: number): number
```

统计指定范围内获取指定 bit 值的数量。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-getBitCountByRange(element: number, fromIndex: number, toIndex: number): number--><!--Device-BitVector-getBitCountByRange(element: number, fromIndex: number, toIndex: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## getBitsByRange

```TypeScript
getBitsByRange(fromIndex: number, toIndex: number): BitVector
```

获取指定范围内的 bit 值。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-getBitsByRange(fromIndex: number, toIndex: number): BitVector--><!--Device-BitVector-getBitsByRange(fromIndex: number, toIndex: number): BitVector-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BitVector](arkts-arkts-collections-bitvector-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## getIndexOf

```TypeScript
getIndexOf(element: number, fromIndex: number, toIndex: number): number
```

返回指定 bit 值首次出现时的索引值，查找失败返回 **-1**。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-getIndexOf(element: number, fromIndex: number, toIndex: number): number--><!--Device-BitVector-getIndexOf(element: number, fromIndex: number, toIndex: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## getLastIndexOf

```TypeScript
getLastIndexOf(element: number, fromIndex: number, toIndex: number): number
```

返回指定 bit 值最后一次出现时的索引值，查找失败返回 **-1**。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-getLastIndexOf(element: number, fromIndex: number, toIndex: number): number--><!--Device-BitVector-getLastIndexOf(element: number, fromIndex: number, toIndex: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## has

```TypeScript
has(element: number, fromIndex: number, toIndex: number): boolean
```

判断范围内是否包含特定 bit 值。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-has(element: number, fromIndex: number, toIndex: number): boolean--><!--Device-BitVector-has(element: number, fromIndex: number, toIndex: number): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## pop

```TypeScript
pop(): number
```

弹出 BitVector 尾部的元素。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-pop(): number--><!--Device-BitVector-pop(): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## push

```TypeScript
push(element: number): boolean
```

在 BitVector 尾部插入元素。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-push(element: number): boolean--><!--Device-BitVector-push(element: number): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## resize

```TypeScript
resize(size: number): void
```

改变 BitVector 的长度。 如果 **size** 大于原 BitVector 的长度，则扩充原 BitVector 的长度，多出部分的元素设置为 0。 如果 **size** 小于等于原 BitVector 的长度，则将原 BitVector 按 size 长度大小裁剪。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-resize(size: number): void--><!--Device-BitVector-resize(size: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## setAllBits

```TypeScript
setAllBits(element: number): void
```

将 BitVector 中所有元素均设为特定 bit 值。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-setAllBits(element: number): void--><!--Device-BitVector-setAllBits(element: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## setBitsByRange

```TypeScript
setBitsByRange(element: number, fromIndex: number, toIndex: number): void
```

将 BitVector 中指定范围的元素均设为特定 bit 值。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-setBitsByRange(element: number, fromIndex: number, toIndex: number): void--><!--Device-BitVector-setBitsByRange(element: number, fromIndex: number, toIndex: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | number | 是 |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## values

```TypeScript
values(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含 BitVector 中每个元素的值。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-values(): IterableIterator<number>--><!--Device-BitVector-values(): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## length

```TypeScript
readonly length: number
```

BitVector 的元素个数。

**类型：** number

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BitVector-readonly length: number--><!--Device-BitVector-readonly length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
