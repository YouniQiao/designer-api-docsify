# RingStyleOptions

环形无刻度样式选项。继承自[ScanEffectOptions](arkts-arkui-progress-scaneffectoptions-i.md)和[CommonProgressStyleOptions](arkts-arkui-progress-commonprogressstyleoptions-i.md)。

**继承/实现关系：** RingStyleOptions extends [ScanEffectOptions](arkts-arkui-progress-scaneffectoptions-i.md), [CommonProgressStyleOptions](arkts-arkui-progress-commonprogressstyleoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: boolean
```

进度条阴影开关。 true：表示打开进度条阴影；false：表示关闭进度条阴影。 默认值：false 。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status?: ProgressStatus
```

设置进度条状态。当设置为ProgressStatus.LOADING时会开启检查更新动效，此时设置进度值不生效。当从ProgressStatus.LOADING设置为ProgressStatus.PROGRESSING时，检查 更新动效会执行到终点再停止。 默认值：ProgressStatus.PROGRESSING。

**类型：** [ProgressStatus](arkts-arkui-progress-progressstatus-e.md)

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
