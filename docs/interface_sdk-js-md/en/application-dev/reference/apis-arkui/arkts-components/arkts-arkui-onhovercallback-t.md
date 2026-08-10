# OnHoverCallback

```TypeScript
declare type OnHoverCallback = (status: boolean, event: HoverEvent) => void
```

鼠标悬浮触发回调。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-unnamed-declare type OnHoverCallback = (status: boolean, event: HoverEvent) => void--><!--Device-unnamed-declare type OnHoverCallback = (status: boolean, event: HoverEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | boolean | Yes | 表示鼠标是否悬浮在组件上。true表示鼠标悬浮在组件上，false表示鼠标离开组件。 |
| event | [HoverEvent](../arkts-apis/arkts-arkui-common-hoverevent-i.md) | Yes | 鼠标悬浮事件对象，包含悬浮事件的详细信息（如鼠标位置等）。 |

