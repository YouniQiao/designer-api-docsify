# onGyroscopeChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onGyroscopeChange

```TypeScript
function onGyroscopeChange(callback: Callback<GyroscopeResponse>, options?: Options): void
```

Subscribe to gyroscope sensor data, {@code SensorId.GYROSCOPE}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function onGyroscopeChange(callback: Callback<GyroscopeResponse>, options?: Options): void--><!--Device-sensor-function onGyroscopeChange(callback: Callback<GyroscopeResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GyroscopeResponse&gt; | Yes | callback gyroscope data. |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

