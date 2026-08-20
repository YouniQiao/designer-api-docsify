# Map

用于存储键值对的集合，其中每个键都是唯一的。

**继承/实现关系：** Map implements ReadonlyMap<K, V>

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Map--><!--Device-unnamed-export class Map-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { HashMap } from '@kit.ArkTS';
import { HashMapCbFn } from '@kit.ArkTS';
import { LightWeightMap } from '@kit.ArkTS';
import { LightWeightMapCbFn } from '@kit.ArkTS';
import { TreeMap } from '@kit.ArkTS';
import { TreeMapForEachCb } from '@kit.ArkTS';
import { TreeMapComparator } from '@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[K, V]>
```

返回遍历Map中所有Entry的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-$_iterator(): IterableIterator<[K, V]>--><!--Device-Map-$_iterator(): IterableIterator<[K, V]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 遍历所有Entry的迭代器。 |

## clear

```TypeScript
clear(): void
```

删除Map中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-clear(): void--><!--Device-Map-clear(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(initialCapacity: int)
```

使用指定的初始容量创建空Map。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(initialCapacity: int)--><!--Device-Map-constructor(initialCapacity: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initialCapacity | int | 是 | Map的初始容量。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
constructor(values: FixedArray<[K, V]>)
```

根据包含键值对的FixedArray创建Map。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(values: FixedArray<[K, V]>)--><!--Device-Map-constructor(values: FixedArray<[K, V]>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | FixedArray&lt;[K, V]&gt; | 是 | 包含键值对的FixedArray。 |

## constructor

```TypeScript
constructor(entries: Array<[K, V]>)
```

根据包含键值对的数组创建Map。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(entries: Array<[K, V]>)--><!--Device-Map-constructor(entries: Array<[K, V]>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | Array&lt;[K, V]&gt; | 是 | 包含键值对的数组。 |

## constructor

```TypeScript
constructor(map: Map<K, V>)
```

根据另一个Map创建新的Map。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(map: Map<K, V>)--><!--Device-Map-constructor(map: Map<K, V>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | Map&lt;K, V&gt; | 是 | 用于创建新Map的源Map。 |

## constructor

```TypeScript
constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)
```

根据可迭代对象或类数组对象创建Map。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)--><!--Device-Map-constructor(entries?: Iterable<[K, V]> | readonly ((readonly [K, V]) | null | undefined)[] | null)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | Iterable&lt;[K, V]&gt; \| readonly ((readonly [K, V]) \| null \| undefined)[] \| null | 否 | 包含键值对的可迭代对象或类数组对象。 |

## delete

```TypeScript
delete(key: K): boolean
```

从Map中移除指定键对应的Entry。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-delete(key: K): boolean--><!--Device-Map-delete(key: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待移除的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该Entry被移除则返回true，否则返回false。 |

## entries

```TypeScript
entries(): IterableIterator<[K, V]>
```

以Entry数组的形式返回Map中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-entries(): IterableIterator<[K, V]>--><!--Device-Map-entries(): IterableIterator<[K, V]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, V]&gt; | 由Entry组成的数组。 |

## forEach

```TypeScript
forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void
```

按插入顺序对Map中的每个键值对执行一次指定的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void--><!--Device-Map-forEach(callbackfn: (v: V, k: K, map: Map<K, V>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (v: V, k: K, map: Map&lt;K, V&gt;) =&gt; void | 是 | 对每个键值对调用的回调函数。 |

## get

```TypeScript
get(key: K): V | undefined
```

返回指定键所关联的值（如果存在）。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-get(key: K): V | undefined--><!--Device-Map-get(key: K): V | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待在Map中查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V \| undefined | 键存在时所关联的值。 |

## get

```TypeScript
get(key: K, def: V): V
```

返回指定键所关联的值；如果键不存在，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-get(key: K, def: V): V--><!--Device-Map-get(key: K, def: V): V-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待在Map中查找的键。 |
| def | V | 是 | 键不存在于Map中时返回的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 键存在时返回对应的值，否则返回默认值。 |

## has

```TypeScript
has(key: K): boolean
```

判断指定的键是否存在于Map中。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-has(key: K): boolean--><!--Device-Map-has(key: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待在Map中查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该键存在于Map中则返回true，否则返回false。 |

## keySet

```TypeScript
public keySet(): Set<K>
```

以Set的形式返回Map中的所有键。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-public keySet(): Set<K>--><!--Device-Map-public keySet(): Set<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Set&lt;K&gt; | 包含所有键的新Set实例。 |

## keys

```TypeScript
keys(): IterableIterator<K>
```

以键迭代器的形式返回Map中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-keys(): IterableIterator<K>--><!--Device-Map-keys(): IterableIterator<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | 包含所有键的迭代器。 |

## set

```TypeScript
set(key: K, val: V): this
```

将一对键和值存入Map。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-set(key: K, val: V): this--><!--Device-Map-set(key: K, val: V): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待存入Map的键。 |
| val | V | 是 | 待存入Map的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 当前Map。 |

## toString

```TypeScript
toString(): string
```

将当前Map转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-toString(): string--><!--Device-Map-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示该Map的字符串。 |

## values

```TypeScript
values(): IterableIterator<V>
```

以值迭代器的形式返回Map中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Map-values(): IterableIterator<V>--><!--Device-Map-values(): IterableIterator<V>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;V&gt; | 包含所有值的迭代器。 |

