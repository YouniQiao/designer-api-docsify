# onOrientationChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onOrientationChange

```TypeScript
function onOrientationChange(callback: Callback<OrientationResponse>, options?: Options): void
```

Subscribe to orientation sensor data, {@code SensorId.ORIENTATION}.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function onOrientationChange(callback: Callback<OrientationResponse>, options?: Options): void--><!--Device-sensor-function onOrientationChange(callback: Callback<OrientationResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
