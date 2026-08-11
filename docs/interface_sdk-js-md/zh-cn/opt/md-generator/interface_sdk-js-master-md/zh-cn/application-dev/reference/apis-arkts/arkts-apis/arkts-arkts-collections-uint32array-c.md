# Uint32Array

一种线性数据结构，底层基于[ArkTS ArrayBuffer](arkts-collections.md)实现。

> **说明：**
> 
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> **装饰器**：\@Sendable

**起始版本：** 12

**装饰器类型：** @Sendable

<!--Device-collections-class Uint32Array--><!--Device-collections-class Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

返回一个迭代器，迭代器的每一项都是一个数字。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-[Symbol.iterator](): IterableIterator<number>--><!--Device-Uint32Array-[Symbol.iterator](): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## at

```TypeScript
at(index: number): number | undefined
```

返回指定下标的元素，如果不存在，则返回**undefined**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-at(index: number): number | undefined--><!--Device-Uint32Array-at(index: number): number | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## constructor

```TypeScript
constructor()
```

构造函数，用于创建一个空的ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-constructor()--><!--Device-Uint32Array-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(length: number)
```

构造函数，用于创建一个指定长度的ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-constructor(length: number)--><!--Device-Uint32Array-constructor(length: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [length](#length) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(elements: Iterable<number>)
```

