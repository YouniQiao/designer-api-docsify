# onceLinearAccelerometerChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceLinearAccelerometerChange

```TypeScript
function onceLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>): void
```

Subscribe to linear acceleration sensor data once, {@code SensorId.LINEAR_ACCELEROMETER}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onceLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>): void--><!--Device-sensor-function onceLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LinearAccelerometerResponse&gt; | Yes | callback linear accelerometer data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

