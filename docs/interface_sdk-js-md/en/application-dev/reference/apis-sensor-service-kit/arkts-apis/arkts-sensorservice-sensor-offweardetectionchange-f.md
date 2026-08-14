# offWearDetectionChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## offWearDetectionChange

```TypeScript
function offWearDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void
```

Unsubscribe to wear detection sensor data, {@code SensorId.WEAR_DETECTION}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function offWearDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void--><!--Device-sensor-function offWearDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | No | callback wear detection data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

