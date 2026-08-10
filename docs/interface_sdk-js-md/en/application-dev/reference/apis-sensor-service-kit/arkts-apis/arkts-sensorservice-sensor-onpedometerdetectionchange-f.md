# onPedometerDetectionChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onPedometerDetectionChange

```TypeScript
function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void
```

Subscribe to pedometer detection sensor data, {@code SensorId.PEDOMETER_DETECTION}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void--><!--Device-sensor-function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PedometerDetectionResponse&gt; | Yes | callback pedometer detection data. |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| 201 | Permission denied. |

