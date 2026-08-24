# SubHeader

子标题组件，用于列表项或内容项顶部，将该列表或内容划分为一个区块，子标题名称用来概括该区块内容。支持多种样式配置，包括图标、主副标题、下拉选择器和操作按钮等，可满足不同场景下的内容分区和导航需求，提升界面的信息层次感和用户体验。适用于 列表分组、内容分类展示、表单分区等场景。

> **说明：**&gt;
> - 该组件仅可在Stage模型下使用。&gt;
> - 如果SubHeader设置通用属性和通用事件，编译工具链会
> 额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到SubHeader本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SubHeader设置通用属性和
> 通用事件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Component

<!--Device-unnamed-export declare struct SubHeader--><!--Device-unnamed-export declare struct SubHeader-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@Builder  build(): void--><!--Device-SubHeader-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## contentMargin

```TypeScript
contentMargin?: LocalizedMargin
```

子标题外边距，不支持设置负数。默认值：`{start: LengthMetrics.resource(``\$r('sys.float.margin_left'))`,`end: LengthMetrics.resource(``\$r('sys.float.margin_right'))}`

**类型：** [LocalizedMargin](arkts-localizedmargin-t.md)

**默认值：** {start: LengthMetrics.resource($r('sys.float.margin_left')), <br> end: LengthMetrics.resource($r('sys.float.margin_right'))}

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  contentMargin?: LocalizedMargin--><!--Device-SubHeader-@PropRef  contentMargin?: LocalizedMargin-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## contentPadding

```TypeScript
contentPadding?: LocalizedPadding
```

子标题内边距，不支持设置负数。默认值：左侧为副标题或副标题加图标时：{start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)}。

**类型：** [LocalizedPadding](arkts-units-localizedpadding-i.md)

**默认值：** set different default values according to the width of the subHeader: <br> When the left area is secondaryTitle or the group of secondaryTitle and icon, <br> the default value is {start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)};

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  contentPadding?: LocalizedPadding--><!--Device-SubHeader-@PropRef  contentPadding?: LocalizedPadding-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

图标资源。默认值：undefined，表示不显示图标。当使用secondaryTitle属性时，设置icon属性才会生效。当同时使用primaryTitle、secondaryTitle、icon属性时，设置primaryTitle属性不生效。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  icon?: ResourceStr--><!--Device-SubHeader-@PropRef  icon?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconSymbolOptions

```TypeScript
iconSymbolOptions?: SymbolOptions
```

icon为SymbolGlyph时的设置项。默认值：undefined，表示不显示图标。

**类型：** [SymbolOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheader-symboloptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-iconSymbolOptions?: SymbolOptions--><!--Device-SubHeader-iconSymbolOptions?: SymbolOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## operationItem

```TypeScript
operationItem?: Array<OperationOption>
```

操作区（右侧）的设置项。当operationType为OperationType.ICON_GROUP时，最多支持配置三个图标项。默认值：undefined，表示不显示操作区。

**类型：** Array&lt;[OperationOption](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheader-operationoption-c.md)&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-operationItem?: Array<OperationOption>--><!--Device-SubHeader-operationItem?: Array<OperationOption>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## operationSymbolOptions

```TypeScript
operationSymbolOptions?: Array<SymbolOptions>
```

operationType为OperationType.ICON_GROUP，operationItem设置多个图标，图标为SymbolGlyph时的设置项。默认值：undefined，表示不设置Symbol图标。

**类型：** Array&lt;[SymbolOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheader-symboloptions-c.md)&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-operationSymbolOptions?: Array<SymbolOptions>--><!--Device-SubHeader-operationSymbolOptions?: Array<SymbolOptions>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## operationType

```TypeScript
operationType?: OperationType
```

操作区（右侧）元素样式。默认值：OperationType.BUTTON

**类型：** [OperationType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheader-operationtype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  operationType?: OperationType--><!--Device-SubHeader-@PropRef  operationType?: OperationType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
primaryTitle?: ResourceStr
```

主标题内容。默认值：undefined，表示不显示标题。当同时使用primaryTitle、secondaryTitle、icon属性时，设置primaryTitle属性不生效。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  primaryTitle?: ResourceStr--><!--Device-SubHeader-@PropRef  primaryTitle?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryTitleModifier

```TypeScript
primaryTitleModifier?: TextModifier
```

设置标题文本属性，如设置标题颜色、字体大小、字重等。默认值：undefined，表示使用系统默认样式。  
**说明：** 只有primaryTitle生效时，该参数才会生效。

**类型：** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-primaryTitleModifier?: TextModifier--><!--Device-SubHeader-primaryTitleModifier?: TextModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
secondaryTitle?: ResourceStr
```

副标题内容。默认值：undefined，表示不显示副标题。当同时使用primaryTitle、secondaryTitle、icon属性时，设置primaryTitle属性不生效。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  secondaryTitle?: ResourceStr--><!--Device-SubHeader-@PropRef  secondaryTitle?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitleModifier

```TypeScript
secondaryTitleModifier?: TextModifier
```

设置副标题文本属性，如设置标题颜色、字体大小、字重等。默认值：undefined，表示使用系统默认样式。

**类型：** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-secondaryTitleModifier?: TextModifier--><!--Device-SubHeader-secondaryTitleModifier?: TextModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## select

```TypeScript
select?: SelectOptions
```

下拉框内容和事件。默认值：undefined，表示不显示下拉框。

**类型：** [SelectOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheader-selectoptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-select?: SelectOptions--><!--Device-SubHeader-select?: SelectOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## titleAccessibilityText

```TypeScript
titleAccessibilityText?: ResourceStr
```

设置标题自定义朗读内容。默认值：undefined，表示不设置自定义朗读内容，默认朗读组件显示的标题内容。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  titleAccessibilityText?: ResourceStr--><!--Device-SubHeader-@PropRef  titleAccessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## titleBuilder

```TypeScript
titleBuilder?: () => void
```

自定义标题区内容。使用titleBuilder时，primaryTitle、secondaryTitle、icon等标题参数不生效。默认值：undefined，表示不使用自定义标题。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @BuilderParam

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@BuilderParam  titleBuilder?: () => void--><!--Device-SubHeader-@BuilderParam  titleBuilder?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## titleId

```TypeScript
titleId?: string
```

标题标识符。需要为标题设置id时使用此参数。默认值：undefined，表示不设置标题标识。

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeader-@PropRef  titleId?: string--><!--Device-SubHeader-@PropRef  titleId?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

