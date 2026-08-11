# Vibrator

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.vibrator/vibrator

**Required permissions:** ohos.permission.VIBRATE

<!--Device-unnamed-export default class Vibrator--><!--Device-unnamed-export default class Vibrator-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## Modules to Import

```TypeScript
import { VibrateOptions } from 'kits/@kit.SensorServiceKit';
```

## vibrate

```TypeScript
static vibrate(options?: VibrateOptions): void
```

Triggers device vibration.

> **NOTE：**
> 
> Except for lite wearables. You are advised to use
> [vibrator.startVibration()](arkts-sensorservice-vibrator-startvibration-f.md#startvibration) since API version 8.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [@ohos.vibrator:vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)(effect:

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

<!--Device-Vibrator-static vibrate(options?: VibrateOptions): void--><!--Device-Vibrator-static vibrate(options?: VibrateOptions): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [VibrateOptions](arkts-sensorservice-system-vibrator-vibrateoptions-i.md) | No |
