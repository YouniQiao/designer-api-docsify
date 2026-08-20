# VisibleAreaChangeCallback

```TypeScript
export type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: double) => void
```

Defines the callback type used in VisibleAreaChange events.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: double) => void--><!--Device-unnamed-export type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isExpanding | boolean | Yes | Indicates the ratio of the visible area to its own area compared to the last change. It is true as the ratio increases and false as the ratio decreases. |
| currentRatio | double | Yes | The value of currentRatio indicates the visibility ratio of the current component. |

