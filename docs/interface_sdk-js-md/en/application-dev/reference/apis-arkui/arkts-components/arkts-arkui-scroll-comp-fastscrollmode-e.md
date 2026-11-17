# FastScrollMode

```TypeScript
declare enum FastScrollMode
```

Enumerates the fast scroll modes for scrolling to a specified index, used with the `fastScroll` field of `ScrollToIndexOptions`.

> **NOTE:** 
> 
> - When the scroll distance is large and a jump is triggered, the component usually scrolls continuously for about 2 screens from the start position, then jumps to a position about 2 screens away from the final stop position and continues scrolling to the final position.One screen refers to the length of the visible area of the scrollable component in the scroll direction.
> - Skipping creation or measurement applies only to the skipped scroll path. Child components required by the two continuous scrolling segments before and after the skip are still created and measured on demand. The actual range also depends on the alignment, extra offset, child component size, and other factors, and is not fixed at 4 screens.
> - Fast scrolling does not guarantee that every child component along the scroll path is traversed and displayed.
> - If `fastScroll` is set to a value not defined in this enum, it is handled as `FastScrollMode.NONE`, and fast scroll optimization is not enabled. The remaining scroll parameters still take effect according to the original rules.

**Since:** 26.1.0

<!--Device-unnamed-declare enum FastScrollMode--><!--Device-unnamed-declare enum FastScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Uses the component's existing `scrollToIndex` behavior without fast scroll optimization.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-FastScrollMode-NONE = 0--><!--Device-FastScrollMode-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SKIP_CREATE_AND_MEASURE

```TypeScript
SKIP_CREATE_AND_MEASURE = 2
```

Skips creating and measuring intermediate items that displayed content and the target's actual layout do not require. For a multi-column `List` that contains both `ListItem` and `ListItemGroup`, use `SKIP_MEASURE`. For `WaterFlow`, this mode is recommended. In `SLIDING_WINDOW` layout mode, WaterFlow locates the target FlowItem without intermediate child components, while `SKIP_MEASURE` still creates intermediate child components along the path, causing extra creation overhead. For `Grid`, if the row or column spans of the target item or intermediate items are unknown, provide complete and accurate span information in advance through `GridLayoutOptions`.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-FastScrollMode-SKIP_CREATE_AND_MEASURE = 2--><!--Device-FastScrollMode-SKIP_CREATE_AND_MEASURE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SKIP_MEASURE

```TypeScript
SKIP_MEASURE = 1
```

Skips measuring intermediate items that displayed content and the target's actual layout do not require. The component may create intermediate items to determine which rows and columns they occupy. A multi-column `List` that contains both `ListItem` and `ListItemGroup` needs item types to determine rows. For `Grid`, intermediate `GridItem` components may be created to determine their row and column spans.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-FastScrollMode-SKIP_MEASURE = 1--><!--Device-FastScrollMode-SKIP_MEASURE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
