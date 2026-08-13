# once_SensorType.SENSOR_TYPE_ID_BAROMETER

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_BAROMETER

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>): void
```

Subscribes to only one data change of the barometer sensor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.BAROMETER, callback: Callback&lt;BarometerResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_BAROMETER | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BarometerResponse&gt; | Yes |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_BAROMETER, (data: sensor.BarometerResponse) => {
  console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
});
```
