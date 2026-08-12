# PhotoSessionForSys (System API)

Implements a photo session for system applications, which sets the parameters of the normal photo mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md#Session).

**Inheritance/Implementation:** PhotoSessionForSys extends [PhotoSession](arkts-camera-camera-photosession-i.md#PhotoSession), [Beauty](arkts-camera-camera-beauty-i-sys.md#Beauty), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#ColorEffect), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [Macro](arkts-camera-camera-macro-i.md#Macro), [SceneDetection](arkts-camera-camera-scenedetection-i-sys.md#SceneDetection), [EffectSuggestion](arkts-camera-camera-effectsuggestion-i-sys.md#EffectSuggestion), [DepthFusion](arkts-camera-camera-depthfusion-i-sys.md#DepthFusion), [ImagingMode](arkts-camera-camera-imagingmode-i-sys.md#ImagingMode)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface PhotoSessionForSys extends PhotoSession, Beauty, ColorEffect, ColorManagement, Macro, SceneDetection, EffectSuggestion, DepthFusion, ImagingMode--><!--Device-camera-interface PhotoSessionForSys extends PhotoSession, Beauty, ColorEffect, ColorManagement, Macro, SceneDetection, EffectSuggestion, DepthFusion, ImagingMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

