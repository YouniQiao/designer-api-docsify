# VibratorPattern

Defines the vibration sequence.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## events

```TypeScript
events: Array<VibratorEvent>
```

Vibration event array, which is the **VibratorPattern** object returned by **build() **.

**Type:** Array&lt;[VibratorEvent](arkts-sensorservice-vibrator-vibratorevent-i.md)&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Sensors.MiscDevice

## time

```TypeScript
time: int
```

Absolute vibration start time, in ms.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Sensors.MiscDevice
