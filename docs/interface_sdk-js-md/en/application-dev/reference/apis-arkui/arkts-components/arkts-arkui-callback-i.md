# Callback

定义基础的回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface Callback<T, V = void>--><!--Device-unnamed-declare interface Callback<T, V = void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(data: T): V
```

定义回调函数的信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Callback-(data: T): V--><!--Device-Callback-(data: T): V-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | 将会在回调函数中被使用的数据 |

**Return value:**

| Type | Description |
| --- | --- |
| V | 返回回调函数的结果。 |

