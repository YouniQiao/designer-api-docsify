# offAccelerometerChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offAccelerometerChange

```TypeScript
function offAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void
```

Unsubscribe to accelerometer sensor data, {@code SensorId.ACCELEROMETER}.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function offAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void--><!--Device-sensor-function offAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
