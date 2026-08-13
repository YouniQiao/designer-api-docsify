# once_SensorId.PEDOMETER_DETECTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorId.PEDOMETER_DETECTION

```TypeScript
function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void
```

Obtains data of the pedometer sensor once.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.PEDOMETER_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER_DETECTION**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | Yes | Callback used to report the sensor data, which is a **PedometerDetectionResponse** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

