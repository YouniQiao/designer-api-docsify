# DepthProfile (System API)

Describes the profile of depth data. It inherits from [Profile](arkts-camera-camera-profile-i.md#Profile).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface DepthProfile--><!--Device-camera-interface DepthProfile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## dataAccuracy

```TypeScript
readonly dataAccuracy: DepthDataAccuracy
```

Accuracy of the depth data, which can be either relative accuracy or absolute accuracy.

**Type:** [DepthDataAccuracy](arkts-camera-camera-depthdataaccuracy-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DepthProfile-readonly dataAccuracy: DepthDataAccuracy--><!--Device-DepthProfile-readonly dataAccuracy: DepthDataAccuracy-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## format

```TypeScript
readonly format: CameraFormat
```

Camera output format.

**Type:** [CameraFormat](arkts-camera-camera-cameraformat-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DepthProfile-readonly format: CameraFormat--><!--Device-DepthProfile-readonly format: CameraFormat-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## size

```TypeScript
readonly size: Size
```

Depth data resolution.

**Type:** Size

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DepthProfile-readonly size: Size--><!--Device-DepthProfile-readonly size: Size-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

