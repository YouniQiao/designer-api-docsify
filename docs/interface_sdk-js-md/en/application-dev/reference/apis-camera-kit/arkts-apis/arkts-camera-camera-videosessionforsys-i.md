# VideoSessionForSys (System API)

Implements a video session for system applications, which sets the parameters of the normal video mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md).

@extends VideoSession, Beauty, ColorEffect, ColorManagement, Macro [since 11 - 14] @extends VideoSession, Beauty, ColorEffect, ColorManagement, Macro, Aperture, ColorReservation [since 15 - 17] @extends VideoSession, Beauty, ColorEffect, ColorManagement, Macro, Aperture, ColorReservation, EffectSuggestion [since 18] @extends VideoSession, Beauty, ColorEffect, ColorManagement, Macro, Aperture, ColorReservation, EffectSuggestion, ImagingMode [since 26.0.0]

**Inheritance/Implementation:** VideoSessionForSys extends [VideoSession](arkts-camera-camera-videosession-i.md), [Beauty](arkts-camera-camera-beauty-i-sys.md), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md), [Macro](arkts-camera-camera-macro-i-sys.md), [Aperture](arkts-camera-camera-aperture-i-sys.md), [ColorReservation](arkts-camera-camera-colorreservation-i-sys.md), [EffectSuggestion](arkts-camera-camera-effectsuggestion-i-sys.md), [ImagingMode](arkts-camera-camera-imagingmode-i-sys.md)

**Since:** 23

<!--Device-camera-interface VideoSessionForSys--><!--Device-camera-interface VideoSessionForSys-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

