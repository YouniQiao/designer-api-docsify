# onceAccelerometerChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceAccelerometerChange

```TypeScript
function onceAccelerometerChange(callback: Callback<AccelerometerResponse>): void
```

Subscribe to accelerometer sensor data once, {@code SensorId.ACCELEROMETER}.

**Since:** 23

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onceAccelerometerChange(callback: Callback<AccelerometerResponse>): void--><!--Device-sensor-function onceAccelerometerChange(callback: Callback<AccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | Yes | callback accelerometer data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

