# AccessibilityCallback

```TypeScript
export type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void
```

Defines the callback type used in accessibility hover events. The value of isHover indicates whether the touch is hovering over the component. The value of event contains information about AccessibilityHoverEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void--><!--Device-unnamed-export type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isHover | boolean | Yes |  |
| event | [AccessibilityHoverEvent](arkts-na-common-accessibilityhoverevent-i.md) | Yes |  |

