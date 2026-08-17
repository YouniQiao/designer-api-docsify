# onSarChange (System API)

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## onSarChange

```TypeScript
function onSarChange(callback: Callback<SarResponse>, options?: Options): void
```

Subscribe to SAR sensor data, {@code SensorId.SAR}.

**Since:** 23

<!--Device-sensor-function onSarChange(callback: Callback<SarResponse>, options?: Options): void--><!--Device-sensor-function onSarChange(callback: Callback<SarResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md)&gt; | Yes | callback sar data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission check failed. A non-system application uses the system API. |

