# VibratorEvent

Vibration event.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorEvent--><!--Device-vibrator-interface VibratorEvent-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## duration

```TypeScript
duration?: int
```

Vibration duration. This parameter is optional, in ms. The value range is (0,5000]. The default value is **48**for short vibration and **1000** for long vibration.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-duration?: int--><!--Device-VibratorEvent-duration?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## eventType

```TypeScript
eventType: VibratorEventType
```

Vibration event type.

**Type:** [VibratorEventType](arkts-sensorservice-vibrator-vibratoreventtype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-eventType: VibratorEventType--><!--Device-VibratorEvent-eventType: VibratorEventType-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## frequency

```TypeScript
frequency?: int
```

Vibration frequency. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the default value is **50**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-frequency?: int--><!--Device-VibratorEvent-frequency?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## index

```TypeScript
index?: int
```

Channel number. This parameter is optional. The value range is [0,2]. If this parameter is left empty, the default value is **0**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-index?: int--><!--Device-VibratorEvent-index?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: int
```

Vibration intensity. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the default value is **100**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-intensity?: int--><!--Device-VibratorEvent-intensity?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## points

```TypeScript
points?: Array<VibratorCurvePoint>
```

Adjustment points of the vibration curve.

**Type:** Array&lt;[VibratorCurvePoint](arkts-sensorservice-vibrator-vibratorcurvepoint-i.md)&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-points?: Array<VibratorCurvePoint>--><!--Device-VibratorEvent-points?: Array<VibratorCurvePoint>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## time

```TypeScript
time: int
```

Vibration start time, in ms. The value range is [0,1800000].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-time: int--><!--Device-VibratorEvent-time: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

