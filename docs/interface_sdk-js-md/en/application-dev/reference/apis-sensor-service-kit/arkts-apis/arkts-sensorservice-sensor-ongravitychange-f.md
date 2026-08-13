# onGravityChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onGravityChange

```TypeScript
function onGravityChange(callback: Callback<GravityResponse>, options?: Options): void
```

Subscribe to gravity sensor data, {@code SensorId.GRAVITY}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function onGravityChange(callback: Callback<GravityResponse>, options?: Options): void--><!--Device-sensor-function onGravityChange(callback: Callback<GravityResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md)&gt; | Yes | callback gravity data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

