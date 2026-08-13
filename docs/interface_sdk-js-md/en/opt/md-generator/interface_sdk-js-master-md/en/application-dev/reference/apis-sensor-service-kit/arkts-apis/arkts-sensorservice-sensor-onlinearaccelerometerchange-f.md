# onLinearAccelerometerChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onLinearAccelerometerChange

```TypeScript
function onLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>, options?: Options): void
```

Subscribe to linear acceleration sensor data, {@code SensorId.LINEAR_ACCELEROMETER}.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>, options?: Options): void--><!--Device-sensor-function onLinearAccelerometerChange(callback: Callback<LinearAccelerometerResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
