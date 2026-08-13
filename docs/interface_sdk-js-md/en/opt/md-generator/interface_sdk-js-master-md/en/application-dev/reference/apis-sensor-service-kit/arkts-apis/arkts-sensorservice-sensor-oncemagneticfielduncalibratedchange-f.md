# onceMagneticFieldUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceMagneticFieldUncalibratedChange

```TypeScript
function onceMagneticFieldUncalibratedChange(callback: Callback<MagneticFieldUncalibratedResponse>): void
```

Subscribe to uncalibrated magnetic field sensor data once, {@code SensorId.MAGNETIC_FIELD_UNCALIBRATED}.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function onceMagneticFieldUncalibratedChange(callback: Callback<MagneticFieldUncalibratedResponse>): void--><!--Device-sensor-function onceMagneticFieldUncalibratedChange(callback: Callback<MagneticFieldUncalibratedResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldUncalibratedResponse](arkts-sensorservice-sensor-magneticfielduncalibratedresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
