# offRotationVectorChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## offRotationVectorChange

```TypeScript
function offRotationVectorChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void
```

Unsubscribe to rotation vector sensor data, {@code SensorId.ROTATION_VECTOR}.

**Since:** 23

<!--Device-sensor-function offRotationVectorChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void--><!--Device-sensor-function offRotationVectorChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationVectorResponse](arkts-sensorservice-sensor-rotationvectorresponse-i.md)&gt; | No | callback rotation vector data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

