# onPedometerDetectionChange

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onPedometerDetectionChange

```TypeScript
function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void
```

Subscribe to pedometer detection sensor data, {@code SensorId.PEDOMETER_DETECTION}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void--><!--Device-sensor-function onPedometerDetectionChange(callback: Callback<PedometerDetectionResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PedometerDetectionResponse&gt; | 是 | callback pedometer detection data. |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |
| 201 | Permission denied. |

