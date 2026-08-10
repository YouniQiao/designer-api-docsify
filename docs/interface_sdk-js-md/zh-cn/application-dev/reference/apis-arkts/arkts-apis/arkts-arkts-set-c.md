# Set

Set implementation.

**继承/实现关系：** Set implements [ReadonlySet<K>](ReadonlySet<K>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Set<K> implements ReadonlySet<K>--><!--Device-unnamed-export class Set<K> implements ReadonlySet<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<K>
```

Returns the default iterator of the Set, which is the values() iterator.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-$_iterator(): IterableIterator<K>--><!--Device-Set-$_iterator(): IterableIterator<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | The default iterator of the Set. |

## add

```TypeScript
add(val: K): this
```

Puts a value into the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-add(val: K): this--><!--Device-Set-add(val: K): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | K | 是 | the value to put into the Set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Add value Set. |

## clear

```TypeScript
clear(): void
```

Deletes all elements from the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-clear(): void--><!--Device-Set-clear(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(bucketsCount: int)
```

Creates a new Set instance with the specified number of buckets.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-constructor(bucketsCount: int)--><!--Device-Set-constructor(bucketsCount: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bucketsCount | int | 是 | The number of buckets for the internal map. &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
constructor(set: Set<K>)
```

Creates a new Set instance from another Set.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-constructor(set: Set<K>)--><!--Device-Set-constructor(set: Set<K>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | Set&lt;K&gt; | 是 | Another Set instance used for initialization. |

## constructor

```TypeScript
constructor(values: K[])
```

Creates a new Set instance from an array.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-constructor(values: K[])--><!--Device-Set-constructor(values: K[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | K[] | 是 | The array used for initialization. |

## constructor

```TypeScript
constructor(elements?: Iterable<K> | FixedArray<K> | null)
```

Creates a new Set instance from an iterable object or FixedArray.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-constructor(elements?: Iterable<K> | FixedArray<K> | null)--><!--Device-Set-constructor(elements?: Iterable<K> | FixedArray<K> | null)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable&lt;K&gt; \| FixedArray&lt;K&gt; \| null | 否 | The iterable object, FixedArray, or null used for initialization. |

## delete

```TypeScript
delete(val: K): boolean
```

Removes a value from the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-delete(val: K): boolean--><!--Device-Set-delete(val: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | K | 是 | the value to remove. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value was removed. |

## entries

```TypeScript
entries(): IterableIterator<[K, K]>
```

Returns an iterable of [v, v] pairs for every value in the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-entries(): IterableIterator<[K, K]>--><!--Device-Set-entries(): IterableIterator<[K, K]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[K, K]&gt; | an iterable of [v, v] pairs. |

## forEach

```TypeScript
forEach(callbackfn: (k: K, v: K, set: Set<K>) => void): void
```

Executes a provided function once per each value in the Set object, in insertion order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-forEach(callbackfn: (k: K, v: K, set: Set<K>) => void): void--><!--Device-Set-forEach(callbackfn: (k: K, v: K, set: Set<K>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (k: K, v: K, set: Set&lt;K&gt;) =&gt; void | 是 | the function to apply. |

## has

```TypeScript
has(val: K): boolean
```

Checks if a value is in the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-has(val: K): boolean--><!--Device-Set-has(val: K): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | K | 是 | the value to find in the Set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value is in the Set. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Despite name, returns elements from the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-keys(): IterableIterator<K>--><!--Device-Set-keys(): IterableIterator<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | an iterable of the values in the Set. |

## toString

```TypeScript
toString(): string
```

Converts this Set to a String.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-toString(): string--><!--Device-Set-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string representing the Set. |

## values

```TypeScript
values(): IterableIterator<K>
```

Returns elements from the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-values(): IterableIterator<K>--><!--Device-Set-values(): IterableIterator<K>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;K&gt; | an iterable of the values in the Set. |

## size

```TypeScript
get size(): int
```

Gets the number of unique elements in the Set.

**类型：** int

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Set-get size(): int--><!--Device-Set-get size(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

