# ArcScrollIndexHandler

```TypeScript
export type ArcScrollIndexHandler = (start: int, end: int, center: int) => void
```

Called when the start, end and center positions of the display change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export type ArcScrollIndexHandler = (start: int, end: int, center: int) => void--><!--Device-unnamed-export type ArcScrollIndexHandler = (start: int, end: int, center: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start index of the display area. <br>The value should be an integer. |
| end | int | Yes | the end index of the display area. <br>The value should be an integer. |
| center | int | Yes | the center index of the display area. <br>The value should be an integer. |

