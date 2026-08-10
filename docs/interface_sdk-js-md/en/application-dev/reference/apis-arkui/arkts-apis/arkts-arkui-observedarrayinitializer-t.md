# ObservedArrayInitializer

```TypeScript
type ObservedArrayInitializer<T> = (index: int) => T
```

ObservedArray的元素初始化函数类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type ObservedArrayInitializer<T> = (index: int) => T--><!--Device-unnamed-type ObservedArrayInitializer<T> = (index: int) => T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前初始化元素的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 对应索引位置的元素值。 |

