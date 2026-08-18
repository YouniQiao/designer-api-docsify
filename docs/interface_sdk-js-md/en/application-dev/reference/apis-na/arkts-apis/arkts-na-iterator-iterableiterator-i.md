# IterableIterator

An object that satisfies both Iterator and Iterable interfaces, meaning it is both an iterator and an iterable

**Inheritance/Implementation:** IterableIterator extends Iterator<T>, Iterable<T>

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface IterableIterator--><!--Device-unnamed-export interface IterableIterator-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns itself, since this object is itself an iterator

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IterableIterator-$_iterator(): IterableIterator<T>--><!--Device-IterableIterator-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-na-iterator-iterableiterator-i.md)&lt;T&gt; | Returns this |

