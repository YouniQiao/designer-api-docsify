# MultiCapsuleSegmentButtonV2

Defines the segmented button with capsule style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct MultiCapsuleSegmentButtonV2--><!--Device-unnamed-export declare struct MultiCapsuleSegmentButtonV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
    build(): void
```

Sets the build function of the segmented button.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Builder    build(): void--><!--Device-MultiCapsuleSegmentButtonV2-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndexes

```TypeScript
@Event
    readonly $selectedIndexes?: OnSelectedIndexesChange
```

Sets the callback function will be invoked when the selectedInexes field of the segmented button is changed.

**Type:** [OnSelectedIndexesChange](../../apis-arkui/arkts-apis/arkts-arkui-onselectedindexeschange-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Event    readonly $selectedIndexes?: OnSelectedIndexesChange--><!--Device-MultiCapsuleSegmentButtonV2-@Event    readonly $selectedIndexes?: OnSelectedIndexesChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundBlurStyle

```TypeScript
@Param
    readonly itemBackgroundBlurStyle?: BlurStyle
```

Sets the background blur style of all segmented button items that are not selected.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyle?: BlurStyle--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundBlurStyleOptions

```TypeScript
@Param
    readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Sets the background blur style options of all segmented button items that are not selected.

**Type:** BackgroundBlurStyleOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundColor

```TypeScript
@Param
    readonly itemBackgroundColor?: ColorMetrics
```

Sets the background color for all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundEffect

```TypeScript
@Param
    readonly itemBackgroundEffect?: BackgroundEffectOptions
```

Sets the background effect of all segmented button items that are not selected.

**Type:** BackgroundEffectOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundEffect?: BackgroundEffectOptions--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
@Param
    readonly itemBorderRadius?: LengthMetrics
```

Sets the border radius for all segmented button items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontColor

```TypeScript
@Param
    readonly itemFontColor?: ColorMetrics
```

Sets the font color for the text of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontSize

```TypeScript
@Param
    readonly itemFontSize?: LengthMetrics
```

Sets the font size for the text of all segmented button items that are not selected.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontWeight

```TypeScript
@Param
    readonly itemFontWeight?: FontWeight
```

Sets the font weight for the text of all segmented button items that are not selected.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconFillColor

```TypeScript
@Param
    readonly itemIconFillColor?: ColorMetrics
```

Sets the fill color for the icon of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconSize

```TypeScript
@Param
    readonly itemIconSize?: SizeT<LengthMetrics>
```

Sets the size for the icon of all segmented button items.

**Type:** SizeT&lt;LengthMetrics&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMaxFontScale

```TypeScript
@Param
    readonly itemMaxFontScale?: double | Resource
```

Sets the max font scale for all items of the segmented button.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMaxFontScale?: double | Resource--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMaxFontScale?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinFontScale

```TypeScript
@Param
    readonly itemMinFontScale?: double | Resource
```

Sets the min font scale for all items of the segmented button.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinFontScale?: double | Resource--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinFontScale?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinHeight

```TypeScript
@Param
    readonly itemMinHeight?: LengthMetrics
```

Sets the min height of all segmented button items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemPadding

```TypeScript
@Param
    readonly itemPadding?: LocalizedPadding
```

Sets the padding of all segmented button items.

**Type:** LocalizedPadding

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedBackgroundColor

```TypeScript
@Param
    readonly itemSelectedBackgroundColor?: ColorMetrics
```

Sets the background color for all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontColor

```TypeScript
@Param
    readonly itemSelectedFontColor?: ColorMetrics
```

Sets the font color for the text of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontSize

```TypeScript
@Param
    readonly itemSelectedFontSize?: LengthMetrics
```

Sets the font size for the text of all segmented button selected items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontWeight

```TypeScript
@Param
    readonly itemSelectedFontWeight?: FontWeight
```

Sets the font weight for the text of all segmented button selected items.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedIconFillColor

```TypeScript
@Param
    readonly itemSelectedIconFillColor?: ColorMetrics
```

Sets the fill color for the icon of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedSymbolFontColor

```TypeScript
@Param
    readonly itemSelectedSymbolFontColor?: ColorMetrics
```

Sets the font color for the symbol icon of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSpace

```TypeScript
@Param
    readonly itemSpace?: LengthMetrics
```

Sets the space for each item of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontColor

```TypeScript
@Param
    readonly itemSymbolFontColor?: ColorMetrics
```

Sets the font color for the symbol icon of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontSize

```TypeScript
@Param
    readonly itemSymbolFontSize?: LengthMetrics
```

Sets the font size for the symbol icon of all segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
    @Param
    readonly items: SegmentButtonV2Items
```

Sets the items of the segmented button.

**Type:** [SegmentButtonV2Items](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsegmentbuttonv2-segmentbuttonv2items-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items--><!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## languageDirection

```TypeScript
@Param
    readonly languageDirection?: Direction
```

Sets the language direction of the segmented button.

**Type:** Direction

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly languageDirection?: Direction--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly languageDirection?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
@Event
    readonly onItemClicked?: Callback<int>
```

Sets the callback function will be invoked when the item of the segmented button is clicked.

**Type:** Callback&lt;int&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Event    readonly onItemClicked?: Callback<int>--><!--Device-MultiCapsuleSegmentButtonV2-@Event    readonly onItemClicked?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Require
    @Param
    readonly selectedIndexes: int[]
```

Sets the selection of the segmented button.

**Type:** int[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly selectedIndexes: int[]--><!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly selectedIndexes: int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

