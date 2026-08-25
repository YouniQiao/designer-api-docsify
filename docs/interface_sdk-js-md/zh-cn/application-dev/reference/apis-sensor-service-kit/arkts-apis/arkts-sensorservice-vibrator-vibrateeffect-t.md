# VibrateEffect

```TypeScript
type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern
```

马达振动效果，支持以下四种：在调用 [vibrator.startVibration&lt;sup&gt;9+&lt;/sup&gt;](arkts-sensorservice-vibrator-startvibration-f.md) 或 [vibrator.startVibration&lt;sup&gt;9+&lt;/sup&gt;](arkts-sensorservice-vibrator-startvibration-f.md) 接口时，此参数的四种类型表示以四种不同的形式触发振动。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Sensors.MiscDevice

| 类型 |
| --- |
| [VibrateTime](arkts-sensorservice-vibrator-vibratetime-i.md) |
| [VibratePreset](arkts-sensorservice-vibrator-vibratepreset-i.md) |
| [VibrateFromFile](arkts-sensorservice-vibrator-vibratefromfile-i.md) |
| [VibrateFromPattern](arkts-sensorservice-vibrator-vibratefrompattern-i.md) |
