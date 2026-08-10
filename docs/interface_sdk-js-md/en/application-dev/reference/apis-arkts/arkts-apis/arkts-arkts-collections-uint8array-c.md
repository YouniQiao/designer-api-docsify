# Uint8Array

一种线性数据结构，底层基于[ArkTS ArrayBuffer](arkts-collections.md)实现。

> **说明：**
> 
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> **装饰器类型：** \@Sendable

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Sendable

<!--Device-collections-class Uint8Array--><!--Device-collections-class Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<number>
```

返回一个迭代器，迭代器的每一项都是一个数字。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-[Symbol.iterator](): IterableIterator<number>--><!--Device-Uint8Array-[Symbol.iterator](): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt; | 生成数字的迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## at

```TypeScript
at(index: number): number | undefined
```

返回指定下标的元素，如果不存在，则返回**undefined**。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-at(index: number): number | undefined--><!--Device-Uint8Array-at(index: number): number | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 要返回的元素的索引（从零开始）。&lt;br/&gt; 如果传入负数，则从最后一个元素开始倒数。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 获取到的元素；如果未找到，则返回**undefined**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The at method cannot be bound. |
| 10200201 | Concurrent modification error. |

## constructor

```TypeScript
constructor()
```

构造函数，用于创建一个空的ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-constructor()--><!--Device-Uint8Array-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The Uint8Array's constructor cannot be directly invoked. |

## constructor

```TypeScript
constructor(length: number)
```

构造函数，用于创建一个指定长度的ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-constructor(length: number)--><!--Device-Uint8Array-constructor(length: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | Yes | 用于指定ArkTS Uint8Array的长度。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The Uint8Array's constructor cannot be directly invoked. |

## constructor

```TypeScript
constructor(elements: Iterable<number>)
```

构造函数，以Iterable创建一个ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-constructor(elements: Iterable<number>)--><!--Device-Uint8Array-constructor(elements: Iterable<number>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | Iterable&lt;number&gt; | Yes | 可迭代数字集合，用于构造ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The Uint8Array's constructor cannot be directly invoked. |

## constructor

```TypeScript
constructor(array: ArrayLike<number> | ArrayBuffer)
```

构造函数，以ArrayLike或ArkTS ArrayBuffer创建一个ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-constructor(array: ArrayLike<number> | ArrayBuffer)--><!--Device-Uint8Array-constructor(array: ArrayLike<number> | ArrayBuffer)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;number&gt; \| ArrayBuffer | Yes | 用于构造ArkTS Uint8Array的对象。当参数类型是ArrayBuffer时，buffer所占的 字节数须是4的整数倍。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The Uint8Array's constructor cannot be directly invoked. |

## constructor

```TypeScript
constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)
```

构造函数，以ArrayBuffer创建一个ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)--><!--Device-Uint8Array-constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | 用于构造ArkTS Uint8Array的ArrayBuffer对象。buffer所占的字节数须是4的整数倍。 |
| byteOffset | number | No | 指定buffer的字节偏移，从0开始。默认值为**0**。 |
| length | number | No | 指定ArkTS Uint8Array的长度。默认值为**0**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The Uint8Array's constructor cannot be directly invoked. |

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): Uint8Array
```

从ArkTS Uint8Array指定范围内的元素依次拷贝到目标位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-copyWithin(target: number, start: number, end?: number): Uint8Array--><!--Device-Uint8Array-copyWithin(target: number, start: number, end?: number): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | number | Yes | 目标起始位置的下标。如果传入负数，则指代 `target + array.length` 位置的下标。 |
| start | number | Yes | 源起始位置的下标。如果传入负数，则指代 `start + Uint8Array.length` 位置的下标。 |
| end | number | No | 源终止位置的下标（不包含end位置的元素）。如果传入负数，则指代 `end + Uint8Array.length` 位置的下标。默认值为ArkTS Uint8Array的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 修改后的ArkTS Uint8Array。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The copyWithin method cannot be bound. |
| 10200201 | Concurrent modification error. |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint8Array中每个元素的键值对。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-entries(): IterableIterator<[number, number]>--><!--Device-Uint8Array-entries(): IterableIterator<[number, number]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, number]&gt; | 迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound. |
| 10200201 | Concurrent modification error. |

## every