构造函数，以Iterable创建一个ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-constructor(elements: Iterable<number>)--><!--Device-Uint32Array-constructor(elements: Iterable<number>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elements | Iterable&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(array: ArrayLike<number> | ArrayBuffer)
```

构造函数，以ArrayLike或ArkTS ArrayBuffer创建一个ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-constructor(array: ArrayLike<number> | ArrayBuffer)--><!--Device-Uint32Array-constructor(array: ArrayLike<number> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | ArrayLike&lt;number&gt; \| ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)
```

构造函数，以ArrayBuffer创建一个ArkTS Uint32Array对象。Uint32Array与传入的ArrayBuffer共享同一份底层数据。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)--><!--Device-Uint32Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [buffer](#buffer) | ArrayBuffer | 是 |
| [byteOffset](#byteoffset) | number | 否 |
| [length](#length) | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Uint32Array
```

将ArkTS Uint32Array指定范围内的元素依次拷贝到目标位置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-copyWithin(target: number, start: number, end?: number): Uint32Array--><!--Device-Uint32Array-copyWithin(target: number, start: number, end?: number): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | number | 是 |
| start | number | 是 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint32Array中每个元素的键值对。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-entries(): IterableIterator<[number, number]>--><!--Device-Uint32Array-entries(): IterableIterator<[number, number]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;[number, number]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## every

```TypeScript
every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean
```

测试ArkTS Uint32Array中的所有元素是否满足指定条件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean--><!--Device-Uint32Array-every(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): Uint32Array
```

使用特定值填充ArkTS Uint32Array指定范围的全部元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-fill(value: number, start?: number, end?: number): Uint32Array--><!--Device-Uint32Array-fill(value: number, start?: number, end?: number): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## filter

```TypeScript
filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array
```

返回一个新的ArkTS Uint32Array对象，其包含满足指定条件的所有元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array--><!--Device-Uint32Array-filter(predicate: TypedArrayPredicateFn<number, Uint32Array>): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## find

```TypeScript
find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined
```

返回ArkTS Uint32Array中第一个满足指定条件的元素的值，如果所有元素都不满足，则返回**undefined**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined--><!--Device-Uint32Array-find(predicate: TypedArrayPredicateFn<number, Uint32Array>): number | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## findIndex

```TypeScript
findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number
```

返回ArkTS Uint32Array中第一个满足指定条件的元素索引，如果所有元素都不满足，则返回**-1**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number--><!--Device-Uint32Array-findIndex(predicate: TypedArrayPredicateFn<number, Uint32Array>): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## forEach

```TypeScript
forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void
```

对ArkTS Uint32Array中的每个元素执行提供的回调函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void--><!--Device-Uint32Array-forEach(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md)&lt;number, Uint32Array&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## from

```TypeScript
static from(arrayLike: ArrayLike<number>): Uint32Array
```

从一个ArrayLike中创建一个ArkTS Uint32Array对象，通过映射函数对每个元素进行转换。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-static from(arrayLike: ArrayLike<number>): Uint32Array--><!--Device-Uint32Array-static from(arrayLike: ArrayLike<number>): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array
```

从一个ArrayLike中创建一个ArkTS Uint32Array对象，通过映射函数对每个元素进行转换。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array--><!--Device-Uint32Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike&lt;T&gt; | 是 |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;T, number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

## from

```TypeScript
static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array
```

从一个可迭代对象中创建一个ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array--><!--Device-Uint32Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | Iterable&lt;number&gt; | 是 |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;number, number&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

## includes

```TypeScript
includes(searchElement: number, fromIndex?: number): boolean
```

判断ArkTS Uint32Array是否包含特定元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-includes(searchElement: number, fromIndex?: number): boolean--><!--Device-Uint32Array-includes(searchElement: number, fromIndex?: number): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | number | 是 |
| fromIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

返回在ArkTS Uint32Array中给定元素的第一个索引，如果不存在，则返回**-1**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint32Array-indexOf(searchElement: number, fromIndex?: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | number | 是 |
| fromIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## join

```TypeScript
join(separator?: string): string
```

将ArkTS Uint32Array的所有元素拼接成一个字符串，元素之间使用指定的分隔符分隔。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-join(separator?: string): string--><!--Device-Uint32Array-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| separator | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## keys

```TypeScript
keys(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint32Array中每个元素的键（下标）。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-keys(): IterableIterator<number>--><!--Device-Uint32Array-keys(): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

返回ArkTS Uint32Array实例中最后一次出现给定元素的索引，如果不存在，则返回**-1**。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint32Array-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | number | 是 |
| fromIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## map

```TypeScript
map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array
```

对ArkTS Uint32Array中的每个元素应用指定的回调函数，并使用结果创建一个新的ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array--><!--Device-Uint32Array-map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md)&lt;number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## of

```TypeScript
static of(...items: number[]): Uint32Array
```

通过可变数量的参数创建一个新的ArkTS Uint32Array对象。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-static of(...items: number[]): Uint32Array--><!--Device-Uint32Array-static of(...items: number[]): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number
```

对每个元素执行归约函数，并返回最终的归约结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number--><!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number
```

对ArkTS Uint32Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number--><!--Device-Uint32Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>, initialValue: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint32Array&gt; | 是 |
| initialValue | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reduce

```TypeScript
reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U
```

对ArkTS Uint32Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U--><!--Device-Uint32Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint32Array&gt; | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reduceRight

```TypeScript
reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U
```

反向遍历ArkTS Uint32Array，对ArkTS Uint32Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U--><!--Device-Uint32Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint32Array&gt; | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reduceRight

```TypeScript
reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number
```

反向遍历ArkTS Uint32Array，对每个元素执行归约函数，并返回最终的归约结果。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number--><!--Device-Uint32Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reverse

```TypeScript
reverse(): Uint32Array
```

原地反转ArkTS Uint32Array的元素顺序（修改原数组），并返回修改后的原数组引用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-reverse(): Uint32Array--><!--Device-Uint32Array-reverse(): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

将传入的ArrayLike元素依次写入到指定的起始位置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint32Array-set(array: ArrayLike<number>, offset?: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | ArrayLike&lt;number&gt; | 是 |
| offset | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## slice

```TypeScript
slice(start?: number, end?: number): Uint32Array
```

返回一个新的ArkTS Uint32Array对象，其包含原ArkTS Uint32Array指定范围的内容。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-slice(start?: number, end?: number): Uint32Array--><!--Device-Uint32Array-slice(start?: number, end?: number): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## some

```TypeScript
some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean
```

测试ArkTS Uint32Array中是否存在元素满足指定条件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean--><!--Device-Uint32Array-some(predicate: TypedArrayPredicateFn<number, Uint32Array>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint32Array&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## sort

```TypeScript
sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array
```

原地对ArkTS Uint32Array进行排序（修改原数组），并返回排序后的原数组引用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array--><!--Device-Uint32Array-sort(compareFn?: TypedArrayCompareFn<number>): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md)&lt;number&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint32Array
```

从指定的位置截取数组，返回一个新的、基于相同ArkTS ArrayBuffer的ArkTS Uint32Array对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-subarray(begin?: number, end?: number): Uint32Array--><!--Device-Uint32Array-subarray(begin?: number, end?: number): Uint32Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Uint32Array |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

根据当前应用的系统地区获取符合当前文化习惯的数字表示形式，让每个元素调用自己的**toLocaleString**方法把数字转换为字符串，然后使用逗号（,）将每个元素的结果字符串按照顺序拼接成字符串。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-toLocaleString(): string--><!--Device-Uint32Array-toLocaleString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## toString

```TypeScript
toString(): string
```

将ArkTS Uint32Array转换为字符串。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-toString(): string--><!--Device-Uint32Array-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## values

```TypeScript
values(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint32Array中每个元素的值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-values(): IterableIterator<number>--><!--Device-Uint32Array-values(): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## BYTES_PER_ELEMENT

```TypeScript
static readonly BYTES_PER_ELEMENT: number
```

ArkTS Uint32Array中每个元素所占的字节数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-static readonly BYTES_PER_ELEMENT: number--><!--Device-Uint32Array-static readonly BYTES_PER_ELEMENT: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## [index: number]

```TypeScript
[index: number]: number
```

返回ArkTS Uint32Array指定索引位置的元素。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-[index: number]: number--><!--Device-Uint32Array-[index: number]: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

ArkTS Uint32Array底层使用的ArrayBuffer对象。

**类型：** ArrayBuffer

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-readonly buffer: ArrayBuffer--><!--Device-Uint32Array-readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: number
```

ArkTS Uint32Array所占的字节数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-readonly byteLength: number--><!--Device-Uint32Array-readonly byteLength: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: number
```

ArkTS Uint32Array距离其ArrayBuffer起始位置的字节偏移。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-readonly byteOffset: number--><!--Device-Uint32Array-readonly byteOffset: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

ArkTS Uint32Array元素个数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint32Array-readonly length: number--><!--Device-Uint32Array-readonly length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
