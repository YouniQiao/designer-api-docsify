# PhotoSessionForSys (System API)

Implements a photo session for system applications, which sets the parameters of the normal photo mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md#camerainput) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md#cameraoutput) instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md#session).

**Inheritance/Implementation:** PhotoSessionForSys extends [PhotoSession](arkts-camera-camera-photosession-i.md#photosession), [Beauty](arkts-camera-camera-beauty-i-sys.md#beauty-system-api), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#coloreffect-system-api), [ColorManagement](arkts-camera-camera-colormanagement-i.md#colormanagement), [Macro](arkts-camera-camera-macro-i-sys.md#macro-system-api), [SceneDetection](arkts-camera-camera-scenedetection-i-sys.md#scenedetection-system-api), [EffectSuggestion](arkts-camera-camera-effectsuggestion-i-sys.md#effectsuggestion-system-api), [DepthFusion](arkts-camera-camera-depthfusion-i-sys.md#depthfusion-system-api), [ImagingMode](arkts-camera-camera-imagingmode-i-sys.md#imagingmode-system-api)

**Since:** 23

<!--Device-camera-interface PhotoSessionForSys--><!--Device-camera-interface PhotoSessionForSys-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

