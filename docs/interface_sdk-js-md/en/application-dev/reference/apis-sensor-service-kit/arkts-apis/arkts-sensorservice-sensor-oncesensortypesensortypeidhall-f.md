# once_SensorType.SENSOR_TYPE_ID_HALL

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## once_SensorType.SENSOR_TYPE_ID_HALL

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_HALL, callback: Callback<HallResponse>): void
```

Subscribes to only one data change of the Hall effect sensor.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.HALL, callback: Callback&lt;HallResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_HALL, callback: Callback<HallResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_HALL, callback: Callback<HallResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HALL | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_HALL**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HallResponse](arkts-sensorservice-sensor-hallresponse-i.md)&gt; | Yes | One-shot callback used to return the Hall effect sensor data. The reported data type in the callback is **HallResponse**. |

