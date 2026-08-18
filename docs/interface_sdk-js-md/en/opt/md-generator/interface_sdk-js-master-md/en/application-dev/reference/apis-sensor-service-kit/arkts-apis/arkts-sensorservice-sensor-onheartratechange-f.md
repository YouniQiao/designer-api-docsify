# onHeartRateChange

## Modules to Import

```TypeScript
```

## onHeartRateChange

```TypeScript
function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void
```

Subscribe to heart rate sensor data, {@code SensorId.HEART_RATE}.

**Since:** 23

**Required permissions:** ohos.permission.READ_HEALTH_DATA

<!--Device-sensor-function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void--><!--Device-sensor-function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
