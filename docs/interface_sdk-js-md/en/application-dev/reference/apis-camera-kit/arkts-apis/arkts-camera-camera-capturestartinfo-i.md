# CaptureStartInfo

Describes the capture start information.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface CaptureStartInfo--><!--Device-camera-interface CaptureStartInfo-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## captureId

```TypeScript
captureId: int
```

ID of this capture action.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CaptureStartInfo-captureId: int--><!--Device-CaptureStartInfo-captureId: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## time

```TypeScript
time: long
```

Estimated duration when the sensor captures frames at the bottom layer in a single capture. If **-1** is reported, there is no estimated duration.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CaptureStartInfo-time: long--><!--Device-CaptureStartInfo-time: long-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

