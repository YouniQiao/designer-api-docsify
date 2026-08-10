# VibratorPattern

马达振动序列，每个events代表一个振动事件。通过[VibratorPatternBuilder.build](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md#build)方法生成，作为  
[VibrateFromPattern](arkts-sensorservice-vibrator-vibratefrompattern-i.md)的pattern参数传入  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)接口触发振动。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorPattern--><!--Device-vibrator-interface VibratorPattern-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## events

```TypeScript
events: Array<VibratorEvent>
```

振动事件数组。由[VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md)的addContinuousEvent和addTransientEvent方法添加后通过build方法生成。同一VibratorPattern中多个VibratorEvent的time值不能重叠。

**Type:** Array&lt;VibratorEvent&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorPattern-events: Array<VibratorEvent>--><!--Device-VibratorPattern-events: Array<VibratorEvent>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## time

```TypeScript
time: int
```

振动绝对起始时间。单位：ms。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorPattern-time: int--><!--Device-VibratorPattern-time: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

