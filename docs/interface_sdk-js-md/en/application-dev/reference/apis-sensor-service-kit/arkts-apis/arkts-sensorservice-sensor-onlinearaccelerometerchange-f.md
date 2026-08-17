# onLinearAccelerometerChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## onLinearAccelerometerChange

```TypeScript
function onLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>, options?: Options): void
```

Subscribe to linear acceleration sensor data, {@code SensorId.LINEAR_ACCELEROMETER}.

**Since:** 23

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>, options?: Options): void--><!--Device-sensor-function onLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | Yes | callback linear accelerometer data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

