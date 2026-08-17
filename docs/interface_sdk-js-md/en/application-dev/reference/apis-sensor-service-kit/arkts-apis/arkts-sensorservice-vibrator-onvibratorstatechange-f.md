# onVibratorStateChange

## Modules to Import

```TypeScript
import { vibrator } from 'vibrator';
```

## onVibratorStateChange

```TypeScript
function onVibratorStateChange(callback: Callback<VibratorStatusEvent>): void
```

Register a callback function to be called when a vibrator plugin or unplug event occurs.

**Since:** 23

<!--Device-vibrator-function onVibratorStateChange(callback: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function onVibratorStateChange(callback: Callback<VibratorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | Yes | The callback function to be executed when <br> the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) | Device operation failed. |

