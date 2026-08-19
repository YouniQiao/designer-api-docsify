# once_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void
```

Subscribes to only one data change of the wear detection sensor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.WEAR_DETECTION, callback: Callback&lt;WearDetectionResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_WEAR_DETECTION | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_WEAR_DETECTION**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | Yes | One-shot callback used to return the wear detection sensor data. The reported data type in the callback is **WearDetectionResponse**. |

