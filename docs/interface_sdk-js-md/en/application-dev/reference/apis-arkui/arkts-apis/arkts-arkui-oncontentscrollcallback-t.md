# OnContentScrollCallback

```TypeScript
export type OnContentScrollCallback = (totalOffsetX: double, totalOffsetY: double) => void
```

Defines a TextInput callback when onContentScroll. Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnContentScrollCallback = (totalOffsetX: double, totalOffsetY: double) => void--><!--Device-unnamed-export type OnContentScrollCallback = (totalOffsetX: double, totalOffsetY: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalOffsetX | double | Yes | The text is offset in px on the horizontal axis of the content area. |
| totalOffsetY | double | Yes | The text is offset in px on the vertical axis of the content area. |

