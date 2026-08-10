# ArrayLike

Represents an object that has a length property and can be indexed.

**Inheritance/Implementation:** ArrayLike extends [Iterable<T>](Iterable<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface ArrayLike<out T> extends Iterable<T>--><!--Device-unnamed-export interface ArrayLike<out T> extends Iterable<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(index: int): T
```

Gets the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayLike-$_get(index: int): T--><!--Device-ArrayLike-$_get(index: int): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The zero-based index of the element to get. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The element at the specified index. |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns an iterator for the elements in the ArrayLike object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayLike-$_iterator(): IterableIterator<T>--><!--Device-ArrayLike-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | An iterator instance. |

## length

```TypeScript
get length(): int
```

Get length of the ArrayLike.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayLike-get length(): int--><!--Device-ArrayLike-get length(): int-End-->

**System capability:** SystemCapability.Utils.Lang

