# onSarChange (System API)

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onSarChange

```TypeScript
function onSarChange(callback: Callback<SarResponse>, options?: Options): void
```

Subscribe to SAR sensor data, {@code SensorId.SAR}.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function onSarChange(callback: Callback<SarResponse>, options?: Options): void--><!--Device-sensor-function onSarChange(callback: Callback<SarResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
