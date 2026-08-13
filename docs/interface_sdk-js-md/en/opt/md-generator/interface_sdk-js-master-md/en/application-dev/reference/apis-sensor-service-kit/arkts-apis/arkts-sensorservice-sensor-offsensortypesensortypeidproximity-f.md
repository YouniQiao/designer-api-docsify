# off_SensorType.SENSOR_TYPE_ID_PROXIMITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_PROXIMITY

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback?: Callback<ProximityResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.PROXIMITY, callback?: Callback&lt;ProximityResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback?: Callback<ProximityResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback?: Callback<ProximityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PROXIMITY | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProximityResponse&gt; | No |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.ProximityResponse) {
  console.info('Succeeded in invoking off. Distance: ' + data.distance);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PROXIMITY, callback);
```
