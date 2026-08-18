# once_SensorType.SENSOR_TYPE_ID_HUMIDITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_HUMIDITY

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>): void
```

Subscribes to only one data change of the humidity sensor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.HUMIDITY, callback: Callback&lt;HumidityResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HUMIDITY | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_HUMIDITY**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | Yes | One-shot callback used to return the humidity sensor data. The reported data type in the callback is **HumidityResponse**. |

