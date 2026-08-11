# MenuCallback

```TypeScript
export type MenuCallback = (start: int, end: int) => void
```

Callback function when the selection menu show or hide.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type MenuCallback = (start: int, end: int) => void--><!--Device-unnamed-export type MenuCallback = (start: int, end: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | Start offset of the selected content in rich editor. |
| end | int | Yes | End offset of the selected content in rich editor. |

