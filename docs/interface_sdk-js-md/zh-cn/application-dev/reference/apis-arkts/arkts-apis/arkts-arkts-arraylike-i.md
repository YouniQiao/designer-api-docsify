# ArrayLike

Represents an object that has a length property and can be indexed.

**继承/实现关系：** ArrayLike extends [Iterable<T>](Iterable<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ArrayLike<out T> extends Iterable<T>--><!--Device-unnamed-export interface ArrayLike<out T> extends Iterable<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(index: int): T
```

Gets the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayLike-$_get(index: int): T--><!--Device-ArrayLike-$_get(index: int): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The zero-based index of the element to get. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The element at the specified index. |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns an iterator for the elements in the ArrayLike object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayLike-$_iterator(): IterableIterator<T>--><!--Device-ArrayLike-$_iterator(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | An iterator instance. |

## length

```TypeScript
get length(): int
```

Get length of the ArrayLike.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayLike-get length(): int--><!--Device-ArrayLike-get length(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

