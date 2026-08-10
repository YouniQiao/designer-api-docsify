# onMagneticFieldChange

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onMagneticFieldChange

```TypeScript
function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void
```

Subscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void--><!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MagneticFieldResponse&gt; | 是 | callback magnetic field data. |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

