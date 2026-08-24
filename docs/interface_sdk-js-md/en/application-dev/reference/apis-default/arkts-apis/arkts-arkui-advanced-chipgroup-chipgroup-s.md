# ChipGroup

Defines chipGroup.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct ChipGroup--><!--Device-unnamed-export declare struct ChipGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@Builder  build(): void--><!--Device-ChipGroup-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundSystemMaterial

```TypeScript
backgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  backgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroup-@PropRef  backgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupPadding

```TypeScript
chipGroupPadding?: ChipGroupPaddingOptions
```

Chip group padding (only support top and bottom).

**Type:** [ChipGroupPaddingOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-chipgrouppaddingoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  chipGroupPadding?: ChipGroupPaddingOptions--><!--Device-ChipGroup-@PropRef  chipGroupPadding?: ChipGroupPaddingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupSpace

```TypeScript
chipGroupSpace?: ChipGroupSpaceOptions
```

Chip group space.

**Type:** [ChipGroupSpaceOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-chipgroupspaceoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  chipGroupSpace?: ChipGroupSpaceOptions--><!--Device-ChipGroup-@PropRef  chipGroupSpace?: ChipGroupSpaceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
items: ChipGroupItemOptions[]
```

Chip item.

**Type:** [ChipGroupItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-chipgroupitemoptions-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Require, @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@Require  @PropRef  items: ChipGroupItemOptions[]--><!--Device-ChipGroup-@Require  @PropRef  items: ChipGroupItemOptions[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemStyle

```TypeScript
itemStyle?: ChipItemStyle
```

Chip item style.

**Type:** [ChipItemStyle](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-chipitemstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  itemStyle?: ChipItemStyle--><!--Device-ChipGroup-@PropRef  itemStyle?: ChipItemStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiple

```TypeScript
multiple?: boolean
```

Support multiple chip item selection.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  multiple?: boolean--><!--Device-ChipGroup-@PropRef  multiple?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<Array<int>>
```

Chip group callback. when chip status is changed, this onChange is called.

**Type:** Callback&lt;Array&lt;int&gt;&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-onChange?: Callback<Array<int>>--><!--Device-ChipGroup-onChange?: Callback<Array<int>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundSystemMaterial

```TypeScript
selectedBackgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component when selected. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  selectedBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroup-@PropRef  selectedBackgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
selectedIndexes?: Array<int>
```

Default selected chip item indexes.

**Type:** Array&lt;int&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@PropRef  selectedIndexes?: Array<int>--><!--Device-ChipGroup-@PropRef  selectedIndexes?: Array<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffix

```TypeScript
suffix?: ChipGroupSuffixBuilder
```

The builder function which will be rendered in the suffix of ChipGroup.

**Type:** [ChipGroupSuffixBuilder](arkts-chipgroupsuffixbuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChipGroup-@BuilderParam  suffix?: ChipGroupSuffixBuilder--><!--Device-ChipGroup-@BuilderParam  suffix?: ChipGroupSuffixBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

