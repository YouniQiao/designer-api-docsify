# HoverCallback

```TypeScript
export type HoverCallback = (isHover: boolean, event: HoverEvent) => void
```

Defines the callback type used in hover events. The value of isHover indicates whether the mouse is hovering over the component. The value of event contains information about HoverEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type HoverCallback = (isHover: boolean, event: HoverEvent) => void--><!--Device-unnamed-export type HoverCallback = (isHover: boolean, event: HoverEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isHover | boolean | Yes |  |
| event | [HoverEvent](arkts-na-common-hoverevent-i.md) | Yes |  |

