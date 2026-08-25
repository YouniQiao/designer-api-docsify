# BadgeParam

包含用于创建Badge组件的基础参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: BadgePosition | Position
```

设置提示点显示位置。 默认值：BadgePosition.RightTop。 undefined **说明：** 对于位置类型，不支持百分比值。 <br>如果设置了无效值，则使用默认值（0,0）。 表示组件的左上角，将使用。 <br>使用BadgePosition类型时，位置将基于方向属性进行镜像。

**类型：** [BadgePosition](arkts-arkui-badge-badgeposition-e.md) \| [Position](arkts-arkui-position-i.md)

**默认值：** BadgePosition.RightTop

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Badge组件可设置样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。

**类型：** [BadgeStyle](arkts-arkui-badge-badgestyle-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
