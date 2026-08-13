# onPedometerDetectionChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onPedometerDetectionChange

```TypeScript
function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void
```

Subscribe to pedometer detection sensor data, {@code SensorId.PEDOMETER_DETECTION}.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void--><!--Device-sensor-function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
