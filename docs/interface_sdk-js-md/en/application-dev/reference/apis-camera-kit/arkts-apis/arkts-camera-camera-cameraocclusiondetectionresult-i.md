# CameraOcclusionDetectionResult

镜头遮挡或脏污检测回调返回的接口实例，表示镜头遮挡或脏污状态信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface CameraOcclusionDetectionResult--><!--Device-camera-interface CameraOcclusionDetectionResult-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## isCameraLensDirty

```TypeScript
readonly isCameraLensDirty: boolean
```

镜头是否有脏污。true表示镜头有脏污，false表示镜头无脏污。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraOcclusionDetectionResult-readonly isCameraLensDirty: boolean--><!--Device-CameraOcclusionDetectionResult-readonly isCameraLensDirty: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isCameraOccluded

```TypeScript
readonly isCameraOccluded: boolean
```

镜头是否被遮挡。true表示镜头被遮挡，false表示镜头无遮挡。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraOcclusionDetectionResult-readonly isCameraOccluded: boolean--><!--Device-CameraOcclusionDetectionResult-readonly isCameraOccluded: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

