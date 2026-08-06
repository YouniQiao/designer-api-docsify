# IterableIterator

An object that satisfies both Iterator and Iterable interfaces, meaning it is both an iterator and an iterable

**Inheritance/Implementation:** IterableIterator extends [Iterator<T>](Iterator<T>), [Iterable<T>](Iterable<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface IterableIterator<out T> extends Iterator<T>, Iterable<T>--><!--Device-unnamed-export interface IterableIterator<out T> extends Iterator<T>, Iterable<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns itself, since this object is itself an iterator

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IterableIterator-$_iterator(): IterableIterator<T>--><!--Device-IterableIterator-$_iterator(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; |  Returns this |

