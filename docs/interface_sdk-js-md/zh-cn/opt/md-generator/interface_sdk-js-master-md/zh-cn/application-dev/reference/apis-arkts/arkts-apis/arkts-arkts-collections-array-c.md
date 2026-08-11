# Array

一种线性数据结构，底层基于数组实现，可以在ArkTS上并发实例间传递。

当需要在ArkTS上并发实例间传递Array时，可以通过传递Array引用提升传递性能。

> **说明：**
> 
> - 本模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> 本节使用以下标识来表示泛型的使用：

- T：Type，支持  
[Sendable支持的数据类型](../../../arkts-utils/arkts-sendable.md#sendable支持的数据类型)。  
**装饰器**：\@Sendable

**继承/实现关系：** Array implements [ConcatArray<T>](ConcatArray<T>)

**起始版本：** 12

**装饰器类型：** @Sendable

<!--Device-collections-class Array<T> implements ConcatArray<T>--><!--Device-collections-class Array<T> implements ConcatArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

获取一个迭代器，迭代器的每一项都是一个 JavaScript 对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-[Symbol.iterator](): IterableIterator<T>--><!--Device-Array-[Symbol.iterator](): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## at

```TypeScript
at(index: number): T | undefined
```

返回ArkTS Array中指定索引位置的元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-at(index: number): T | undefined--><!--Device-Array-at(index: number): T | undefined-End-->

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
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## concat

```TypeScript
concat(...items: ConcatArray<T>[]): Array<T>
```

将ArkTS Array与一个或多个数组拼接。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-concat(...items: ConcatArray<T>[]): Array<T>--><!--Device-Array-concat(...items: ConcatArray<T>[]): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | [ConcatArray](arkts-arkts-collections-concatarray-i.md)&lt;T&gt;[] | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## constructor

```TypeScript
constructor()
```

创建一个空的ArkTS Array的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-constructor()--><!--Device-Array-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(first: T, ...left: T[])
```

ArkTS Array的构造函数，通过开发者提供的元素进行初始化。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-constructor(first: T, ...left: T[])--><!--Device-Array-constructor(first: T, ...left: T[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| first | T | 是 |
| left | T[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(...items: T[])
```

ArkTS Array的构造函数，通过开发者提供的元素进行初始化。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-constructor(...items: T[])--><!--Device-Array-constructor(...items: T[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Array<T>
```

从ArkTS Array指定范围内的元素依次拷贝到目标位置。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-copyWithin(target: number, start: number, end?: number): Array<T>--><!--Device-Array-copyWithin(target: number, start: number, end?: number): Array<T>-End-->

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
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## create

```TypeScript
static create<T>(arrayLength: number, initialValue: T): Array<T>
```

生成一个固定长度的ArkTS Array，其中每个元素的初始值为给定的初始值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static create<T>(arrayLength: number, initialValue: T): Array<T>--><!--Device-Array-static create<T>(arrayLength: number, initialValue: T): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLength | number | 是 |
| initialValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## entries

```TypeScript
entries(): IterableIterator<[number, T]>
```

返回一个迭代器对象，该对象包含ArkTS Array中每个元素的键值对。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-entries(): IterableIterator<[number, T]>--><!--Device-Array-entries(): IterableIterator<[number, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;[number, T]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## every

```TypeScript
every(predicate: ArrayPredicateFn<T, Array<T>>): boolean
```

测试ArkTS Array中的所有元素是否满足指定条件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-every(predicate: ArrayPredicateFn<T, Array<T>>): boolean--><!--Device-Array-every(predicate: ArrayPredicateFn<T, Array<T>>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [ArrayPredicateFn](arkts-arkts-collections-arraypredicatefn-t.md)&lt;T, Array&lt;T&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## extendTo

```TypeScript
extendTo(arrayLength: number, initialValue: T): void
```

使用指定初始值填充新增元素，使Array扩展到指定长度。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-extendTo(arrayLength: number, initialValue: T): void--><!--Device-Array-extendTo(arrayLength: number, initialValue: T): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLength | number | 是 |
| initialValue | T | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## fill

```TypeScript
fill(value: T, start?: number, end?: number): Array<T>
```

使用指定的值填充ArkTS Array中指定范围的所有元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-fill(value: T, start?: number, end?: number): Array<T>--><!--Device-Array-fill(value: T, start?: number, end?: number): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## filter

```TypeScript
filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T>
```

返回一个新Array，其中包含通过指定回调函数测试的所有元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T>--><!--Device-Array-filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | (value: T, index: number, array: Array&lt;T&gt;) =&gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## find

```TypeScript
find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined
```

返回通过回调函数测试的第一个元素的值。如果所有元素都不满足，则返回**undefined**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined--><!--Device-Array-find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | (value: T, index: number, obj: Array&lt;T&gt;) =&gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number
```

返回通过回调函数测试的第一个元素的索引，如果所有元素都不满足，则返回**-1**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number--><!--Device-Array-findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | (value: T, index: number, obj: Array&lt;T&gt;) =&gt; boolean | 是 |

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
forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void
```

对ArkTS Array中的每个元素执行提供的回调函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void--><!--Device-Array-forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index: number, array: Array&lt;T&gt;) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>): Array<T>
```

从一个实现了ArrayLike接口的对象创建一个新的ArkTS Array。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static from<T>(arrayLike: ArrayLike<T>): Array<T>--><!--Device-Array-static from<T>(arrayLike: ArrayLike<T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## from

```TypeScript
static from<T>(iterable: Iterable<T>): Array<T>
```

从一个实现了Iterable接口的对象创建一个新的ArkTS Array。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static from<T>(iterable: Iterable<T>): Array<T>--><!--Device-Array-static from<T>(iterable: Iterable<T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iterable | Iterable&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>
```

从一个实现了ArrayLike接口的对象创建一个新的ArkTS Array，并使用自定义函数处理每个数组元素。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>--><!--Device-Array-static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike&lt;T&gt; \| Iterable&lt;T&gt; | 是 |
| mapFn | [ArrayFromMapFn](arkts-arkts-collections-arrayfrommapfn-t.md)&lt;T, T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

## from

```TypeScript
static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>
```

从一个实现了ArrayLike接口的对象创建一个新的ArkTS Array，并使用自定义函数处理每个数组元素。ArrayLike接口对象的元素类型可以和数组元素的类型不一样。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>--><!--Device-Array-static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike&lt;U&gt; \| Iterable&lt;U&gt; | 是 |
| mapFn | [ArrayFromMapFn](arkts-arkts-collections-arrayfrommapfn-t.md)&lt;U, T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: number): boolean
```

判断ArkTS Array是否包含指定的元素，并返回一个布尔值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-includes(searchElement: T, fromIndex?: number): boolean--><!--Device-Array-includes(searchElement: T, fromIndex?: number): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | T | 是 |
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
indexOf(searchElement: T, fromIndex?: number): number
```

返回在ArkTS Array中搜索元素首次出现的索引，如果不存在则返回**-1**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-indexOf(searchElement: T, fromIndex?: number): number--><!--Device-Array-indexOf(searchElement: T, fromIndex?: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | T | 是 |
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

## isArray

```TypeScript
static isArray(value: Object | undefined | null): boolean
```

检查传入的参数是否是一个ArkTS Array。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static isArray(value: Object | undefined | null): boolean--><!--Device-Array-static isArray(value: Object | undefined | null): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object \| undefined \| null | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## join

```TypeScript
join(separator?: string): string
```

将ArkTS Array的所有元素连接成一个字符串，元素之间可以用指定的分隔符分隔。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-join(separator?: string): string--><!--Device-Array-join(separator?: string): string-End-->

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

返回一个迭代器对象，该对象包含ArkTS Array中每个元素的索引。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-keys(): IterableIterator<number>--><!--Device-Array-keys(): IterableIterator<number>-End-->

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
lastIndexOf(searchElement: T, fromIndex?: number): number
```

返回ArkTS Array实例中最后一次出现指定值的索引。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-lastIndexOf(searchElement: T, fromIndex?: number): number--><!--Device-Array-lastIndexOf(searchElement: T, fromIndex?: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | T | 是 |
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
map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U>
```

对ArkTS Array中的每个元素执行提供的回调函数，并返回一个新的Array，该Array包含回调函数的结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U>--><!--Device-Array-map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: T, index: number, array: Array&lt;T&gt;) =&gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;U&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## of

```TypeScript
static of<T>(...items: T[]): Array<T>
```

通过可变数量的参数创建一个新的ArkTS Array。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-static of<T>(...items: T[]): Array<T>--><!--Device-Array-static of<T>(...items: T[]): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

## pop

```TypeScript
pop(): T | undefined
```

从ArkTS Array中移除并返回最后一个元素。如果Array为空，则返回**undefined**，且Array不发生变化。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-pop(): T | undefined--><!--Device-Array-pop(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## push

```TypeScript
push(...items: T[]): number
```

在ArkTS Array的末尾添加元素，并返回新的Array长度。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-push(...items: T[]): number--><!--Device-Array-push(...items: T[]): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

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
reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T
```

对ArkTS Array中的每个元素执行回调函数，将上一次的返回值作为累加值，并返回最终的结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T--><!--Device-Array-reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (previousValue: T, currentValue: T, currentIndex: number, array: Array&lt;T&gt;) =&gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reduce

```TypeScript
reduce<U>(
      callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U,
      initialValue: U
    ): U
```

与前一个API类似，此API接受一个初始值作为第二个参数，用于在Array遍历开始前初始化累加器。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-reduce<U>(      callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U,      initialValue: U    ): U--><!--Device-Array-reduce<U>(      callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U,      initialValue: U    ): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (previousValue: U, currentValue: T, currentIndex: number, array: Array&lt;T&gt;) =&gt; U | 是 |
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
reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U
```

此API与  
[reduceRight](arkts-arkts-collections-array-c.md#reduceright)方法类似，但它接受一个初始值作为第二个参数，用于在Array从右到左顺序遍历开始前初始化累加器。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U--><!--Device-Array-reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [ArrayReduceCallback](arkts-arkts-collections-arrayreducecallback-t.md)&lt;U, T, Array&lt;T&gt;&gt; | 是 |
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
reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T
```

对ArkTS Array中的每个元素按照从右到左顺序执行回调函数，将其结果作为累加值，并返回最终的值。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T--><!--Device-Array-reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [ArrayReduceCallback](arkts-arkts-collections-arrayreducecallback-t.md)&lt;T, T, Array&lt;T&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## reverse

```TypeScript
reverse(): Array<T>
```

反转ArkTS Array数组中的元素，并返回同一数组的引用。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-reverse(): Array<T>--><!--Device-Array-reverse(): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## shift

```TypeScript
shift(): T | undefined
```

从ArkTS Array中移除并返回第一个元素。如果Array为空，则返回**undefined**，且Array不发生变化。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-shift(): T | undefined--><!--Device-Array-shift(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## shrinkTo

```TypeScript
shrinkTo(arrayLength: number): void
```

使ArkTS Array收缩到指定长度。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-shrinkTo(arrayLength: number): void--><!--Device-Array-shrinkTo(arrayLength: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLength | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## slice

```TypeScript
slice(start?: number, end?: number): Array<T>
```

选取ArkTS Array中一段范围内的元素创建新数组。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-slice(start?: number, end?: number): Array<T>--><!--Device-Array-slice(start?: number, end?: number): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## some

```TypeScript
some(predicate: ArrayPredicateFn<T, Array<T>>): boolean
```

测试ArkTS Array是否存在满足指定条件的元素。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-some(predicate: ArrayPredicateFn<T, Array<T>>): boolean--><!--Device-Array-some(predicate: ArrayPredicateFn<T, Array<T>>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicate | [ArrayPredicateFn](arkts-arkts-collections-arraypredicatefn-t.md)&lt;T, Array&lt;T&gt;&gt; | 是 |

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
sort(compareFn?: (a: T, b: T) => number): Array<T>
```

对ArkTS Array进行排序，并返回排序后的Array。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-sort(compareFn?: (a: T, b: T) => number): Array<T>--><!--Device-Array-sort(compareFn?: (a: T, b: T) => number): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## splice

```TypeScript
splice(start: number): Array<T>
```

删除Array中指定位置(start)以及之后的所有元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-splice(start: number): Array<T>--><!--Device-Array-splice(start: number): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## splice

```TypeScript
splice(start: number, deleteCount: number, ...items: T[]): Array<T>
```

删除Array中指定位置的元素，并在同一位置插入新元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-splice(start: number, deleteCount: number, ...items: T[]): Array<T>--><!--Device-Array-splice(start: number, deleteCount: number, ...items: T[]): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| deleteCount | number | 是 |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

根据当前应用所在的系统地区获取符合当前文化习惯的字符串表示形式。让每个元素通过自身的  
**toLocaleString**方法转换为字符串，然后使用逗号（,）将这些字符串按顺序拼接。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-toLocaleString(): string--><!--Device-Array-toLocaleString(): string-End-->

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

将ArkTS Array转换为字符串。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Array-toString(): string--><!--Device-Array-toString(): string-End-->

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

## unshift

```TypeScript
unshift(...items: T[]): number
```

在ArkTS Array的首端插入元素，并返回新的Array长度。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-unshift(...items: T[]): number--><!--Device-Array-unshift(...items: T[]): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## values

```TypeScript
values(): IterableIterator<T>
```

返回一个迭代器对象，该对象包含ArkTS Array中每个元素的值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-values(): IterableIterator<T>--><!--Device-Array-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator&lt;T&gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## [index: number]

```TypeScript
[index: number]: T
```

返回Array中指定索引位置的元素。

**类型：** T

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-[index: number]: T--><!--Device-Array-[index: number]: T-End-->

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

Array的元素个数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Array-readonly length: number--><!--Device-Array-readonly length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
