# ScrollToIndexOptions

```TypeScript
declare interface ScrollToIndexOptions
```

Provides parameters for scrolling to a specific index.

**Since:** 12

<!--Device-unnamed-declare interface ScrollToIndexOptions--><!--Device-unnamed-declare interface ScrollToIndexOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraOffset

```TypeScript
extraOffset?: LengthMetrics
```

Extra offset for scrolling to a specified index.

**Type:** LengthMetrics

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollToIndexOptions-extraOffset?: LengthMetrics--><!--Device-ScrollToIndexOptions-extraOffset?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fastScroll

```TypeScript
fastScroll?: FastScrollMode
```

Fast scroll mode used when scrolling to a specified index. When set to `SKIP_MEASURE`, intermediate child components are not measured. When set to `SKIP_CREATE_AND_MEASURE`, intermediate child components are neither created nor measured. Supported by `List`, `Grid`, and `WaterFlow` in `SLIDING_WINDOW` layout mode, and takes effect only when the `smooth` parameter of `scrollToIndex` is `true`. Default value: `FastScrollMode.NONE`, which is the same as not setting this parameter. Value range: `0`, `1`, and `2` defined in this enum. Other values are handled as `FastScrollMode.NONE`, without fast scroll optimization, and the remaining scroll parameters still take effect according to the original rules. The setting applies only to this call. The next call uses `NONE` if `fastScroll` is omitted.

For `Grid`, express special row or column placement through `GridLayoutOptions`. `SKIP_CREATE_AND_MEASURE` does not discover explicit placement specified only when creating a cold `GridItem`. This usage requirement does not change `SKIP_MEASURE` or `NONE`.

For `Grid`, retained items include those in the viewports at the start and end of the animation, items needed to determine the target's actual layout, and spanning items that overlap the target viewport.

For `SKIP_CREATE_AND_MEASURE`, configure complete row and column spans through [GridLayoutOptions](arkts-arkui-grid-comp-gridlayoutoptions-i.md) before requesting the scroll if any uncreated item's spans are unknown. The information must be available before the corresponding `GridItem` is created. In `GridLayoutOptions`, `regularSize` describes regular items' spans, `irregularIndexes` identifies irregular items, and `onGetIrregularSizeByIndex` supplies their spans. Follow the requirements documented for these fields. For custom positioning, follow the position and span requirements documented for `GridLayoutOptions.onGetRectByIndex`. Include every spanning item whose row or column occupancy affects the target position, even if the item is outside the target viewport. Providing only the target's spans is insufficient. Every span must match the actual content. This requirement concerns row and column occupancy, not measured pixel sizes.

This mode supports only inputs that meet this span requirement. No scrolling result is guaranteed for missing or inconsistent spans. The mode does not automatically fall back to another mode. The scroll request does not synchronously report arrival or a missing-span error. `SKIP_MEASURE` and `NONE` do not add this span requirement.

**Type:** [FastScrollMode](arkts-arkui-scroll-comp-fastscrollmode-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ScrollToIndexOptions-fastScroll?: FastScrollMode--><!--Device-ScrollToIndexOptions-fastScroll?: FastScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
