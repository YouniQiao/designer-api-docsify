# once_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void
```

Subscribes to only one data change of the ambient temperature sensor.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.AMBIENT_TEMPERATURE, callback: Callback&lt;AmbientTemperatureResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_AMBIENT_TEMPERATURE**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AmbientTemperatureResponse](arkts-sensorservice-sensor-ambienttemperatureresponse-i.md)&gt; | Yes | One-shot callback used to return the ambient temperature sensor data. The reported data type in the callback is **AmbientTemperatureResponse**. |

