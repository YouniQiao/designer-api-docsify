# VideoSessionForSys (System API)

Implements a video session for system applications, which sets the parameters of the normal video mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md#Session).

**Inheritance/Implementation:** VideoSessionForSys extends [VideoSession](arkts-camera-camera-videosession-i.md#VideoSession), [Beauty](arkts-camera-camera-beauty-i-sys.md#Beauty), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#ColorEffect), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [Macro](arkts-camera-camera-macro-i.md#Macro), [Aperture](arkts-camera-camera-aperture-i.md#Aperture), [ColorReservation](arkts-camera-camera-colorreservation-i-sys.md#ColorReservation), [EffectSuggestion](arkts-camera-camera-effectsuggestion-i-sys.md#EffectSuggestion), [ImagingMode](arkts-camera-camera-imagingmode-i-sys.md#ImagingMode)

**Since:** 11

<!--Device-camera-interface VideoSessionForSys extends VideoSession, Beauty, ColorEffect, ColorManagement, Macro, Aperture, ColorReservation, EffectSuggestion, ImagingMode--><!--Device-camera-interface VideoSessionForSys extends VideoSession, Beauty, ColorEffect, ColorManagement, Macro, Aperture, ColorReservation, EffectSuggestion, ImagingMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```
