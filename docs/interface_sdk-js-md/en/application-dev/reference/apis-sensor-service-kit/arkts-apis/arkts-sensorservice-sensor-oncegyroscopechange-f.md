# onceGyroscopeChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceGyroscopeChange

```TypeScript
function onceGyroscopeChange(callback: Callback<GyroscopeResponse>): void
```

Subscribe to gyroscope sensor data once, {@code SensorId.GYROSCOPE}.

**Since:** 23

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function onceGyroscopeChange(callback: Callback<GyroscopeResponse>): void--><!--Device-sensor-function onceGyroscopeChange(callback: Callback<GyroscopeResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GyroscopeResponse&gt; | Yes | callback gyroscope data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

