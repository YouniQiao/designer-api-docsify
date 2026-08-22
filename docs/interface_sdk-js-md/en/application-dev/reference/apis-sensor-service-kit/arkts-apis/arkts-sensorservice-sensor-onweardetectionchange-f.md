# onWearDetectionChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onWearDetectionChange

```TypeScript
function onWearDetectionChange(callback: Callback<WearDetectionResponse>, options?: Options): void
```

Subscribe to wear detection sensor data, {@code SensorId.WEAR_DETECTION}.

**Since:** 23

<!--Device-sensor-function onWearDetectionChange(callback: Callback<WearDetectionResponse>, options?: Options): void--><!--Device-sensor-function onWearDetectionChange(callback: Callback<WearDetectionResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | Yes | callback wear detection data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

