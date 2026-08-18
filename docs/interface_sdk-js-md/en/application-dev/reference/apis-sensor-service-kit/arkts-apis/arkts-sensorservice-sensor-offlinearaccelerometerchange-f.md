# offLinearAccelerometerChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offLinearAccelerometerChange

```TypeScript
function offLinearAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void
```

Unsubscribe to linear acceleration sensor data, {@code SensorId.LINEAR_ACCELEROMETER}.

**Since:** 23

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function offLinearAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void--><!--Device-sensor-function offLinearAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | No | callback linear accelerometer data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

