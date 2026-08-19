# on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER

```TypeScript
function on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>,
    options?: Options): void
```

Subscribes to data changes of the acceleration sensor. If this API is called multiple times for the same application, the last call takes effect.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)(type: SensorId.ACCELEROMETER, callback: Callback&lt;AccelerometerResponse&gt;, options?: Options)

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_ACCELEROMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_ACCELEROMETER**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | Yes | Callback used to return the acceleration sensor data. The reported data type in the callback is **AccelerometerResponse**. |
| options | Options | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

