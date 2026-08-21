# ExpandedRegionLayoutOptions

展开态布局信息。

@interface ExpandedRegionLayoutOptions

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface ExpandedRegionLayoutOptions--><!--Device-unnamed-export interface ExpandedRegionLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## extraRegionPosition

```TypeScript
extraRegionPosition?: ExtraRegionPosition
```

扩展区域的位置信息。当isExtraRegionPerpendicular设置为false时，此字段生效。

**类型：** [ExtraRegionPosition](arkts-arkui-advanced-foldsplitcontainer-extraregionposition-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExpandedRegionLayoutOptions-extraRegionPosition?: ExtraRegionPosition--><!--Device-ExpandedRegionLayoutOptions-extraRegionPosition?: ExtraRegionPosition-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## horizontalSplitRatio

```TypeScript
horizontalSplitRatio?: PresetSplitRatio
```

主要区域与扩展区域之间的宽度比例。此字段在extra有效时生效。

**类型：** [PresetSplitRatio](arkts-arkui-advanced-foldsplitcontainer-presetsplitratio-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExpandedRegionLayoutOptions-horizontalSplitRatio?: PresetSplitRatio--><!--Device-ExpandedRegionLayoutOptions-horizontalSplitRatio?: PresetSplitRatio-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isExtraRegionPerpendicular

```TypeScript
isExtraRegionPerpendicular?: boolean
```

设置为true时，扩展区域从上到下贯穿整个组件；设置为false时，扩展区域不贯穿整个组件。 此字段仅在extra有效时生效。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExpandedRegionLayoutOptions-isExtraRegionPerpendicular?: boolean--><!--Device-ExpandedRegionLayoutOptions-isExtraRegionPerpendicular?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## verticalSplitRatio

```TypeScript
verticalSplitRatio?: PresetSplitRatio
```

主要区域与次要区域之间的高度比例。

**类型：** [PresetSplitRatio](arkts-arkui-advanced-foldsplitcontainer-presetsplitratio-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExpandedRegionLayoutOptions-verticalSplitRatio?: PresetSplitRatio--><!--Device-ExpandedRegionLayoutOptions-verticalSplitRatio?: PresetSplitRatio-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

