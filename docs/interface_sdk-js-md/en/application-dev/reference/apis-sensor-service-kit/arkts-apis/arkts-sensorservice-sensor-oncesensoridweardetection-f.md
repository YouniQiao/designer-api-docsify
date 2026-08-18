# once_SensorId.WEAR_DETECTION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorId.WEAR_DETECTION

```TypeScript
function once(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void
```

Obtains data of the wear detection sensor once.

**Since:** 9

<!--Device-sensor-function once(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void--><!--Device-sensor-function once(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.WEAR_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.WEAR_DETECTION**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | Yes | Callback used to report the sensor data, which is a **WearDetectionResponse** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

