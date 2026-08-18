# onBarometerChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onBarometerChange

```TypeScript
function onBarometerChange(callback: Callback<BarometerResponse>, options?: Options): void
```

Subscribe to barometer sensor data, {@code SensorId.BAROMETER}.

**Since:** 23

<!--Device-sensor-function onBarometerChange(callback: Callback<BarometerResponse>, options?: Options): void--><!--Device-sensor-function onBarometerChange(callback: Callback<BarometerResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BarometerResponse&gt; | Yes | callback barometer data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |

