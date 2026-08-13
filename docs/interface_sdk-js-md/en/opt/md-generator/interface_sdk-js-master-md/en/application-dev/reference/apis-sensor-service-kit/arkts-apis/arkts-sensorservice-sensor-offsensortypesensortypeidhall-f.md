# off_SensorType.SENSOR_TYPE_ID_HALL

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_HALL

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_HALL, callback?: Callback<HallResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.HALL, callback?: Callback&lt;HallResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HALL, callback?: Callback<HallResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HALL, callback?: Callback<HallResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HALL | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HallResponse](arkts-sensorservice-sensor-hallresponse-i.md)&gt; | No |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HallResponse) {
  console.info('Succeeded in invoking off. Status: ' + data.status);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HALL, callback);
```
