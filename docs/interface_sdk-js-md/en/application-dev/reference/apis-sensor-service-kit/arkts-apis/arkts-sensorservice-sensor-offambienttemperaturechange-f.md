# offAmbientTemperatureChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offAmbientTemperatureChange

```TypeScript
function offAmbientTemperatureChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void
```

Unsubscribe to ambient temperature sensor data， {@code SensorId.AMBIENT_TEMPERATURE}.

**Since:** 23

<!--Device-sensor-function offAmbientTemperatureChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void--><!--Device-sensor-function offAmbientTemperatureChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AmbientTemperatureResponse](arkts-sensorservice-sensor-ambienttemperatureresponse-i.md)&gt; | No | callback ambient temperature data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

