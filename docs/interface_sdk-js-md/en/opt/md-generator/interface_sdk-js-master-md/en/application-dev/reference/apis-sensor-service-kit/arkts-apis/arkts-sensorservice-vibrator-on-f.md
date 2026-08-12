# on

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## on('vibratorStateChange')

```TypeScript
function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void
```

Enables listening for vibrator status changes.

**Since:** 19

<!--Device-vibrator-function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'vibratorStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-sensor-service-kit/errorcode-vibrator.md#14600101-device-operation-failed) |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Callback
const vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
  console.info('vibrator state callback info:', JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  // Subscribe to vibratorStateChange events.
  vibrator.on('vibratorStateChange', vibratorStateChangeCallback);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
