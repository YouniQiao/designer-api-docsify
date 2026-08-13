# isHdHapticSupported

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## isHdHapticSupported

```TypeScript
function isHdHapticSupported(): boolean
```

Checks whether HD vibration is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-vibrator-function isHdHapticSupported(): boolean--><!--Device-vibrator-function isHdHapticSupported(): boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether HD vibration is supported.
  let ret = vibrator.isHdHapticSupported();
  console.info(`The query result is ${ret}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
