# ReadonlySet

ReadonlySet implementation.

**继承/实现关系：** ReadonlySet extends [Iterable<T>](Iterable<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ReadonlySet<T> extends Iterable<T>--><!--Device-unnamed-export interface ReadonlySet<T> extends Iterable<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

Returns an iterable of [v, v] pairs for every value in the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlySet-entries(): IterableIterator<[T, T]>--><!--Device-ReadonlySet-entries(): IterableIterator<[T, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[T, T]&gt; | an iterable of [v, v] pairs. |

## forEach

```TypeScript
forEach(callbackfn: (value: T, value2: T, set: ReadonlySet<T>) => void): void
```

Executes a provided function once per each value in the Set object, in insertion order.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlySet-forEach(callbackfn: (value: T, value2: T, set: ReadonlySet<T>) => void): void--><!--Device-ReadonlySet-forEach(callbackfn: (value: T, value2: T, set: ReadonlySet<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, value2: T, set: ReadonlySet&lt;T&gt;) =&gt; void | 是 | the function to apply. |

## has

```TypeScript
has(value: T): boolean
```

Checks if a value is in the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlySet-has(value: T): boolean--><!--Device-ReadonlySet-has(value: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | the value to find in the Set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the value is in the Set. |

## keys

```TypeScript
keys(): IterableIterator<T>
```

Despite name, returns elements from the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlySet-keys(): IterableIterator<T>--><!--Device-ReadonlySet-keys(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | an iterable of the values in the Set. |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns elements from the Set.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlySet-values(): IterableIterator<T>--><!--Device-ReadonlySet-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | an iterable of the values in the Set. |

## size

```TypeScript
get size(): int
```

Returns the number of unique elements in the Set.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlySet-get size(): int--><!--Device-ReadonlySet-get size(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

