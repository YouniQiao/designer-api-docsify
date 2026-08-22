# ChipGroupV2

Defines chipGroupV2.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare struct ChipGroupV2--><!--Device-unnamed-export declare struct ChipGroupV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

Build function for ChipGroupV2

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Builder  build(): void--><!--Device-ChipGroupV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $items

```TypeScript
@Event
  $items?: Callback<ChipGroupV2Items>
```

Two-way binding callback method for ChipV2 item.

**Type:** Callback&lt;[ChipGroupV2Items](arkts-arkuiadvancedchipgroupv2-chipgroupv2items-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Event  $items?: Callback<ChipGroupV2Items>--><!--Device-ChipGroupV2-@Event  $items?: Callback<ChipGroupV2Items>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndexes

```TypeScript
@Event
  $selectedIndexes?: Callback<Array<int>>
```

Two-way binding callback method for selected ChipV2 item indexes.

**Type:** Callback&lt;Array&lt;int&gt;&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Event  $selectedIndexes?: Callback<Array<int>>--><!--Device-ChipGroupV2-@Event  $selectedIndexes?: Callback<Array<int>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupPadding

```TypeScript
@Param
  chipGroupPadding?: ChipGroupV2Padding
```

ChipGroupV2 padding (only support top and bottom).

**Type:** [ChipGroupV2Padding](arkts-arkuiadvancedchipgroupv2-chipgroupv2padding-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Param  chipGroupPadding?: ChipGroupV2Padding--><!--Device-ChipGroupV2-@Param  chipGroupPadding?: ChipGroupV2Padding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupSpace

```TypeScript
@Param
  chipGroupSpace?: ChipGroupV2Space
```

Left and right inner margins and spacing between ChipV2

**Type:** [ChipGroupV2Space](arkts-arkuiadvancedchipgroupv2-chipgroupv2space-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Param  chipGroupSpace?: ChipGroupV2Space--><!--Device-ChipGroupV2-@Param  chipGroupSpace?: ChipGroupV2Space-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemStyle

```TypeScript
@Param
  itemStyle?: ChipGroupV2ItemStyle
```

ChipV2 item style.

**Type:** [ChipGroupV2ItemStyle](arkts-arkuiadvancedchipgroupv2-chipgroupv2itemstyle-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Param  itemStyle?: ChipGroupV2ItemStyle--><!--Device-ChipGroupV2-@Param  itemStyle?: ChipGroupV2ItemStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @Param
  items: ChipGroupV2Items
```

ChipV2 item.

**Type:** [ChipGroupV2Items](arkts-arkuiadvancedchipgroupv2-chipgroupv2items-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Require  @Param  items: ChipGroupV2Items--><!--Device-ChipGroupV2-@Require  @Param  items: ChipGroupV2Items-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiple

```TypeScript
@Param
  multiple?: boolean
```

Whether to select multiple ChipV2 items

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Param  multiple?: boolean--><!--Device-ChipGroupV2-@Param  multiple?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
@Event
  onChange?: Callback<Array<int>>
```

Chip group callback. when chipV2 status is changed, this onChange is called.

**Type:** Callback&lt;Array&lt;int&gt;&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Event  onChange?: Callback<Array<int>>--><!--Device-ChipGroupV2-@Event  onChange?: Callback<Array<int>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Param
  selectedIndexes?: Array<int>
```

Selected ChipV2 item indexes.

**Type:** Array&lt;int&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@Param  selectedIndexes?: Array<int>--><!--Device-ChipGroupV2-@Param  selectedIndexes?: Array<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffix

```TypeScript
@BuilderParam
  suffix?: ChipGroupV2SuffixBuilder
```

The builder function which will be rendered in the suffix of ChipGroupV2.

**Type:** [ChipGroupV2SuffixBuilder](arkts-chipgroupv2suffixbuilder-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroupV2-@BuilderParam  suffix?: ChipGroupV2SuffixBuilder--><!--Device-ChipGroupV2-@BuilderParam  suffix?: ChipGroupV2SuffixBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

