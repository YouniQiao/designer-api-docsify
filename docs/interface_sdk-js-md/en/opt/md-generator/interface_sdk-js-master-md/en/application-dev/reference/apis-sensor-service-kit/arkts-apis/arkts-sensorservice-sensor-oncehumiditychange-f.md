# onceHumidityChange

## Modules to Import

```TypeScript
```

## onceHumidityChange

```TypeScript
function onceHumidityChange(callback: Callback<HumidityResponse>): void
```

Subscribe to humidity sensor data once, {@code SensorId.HUMIDITY}.

**Since:** 23

<!--Device-sensor-function onceHumidityChange(callback: Callback<HumidityResponse>): void--><!--Device-sensor-function onceHumidityChange(callback: Callback<HumidityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
