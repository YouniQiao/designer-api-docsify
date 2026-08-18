# off_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback?: Callback<WearDetectionResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_sensoridcolor)(type: SensorId.WEAR_DETECTION, callback?: Callback&lt;WearDetectionResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback?: Callback<WearDetectionResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback?: Callback<WearDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_WEAR_DETECTION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR_TYPE_ID_WEAR_DETECTION**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

