# off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void
```

Unsubscribes from sensor data changes.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.PEDOMETER_DETECTION, callback?: Callback&lt;PedometerDetectionResponse&gt;)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR_TYPE_ID_PEDOMETER_DETECTION**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

