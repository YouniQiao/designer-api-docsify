# HoverModeRegionLayoutOptions

悬停态布局信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface HoverModeRegionLayoutOptions--><!--Device-unnamed-export interface HoverModeRegionLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## extraRegionPosition

```TypeScript
extraRegionPosition?: ExtraRegionPosition
```

扩展区域的位置信息，当且仅当showExtraRegion设置为true时此字段才生效。

**类型：** [ExtraRegionPosition](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-foldsplitcontainer-extraregionposition-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeRegionLayoutOptions-extraRegionPosition?: ExtraRegionPosition--><!--Device-HoverModeRegionLayoutOptions-extraRegionPosition?: ExtraRegionPosition-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## horizontalSplitRatio

```TypeScript
horizontalSplitRatio?: PresetSplitRatio
```

主要区域与扩展区域之间的宽度比例，当且仅当extra有效时此字段才生效。

**类型：** [PresetSplitRatio](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-foldsplitcontainer-presetsplitratio-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeRegionLayoutOptions-horizontalSplitRatio?: PresetSplitRatio--><!--Device-HoverModeRegionLayoutOptions-horizontalSplitRatio?: PresetSplitRatio-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## showExtraRegion

```TypeScript
showExtraRegion?: boolean
```

可折叠屏幕在半折叠状态下是否显示扩展区域。设置为true时表示显示扩展区域， 设置为false时表示不显示扩展区域。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeRegionLayoutOptions-showExtraRegion?: boolean--><!--Device-HoverModeRegionLayoutOptions-showExtraRegion?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

