# ItemGeneratorFunc

```TypeScript
declare type ItemGeneratorFunc<T> = (item: T, index: int) => void
```

Define item generator function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type ItemGeneratorFunc<T> = (item: T, index: int) => void--><!--Device-unnamed-declare type ItemGeneratorFunc<T> = (item: T, index: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | item in an array |
| index | int | Yes | index corresponding to an array item. 取值限定为整数。 |

