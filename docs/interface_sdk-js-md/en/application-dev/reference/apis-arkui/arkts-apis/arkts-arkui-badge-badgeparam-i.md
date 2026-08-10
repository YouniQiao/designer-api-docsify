# BadgeParam

包含用于创建Badge组件的基础参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BadgeParam--><!--Device-unnamed-export declare interface BadgeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: BadgePosition | Position
```

设置提示点显示位置。默认值：BadgePosition.RightTop。undefined  
**说明：**对于位置类型，不支持百分比值。&lt;br&gt;如果设置了无效值，则使用默认值（0,0）。表示组件的左上角，将使用。&lt;br&gt;使用BadgePosition类型时，位置将基于方向属性进行镜像。

**Type:** [BadgePosition](arkts-arkui-badge-badgeposition-e.md) \| Position

**Default:** BadgePosition.RightTop

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParam-position?: BadgePosition | Position--><!--Device-BadgeParam-position?: BadgePosition | Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Badge组件可设置样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。

**Type:** [BadgeStyle](../arkts-components/arkts-arkui-badgestyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParam-style: BadgeStyle--><!--Device-BadgeParam-style: BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

