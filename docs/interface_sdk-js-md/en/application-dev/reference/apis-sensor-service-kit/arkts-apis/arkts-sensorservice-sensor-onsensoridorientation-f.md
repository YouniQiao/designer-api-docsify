# on_SensorId.ORIENTATION

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorId.ORIENTATION

```TypeScript
function on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>,
    options?: Options): void
```

Subscribes to data of the orientation sensor. &gt; **NOTE：**&gt; &gt; Applications or services invoking this API can prompt users to use figure-8 calibration to improve the accuracy &gt; of the direction sensor. The sensor has a theoretical error of ±5 degrees, but the specific precision may vary &gt; depending on different driver implementations and algorithmic designs.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sensor-function on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.ORIENTATION | Yes | Sensor type. The value is fixed at **SensorId.ORIENTATION**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md)&gt; | Yes | Callback used to report the sensor data, which is a **OrientationResponse** object. |
| options | Options | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

