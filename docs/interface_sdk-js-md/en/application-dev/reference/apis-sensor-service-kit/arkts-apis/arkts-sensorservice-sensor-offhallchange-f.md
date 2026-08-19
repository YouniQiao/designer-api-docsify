# offHallChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offHallChange

```TypeScript
function offHallChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void
```

Unsubscribe to hall sensor data, {@code SensorId.HALL}.

**Since:** 23

<!--Device-sensor-function offHallChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void--><!--Device-sensor-function offHallChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[HallResponse](arkts-sensorservice-sensor-hallresponse-i.md)&gt; | No | callback hall data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

