# off_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## off_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.LINEAR_ACCELEROMETER, callback?: Callback&lt;LinearAccelerometerResponse&gt;)

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR_TYPE_ID_LINEAR_ACCELERATION**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

