# onceWearDetectionChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceWearDetectionChange

```TypeScript
function onceWearDetectionChange(callback: Callback<WearDetectionResponse>): void
```

Subscribe to wear detection sensor data once, {@code SensorId.WEAR_DETECTION}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onceWearDetectionChange(callback: Callback<WearDetectionResponse>): void--><!--Device-sensor-function onceWearDetectionChange(callback: Callback<WearDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WearDetectionResponse&gt; | Yes | callback wear detection data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

