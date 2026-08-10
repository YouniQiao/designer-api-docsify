# Iterator

Iterator interface that defines a method to get the next value in a sequence

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Iterator<out T>--><!--Device-unnamed-export interface Iterator<out T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## next

```TypeScript
next(): IteratorResult<T>
```

Returns the next result in the iterator

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Iterator-next(): IteratorResult<T>--><!--Device-Iterator-next(): IteratorResult<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](arkts-arkts-iterator-iteratorresult-c.md)&lt;T&gt; | An IteratorResult object containing the iteration status and value |

