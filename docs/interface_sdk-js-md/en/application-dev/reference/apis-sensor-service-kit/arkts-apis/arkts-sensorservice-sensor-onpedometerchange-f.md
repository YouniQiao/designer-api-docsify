# onPedometerChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onPedometerChange

```TypeScript
function onPedometerChange(callback: Callback<PedometerResponse>, options?: Options): void
```

Subscribe to pedometer sensor data, {@code SensorId.PEDOMETER}.

**Since:** 23

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function onPedometerChange(callback: Callback<PedometerResponse>, options?: Options): void--><!--Device-sensor-function onPedometerChange(callback: Callback<PedometerResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md)&gt; | Yes | callback pedometer data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

