# offSensorStatusChange

## Modules to Import

```TypeScript
```

## offSensorStatusChange

```TypeScript
function offSensorStatusChange(callback?: Callback<SensorStatusEvent>): void
```

Stop listening on device status changes.

**Since:** 23

<!--Device-sensor-function offSensorStatusChange(callback?: Callback<SensorStatusEvent>): void--><!--Device-sensor-function offSensorStatusChange(callback?: Callback<SensorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SensorStatusEvent](arkts-sensorservice-sensor-sensorstatusevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
