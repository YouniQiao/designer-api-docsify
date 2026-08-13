# ManualExposure（系统接口）

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md#ManualExposureQuery（系统接口）) Provides APIs to obtain and set the exposure duration.

**继承/实现关系：** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md#ManualExposureQuery（系统接口）)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface ManualExposure--><!--Device-camera-interface ManualExposure-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getExposureDuration

```TypeScript
getExposureDuration(): number
```

Gets current exposure value.

**起始版本：** 24

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ManualExposure-getExposureDuration(): int--><!--Device-ManualExposure-getExposureDuration(): int-End-->

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

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ManualExposure-setExposureDuration(exposureDuration: int): void--><!--Device-ManualExposure-setExposureDuration(exposureDuration: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exposureDuration | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
