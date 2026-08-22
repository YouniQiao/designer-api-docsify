# oncePedometerDetectionChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## oncePedometerDetectionChange

```TypeScript
function oncePedometerDetectionChange(callback: Callback<PedometerDetectionResponse>): void
```

Subscribe to pedometer detection sensor data once, {@code SensorId.PEDOMETER_DETECTION}.

**Since:** 23

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function oncePedometerDetectionChange(callback: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function oncePedometerDetectionChange(callback: Callback<PedometerDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | Yes | callback pedometer detection data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

