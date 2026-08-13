# AutoExposure

AutoExposure继承自[AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md#AutoExposureQuery)。 自动曝光类，对设备自动曝光（AE）操作。

**继承/实现关系：** AutoExposure extends [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md#AutoExposureQuery)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface AutoExposure--><!--Device-camera-interface AutoExposure-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getExposureMeteringMode

```TypeScript
getExposureMeteringMode(): ExposureMeteringMode
```

获取当前曝光测光模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-getExposureMeteringMode(): ExposureMeteringMode--><!--Device-AutoExposure-getExposureMeteringMode(): ExposureMeteringMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setExposureMeteringMode

```TypeScript
setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void
```

设置曝光测光模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void--><!--Device-AutoExposure-setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aeMeteringMode | [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
