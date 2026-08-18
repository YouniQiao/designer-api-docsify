# onSignificantMotionChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onSignificantMotionChange

```TypeScript
function onSignificantMotionChange(callback: Callback<SignificantMotionResponse>, options?: Options): void
```

Subscribe to significant motion sensor data, {@code SensorId.SIGNIFICANT_MOTION}.

**Since:** 23

<!--Device-sensor-function onSignificantMotionChange(callback: Callback<SignificantMotionResponse>, options?: Options): void--><!--Device-sensor-function onSignificantMotionChange(callback: Callback<SignificantMotionResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SignificantMotionResponse](arkts-sensorservice-sensor-significantmotionresponse-i.md)&gt; | Yes | callback significant motion data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

