# Vibrator

**起始版本：** 3

**废弃版本：** 8

**替代接口：** [vibrator/vibrator](ohos.vibrator/vibrator)

**需要权限：** ohos.permission.VIBRATE

<!--Device-unnamed-export default class Vibrator--><!--Device-unnamed-export default class Vibrator-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice.Lite

## vibrate

```TypeScript
static vibrate(options?: VibrateOptions): void
```

触发设备振动，根据指定的振动模式执行短振动或长振动效果。该接口通过callback方式返回调用结果。

> **说明：**
> 
> 除Lite Wearable外，从API version 8开始，建议使用
> [vibrator.startVibration()](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)
> 替代。

**起始版本：** 3

**废弃版本：** 8

**替代接口：** [startVibration](@ohos.vibrator:vibrator.startVibration(effect:)

**需要权限：** ohos.permission.VIBRATE

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Vibrator-static vibrate(options?: VibrateOptions): void--><!--Device-Vibrator-static vibrate(options?: VibrateOptions): void-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [VibrateOptions](arkts-sensorservice-system-vibrator-vibrateoptions-i.md) | 否 |
