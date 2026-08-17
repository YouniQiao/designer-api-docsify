# offPedometerDetectionChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## offPedometerDetectionChange

```TypeScript
function offPedometerDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void
```

Unsubscribe to pedometer detection sensor data, {@code SensorId.PEDOMETER_DETECTION}.

**Since:** 23

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function offPedometerDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function offPedometerDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | No | callback pedometer detection data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

