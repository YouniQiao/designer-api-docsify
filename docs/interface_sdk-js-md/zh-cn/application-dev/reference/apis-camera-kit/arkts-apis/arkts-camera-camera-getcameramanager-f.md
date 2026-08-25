# getCameraManager

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getCameraManager

```TypeScript
function getCameraManager(context: Context): CameraManager
```

获取相机管理器实例，同步返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraManager](arkts-camera-camera-cameramanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
