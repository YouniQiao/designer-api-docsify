# off

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## off('vibratorStateChange')

```TypeScript
function off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void
```

Disables listening for vibrator status changes.

**Since:** 19

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'vibratorStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) |
