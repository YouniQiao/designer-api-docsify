# SceneDetection（系统接口）

Provides the scene detection capability. It inherits from [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md).

**继承/实现关系：** SceneDetection extends [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md)

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## enableSceneFeature

```TypeScript
enableSceneFeature(type: SceneFeatureType, enabled: boolean): void
```

Enables or disables a scene feature. This API must be called after [SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) of the corresponding scene feature is received.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | 是 |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
