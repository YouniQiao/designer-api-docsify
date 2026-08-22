# OnMoveHandler

```TypeScript
export type OnMoveHandler = (from: int, to: int) => void
```

Defines the onMove callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnMoveHandler = (from: int, to: int) => void--><!--Device-unnamed-export type OnMoveHandler = (from: int, to: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | int | Yes | Index number for moving elements. |
| to | int | Yes | Target index number for moving elements. |

