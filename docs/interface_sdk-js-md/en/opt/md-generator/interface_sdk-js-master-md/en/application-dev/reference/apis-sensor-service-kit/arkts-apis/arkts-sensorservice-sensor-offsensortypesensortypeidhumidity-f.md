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

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.HUMIDITY, callback?: Callback&lt;HumidityResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback?: Callback<HumidityResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback?: Callback<HumidityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HUMIDITY | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | No |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HumidityResponse) {
  console.info('Succeeded in invoking off. Humidity: ' + data.humidity);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HUMIDITY, callback);
```
