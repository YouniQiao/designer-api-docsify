# getCameraManager

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getCameraManager

```TypeScript
function getCameraManager(context: Context): CameraManager
```

获取相机管理器实例，同步返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-camera-function getCameraManager(context: Context): CameraManager--><!--Device-camera-function getCameraManager(context: Context): CameraManager-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraManager](arkts-camera-camera-cameramanager-i.md) | 相机管理器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraManager(context: common.BaseContext): camera.CameraManager | undefined {
  let cameraManager: camera.CameraManager | undefined = undefined;
  try {
    cameraManager = camera.getCameraManager(context);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getCameraManager call failed. error code: ${err.code}`);
  }
  return cameraManager;
}
```

