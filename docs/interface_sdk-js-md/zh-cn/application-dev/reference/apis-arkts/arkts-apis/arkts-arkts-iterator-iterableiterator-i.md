# IterableIterator

An object that satisfies both Iterator and Iterable interfaces, meaning it is both an iterator and an iterable

**继承/实现关系：** IterableIterator extends [Iterator<T>](Iterator<T>), [Iterable<T>](Iterable<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface IterableIterator<out T> extends Iterator<T>, Iterable<T>--><!--Device-unnamed-export interface IterableIterator<out T> extends Iterator<T>, Iterable<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

Returns itself, since this object is itself an iterator

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IterableIterator-$_iterator(): IterableIterator<T>--><!--Device-IterableIterator-$_iterator(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | Returns this |

