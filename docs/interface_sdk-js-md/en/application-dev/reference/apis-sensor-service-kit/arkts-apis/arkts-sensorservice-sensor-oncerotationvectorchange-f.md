# onceRotationVectorChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## onceRotationVectorChange

```TypeScript
function onceRotationVectorChange(callback: Callback<RotationVectorResponse>): void
```

Subscribe to rotation vector sensor data once, {@code SensorId.ROTATION_VECTOR}.

**Since:** 23

<!--Device-sensor-function onceRotationVectorChange(callback: Callback<RotationVectorResponse>): void--><!--Device-sensor-function onceRotationVectorChange(callback: Callback<RotationVectorResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationVectorResponse](arkts-sensorservice-sensor-rotationvectorresponse-i.md)&gt; | Yes | callback rotation vector data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

