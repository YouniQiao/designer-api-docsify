# once_SensorId.ACCELEROMETER_UNCALIBRATED

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorId.ACCELEROMETER_UNCALIBRATED

```TypeScript
function once(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void
```

Obtains data of the uncalibrated acceleration sensor once.

**Since:** 9

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-sensor-function once(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void--><!--Device-sensor-function once(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.ACCELEROMETER_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER_UNCALIBRATED**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AccelerometerUncalibratedResponse](arkts-sensorservice-sensor-accelerometeruncalibratedresponse-i.md)&gt; | Yes | Callback used to report the sensor data, which is an **AccelerometerUncalibratedResponse** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

