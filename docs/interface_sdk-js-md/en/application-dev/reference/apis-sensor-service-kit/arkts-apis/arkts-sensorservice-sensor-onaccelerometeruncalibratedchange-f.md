# onAccelerometerUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onAccelerometerUncalibratedChange

```TypeScript
function onAccelerometerUncalibratedChange(callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void
```

Subscribe to uncalibrated accelerometer sensor data, {@code SensorId.ACCELEROMETER_UNCALIBRATED}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onAccelerometerUncalibratedChange(callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void--><!--Device-sensor-function onAccelerometerUncalibratedChange(callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AccelerometerUncalibratedResponse](arkts-sensorservice-sensor-accelerometeruncalibratedresponse-i.md)&gt; | Yes | callback uncalibrated accelerometer data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