```TypeScript
every(predicate: TypedArrayPredicateFn<number, Uint8Array>): boolean
```

测试ArkTS Uint8Array中的所有元素是否满足指定条件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-every(predicate: TypedArrayPredicateFn<number, Uint8Array>): boolean--><!--Device-Uint8Array-every(predicate: TypedArrayPredicateFn<number, Uint8Array>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8Array&gt; | Yes | 用于测试的断言函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查结果。如果所有元素都满足指定条件则返回**true**；否则返回**false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The every method cannot be bound. |
| 10200201 | Concurrent modification error. |

## fill

```TypeScript
fill(value: number, start?: number, end?: number): Uint8Array
```

使用特定值填充ArkTS Uint8Array指定范围的全部元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-fill(value: number, start?: number, end?: number): Uint8Array--><!--Device-Uint8Array-fill(value: number, start?: number, end?: number): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 待填充的值。 |
| start | number | No | 开始填充的索引。如果传入负数，则指代 `start + Uint8Array.length` 位置的下标。默认值为**0**。 |
| end | number | No | 结束填充的索引（不包含该元素）。如果传入负数，则指代 `end + Uint8Array.length` 位置的下标。默认值为ArkTS Uint8Array的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 填充后的ArkTS Uint8Array。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The fill method cannot be bound. |
| 10200201 | Concurrent modification error. |

## filter

```TypeScript
filter(predicate: TypedArrayPredicateFn<number, Uint8Array>): Uint8Array
```

返回一个新的ArkTS Uint8Array对象，其包含满足指定条件的所有元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-filter(predicate: TypedArrayPredicateFn<number, Uint8Array>): Uint8Array--><!--Device-Uint8Array-filter(predicate: TypedArrayPredicateFn<number, Uint8Array>): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8Array&gt; | Yes | 用于元素过滤的断言函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 过滤后的ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The filter method cannot be bound. |
| 10200201 | Concurrent modification error. |

## find

```TypeScript
find(predicate: TypedArrayPredicateFn<number, Uint8Array>): number | undefined
```

返回ArkTS Uint8Array中第一个满足指定条件的元素的值，如果所有元素都不满足，则返回**undefined**。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-find(predicate: TypedArrayPredicateFn<number, Uint8Array>): number | undefined--><!--Device-Uint8Array-find(predicate: TypedArrayPredicateFn<number, Uint8Array>): number | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8Array&gt; | Yes | 用于元素查找的断言函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 第一个满足条件的元素的值；如果所有元素都不满足条件，则返回 **undefined**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The find method cannot be bound. |
| 10200201 | Concurrent modification error. |

## findIndex

```TypeScript
findIndex(predicate: TypedArrayPredicateFn<number, Uint8Array>): number
```

返回ArkTS Uint8Array中第一个满足指定条件的元素索引，如果所有元素都不满足，则返回**-1**。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-findIndex(predicate: TypedArrayPredicateFn<number, Uint8Array>): number--><!--Device-Uint8Array-findIndex(predicate: TypedArrayPredicateFn<number, Uint8Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8Array&gt; | Yes | 用于元素查找的断言函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 第一个满足条件的元素索引；如果所有元素都不满足条件， 则返回**-1**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The findIndex method cannot be bound. |
| 10200201 | Concurrent modification error. |

## forEach

```TypeScript
forEach(callbackFn: TypedArrayForEachCallback<number, Uint8Array>): void
```

对ArkTS Uint8Array中的每个元素执行提供的回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-forEach(callbackFn: TypedArrayForEachCallback<number, Uint8Array>): void--><!--Device-Uint8Array-forEach(callbackFn: TypedArrayForEachCallback<number, Uint8Array>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md)&lt;number, Uint8Array&gt; | Yes | 用于对每个元素执行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |
| 10200201 | Concurrent modification error. |

## from

```TypeScript
static from(arrayLike: ArrayLike<number>): Uint8Array
```

从一个ArrayLike或者可迭代对象中创建一个ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-static from(arrayLike: ArrayLike<number>): Uint8Array--><!--Device-Uint8Array-static from(arrayLike: ArrayLike<number>): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;number&gt; | Yes | 用于构造ArkTS Uint8Array的ArrayLike对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新创建的ArkTS Uint8Array对象。 |

## from

```TypeScript
static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8Array
```

从一个ArrayLike中创建一个ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8Array--><!--Device-Uint8Array-static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;T&gt; | Yes | 用于构造ArkTS Uint8Array的ArrayLike对象。 |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;T, number&gt; | Yes | 映射函数，对数组的每个元素调用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新创建的ArkTS Uint8Array对象。 |

## from

```TypeScript
static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8Array
```

从一个可迭代对象中创建一个ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8Array--><!--Device-Uint8Array-static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | Iterable&lt;number&gt; | Yes | 用于构造ArkTS Uint8Array的可迭代对象。 |
| mapFn | [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md)&lt;number, number&gt; | No | 映射函数，对数组的每个元素 调用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新创建的ArkTS Uint8Array对象。 |

## includes

```TypeScript
includes(searchElement: number, fromIndex?: number): boolean
```

判断ArkTS Uint8Array是否包含特定元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-includes(searchElement: number, fromIndex?: number): boolean--><!--Device-Uint8Array-includes(searchElement: number, fromIndex?: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | number | Yes | 待搜索的元素。 |
| fromIndex | number | No | 在数组中开始搜索searchElement的位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查结果。如果该元素存在则返回**true**；否则返回 **false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The includes method cannot be bound. |
| 10200201 | Concurrent modification error. |

## indexOf

```TypeScript
indexOf(searchElement: number, fromIndex?: number): number
```

返回ArkTS Uint8Array中给定元素的第一个索引，如果不存在，则返回**-1**。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-indexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8Array-indexOf(searchElement: number, fromIndex?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | number | Yes | 待索引的值。 |
| fromIndex | number | No | 搜索的起始下标。默认值为**0**。如果下标大于等于ArkTS Uint8Array的长度， 则返回**-1**。如果传入负数，则从前到后从ArkTS Uint8Array末尾开始搜索。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 该值第一次出现的索引。如果未找到该值，则返回**-1**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The indexOf method cannot be bound. |
| 10200201 | Concurrent modification error. |

## join

```TypeScript
join(separator?: string): string
```

将ArkTS Uint8Array的所有元素拼接成一个字符串，元素之间使用指定的分隔符分隔。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-join(separator?: string): string--><!--Device-Uint8Array-join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No | 分隔字符串。如果未传入任何值，则使用逗号（,）作为 分隔符。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 拼接得到的字符串。如果数组为空，则返回空字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The join method cannot be bound. |
| 10200201 | Concurrent modification error. |

## keys

```TypeScript
keys(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint8Array中每个元素的键（下标）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-keys(): IterableIterator<number>--><!--Device-Uint8Array-keys(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt; | 迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The keys method cannot be bound. |
| 10200201 | Concurrent modification error. |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: number, fromIndex?: number): number
```

返回ArkTS Uint8Array实例中最后一次出现指定值的索引。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8Array-lastIndexOf(searchElement: number, fromIndex?: number): number--><!--Device-Uint8Array-lastIndexOf(searchElement: number, fromIndex?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchElement | number | Yes | 待索引的值。 |
| fromIndex | number | No | 搜索的起始下标。默认值为**0**。如果下标大于等于ArkTS Uint8Array的长度， 则返回**-1**。如果传入负数，则从后到前从ArkTS Uint8Array末尾开始搜索。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 该值最后一次出现的索引。如果未找到该值，则返回**-1**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The lastIndexOf method cannot be bound. |
| 10200201 | Concurrent modification error. |

## map

```TypeScript
map(callbackFn: TypedArrayMapCallback<number, Uint8Array>): Uint8Array
```

对ArkTS Uint8Array中的每个元素应用指定的回调函数，并使用结果创建一个新的ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-map(callbackFn: TypedArrayMapCallback<number, Uint8Array>): Uint8Array--><!--Device-Uint8Array-map(callbackFn: TypedArrayMapCallback<number, Uint8Array>): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md)&lt;number, Uint8Array&gt; | Yes | 一个最多接受三个参数的函数。 map方法对数组中的每个元素调用一次callbackfn函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新的ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The map method cannot be bound. |
| 10200201 | Concurrent modification error. |

## of

```TypeScript
static of(...items: number[]): Uint8Array
```

通过可变数量的参数创建一个新的ArkTS Uint8Array对象。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8Array-static of(...items: number[]): Uint8Array--><!--Device-Uint8Array-static of(...items: number[]): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | number[] | Yes | 用于创建数组的元素，参数个数可以是0个、1个或者多个。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新的ArkTS Uint8Array实例。可能的原因：1.必填参数未指定； &lt;br&gt;2.参数类型不正确；3.参数校验失败。 |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number
```

对ArkTS Uint8Array中的每个元素执行归约函数，并返回最终的归约结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number--><!--Device-Uint8Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint8Array&gt; | Yes | 一个最多接受四个参数的函数。 reduce方法对数组中的每个元素调用一次callbackfn函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 由最后一次调用归约函数返回的最终结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The reduce method cannot be bound. |
| 10200201 | Concurrent modification error. |

## reduce

```TypeScript
reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>, initialValue: number): number
```

对ArkTS Uint8Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>, initialValue: number): number--><!--Device-Uint8Array-reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>, initialValue: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint8Array&gt; | Yes | 一个最多接受四个参数的函数。 reduce方法对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | number | Yes | 如果指定了initialValue，则将其作为初始值开始 累加。首次调用callbackfn函数时，将该值作为参数提供， 而不是使用数组元素的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 由最后一次调用归约函数返回的最终结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The reduce method cannot be bound. |
| 10200201 | Concurrent modification error. |

## reduce

```TypeScript
reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U
```

对ArkTS Uint8Array中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U--><!--Device-Uint8Array-reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint8Array&gt; | Yes | 归约函数。 |
| initialValue | U | Yes | 初始值。 |

**Return value:**

| Type | Description |
| --- | --- |
| U | 由最后一次调用归约函数返回的最终结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The reduce method cannot be bound. |
| 10200201 | Concurrent modification error. |

## reduceRight

```TypeScript
reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U
```

反向遍历ArkTS Uint8Array，对每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U--><!--Device-Uint8Array-reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;U, number, Uint8Array&gt; | Yes | 对Uint8Array中的每个元素 调用的函数。 |
| initialValue | U | Yes | 作为回调函数首次调用的第一个参数的值。 &lt;br&gt;如果未提供初始值，则使用Uint8Array的最后一个元素， &lt;br&gt;回调将从倒数第二个元素开始调用。 |

**Return value:**

| Type | Description |
| --- | --- |
| U | 由最后一次调用归约函数返回的最终结果。可能的原因： 1.必填参数未指定。 2.参数类型不正确。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The reduceRight method cannot be bound. |
| 10200201 | Concurrent modification error. |

## reduceRight

```TypeScript
reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number
```

反向遍历ArkTS Uint8Array，对每个元素执行归约函数，并返回最终的归约结果。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number--><!--Device-Uint8Array-reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md)&lt;number, number, Uint8Array&gt; | Yes | 对Uint8Array中的每个元素 调用的函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 由最后一次调用归约函数返回的最终结果。可能的原因： 1.必填参数未指定。 2.参数类型不正确。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The reduceRight method cannot be bound. |
| 10200201 | Concurrent modification error. |

## reverse

```TypeScript
reverse(): Uint8Array
```

反转ArkTS Uint8Array。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-reverse(): Uint8Array--><!--Device-Uint8Array-reverse(): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 反转后的ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The reverse method cannot be bound. |
| 10200201 | Concurrent modification error. |

## set

```TypeScript
set(array: ArrayLike<number>, offset?: number): void
```

将传入的ArrayLike元素依次写入到指定的起始位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-set(array: ArrayLike<number>, offset?: number): void--><!--Device-Uint8Array-set(array: ArrayLike<number>, offset?: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;number&gt; | Yes | 用于设置的ArrayLike对象。 |
| offset | number | No | 当前数组中要写入值的起始位置索引。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The set method cannot be bound. |
| 10200201 | Concurrent modification error. |

## slice

```TypeScript
slice(start?: number, end?: number): Uint8Array
```

返回一个新的ArkTS Uint8Array对象，其包含原ArkTS Uint8Array指定范围的内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-slice(start?: number, end?: number): Uint8Array--><!--Device-Uint8Array-slice(start?: number, end?: number): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | No | 开始索引。如果传入负数，则指代 `start + Uint8Array.length` 位置的下标。默认值为**0**。 |
| end | number | No | 结束索引（不包含该元素）。如果传入负数，则指代 `end + Uint8Array.length` 位置的下标。默认值为ArkTS Uint8Array的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新的ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The slice method cannot be bound. |
| 10200201 | Concurrent modification error. |

## some

```TypeScript
some(predicate: TypedArrayPredicateFn<number, Uint8Array>): boolean
```

测试ArkTS Uint8Array中是否存在元素满足指定条件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-some(predicate: TypedArrayPredicateFn<number, Uint8Array>): boolean--><!--Device-Uint8Array-some(predicate: TypedArrayPredicateFn<number, Uint8Array>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md)&lt;number, Uint8Array&gt; | Yes | 用于测试的断言函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查结果。如果存在元素满足指定条件则返回**true**； 否则返回**false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The some method cannot be bound. |
| 10200201 | Concurrent modification error. |

## sort

```TypeScript
sort(compareFn?: TypedArrayCompareFn<number>): Uint8Array
```

对ArkTS Uint8Array进行排序，并返回排序后的ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-sort(compareFn?: TypedArrayCompareFn<number>): Uint8Array--><!--Device-Uint8Array-sort(compareFn?: TypedArrayCompareFn<number>): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md)&lt;number&gt; | No | 用于确定元素顺序的函数。默认使用升序排序。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 排序后的ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The sort method cannot be bound. |
| 10200201 | Concurrent modification error. |

## subarray

```TypeScript
subarray(begin?: number, end?: number): Uint8Array
```

从指定的位置截取数组，返回一个新的、基于相同ArkTS ArrayBuffer的ArkTS Uint8Array对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-subarray(begin?: number, end?: number): Uint8Array--><!--Device-Uint8Array-subarray(begin?: number, end?: number): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | No | 开始索引。如果传入负数，则指代 `begin + Uint8Array.length` 位置的下标。默认值为**0**。 |
| end | number | No | 结束索引（不包含该元素）。如果传入负数，则指代 `end + Uint8Array.length` 位置的下标。默认值为ArkTS Uint8Array的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 新的ArkTS Uint8Array对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The subarray method cannot be bound. |
| 10200201 | Concurrent modification error. |

## toLocaleString

```TypeScript
toLocaleString(): string
```

根据当前应用的系统地区获取符合当前文化习惯的数字表示形式，让每个元素调用自己的toLocaleString方法把数字转换为字符串，然后使用逗号将每个元素的结果字符串按照顺序拼接成字符串。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8Array-toLocaleString(): string--><!--Device-Uint8Array-toLocaleString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 一个包含数组所有元素的字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The toLocaleString method cannot be bound. |
| 10200201 | Concurrent modification error. |

## toString

```TypeScript
toString(): string
```

将ArkTS Uint8Array转换为字符串。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Uint8Array-toString(): string--><!--Device-Uint8Array-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 一个包含数组所有元素的字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The toString method cannot be bound. |
| 10200201 | Concurrent modification error. |

## values

```TypeScript
values(): IterableIterator<number>
```

返回一个新的迭代器对象，该对象包含ArkTS Uint8Array中每个元素的值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-values(): IterableIterator<number>--><!--Device-Uint8Array-values(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt; | 迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound. |
| 10200201 | Concurrent modification error. |

## BYTES_PER_ELEMENT

```TypeScript
static readonly BYTES_PER_ELEMENT: number
```

ArkTS Uint8Array中每个元素所占用的字节数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-static readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8Array-static readonly BYTES_PER_ELEMENT: number-End-->

**System capability:** SystemCapability.Utils.Lang

## [index: number]

```TypeScript
[index: number]: number
```

返回指定索引位置的元素。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-[index: number]: number--><!--Device-Uint8Array-[index: number]: number-End-->

**System capability:** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

ArkTS Uint8Array底层使用的buffer。

**Type:** ArrayBuffer

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-readonly buffer: ArrayBuffer--><!--Device-Uint8Array-readonly buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: number
```

ArkTS Uint8Array所占的字节数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-readonly byteLength: number--><!--Device-Uint8Array-readonly byteLength: number-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: number
```

ArkTS Uint8Array距离其ArrayBuffer起始位置的偏移。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-readonly byteOffset: number--><!--Device-Uint8Array-readonly byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
readonly length: number
```

ArkTS Uint8Array元素个数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Uint8Array-readonly length: number--><!--Device-Uint8Array-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang

