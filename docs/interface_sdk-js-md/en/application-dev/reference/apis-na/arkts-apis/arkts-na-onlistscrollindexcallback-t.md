# OnListScrollIndexCallback

```TypeScript
export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void
```

Defines the callback type used in onScrollIndex.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void--><!--Device-unnamed-export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the first index in visible content. |
| end | int | Yes | the last index in visible content. |
| center | int | Yes | the center index in visible content. |

