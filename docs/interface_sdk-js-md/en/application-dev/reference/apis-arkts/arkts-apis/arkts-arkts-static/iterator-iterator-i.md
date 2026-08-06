# Iterator

Iterator interface that defines a method to get the next value in a sequence

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface Iterator<out T>--><!--Device-unnamed-export interface Iterator<out T>-End-->

**System capability:** SystemCapability.Utils.Lang

## next

```TypeScript
next(): IteratorResult<T>
```

Returns the next result in the iterator

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Iterator-next(): IteratorResult<T>--><!--Device-Iterator-next(): IteratorResult<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; |  An IteratorResult object containing the iteration status and value |

