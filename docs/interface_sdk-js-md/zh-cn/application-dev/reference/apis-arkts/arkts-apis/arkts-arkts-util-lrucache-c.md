# LRUCache

提供在缓存已满时丢弃最近最少使用的数据以腾出空间给新元素的 API。此类使用最近最少使用（LRU）算法，该算法认为最近 使用的数据可能在不久的将来再次被访问，而最少访问的数据是最不具价值的数据，应从缓存中移除。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[K, V]>
```

指定对象的默认迭代器。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[K, V] & gt; |

## afterRemoval

```TypeScript
afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void
```

在移除值后执行后续操作。后续操作必须由开发者实现。该 API 在删除操作期间会被调用，例如 [get&lt;sup&gt;9+&lt;/sup&gt;](#get)、[put&lt;sup&gt;9+&lt;/sup&gt;](#put)、 [remove&lt;sup&gt;9+&lt;/sup&gt;](#remove)、[clear&lt;sup&gt;9+&lt;/sup&gt;](#clear) 和 [updateCapacity&lt;sup&gt;9+&lt;/sup&gt;](#updatecapacity)。

> **NOTE：**&gt;
> 如果在调用 [clear&lt;sup&gt;9+&lt;/sup&gt;](#clear) 和
> [updateCapacity&lt;sup&gt;9+&lt;/sup&gt;](#updatecapacity) 后执行回调方法，并且输入的 **key** 和
> **value** 参数为 MapIterator 类型，请参考示例 2 执行后续操作。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEvict | boolean | 是 |
| key | K | 是 |
| value | V | 是 |
| newValue | V | 是 |

## clear

```TypeScript
clear(): void
```

清除此缓存中的键值对。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(capacity?: number)
```

用于创建 **LRUCache** 实例的构造函数。缓存的默认容量为 64。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capacity | number | 否 |

## contains

```TypeScript
contains(key: K): boolean
```

判断此缓存是否包含指定的 key。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## createDefault

```TypeScript
createDefault(key: K): V
```

在缓存中无匹配的 key 时执行后续操作，并返回与该 key 关联的值（默认为 **undefined**）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| V |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

返回一个迭代器对象，该对象按插入顺序遍历此对象中的所有键值对（[key, value]）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[K, V] & gt; |

## get

```TypeScript
get(key: K): V | undefined
```

获取 key 对应的值。如果该 key 不在缓存中，则调用 [createDefault&lt;sup&gt;9+&lt;/sup&gt;](#createdefault) 创建该 key。如果 **createDefault** 中指定的值 不为 **undefined**，则调用 [afterRemoval&lt;sup&gt;9+&lt;/sup&gt;](#afterremoval) 返回 **createDefault** 中指定的值。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| V \| undefined |

## getCapacity

```TypeScript
getCapacity(): number
```

获取此缓存的容量。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getCreateCount

```TypeScript
getCreateCount(): number
```

获取创建对象的次数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getMatchCount

```TypeScript
getMatchCount(): number
```

获取查询值匹配的次数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getMissCount

```TypeScript
getMissCount(): number
```

获取查询值未匹配的次数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getPutCount

```TypeScript
getPutCount(): number
```

获取向此缓存添加的次数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getRemovalCount

```TypeScript
getRemovalCount(): number
```

获取此缓存中键值对被回收的次数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断此缓存是否为空。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## keys

```TypeScript
keys(): K[]
```

获取此缓存中的所有 key，按从最近最少访问到最近最多访问的顺序排列。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| K[] |

## put

```TypeScript
put(key: K, value: V): V
```

向此缓存添加键值对，并返回与该 key 关联的值。如果缓存中的值总数大于指定容量，则执行删除操作。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |
| value | V | 是 |

**返回值：**

| 类型 |
| --- |
| V |

## remove

```TypeScript
remove(key: K): V | undefined
```

从此缓存中移除 key 及其关联的值，并返回与该 key 关联的值。如果 key 不存在，则返回 **undefined**。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| V \| undefined |

## toString

```TypeScript
toString(): string
```

获取此缓存的字符串表示形式。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## updateCapacity

```TypeScript
updateCapacity(newCapacity: number): void
```

改变缓存容量。如果新容量小于等于 **0**，则抛出异常。如果缓存中的值总数大于指定容量，则执行删除操作。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newCapacity | number | 是 |

## values

```TypeScript
values(): V[]
```

获取此缓存中的所有值，按从最近最少访问到最近最多访问的顺序排列。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| V[] |

## length

```TypeScript
length: number
```

当前缓存中值的总数。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
