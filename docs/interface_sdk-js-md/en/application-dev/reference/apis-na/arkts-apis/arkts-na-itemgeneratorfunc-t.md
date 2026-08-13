# ItemGeneratorFunc

```TypeScript
@Builder
declare type ItemGeneratorFunc<T> = (item: T, index: int) => void
```

Defines item generator function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderdeclare type ItemGeneratorFunc<T> = (item: T, index: int) => void--><!--Device-unnamed-@Builderdeclare type ItemGeneratorFunc<T> = (item: T, index: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | item in an array |
| index | int | Yes | index corresponding to an array item. |

