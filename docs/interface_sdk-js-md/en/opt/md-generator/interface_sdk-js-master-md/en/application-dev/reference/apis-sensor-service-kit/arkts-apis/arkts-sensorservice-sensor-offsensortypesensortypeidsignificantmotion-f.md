# off_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback?: Callback<SignificantMotionResponse>): void
```

Unsubscribes from valid motion sensor data.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.SIGNIFICANT_MOTION, callback?: Callback&lt;SignificantMotionResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback?: Callback<SignificantMotionResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback?: Callback<SignificantMotionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SignificantMotionResponse](arkts-sensorservice-sensor-significantmotionresponse-i.md)&gt; | No |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.SignificantMotionResponse) {
  console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback);
```
