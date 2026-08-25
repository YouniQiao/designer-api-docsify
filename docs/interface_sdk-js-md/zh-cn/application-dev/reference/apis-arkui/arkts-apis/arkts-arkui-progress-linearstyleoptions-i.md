# LinearStyleOptions

线性样式选项。继承自[ScanEffectOptions](arkts-arkui-progress-scaneffectoptions-i.md)和[CommonProgressStyleOptions](arkts-arkui-progress-commonprogressstyleoptions-i.md)。

**继承/实现关系：** LinearStyleOptions extends [ScanEffectOptions](arkts-arkui-progress-scaneffectoptions-i.md), [CommonProgressStyleOptions](arkts-arkui-progress-commonprogressstyleoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## strokeRadius

```TypeScript
strokeRadius?: PX | VP | LPX | Resource
```

设置线性进度条的圆角半径。 取值范围[0, strokeWidth / 2]。 默认值：strokeWidth / 2。

**类型：** [PX](arkts-arkui-px-t.md) \| [VP](arkts-arkui-vp-t.md) \| [LPX](arkts-arkui-lpx-t.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**默认值：** strokeWidth / 2

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Length
```

设置进度条宽度（不支持百分比设置）。 默认值：4vp。

**类型：** [Length](arkts-arkui-length-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
