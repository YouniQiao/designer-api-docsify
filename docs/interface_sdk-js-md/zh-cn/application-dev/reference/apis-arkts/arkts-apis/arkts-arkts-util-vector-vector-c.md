# Vector

Vector是一种线性数据结构，底层基于数组实现，解决了需要动态扩容、高效随机访问的数据存储问题。 当Vector的内存用尽时，会自动分配更大的连续内存区，将原先的元素复制到新的内存区，并释放旧的内存区。 使用Vector能够高效快速地访问元素，其2倍扩容策略减少了频繁的内存重分配，同时丰富的操作接口提供了更灵活的数据管理能力。 Vector和[ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)相似，都是基于数组实现，但Vector提供了更多操作数组的接口。 它们都可以动态调整容量，但Vector每次扩容增加1倍，ArrayList只扩容0.5倍。 **推荐使用场景：** 当需要频繁按索引随机访问元素且数据量较大时，推荐使用Vector来存取数据。 文档中使用了泛型，涉及以下泛型标记符：  
- T：Type，类

> **说明：**&gt;
> - 此模块提供的接口从API version 9开始废弃。建议使用
> [@ohos.util.ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { Vector } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，用于遍历Vector中的元素。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

## add

```TypeScript
add(element: T): boolean
```

在Vector中尾部插入元素，插入成功后Vector的长度增加1。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## clear

```TypeScript
clear(): void
```

清除Vector中的所有元素，并将length置为0。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## clone

```TypeScript
clone(): Vector<T>
```

克隆一个实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Vector](arkts-arkts-util-vector-vector-c.md)&lt;T&gt; |

## constructor

```TypeScript
constructor()
```

Vector的构造函数。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

将Vector实例转换为数组。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## copyToArray

```TypeScript
copyToArray(array: Array<T>): void
```

将Vector中的元素复制到指定数组中，覆盖数组中相同下标的元素。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | Array & lt;T & gt; | 是 |

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, vector?: Vector<T>) => void, thisArg?: Object): void
```

通过回调函数来遍历Vector实例对象上的元素以及元素对应的下标。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, vector?: Vector & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

## get

```TypeScript
get(index: number): T
```

根据下标值获取Vector实例中的元素，index取值范围为[0, length-1]。Vector为空或下标越界时返回undefined。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## getCapacity

```TypeScript
getCapacity(): number
```

获取Vector实例的容量大小。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getFirstElement

```TypeScript
getFirstElement(): T
```

获取Vector实例中的第一个元素。Vector为空时返回undefined。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

## getIndexFrom

```TypeScript
getIndexFrom(element: T, index: number): number
```

从指定索引向高索引方向搜索，返回该元素的下标索引。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getIndexOf

```TypeScript
getIndexOf(element: T): number
```

获取指定元素第一次出现的下标值，如果未找到则返回-1。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getLastElement

```TypeScript
getLastElement(): T
```

获取Vector实例中的最后一个元素。Vector为空时返回undefined。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

## getLastIndexFrom

```TypeScript
getLastIndexFrom(element: T, index: number): number
```

从指定索引向低索引方向搜索，返回该元素的下标索引。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getLastIndexOf

```TypeScript
getLastIndexOf(element: T): number
```

获取指定元素最后一次出现的下标值，如果未找到则返回-1。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## has

```TypeScript
has(element: T): boolean
```

判断此Vector中是否含有该指定元素。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## increaseCapacityTo

```TypeScript
increaseCapacityTo(newCapacity: number): void
```

如果传入的新容量大于或等于当前Vector实例的元素个数，将容量变更为新容量；如果传入的新容量小于当前Vector实例的元素个数，不做变更。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newCapacity | number | 是 |

## insert

```TypeScript
insert(element: T, index: number): void
```

在长度范围内的指定位置插入元素，并将该位置后续元素向右移动。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |
| index | number | 是 |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断Vector是否为空。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## remove

```TypeScript
remove(element: T): boolean
```

删除指定元素第一次出现的元素。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## removeByIndex

```TypeScript
removeByIndex(index: number): T
```

根据下标值找到对应元素并删除，同时将该位置后续元素向左移动，返回被删除的元素。index取值范围为[0, length-1]。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## removeByRange

```TypeScript
removeByRange(fromIndex: number, toIndex: number): void
```

从一段范围内删除元素，包括起始值但不包括终止值，删除后后续元素向左移动，Vector的长度相应减少。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, vector?: Vector<T>) => T, thisArg?: Object): void
```

通过回调函数操作Vector中的元素，用回调函数返回的元素替换原元素。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, vector?: Vector & lt;T & gt;) = & gt; T | 是 |
| thisArg | Object | 否 |

## set

```TypeScript
set(index: number, element: T): T
```

将此Vector中指定位置的元素替换为指定元素。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## setLength

```TypeScript
setLength(newSize: number): void
```

设置Vector实例的元素个数。若newSize大于当前元素个数则进行扩容，若newSize小于当前元素个数则截断删除超出部分的元素。newSize=0时清空所有元素，length置为0。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newSize | number | 是 |

## sort

```TypeScript
sort(comparator?: (firstValue: T, secondValue: T) => number): void
```

对Vector中的元素进行一个排序操作。排序后元素的索引位置会发生改变，排序前通过getIndexOf、getLastIndexOf等方法获取的索引值将不再有效，需重新查询索引。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | (firstValue: T, secondValue: T) = & gt; number | 否 |

## subVector

```TypeScript
subVector(fromIndex: number, toIndex: number): Vector<T>
```

获取Vector实例中指定范围内的元素，包括起始位置但不包括结束位置的元素，作为一个新的Vector实例返回。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Vector](arkts-arkts-util-vector-vector-c.md)&lt;T&gt; |

## toString

```TypeScript
toString(): string
```

用逗号（,）将Vector实例中的元素拼接成字符串。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## trimToCurrentLength

```TypeScript
trimToCurrentLength(): void
```

把容量限制为当前的length大小。适用于在完成元素添加后释放多余的内存空间，优化内存使用。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Vector的元素个数。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.Utils.Lang
