# Vibrator

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [vibrator/vibrator](arkts-vibrator.md)

**Required permissions:** ohos.permission.VIBRATE

<!--Device-unnamed-export default class Vibrator--><!--Device-unnamed-export default class Vibrator-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## Modules to Import

```TypeScript
import { Vibrator, VibrateOptions } from '@kit.SensorServiceKit';
```

## vibrate

```TypeScript
static vibrate(options?: VibrateOptions): void
```

Triggers device vibration.

> **NOTE：**
> 
> Except for lite wearables. You are advised to use
> [vibrator.startVibration()](arkts-sensorservice-vibrator-startvibration-f.md) since API version 8.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md)(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

<!--Device-Vibrator-static vibrate(options?: VibrateOptions): void--><!--Device-Vibrator-static vibrate(options?: VibrateOptions): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [VibrateOptions](arkts-sensorservice-systemvibrator-vibrateoptions-i.md) | No | Vibration options. |

**Examples**

```TypeScript
import { Vibrator, VibrateOptions } from '@kit.SensorServiceKit';

let vibrateOptions: VibrateOptions = {
  mode: 'short',
  success: () => {
    console.info('Succeed in vibrating');
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to vibrate. Data: ${data}, code: ${code}`);
  },
  complete: () => {
    console.info('completed in vibrating');
  }
};
Vibrator.vibrate(vibrateOptions);
```

