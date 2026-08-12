# offVibratorStateChange

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## offVibratorStateChange

```TypeScript
function offVibratorStateChange(callback?: Callback<VibratorStatusEvent>): void
```

Unregister a callback function for vibrator plugin or unplug events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-vibrator-function offVibratorStateChange(callback?: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function offVibratorStateChange(callback?: Callback<VibratorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | No | The callback function to be removed from the event listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14600101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-sensor-service-kit/errorcode-vibrator.md#14600101-device-operation-failed) | Device operation failed. |

