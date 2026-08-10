# VibrateFromPattern

自定义振动效果触发马达振动。适用于需要灵活组合振动事件的交互反馈场景（如表情包拟真效果、游戏场景/操作反馈）。与VibrateFromFile相比，VibrateFromFile是面向文件中提前定制好的效果，将振动事件以文件描述符形式传递；VibrateFromPattern提供更加灵活的振动事件排列组合，将振动事件以振动事件数组的形式传递。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibrateFromPattern--><!--Device-vibrator-interface VibrateFromPattern-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## pattern

```TypeScript
pattern: VibratorPattern
```

振动事件数组。由[VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md)的addContinuousEvent和addTransientEvent方法添加后通过build方法生成。同一VibratorPattern中多个VibratorEvent的time值不能重叠。

**Type:** [VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibrateFromPattern-pattern: VibratorPattern--><!--Device-VibrateFromPattern-pattern: VibratorPattern-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## type

```TypeScript
type: 'pattern'
```

值为'pattern'，根据组合模式触发马达振动。固定值，不可更改。

**Type:** 'pattern'

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibrateFromPattern-type: 'pattern'--><!--Device-VibrateFromPattern-type: 'pattern'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

