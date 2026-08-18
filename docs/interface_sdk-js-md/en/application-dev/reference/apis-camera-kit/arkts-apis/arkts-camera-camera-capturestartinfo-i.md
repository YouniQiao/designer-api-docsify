# CaptureStartInfo

Describes the capture start information.

**Since:** 23

<!--Device-camera-interface CaptureStartInfo--><!--Device-camera-interface CaptureStartInfo-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## captureId

```TypeScript
captureId: int
```

ID of this capture action.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CaptureStartInfo-captureId: int--><!--Device-CaptureStartInfo-captureId: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## time

```TypeScript
time: long
```

Estimated duration when the sensor captures frames at the bottom layer in a single capture. If **-1** is reported, there is no estimated duration.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CaptureStartInfo-time: long--><!--Device-CaptureStartInfo-time: long-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

