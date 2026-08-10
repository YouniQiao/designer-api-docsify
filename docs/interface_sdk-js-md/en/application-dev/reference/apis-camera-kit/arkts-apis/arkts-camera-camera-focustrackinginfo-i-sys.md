# FocusTrackingInfo (System API)

Describes the focus tracking information, which is obtained by calling VideoSessionForSys.  
[on('focusTrackingInfoAvailable')](camera.VideoSession.on(type: 'focusTrackingInfoAvailable', callback: Callback&lt;FocusTrackingInfo&gt;)).

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-camera-interface FocusTrackingInfo--><!--Device-camera-interface FocusTrackingInfo-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## trackingMode

```TypeScript
trackingMode: FocusTrackingMode
```

Tracing mode.

**Type:** [FocusTrackingMode](arkts-camera-camera-focustrackingmode-e-sys.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-FocusTrackingInfo-trackingMode: FocusTrackingMode--><!--Device-FocusTrackingInfo-trackingMode: FocusTrackingMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## trackingRegion

```TypeScript
trackingRegion: Rect
```

Tracking region.

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-FocusTrackingInfo-trackingRegion: Rect--><!--Device-FocusTrackingInfo-trackingRegion: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

