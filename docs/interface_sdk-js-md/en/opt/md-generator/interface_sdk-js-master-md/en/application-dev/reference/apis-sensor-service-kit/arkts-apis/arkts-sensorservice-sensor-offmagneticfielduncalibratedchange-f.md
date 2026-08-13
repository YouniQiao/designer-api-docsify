# offMagneticFieldUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offMagneticFieldUncalibratedChange

```TypeScript
function offMagneticFieldUncalibratedChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void
```

Unsubscribe to uncalibrated magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD_UNCALIBRATED}.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function offMagneticFieldUncalibratedChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void--><!--Device-sensor-function offMagneticFieldUncalibratedChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldUncalibratedResponse](arkts-sensorservice-sensor-magneticfielduncalibratedresponse-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
