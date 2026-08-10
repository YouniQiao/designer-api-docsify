# OnHoverStatusChangeCallback

```TypeScript
export type OnHoverStatusChangeCallback = (param: HoverEventParam) => void
```

当前设备的悬停状态改变时触发的回调。

Anonymous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnHoverStatusChangeCallback = (param: HoverEventParam) => void--><!--Device-unnamed-export type OnHoverStatusChangeCallback = (param: HoverEventParam) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [HoverEventParam](../arkts-components/arkts-arkui-hovereventparam-i.md) | Yes | 当前设备与悬停状态相关的参数，包括设备的折叠状态、 悬停状态、应用方向以及窗口模式枚举。 |

