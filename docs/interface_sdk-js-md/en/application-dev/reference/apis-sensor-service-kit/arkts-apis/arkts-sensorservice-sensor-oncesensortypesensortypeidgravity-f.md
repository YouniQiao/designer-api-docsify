# once_SensorType.SENSOR_TYPE_ID_GRAVITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_GRAVITY

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback: Callback<GravityResponse>): void
```

Subscribes to only one data change of the gravity sensor.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.GRAVITY, callback: Callback&lt;GravityResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback: Callback<GravityResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback: Callback<GravityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_GRAVITY | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_GRAVITY**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md)&gt; | Yes | One-shot callback used to return the gravity sensor data. The reported data type in the callback is **GravityResponse**. |

