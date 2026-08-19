# on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION

```TypeScript
function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>,
    options?: Options): void
```

Subscribes to data changes of the linear acceleration sensor. If this API is called multiple times for the same application, the last call takes effect.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)(type: SensorId.LINEAR_ACCELEROMETER, callback: Callback&lt;LinearAccelerometerResponse&gt;, options?: Options)

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION | Yes | Type of the sensor to subscribe to, which is **SENSOR_TYPE_ID_LINEAR_ACCELERATION**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | Yes | Callback used to return the linear acceleration sensor data. The reported data type in the callback is **LinearAccelerometerResponse**. |
| options | Options | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

