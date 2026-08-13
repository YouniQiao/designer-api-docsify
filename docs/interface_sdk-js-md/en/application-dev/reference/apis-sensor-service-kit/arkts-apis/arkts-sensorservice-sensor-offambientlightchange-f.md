# offAmbientLightChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offAmbientLightChange

```TypeScript
function offAmbientLightChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void
```

Unsubscribe to ambient light sensor data, {@code SensorId.AMBIENT_LIGHT}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function offAmbientLightChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void--><!--Device-sensor-function offAmbientLightChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LightResponse&gt; | No | callback ambient light data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

