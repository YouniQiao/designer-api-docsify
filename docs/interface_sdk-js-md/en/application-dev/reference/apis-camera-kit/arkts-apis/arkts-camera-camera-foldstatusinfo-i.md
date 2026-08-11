# FoldStatusInfo

Describes the fold state information about a foldable device.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface FoldStatusInfo--><!--Device-camera-interface FoldStatusInfo-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## foldStatus

```TypeScript
readonly foldStatus: FoldStatus
```

Fold state.

**Type:** [FoldStatus](../../apis-arkui/arkts-apis/arkts-arkui-enums-foldstatus-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FoldStatusInfo-readonly foldStatus: FoldStatus--><!--Device-FoldStatusInfo-readonly foldStatus: FoldStatus-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## supportedCameras

```TypeScript
readonly supportedCameras: Array<CameraDevice>
```

List of cameras supported in the current fold state.

**Type:** Array&lt;CameraDevice&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FoldStatusInfo-readonly supportedCameras: Array<CameraDevice>--><!--Device-FoldStatusInfo-readonly supportedCameras: Array<CameraDevice>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

