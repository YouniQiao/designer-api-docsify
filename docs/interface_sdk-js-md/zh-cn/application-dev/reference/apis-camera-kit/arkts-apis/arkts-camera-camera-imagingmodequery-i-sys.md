# ImagingModeQuery（系统接口）

Imaging mode query object.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-camera-interface ImagingModeQuery--><!--Device-camera-interface ImagingModeQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## isImagingModeSupported

```TypeScript
isImagingModeSupported(mode: CameraImagingMode): boolean
```

Checks whether a camera imaging mode is supported.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImagingModeQuery-isImagingModeSupported(mode: CameraImagingMode): boolean--><!--Device-ImagingModeQuery-isImagingModeSupported(mode: CameraImagingMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) | 是 | Imaging mode. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Is the imaging mode supported. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config, only throw in session usage. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

