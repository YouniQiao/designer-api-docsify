# offWearDetectionChange

## Modules to Import

```TypeScript
```

## offWearDetectionChange

```TypeScript
function offWearDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void
```

Unsubscribe to wear detection sensor data, {@code SensorId.WEAR_DETECTION}.

**Since:** 23

<!--Device-sensor-function offWearDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void--><!--Device-sensor-function offWearDetectionChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
