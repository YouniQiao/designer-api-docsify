# once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void
```

Subscribes to only one data change of the acceleration sensor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.ACCELEROMETER, callback: Callback&lt;AccelerometerResponse&gt;)

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_ACCELEROMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_ACCELEROMETER**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;AccelerometerResponse&gt; | Yes | One-shot callback used to return the acceleration sensor data. The reported data type in the callback is **AccelerometerResponse**. |

