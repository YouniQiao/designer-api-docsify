# getEffectInfoSync

## Modules to Import

```TypeScript
```

## getEffectInfoSync

```TypeScript
function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo
```

Obtains the preset vibration effect based on the device ID and vibrator ID to determine whether the preset vibration effect is supported.

**Since:** 23

<!--Device-vibrator-function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo--><!--Device-vibrator-function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effectId | string | Yes |
| param | [VibratorInfoParam](arkts-sensorservice-vibrator-vibratorinfoparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EffectInfo](arkts-sensorservice-vibrator-effectinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) |

**Examples**

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  const effectInfo: vibrator.EffectInfo = vibrator.getEffectInfoSync('haptic.clock.timer', { deviceId: 1, vibratorId: 3});
  console.info(`isEffectSupported: ${effectInfo.isEffectSupported}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
