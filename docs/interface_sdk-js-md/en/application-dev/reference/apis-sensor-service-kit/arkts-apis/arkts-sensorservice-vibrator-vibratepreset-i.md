# VibratePreset

Represents the preset vibration effect. You can pass **VibratePreset** to  
[VibrateEffect9+](arkts-sensorservice-vibrator-vibrateeffect-t.md#VibrateEffect) to specify a preset vibration effect when calling  
[vibrator.startVibration9+](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)or [vibrator.startVibration9+](arkts-sensorservice-vibrator-startvibration-f.md#startVibration-1).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratePreset--><!--Device-vibrator-interface VibratePreset-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## count

```TypeScript
count?: int
```

Number of repeated vibrations. This parameter is optional. The default value is **1**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VibratePreset-count?: int--><!--Device-VibratePreset-count?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## effectId

```TypeScript
effectId: string
```

Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64characters are used.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VibratePreset-effectId: string--><!--Device-VibratePreset-effectId: string-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: int
```

Vibration intensity. This parameter is optional. The value range is [0, 100]. The default value is **100**. If vibration intensity adjustment is not supported, the default vibration intensity will be used.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-VibratePreset-intensity?: int--><!--Device-VibratePreset-intensity?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## type

```TypeScript
type: 'preset'
```

The value **preset** means that vibration is triggered based on the specified effect.

**Type:** 'preset'

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VibratePreset-type: 'preset'--><!--Device-VibratePreset-type: 'preset'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

