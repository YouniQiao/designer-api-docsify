# CaptureStartInfo

拍照开始信息。

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

拍照的ID。

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

预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CaptureStartInfo-time: long--><!--Device-CaptureStartInfo-time: long-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

