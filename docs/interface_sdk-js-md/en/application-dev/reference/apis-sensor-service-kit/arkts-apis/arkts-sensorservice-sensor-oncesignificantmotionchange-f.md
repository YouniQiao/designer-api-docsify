# onceSignificantMotionChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceSignificantMotionChange

```TypeScript
function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void
```

Subscribe to significant motion sensor data once, {@code SensorId.SIGNIFICANT_MOTION}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void--><!--Device-sensor-function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SignificantMotionResponse&gt; | Yes | callback significant motion data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

