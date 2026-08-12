# Uint8ClampedArray

一种线性数据结构，底层基于[ArkTS ArrayBuffer](./arkts/@arkts.collections:collections)实现。

> **说明：**
> 
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> **装饰器类型**：\@Sendable

**起始版本：** 12

**装饰器类型：** @Sendable

<!--Device-collections-class Uint8ClampedArray--><!--Device-collections-class Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

返回一个迭代器，迭代器的每一项都是一个数字对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-[Symbol.iterator](): IterableIterator<number>--><!--Device-Uint8ClampedArray-[Symbol.iterator](): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |

## at

```TypeScript
at(index: number): number | undefined
```

返回指定下标的元素，如果不存在，则返回undefined。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-at(index: number): number | undefined--><!--Device-Uint8ClampedArray-at(index: number): number | undefined-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## constructor

```TypeScript
constructor()
```

构造函数，用于创建一个空ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-constructor()--><!--Device-Uint8ClampedArray-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(length: number)
```

构造函数，用于创建一个指定长度的ArkTS Uint8ClampedArray对象，所有元素初始值为0。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-constructor(length: number)--><!--Device-Uint8ClampedArray-constructor(length: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [length](#length) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(elements: Iterable<number>)
```

构造函数，以Iterable创建一个ArkTS Uint8ClampedArray对象，且ArkTS Uint8ClampedArray中的各元素都会经过钳位处理。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-constructor(elements: Iterable<number>)--><!--Device-Uint8ClampedArray-constructor(elements: Iterable<number>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Iterable & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(array: ArrayLike<number> | ArrayBuffer)
```

构造函数，以ArrayLike或ArkTS ArrayBuffer创建一个ArkTS Uint8ClampedArray对象，且ArkTS Uint8ClampedArray中的各元素都会经过钳位处理。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-constructor(array: ArrayLike<number> | ArrayBuffer)--><!--Device-Uint8ClampedArray-constructor(array: ArrayLike<number> | ArrayBuffer)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | ArrayLike & lt;number & gt; \ | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-构造函数调用异常) |

## constructor

```TypeScript
constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)
```

构造函数，以ArrayBuffer创建一个ArkTS Uint8ClampedArray对象，且ArkTS Uint8ClampedArray和ArrayBuffer共享内存。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)--><!--Device-Uint8ClampedArray-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)-End-->

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
| [10200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-构造函数调用异常) |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Uint8ClampedArray
```

从ArkTS Uint8ClampedArray指定范围内的元素依次拷贝到自身buffer内目标位置，覆盖目标范围内原有数据。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-copyWithin(target: number, start: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-copyWithin(target: number, start: number, end?: number): Uint8ClampedArray-End-->

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
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint8ClampedArray中每个元素的键值对。迭代器遍历期间不能使用会改变ArkTS Uint8ClampedArray数组内容的方法。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-entries(): IterableIterator<[number, number]>--><!--Device-Uint8ClampedArray-entries(): IterableIterator<[number, number]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[number, number] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## every

```TypeScript
every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean
```

测试ArkTS Uint8ClampedArray中的所有元素是否满足指定条件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean--><!--Device-Uint8ClampedArray-every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): Uint8ClampedArray
```

使用特定值填充ArkTS Uint8ClampedArray指定范围的全部元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-fill(value: number, start?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-fill(value: number, start?: number, end?: number): Uint8ClampedArray-End-->

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
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## filter

```TypeScript
filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray
```

返回一个新ArkTS Uint8ClampedArray，其包含满足指定条件的所有元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## find

```TypeScript
find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined
```

返回ArkTS Uint8ClampedArray中第一个满足指定条件的元素的值，如果所有元素都不满足，则返回undefined。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined--><!--Device-Uint8ClampedArray-find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## findIndex

```TypeScript
findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number
```

返回ArkTS Uint8ClampedArray中第一个满足指定条件的元素索引，如果所有元素都不满足，则返回-1。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number--><!--Device-Uint8ClampedArray-findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## forEach

```TypeScript
forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void
```

对ArkTS Uint8ClampedArray中的每个元素执行提供的回调函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void--><!--Device-Uint8ClampedArray-forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## from

```TypeScript
static from(arrayLike: ArrayLike<number>): Uint8ClampedArray
```

从一个ArrayLike中创建一个ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-static from(arrayLike: ArrayLike<number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static from(arrayLike: ArrayLike<number>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray
```

从一个ArrayLike中创建一个ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike & lt;T & gt; | 是 |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;T, number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

## from

```TypeScript
static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray
```

从一个可迭代对象中创建一个ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | Iterable & lt;number & gt; | 是 |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;number, number&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

## includes

```TypeScript
includes(searchElement: number, fromIndex?: number): boolean
```

判断ArkTS Uint8ClampedArray是否包含特定元素。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-includes(searchElement: number, fromIndex?: number): boolean--><!--Device-Uint8ClampedArray-includes(searchElement: number, fromIndex?: number): boolean-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

返回在ArkTS Uint8ClampedArray中给定元素的第一个索引，如果不存在，则返回-1。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8ClampedArray-indexOf(searchElement: number, fromIndex?: number): number-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## join

```TypeScript
join(separator?: string): string
```

