# OutlineOptions

外描边选项设置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface OutlineOptions--><!--Device-unnamed-export declare interface OutlineOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: EdgeColors | ResourceColor | LocalizedEdgeColors
```

设置外描边颜色。

默认值：Color.Black

**Type:** [EdgeColors](arkts-arkui-units-edgecolors-i.md) \| ResourceColor \| LocalizedEdgeColors

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OutlineOptions-color?: EdgeColors | ResourceColor | LocalizedEdgeColors--><!--Device-OutlineOptions-color?: EdgeColors | ResourceColor | LocalizedEdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: OutlineRadiuses | Dimension
```

设置外描边圆角半径，不支持百分比。

默认值：0

最大生效值：组件width/2 + outlineWidth或组件height/2 + outlineWidth。

**Type:** [OutlineRadiuses](arkts-arkui-units-outlineradiuses-i.md) \| Dimension

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OutlineOptions-radius?: OutlineRadiuses | Dimension--><!--Device-OutlineOptions-radius?: OutlineRadiuses | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: EdgeOutlineStyles | OutlineStyle
```

设置外描边样式。

默认值：OutlineStyle.SOLID

**Type:** [EdgeOutlineStyles](arkts-arkui-units-edgeoutlinestyles-i.md) \| OutlineStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OutlineOptions-style?: EdgeOutlineStyles | OutlineStyle--><!--Device-OutlineOptions-style?: EdgeOutlineStyles | OutlineStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: EdgeOutlineWidths | Dimension
```

设置外描边宽度，不支持百分比。

默认值：0，外描边效果中width为必设项，否则不显示外描边。

**Type:** [EdgeOutlineWidths](arkts-arkui-units-edgeoutlinewidths-i.md) \| Dimension

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OutlineOptions-width?: EdgeOutlineWidths | Dimension--><!--Device-OutlineOptions-width?: EdgeOutlineWidths | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

