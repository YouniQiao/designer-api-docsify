# offProximityChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offProximityChange

```TypeScript
function offProximityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void
```

Unsubscribe to proximity sensor data, {@code SensorId.PROXIMITY}.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function offProximityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void--><!--Device-sensor-function offProximityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProximityResponse&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
