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

**Deprecated since:** -1

<!--Device-sensor-function offAmbientLightChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void--><!--Device-sensor-function offAmbientLightChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LightResponse&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
