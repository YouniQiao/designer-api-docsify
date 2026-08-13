# off_SensorType.SENSOR_TYPE_ID_HUMIDITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_HUMIDITY

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback?: Callback<HumidityResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.HUMIDITY, callback?: Callback&lt;HumidityResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback?: Callback<HumidityResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback?: Callback<HumidityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HUMIDITY | Yes | Type of the sensor to unsubscribe from, which is **SENSOR_TYPE_ID_HUMIDITY**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

