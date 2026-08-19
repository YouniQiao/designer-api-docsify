# onFusionPressureChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onFusionPressureChange

```TypeScript
function onFusionPressureChange(callback: Callback<FusionPressureResponse>, options?: Options): void
```

Subscribe to fusion pressure sensor data, {@code SensorId.FUSION_PRESSURE}.

**Since:** 23

<!--Device-sensor-function onFusionPressureChange(callback: Callback<FusionPressureResponse>, options?: Options): void--><!--Device-sensor-function onFusionPressureChange(callback: Callback<FusionPressureResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FusionPressureResponse](arkts-sensorservice-sensor-fusionpressureresponse-i.md)&gt; | Yes | callback fusion pressure percent data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

