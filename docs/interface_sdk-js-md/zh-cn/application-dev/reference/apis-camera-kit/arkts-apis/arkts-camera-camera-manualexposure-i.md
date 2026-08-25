# ManualExposure

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md) Provides APIs to obtain and set the exposure duration.

**继承/实现关系：** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)

**起始版本：** 24

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getExposureDuration

```TypeScript
getExposureDuration(): number
```

Gets current exposure value.

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setExposureDuration

```TypeScript
setExposureDuration(exposureDuration: number): void
```

Sets Exposure duration value, units: microseconds.This control is only effective if ExposureMode is set to EXPOSURE_MODE_MANUAL.

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exposureDuration | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
