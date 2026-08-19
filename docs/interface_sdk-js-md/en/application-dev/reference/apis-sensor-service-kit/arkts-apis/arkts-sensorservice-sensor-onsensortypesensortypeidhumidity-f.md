# on_SensorType.SENSOR_TYPE_ID_HUMIDITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorType.SENSOR_TYPE_ID_HUMIDITY

```TypeScript
function on(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>,
    options?: Options): void
```

Subscribes to data changes of the humidity sensor. If this API is called multiple times for the same application, the last call takes effect.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)(type: SensorId.HUMIDITY, callback: Callback&lt;HumidityResponse&gt;, options?: Options)

<!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HUMIDITY | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_HUMIDITY**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | Yes | Callback used to return the humidity sensor data. The reported data type in the callback is **HumidityResponse**. |
| options | Options | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

