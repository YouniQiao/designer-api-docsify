# onceHeartRateChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceHeartRateChange

```TypeScript
function onceHeartRateChange(callback: Callback<HeartRateResponse>): void
```

Subscribe to heart rate sensor data once, {@code SensorId.HEART_RATE}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.READ_HEALTH_DATA

<!--Device-sensor-function onceHeartRateChange(callback: Callback<HeartRateResponse>): void--><!--Device-sensor-function onceHeartRateChange(callback: Callback<HeartRateResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | Yes | callback heart rate data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| 201 | Permission denied. |

