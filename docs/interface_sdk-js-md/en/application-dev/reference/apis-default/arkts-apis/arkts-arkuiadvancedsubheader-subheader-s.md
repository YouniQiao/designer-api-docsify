# SubHeader

The **SubHeader** component is positioned at the top of list items or content sections, organizing lists or content into distinct groups. The subheader text summarizes the content within each respective section.

> **NOTE：**
> 
> - This component can be used only in the stage model.
> 
> - If the **SubHeader** component has universal attributes and
> universal events configured, the compiler toolchain automatically
> generates an additional **__Common__** node and mounts the universal attributes and universal events on this node
> rather than the **SubHeader** component itself. As a result, the configured universal attributes and universal
> events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events
> with the **SubHeader** component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct SubHeader--><!--Device-unnamed-export declare struct SubHeader-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@Builder  build(): void--><!--Device-SubHeader-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentMargin

```TypeScript
@PropRef
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

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  contentMargin?: LocalizedMargin--><!--Device-SubHeader-@PropRef  contentMargin?: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentPadding

```TypeScript
@PropRef
  contentPadding?: LocalizedPadding
```

Padding of the content.

Default value:

If a secondary title, with or without an icon, is displayed on the left:

{start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)}

**Type:** LocalizedPadding

**Default:** set different default values according to the width of the subHeader: <br> When the left area is secondaryTitle or the group of secondaryTitle and icon, <br> the default value is {start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)};

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  contentPadding?: LocalizedPadding--><!--Device-SubHeader-@PropRef  contentPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
@PropRef
  icon?: ResourceStr
```

Icon.

Default value: **undefined**, indicating that no icon is displayed.

The **icon** attribute takes effect only when the **secondaryTitle** attribute is used.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  icon?: ResourceStr--><!--Device-SubHeader-@PropRef  icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconSymbolOptions

```TypeScript
iconSymbolOptions?: SymbolOptions
```

Icon symbol options. This parameter is available when **icon** is set to a symbol glyph.

Default value: **undefined**, indicating that no icon is displayed.

**Type:** [SymbolOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsubheader-symboloptions-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-iconSymbolOptions?: SymbolOptions--><!--Device-SubHeader-iconSymbolOptions?: SymbolOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationItem

```TypeScript
operationItem?: Array<OperationOption>
```

Items in the operation area (right).

Default value: **undefined**, indicating that the operation area is not displayed.

**Type:** Array&lt;[OperationOption](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsubheader-operationoption-c.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-operationItem?: Array<OperationOption>--><!--Device-SubHeader-operationItem?: Array<OperationOption>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationSymbolOptions

```TypeScript
operationSymbolOptions?: Array<SymbolOptions>
```

Icon symbol options.

This parameter is available when **operationType** is set to **OperationType.ICON_GROUP** and **operationItem** is set to an array of symbol glyphs.

Default value: **undefined**, indicating that no symbol icon is set.

**Type:** Array&lt;[SymbolOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsubheader-symboloptions-c.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-operationSymbolOptions?: Array<SymbolOptions>--><!--Device-SubHeader-operationSymbolOptions?: Array<SymbolOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationType

```TypeScript
@PropRef
  operationType?: OperationType
```

Style of elements in the operation area (right).

Default value: **OperationType.BUTTON**

**Type:** [OperationType](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsubheader-operationtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  operationType?: OperationType--><!--Device-SubHeader-@PropRef  operationType?: OperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@PropRef
  primaryTitle?: ResourceStr
```

Primary title.

Default value: **undefined**, indicating that no primary title is displayed.

When the **primaryTitle**, **secondaryTitle**, and **icon** attributes are used simultaneously, the **primaryTitle** attribute will not take effect.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  primaryTitle?: ResourceStr--><!--Device-SubHeader-@PropRef  primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitleModifier

```TypeScript
primaryTitleModifier?: TextModifier
```

Text attributes of the primary title, such as the font color, font size, and font weight.

Default value: **undefined**, indicating that the default style is used.

**Type:** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-primaryTitleModifier?: TextModifier--><!--Device-SubHeader-primaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@PropRef
  secondaryTitle?: ResourceStr
```

Secondary title.

Default value: **undefined**, indicating that no secondary title is displayed.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  secondaryTitle?: ResourceStr--><!--Device-SubHeader-@PropRef  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitleModifier

```TypeScript
secondaryTitleModifier?: TextModifier
```

Text attributes of the secondary title, such as the font color, font size, and font weight.

Default value: **undefined**, indicating that the default style is used.

**Type:** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-secondaryTitleModifier?: TextModifier--><!--Device-SubHeader-secondaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## select

```TypeScript
select?: SelectOptions
```

Content and events for selection.

Default value: **undefined**, indicating that no drop-down list is displayed.

**Type:** [SelectOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsubheader-selectoptions-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-select?: SelectOptions--><!--Device-SubHeader-select?: SelectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleAccessibilityText

```TypeScript
@PropRef
  titleAccessibilityText?: ResourceStr
```

Customized content to be read in the title.

Default value: **undefined**.

If the value is **undefined**, the title content displayed by the component is read by default.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  titleAccessibilityText?: ResourceStr--><!--Device-SubHeader-@PropRef  titleAccessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleBuilder

```TypeScript
@BuilderParam
  titleBuilder?: () => void
```

Content of the custom title area.

Default value: **undefined**, indicating that no custom title is used.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@BuilderParam  titleBuilder?: () => void--><!--Device-SubHeader-@BuilderParam  titleBuilder?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleId

```TypeScript
@PropRef
  titleId?: string
```

Set the id for the title.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeader-@PropRef  titleId?: string--><!--Device-SubHeader-@PropRef  titleId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

