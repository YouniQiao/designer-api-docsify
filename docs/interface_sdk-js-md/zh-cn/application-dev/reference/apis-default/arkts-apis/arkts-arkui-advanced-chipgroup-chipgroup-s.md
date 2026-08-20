# ChipGroup

ChipGroup组件提供操作块群组，用于文件或资源内容的分类等场景。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare struct ChipGroup--><!--Device-unnamed-export declare struct ChipGroup-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

build函数用于构造ChipGroup高级组件。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@Builder  build(): void--><!--Device-ChipGroup-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## backgroundSystemMaterial

```TypeScript
@PropRef
  backgroundSystemMaterial?: uiMaterial.Material
```

设置IconGroup后缀背景系统材质。

**类型：** uiMaterial.Material

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  backgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroup-@PropRef  backgroundSystemMaterial?: uiMaterial.Material-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## chipGroupPadding

```TypeScript
@PropRef
  chipGroupPadding?: ChipGroupPaddingOptions
```

设置ChipGroup的上下内边距，以控制整体高度。类型为[ChipGroupPaddingOptions](arkts-arkui-advanced-chipgroup-chipgrouppaddingoptions-i.md)。

默认值：{ top: 14, bottom: 14 }

单位：vp

值为undefined时，按默认值处理。

**类型：** [ChipGroupPaddingOptions](arkts-arkui-advanced-chipgroup-chipgrouppaddingoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  chipGroupPadding?: ChipGroupPaddingOptions--><!--Device-ChipGroup-@PropRef  chipGroupPadding?: ChipGroupPaddingOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## chipGroupSpace

```TypeScript
@PropRef
  chipGroupSpace?: ChipGroupSpaceOptions
```

左右内边距及Chip之间间距。参考[ChipGroupSpaceOptions](arkts-arkui-advanced-chipgroup-chipgroupspaceoptions-i.md)类型。

默认值：{ itemSpace: 8, startSpace: 16, endSpace: 16 }

单位：vp

值为undefined时，按默认值处理。

**类型：** [ChipGroupSpaceOptions](arkts-arkui-advanced-chipgroup-chipgroupspaceoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  chipGroupSpace?: ChipGroupSpaceOptions--><!--Device-ChipGroup-@PropRef  chipGroupSpace?: ChipGroupSpaceOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemStyle

```TypeScript
@PropRef
  itemStyle?: ChipItemStyle
```

`Chip`的`style`属性，如颜色，大小等，参考[ChipItemStyle](arkts-arkui-advanced-chipgroup-chipitemstyle-i.md)类型。

默认值：

{ size: ChipSize.NORMAL, backgroundColor: \$r('sys.color.ohos_id_color_button_normal'), fontColor: \$r(' sys.color.ohos_id_color_text_primary'), selectedFontColor: \$r('sys.color.ohos_id_color_text_primary_contrary'), selectedBackgroundColor: \$r('sys.color.ohos_id_color_emphasize') }

值为undefined时，按默认值处理。

**类型：** [ChipItemStyle](arkts-arkui-advanced-chipgroup-chipitemstyle-i.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  itemStyle?: ChipItemStyle--><!--Device-ChipGroup-@PropRef  itemStyle?: ChipItemStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @PropRef
  items: ChipGroupItemOptions[]
```

每个Chip的特定属性，参考 [ChipGroupItemOptions[]][ChipGroupItemOptions](arkts-arkui-advanced-chipgroup-chipgroupitemoptions-i.md)类型。

若为undefined时，ChipGroup默认为空。

**类型：** [ChipGroupItemOptions](arkts-arkui-advanced-chipgroup-chipgroupitemoptions-i.md)[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@Require  @PropRef  items: ChipGroupItemOptions[]--><!--Device-ChipGroup-@Require  @PropRef  items: ChipGroupItemOptions[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## multiple

```TypeScript
@PropRef
  multiple?: boolean
```

是否选中多个`Chip`。

`true`：支持多个`Chip`选中；`false`：仅支持单个`Chip`选中。

默认值：`false`

值为undefined时，按默认值处理。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  multiple?: boolean--><!--Device-ChipGroup-@PropRef  multiple?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<Array<int>>
```

Chip状态改变时的回调方法。

若为undefined，表示解绑事件。

**类型：** Callback&lt;Array&lt;int&gt;&gt;

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-onChange?: Callback<Array<int>>--><!--Device-ChipGroup-onChange?: Callback<Array<int>>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundSystemMaterial

```TypeScript
@PropRef
  selectedBackgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component when selected. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**类型：** uiMaterial.Material

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  selectedBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroup-@PropRef  selectedBackgroundSystemMaterial?: uiMaterial.Material-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@PropRef
  selectedIndexes?: Array<int>
```

被选中Chip的索引。

默认值：[0]

值为undefined时，按默认值处理。

**类型：** Array&lt;int&gt;

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@PropRef  selectedIndexes?: Array<int>--><!--Device-ChipGroup-@PropRef  selectedIndexes?: Array<int>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## suffix

```TypeScript
@BuilderParam
  suffix?: ChipGroupSuffixBuilder
```

支持开发者自定义builder，如需在组件最右侧显示自定义内容可配置suffix属性，使用属性suffix需引用[IconGroupSuffix](arkts-arkui-advanced-chipgroup-icongroupsuffix-s.md)接口。

默认不传入时，没有suffix。

值为undefined时，没有suffix。

**类型：** [ChipGroupSuffixBuilder](arkts-chipgroupsuffixbuilder-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroup-@BuilderParam  suffix?: ChipGroupSuffixBuilder--><!--Device-ChipGroup-@BuilderParam  suffix?: ChipGroupSuffixBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

