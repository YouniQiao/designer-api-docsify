# off_SensorId.ACCELEROMETER

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## off_SensorId.ACCELEROMETER

```TypeScript
function off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void
```

Unsubscribes from data of the acceleration sensor.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCELEROMETER

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sensor-function off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void--><!--Device-sensor-function off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |


## off_SensorId.ACCELEROMETER

```TypeScript
function off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void
```

Unsubscribes from data of the acceleration sensor.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCELEROMETER

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-sensor-function off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void--><!--Device-sensor-function off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER**. |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

