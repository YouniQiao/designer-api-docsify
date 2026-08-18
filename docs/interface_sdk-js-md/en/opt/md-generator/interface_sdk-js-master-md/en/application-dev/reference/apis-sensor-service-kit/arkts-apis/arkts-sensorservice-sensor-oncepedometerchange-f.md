# oncePedometerChange

## Modules to Import

```TypeScript
```

## oncePedometerChange

```TypeScript
function oncePedometerChange(callback: Callback<PedometerResponse>): void
```

Subscribe to pedometer sensor data once, {@code SensorId.PEDOMETER}.

**Since:** 23

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function oncePedometerChange(callback: Callback<PedometerResponse>): void--><!--Device-sensor-function oncePedometerChange(callback: Callback<PedometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
