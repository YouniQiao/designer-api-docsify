# offGyroscopeChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offGyroscopeChange

```TypeScript
function offGyroscopeChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void
```

Unsubscribe to gyroscope sensor data, {@code SensorId.GYROSCOPE}.

**Since:** 23

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function offGyroscopeChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void--><!--Device-sensor-function offGyroscopeChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;GyroscopeResponse&gt; | No | callback gyroscope data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

