# once_SensorType.SENSOR_TYPE_ID_PROXIMITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_PROXIMITY

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback: Callback<ProximityResponse>): void
```

Subscribes to only one data change of the proximity sensor.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.PROXIMITY, callback: Callback&lt;ProximityResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback: Callback<ProximityResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback: Callback<ProximityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PROXIMITY | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_PROXIMITY**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProximityResponse&gt; | Yes | One-shot callback used to return the proximity sensor data. The reported data type in the callback is **ProximityResponse**. |

