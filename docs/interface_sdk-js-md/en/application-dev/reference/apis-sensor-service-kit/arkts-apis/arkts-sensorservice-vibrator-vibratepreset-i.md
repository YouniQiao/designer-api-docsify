# VibratePreset

```TypeScript
interface VibratePreset
```

Represents the preset vibration effect. When [vibrator.startVibration&lt;sup&gt;9+&lt;/sup&gt;](arkts-sensorservice-vibrator-startvibration-f.md) or [vibrator.startVibration&lt;sup&gt;9+&lt;/sup&gt;](arkts-sensorservice-vibrator-startvibration-f.md#startvibration-1) is called, the value of [VibrateEffect&lt;sup&gt;9+&lt;/sup&gt;](arkts-sensorservice-vibrator-vibrateeffect-t.md) can be **VibratePreset**, indicating that the preset vibration effect is triggered.

**Since:** 9

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## count

```TypeScript
count?: number
```

Number of repeated vibrations. This parameter is optional. The default value is **1**.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.MiscDevice

## effectId

```TypeScript
effectId: string
```

Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used.

**Type:** string

**Since:** 9

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: number
```

Vibration intensity. This parameter is optional. The value range is [0, 100]. The default value is **100**. If vibration intensity adjustment is not supported, the default vibration intensity will be used.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.Sensors.MiscDevice

## type

```TypeScript
type: 'preset'
```

The value **preset** means that vibration is triggered based on the specified effect.

**Type:** 'preset'

**Since:** 9

**System capability:** SystemCapability.Sensors.MiscDevice
