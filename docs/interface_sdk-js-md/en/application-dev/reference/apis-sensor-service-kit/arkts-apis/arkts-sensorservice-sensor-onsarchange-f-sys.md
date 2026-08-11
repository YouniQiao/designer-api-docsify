# onSarChange (System API)

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onSarChange

```TypeScript
function onSarChange(callback: Callback<SarResponse>, options?: Options): void
```

Subscribe to SAR sensor data, {@code SensorId.SAR}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onSarChange(callback: Callback<SarResponse>, options?: Options): void--><!--Device-sensor-function onSarChange(callback: Callback<SarResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SarResponse&gt; | Yes | callback sar data. |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission check failed. A non-system application uses the system API. |

