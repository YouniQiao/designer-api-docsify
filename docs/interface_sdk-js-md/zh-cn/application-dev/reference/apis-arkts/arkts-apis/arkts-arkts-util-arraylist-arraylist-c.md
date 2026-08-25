# ArrayList

ArrayList是一种线性数据结构，底层基于数组实现，解决了固定大小数组无法动态扩容的限制。ArrayList会根据实际需要动态调整容量，每次扩容增加50%。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { ArrayList } from 'kits/@kit.ArkTS';
import { ArrayListComparatorFn } from 'kits/@kit.ArkTS';
import { ArrayListForEachCb } from 'kits/@kit.ArkTS';
import { ArrayListReplaceCb } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器按照ArrayList中元素的顺序依次返回类型为T的元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## add

```TypeScript
add(element: T): boolean
```

在ArrayList尾部插入元素。批量添加元素时，建议先调用increaseCapacityTo方法扩充容量，避免多次自动扩容带来的性能开销。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## clear

```TypeScript
clear(): void
```

清除ArrayList中的所有元素，并把length置为0。此方法不会释放预留的容量空间，如需释放容量请调用trimToCurrentLength方法。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## clone

```TypeScript
clone(): ArrayList<T>
```

克隆一个与ArrayList相同的实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## constructor

```TypeScript
constructor()
```

ArrayList的构造函数，用于创建一个空的ArrayList实例。该构造函数需通过new关键字调用，不可作为普通函数直接调用，否则将抛出异常。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

把当前ArrayList实例转换成数组，并返回转换后的数组。此操作不会修改原ArrayList实例，对返回数组的修改也不会影响原实例。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => void, thisArg?: Object): void
```

在遍历ArrayList实例对象的过程中，对每个元素执行回调函数。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, arrlist?: ArrayList & lt;T & gt;) = & gt; void | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## getCapacity

```TypeScript
getCapacity(): number
```

返回当前实例的容量大小。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## getIndexOf

```TypeScript
getIndexOf(element: T): number
```

返回指定元素第一次出现的下标，查找失败返回-1。与getLastIndexOf的区别在于，该方法返回元素首次出现的位置，getLastIndexOf返回元素最后一次出现的位置。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## getLastIndexOf

```TypeScript
getLastIndexOf(element: T): number
```

返回指定元素最后一次出现的下标，查找失败返回-1。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## has

```TypeScript
has(element: T): boolean
```

判断此ArrayList中是否包含指定元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## increaseCapacityTo

```TypeScript
increaseCapacityTo(newCapacity: number): void
```

如果传入的新容量大于或等于ArrayList中的元素个数，将容量变更为新容量；如果传入的新容量小于ArrayList中的元素个数，则容量保持不变。当需要批量添加元素时，可预先调用此方法扩充容量，避免多次自动扩容带来的性能开销。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newCapacity | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## insert

```TypeScript
insert(element: T, index: number): void
```

在长度范围内指定位置index插入元素element。调用成功后，ArrayList的length增加1，index位置及之后的元素依次向后移动一位。如果index超出范围，则抛出异常。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |
| index | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断该ArrayList是否为空。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## remove

```TypeScript
remove(element: T): boolean
```

删除查找到的第一个指定元素。删除成功后，ArrayList的length减少1，被删除元素之后的元素依次向前移动一位。如果未找到指定元素，则不执行删除操作。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| element | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## removeByIndex

```TypeScript
removeByIndex(index: number): T
```

根据指定下标删除元素，并返回被删除的元素。删除后，ArrayList的length减少1，被删除元素之后的元素依次向前移动一位。如果index超出范围，则抛出异常。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## removeByRange

```TypeScript
removeByRange(fromIndex: number, toIndex: number): void
```

删除指定范围内的元素，即左闭右开区间[fromIndex, toIndex)。删除后，ArrayList的length减少对应的元素个数，toIndex之后的元素依次向前移动。如果fromIndex或toIndex超出范围， 则抛出异常。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => T, thisArg?: Object): void
```

遍历ArrayList中的每个元素，对每个元素执行回调函数，用回调函数返回的值替换原元素。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, arrlist?: ArrayList & lt;T & gt;) = & gt; T | 是 |
| thisArg | Object | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## sort

```TypeScript
sort(comparator?: ArrayListComparatorFn<T>): void
```

根据指定比较器所定义的顺序，对ArrayList中的元素进行排序。排序后，ArrayList的元素个数不变，元素位置按比较器定义的顺序重新排列。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | [ArrayListComparatorFn](arkts-arkts-arraylistcomparatorfn-t.md)&lt;T&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## subArrayList

```TypeScript
subArrayList(fromIndex: number, toIndex: number): ArrayList<T>
```

根据下标截取ArrayList中的一段元素，并返回这一段ArrayList实例，即左闭右开区间[fromIndex, toIndex)。如果fromIndex或toIndex超出范围，则抛出异常。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromIndex | number | 是 |
| toIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## trimToCurrentLength

```TypeScript
trimToCurrentLength(): void
```

释放ArrayList中预留的空间，把容量调整为当前的元素个数。当ArrayList的容量远大于当前元素个数时（如经过多次删除操作后），可调用此方法释放多余空间以优化内存占用。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## [index: int]

```TypeScript
[index: number]: T
```

获取指定下标对应位置的元素。如果index超出范围，则抛出异常。

**类型：** T

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

ArrayList的元素个数。

**类型：** number

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
