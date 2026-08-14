# once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void
```

Subscribes to only one data change of the magnetic field sensor.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.MAGNETIC_FIELD, callback: Callback&lt;MagneticFieldResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_MAGNETIC_FIELD**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | Yes | One-shot callback used to return the magnetic field sensor data. The reported data type in the callback is **MagneticFieldResponse**. |

