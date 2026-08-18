# onMagneticFieldChange

## Modules to Import

```TypeScript
```

## onMagneticFieldChange

```TypeScript
function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void
```

Subscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}.

**Since:** 23

<!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void--><!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
