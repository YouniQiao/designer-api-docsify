# VibratorCurvePoint

Defines the gain relative to the vibration intensity.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-vibrator-interface VibratorCurvePoint--><!--Device-vibrator-interface VibratorCurvePoint-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## frequency

```TypeScript
frequency?: int
```

Change relative to the vibration frequency. This parameter is optional. The value range is [-100,100]. If this parameter is left empty, the default value is **0**.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VibratorCurvePoint-frequency?: int--><!--Device-VibratorCurvePoint-frequency?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: double
```

Gain relative to the vibration intensity. This parameter is optional. The value range is [0,100%]. If this parameter is left empty, the default value is **1**.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VibratorCurvePoint-intensity?: double--><!--Device-VibratorCurvePoint-intensity?: double-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## time

```TypeScript
time: int
```

Start time offset, in ms.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VibratorCurvePoint-time: int--><!--Device-VibratorCurvePoint-time: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

