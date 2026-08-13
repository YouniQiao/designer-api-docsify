# off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.MAGNETIC_FIELD, callback?: Callback&lt;MagneticFieldResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD | Yes | Type of the sensor to unsubscribe from, which is **SENSOR_TYPE_ID_MAGNETIC_FIELD**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

