# off_SensorType.SENSOR_TYPE_ID_GYROSCOPE

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_GYROSCOPE

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.GYROSCOPE, callback?: Callback&lt;GyroscopeResponse&gt;)

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_GYROSCOPE | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GyroscopeResponse&gt; | No |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GyroscopeResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback);
```
