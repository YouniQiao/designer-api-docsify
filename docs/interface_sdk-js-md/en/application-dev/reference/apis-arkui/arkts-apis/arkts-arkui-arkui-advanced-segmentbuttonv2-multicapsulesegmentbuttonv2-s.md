# MultiCapsuleSegmentButtonV2

Defines the segmented button with multi capsule style.

**Since:** 18

<!--Device-unnamed-export declare struct MultiCapsuleSegmentButtonV2--><!--Device-unnamed-export declare struct MultiCapsuleSegmentButtonV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

Sets the build function of the segmented button.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-build(): void--><!--Device-MultiCapsuleSegmentButtonV2-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndexes

```TypeScript
@Event
    $selectedIndexes: OnSelectedIndexesChange
```

Callback invoked when the selected item changes.

**Type:** [OnSelectedIndexesChange](arkts-arkui-onselectedindexeschange-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Event    $selectedIndexes: OnSelectedIndexesChange--><!--Device-MultiCapsuleSegmentButtonV2-@Event    $selectedIndexes: OnSelectedIndexesChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundBlurStyle

```TypeScript
@Param
    readonly itemBackgroundBlurStyle?: BlurStyle
```

Background blur style of segmented button items.

Default value: **undefined**

This property is read-only.

**Type:** BlurStyle

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyle?: BlurStyle--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundBlurStyleOptions

```TypeScript
@Param
    readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Background blur style options of segmented button items.

Default value: **undefined**

This property is read-only.

**Type:** BackgroundBlurStyleOptions

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundColor

```TypeScript
@Param
    readonly itemBackgroundColor?: ColorMetrics
```

Background color of unselected segmented button items.

Default value: **\$r('sys.color.segment_button_v2_multi_capsule_button_background')**

If the value is **undefined**, the default value is used.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundEffect

```TypeScript
@Param
    readonly itemBackgroundEffect?: BackgroundEffectOptions
```

Background effect of segmented button items.

Default value: **undefined**

This property is read-only.

**Type:** BackgroundEffectOptions

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundEffect?: BackgroundEffectOptions--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBackgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
@Param
    readonly itemBorderRadius?: LengthMetrics
```

Border radius of segmented button items.

Value range: [0, +∞)

Default value: **\$r('sys.float.segment_button_v2_selected_corner_radius')**.

If the value is out of the range, the default value is used.

This property is read-only.

**Type:** LengthMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontColor

```TypeScript
@Param
    readonly itemFontColor?: ColorMetrics
```

Font color of unselected segmented button items.

Default value: **\$r('sys.color.font_secondary')**

If the value is **undefined**, the default value is used.

**NOTE：**

When **fontColor** of **textModifier** is set for **items**, **itemFontColor** has no effect.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontSize

```TypeScript
@Param
    readonly itemFontSize?: LengthMetrics
```

Font size of unselected segmented button items.

Value range: [0, +∞)

Default value: **14fp**

**NOTE：**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemFontSize** has no effect.

This property is read-only.

**Type:** LengthMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemFontWeight

```TypeScript
@Param
    readonly itemFontWeight?: FontWeight
```

Font weight of unselected segmented button items.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE：**

When **fontWeight** of **textModifier** is set for **items**, **itemFontWeight** has no effect.

This property is read-only.

**Type:** FontWeight

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconFillColor

```TypeScript
@Param
    readonly itemIconFillColor?: ColorMetrics
```

Icon color of unselected segmented button items.

Default value: **\$r('sys.color.font_secondary')**

If the value is **undefined**, the default value is used.

**NOTE：**

When **fillColor** of **iconModifier** is set for **items**, **itemIconFillColor** has no effect.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemIconSize

```TypeScript
@Param
    readonly itemIconSize?: SizeT<LengthMetrics>
```

Image-type icon size of segmented button items.

Value range: [0, +∞)

Default value: **{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }**.

If the value is out of the range, the default value is used.

**NOTE：**

When **width** and **height** of **iconModifier** are set for **items**, **itemIconSize** has no effect.

This property is read-only.

**Type:** SizeT&lt;LengthMetrics&gt;

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemIconSize?: SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMaxFontScale

```TypeScript
@Param
    readonly itemMaxFontScale?: number | Resource
```

Maximum font scale factor of the segmented button item text.

Value range: [1, 2]

Default value: **1**

**NOTE：**

A value less than 1 is treated as **1**. A value greater than 2 is treated as **2**. Abnormal values are ineffective by default.

This property is read-only.

**Type:** number \| Resource

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMaxFontScale?: number | Resource--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMaxFontScale?: number | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinFontScale

```TypeScript
@Param
    readonly itemMinFontScale?: number | Resource
```

Minimum font scale factor of the segmented button item text.

Value range: [0, 1]

Default value: **0**

**NOTE：**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**. Abnormal values are ineffective by default.

This property is read-only.

**Type:** number \| Resource

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinFontScale?: number | Resource--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinFontScale?: number | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemMinHeight

```TypeScript
@Param
    readonly itemMinHeight?: LengthMetrics
```

Minimum height of the segmented button item.

Value range: [0, +∞)

Default value:

**\$r('sys.float.segment_button_v2_singleline_selected_height')** for text-only buttons and icon-only buttons, and **\$r('sys.float.segment_button_v2_doubleline_selected_height')** for buttons with both an icon and text.

If the value is out of the range, the default value is used.

This property is read-only.

**Type:** LengthMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemMinHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemPadding

```TypeScript
@Param
    readonly itemPadding?: LocalizedPadding
```

Padding of the segmented button item.

Default value: **{top: LengthMetrics.resource (\$r('sys.float.padding_level2')), bottom: LengthMetrics. resource (\$r('sys.float.padding_level2')), start: LengthMetrics.resource(\$r('sys.float.padding_level4')), end: LengthMetrics.resource(\$r('sys.float.padding_level4'))}**

If the value is **undefined**, the default value is used.

This property is read-only.

**Type:** LocalizedPadding

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
    @Param
    readonly items: SegmentButtonV2Items
```

Items of the segmented button.

If the value is **undefined**, the option information is not displayed.

This property is read-only.

**Type:** [SegmentButtonV2Items](arkts-arkui-arkui-advanced-segmentbuttonv2-segmentbuttonv2items-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items--><!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly items: SegmentButtonV2Items-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedBackgroundColor

```TypeScript
@Param
    readonly itemSelectedBackgroundColor?: ColorMetrics
```

Background color of the selected segmented button item.

Default value: **\$r('sys.color.segment_button_v2_tab_selected_item_background')**

If the value is **undefined**, the default value is used.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontColor

```TypeScript
@Param
    readonly itemSelectedFontColor?: ColorMetrics
```

Font color of the selected segmented button item.

Default value: **\$r('sys.color.font_primary')**.

If the value is **undefined**, the default value is used.

**NOTE：**

When **fontColor** of **textModifier** is set for **items**, **itemSelectedFontColor** has no effect.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontSize

```TypeScript
@Param
    readonly itemSelectedFontSize?: LengthMetrics
```

Font size of the selected segmented button item.

Value range: [0, +∞)

Default value: **14fp**

**NOTE：**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemSelectedFontSize** has no effect.

This property is read-only.

**Type:** LengthMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontWeight

```TypeScript
@Param
    readonly itemSelectedFontWeight?: FontWeight
```

Font weight of the selected segmented button item.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE：**

When **fontWeight** of **textModifier** is set for **items**, **itemSelectedFontWeight** has no effect.

This property is read-only.

**Type:** FontWeight

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedIconFillColor

```TypeScript
@Param
    readonly itemSelectedIconFillColor?: ColorMetrics
```

Icon color of the selected segmented button item.

Default value: **\$r('sys.color.font_primary')**

If the value is **undefined**, the default value is used.

**NOTE：**

When **fillColor** of **iconModifier** is set for **items**, **itemSelectedIconFillColor** has no effect.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedIconFillColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedSymbolFontColor

```TypeScript
@Param
    readonly itemSelectedSymbolFontColor?: ColorMetrics
```

HM Symbol icon color of the selected segmented button item.

Default value: **\$r('sys.color.font_primary')**

If the value is **undefined**, the default value is used.

**NOTE：**

When **fontColor** of **symbolModifier** is set for **items**, **itemSelectedSymbolFontColor** has no effect.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSelectedSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSpace

```TypeScript
@Param
    readonly itemSpace?: LengthMetrics
```

Space between segmented button items.

Value range: [0, +∞)

Default value: **LengthMetrics.vp(1)**

**NOTE：**

Percentage values are not supported. If an invalid value is set, the default value is used.

This property is read-only.

**Type:** LengthMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSpace?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontColor

```TypeScript
@Param
    readonly itemSymbolFontColor?: ColorMetrics
```

HM Symbol icon color of unselected segmented button items.

Default value: **\$r('sys.color.font_secondary')**

If the value is **undefined**, the default value is used.

**NOTE：**

When **fontColor** of **symbolModifier** is set for **items**, **itemSymbolFontColor** has no effect.

This property is read-only.

**Type:** ColorMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontSize

```TypeScript
@Param
    readonly itemSymbolFontSize?: LengthMetrics
```

HM Symbol icon size of segmented button items.

Value range: [0, +∞)

Default value: **20fp**

**NOTE：**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **symbolModifier** is set for **items**, **itemSymbolFontSize** has no effect.

This property is read-only.

**Type:** LengthMetrics

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly itemSymbolFontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## languageDirection

```TypeScript
@Param
    readonly languageDirection?: Direction
```

Language direction of the segmented button.

Default value: **Direction.Auto**

If the value is out of the range, the default value is used.

This property is read-only.

**Type:** Direction

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly languageDirection?: Direction--><!--Device-MultiCapsuleSegmentButtonV2-@Param    readonly languageDirection?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
@Event
    onItemClicked?: Callback<number>
```

Callback invoked when a segmented button item is clicked.

**Type:** Callback&lt;number&gt;

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Event    onItemClicked?: Callback<number>--><!--Device-MultiCapsuleSegmentButtonV2-@Event    onItemClicked?: Callback<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Require
    @Param
    readonly selectedIndexes: number[]
```

Array of indexes of the selected segmented button items. The index is zero-based and increments by 1.

If the value is **undefined**, no item is selected.

**NOTE：**

Only valid button indexes are supported. An empty array [] indicates no selection.

This property is read-only.

**Type:** number[]

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly selectedIndexes: number[]--><!--Device-MultiCapsuleSegmentButtonV2-@Require    @Param    readonly selectedIndexes: number[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

