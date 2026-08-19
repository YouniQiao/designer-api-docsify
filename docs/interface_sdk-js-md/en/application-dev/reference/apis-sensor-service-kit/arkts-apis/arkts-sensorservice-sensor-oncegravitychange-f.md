# onceGravityChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceGravityChange

```TypeScript
function onceGravityChange(callback: Callback<GravityResponse>): void
```

Subscribe to gravity sensor data once, {@code SensorId.GRAVITY}.

**Since:** 23

<!--Device-sensor-function onceGravityChange(callback: Callback<GravityResponse>): void--><!--Device-sensor-function onceGravityChange(callback: Callback<GravityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md)&gt; | Yes | callback gravity data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

