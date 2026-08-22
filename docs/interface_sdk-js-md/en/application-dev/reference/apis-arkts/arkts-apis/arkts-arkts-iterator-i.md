# Iterator

Iterator interface that defines a method to get the next value in a sequence

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export interface Iterator--><!--Device-unnamed-export interface Iterator-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## next

```TypeScript
next(): IteratorResult<T>
```

Returns the next result in the iterator

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Iterator-next(): IteratorResult<T>--><!--Device-Iterator-next(): IteratorResult<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-arkts-iterator-iteratorresult-c.md)&lt;T&gt; | An IteratorResult object containing the iteration status and value |

