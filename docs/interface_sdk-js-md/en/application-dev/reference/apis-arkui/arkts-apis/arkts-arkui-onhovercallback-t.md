# OnHoverCallback

```TypeScript
export type OnHoverCallback = (status: boolean, event: HoverEvent) => void
```

鼠标悬浮触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnHoverCallback = (status: boolean, event: HoverEvent) => void--><!--Device-unnamed-export type OnHoverCallback = (status: boolean, event: HoverEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | boolean | Yes | 表示鼠标是否悬浮在组件上，鼠标进入组件时为true，离开组件时为false。 |
| event | [HoverEvent](../arkts-components/arkts-arkui-hoverevent-i.md) | Yes | 设置悬浮事件。 |

