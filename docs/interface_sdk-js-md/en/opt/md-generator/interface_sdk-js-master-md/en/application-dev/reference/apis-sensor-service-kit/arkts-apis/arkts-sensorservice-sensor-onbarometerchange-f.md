# onBarometerChange

## Modules to Import

```TypeScript
```

## onBarometerChange

```TypeScript
function onBarometerChange(callback: Callback<BarometerResponse>, options?: Options): void
```

Subscribe to barometer sensor data, {@code SensorId.BAROMETER}.

**Since:** 23

<!--Device-sensor-function onBarometerChange(callback: Callback<BarometerResponse>, options?: Options): void--><!--Device-sensor-function onBarometerChange(callback: Callback<BarometerResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BarometerResponse&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
