# onceGyroscopeChange

## Modules to Import

```TypeScript
```

## onceGyroscopeChange

```TypeScript
function onceGyroscopeChange(callback: Callback<GyroscopeResponse>): void
```

Subscribe to gyroscope sensor data once, {@code SensorId.GYROSCOPE}.

**Since:** 23

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function onceGyroscopeChange(callback: Callback<GyroscopeResponse>): void--><!--Device-sensor-function onceGyroscopeChange(callback: Callback<GyroscopeResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GyroscopeResponse&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
