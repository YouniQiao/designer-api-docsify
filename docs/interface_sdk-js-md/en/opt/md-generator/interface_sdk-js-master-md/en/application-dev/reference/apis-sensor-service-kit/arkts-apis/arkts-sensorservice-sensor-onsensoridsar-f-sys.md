# on_SensorId.SAR (System API)

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorId.SAR

```TypeScript
function on(type: SensorId.SAR, callback: Callback<SarResponse>, options?: Options): void
```

Subscribes to data of the Sodium Adsorption Ratio (SAR) sensor.

**Since:** 10

**Deprecated since:** -1

<!--Device-sensor-function on(type: SensorId.SAR, callback: Callback<SarResponse>, options?: Options): void--><!--Device-sensor-function on(type: SensorId.SAR, callback: Callback<SarResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorId.SAR | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
