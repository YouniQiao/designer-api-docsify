# off_SensorId.MAGNETIC_FIELD

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## off_SensorId.MAGNETIC_FIELD

```TypeScript
function off(type: SensorId.MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void
```

Unsubscribes from data of the magnetic field sensor.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-sensor-function off(type: SensorId.MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function off(type: SensorId.MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.MAGNETIC_FIELD | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC_FIELD**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |


## off_SensorId.MAGNETIC_FIELD

```TypeScript
function off(type: SensorId.MAGNETIC_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void
```

Unsubscribes from data of the magnetic field sensor.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

<!--Device-sensor-function off(type: SensorId.MAGNETIC_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function off(type: SensorId.MAGNETIC_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.MAGNETIC_FIELD | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC_FIELD**. |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

