# ChipGroupV2

定义ChipGroupV2。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare struct ChipGroupV2--><!--Device-unnamed-export declare struct ChipGroupV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

ChipGroupV2的build函数

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Builder  build(): void--><!--Device-ChipGroupV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $items

```TypeScript
@Event
  $items?: Callback<ChipGroupV2Items>
```

ChipV2项目的双向绑定回调方法。

**类型：** Callback&lt;[ChipGroupV2Items](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroupv2-chipgroupv2items-c.md)&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Event  $items?: Callback<ChipGroupV2Items>--><!--Device-ChipGroupV2-@Event  $items?: Callback<ChipGroupV2Items>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndexes

```TypeScript
@Event
  $selectedIndexes?: Callback<Array<int>>
```

双向绑定回调方法，为选中的ChipV2项目索引。

**类型：** Callback&lt;Array&lt;int&gt;&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Event  $selectedIndexes?: Callback<Array<int>>--><!--Device-ChipGroupV2-@Event  $selectedIndexes?: Callback<Array<int>>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## chipGroupPadding

```TypeScript
@Param
  chipGroupPadding?: ChipGroupV2Padding
```

设置ChipGroupV2的上下内边距

**类型：** [ChipGroupV2Padding](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroupv2-chipgroupv2padding-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Param  chipGroupPadding?: ChipGroupV2Padding--><!--Device-ChipGroupV2-@Param  chipGroupPadding?: ChipGroupV2Padding-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## chipGroupSpace

```TypeScript
@Param
  chipGroupSpace?: ChipGroupV2Space
```

左右内边距及ChipV2之间间距

**类型：** [ChipGroupV2Space](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroupv2-chipgroupv2space-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Param  chipGroupSpace?: ChipGroupV2Space--><!--Device-ChipGroupV2-@Param  chipGroupSpace?: ChipGroupV2Space-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemStyle

```TypeScript
@Param
  itemStyle?: ChipGroupV2ItemStyle
```

ChipV2项样式。

**类型：** [ChipGroupV2ItemStyle](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroupv2-chipgroupv2itemstyle-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Param  itemStyle?: ChipGroupV2ItemStyle--><!--Device-ChipGroupV2-@Param  itemStyle?: ChipGroupV2ItemStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @Param
  items: ChipGroupV2Items
```

每个ChipV2的特定属性

**类型：** [ChipGroupV2Items](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroupv2-chipgroupv2items-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Require  @Param  items: ChipGroupV2Items--><!--Device-ChipGroupV2-@Require  @Param  items: ChipGroupV2Items-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## multiple

```TypeScript
@Param
  multiple?: boolean
```

是否选中多个ChipV2

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Param  multiple?: boolean--><!--Device-ChipGroupV2-@Param  multiple?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
@Event
  onChange?: Callback<Array<int>>
```

ChipV2状态改变时的回调方法

**类型：** Callback&lt;Array&lt;int&gt;&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Event  onChange?: Callback<Array<int>>--><!--Device-ChipGroupV2-@Event  onChange?: Callback<Array<int>>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Param
  selectedIndexes?: Array<int>
```

选择的ChipV2索引。

**类型：** Array&lt;int&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@Param  selectedIndexes?: Array<int>--><!--Device-ChipGroupV2-@Param  selectedIndexes?: Array<int>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## suffix

```TypeScript
@BuilderParam
  suffix?: ChipGroupV2SuffixBuilder
```

将在ChipGroupV2的后缀中渲染的构建器函数。

**类型：** [ChipGroupV2SuffixBuilder](arkts-chipgroupv2suffixbuilder-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2-@BuilderParam  suffix?: ChipGroupV2SuffixBuilder--><!--Device-ChipGroupV2-@BuilderParam  suffix?: ChipGroupV2SuffixBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

