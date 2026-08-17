# OnHoverCallback

```TypeScript
export type OnHoverCallback = (status: boolean, event: HoverEvent) => void
```

callback of the on hover event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnHoverCallback = (status: boolean, event: HoverEvent) => void--><!--Device-unnamed-export type OnHoverCallback = (status: boolean, event: HoverEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | boolean | Yes | The hover status |
| event | [HoverEvent](../arkts-components/arkts-arkui-hoverevent-i.md) | Yes | The event info for hover. |

