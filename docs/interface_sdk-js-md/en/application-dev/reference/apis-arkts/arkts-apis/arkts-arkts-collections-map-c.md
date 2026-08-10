# Map

一种基于键值对存储的非线性数据结构，能够高效地通过唯一键来存取对应的值。

> **说明：**
> 
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> 本节使用以下标识符来表示泛型的使用：

- K：Key，键。  
- V：Value，值。  
K和V类型都需为  
[Sendable支持的数据类型](../../../arkts-utils/arkts-sendable.md#sendable支持的数据类型)。  
**装饰器类型**：\@Sendable

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Sendable

<!--Device-collections-class Map<K, V>--><!--Device-collections-class Map<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。说明：本接口不支持在.ets文件中使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-[Symbol.iterator](): IterableIterator<[K, V]>--><!--Device-Map-[Symbol.iterator](): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 返回一个迭代器对象，该对象包含键值对。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

## clear

```TypeScript
clear(): void
```

删除该Map中的所有元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-clear(): void--><!--Device-Map-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The clear method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## constructor

```TypeScript
constructor(entries?: readonly (readonly [K, V])[] | null)
```

构造函数，用于创建ArkTS Map对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-constructor(entries?: readonly (readonly [K, V])[] | null)--><!--Device-Map-constructor(entries?: readonly (readonly [K, V])[] | null)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entries | readonly (readonly [K, V])[] \| null | No | 键值对数组或其它可迭代对象。 默认值为**null**，创建一个空Map对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The ArkTS Map's constructor cannot be directly invoked. |

## constructor

```TypeScript
constructor(iterable: Iterable<readonly [K, V]>)
```

创建ArkTS Map对象的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-constructor(iterable: Iterable<readonly [K, V]>)--><!--Device-Map-constructor(iterable: Iterable<readonly [K, V]>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iterable | Iterable&lt;readonly [K, V]&gt; | Yes | 用于构造ArkTS Map的对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200012 | The ArkTS Map's constructor cannot be directly invoked. |

## delete

```TypeScript
delete(key: K): boolean
```

删除该Map中指定元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-delete(key: K): boolean--><!--Device-Map-delete(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 待删除元素的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 操作结果。如果元素存在并已被删除，则返回**true**； 否则该元素不存在，返回**false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The delete method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

返回一个Map迭代器对象，该对象包含了此Map中的每个元素的[key, value]对。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-entries(): IterableIterator<[K, V]>--><!--Device-Map-entries(): IterableIterator<[K, V]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | Map迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The entries method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## forEach

```TypeScript
forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void
```

按插入顺序对该Map中的每个键/值对执行一次回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void--><!--Device-Map-forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: V, key: K, map: Map&lt;K, V&gt;) =&gt; void | Yes | 对每个键值对运行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The forEach method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## get

```TypeScript
get(key: K): V | undefined
```

返回该Map中的指定元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-get(key: K): V | undefined--><!--Device-Map-get(key: K): V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 指定key。 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 与指定键相关联的元素，如果键在Map对象中找不到，则返回**undefined**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The get method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## has

```TypeScript
has(key: K): boolean
```

判断该Map中是否存在指定元素。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-has(key: K): boolean--><!--Device-Map-has(key: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 待查找元素的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 判断结果。如果存在指定元素，则返回**true**，否则返回 **false**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The has method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

返回一个Map迭代器对象，该对象包含了此Map中每个元素的键。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-keys(): IterableIterator<K>--><!--Device-Map-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | Map迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The keys method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## set

```TypeScript
set(key: K, value: V): Map<K, V>
```

向该Map添加或更新一个指定的键值对。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-set(key: K, value: V): Map<K, V>--><!--Device-Map-set(key: K, value: V): Map<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes | 添加或更新指定元素的键。 |
| value | V | Yes | 添加或更新指定元素的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;K, V&gt; | 新的Map对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The set method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## values

```TypeScript
values(): IterableIterator<V>
```

返回一个Map迭代器对象，该对象包含此Map中每个元素的值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-values(): IterableIterator<V>--><!--Device-Map-values(): IterableIterator<V>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; | Map迭代器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200011 | The values method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

## size

```TypeScript
readonly size: number
```

Map的元素个数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Map-readonly size: number--><!--Device-Map-readonly size: number-End-->

**System capability:** SystemCapability.Utils.Lang

