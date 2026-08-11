# offHumidityChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## offHumidityChange

```TypeScript
function offHumidityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void
```

Unsubscribe to humidity sensor data, {@code SensorId.HUMIDITY}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function offHumidityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void--><!--Device-sensor-function offHumidityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HumidityResponse&gt; | No | callback humidity data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

