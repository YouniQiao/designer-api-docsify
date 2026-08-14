# onHumidityChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## onHumidityChange

```TypeScript
function onHumidityChange(callback: Callback<HumidityResponse>, options?: Options): void
```

Subscribe to humidity sensor data, {@code SensorId.HUMIDITY}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function onHumidityChange(callback: Callback<HumidityResponse>, options?: Options): void--><!--Device-sensor-function onHumidityChange(callback: Callback<HumidityResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | Yes | callback humidity data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

