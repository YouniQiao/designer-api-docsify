# SceneDetection (System API)

Provides the scene detection capability. It inherits from [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md#SceneDetectionQuery-(System-API)).

**Inheritance/Implementation:** SceneDetection extends [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md#SceneDetectionQuery-(System-API))

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface SceneDetection--><!--Device-camera-interface SceneDetection-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## enableSceneFeature

```TypeScript
enableSceneFeature(type: SceneFeatureType, enabled: boolean): void
```

Enables or disables a scene feature. This API must be called after [SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md#SceneFeatureDetectionResult-(System-API)) of the corresponding scene feature is received.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneDetection-enableSceneFeature(type: SceneFeatureType, enabled: boolean): void--><!--Device-SceneDetection-enableSceneFeature(type: SceneFeatureType, enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | Yes | Scene feature. |
| enabled | boolean | Yes | Whether to enable the scene feature. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableSceneFeature(photoSession: camera.PhotoSessionForSys, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput): void {
  photoSession.beginConfig();
  photoSession.addInput(cameraInput);
  photoSession.addOutput(previewOutput);
  photoSession.commitConfig();

  photoSession.on('featureDetection', camera.SceneFeatureType.MOON_CAPTURE_BOOST,
    (err: BusinessError, statusObject: camera.SceneFeatureDetectionResult) => {
      if (err !== undefined && err.code !== 0) {
        console.error(`Callback Error, errorCode: ${err.code}`);
        return;
      }
      console.info(
        `on featureDetectionStatus featureType:${statusObject.featureType} detected:${statusObject.detected}`);
      if (statusObject.featureType === camera.SceneFeatureType.MOON_CAPTURE_BOOST) {
        try {
          photoSession.enableSceneFeature(statusObject.featureType, statusObject.detected);
        } catch (error) {
          let err = error as BusinessError;
          console.error(`The enableSceneFeature call failed. error code: ${err.code}`);
        }
      }
    });
}
```

