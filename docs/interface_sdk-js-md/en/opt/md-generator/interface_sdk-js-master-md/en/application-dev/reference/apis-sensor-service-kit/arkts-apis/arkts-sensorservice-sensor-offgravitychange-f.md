# offGravityChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offGravityChange

```TypeScript
function offGravityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void
```

Unsubscribe to gravity sensor data, {@code SensorId.GRAVITY}.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function offGravityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void--><!--Device-sensor-function offGravityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
