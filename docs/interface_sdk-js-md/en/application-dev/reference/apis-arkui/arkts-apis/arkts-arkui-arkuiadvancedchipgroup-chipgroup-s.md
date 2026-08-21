# ChipGroup


> **NOTE：**
> 
> 1. When **multiple** is set to **false**, if **selectedIndexes** is not passed in, the first chip is automatically
> selected by default. However, if the provided **selectedIndexes** includes multiple elements, the chip at the first
> index is selected by default.
> 
> 2. To use the suffix functionality, the **IconGroupSuffix** API must be imported. If this API is not provided, the
> suffix area will remain empty.
> 
> 3. The icon fill colors (**fillColor** and **activedFillColor**) must match the font color (**fontColor**). If
> different colors need to be set, use **prefixSymbol** when passing in
> [ChipGroupSpaceOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupspaceoptions-i.md).

**Since:** 12

<!--Device-unnamed-export declare struct ChipGroup--><!--Device-unnamed-export declare struct ChipGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## backgroundSystemMaterial

```TypeScript
@Prop
  backgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroup-@Prop  backgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroup-@Prop  backgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupPadding

```TypeScript
@Prop
  chipGroupPadding?: ChipGroupPaddingOptions
```

Top and bottom padding, used to control the overall height. The type is [ChipGroupPaddingOptions](arkts-arkui-arkuiadvancedchipgroup-chipgrouppaddingoptions-i.md).

Default value: { top: 14, bottom: 14 }

Unit: vp

If the value is **undefined**, the default value is used.

**Type:** [ChipGroupPaddingOptions](arkts-arkui-arkuiadvancedchipgroup-chipgrouppaddingoptions-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@Prop  chipGroupPadding?: ChipGroupPaddingOptions--><!--Device-ChipGroup-@Prop  chipGroupPadding?: ChipGroupPaddingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## chipGroupSpace

```TypeScript
@Prop
  chipGroupSpace?: ChipGroupSpaceOptions
```

Left and right padding and spacing between chips. For details, see [ChipGroupSpaceOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupspaceoptions-i.md).

Default value: { itemSpace: 8, startSpace: 16, endSpace: 16 }

Unit: vp

If the value is **undefined**, the default value is used.

**Type:** [ChipGroupSpaceOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupspaceoptions-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@Prop  chipGroupSpace?: ChipGroupSpaceOptions--><!--Device-ChipGroup-@Prop  chipGroupSpace?: ChipGroupSpaceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemStyle

```TypeScript
@Prop
  itemStyle?: ChipItemStyle
```

Style attributes of the chip, such as the color and size. For details, see [ChipItemStyle](arkts-arkui-arkuiadvancedchipgroup-chipitemstyle-i.md).

Default value:

{ size: ChipSize.NORMAL, backgroundColor: \$r('sys.color.ohos_id_color_button_normal'), fontColor: \$r(' sys.color.ohos_id_color_text_primary'), selectedFontColor: \$r('sys.color.ohos_id_color_text_primary_contrary'), selectedBackgroundColor: \$r('sys.color.ohos_id_color_emphasize') }

If the value is **undefined**, the default value is used.

**Type:** [ChipItemStyle](arkts-arkui-arkuiadvancedchipgroup-chipitemstyle-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@Prop  itemStyle?: ChipItemStyle--><!--Device-ChipGroup-@Prop  itemStyle?: ChipItemStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @Prop
  items: ChipGroupItemOptions[]
```

Specific attributes of each chip. For details, see [ChipGroupItemOptions[]][ChipGroupItemOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupitemoptions-i.md).

If the value is **undefined**, the **ChipGroup** component is empty by default.

**Type:** [ChipGroupItemOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupitemoptions-i.md)[]

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@Require  @Prop  items: ChipGroupItemOptions[]--><!--Device-ChipGroup-@Require  @Prop  items: ChipGroupItemOptions[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiple

```TypeScript
@Prop
  multiple?: boolean
```

Whether to select multiple chips.

**true**: Multiple chips can be selected. **false**: Only one chip can be selected.

Default value: **false**

If the value is **undefined**, the default value is used.

**Type:** boolean

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@Prop  multiple?: boolean--><!--Device-ChipGroup-@Prop  multiple?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<Array<number>>
```

Callback invoked when the chip status changes.

If the value is **undefined**, the event is unbound.

**Type:** Callback&lt;Array&lt;number&gt;&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-onChange?: Callback<Array<number>>--><!--Device-ChipGroup-onChange?: Callback<Array<number>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundSystemMaterial

```TypeScript
@Prop
  selectedBackgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component when selected. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroup-@Prop  selectedBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroup-@Prop  selectedBackgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Prop
  selectedIndexes?: Array<number>
```

Index of the selected chip.

Default value: **[0]**

If the value is **undefined**, the default value is used.

**Type:** Array&lt;number&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@Prop  selectedIndexes?: Array<number>--><!--Device-ChipGroup-@Prop  selectedIndexes?: Array<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffix

```TypeScript
@BuilderParam
  suffix?: Callback<void>
```

Callback used to customize a builder. To display custom content on the rightmost side of the component, configure the **suffix** property. Use of the **suffix** property requires referencing the [IconGroupSuffix](arkts-arkui-arkuiadvancedchipgroup-icongroupsuffix-s.md) API.

By default, if this parameter is not passed, there is no suffix.

If the value is **undefined**, there is no suffix.

**Type:** Callback&lt;void&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroup-@BuilderParam  suffix?: Callback<void>--><!--Device-ChipGroup-@BuilderParam  suffix?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

