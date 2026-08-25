# Map

用于存储键值对的集合，其中每个键都是唯一的。

**继承/实现关系：** Map implements ReadonlyMap<K, V>

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

返回遍历Map中所有Entry的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; |

## clear

```TypeScript
clear(): void
```

删除Map中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(initialCapacity: int)
```

使用指定的初始容量创建空Map。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| initialCapacity | int | 是 |

## constructor

```TypeScript
constructor(values: FixedArray<[K, V]>)
```

根据包含键值对的FixedArray创建Map。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [values](#values) | FixedArray & lt;[K, V] & gt; | 是 |

## constructor

```TypeScript
constructor(entries: Array<[K, V]>)
```

根据包含键值对的数组创建Map。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [entries](#entries) | Array & lt;[K, V] & gt; | 是 |

## constructor

```TypeScript
constructor(map: Map<K, V>)
```

根据另一个Map创建新的Map。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| map | Map & lt;K, V & gt; | 是 |

## constructor

```TypeScript
constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)
```

根据可迭代对象或类数组对象创建Map。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [entries](#entries) | Iterable & lt;[K, V] & gt; \ | readonly ((readonly [K, V]) \| null \| undefined)[] \| null | 否 |

## delete

```TypeScript
delete(key: K): boolean
```

从Map中移除指定键对应的Entry。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

以Entry数组的形式返回Map中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; |

## forEach

```TypeScript
forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void
```

按插入顺序对Map中的每个键值对执行一次指定的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (v: V, k: K, map: Map & lt;K, V & gt;) = & gt; void | 是 |

## get

```TypeScript
get(key: K): V | undefined
```

返回指定键所关联的值（如果存在）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| V \| undefined |

## get

```TypeScript
get(key: K, def: V): V
```

返回指定键所关联的值；如果键不存在，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |
| def | V | 是 |

**返回值：**

| 类型 |
| --- |
| V |

## has

```TypeScript
has(key: K): boolean
```

判断指定的键是否存在于Map中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## keys

```TypeScript
keys(): IterableIterator<K>
```

以键迭代器的形式返回Map中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; |

## keySet

```TypeScript
public keySet(): Set<K>
```

以Set的形式返回Map中的所有键。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Set & lt;K & gt; |

## set

```TypeScript
set(key: K, val: V): this
```

将一对键和值存入Map。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | K | 是 |
| val | V | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## toString

```TypeScript
toString(): string
```

将当前Map转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## values

```TypeScript
values(): IterableIterator<V>
```

以值迭代器的形式返回Map中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; |

## size

```TypeScript
get size(): int
```

返回Map中键值对的number。

**类型：** int

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
