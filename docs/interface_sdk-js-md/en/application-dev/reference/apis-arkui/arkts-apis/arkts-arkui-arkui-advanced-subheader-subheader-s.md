# SubHeader

The **SubHeader** component is positioned at the top of list items or content sections, organizing lists or content into distinct groups. The subheader text summarizes the content within each respective section.

> **NOTE：**
> 
> - This component can be used only in the stage model.
> 
> - If the **SubHeader** component has universal attributes and &gt; universal events configured, the compiler toolchain automatically &gt; generates an additional **__Common__** node and mounts the universal attributes and universal events on this node &gt; rather than the **SubHeader** component itself. As a result, the configured universal attributes and universal &gt; events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events &gt; with the **SubHeader** component.

**Since:** 10

<!--Device-unnamed-export declare struct SubHeader--><!--Device-unnamed-export declare struct SubHeader-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OperationOption, OperationType, SelectOptions, SubHeader, SymbolOptions } from '@kit.ArkUI';
import { SubHeaderV2IconType, SubHeaderV2Title, SubHeaderV2Select, SubHeaderV2, SubHeaderV2OperationType, SubHeaderV2OperationItem, SubHeaderV2OperationItemType } from '@kit.ArkUI';
```

## contentMargin

```TypeScript
@Prop
  contentMargin?: LocalizedMargin
```

Margin of the content. Negative numbers are not supported.

Default value:

`{start: LengthMetrics.resource(`

`\$r('sys.float.margin_left'))`,

`end: LengthMetrics.resource(`

`\$r('sys.float.margin_right'))}`

**Type:** LocalizedMargin

**Default:** {start: LengthMetrics.resource($r('sys.float.margin_left')), <br> end: LengthMetrics.resource($r('sys.float.margin_right'))}

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-@Prop  contentMargin?: LocalizedMargin--><!--Device-SubHeader-@Prop  contentMargin?: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentPadding

```TypeScript
@Prop
  contentPadding?: LocalizedPadding
```

Padding of the content.

Default value:

If a secondary title, with or without an icon, is displayed on the left:

{start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)}

**Type:** LocalizedPadding

**Default:** set different default values according to the width of the subHeader: <br> When the left area is secondaryTitle or the group of secondaryTitle and icon, <br> the default value is {start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)};

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-@Prop  contentPadding?: LocalizedPadding--><!--Device-SubHeader-@Prop  contentPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
@Prop
  icon?: ResourceStr
```

Icon.

Default value: **undefined**, indicating that no icon is displayed.

The **icon** attribute takes effect only when the **secondaryTitle** attribute is used.

**Type:** ResourceStr

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubHeader-@Prop  icon?: ResourceStr--><!--Device-SubHeader-@Prop  icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconSymbolOptions

```TypeScript
iconSymbolOptions?: SymbolOptions
```

Icon symbol options. This parameter is available when **icon** is set to a symbol glyph.

Default value: **undefined**, indicating that no icon is displayed.

**Type:** [SymbolOptions](arkts-arkui-arkui-advanced-subheader-symboloptions-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-iconSymbolOptions?: SymbolOptions--><!--Device-SubHeader-iconSymbolOptions?: SymbolOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationItem

```TypeScript
operationItem?: Array<OperationOption>
```

Items in the operation area (right).

Default value: **undefined**, indicating that the operation area is not displayed.

**Type:** Array&lt;[OperationOption](arkts-arkui-arkui-advanced-subheader-operationoption-c.md)&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubHeader-operationItem?: Array<OperationOption>--><!--Device-SubHeader-operationItem?: Array<OperationOption>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationSymbolOptions

```TypeScript
operationSymbolOptions?: Array<SymbolOptions>
```

Icon symbol options.

This parameter is available when **operationType** is set to **OperationType.ICON_GROUP** and **operationItem** is set to an array of symbol glyphs.

Default value: **undefined**, indicating that no symbol icon is set.

**Type:** Array&lt;[SymbolOptions](arkts-arkui-arkui-advanced-subheader-symboloptions-c.md)&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-operationSymbolOptions?: Array<SymbolOptions>--><!--Device-SubHeader-operationSymbolOptions?: Array<SymbolOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationType

```TypeScript
@Prop
  operationType?: OperationType
```

Style of elements in the operation area (right).

Default value: **OperationType.BUTTON**

**Type:** [OperationType](arkts-arkui-arkui-advanced-subheader-operationtype-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubHeader-@Prop  operationType?: OperationType--><!--Device-SubHeader-@Prop  operationType?: OperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Prop
  primaryTitle?: ResourceStr
```

Primary title.

Default value: **undefined**, indicating that no primary title is displayed.

When the **primaryTitle**, **secondaryTitle**, and **icon** attributes are used simultaneously, the **primaryTitle** attribute will not take effect.

**Type:** ResourceStr

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubHeader-@Prop  primaryTitle?: ResourceStr--><!--Device-SubHeader-@Prop  primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitleModifier

```TypeScript
primaryTitleModifier?: TextModifier
```

Text attributes of the primary title, such as the font color, font size, and font weight.

Default value: **undefined**, indicating that the default style is used.

**Type:** [TextModifier](arkts-arkui-textmodifier-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-primaryTitleModifier?: TextModifier--><!--Device-SubHeader-primaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Prop
  secondaryTitle?: ResourceStr
```

Secondary title.

Default value: **undefined**, indicating that no secondary title is displayed.

**Type:** ResourceStr

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubHeader-@Prop  secondaryTitle?: ResourceStr--><!--Device-SubHeader-@Prop  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitleModifier

```TypeScript
secondaryTitleModifier?: TextModifier
```

Text attributes of the secondary title, such as the font color, font size, and font weight.

Default value: **undefined**, indicating that the default style is used.

**Type:** [TextModifier](arkts-arkui-textmodifier-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-secondaryTitleModifier?: TextModifier--><!--Device-SubHeader-secondaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## select

```TypeScript
select?: SelectOptions
```

Content and events for selection.

Default value: **undefined**, indicating that no drop-down list is displayed.

**Type:** [SelectOptions](arkts-arkui-arkui-advanced-subheader-selectoptions-c.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubHeader-select?: SelectOptions--><!--Device-SubHeader-select?: SelectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleAccessibilityText

```TypeScript
@Prop
  titleAccessibilityText?: ResourceStr
```

Customized content to be read in the title.

Default value: **undefined**.

If the value is **undefined**, the title content displayed by the component is read by default.

**Type:** ResourceStr

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SubHeader-@Prop  titleAccessibilityText?: ResourceStr--><!--Device-SubHeader-@Prop  titleAccessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleBuilder

```TypeScript
@BuilderParam
  titleBuilder?: () => void
```

Content of the custom title area.

Default value: **undefined**, indicating that no custom title is used.

**Type:** () =&gt; void

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubHeader-@BuilderParam  titleBuilder?: () => void--><!--Device-SubHeader-@BuilderParam  titleBuilder?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleId

```TypeScript
@Prop
  titleId?: string
```

Set the titleId for title.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-SubHeader-@Prop  titleId?: string--><!--Device-SubHeader-@Prop  titleId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

