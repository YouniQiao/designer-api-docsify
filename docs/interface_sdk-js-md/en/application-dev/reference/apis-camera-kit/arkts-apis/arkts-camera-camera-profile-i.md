# Profile

Describes the camera profile.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface Profile--><!--Device-camera-interface Profile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## format

```TypeScript
readonly format: CameraFormat
```

Output format.

**Type:** [CameraFormat](arkts-camera-camera-cameraformat-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Profile-readonly format: CameraFormat--><!--Device-Profile-readonly format: CameraFormat-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## size

```TypeScript
readonly size: Size
```

Resolution.

The size setting corresponds to the camera's resolution width and height, rather than the actual dimensions of the output image.

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Profile-readonly size: Size--><!--Device-Profile-readonly size: Size-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

