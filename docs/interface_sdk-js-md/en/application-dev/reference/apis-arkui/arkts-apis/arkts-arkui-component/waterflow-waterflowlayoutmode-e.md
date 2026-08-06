# WaterFlowLayoutMode

Declare layout modes of WaterFlow.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum WaterFlowLayoutMode--><!--Device-unnamed-export declare enum WaterFlowLayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_TOP_DOWN

```TypeScript
ALWAYS_TOP_DOWN = 0
```

Default layout mode where water flow items are arranged from top to bottom. Items in the viewport depend on the layout of all items above them.As such, in cases of redirection or switching the number of columns, the layout of all items above the viewport must be recalculated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowLayoutMode-ALWAYS_TOP_DOWN = 0--><!--Device-WaterFlowLayoutMode-ALWAYS_TOP_DOWN = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDING_WINDOW

```TypeScript
SLIDING_WINDOW = 1
```

Sliding window mode. This mode only takes into account the layout in the viewport,without depending on water flow items above the viewport.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ 1. During a non-animated redirection to a distant location, water flow items are laid out forward or backward based on the target position.If the user then swipes back to the position prior to the redirection, the layout of the content may not be consistent with its previous state.This can lead to misalignment of the top nodes when the user swipes back to the top after the redirection.To counteract this issue, in this layout mode, the layout will be automatically adjusted after reaching the top of the viewport to ensure that the top is aligned.If there are multiple sections, adjustments will be made to the sections within the viewport when scrolling ends.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_ 2. The total offset returned by the currentOffset API of scroller is inaccurate after a redirection or data update. This offset will be recalibrated when the user swipes back to the top.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ 3. If a jump action (for example, by calling scrollToIndex without animation or scrollEdge) and an input offset (such as from a swipe gesture or a scrolling animation) are both initiated within the same frame, both will be executed.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ 4. If the scrollToIndex API is called without animation to jump to a distant position (beyond the range of visible water flow items in the window),the total offset is calculated in the sliding window mode.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowLayoutMode-SLIDING_WINDOW = 1--><!--Device-WaterFlowLayoutMode-SLIDING_WINDOW = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

