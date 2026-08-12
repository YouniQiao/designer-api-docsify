# onceAccelerometerUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceAccelerometerUncalibratedChange

```TypeScript
function onceAccelerometerUncalibratedChange(callback: Callback<AccelerometerUncalibratedResponse>): void
```

Subscribe to uncalibrated accelerometer sensor data once, {@code SensorId.ACCELEROMETER_UNCALIBRATED}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onceAccelerometerUncalibratedChange(callback: Callback<AccelerometerUncalibratedResponse>): void--><!--Device-sensor-function onceAccelerometerUncalibratedChange(callback: Callback<AccelerometerUncalibratedResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AccelerometerUncalibratedResponse](arkts-sensorservice-sensor-accelerometeruncalibratedresponse-i.md)&gt; | Yes | callback uncalibrated accelerometer data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

