# DepthFusion（系统接口）

Depth fusion class. It inherits from [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md).

**继承/实现关系：** DepthFusion extends [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md)

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## enableDepthFusion

```TypeScript
enableDepthFusion(enabled: boolean): void
```

Enables depth fusion.

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## isDepthFusionEnabled

```TypeScript
isDepthFusionEnabled(): boolean
```

Checks whether depth fusion is enabled.

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
