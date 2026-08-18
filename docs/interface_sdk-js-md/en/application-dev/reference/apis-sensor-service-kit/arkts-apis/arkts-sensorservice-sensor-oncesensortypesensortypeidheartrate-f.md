# once_SensorType.SENSOR_TYPE_ID_HEART_RATE

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorType.SENSOR_TYPE_ID_HEART_RATE

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>): void
```

Subscribes to only one data change of the heart rate sensor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** once(type: SensorId.HEART_RATE, callback: Callback&lt;HeartRateResponse&gt;)

**Required permissions:** ohos.permission.HEART_RATE

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HEART_RATE | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_HEART_RATE**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;HeartRateResponse&gt; | Yes | One-shot callback used to return the heart rate sensor data. The reported data type in the callback is **HeartRateResponse**. |

