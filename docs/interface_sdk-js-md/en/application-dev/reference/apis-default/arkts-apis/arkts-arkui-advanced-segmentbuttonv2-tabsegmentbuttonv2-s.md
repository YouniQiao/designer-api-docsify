# TabSegmentButtonV2

Defines segmented button with tab style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct TabSegmentButtonV2--><!--Device-unnamed-export declare struct TabSegmentButtonV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
build(): void
```

Sets the build function of the segmented button.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Builder    build(): void--><!--Device-TabSegmentButtonV2-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndex

```TypeScript
readonly $selectedIndex?: OnSelectedIndexChange
```

Sets the callback function which will be invoked when the selected index of the segmented button is changed.

**Type:** [OnSelectedIndexChange](../../apis-arkui/arkts-apis/arkts-arkui-onselectedindexchange-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Event

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Event    readonly $selectedIndex?: OnSelectedIndexChange--><!--Device-TabSegmentButtonV2-@Event    readonly $selectedIndex?: OnSelectedIndexChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundBlurStyle

```TypeScript
readonly buttonBackgroundBlurStyle?: BlurStyle
```

Sets the background blur style of the segmented button.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyle?: BlurStyle--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundBlurStyleOptions

```TypeScript
readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Sets the background blur style options of the segmented button.

**Type:** BackgroundBlurStyleOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundColor

```TypeScript
readonly buttonBackgroundColor?: ColorMetrics
```

Sets the background color of the segmented button.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundEffect

```TypeScript
readonly buttonBackgroundEffect?: BackgroundEffectOptions
```

Sets the background effect of the segmented button.

**Type:** BackgroundEffectOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundEffect?: BackgroundEffectOptions--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBackgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonBorderRadius

```TypeScript
readonly buttonBorderRadius?: LengthMetrics
```

Sets the border radius of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonBorderRadius?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonMinHeight

```TypeScript
readonly buttonMinHeight?: LengthMetrics
```

Sets the min height of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonMinHeight?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonMinHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonPadding

```TypeScript
readonly buttonPadding?: LengthMetrics
```

Sets the padding of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly buttonPadding?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly buttonPadding?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableStateAnimation

```TypeScript
readonly enableStateAnimation?: boolean
```

Enable animation when selectedIndexes change.

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly enableStateAnimation?: boolean--><!--Device-TabSegmentButtonV2-@Param    readonly enableStateAnimation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
readonly itemBorderRadius?: LengthMetrics
```

Sets the border radius for all segmented button items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontColor

```TypeScript
readonly itemFontColor?: ColorMetrics
```

Sets the font color for the text of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontSize

```TypeScript
readonly itemFontSize?: LengthMetrics
```

Sets the font size for the text of all segmented button items that are not selected.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontWeight

```TypeScript
readonly itemFontWeight?: FontWeight
```

Sets the font weight for the text of all segmented button items that are not selected.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight--><!--Device-TabSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconFillColor

```TypeScript
readonly itemIconFillColor?: ColorMetrics
```

Sets the fill color for the icon of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconSize

```TypeScript
readonly itemIconSize?: SizeT<LengthMetrics>
```

Sets the size for the icon of all segmented button items.

**Type:** SizeT&lt;LengthMetrics&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>--><!--Device-TabSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMaxFontScale

```TypeScript
readonly itemMaxFontScale?: double | Resource
```

Sets the max font scale for all items of the segmented button.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemMaxFontScale?: double | Resource--><!--Device-TabSegmentButtonV2-@Param    readonly itemMaxFontScale?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinFontScale

```TypeScript
readonly itemMinFontScale?: double | Resource
```

Sets the min font scale for all items of the segmented button.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemMinFontScale?: double | Resource--><!--Device-TabSegmentButtonV2-@Param    readonly itemMinFontScale?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinHeight

```TypeScript
readonly itemMinHeight?: LengthMetrics
```

Sets the min height of all segmented button items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemPadding

```TypeScript
readonly itemPadding?: LocalizedPadding
```

Sets the padding of all segmented button items.

**Type:** LocalizedPadding

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding--><!--Device-TabSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
readonly items: SegmentButtonV2Items
```

Sets the items of the segmented button.

**Type:** [SegmentButtonV2Items](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbuttonv2-segmentbuttonv2items-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items--><!--Device-TabSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedBackgroundColor

```TypeScript
readonly itemSelectedBackgroundColor?: ColorMetrics
```

Sets the background color for all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontColor

```TypeScript
readonly itemSelectedFontColor?: ColorMetrics
```

Sets the font color for the text of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontSize

```TypeScript
readonly itemSelectedFontSize?: LengthMetrics
```

Sets the font size for the text of all segmented button selected items.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontWeight

```TypeScript
readonly itemSelectedFontWeight?: FontWeight
```

Sets the font weight for the text of all segmented button selected items.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedIconFillColor

```TypeScript
readonly itemSelectedIconFillColor?: ColorMetrics
```

Sets the fill color for the icon of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedSymbolFontColor

```TypeScript
readonly itemSelectedSymbolFontColor?: ColorMetrics
```

Sets the font color for the symbol icon of all segmented button selected items.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemShadow

```TypeScript
readonly itemShadow?: ShadowOptions | ShadowStyle
```

Sets the shadow of all segmented button items.

**Type:** ShadowOptions \| ShadowStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemShadow?: ShadowOptions | ShadowStyle--><!--Device-TabSegmentButtonV2-@Param    readonly itemShadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSpace

```TypeScript
readonly itemSpace?: LengthMetrics
```

Sets the space for all item of the segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontColor

```TypeScript
readonly itemSymbolFontColor?: ColorMetrics
```

Sets the font color for the symbol icon of all segmented button items that are not selected.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontSize

```TypeScript
readonly itemSymbolFontSize?: LengthMetrics
```

Sets the font size for the symbol icon of all segmented button.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## languageDirection

```TypeScript
readonly languageDirection?: Direction
```

Sets the language direction of the segmented button.

**Type:** Direction

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Param    readonly languageDirection?: Direction--><!--Device-TabSegmentButtonV2-@Param    readonly languageDirection?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
readonly onItemClicked?: Callback<int>
```

Sets the callback function which will be invoked when the item of the segmented button is clicked.

**Type:** Callback&lt;int&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Event

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Event    readonly onItemClicked?: Callback<int>--><!--Device-TabSegmentButtonV2-@Event    readonly onItemClicked?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
readonly selectedIndex: int
```

Sets the selected index of the segmented button. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabSegmentButtonV2-@Require    @Param    readonly selectedIndex: int--><!--Device-TabSegmentButtonV2-@Require    @Param    readonly selectedIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

