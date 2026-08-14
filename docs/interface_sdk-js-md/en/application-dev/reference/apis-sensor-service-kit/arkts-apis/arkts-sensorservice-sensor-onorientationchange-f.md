# onOrientationChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## onOrientationChange

```TypeScript
function onOrientationChange(callback: Callback<OrientationResponse>, options?: Options): void
```

Subscribe to orientation sensor data, {@code SensorId.ORIENTATION}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function onOrientationChange(callback: Callback<OrientationResponse>, options?: Options): void--><!--Device-sensor-function onOrientationChange(callback: Callback<OrientationResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md)&gt; | Yes | callback orientation data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

