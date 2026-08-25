# ManualExposure

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md) Provides APIs to obtain and set the exposure duration.

**继承/实现关系：** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)

**起始版本：** 24

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getExposure

```TypeScript
getExposure(): number
```

Obtains the manual exposure duration in use.

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400101](../errorcode-camera.md#7400101-无效入参) |

## setExposure

```TypeScript
setExposure(exposure: number): void
```

Sets the manual exposure duration. Before using this API, call [getSupportedExposureRange](arkts-camera-camera-manualexposurequery-i-sys.md#getsupportedexposurerange) to obtain the supported manual exposure durations, in ms.

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [exposure](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenepostprocesssettings-tonemappingsettings-i.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
