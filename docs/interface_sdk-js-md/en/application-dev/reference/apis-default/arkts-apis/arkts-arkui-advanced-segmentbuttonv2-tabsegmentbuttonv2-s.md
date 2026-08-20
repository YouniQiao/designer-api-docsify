# TabSegmentButtonV2

Defines segmented button with tab style.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct TabSegmentButtonV2--><!--Device-unnamed-export declare struct TabSegmentButtonV2-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Builder    build(): void--><!--Device-TabSegmentButtonV2-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndex

```TypeScript
@Event
    readonly $selectedIndex?: OnSelectedIndexChange
```

Sets the callback function which will be invoked when the selected index of the segmented button is changed.

**Type:** [OnSelectedIndexChange](arkts-onselectedindexchange-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Event    readonly $selectedIndex?: OnSelectedIndexChange--><!--Device-TabSegmentButtonV2-@Event    readonly $selectedIndex?: OnSelectedIndexChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundBlurStyle

```TypeScript
@Param
    readonly buttonBackgroundBlurStyle?: BlurStyle
```

Sets the background blur style of the segmented button.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyle?: BlurStyle--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundBlurStyleOptions

```TypeScript
@Param
    readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Sets the background blur style options of the segmented button.

**Type:** BackgroundBlurStyleOptions

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundColor

```TypeScript
@Param
    readonly buttonBackgroundColor?: ColorMetrics
```

Sets the background color of the segmented button.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundEffect

```TypeScript
@Param
    readonly buttonBackgroundEffect?: BackgroundEffectOptions
```

Sets the background effect of the segmented button.

**Type:** BackgroundEffectOptions

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundEffect?: BackgroundEffectOptions--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBorderRadius

```TypeScript
@Param
    readonly buttonBorderRadius?: LengthMetrics
```

Sets the border radius of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBorderRadius?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonMinHeight

```TypeScript
@Param
    readonly buttonMinHeight?: LengthMetrics
```

Sets the min height of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonMinHeight?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonMinHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonPadding

```TypeScript
@Param
    readonly buttonPadding?: LengthMetrics
```

Sets the padding of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonPadding?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonPadding?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableStateAnimation

```TypeScript
@Param
    readonly enableStateAnimation?: boolean
```

Enable animation when selectedIndexes change.

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly enableStateAnimation?: boolean--><!--Device-TabSegmentButtonV2-@Param    readonly enableStateAnimation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
@Param
    readonly itemBorderRadius?: LengthMetrics
```

Sets the border radius for all segmented button items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontColor

```TypeScript
@Param
    readonly itemFontColor?: ColorMetrics
```

Sets the font color for the text of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontSize

```TypeScript
@Param
    readonly itemFontSize?: LengthMetrics
```

Sets the font size for the text of all segmented button items that are not selected.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontWeight

```TypeScript
@Param
    readonly itemFontWeight?: FontWeight
```

Sets the font weight for the text of all segmented button items that are not selected.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight--><!--Device-TabSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconFillColor

```TypeScript
@Param
    readonly itemIconFillColor?: ColorMetrics
```

Sets the fill color for the icon of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconSize

```TypeScript
@Param
    readonly itemIconSize?: SizeT<LengthMetrics>
```

Sets the size for the icon of all segmented button items.

**Type:** SizeT&lt;LengthMetrics&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>--><!--Device-TabSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMaxFontScale

```TypeScript
@Param
    readonly itemMaxFontScale?: double | Resource
```

Sets the max font scale for all items of the segmented button.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemMaxFontScale?: double | Resource--><!--Device-TabSegmentButtonV2-@Param    readonly itemMaxFontScale?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinFontScale

```TypeScript
@Param
    readonly itemMinFontScale?: double | Resource
```

Sets the min font scale for all items of the segmented button.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemMinFontScale?: double | Resource--><!--Device-TabSegmentButtonV2-@Param    readonly itemMinFontScale?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinHeight

```TypeScript
@Param
    readonly itemMinHeight?: LengthMetrics
```

Sets the min height of all segmented button items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemPadding

```TypeScript
@Param
    readonly itemPadding?: LocalizedPadding
```

Sets the padding of all segmented button items.

**Type:** LocalizedPadding

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding--><!--Device-TabSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedBackgroundColor

```TypeScript
@Param
    readonly itemSelectedBackgroundColor?: ColorMetrics
```

Sets the background color for all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontColor

```TypeScript
@Param
    readonly itemSelectedFontColor?: ColorMetrics
```

Sets the font color for the text of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontSize

```TypeScript
@Param
    readonly itemSelectedFontSize?: LengthMetrics
```

Sets the font size for the text of all segmented button selected items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontWeight

```TypeScript
@Param
    readonly itemSelectedFontWeight?: FontWeight
```

Sets the font weight for the text of all segmented button selected items.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedIconFillColor

```TypeScript
@Param
    readonly itemSelectedIconFillColor?: ColorMetrics
```

Sets the fill color for the icon of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedSymbolFontColor

```TypeScript
@Param
    readonly itemSelectedSymbolFontColor?: ColorMetrics
```

Sets the font color for the symbol icon of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemShadow

```TypeScript
@Param
    readonly itemShadow?: ShadowOptions | ShadowStyle
```

Sets the shadow of all segmented button items.

**Type:** ShadowOptions \| ShadowStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemShadow?: ShadowOptions | ShadowStyle--><!--Device-TabSegmentButtonV2-@Param    readonly itemShadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSpace

```TypeScript
@Param
    readonly itemSpace?: LengthMetrics
```

Sets the space for all item of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontColor

```TypeScript
@Param
    readonly itemSymbolFontColor?: ColorMetrics
```

Sets the font color for the symbol icon of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontSize

```TypeScript
@Param
    readonly itemSymbolFontSize?: LengthMetrics
```

Sets the font size for the symbol icon of all segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
    @Param
    readonly items: SegmentButtonV2Items
```

Sets the items of the segmented button.

**Type:** [SegmentButtonV2Items](arkts-arkui-advanced-segmentbuttonv2-segmentbuttonv2items-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items--><!--Device-TabSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## languageDirection

```TypeScript
@Param
    readonly languageDirection?: Direction
```

Sets the language direction of the segmented button.

**Type:** Direction

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly languageDirection?: Direction--><!--Device-TabSegmentButtonV2-@Param    readonly languageDirection?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
@Event
    readonly onItemClicked?: Callback<int>
```

Sets the callback function which will be invoked when the item of the segmented button is clicked.

**Type:** Callback&lt;int&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Event    readonly onItemClicked?: Callback<int>--><!--Device-TabSegmentButtonV2-@Event    readonly onItemClicked?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
@Require
    @Param
    readonly selectedIndex: int
```

Sets the selected index of the segmented button. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Require    @Param    readonly selectedIndex: int--><!--Device-TabSegmentButtonV2-@Require    @Param    readonly selectedIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