将ArkTS Uint8ClampedArray的所有元素拼接成一个字符串，元素之间使用指定的分隔符分隔。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-join(separator?: string): string--><!--Device-Uint8ClampedArray-join(separator?: string): string-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## keys

```TypeScript
keys(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint8ClampedArray中每个元素的键（下标）。迭代器遍历期间不能使用会改变ArkTS Uint8ClampedArray数组内容的方法。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-keys(): IterableIterator<number>--><!--Device-Uint8ClampedArray-keys(): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

返回ArkTS Uint8ClampedArray实例中最后一次出现searchElement的索引，如果对象不包含，则为-1。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8ClampedArray-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## map

```TypeScript
map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray
```

对ArkTS Uint8ClampedArray中的每个元素应用指定的回调函数，并使用结果创建一个新的ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## of

```TypeScript
static of(...items: number[]): Uint8ClampedArray
```

通过可变数量的参数创建一个新的ArkTS Uint8ClampedArray对象，参数个数可以是0个、1个或者多个。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-static of(...items: number[]): Uint8ClampedArray--><!--Device-Uint8ClampedArray-static of(...items: number[]): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number
```

对ArkTS Uint8ClampedArray中的每个元素执行归约函数，并返回最终的归约结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number--><!--Device-Uint8ClampedArray-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## reduce

```TypeScript
reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U
```

对ArkTS Uint8ClampedArray中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U--><!--Device-Uint8ClampedArray-reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## reduceRight

```TypeScript
reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U
```

反向遍历ArkTS Uint8ClampedArray，对ArkTS Uint8ClampedArray中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U--><!--Device-Uint8ClampedArray-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## reduceRight

```TypeScript
reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number
```

反向遍历ArkTS Uint8ClampedArray，对ArkTS Uint8ClampedArray中的每个元素执行归约函数，并返回最终的归约结果。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number--><!--Device-Uint8ClampedArray-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## reverse

```TypeScript
reverse(): Uint8ClampedArray
```

反转ArkTS Uint8ClampedArray中元素的顺序，并返回反转后的ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-reverse(): Uint8ClampedArray--><!--Device-Uint8ClampedArray-reverse(): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

将传入的ArrayLike元素依次写入到指定的起始位置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint8ClampedArray-set(array: ArrayLike<number>, offset?: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | ArrayLike & lt;number & gt; | 是 |
| offset | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## slice

```TypeScript
slice(start?: number, end?: number): Uint8ClampedArray
```

返回一个新的ArkTS Uint8ClampedArray对象，其包含原ArkTS Uint8ClampedArray指定范围的内容。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-slice(start?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-slice(start?: number, end?: number): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## some

```TypeScript
some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean
```

测试ArkTS Uint8ClampedArray中是否存在元素满足指定条件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean--><!--Device-Uint8ClampedArray-some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## sort

```TypeScript
sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray
```

对ArkTS Uint8ClampedArray进行排序，并返回排序后的ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray--><!--Device-Uint8ClampedArray-sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md)&lt;number&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint8ClampedArray
```

从指定的位置截取数组，返回一个新的、基于相同ArkTS ArrayBuffer的ArkTS Uint8ClampedArray对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-subarray(begin?: number, end?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArray-subarray(begin?: number, end?: number): Uint8ClampedArray-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## toLocaleString

```TypeScript
toLocaleString(): string
```

根据当前应用的系统地区获取符合当前文化习惯的数字表示形式，让每个元素调用自己的toLocaleString方法把数字转换为字符串，然后使用逗号将每个元素的结果字符串按照顺序拼接成字符串。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-toLocaleString(): string--><!--Device-Uint8ClampedArray-toLocaleString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## toString

```TypeScript
toString(): string
```

将ArkTS Uint8ClampedArray转换为字符串。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-toString(): string--><!--Device-Uint8ClampedArray-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## values

```TypeScript
values(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint8ClampedArray中每个元素的值。迭代器遍历期间不能使用会改变ArkTS Uint8ClampedArray数组内容的方法。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-values(): IterableIterator<number>--><!--Device-Uint8ClampedArray-values(): IterableIterator<number>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent修改错误) |

## BYTES_PER_ELEMENT

```TypeScript
static readonly BYTES_PER_ELEMENT: number
```

ArkTS Uint8ClampedArray中每个元素所占的字节数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-static readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8ClampedArray-static readonly BYTES_PER_ELEMENT: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## [index: number]

```TypeScript
[index: number]: number
```

返回Uint8ClampedArray指定索引位置的元素。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-[index: number]: number--><!--Device-Uint8ClampedArray-[index: number]: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

ArkTS Uint8ClampedArray底层使用的buffer。

**类型：** ArrayBuffer

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-readonly buffer: ArrayBuffer--><!--Device-Uint8ClampedArray-readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: number
```

ArkTS Uint8ClampedArray所占的字节数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-readonly byteLength: number--><!--Device-Uint8ClampedArray-readonly byteLength: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: number
```

ArkTS Uint8ClampedArray距离其ArrayBuffer起始位置的偏移。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-readonly byteOffset: number--><!--Device-Uint8ClampedArray-readonly byteOffset: number-End-->

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

ArkTS Uint8ClampedArray元素个数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Uint8ClampedArray-readonly length: number--><!--Device-Uint8ClampedArray-readonly length: number-End-->

**系统能力：** SystemCapability.Utils.Lang
