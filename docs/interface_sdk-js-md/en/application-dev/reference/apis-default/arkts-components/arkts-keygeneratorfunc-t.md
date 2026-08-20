# KeyGeneratorFunc

```TypeScript
type KeyGeneratorFunc<T> = (item: T, index: int) => string
```

Defines key generator function.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type KeyGeneratorFunc<T> = (item: T, index: int) => string--><!--Device-unnamed-type KeyGeneratorFunc<T> = (item: T, index: int) => string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | data item. |
| index | int | Yes | data index in array. |

**Return value:**

| Type | Description |
| --- | --- |
| string | key value. |

