# KeyGeneratorFunc

```TypeScript
type KeyGeneratorFunc<T> = (item: T, index: int) => string
```

键值生成函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type KeyGeneratorFunc<T> = (item: T, index: int) => string--><!--Device-unnamed-type KeyGeneratorFunc<T> = (item: T, index: int) => string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | `arr`数组中的数据项。 |
| index | int | Yes | `arr`数组中的数据项索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | key value. |

