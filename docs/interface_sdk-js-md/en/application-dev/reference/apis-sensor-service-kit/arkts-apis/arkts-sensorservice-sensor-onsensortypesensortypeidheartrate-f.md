# on_SensorType.SENSOR_TYPE_ID_HEART_RATE

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorType.SENSOR_TYPE_ID_HEART_RATE

```TypeScript
function on(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>,
    options?: Options): void
```

Subscribes to data changes of the heart rate sensor. If this API is called multiple times for the same application, the last call takes effect.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)(type: SensorId.HEART_RATE, callback: Callback&lt;HeartRateResponse&gt;, options?: Options)

**Required permissions:** ohos.permission.HEALTH_DATA

<!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HEART_RATE | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_HEART_RATE**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | Yes | Callback used to return the heart rate sensor data. The reported data type in the callback is **HeartRateResponse**. |
| options | Options | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

