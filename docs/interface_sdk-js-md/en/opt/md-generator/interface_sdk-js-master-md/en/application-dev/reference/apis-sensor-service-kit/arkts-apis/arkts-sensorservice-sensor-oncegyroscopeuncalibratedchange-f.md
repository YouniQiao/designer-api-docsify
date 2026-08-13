# onceGyroscopeUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceGyroscopeUncalibratedChange

```TypeScript
function onceGyroscopeUncalibratedChange(callback: Callback<GyroscopeUncalibratedResponse>): void
```

Subscribe to uncalibrated gyroscope sensor data once, {@code SensorId.GYROSCOPE_UNCALIBRATED}.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function onceGyroscopeUncalibratedChange(callback: Callback<GyroscopeUncalibratedResponse>): void--><!--Device-sensor-function onceGyroscopeUncalibratedChange(callback: Callback<GyroscopeUncalibratedResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
