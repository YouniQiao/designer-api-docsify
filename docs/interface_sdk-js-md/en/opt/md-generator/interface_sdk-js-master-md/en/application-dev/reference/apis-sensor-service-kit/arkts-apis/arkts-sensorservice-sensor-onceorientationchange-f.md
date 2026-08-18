# onceOrientationChange

## Modules to Import

```TypeScript
```

## onceOrientationChange

```TypeScript
function onceOrientationChange(callback: Callback<OrientationResponse>): void
```

Subscribe to orientation sensor data once, {@code SensorId.ORIENTATION}.

**Since:** 23

<!--Device-sensor-function onceOrientationChange(callback: Callback<OrientationResponse>): void--><!--Device-sensor-function onceOrientationChange(callback: Callback<OrientationResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
