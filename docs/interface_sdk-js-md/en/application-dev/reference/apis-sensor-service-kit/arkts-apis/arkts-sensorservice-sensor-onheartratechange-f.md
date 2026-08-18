# onHeartRateChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onHeartRateChange

```TypeScript
function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void
```

Subscribe to heart rate sensor data, {@code SensorId.HEART_RATE}.

**Since:** 23

**Required permissions:** ohos.permission.READ_HEALTH_DATA

<!--Device-sensor-function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void--><!--Device-sensor-function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | Yes | callback heart rate data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

