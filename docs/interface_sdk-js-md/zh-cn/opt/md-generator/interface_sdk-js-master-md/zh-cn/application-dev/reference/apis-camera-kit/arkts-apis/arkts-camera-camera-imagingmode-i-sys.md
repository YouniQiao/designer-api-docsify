# ImagingMode（系统接口）

Implements imaging mode.

**继承/实现关系：** ImagingMode extends [ImagingModeQuery](arkts-camera-camera-imagingmodequery-i-sys.md#ImagingModeQuery)

**起始版本：** 26.0.0

<!--Device-camera-interface ImagingMode extends ImagingModeQuery--><!--Device-camera-interface ImagingMode extends ImagingModeQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getImagingMode

```TypeScript
getImagingMode(): CameraImagingMode
```

Gets current imaging mode.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImagingMode-getImagingMode(): CameraImagingMode--><!--Device-ImagingMode-getImagingMode(): CameraImagingMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## setImagingMode

```TypeScript
setImagingMode(mode: CameraImagingMode): void
```

Sets imaging mode.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImagingMode-setImagingMode(mode: CameraImagingMode): void--><!--Device-ImagingMode-setImagingMode(mode: CameraImagingMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
