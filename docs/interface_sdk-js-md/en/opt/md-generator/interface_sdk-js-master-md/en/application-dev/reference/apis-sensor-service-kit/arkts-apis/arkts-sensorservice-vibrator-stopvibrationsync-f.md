# stopVibrationSync

## Modules to Import

```TypeScript
```

## stopVibrationSync

```TypeScript
function stopVibrationSync(): void
```

Stops any form of motor vibration.

**Since:** 23

**Required permissions:** ohos.permission.VIBRATE

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-vibrator-function stopVibrationSync(): void--><!--Device-vibrator-function stopVibrationSync(): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) |

**Examples**

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Stop any form of vibration.
  vibrator.stopVibrationSync()
  console.info('Succeed in stopping vibration');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
