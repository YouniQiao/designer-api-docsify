# once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void
```

Subscribes to only one data change of the pedometer detection sensor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.PEDOMETER_DETECTION, callback: Callback&lt;PedometerDetectionResponse&gt;)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_PEDOMETER_DETECTION**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | Yes | One-shot callback used to return the pedometer detection sensor data. The reported data type in the callback is **PedometerDetectionResponse**. |

