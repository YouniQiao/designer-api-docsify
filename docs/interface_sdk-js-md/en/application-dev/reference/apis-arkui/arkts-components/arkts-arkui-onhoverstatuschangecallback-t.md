# OnHoverStatusChangeCallback

```TypeScript
declare type OnHoverStatusChangeCallback = (param: HoverEventParam) => void
```

当前设备的悬停状态改变时触发的回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnHoverStatusChangeCallback = (param: HoverEventParam) => void--><!--Device-unnamed-declare type OnHoverStatusChangeCallback = (param: HoverEventParam) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [HoverEventParam](arkts-arkui-hovereventparam-i.md) | Yes | 当前设备与悬停状态相关的参数，包括设备的折叠状态、悬停状态、应用方向以及窗口模式枚举。 |

