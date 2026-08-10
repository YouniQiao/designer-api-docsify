# Set

一种存储唯一值的非线性数据结构，能够高效地进行元素存在性检测和去重操作。

> **说明：**
> 
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> 本节使用以下标识来表示泛型的使用：

- T：Type，支持[Sendable支持的数据类型](../../../arkts-utils/arkts-sendable.md#sendable支持的数据类型)。  
**装饰器类型：** \@Sendable

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Sendable

<!--Device-collections-class Set<T>--><!--Device-collections-class Set<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。说明：本接口不支持在.ets文件中使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-[Symbol.iterator](): IterableIterator<T>--><!--Device-Set-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## add

```TypeScript
add(value: T): Set<T>
```

检查此Set中是否存在指定值，如果不存在，则将该值添加到Set中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-add(value: T): Set<T>--><!--Device-Set-add(value: T): Set<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 目标值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Set&lt;T&gt; | Set对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The add method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## clear

```TypeScript
clear(): void
```

删除此Set中的所有元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-clear(): void--><!--Device-Set-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## constructor

```TypeScript
constructor(values?: readonly T[] | null)
```

构造函数，用于创建ArkTS Set对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-constructor(values?: readonly T[] | null)--><!--Device-Set-constructor(values?: readonly T[] | null)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | readonly T[] \| null | No | 数组或其它可迭代对象。默认值为**null**，表示创建一个空Set对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The ArkTS Set's constructor cannot be directly invoked. |

## constructor

```TypeScript
constructor(iterable: Iterable<T>)
```

创建ArkTS Set对象的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-constructor(iterable: Iterable<T>)--><!--Device-Set-constructor(iterable: Iterable<T>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iterable | Iterable&lt;T&gt; | Yes | 用于构造ArkTS Set的对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The ArkTS Set's constructor cannot be directly invoked. |

## delete

```TypeScript
delete(value: T): boolean
```

删除此Set中的指定元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-delete(value: T): boolean--><!--Device-Set-delete(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 目标值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 操作结果。成功删除返回**true**，否则返回**false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The delete method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

返回一个Set迭代器对象，该对象包含了此Set中每个元素的键值对。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-entries(): IterableIterator<[T, T]>--><!--Device-Set-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[T, T]&gt; | 返回一个Set迭代器对象，该对象包含了此Set中每个元素的键值对。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## forEach

```TypeScript
forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void
```

对此Set中的每个键值对执行一次回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void--><!--Device-Set-forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: T, value2: T, set: Set&lt;T&gt;) =&gt; void | Yes | 对每个键值对运行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## has

```TypeScript
has(value: T): boolean
```

判断此Set中是否存在指定值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-has(value: T): boolean--><!--Device-Set-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 目标键。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查结果。如果存在指定元素，则返回**true**，否则返回**false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The has method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## keys

```TypeScript
keys(): IterableIterator<T>
```

返回一个Set迭代器对象，该对象包含了此Set中每个元素的键。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-keys(): IterableIterator<T>--><!--Device-Set-keys(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回一个Set迭代器对象，该对象包含了此Set中每个元素的键。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The keys method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## values

```TypeScript
values(): IterableIterator<T>
```

返回一个Set迭代器对象，该对象包含了此Set中每个元素的值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-values(): IterableIterator<T>--><!--Device-Set-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 返回一个Set迭代器对象，该对象包含了此Set中每个元素的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## size

```TypeScript
readonly size: number
```

Set的元素个数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-readonly size: number--><!--Device-Set-readonly size: number-End-->

**System capability:** SystemCapability.Utils.Lang

